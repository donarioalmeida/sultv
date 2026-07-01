#!/usr/bin/env python3
"""
publicar_posts_2026_05_25.py — publica APENAS os posts post_instagram
PUBLICAR da pauta do dia que não saíram na fase publicar (interrompida por
timeout). Evita re-rodar --fase publicar inteira (não-idempotente) — não toca
em matérias nem re-promove dupes.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from dataclasses import fields

sys.path.insert(0, str(Path(__file__).resolve().parent))

# carrega .env
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except Exception:
    pass

from curador import MateriaPronta
from publicar_post import publicar_post

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-05-25"

pauta_path = ROOT / "state" / f"pauta_{HOJE}.json"
data = json.loads(pauta_path.read_text(encoding="utf-8"))
pauta_dict = data.get("pauta", [])

valid_fields = {f.name for f in fields(MateriaPronta)}
pauta = [MateriaPronta(**{k: v for k, v in d.items() if k in valid_fields}) for d in pauta_dict]

posts = [m for m in pauta
         if m.decisao_final == "PUBLICAR"
         and m.formato_sugerido in ("post_instagram", "card_carrossel")
         and getattr(m, "post_instagram", None)]

print(f"[posts] {len(posts)} posts post_instagram PUBLICAR para publicar:")
for m in posts:
    print(f"   - {m.titulo_sultv[:70]}")

resultados = []
for m in posts:
    try:
        res = publicar_post(m, link_artigo="")
        if res:
            resultados.append((m.titulo_sultv, res))
            print(f"[post] PUBLICADO: {res}")
        else:
            print(f"[post] ⚠ retorno vazio para: {m.titulo_sultv[:60]}")
    except Exception as e:
        print(f"[post] ✗ Falha em '{m.titulo_sultv[:50]}': {e}")

print(f"\n[posts] Total publicados: {len(resultados)}")
for t, r in resultados:
    print(f"   ✔ {t[:60]} -> {r}")
