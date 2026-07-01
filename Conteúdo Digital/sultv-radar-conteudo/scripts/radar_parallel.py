#!/usr/bin/env python3
"""
radar_parallel.py — wrapper paralelo do radar_main.py.

Mantém EXATAMENTE a mesma lógica e estado (state/ultimo_run.json,
logs/YYYY-MM-DD.json, mesmos guardrails, quotas, boost geográfico),
mas roda as chamadas Haiku/Sonnet em ThreadPoolExecutor para caber em
janelas curtas de execução.

Steps idempotentes (mesmas chaves do radar_main.py):
  --step coleta      coleta + dedup + curadoria Haiku paralela
  --step angulacao   Sonnet top 20 em paralelo
  --step persistir   guardrail final em paralelo + grava Sheets
  --step produzir    igual ao original
  --step verify      igual ao original
"""
from __future__ import annotations
import argparse
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, fields
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))


def _load_env_file():
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "'"):
            v = v[1:-1]
        if k and k not in os.environ:
            os.environ[k] = v


_load_env_file()

from coletor import coletar_todas_fontes
from dedup import dedup_pipeline_completo
from curador import (
    curar_haiku, angular_sonnet, guardrail_final,
    score_combinado, MateriaBruta, MateriaCurada, MateriaPronta,
    QUOTA_DIARIA_PUBLICACAO, TOP_N_ANGULACAO, TOP_N_PERSISTIDO,
)
from geografia import (
    aplicar_boost_geografico, aplicar_quota_diversidade,
    relatorio_distribuicao, QUOTA_POR_CIDADE,
)
from sheets_writer import write_radar_diario, write_historico, ler_hashes_recentes
from produzir_short import produzir_short
from produzir_materia import produzir_materia
from publicar_post import publicar_post
from enviar_relatorio import enviar_relatorio_diario
from guardrails import passa_stop_list

import anthropic

LOG_DIR = ROOT / "logs"
STATE_FILE = ROOT / "state" / "ultimo_run.json"
LOG_DIR.mkdir(exist_ok=True)
STATE_FILE.parent.mkdir(exist_ok=True)

WORKERS = int(os.environ.get("RADAR_WORKERS", "12"))


def _log(stage: str, payload: dict):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    f = LOG_DIR / f"{today}.json"
    line = json.dumps(
        {"ts": datetime.now(timezone.utc).isoformat(), "stage": stage, **payload},
        ensure_ascii=False,
    )
    with open(f, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def _save_state(key: str, data):
    state = {}
    if STATE_FILE.exists():
        state = json.loads(STATE_FILE.read_text())
    state[key] = data
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, default=str, indent=2))


def _load_state(key: str, default=None):
    if not STATE_FILE.exists():
        return default
    return json.loads(STATE_FILE.read_text()).get(key, default)


# ============================================================
# Step coleta — paralelo
# ============================================================

def step_coleta_so():
    """Coleta + dedup apenas — salva 'candidatos' no state, sem Haiku."""
    print(f"[radar-par] Coletando das fontes...", flush=True)
    brutos = coletar_todas_fontes()
    _log("coleta", {"total_brutos": len(brutos)})
    print(f"[radar-par] {len(brutos)} brutos", flush=True)
    print("[radar-par] Aplicando dedup (3 camadas)...", flush=True)
    try:
        hashes_recentes = ler_hashes_recentes(horas=48)
    except Exception as e:
        print(f"[radar-par] AVISO: Sheets indisponível ({e.__class__.__name__}). Hashes locais.", flush=True)
        prev = (_load_state("aprovadas", []) or []) + (_load_state("persistidas", []) or [])
        hashes_recentes = {d.get("id_hash") for d in prev if d.get("id_hash")}
    dedupados = dedup_pipeline_completo(brutos, hashes_recentes)
    _log("dedup", {"antes": len(brutos), "depois": len(dedupados)})
    candidatos = [it for it in dedupados if passa_stop_list(it.titulo + " " + it.resumo)]
    print(f"[radar-par] {len(candidatos)} candidatos passam stop_list", flush=True)
    _save_state("candidatos", [it.__dict__ for it in candidatos])
    return candidatos


