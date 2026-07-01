#!/usr/bin/env python3
"""publicar_so_pendentes_2026_05_28.py — publica em redes APENAS o item solicitado via argv.

Uso: PYTHONPATH=/tmp/mypylibs python3 scripts/publicar_so_pendentes_2026_05_28.py <id_hash_prefix>
"""
from __future__ import annotations
import json, sys, os
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-05-28"

sys.path.insert(0, str(ROOT / "scripts"))

from dotenv import load_dotenv  # type: ignore
load_dotenv(ROOT / ".env")

from curador import MateriaBruta  # type: ignore
from publicar_post import publicar_post  # type: ignore


def main():
    prefix = sys.argv[1] if len(sys.argv) > 1 else ""
    if not prefix:
        print("uso: <id_hash_prefix>")
        sys.exit(2)

    pauta_path = ROOT / "state" / f"pauta_{HOJE}.json"
    pauta = json.loads(pauta_path.read_text(encoding="utf-8"))

    alvo = None
    for it in pauta.get("pauta", []):
        if it["id_hash"].startswith(prefix):
            alvo = it
            break
    if not alvo:
        print(f"nao achei id_hash com prefixo {prefix}")
        sys.exit(3)

    if alvo.get("decisao_final") != "PUBLICAR":
        print(f"item {alvo['id_hash'][:12]} nao eh PUBLICAR ({alvo.get('decisao_final')})")
        sys.exit(4)

    # Reconstroi MateriaBruta com os campos essenciais
    m_dict = {
        "id_hash": alvo["id_hash"],
        "titulo": alvo.get("titulo_sultv") or alvo.get("titulo", ""),
        "resumo": alvo.get("subtitulo", "") or alvo.get("resumo", ""),
        "url": alvo.get("url", ""),
        "fonte_nome": alvo.get("fonte_nome", ""),
        "cidade": alvo.get("cidade", ""),
        "publicado_em": alvo.get("publicado_em", ""),
        "coletado_em": alvo.get("coletado_em", ""),
        "tag_principal": alvo.get("tag_principal", ""),
        "tags_secundarias": alvo.get("tags_secundarias", []),
        "score_fonte": alvo.get("score_fonte", 0),
        "score_editorial": alvo.get("score_editorial", 0),
        "formato_sugerido": alvo.get("formato_sugerido", "post_instagram"),
        "post_instagram": alvo.get("post_instagram", {}),
        "lead": alvo.get("lead", ""),
        "ganchos_3": alvo.get("ganchos_3", []),
        "angulo_editorial": alvo.get("angulo_editorial", ""),
        "subtitulo": alvo.get("subtitulo", ""),
        "tag_thumbnail": alvo.get("tag_thumbnail", ""),
        "briefing_visual": alvo.get("briefing_visual", {}),
    }

    class M:
        pass
    m = M()
    for k, v in m_dict.items():
        setattr(m, k, v)

    print(f"[publicar-pendente] {m.id_hash[:12]} — {m.titulo[:60]}")
    res = publicar_post(m, link_artigo="")
    print(f"[publicar-pendente] resultado: {res}")

    # registra log local sucesso/falha
    log_path = ROOT / "logs" / f"{HOJE}.json"
    log_path.parent.mkdir(exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({
            "ts": datetime.now(timezone.utc).isoformat(),
            "stage": "cowork_publicar_pendente",
            "id_hash": m.id_hash,
            "titulo": m.titulo[:80],
            "resultado": res,
        }, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
