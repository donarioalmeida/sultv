#!/usr/bin/env python3
"""
wix_dedup.py — dedup pré-publicação no Wix Blog (ponto crítico Donário 2026-05-16).

Antes de criar/publicar uma matéria, verifica DUAS fontes de verdade:

1. **Histórico local persistente** (state/historico_publicacoes.json)
   Toda matéria que o Radar já publicou no Wix fica registrada aqui — com
   id_hash da fonte, URL original, título original, título normalizado,
   post_id Wix e timestamp. Permite detectar:
   - mesma URL fonte (id_hash idêntico)
   - mesmo título institucional (norm)
   - mesma URL canônica da fonte (mesmo que o id_hash mude por mudança de tracking)

2. **Wix Blog (consulta online)** via `POST /blog/v3/posts/query`
   Bate o título contra os posts publicados — `$eq` (exato) e `$contains`
   (fuzzy com slug do título). É a rede de segurança final caso o histórico
   local tenha sido perdido ou esteja desatualizado.

Se qualquer das duas reportar duplicata, a função `checar_duplicata()` retorna
o motivo + URL existente. O `produzir_materia.publicar_materia_com_texto`
deve consultar isso ANTES de criar o draft post.
"""
from __future__ import annotations
import json
import os
import re
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests


ROOT = Path(__file__).resolve().parent.parent
HISTORICO_PATH = ROOT / "state" / "historico_publicacoes.json"
WIX_API_BASE = "https://www.wixapis.com/blog/v3"

# Janela "recente": títulos publicados nos últimos N dias contam como duplicata.
# Acima disso, mesmo título pode ser republicado (raridade, mas legítimo —
# ex.: campanha do agasalho de Pelotas ano que vem).
JANELA_DEDUP_DIAS = 365


# ============================================================
# Normalização
# ============================================================

_STOPWORDS = {"a","o","os","as","e","é","de","do","da","dos","das","no","na",
              "nos","nas","em","um","uma","uns","umas","para","por","com","sem",
              "que","se","ao","aos","à","às","já","também","mas","ou"}


def _normalizar_titulo(s: str) -> str:
    """Normaliza título para comparação fuzzy: lowercase, sem acentos, sem pontuação,
    sem stopwords, espaços colapsados."""
    if not s:
        return ""
    s = s.lower().strip()
    # remove acentuação básica (mantém ç → c)
    s = (s.replace("á","a").replace("à","a").replace("â","a").replace("ã","a")
           .replace("é","e").replace("ê","e")
           .replace("í","i")
           .replace("ó","o").replace("ô","o").replace("õ","o")
           .replace("ú","u").replace("ü","u")
           .replace("ç","c"))
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    palavras = [w for w in s.split() if w and w not in _STOPWORDS]
    return " ".join(palavras)


def _canonical_url(url: str) -> str:
    """Versão canônica da URL fonte (sem tracking params, sem trailing slash)."""
    if not url:
        return ""
    p = urllib.parse.urlparse(url.lower().strip())
    qs = "&".join(q for q in (p.query or "").split("&")
                  if not q.startswith(("utm_", "fbclid", "gclid", "ref=")))
    return urllib.parse.urlunparse((p.scheme, p.netloc,
                                     p.path.rstrip("/"), "", qs, ""))


# ============================================================
# Histórico local persistente
# ============================================================

def carregar_historico() -> list[dict]:
    """Lê state/historico_publicacoes.json. Retorna lista de dicts (vazia se não existir)."""
    if not HISTORICO_PATH.exists():
        return []
    try:
        data = json.loads(HISTORICO_PATH.read_text(encoding="utf-8"))
        return data.get("publicacoes", []) if isinstance(data, dict) else data
    except Exception as e:
        print(f"[wix_dedup] erro lendo histórico: {e}")
        return []


def registrar_publicacao(m, post_id_wix: str, post_url: str,
                          titulo_publicado: str = "") -> None:
    """Append-only: registra a publicação no histórico após sucesso no Wix."""
    HISTORICO_PATH.parent.mkdir(parents=True, exist_ok=True)
    historico = carregar_historico()

    entry = {
        "id_hash": getattr(m, "id_hash", ""),
        "url_fonte": _canonical_url(getattr(m, "url", "")),
        "titulo_original": getattr(m, "titulo", ""),
        "titulo_sultv": titulo_publicado or getattr(m, "titulo_sultv", ""),
        "titulo_normalizado": _normalizar_titulo(
            titulo_publicado or getattr(m, "titulo_sultv", "") or
            getattr(m, "titulo", "")
        ),
        "fonte_nome": getattr(m, "fonte_nome", ""),
        "cidade": getattr(m, "cidade", ""),
        "post_id_wix": post_id_wix,
        "post_url": post_url,
        "publicado_em": datetime.now(timezone.utc).isoformat(),
    }
    historico.append(entry)
    payload = {
        "ultimo_update": datetime.now(timezone.utc).isoformat(),
        "total": len(historico),
        "publicacoes": historico,
    }
    HISTORICO_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[wix_dedup] registrado no histórico: {post_id_wix} "
          f"({entry['titulo_normalizado'][:60]})")