def step_haiku():
    """Lê candidatos do state e roda Haiku em paralelo, com checkpoint incremental e deadline."""
    import time as _time
    cand_dict = _load_state("candidatos", [])
    if not cand_dict:
        print("[radar-par] Sem candidatos. Rode --step coleta-so antes.")
        return []
    candidatos = [MateriaBruta(**{k: v for k, v in d.items() if k in {f.name for f in fields(MateriaBruta)}})
                  for d in cand_dict]

    # Carrega itens já curados (checkpoint resumível)
    curadas_dict = _load_state("curadas_partial", []) or []
    ja_curadas_hashes = {d.get("id_hash") for d in curadas_dict}
    pendentes = [it for it in candidatos if it.id_hash not in ja_curadas_hashes]
    print(f"[radar-par] Haiku: {len(curadas_dict)} já curadas, {len(pendentes)} pendentes (workers={WORKERS})...", flush=True)

    client = anthropic.Anthropic()
    deadline = _time.time() + int(os.environ.get("HAIKU_DEADLINE", "30"))

    def _curar(it):
        try:
            c = curar_haiku(client, it)
        except Exception:
            return None
        if not c:
            return None
        m = MateriaCurada(
            **asdict(it),
            score_editorial=int(c.get("score_editorial", 0)),
            tag_principal=c.get("tag_principal", "outro"),
            tags_secundarias=c.get("tags_secundarias", []),
            formato_sugerido=c.get("formato_sugerido", "descartar"),
            justificativa=c.get("justificativa", ""),
            alerta_guardrail=bool(c.get("alerta_guardrail", False)),
            guardrail_motivo=c.get("guardrail_motivo", ""),
        )
        m.score_combinado = score_combinado(m.score_fonte, m.score_editorial)
        return m

    novas = []
    if pendentes:
        with ThreadPoolExecutor(max_workers=WORKERS) as ex:
            futures = {ex.submit(_curar, it): it for it in pendentes}
            completed = 0
            for fu in as_completed(futures):
                if _time.time() > deadline:
                    for f in futures: f.cancel()
                    break
                m = fu.result()
                if m is not None:
                    novas.append(m)
                completed += 1
                if completed % 30 == 0:
                    # checkpoint incremental
                    _save_state("curadas_partial", curadas_dict + [n.__dict__ for n in novas])

    curadas_dict_final = curadas_dict + [n.__dict__ for n in novas]
    _save_state("curadas_partial", curadas_dict_final)
    # se ainda tem pendentes, sai sem finalizar — próxima chamada continua
    pendentes_apos = [it for it in candidatos if it.id_hash not in {d.get("id_hash") for d in curadas_dict_final}]
    if pendentes_apos:
        print(f"[radar-par] Haiku parcial: {len(curadas_dict_final)} curadas, {len(pendentes_apos)} restantes. Rode --step haiku de novo para continuar.", flush=True)
        return []

    # Reconstrói lista MateriaCurada
    curadas = [MateriaCurada(**{k: v for k, v in d.items() if k in {f.name for f in fields(MateriaCurada)}})
               for d in curadas_dict_final]

    aprovadas = [m for m in curadas if not m.alerta_guardrail and m.formato_sugerido != "descartar"]
    aprovadas.sort(key=lambda m: m.score_combinado, reverse=True)
    aprovadas = aplicar_boost_geografico(aprovadas)
    distribuicao_antes = relatorio_distribuicao(aprovadas)
    aprovadas = aplicar_quota_diversidade(aprovadas, max_por_cidade=QUOTA_POR_CIDADE)
    distribuicao_depois = relatorio_distribuicao(aprovadas)

    _log("curadoria_haiku", {
        "curadas": len(curadas),
        "aprovadas_pos_boost_e_quota": len(aprovadas),
        "bloqueadas_guardrail": sum(1 for m in curadas if m.alerta_guardrail),
        "descartadas": sum(1 for m in curadas if m.formato_sugerido == "descartar"),
        "distribuicao_antes_quota": distribuicao_antes,
        "distribuicao_depois_quota": distribuicao_depois,
    })
    print(f"[radar-par] {len(aprovadas)} aprovadas (cidades: {distribuicao_depois})", flush=True)
    _save_state("aprovadas", [m.__dict__ for m in aprovadas])
    return aprovadas


