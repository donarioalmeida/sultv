#!/usr/bin/env python3
"""coleta_instagram.py — coleta posts de contas Instagram da watchlist via
Business Discovery API (Meta Graph) e MERGE em state/candidatos_<date>.json.

Criado em 2026-06-06 a pedido de Donário ("incluir @ de usuários Instagram").

Como funciona:
- Lê state/instagram_watchlist.json (handles + cidade + tipo + score_fonte)
- Para cada handle, chama business_discovery com o token Meta da SulTV
  (só funciona para contas COMERCIAIS/CRIADOR; pessoais retornam erro)
- Filtra posts das últimas RADAR_IG_JANELA_H horas (default 48)
- Normaliza cada post para o formato de candidato do Radar
  (titulo = 1ª linha da caption; resumo = caption; url = permalink)
- Faz merge dedupado (id_hash) em state/candidatos_<date>.json

Requisito de token (corrigido 2026-06-07): a Business Discovery exige um
**USER token** (não Page token) com os escopos `instagram_basic` +
`instagram_manage_insights` + `pages_read_engagement`. O script usa
META_BD_USER_TOKEN do .env (token de usuário long-lived, ~60 dias) e cai
para META_LONG_LIVED_TOKEN apenas como fallback. Sem o escopo/tipo certo a
API devolve erro #10 — o script avisa e sai sem quebrar a coleta.

Uso (após coleta_deadline.py, antes de classificar_cowork.py):
  PYTHONPATH=/tmp/pylibs python3 scripts/coleta_instagram.py
"""
from __future__ import annotations
import json, os, sys, hashlib
from datetime import datetime, timezone, timedelta
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent.parent
HOJE = datetime.now(timezone.utc).date().isoformat()
WATCHLIST = ROOT / "state" / "instagram_watchlist.json"
CANDIDATOS = ROOT / "state" / f"candidatos_{HOJE}.json"
JANELA_H = int(os.getenv("RADAR_IG_JANELA_H", "48"))

for raw in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
    line = raw.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

TOKEN = os.environ.get("META_BD_USER_TOKEN", "") or os.environ.get("META_LONG_LIVED_TOKEN", "")
IG_ID = os.environ.get("META_IG_BUSINESS_ID", "17841457371532451")


def _post_para_candidato(post: dict, conta: dict) -> dict:
    caption = (post.get("caption") or "").strip()
    linhas = [l.strip() for l in caption.splitlines() if l.strip()]
    titulo = (linhas[0] if linhas else "(post sem legenda)")[:140]
    url = post.get("permalink", "")
    return {
        "id_hash": hashlib.sha1(url.encode()).hexdigest(),
        "coletado_em": datetime.now(timezone.utc).isoformat(),
        "bloco": "D",
        "fonte_id": 900,  # faixa 900+ reservada para Instagram watchlist
        "fonte_nome": f"Instagram @{conta['handle']}",
        "cidade": conta.get("cidade", "RS"),
        "titulo": titulo,
        "resumo": caption[:800],
        "url": url,
        "publicado_em": post.get("timestamp", ""),
        "score_fonte": conta.get("score_fonte", 18),
    }


def main():
    if not TOKEN:
        print("[ig] META_LONG_LIVED_TOKEN ausente — pulando coleta Instagram")
        return
    wl = json.loads(WATCHLIST.read_text(encoding="utf-8"))
    contas = wl.get("contas", [])
    if not contas:
        print("[ig] watchlist vazia — nada a coletar")
        return

    corte = datetime.now(timezone.utc) - timedelta(hours=JANELA_H)
    novos, erros = [], 0
    for conta in contas:
        h = conta["handle"]
        params = {
            "fields": (f"business_discovery.username({h})"
                       "{username,media.limit(10){caption,permalink,timestamp}}"),
            "access_token": TOKEN,
        }
        try:
            r = requests.get(f"https://graph.facebook.com/v21.0/{IG_ID}",
                             params=params, timeout=20)
        except Exception as e:
            print(f"[ig] @{h}: exceção {e}")
            erros += 1
            continue
        if r.status_code != 200:
            msg = r.json().get("error", {}).get("message", r.text[:80])
            if "(#10)" in msg or "permission" in msg.lower():
                print(f"[ig] @{h}: sem permissão (#10) — token precisa de "
                      "instagram_basic + business_management. Abortando coleta IG.")
                return
            print(f"[ig] @{h}: HTTP {r.status_code} {msg[:80]}")
            erros += 1
            continue
        media = (r.json().get("business_discovery", {})
                 .get("media", {}).get("data", []))
        cont = 0
        for post in media:
            ts = post.get("timestamp", "")
            try:
                dt = datetime.fromisoformat(ts.replace("+0000", "+00:00"))
            except Exception:
                continue
            if dt < corte:
                continue
            novos.append(_post_para_candidato(post, conta))
            cont += 1
        print(f"[ig] @{h}: {cont} posts na janela de {JANELA_H}h")

    if not novos:
        print(f"[ig] nenhum post novo nas contas da watchlist ({erros} erros)")
        return

    # merge dedupado nos candidatos do dia
    if CANDIDATOS.exists():
        data = json.loads(CANDIDATOS.read_text(encoding="utf-8"))
        itens = data.get("candidatos") or data.get("itens") or []
        chave = "candidatos" if "candidatos" in data else ("itens" if "itens" in data else None)
    else:
        data, itens, chave = {"data": HOJE, "candidatos": []}, [], "candidatos"
    vistos = {i["id_hash"] for i in itens}
    add = [n for n in novos if n["id_hash"] not in vistos]
    itens.extend(add)
    if chave:
        data[chave] = itens
    data["total"] = len(itens)
    CANDIDATOS.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[ig] merge: +{len(add)} candidatos Instagram -> {CANDIDATOS.name} (total {len(itens)})")


if __name__ == "__main__":
    main()
