#!/usr/bin/env python3
"""
resume_posts_2026_05_21.py — retoma a publicação dos posts que NÃO completaram
no --fase publicar de hoje (que deu timeout no bash 45s).

Estado conhecido antes deste script:
  - Fenasul (024d2403): FB PUBLICADO (09:11), IG NÃO publicado  -> só IG aqui
  - IR Venâncio (666340ab): NÃO publicado                        -> FB + IG
  - Vinícola Aurora (2e166c78): NÃO publicado                    -> FB + IG
  - Sulgás (6b80d389): NÃO publicado                             -> FB + IG

Publicação não é idempotente: por isso Fenasul recebe SÓ IG.
"""
import json, sys
from pathlib import Path
from dataclasses import fields

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from cowork_pipeline import _load_env_file
_load_env_file()

import os
from curador import MateriaPronta
from publicar_post import (
    publicar_post,
    _gerar_e_subir_imagens_post,
    _formatar_caption_ig,
    _publicar_instagram_simples,
    _meta_token_valido,
)

HOJE = "2026-05-21"
FENASUL = "024d2403c8ef0d4f44c4e0ba5270d5401584ccd6"
SO_IG = {FENASUL}                       # já tem FB — publicar só IG
RESTANTES = {                            # FB + IG completo
    "666340ab1a91f60b7ea9badf39ae6dcb82b40f71",
    "2e166c784f3e61c919ebe50cea48f022ee37105e",
    "6b80d389f02bc58f4cb0286f35d1d601edc895d2",
}

pauta = json.loads((ROOT / "state" / f"pauta_{HOJE}.json").read_text(encoding="utf-8"))["pauta"]
valid = {f.name for f in fields(MateriaPronta)}
itens = {d["id_hash"]: MateriaPronta(**{k: v for k, v in d.items() if k in valid}) for d in pauta}

alvo = sys.argv[1] if len(sys.argv) > 1 else ""

if alvo == "fenasul":
    # Fenasul — só IG (FB já publicado)
    m = itens[FENASUL]
    token = _meta_token_valido()
    ig_id = os.getenv("META_IG_BUSINESS_ID", "").strip()
    img = _gerar_e_subir_imagens_post(m)
    if token and ig_id and img and img.get("ig_url"):
        caption = _formatar_caption_ig(m)
        res = _publicar_instagram_simples(img["ig_url"], caption, ig_id, token)
        print(f"[resume] Fenasul IG -> {res}")
    else:
        print("[resume] Fenasul IG não publicado (token/ig_id/img ausente)")
elif alvo in RESTANTES:
    res = publicar_post(itens[alvo])
    print(f"[resume] {alvo[:8]} -> {res}")
else:
    print(f"[resume] alvo inválido: {alvo!r}. Use 'fenasul' ou um id_hash de RESTANTES.")
    sys.exit(2)