def step_coleta():
    print(f"[radar-par] Coletando das fontes... (workers={WORKERS})", flush=True)
    brutos = coletar_todas_fontes()
    _log("coleta", {"total_brutos": len(brutos)})
    print(f"[radar-par] {len(brutos)} brutos", flush=True)

    print("[radar-par] Aplicando dedup (3 camadas)...", flush=True)
    try:
        hashes_recentes = ler_hashes_recentes(horas=48)
    except Exception as e:
        print(f"[radar-par] AVISO: Sheets indisponível para dedup ({e.__class__.__name__}). "
              f"Usando hashes locais do state.", flush=True)
        prev = _load_state("aprovadas", []) or []
        prev2 = _load_state("persistidas", []) or []
        hashes_recentes = set()
        for d in prev + prev2:
            h = d.get("id_hash")
            if h:
                hashes_recentes.add(h)
    dedupados = dedup_pipeline_completo(brutos, hashes_recentes)
    _log("dedup", {"antes": len(brutos), "depois": len(dedupados)})
    print(f"[radar-par] {len(dedupados)} após dedup", flush=True)

    candidatos = [it for it in dedupados if passa_stop_list(it.titulo + " " + it.resumo)]
    print(f"[radar-par] {len(candidatos)} passam stop_list — curadoria Haiku paralela...", flush=True)

    client = anthropic.Anthropic()

    def _curar(it: MateriaBruta):
        try:
            c = curar_haiku(client, it)
        except Exception as e:
            return None
        if not c:
            return None
        m = MateriaCurada(
            **asdict(it),
            score_editorial=int(c.get("score_editorial", 0)),
            tag_principal=c.get("tag_principal", "outro"),
            tags_secundarias=c.get("tags_secundarias", []),
            formato_sugerido=c.get("formato_sugerido", "descartar"),
            justificativa=c.get("justificativa", ""),
            alerta_guardrail=bool(c.get("alerta_guardrail", False)),
            guardrail_motivo=c.get("guardrail_motivo", ""),
        )
        m.score_combinado = score_combinado(m.score_fonte, m.score_editorial)
        return m

    curadas: list[MateriaCurada] = []
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = [ex.submit(_curar, it) for it in candidatos]
        for fu in as_completed(futures):
            m = fu.result()
            if m is not None:
                curadas.append(m)

    aprovadas = [m for m in curadas if not m.alerta_guardrail and m.formato_sugerido != "descartar"]
    aprovadas.sort(key=lambda m: m.score_combinado, reverse=True)

    aprovadas = aplicar_boost_geografico(aprovadas)
    distribuicao_antes = relatorio_distribuicao(aprovadas)
    aprovadas = aplicar_quota_diversidade(aprovadas, max_por_cidade=QUOTA_POR_CIDADE)
    distribuicao_depois = relatorio_distribuicao(aprovadas)

    _log("curadoria_haiku", {
        "curadas": len(curadas),
        "aprovadas_pos_boost_e_quota": len(aprovadas),
        "bloqueadas_guardrail": sum(1 for m in curadas if m.alerta_guardrail),
        "descartadas": sum(1 for m in curadas if m.formato_sugerido == "descartar"),
        "distribuicao_antes_quota": distribuicao_antes,
        "distribuicao_depois_quota": distribuicao_depois,
    })
    print(f"[radar-par] {len(aprovadas)} aprovadas (cidades: {distribuicao_depois})", flush=True)
    _save_state("aprovadas", [m.__dict__ for m in aprovadas])
    return aprovadas


# ============================================================
# Step angulacao — paralelo
# ============================================================

