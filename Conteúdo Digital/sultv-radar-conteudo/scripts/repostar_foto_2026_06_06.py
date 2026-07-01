#!/usr/bin/env python3
"""repostar_foto_2026_06_06.py — reposta FB/IG com foto real após fix do gate og:image.

Contexto: posts de 06/06 saíram com gradiente (gate 900px rejeitava og:image).
Os 4 posts FB verdes foram apagados via Graph API. Este script reposta um item
por execução (teto bash 45s), regenerando a imagem pela cascata corrigida.

Uso: PYTHONPATH=/tmp/pylibs python3 scripts/repostar_foto_2026_06_06.py <id_hash_prefix>
"""
from __future__ import annotations
import json, sys, os
from dataclasses import fields
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
HOJE = "2026-06-06"

for raw in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
    line = raw.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

from curador import MateriaPronta
from publicar_post import publicar_post

PAUTA = ROOT / "state" / f"pauta_{HOJE}.json"
URLMAP = ROOT / "state" / f"url_por_hash_{HOJE}.json"
SOCIAL = ROOT / "state" / f"social_posted_{HOJE}.json"


def main():
    prefix = sys.argv[1]
    pauta = json.loads(PAUTA.read_text(encoding="utf-8"))["pauta"]
    urlmap = json.loads(URLMAP.read_text(encoding="utf-8"))
    valid = {f.name for f in fields(MateriaPronta)}
    alvo = next(d for d in pauta if d["id_hash"].startswith(prefix))
    m = MateriaPronta(**{k: v for k, v in alvo.items() if k in valid})
    link = urlmap.get(m.id_hash, "")
    print(f"[repost] {m.id_hash[:8]} {m.titulo_sultv[:50]} link={'sim' if link else 'nao'}")
    res = publicar_post(m, link_artigo=link)
    print(f"[repost] resultado: {res}")
    if res:
        social = json.loads(SOCIAL.read_text(encoding="utf-8"))
        social["promo:" + m.id_hash] = {"res": res, "titulo": m.titulo_sultv,
                                        "obs": "repost com foto real (fix gate og 2026-06-06)"}
        SOCIAL.write_text(json.dumps(social, ensure_ascii=False, indent=2), encoding="utf-8")
        print("[repost] social state atualizado")


if __name__ == "__main__":
    main()
