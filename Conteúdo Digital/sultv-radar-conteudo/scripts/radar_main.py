#!/usr/bin/env python3
"""
sultv-radar-conteudo — orquestrador principal
=============================================
Entry-point da skill. Executado diariamente às 06:00 via skill `schedule`.

Modos:
  --modo auto         pipeline completo (coleta → curadoria → produção → publicação)
  --modo dry-run      gera pauta no Sheets mas NÃO publica nada
  --modo coleta-apenas só coleta + dedup (sem IA)

Etapas (idempotentes — podem ser chamadas isoladamente):
  --step coleta       coleta + filtro temporal + dedup
  --step angulacao    Sonnet em cima do top 20
  --step persistir    guardrail final + grava Sheets
  --step produzir     dispara skills de produção
  --step verify       imprime state final do dia
"""
from __future__ import annotations
import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))


def _load_env_file():
    """Lê o .env e popula os.environ ANTES de qualquer outro import que dependa de env vars."""
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip()
        # remove aspas envolventes se houver
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
from preflight import preflight as _preflight

import anthropic

LOG_DIR = ROOT / "logs"
STATE_FILE = ROOT / "state" / "ultimo_run.json"
LOG_DIR.mkdir(exist_ok=True)
STATE_FILE.parent.mkdir(exist_ok=True)


def _log(stage: str, payload: dict):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    f = LOG_DIR / f"{today}.json"
    line = json.dumps({"ts": datetime.now(timezone.utc).isoformat(), "stage": stage, **payload}, ensure_ascii=False)
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
# Etapas
# ============================================================

def step_coleta() -> list[MateriaBruta]:
    print("[radar] Coletando das 118 fontes...")
    brutos = coletar_todas_fontes()
    _log("coleta", {"total_brutos": len(brutos)})
    print(f"[radar] {len(brutos)} itens brutos coletados")

    print("[radar] Aplicando dedup (3 camadas)...")
    hashes_recentes = ler_hashes_recentes(horas=48)
    dedupados = dedup_pipeline_completo(brutos, hashes_recentes)
    _log("dedup", {"antes": len(brutos), "depois": len(dedupados)})
    print(f"[radar] {len(dedupados)} itens após dedup")

    print("[radar] Curadoria Haiku (classificação em massa)...")
    client = anthropic.Anthropic()
    curadas: list[MateriaCurada] = []
    for it in dedupados:
        if not passa_stop_list(it.titulo + " " + it.resumo):
            continue
        c = curar_haiku(client, it)
        if not c:
            continue
        from dataclasses import asdict
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
        curadas.append(m)

    aprovadas = [m for m in curadas
                 if not m.alerta_guardrail
                 and m.formato_sugerido != "descartar"]
    aprovadas.sort(key=lambda m: m.score_combinado, reverse=True)

    # Camada A: boost geográfico (Camaquã/Tapes/Arambaré +3, Cristal/Chuvisca/SLS +2, Pelotas +1)
    aprovadas = aplicar_boost_geografico(aprovadas)

    # Camada B: quota de diversidade — máx 2 matérias por cidade
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
    print(f"[radar] {len(aprovadas)} matérias aprovadas para angulação (após boost geográfico + quota {QUOTA_POR_CIDADE}/cidade)")
    print(f"[radar] Distribuição por cidade: {distribuicao_depois}")
    _save_state("aprovadas", [m.__dict__ for m in aprovadas])
    return aprovadas