def step_angulacao():
    import time as _time
    aprovadas_dict = _load_state("aprovadas", [])
    if not aprovadas_dict:
        print("[radar-par] Sem aprovadas. Rode --step coleta antes.")
        return []
    aprovadas = [MateriaCurada(**{k: v for k, v in d.items() if k in {f.name for f in fields(MateriaCurada)}})
                 for d in aprovadas_dict]
    top = aprovadas[:TOP_N_ANGULACAO]

    # Carrega já feitas (resumível) — usa "prontas_partial" para não conflitar com prontas finais persistidas
    prontas_partial = _load_state("prontas_partial", []) or []
    feitas_hashes = {d.get("id_hash") for d in prontas_partial}
    pendentes = [m for m in top if m.id_hash not in feitas_hashes]
    print(f"[radar-par] Angulação Sonnet: {len(prontas_partial)} feitas, {len(pendentes)} pendentes (workers={WORKERS})", flush=True)

    client = anthropic.Anthropic()
    deadline = _time.time() + int(os.environ.get("SONNET_DEADLINE", "32"))

    def _angular(m: MateriaCurada):
        # retry com backoff para 429
        import anthropic as _ant
        import time as _t
        for tentativa in range(4):
            try:
                a = angular_sonnet(client, m)
                break
            except _ant.RateLimitError:
                _t.sleep(8 + tentativa * 4)
                continue
            except Exception:
                return None
        else:
            return None
        if not a:
            return None
        return MateriaPronta(
            **asdict(m),
            titulo_sultv=a.get("titulo_sultv", m.titulo),
            subtitulo=a.get("subtitulo", ""),
            lead=a.get("lead", ""),
            ganchos_3=a.get("ganchos_3", []),
            angulo_editorial=a.get("angulo_editorial", ""),
            fontes_complementares_sugeridas=a.get("fontes_complementares_sugeridas", []),
            roteiro_short_60s=a.get("roteiro_short_60s", {}),
            lead_materia_longa=a.get("lead_materia_longa", ""),
            post_instagram=a.get("post_instagram", {}),
            card_carrossel=a.get("card_carrossel", {}),
            tag_thumbnail=a.get("tag_thumbnail", ""),
        )

    novas: list[MateriaPronta] = []
    if pendentes:
        ex = ThreadPoolExecutor(max_workers=WORKERS)
        futures = {ex.submit(_angular, m): m for m in pendentes}
        done = 0
        try:
            for fu in as_completed(futures, timeout=max(0.1, deadline - _time.time())):
                mp = fu.result()
                if mp is not None:
                    novas.append(mp)
                done += 1
                # checkpoint a cada item
                _save_state("prontas_partial", prontas_partial + [n.__dict__ for n in novas])
                print(f"  [angulo] {done}/{len(pendentes)} done", flush=True)
                if _time.time() > deadline:
                    break
        except Exception as e:
            print(f"  [angulo] timeout/erro no loop: {e.__class__.__name__}", flush=True)
        finally:
            for f in futures: f.cancel()
            ex.shutdown(wait=False, cancel_futures=True)

    final_partial = prontas_partial + [n.__dict__ for n in novas]
    _save_state("prontas_partial", final_partial)

    pendentes_apos = [m for m in top if m.id_hash not in {d.get("id_hash") for d in final_partial}]
    forcar_finalizar = os.environ.get("ANGULACAO_FORCE_FINAL", "").strip() == "1"
    if pendentes_apos and not forcar_finalizar:
        print(f"[radar-par] Angulação parcial: {len(final_partial)}/{len(top)} feitas. Rode --step angulacao de novo (ou ANGULACAO_FORCE_FINAL=1 para finalizar com o que tem).", flush=True)
        return []

    if pendentes_apos:
        print(f"[radar-par] Finalizando com angulação parcial: {len(final_partial)}/{len(top)} (forçado)", flush=True)

    prontas = [MateriaPronta(**{k: v for k, v in d.items() if k in {f.name for f in fields(MateriaPronta)}})
               for d in final_partial]
    prontas.sort(key=lambda m: m.score_combinado, reverse=True)
    _log("angulacao", {"prontas": len(prontas)})
    _save_state("prontas", [m.__dict__ for m in prontas])
    print(f"[radar-par] {len(prontas)} prontas", flush=True)
    return prontas


