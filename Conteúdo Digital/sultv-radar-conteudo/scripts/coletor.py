"""
coletor.py — coleta unificada das 118 fontes
=============================================
Lê o banco de fontes (banco_fontes.json), dispatcha para o coletor adequado
(RSS / API / Scraping HTML / X/Twitter / PDF) e devolve lista de MateriaBruta.

Roda em paralelo (ThreadPoolExecutor) com cap de 16 workers.
"""
from __future__ import annotations
import hashlib
import json
import re
import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse

import feedparser
import requests
from bs4 import BeautifulSoup

from curador import MateriaBruta

# feedparser.parse(url) usa urllib SEM timeout e pode travar indefinidamente em
# rede lenta. Um timeout default de socket garante que cada fetch RSS aborte
# sozinho, mesmo dentro do feedparser (Donário 2026-06-01).
socket.setdefaulttimeout(12)

ROOT = Path(__file__).resolve().parent.parent
BANCO_FONTES = ROOT / "scripts" / "banco_fontes.json"
USER_AGENT = "Mozilla/5.0 (compatible; SulTVRadar/1.0; +https://www.sultv.com.br)"
TIMEOUT = 20
MAX_WORKERS = 16


def canonical_url(url: str) -> str:
    p = urlparse(url.lower().strip())
    qs = "&".join(q for q in (p.query or "").split("&")
                  if not q.startswith(("utm_", "fbclid", "gclid", "ref=")))
    return urlunparse((p.scheme, p.netloc, p.path.rstrip("/"), "", qs, ""))


def url_hash(url: str) -> str:
    return hashlib.sha1(canonical_url(url).encode()).hexdigest()


def carregar_banco() -> list[dict]:
    return json.loads(BANCO_FONTES.read_text(encoding="utf-8"))


# ============================================================
# Coletores específicos
# ============================================================

def _coletar_rss(fonte: dict) -> list[MateriaBruta]:
    # Prefere o feed_url validado (Donário 2026-06-01); cai p/ url da homepage.
    feed_url = (fonte.get("feed_url") or "").strip() or fonte["url"]
    feed = feedparser.parse(feed_url, agent=USER_AGENT)
    out = []
    for entry in feed.entries[:50]:
        url = entry.get("link", "")
        if not url:
            continue
        out.append(MateriaBruta(
            id_hash=url_hash(url),
            coletado_em=datetime.now(timezone.utc).isoformat(),
            bloco=fonte["bloco"],
            fonte_id=fonte["id"],
            fonte_nome=fonte["nome"],
            cidade=fonte.get("cidade", ""),
            titulo=entry.get("title", "")[:300],
            resumo=BeautifulSoup(entry.get("summary", "") or "", "html.parser").get_text()[:1000],
            url=url,
            publicado_em=entry.get("published", "") or entry.get("updated", "") or "",
            score_fonte=fonte["score"],
        ))
    return out


def _coletar_scraping(fonte: dict) -> list[MateriaBruta]:
    """Scraping leve — pega <article> e <h2><a> do índice. Cada site exige tunning."""
    try:
        r = requests.get(fonte["url"], headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT)
        r.raise_for_status()
    except Exception:
        return []
    soup = BeautifulSoup(r.text, "html.parser")
    out = []
    # Heurística genérica — em produção, parser específico por fonte
    for art in soup.find_all(["article", "li", "div"], class_=lambda c: c and any(k in c for k in ["post", "news", "noticia", "card"]))[:30]:
        a = art.find("a", href=True)
        h = art.find(["h2", "h3", "h1"])
        if not a or not h:
            continue
        url = a["href"]
        if url.startswith("/"):
            base = "{0.scheme}://{0.netloc}".format(urlparse(fonte["url"]))
            url = base + url
        titulo = h.get_text(strip=True)[:300]
        if len(titulo) < 15:
            continue
        out.append(MateriaBruta(
            id_hash=url_hash(url),
            coletado_em=datetime.now(timezone.utc).isoformat(),
            bloco=fonte["bloco"],
            fonte_id=fonte["id"],
            fonte_nome=fonte["nome"],
            cidade=fonte.get("cidade", ""),
            titulo=titulo,
            resumo=art.get_text(" ", strip=True)[:800],
            url=url,
            publicado_em="",
            score_fonte=fonte["score"],
        ))
    return out


def _coletar_api_inmet(fonte: dict) -> list[MateriaBruta]:
    """Exemplo de coletor de API específica — INMET previsão por município RS."""
    # Stub — implementação completa requer endpoint específico
    return []


def _coletar_x(fonte: dict) -> list[MateriaBruta]:
    """X/Twitter via proxy nitter ou X API. Stub neste arquivo."""
    return []


def _coletar_pdf(fonte: dict) -> list[MateriaBruta]:
    """Boletins SEAPI/COPAAERGS em PDF. Stub neste arquivo."""
    return []


