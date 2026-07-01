#!/usr/bin/env python3
"""Publica apenas o post da Wine SA (Bento Gonçalves) — o terceiro post do dia,
que pode ter sido interrompido por timeout na fase publicar."""
from __future__ import annotations
import json
import os
import sys
from dataclasses import fields
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dotenv import load_dotenv
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

from curador import MateriaPronta
from publicar_post import publicar_post

ID_WINE = "bc7b4592afbe4be54f5137a9e16b76cb4ddeeb92"
data = json.loads((ROOT / "state" / "pauta_2026-05-17.json").read_text(encoding="utf-8"))
valid = {f.name for f in fields(MateriaPronta)}
item = next(m for m in data["pauta"] if m["id_hash"] == ID_WINE)
m = MateriaPronta(**{k: v for k, v in item.items() if k in valid})
res = publicar_post(m)
print(f"[wine] resultado: {res}")