def _dias_desde(iso_ts: str) -> float:
    try:
        ts = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - ts).total_seconds() / 86400.0
    except Exception:
        return 9999.0


def _checar_historico_local(m) -> Optional[dict]:
    """Procura match no histórico local. Retorna o entry existente ou None.

    Critérios (qualquer um já basta):
    - id_hash idêntico
    - url_fonte canônica idêntica
    - titulo_normalizado idêntico (publicado há ≤ JANELA_DEDUP_DIAS dias)
    """
    historico = carregar_historico()
    if not historico:
        return None

    id_hash = getattr(m, "id_hash", "")
    url_canon = _canonical_url(getattr(m, "url", ""))
    titulo_norm = _normalizar_titulo(
        getattr(m, "titulo_sultv", "") or getattr(m, "titulo", "")
    )

    for entry in historico:
        if id_hash and entry.get("id_hash") == id_hash:
            return {**entry, "match": "id_hash"}
        if url_canon and entry.get("url_fonte") == url_canon:
            return {**entry, "match": "url_canonica"}
        if titulo_norm and entry.get("titulo_normalizado") == titulo_norm:
            if _dias_desde(entry.get("publicado_em", "")) <= JANELA_DEDUP_DIAS:
                return {**entry, "match": "titulo_normalizado"}
    return None


# ============================================================
# Consulta online no Wix Blog
# ============================================================

def _wix_headers() -> dict:
    token = os.getenv("WIX_SITE_TOKEN", "").strip()
    if not token or token.endswith("...") or len(token) < 30:
        return {}
    h = {"Authorization": token, "Content-Type": "application/json"}
    site_id = os.getenv("WIX_SITE_ID", "").strip()
    if site_id:
        h["wix-site-id"] = site_id
    return h


def _consultar_wix_por_titulo(titulo: str, modo: str = "eq") -> list[dict]:
    """POST /blog/v3/posts/query — devolve lista de posts (até 5) por título.

    `modo` ∈ {"eq", "contains", "starts_with"}.
    """
    h = _wix_headers()
    if not h:
        return []
    op = {"eq": "$eq", "contains": "$contains", "starts_with": "$startsWith"}.get(modo, "$eq")
    body = {
        "filter": {"title": {op: titulo}},
        "paging": {"limit": 5, "offset": 0},
        "fieldsets": ["URL"],
    }
    try:
        r = requests.post(f"{WIX_API_BASE}/posts/query",
                          headers=h, json=body, timeout=12)
        if r.status_code == 404:
            return []
        r.raise_for_status()
        return r.json().get("posts", []) or []
    except Exception as e:
        print(f"[wix_dedup] consulta Wix falhou ({modo}): {e}")
        return []