# ============================================================
# Scraper de prefeituras municipais (Donário 2026-06-01)
# ============================================================
# Sites de prefeituras das cidades-núcleo usam CMS distintos (Atende.net,
# portal próprio, etc.), mas os links de matéria seguem padrões reconhecíveis:
#   /noticia/view/<id>/<slug>            (Arambaré)
#   /noticias/<slug>                     (Cristal, Sentinela do Sul)
#   /portal/noticias/.../<id>/<slug>     (São Lourenço, Tapes)
#   /site/noticias/<secao>/<id>-<slug>   (Chuvisca)
#   /noticiasView/<id>_<slug>            (Barra do Ribeiro)
_PREF_NOISE = [
    re.compile(r'^foto de capa da not[ií]cia:\s*', re.I),
    re.compile(r'^h[áa]\s+\d+\s*(hora|dia|minuto|m[eê]s|ano)s?(\s+atr[áa]s)?', re.I),
    re.compile(r'\b\d{2}/\d{2}/\d{4}\b'),          # datas dd/mm/aaaa
    re.compile(r'^[A-Z]{3}\d{2}'),                 # códigos tipo JUN01 (colado ou não)
]


def _pref_limpa_titulo(t: str) -> str:
    t = " ".join((t or "").split())
    for _ in range(3):
        for rgx in _PREF_NOISE:
            t = rgx.sub("", t).strip()
    return t


def _pref_eh_item(href: str) -> bool:
    if not re.search(r'notici', href, re.I):
        return False
    low = href.lower().rstrip("/")
    if low.endswith(("/noticia", "/noticias", "/cidadao/noticia")):
        return False  # listagem/índice, não item
    tail = href.rstrip("/").split("/")[-1]
    return len(tail) >= 10 and re.search(r'[a-zçãéíóâêõ]{4}', tail.lower()) is not None


def _coletar_prefeitura(fonte: dict) -> list[MateriaBruta]:
    """Coleta as matérias da página de notícias de uma prefeitura municipal.

    `fonte["url"]` deve apontar para a LISTAGEM de notícias. O título bruto pode
    vir com ruído (categoria/data) — a angulação (fase 4) reescreve o titulo_sultv.
    """
    try:
        r = requests.get(fonte["url"], headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT)
        r.raise_for_status()
    except Exception:
        return []
    soup = BeautifulSoup(r.text, "html.parser")
    p = urlparse(fonte["url"])
    base = f"{p.scheme}://{p.netloc}"
    out, seen = [], set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not _pref_eh_item(href):
            continue
        full = urljoin(base, href)
        if full in seen:
            continue
        titulo = _pref_limpa_titulo(a.get_text(strip=True) or a.get("title") or "")
        if len(titulo) < 15:
            img = a.find("img")
            if img and img.get("alt"):
                titulo = _pref_limpa_titulo(img["alt"])
        if len(titulo) < 15:
            h = a.find(["h1", "h2", "h3", "h4"])
            if h:
                titulo = _pref_limpa_titulo(h.get_text(strip=True))
        if len(titulo) < 15:
            continue
        seen.add(full)
        out.append(MateriaBruta(
            id_hash=url_hash(full),
            coletado_em=datetime.now(timezone.utc).isoformat(),
            bloco=fonte["bloco"],
            fonte_id=fonte["id"],
            fonte_nome=fonte["nome"],
            cidade=fonte.get("cidade", ""),
            titulo=titulo[:300],
            resumo="",
            url=full,
            publicado_em="",
            score_fonte=fonte["score"],
        ))
    return out[:30]


# ============================================================
# Dispatcher
# ============================================================

def _dispatch(fonte: dict) -> list[MateriaBruta]:
    metodo = fonte.get("metodo", "")
    try:
        if "Prefeitura" in metodo:
            return _coletar_prefeitura(fonte)
        if "RSS" in metodo and "API" not in metodo:
            return _coletar_rss(fonte)
        if "API" in metodo and "RSS" not in metodo:
            return _coletar_api_inmet(fonte) if "INMET" in fonte["nome"] else []
        if "RSS + API" in metodo:
            return _coletar_rss(fonte)
        if "X API" in metodo or "Twitter" in metodo:
            return _coletar_x(fonte)
        if "PDF" in metodo:
            return _coletar_pdf(fonte)
        if "Scraping" in metodo:
            return _coletar_scraping(fonte)
        if "Stream" in metodo or "Histórico" in metodo or "Newsletter" in metodo:
            return []  # fora de escopo do Passo 2
        return _coletar_scraping(fonte)
    except Exception as e:
        print(f"[coletor] FALHA em {fonte['nome']}: {e}")
        return []


def coletar_todas_fontes() -> list[MateriaBruta]:
    fontes = carregar_banco()
    out: list[MateriaBruta] = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(_dispatch, f): f for f in fontes}
        for fut in as_completed(futures):
            out.extend(fut.result())
            time.sleep(0.05)  # leve back-off para evitar saturar saída
    return out
