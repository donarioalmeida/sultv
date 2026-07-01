#!/usr/bin/env python3
"""limpar_texto_wix_2026_06_06.py — aplica regra 11 (sem menção a veículos) nas
matérias já publicadas hoje: rebuild do richContent a partir do .md limpo,
PATCH no draft-post e republish. Mantém capa, categorias e título.

Uso: PYTHONPATH=/tmp/pylibs python3 scripts/limpar_texto_wix_2026_06_06.py <id_hash_prefix>
"""
from __future__ import annotations
import json, sys, os
from dataclasses import fields
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
HOJE = "2026-06-06"

for raw in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
    line = raw.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

from curador import MateriaPronta
import produzir_materia as pm

TOKEN = os.environ["WIX_SITE_TOKEN"]
H = {"Authorization": TOKEN, "Content-Type": "application/json"}
if os.getenv("WIX_SITE_ID", "").strip():
    H["wix-site-id"] = os.environ["WIX_SITE_ID"].strip()
DRAFTS = "https://www.wixapis.com/blog/v3/draft-posts"
POSTS_QUERY = "https://www.wixapis.com/blog/v3/posts/query"


def main():
    prefix = sys.argv[1]
    pauta = json.loads((ROOT / "state" / f"pauta_{HOJE}.json").read_text(encoding="utf-8"))["pauta"]
    valid = {f.name for f in fields(MateriaPronta)}
    alvo = next(d for d in pauta if d["id_hash"].startswith(prefix))
    m = MateriaPronta(**{k: v for k, v in alvo.items() if k in valid})

    corpo = (ROOT / "state" / f"materias_{HOJE}" / f"{m.id_hash}.md").read_text(encoding="utf-8")
    reescrita = pm._parse_resposta_sonnet(corpo)
    assert reescrita.get("artigo"), "md sem ### Artigo ###"
    pm._REESCRITA_CACHE[m.id_hash] = reescrita

    # localizar post publicado
    q = {"filter": {"title": {"$startsWith": m.titulo_sultv[:50]}},
         "paging": {"limit": 5, "offset": 0}, "fieldsets": ["URL"]}
    r = requests.post(POSTS_QUERY, headers=H, json=q, timeout=20)
    r.raise_for_status()
    posts = r.json().get("posts", [])
    assert posts, f"post não encontrado: {m.titulo_sultv[:60]}"
    post = posts[0]
    pid = post["id"]
    img = ((post.get("media") or {}).get("wixMedia") or {}).get("image") or {}
    cover = None
    if img.get("id"):
        cover = {"id": img["id"], "url": img.get("url", ""),
                 "width": img.get("width") or 1600, "height": img.get("height") or 900,
                 "alt_text": img.get("altText") or m.titulo_sultv[:140],
                 "fonte_credito": "", "origem": "existente"}
    print(f"[limpar] post {pid} cover={'sim' if cover else 'não'}")

    body = pm._build_post_body(m, cover=cover)
    patch = {"draftPost": {"id": pid,
                           "richContent": body["richContent"],
                           "seoData": body.get("seoData", {})}}
    r = requests.patch(f"{DRAFTS}/{pid}", headers=H, json=patch, timeout=30)
    print(f"[limpar] PATCH: {r.status_code} {r.text[:150] if r.status_code >= 400 else ''}")
    r.raise_for_status()
    r = requests.post(f"{DRAFTS}/{pid}/publish", headers=H, timeout=30)
    print(f"[limpar] publish: {r.status_code}")
    r.raise_for_status()
    print(f"[limpar] ✅ texto limpo republicado: {m.titulo_sultv[:60]}")


if __name__ == "__main__":
    main()
