#!/usr/bin/env python3
"""
cowork_pipeline.py — pipeline do radar sem dependência da API Anthropic
========================================================================
Substitui o radar_main.py para o cenário em que o Cowork (Claude) faz toda a
parte de IA dentro da própria sessão, ao invés de chamar api.anthropic.com.

Fases (todas idempotentes, executadas pelo scheduled task `sultv-radar-pauta-diaria`):

  --fase coleta
      Roda coletor + dedup, escreve state/candidatos_YYYY-MM-DD.json
      Nenhuma chamada Anthropic. Apenas RSS/HTTP scraping + Voyage embeddings
      pra dedup (Voyage tem free tier de 50M tokens/mês).

  --fase aprovar
      Lê state/curadas_YYYY-MM-DD.json (que o Claude no Cowork escreveu
      após classificar cada item dos candidatos), aplica boost geográfico
      + quota de diversidade, escreve state/aprovadas_YYYY-MM-DD.json.
      Sem IA.

  --fase publicar
      Lê state/pauta_YYYY-MM-DD.json + state/materias_YYYY-MM-DD/*.md (que
      o Claude no Cowork escreveu), publica via Wix Blog + Meta Graph API,
      grava na aba Radar_Diario do Sheets, envia e-mail de status.
      Sem IA.

Uso típico (em sequência, com Claude fazendo o trabalho de IA entre as fases):

  python3 scripts/cowork_pipeline.py --fase coleta
  # ... Claude lê candidatos.json, escreve curadas.json ...
  python3 scripts/cowork_pipeline.py --fase aprovar
  # ... Claude lê aprovadas.json, escreve pauta.json + materias/*.md ...
  python3 scripts/cowork_pipeline.py --fase publicar
"""
from __future__ import annotations
import argparse
import json
import sys
from dataclasses import asdict, fields
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))


def _load_env_file():
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    import os
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


def _hoje() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _state_path(nome: str) -> Path:
    return ROOT / "state" / f"{nome}_{_hoje()}.json"


def _materias_dir() -> Path:
    return ROOT / "state" / f"materias_{_hoje()}"