# ============================================================
# Step persistir — paralelo, mas quota é sequencial
# ============================================================

def step_persistir():
    import time as _time
    prontas_dict = _load_state("prontas", [])
    if not prontas_dict:
        print("[radar-par] Sem prontas. Rode --step angulacao antes.")
        return []
    prontas = [MateriaPronta(**{k: v for k, v in d.items() if k in {f.name for f in fields(MateriaPronta)}})
               for d in prontas_dict]

    # Resumível
    decisoes_partial = _load_state("decisoes_partial", []) or []
    decididos_hashes = {d.get("id_hash") for d in decisoes_partial}
    pendentes = [m for m in prontas if m.id_hash not in decididos_hashes]
    print(f"[radar-par] Guardrail final: {len(decisoes_partial)} decididos, {len(pendentes)} pendentes (workers={WORKERS})", flush=True)

    client = anthropic.Anthropic()
    deadline = _time.time() + int(os.environ.get("GUARDRAIL_DEADLINE", "36"))

    def _gr(m: MateriaPronta):
        import anthropic as _ant
        for tentativa in range(3):
            try:
                g = guardrail_final(client, m, QUOTA_DIARIA_PUBLICACAO)
                return m, g
            except _ant.RateLimitError:
                _time.sleep(5 + tentativa * 3)
                continue
            except Exception:
                return m, None
        return m, None

    if pendentes:
        ex = ThreadPoolExecutor(max_workers=WORKERS)
        futures = {ex.submit(_gr, m): m for m in pendentes}
        try:
            for fu in as_completed(futures, timeout=max(0.1, deadline - _time.time())):
                m, g = fu.result()
                rec = {"id_hash": m.id_hash, "decisao": (g or {}).get("decisao") if g else None,
                       "explicacao_curta": (g or {}).get("explicacao_curta", "")}
                decisoes_partial.append(rec)
                _save_state("decisoes_partial", decisoes_partial)
                print(f"  [gr] {len(decisoes_partial)}/{len(prontas)} → {rec['decisao']}", flush=True)
                if _time.time() > deadline:
                    break
        except Exception as e:
            print(f"  [gr] timeout: {e.__class__.__name__}", flush=True)
        finally:
            for f in futures: f.cancel()
            ex.shutdown(wait=False, cancel_futures=True)

    pendentes_apos = [m for m in prontas if m.id_hash not in {d.get("id_hash") for d in decisoes_partial}]
    if pendentes_apos:
        print(f"[radar-par] Guardrail parcial: {len(decisoes_partial)}/{len(prontas)} decididos. Rode --step persistir de novo.", flush=True)
        return []

    # Reconstrói lista (m, g) a partir do partial
    by_hash = {d["id_hash"]: d for d in decisoes_partial}
    decisoes = [(m, by_hash.get(m.id_hash)) for m in prontas]

    # Reordena pelo score combinado para aplicar quota corretamente
    decisoes.sort(key=lambda x: x[0].score_combinado, reverse=True)

    quota = QUOTA_DIARIA_PUBLICACAO
    final = []
    for m, g in decisoes:
        decisao_val = (g or {}).get("decisao")
        if not g or not decisao_val:
            m.decisao_final = "ALERTA_HUMANO"
            m.decisao_motivo = "Parse JSON do guardrail final falhou — revisar manualmente"
        else:
            m.decisao_final = decisao_val
            m.decisao_motivo = g.get("explicacao_curta", "")
        if m.decisao_final == "PUBLICAR" and quota <= 0:
            # quota esgotada → rebaixa
            m.decisao_final = "REBAIXAR"
            m.decisao_motivo = (m.decisao_motivo or "") + " | Quota diária esgotada"
        if m.decisao_final == "PUBLICAR":
            quota = max(0, quota - 1)
        final.append(m)

    persisted = final[:TOP_N_PERSISTIDO]
    try:
        write_radar_diario(persisted)
        write_historico(persisted)
        sheets_ok = True
    except Exception as e:
        print(f"[radar-par] AVISO: gravação no Sheets falhou ({e.__class__.__name__}: {e}). "
              f"Persistindo apenas no state local.", flush=True)
        sheets_ok = False
    _save_state("sheets_ok_ultima_execucao", sheets_ok)
    _log("persistir", {
        "persistidas": len(persisted),
        "publicar": sum(1 for m in persisted if m.decisao_final == "PUBLICAR"),
        "rebaixar": sum(1 for m in persisted if m.decisao_final == "REBAIXAR"),
        "bloquear": sum(1 for m in persisted if m.decisao_final == "BLOQUEAR"),
        "alerta_humano": sum(1 for m in persisted if m.decisao_final == "ALERTA_HUMANO"),
    })
    _save_state("persistidas", [m.__dict__ for m in persisted])
    print(f"[radar-par] {len(persisted)} persistidas no Sheets", flush=True)
    return persisted


