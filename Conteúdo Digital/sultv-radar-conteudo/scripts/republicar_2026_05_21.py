#!/usr/bin/env python3
"""
republicar_2026_05_21.py — republica os 4 posts de hoje com a LEGENDA CORRIGIDA
(o bug que descartava o texto) + imagem regenerada pela nova cascata regional.

Por post (1 por chamada, respeitando o bash de 45s):
  1. publicar_post(m) -> novo FB + novo IG (legenda por rede + texto correto)
  2. se o novo FB subiu, DELETA o FB antigo (sem texto) via Graph API
  3. o IG antigo NÃO é deletável via API -> reportado para remoção manual no app

Uso: python3 scripts/republicar_2026_05_21.py <id_hash>
"""
import sys, json
from pathlib import Path
from dataclasses import fields

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from cowork_pipeline import _load_env_file
_load_env_file()

import os, requests
from curador import MateriaPronta
from publicar_post import publicar_post, _meta_token_valido, META_GRAPH

HOJE = "2026-05-21"

# id_hash -> {fb antigo, ig antigo (só p/ relatório de remoção manual)}
ANTIGOS = {
    "024d2403c8ef0d4f44c4e0ba5270d5401584ccd6": {  # Fenasul
        "fb": "105995162382818_1028576326795310", "ig": "18112634395879527"},
    "666340ab1a91f60b7ea9badf39ae6dcb82b40f71": {  # IR Venâncio
        "fb": "105995162382818_1028578196795123", "ig": "17888940048374754"},
    "2e166c784f3e61c919ebe50cea48f022ee37105e": {  # Vinícola Aurora
        "fb": "105995162382818_1028578466795096", "ig": "18091616159196620"},
    "6b80d389f02bc58f4cb0286f35d1d601edc895d2": {  # Sulgás
        "fb": "105995162382818_1028578983461711", "ig": "17929971423270323"},
}


def _deletar_fb(post_id: str, token: str) -> bool:
    try:
        r = requests.delete(f"{META_GRAPH}/{post_id}",
                            params={"access_token": token}, timeout=60)
        ok = r.status_code == 200 and r.json().get("success", True)
        print(f"[del-fb] {post_id} -> {r.status_code} {r.text[:120]}")
        return bool(ok)
    except Exception as e:
        print(f"[del-fb] erro: {e}")
        return False


def main():
    h = sys.argv[1] if len(sys.argv) > 1 else ""
    if h not in ANTIGOS:
        print(f"id_hash inválido: {h!r}")
        sys.exit(2)

    pauta = json.loads((ROOT / "state" / f"pauta_{HOJE}.json").read_text())["pauta"]
    valid = {f.name for f in fields(MateriaPronta)}
    d = next(x for x in pauta if x["id_hash"] == h)
    m = MateriaPronta(**{k: v for k, v in d.items() if k in valid})

    print(f"=== Republicando: {d['titulo_sultv'][:60]} ===")
    res = publicar_post(m)            # novo FB + novo IG, legenda corrigida
    print(f"[novo] {res}")

    token = _meta_token_valido()
    if res and "fb:" in (res or "") and token:
        # novo FB subiu -> remove o antigo sem texto
        _deletar_fb(ANTIGOS[h]["fb"], token)
    else:
        print("[del-fb] PULADO — novo FB não confirmado; antigo mantido p/ não perder presença")

    print(f"[ig-antigo] remover manualmente no app: media_id={ANTIGOS[h]['ig']}")


if __name__ == "__main__":
    main()