def _log(stage: str, payload: dict):
    f = ROOT / "logs" / f"{_hoje()}.json"
    f.parent.mkdir(exist_ok=True)
    line = json.dumps(
        {"ts": datetime.now(timezone.utc).isoformat(), "stage": stage, **payload},
        ensure_ascii=False,
    )
    with open(f, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


# ============================================================
# FASE 1: COLETA (sem IA)
# ============================================================

def fase_coleta() -> None:
    """Coleta + dedup. Sem IA. Escreve state/candidatos_YYYY-MM-DD.json."""
    from coletor import coletar_todas_fontes
    from dedup import dedup_pipeline_completo
    from sheets_writer import ler_hashes_recentes
    from guardrails import passa_stop_list

    print("[cowork] Fase 1/3: coleta + dedup (sem IA)")
    print("[cowork] Coletando das fontes...")
    brutos = coletar_todas_fontes()
    _log("cowork_coleta", {"total_brutos": len(brutos)})
    print(f"[cowork] {len(brutos)} itens brutos coletados")

    print("[cowork] Aplicando dedup (3 camadas)...")
    hashes_recentes = ler_hashes_recentes(horas=48)
    dedupados = dedup_pipeline_completo(brutos, hashes_recentes)
    _log("cowork_dedup", {"antes": len(brutos), "depois": len(dedupados)})
    print(f"[cowork] {len(dedupados)} itens após dedup")

    # Stop-list lexical antes de mandar pro Claude classificar
    filtrados = [it for it in dedupados if passa_stop_list(it.titulo + " " + it.resumo)]
    print(f"[cowork] {len(filtrados)} itens após stop-list lexical")

    # Persiste como lista de dicts pro Claude ler em uma única operação
    out = _state_path("candidatos")
    out.parent.mkdir(exist_ok=True)
    payload = {
        "data": _hoje(),
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "total": len(filtrados),
        "candidatos": [asdict(it) for it in filtrados],
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[cowork] ✅ Escrito: {out}")
    print(f"[cowork] Próximo passo: Claude lê {out.name}, classifica cada item")
    print(f"[cowork] seguindo prompts/01_classificacao_massa.md + prompts/04_guardrails_classifier.md")
    print(f"[cowork] e escreve state/curadas_{_hoje()}.json com mesma estrutura + campos:")
    print(f"[cowork]   score_editorial, tag_principal, tags_secundarias,")
    print(f"[cowork]   formato_sugerido, justificativa, alerta_guardrail, guardrail_motivo")


# ============================================================
# FASE 2: APROVAR (lê curadas que Claude escreveu, aplica boost+quota, sem IA)
# ============================================================

def fase_aprovar() -> None:
    """Lê curadas.json escrito pelo Claude, aplica boost geográfico + quota
    de diversidade, escreve aprovadas.json. Sem IA."""
    from curador import MateriaCurada, score_combinado
    from geografia import aplicar_boost_geografico, aplicar_quota_diversidade, QUOTA_POR_CIDADE, relatorio_distribuicao

    inp = _state_path("curadas")
    if not inp.exists():
        print(f"[cowork] ✗ Arquivo {inp} não existe — Claude ainda não classificou os candidatos.")
        sys.exit(2)

    data = json.loads(inp.read_text(encoding="utf-8"))
    curadas_dict = data.get("curadas", [])
    if not curadas_dict:
        print(f"[cowork] ✗ {inp} está vazio.")
        sys.exit(2)

    print(f"[cowork] Fase 2/3: aprovar (boost + quota) em {len(curadas_dict)} itens curados")

    # Hidrata como MateriaCurada
    valid_fields = {f.name for f in fields(MateriaCurada)}
    curadas = []
    for d in curadas_dict:
        m = MateriaCurada(**{k: v for k, v in d.items() if k in valid_fields})
        if not m.score_combinado:
            m.score_combinado = score_combinado(m.score_fonte, m.score_editorial)
        curadas.append(m)

    aprovadas = [m for m in curadas
                 if not m.alerta_guardrail
                 and m.formato_sugerido != "descartar"]
    aprovadas.sort(key=lambda m: m.score_combinado, reverse=True)

    aprovadas = aplicar_boost_geografico(aprovadas)
    distribuicao_antes = relatorio_distribuicao(aprovadas)
    aprovadas = aplicar_quota_diversidade(aprovadas, max_por_cidade=QUOTA_POR_CIDADE)
    distribuicao_depois = relatorio_distribuicao(aprovadas)

    _log("cowork_aprovar", {
        "curadas": len(curadas),
        "aprovadas_pos_boost_e_quota": len(aprovadas),
        "bloqueadas_guardrail": sum(1 for m in curadas if m.alerta_guardrail),
        "descartadas": sum(1 for m in curadas if m.formato_sugerido == "descartar"),
        "distribuicao_antes_quota": distribuicao_antes,
        "distribuicao_depois_quota": distribuicao_depois,
    })

    print(f"[cowork] {len(aprovadas)} aprovadas após boost geográfico + quota {QUOTA_POR_CIDADE}/cidade")
    print(f"[cowork] Distribuição por cidade: {distribuicao_depois}")

    out = _state_path("aprovadas")
    payload = {
        "data": _hoje(),
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "total": len(aprovadas),
        "top_n_angulacao": 20,
        "aprovadas": [m.__dict__ for m in aprovadas],
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[cowork] ✅ Escrito: {out}")
    print(f"[cowork] Próximo passo: Claude lê {out.name}, angula top 20")
    print(f"[cowork] seguindo prompts/02_angulacao_editorial.md, aplica guardrail final")
    print(f"[cowork] seguindo prompts/04_guardrails_classifier.md, e escreve:")
    print(f"[cowork]   state/pauta_{_hoje()}.json — pauta completa com decisao_final")
    print(f"[cowork]   state/materias_{_hoje()}/<id_hash>.md — corpo de cada matéria longa aprovada")


# ============================================================
# FASE 3: PUBLICAR (lê pauta + matérias que Claude escreveu, publica, sem IA)
# ============================================================

def fase_publicar() -> None:
    """Lê pauta.json + materias/ escritos pelo Claude, publica via Wix Blog +
    Meta API, escreve na aba Radar_Diario do Sheets, envia e-mail de status."""
    from curador import MateriaPronta, QUOTA_DIARIA_PUBLICACAO
    from sheets_writer import write_radar_diario, write_historico
    from publicar_post import publicar_post
    from enviar_relatorio import enviar_relatorio_diario

    # Import condicional: produzir_materia tem hooks pra usar texto já escrito
    from produzir_materia import publicar_materia_com_texto

    inp = _state_path("pauta")
    if not inp.exists():
        print(f"[cowork] ✗ {inp} não existe — Claude ainda não escreveu a pauta.")
        sys.exit(2)

    data = json.loads(inp.read_text(encoding="utf-8"))
    pauta_dict = data.get("pauta", [])
    if not pauta_dict:
        print(f"[cowork] ✗ {inp} está vazio.")
        sys.exit(2)

    valid_fields = {f.name for f in fields(MateriaPronta)}
    pauta = [MateriaPronta(**{k: v for k, v in d.items() if k in valid_fields}) for d in pauta_dict]

    print(f"[cowork] Fase 3/3: publicar ({len(pauta)} itens na pauta)")

    # 1. Persiste na aba Radar_Diario do Sheets (com decisao_final)
    print(f"[cowork] Persistindo no Google Sheets...")
    try:
        write_radar_diario(pauta)
        write_historico(pauta)
        sheets_ok = True
    except Exception as e:
        print(f"[cowork] ⚠ Sheets falhou: {e}")
        sheets_ok = False

    # 2. Separa publicáveis
    publicar = [m for m in pauta if m.decisao_final == "PUBLICAR"]
    shorts_descartados = [m for m in publicar if m.formato_sugerido == "short_60s"]
    materias = [m for m in publicar if m.formato_sugerido in ("materia_longa", "nota_curta")][:10]
    posts = [m for m in publicar if m.formato_sugerido in ("post_instagram", "card_carrossel")][:15]

    print(f"[cowork] YouTube descontinuado — pulando {len(shorts_descartados)} short_60s")

    # 3. Publica matérias longas — usa texto que Claude escreveu em state/materias/<id>.md
    materias_dir = _materias_dir()
    materias_urls = []
    # Mapa id_hash → URL pública da matéria (só URLs de site, não drafts),
    # para o CTA dos posts linkar a matéria certa em vez da home (Donário 2026-05-21).
    url_por_hash = {}
    if materias:
        print(f"[cowork] Publicando {len(materias)} matérias...")
        for m in materias:
            md_path = materias_dir / f"{m.id_hash}.md"
            if not md_path.exists():
                print(f"[materia] ✗ {md_path.name} não existe — pulando {m.titulo_sultv[:60]}")
                continue
            corpo = md_path.read_text(encoding="utf-8")
            try:
                url = publicar_materia_com_texto(m, corpo)
                if url:
                    materias_urls.append(url)
                    # Só guarda URL pública (post no site), não link de draft do editor.
                    if "/post/" in url or "sultv.com.br" in url:
                        url_por_hash[m.id_hash] = url
                    print(f"[materia] PUBLICADA: {url}")
            except Exception as e:
                print(f"[materia] ✗ Falha ao publicar {m.titulo_sultv[:60]}: {e}")

    # 4. Publica posts em redes (Facebook + Instagram)
    posts_urls = []
    if posts:
        print(f"[cowork] Publicando {len(posts)} posts em redes...")
        for m in posts:
            try:
                # Link da matéria: campo explícito da angulação OU URL publicada
                # nesta execução para o mesmo id_hash. Sem isso, CTA usa marca/home.
                link = (getattr(m, "url_artigo", "") or "").strip() \
                    or url_por_hash.get(m.id_hash, "")
                res = publicar_post(m, link_artigo=link)
                if res:
                    posts_urls.append(res)
                    print(f"[post] PUBLICADO: {res}")
            except Exception as e:
                print(f"[post] ✗ Falha: {e}")

    # 4b. Ponto 2 (Donário 2026-05-21): cada matéria longa publicada vira também
    # um post social (FB+IG) com link DIRETO pro artigo — matéria como motor de
    # tráfego do site. Só dispara para matérias com URL pública (não drafts) e que
    # tenham post_instagram na angulação.
    materias_social_urls = []
    materias_para_social = [m for m in materias
                            if url_por_hash.get(m.id_hash)
                            and getattr(m, "post_instagram", None)]
    if materias_para_social:
        print(f"[cowork] Promovendo {len(materias_para_social)} matérias no social...")
        for m in materias_para_social:
            try:
                res = publicar_post(m, link_artigo=url_por_hash[m.id_hash])
                if res:
                    materias_social_urls.append(res)
                    print(f"[post-materia] PROMOVIDA: {res}")
            except Exception as e:
                print(f"[post-materia] ✗ Falha: {e}")
        posts_urls.extend(materias_social_urls)

    # 5. Log final
    _log("cowork_publicar", {
        "pauta_total": len(pauta),
        "publicar": len(publicar),
        "materias_publicadas": len(materias_urls),
        "posts_publicados": len(posts_urls),
        "materias_promovidas_social": len(materias_social_urls),
        "shorts_descartados": len(shorts_descartados),
        "sheets_ok": sheets_ok,
    })
    print(f"[cowork] ✅ Publicação concluída")
    print(f"[cowork]   Matérias: {len(materias_urls)} / Posts: {len(posts_urls)}")

    # 6. E-mail de status
    try:
        enviar_relatorio_diario(pauta_dict)
        print(f"[cowork] E-mail de status enviado")
    except Exception as e:
        print(f"[cowork] ⚠ E-mail falhou: {e}")


# ============================================================
# Verify
# ============================================================

def fase_verify() -> None:
    print(f"[cowork] === Estado do dia {_hoje()} ===")
    for nome in ("candidatos", "curadas", "aprovadas", "pauta"):
        p = _state_path(nome)
        if p.exists():
            data = json.loads(p.read_text(encoding="utf-8"))
            n = data.get("total", "?")
            print(f"  ✅ {p.name}: {n} itens")
        else:
            print(f"  ✗ {p.name}: não existe")

    md_dir = _materias_dir()
    if md_dir.exists():
        mds = list(md_dir.glob("*.md"))
        print(f"  ✅ {md_dir.name}/: {len(mds)} matérias escritas")
    else:
        print(f"  ✗ {md_dir.name}/: vazio")


# ============================================================
# Main
# ============================================================

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--fase", required=True, choices=["coleta", "aprovar", "publicar", "verify"])
    args = p.parse_args()

    if args.fase == "coleta":
        fase_coleta()
    elif args.fase == "aprovar":
        fase_aprovar()
    elif args.fase == "publicar":
        fase_publicar()
    elif args.fase == "verify":
        fase_verify()


if __name__ == "__main__":
    main()