def step_produzir(modo: str = "auto"):
    persistidas_dict = _load_state("persistidas", [])
    if not persistidas_dict:
        print("[radar-par] Sem persistidas. Rode --step persistir antes.")
        return
    persistidas = [MateriaPronta(**{k: v for k, v in d.items() if k in {f.name for f in fields(MateriaPronta)}})
                   for d in persistidas_dict]

    publicar = [m for m in persistidas if m.decisao_final == "PUBLICAR"]
    # YouTube descontinuado em 08/05/2026 — short_60s não são mais produzidos
    # nem enviados ao canal. Itens classificados como short_60s permanecem no
    # Sheets/state pra auditoria, mas saem do funil de publicação do dia.
    shorts_descartados = [m for m in publicar if m.formato_sugerido == "short_60s"]
    materias = [m for m in publicar if m.formato_sugerido in ("materia_longa", "nota_curta")][:10]
    posts = [m for m in publicar if m.formato_sugerido in ("post_instagram", "card_carrossel")][:15]

    if modo == "dry-run":
        print(f"[radar-par] DRY-RUN — Mat:{len(materias)} Posts:{len(posts)} "
              f"Shorts descartados (YouTube OFF):{len(shorts_descartados)}")
        return

    if shorts_descartados:
        print(f"[radar-par] YouTube descontinuado — pulando {len(shorts_descartados)} "
              f"short_60s (decisão 08/05/2026)", flush=True)
    print(f"[radar-par] Produzindo {len(materias)} matérias...", flush=True)
    for m in materias:
        try: produzir_materia(m)
        except Exception as e: print(f"  [erro mat] {e}", flush=True)
    print(f"[radar-par] Publicando {len(posts)} posts...", flush=True)
    for m in posts:
        try: publicar_post(m)
        except Exception as e: print(f"  [erro post] {e}", flush=True)
    _log("producao", {"shorts": 0, "shorts_descartados": len(shorts_descartados),
                      "materias": len(materias), "posts": len(posts)})


def step_verify():
    if not STATE_FILE.exists():
        print("[radar-par] Sem state.")
        return
    state = json.loads(STATE_FILE.read_text())
    print(json.dumps(
        {k: (len(v) if isinstance(v, list) else v) for k, v in state.items()},
        indent=2, ensure_ascii=False))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--step", required=True, choices=["coleta-so", "haiku", "coleta", "angulacao", "persistir", "produzir", "verify"])
    p.add_argument("--modo", default="auto", choices=["auto", "dry-run"])
    args = p.parse_args()
    {
        "coleta-so": step_coleta_so,
        "haiku": step_haiku,
        "coleta": step_coleta,
        "angulacao": step_angulacao,
        "persistir": step_persistir,
        "produzir": lambda: step_produzir(args.modo),
        "verify": step_verify,
    }[args.step]()


if __name__ == "__main__":
    main()