def _consultar_wix(titulo: str) -> Optional[dict]:
    """Procura post publicado no Wix com o mesmo título.

    Tenta exato primeiro (case-sensitive limitação do Wix Query). Se nada,
    tenta `$contains` com as 6 primeiras palavras significativas (segmento mais
    discriminante do título). Retorna o post existente ou None.
    """
    if not titulo:
        return None

    # 1. Match exato (case-sensitive)
    posts = _consultar_wix_por_titulo(titulo, modo="eq")
    if posts:
        return {**posts[0], "match": "wix_titulo_eq"}

    # 2. Match starts_with usando os primeiros ~50 chars (Wix é case-sensitive
    # então variações de capitalização não pegam no $eq; starts_with com prefixo
    # mais discriminante costuma resolver)
    prefix = titulo[:50].strip()
    if prefix and prefix != titulo:
        posts = _consultar_wix_por_titulo(prefix, modo="starts_with")
        if posts:
            return {**posts[0], "match": "wix_titulo_starts_with"}

    # 3. Match contains com segmento mais discriminante (4-6 palavras)
    norm = _normalizar_titulo(titulo)
    palavras = norm.split()
    if len(palavras) >= 4:
        # Usa as 4 palavras mais "raras" — heurística simples: descarta as
        # palavras genéricas conhecidas e pega as do meio do título
        segmento = " ".join(palavras[1:5])
        if segmento and segmento != norm:
            posts = _consultar_wix_por_titulo(segmento, modo="contains")
            if posts:
                # Confirma com normalização para evitar falsos positivos
                for p in posts:
                    p_norm = _normalizar_titulo(p.get("title", ""))
                    sobreposicao = set(norm.split()) & set(p_norm.split())
                    if len(sobreposicao) >= max(4, len(norm.split()) // 2):
                        return {**p, "match": "wix_titulo_contains_fuzzy"}
    return None


# ============================================================
# API pública
# ============================================================

def checar_duplicata(m, titulo_publicar: str = "") -> Optional[dict]:
    """Decide se a matéria é duplicata. Retorna dict com motivo + URL existente
    ou None se for nova.

    Faz na ordem: histórico local → Wix online. Para na primeira positiva.

    `titulo_publicar` (opcional) é o titulo_sultv reescrito que vai ser
    enviado ao Wix — quando não informado, usa `m.titulo_sultv` ou `m.titulo`.
    """
    # 1. Local
    local = _checar_historico_local(m)
    if local:
        return {
            "fonte": "historico_local",
            "match": local.get("match"),
            "post_id": local.get("post_id_wix"),
            "post_url": local.get("post_url"),
            "publicado_em": local.get("publicado_em"),
            "titulo_existente": local.get("titulo_sultv") or local.get("titulo_original"),
        }

    # 2. Wix online
    titulo = (titulo_publicar or getattr(m, "titulo_sultv", "") or
              getattr(m, "titulo", "")).strip()
    if titulo:
        online = _consultar_wix(titulo)
        if online:
            slug = online.get("slug", "")
            return {
                "fonte": "wix_online",
                "match": online.get("match"),
                "post_id": online.get("id"),
                "post_url": online.get("url", {}).get("base", "") + "/" +
                            online.get("url", {}).get("path", "") if online.get("url") else f"https://www.sultv.com.br/post/{slug}",
                "titulo_existente": online.get("title"),
            }

    return None


# ============================================================
# CLI helpers
# ============================================================

def backfill_de_pauta(pauta_path: str, urls_publicadas: dict) -> int:
    """Popula o histórico com publicações antigas a partir de state/pauta_<date>.json.

    `urls_publicadas` é dict {id_hash: post_url} — geralmente extraído manualmente
    do log de execução do dia ou da resposta do Wix.

    Retorna número de entradas adicionadas.
    """
    pauta = json.loads(Path(pauta_path).read_text(encoding="utf-8"))
    items = pauta.get("pauta", [])
    historico = carregar_historico()
    ids_existentes = {e["id_hash"] for e in historico if e.get("id_hash")}
    n = 0
    for it in items:
        if it.get("decisao_final") != "PUBLICAR":
            continue
        h = it["id_hash"]
        if h in ids_existentes:
            continue
        url_publicada = urls_publicadas.get(h)
        if not url_publicada:
            continue
        post_id = url_publicada.rstrip("/").split("/")[-1]
        entry = {
            "id_hash": h,
            "url_fonte": _canonical_url(it.get("url", "")),
            "titulo_original": it.get("titulo", ""),
            "titulo_sultv": it.get("titulo_sultv", ""),
            "titulo_normalizado": _normalizar_titulo(
                it.get("titulo_sultv") or it.get("titulo", "")
            ),
            "fonte_nome": it.get("fonte_nome", ""),
            "cidade": it.get("cidade", ""),
            "post_id_wix": post_id,
            "post_url": url_publicada,
            "publicado_em": pauta.get("gerado_em", datetime.now(timezone.utc).isoformat()),
        }
        historico.append(entry)
        n += 1

    if n:
        HISTORICO_PATH.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "ultimo_update": datetime.now(timezone.utc).isoformat(),
            "total": len(historico),
            "publicacoes": historico,
        }
        HISTORICO_PATH.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    return n


if __name__ == "__main__":
    import sys
    if "--dump" in sys.argv:
        h = carregar_historico()
        print(json.dumps(h[-10:], ensure_ascii=False, indent=2))
        print(f"\nTotal: {len(h)} publicações")
    else:
        print(f"Histórico em {HISTORICO_PATH}")
        h = carregar_historico()
        print(f"Total: {len(h)} publicações registradas")
