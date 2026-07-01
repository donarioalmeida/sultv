#!/usr/bin/env python3
"""trocar_capa_2026_06_06.py — substitui capa gradiente pela foto real (fix gate og).

Uso: PYTHONPATH=/tmp/pylibs python3 scripts/trocar_capa_2026_06_06.py <id_hash_prefix>
Fluxo: acha o post no Wix por título -> gera imagem pela cascata corrigida ->
upload Wix Media -> PATCH draft-posts/{id} (media) -> POST /publish.
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
from buscar_imagem_limpa import obter_imagem_limpa
from imagens import upload_wix_media

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

    # 1. localizar post pelo título (prefixo 50 chars, como o dedup faz)
    q = {"filter": {"title": {"$startsWith": m.titulo_sultv[:50]}},
         "paging": {"limit": 5, "offset": 0}, "fieldsets": ["URL"]}
    r = requests.post(POSTS_QUERY, headers=H, json=q, timeout=20)
    r.raise_for_status()
    posts = r.json().get("posts", [])
    if not posts:
        print(f"[capa] post não encontrado para: {m.titulo_sultv[:60]}")
        sys.exit(2)
    post = posts[0]
    pid = post["id"]
    print(f"[capa] post: {pid} — {post.get('title','')[:60]}")

    # 2. imagem pela cascata corrigida
    bv = getattr(m, "briefing_visual", None) or {}
    info = obter_imagem_limpa(url_fonte=m.url, titulo=m.titulo_sultv,
                              tag_principal=m.tag_principal, cidade=m.cidade,
                              briefing_visual=bv, gerar_variantes=True,
                              formatos_alvo=["wix_cover"])
    if not info or info.get("origem") == "gradiente_sultv":
        print(f"[capa] cascata devolveu {info.get('origem') if info else None} — abortando (não vale trocar gradiente por gradiente)")
        sys.exit(3)
    raw = (info.get("variantes") or {}).get("wix_cover") or info["bytes"]
    fname = f"radar_{HOJE.replace('-','')}_{m.id_hash[:8]}_cover_fix.jpg"
    up = upload_wix_media(raw, fname, mime_type="image/jpeg")
    if not up or not up.get("id"):
        print("[capa] upload falhou"); sys.exit(4)
    print(f"[capa] upload OK: {up['url']} (origem {info['origem']})")

    # 3. PATCH media + publish
    alt = info.get("alt_text") or m.titulo_sultv[:140]
    media = {"wixMedia": {"image": {"id": up["id"], "url": up["url"],
             "width": up.get("width") or 1600, "height": up.get("height") or 900,
             "altText": alt}}, "displayed": True, "custom": False}
    body = {"draftPost": {"id": pid, "media": media}}
    r = requests.patch(f"{DRAFTS}/{pid}", headers=H, json=body, timeout=30)
    print(f"[capa] PATCH: {r.status_code} {r.text[:150] if r.status_code>=400 else ''}")
    r.raise_for_status()
    r = requests.post(f"{DRAFTS}/{pid}/publish", headers=H, timeout=30)
    print(f"[capa] publish: {r.status_code}")
    r.raise_for_status()
    print(f"[capa] ✅ capa trocada: {m.titulo_sultv[:60]}")


if __name__ == "__main__":
    main()