def step_angulacao() -> list[MateriaPronta]:
    aprovadas_dict = _load_state("aprovadas", [])
    if not aprovadas_dict:
        print("[radar] Sem aprovadas no state. Rode --step coleta antes.")
        return []
    from dataclasses import fields
    aprovadas = [MateriaCurada(**{k: v for k, v in d.items() if k in {f.name for f in fields(MateriaCurada)}})
                 for d in aprovadas_dict]
    top = aprovadas[:TOP_N_ANGULACAO]

    print(f"[radar] Angulação Sonnet em {len(top)} matérias...")
    client = anthropic.Anthropic()
    prontas: list[MateriaPronta] = []
    for m in top:
        a = angular_sonnet(client, m)
        if not a:
            continue
        from dataclasses import asdict
        mp = MateriaPronta(
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
        prontas.append(mp)

    _log("angulacao", {"prontas": len(prontas)})
    _save_state("prontas", [m.__dict__ for m in prontas])
    print(f"[radar] {len(prontas)} matérias com angulação editorial completa")
    return prontas


def step_persistir() -> list[MateriaPronta]:
    prontas_dict = _load_state("prontas", [])
    if not prontas_dict:
        print("[radar] Sem prontas no state. Rode --step angulacao antes.")
        return []
    from dataclasses import fields
    prontas = [MateriaPronta(**{k: v for k, v in d.items() if k in {f.name for f in fields(MateriaPronta)}})
               for d in prontas_dict]

    print(f"[radar] Aplicando guardrail final em {len(prontas)} matérias...")
    client = anthropic.Anthropic()
    quota = QUOTA_DIARIA_PUBLICACAO
    final = []
    for m in prontas:
        g = guardrail_final(client, m, quota)
        if not g or "decisao" not in g:
            # Parse falhou — defaulta para revisão humana, NÃO bloqueia silenciosamente
            m.decisao_final = "ALERTA_HUMANO"
            m.decisao_motivo = "Parse JSON do guardrail final falhou — revisar manualmente"
        else:
            m.decisao_final = g["decisao"]
            m.decisao_motivo = g.get("explicacao_curta", "")
        if m.decisao_final == "PUBLICAR":
            quota = max(0, quota - 1)
        final.append(m)

    persisted = final[:TOP_N_PERSISTIDO]
    write_radar_diario(persisted)
    write_historico(persisted)
    _log("persistir", {
        "persistidas": len(persisted),
        "publicar": sum(1 for m in persisted if m.decisao_final == "PUBLICAR"),
        "rebaixar": sum(1 for m in persisted if m.decisao_final == "REBAIXAR"),
        "bloquear": sum(1 for m in persisted if m.decisao_final == "BLOQUEAR"),
        "alerta_humano": sum(1 for m in persisted if m.decisao_final == "ALERTA_HUMANO"),
    })
    _save_state("persistidas", [m.__dict__ for m in persisted])
    print(f"[radar] {len(persisted)} matérias persistidas no Sheets")
    return persisted


def step_produzir(modo: str = "auto"):
    persistidas_dict = _load_state("persistidas", [])
    if not persistidas_dict:
        print("[radar] Sem persistidas no state. Rode --step persistir antes.")
        return
    from dataclasses import fields
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
        print(f"[radar] DRY-RUN — não publicando. Matérias: {len(materias)} | "
              f"Posts: {len(posts)} | Shorts descartados (YouTube OFF): {len(shorts_descartados)}")
        return

    if shorts_descartados:
        print(f"[radar] YouTube descontinuado — pulando {len(shorts_descartados)} short_60s (decisão 08/05/2026)")
    print(f"[radar] Produzindo {len(materias)} matérias longas...")
    for m in materias:
        produzir_materia(m)
    print(f"[radar] Publicando {len(posts)} posts...")
    for m in posts:
        publicar_post(m)

    _log("producao", {"shorts": 0, "shorts_descartados": len(shorts_descartados),
                      "materias": len(materias), "posts": len(posts)})


def step_verify():
    if not STATE_FILE.exists():
        print("[radar] Sem state — nada a verificar.")
        return
    state = json.loads(STATE_FILE.read_text())
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in state.items()},
                     indent=2, ensure_ascii=False))
    # Dispara relatório SMTP também quando rodando isoladamente via --step verify.
    # (Antes, só era enviado na execução completa via main(), na linha de step_produzir.)
    persistidas = state.get("persistidas") or []
    if persistidas:
        try:
            enviar_relatorio_diario(persistidas)
        except Exception as e:
            print(f"[radar] AVISO: falha ao enviar relatório SMTP ({e.__class__.__name__}: {e})")


# ============================================================
# Main
# ============================================================

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--modo", choices=["auto", "dry-run", "coleta-apenas"], default="auto")
    p.add_argument("--step", choices=["coleta", "angulacao", "persistir", "produzir", "verify"])
    p.add_argument("--data", help="YYYY-MM-DD (default: hoje)")
    p.add_argument("--skip-preflight", action="store_true",
                   help="Pula a checagem de saldo Anthropic (uso emergencial).")
    args = p.parse_args()

    # Preflight: aborta antes de gastar coleta/dedup se a Anthropic não puder atender.
    # Steps puramente de I/O (coleta, verify) podem rodar sem IA — não exigimos saldo.
    precisa_ia = args.step in (None, "angulacao", "persistir", "produzir")
    if precisa_ia and not args.skip_preflight and args.modo != "coleta-apenas":
        if not _preflight():
            print("[radar] ABORT: preflight falhou. Recarregue créditos e rode novamente.")
            sys.exit(2)

    if args.step:
        {
            "coleta": step_coleta,
            "angulacao": step_angulacao,
            "persistir": step_persistir,
            "produzir": lambda: step_produzir(args.modo),
            "verify": step_verify,
        }[args.step]()
        return

    # Pipeline completo
    if args.modo == "coleta-apenas":
        step_coleta()
        return

    step_coleta()
    step_angulacao()
    step_persistir()
    step_produzir(args.modo)

    # Relatório final
    if args.modo != "dry-run":
        enviar_relatorio_diario(_load_state("persistidas", []))
    print("[radar] Pipeline concluído.")


if __name__ == "__main__":
    main()
