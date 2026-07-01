#!/usr/bin/env python3
"""
resume_posts_2026_05_26.py — retoma a publicação dos posts que NÃO completaram
no --fase publicar de hoje (timeout do bash aos 40s).

Estado conhecido antes deste script (verificado via Meta API):
  - Defesa Civil granizo (427ec442): FB + IG PUBLICADOS (09:11) -> NÃO republicar
  - El Niño junho (2675b67b): NÃO publicado                     -> FB + IG
  - Fispal Venâncio (6b40ab03): NÃO publicado                   -> FB + IG
  - Onça-parda Bento (e5e39e4c): NÃO publicado                  -> FB + IG
  - Castramóvel (materia): DUPLICATA — já existia no Wix, sem novo conteúdo

Publicação não é idempotente: granizo fica de fora.
Uso: python3 scripts/resume_posts_2026_05_26.py <id_hash>
"""
import json, sys
from pathlib import Path
from dataclasses import fields

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from cowork_pipeline import _load_env_file
_load_env_file()

from curador import MateriaPronta
from publicar_post import publicar_post

HOJE = "2026-05-26"
RESTANTES = {  # FB + IG completo
    "2675b67bf065e86b34c90c8c9e1ab9b6f19a54d3",  # El Niño
    "6b40ab03e5d50a99a4deaf155a6c713616eb77fa",  # Fispal Venâncio
    "e5e39e4c7a8f4bcb761c2ea78ae528c3a677584e",  # Onça-parda Bento
}

pauta = json.loads((ROOT / "state" / f"pauta_{HOJE}.json").read_text(encoding="utf-8"))["pauta"]
valid = {f.name for f in fields(MateriaPronta)}
itens = {d["id_hash"]: MateriaPronta(**{k: v for k, v in d.items() if k in valid}) for d in pauta}

alvo = sys.argv[1] if len(sys.argv) > 1 else ""

if alvo in RESTANTES:
    res = publicar_post(itens[alvo])
    print(f"[resume] {alvo[:8]} -> {res}")
else:
    print(f"[resume] alvo inválido: {alvo!r}. Use um id_hash de RESTANTES: {sorted(RESTANTES)}")
    sys.exit(2)
