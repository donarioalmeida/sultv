#!/usr/bin/env python3
"""
buscar_imagem_limpa.py — obtém uma imagem REAL representativa para a matéria,
sem nenhum overlay de texto, e gera variantes por formato de cada plataforma.

Estratégia em cascata (conceito Donário 2026-06-16 — TEMA primeiro, ancorado
no Sul do RS / Costa Doce, sem nenhum marcador estrangeiro):
  1. IA gratuita Pollinations (FLUX) — FONTE PRIMÁRIA, prompt travado no
     interior do RS + negativos (sem texto/placa/adesivagem/país estrangeiro)
  2. Gemini Imagen / 3. OpenAI — reforço de IA (se houver créditos; ancorados)
  4. og:image da fonte — só passa pelo filtro anti-texto/anti-estrangeiro (OCR)
  5. acervo livre (Wikimedia/Openverse) com query PT + âncora regional, filtrado
  6. Pexels / Unsplash (stock) — filtrados
  7. Card gráfico SulTV (gradiente liso, sem texto) — último recurso

A imagem reflete o TEMA com ambientação inconfundivelmente gaúcha; a cidade é
reforçada na legenda e no alt text. Fotos reais com texto embutido (banner,
placa, adesivagem de carro, idioma não-português) são REJEITADAS por OCR.

Retorna sempre {bytes, mime, width, height, fonte_credito, alt_text,
variantes: {wix_cover, fb_feed, ig_feed, ig_story?}}.

NUNCA grava texto sobre a imagem. O título e a legenda ficam no Wix
como nó CAPTION SEPARADO, e nas redes ficam na caption do post.

Variáveis de ambiente:
  - PEXELS_API_KEY (opcional)
  - UNSPLASH_ACCESS_KEY (opcional)
  - GEMINI_API_KEY (opcional, Google AI Studio — Imagen 4)
  - OPENAI_API_KEY (opcional, OpenAI — gpt-image-1 ou dall-e-3)
  - IMAGE_GEN_PRIMARY ("gemini" ou "openai", default="gemini")
  - IMAGE_GEN_MODEL_GEMINI (default="imagen-4.0-generate-001";
                            alternativas: imagen-4.0-fast-generate-001,
                            imagen-4.0-ultra-generate-001)
  - IMAGE_GEN_MODEL_OPENAI (default="gpt-image-1"; fallback="dall-e-3")
"""
from __future__ import annotations
import base64
import io
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional

USER_AGENT = "Mozilla/5.0 SulTV-Radar/1.0 (clean-image-fetcher)"
TIMEOUT = 15

# --------------------------------------------------------------------------
# Variantes por formato — dimensões finais por plataforma
# --------------------------------------------------------------------------
FORMATOS = {
    "wix_cover": (1600, 900),    # 16:9 horizontal editorial (cover do post)
    "wix_inline": (1200, 675),   # 16:9 menor (imagem dentro do corpo)
    "fb_feed": (1200, 630),      # 1.91:1 — máximo alcance orgânico Facebook
    "ig_feed": (1080, 1350),     # 4:5 — máximo real estate IG feed
    "ig_quadrado": (1080, 1080), # 1:1 — alternativa IG/FB
    "ig_story": (1080, 1920),    # 9:16 — Stories/Reels capa
}

# Cidades-núcleo SulTV — IA generativa entra antes do stock
CIDADES_NUCLEO = {
    "arambaré", "arambare", "tapes", "camaquã", "camaqua",
    "cristal", "chuvisca", "são lourenço do sul", "sao lourenco do sul",
    "dom feliciano", "barra do ribeiro",
}

# Tags onde og:image geralmente é boa (instituições com sites bem mantidos)
TAGS_OG_PREFERIDO = {"agro", "evento", "economia"}


# ============================================================
# HTTP helpers
# ============================================================
def _http_get(url: str, timeout: int = TIMEOUT,
              headers: dict | None = None) -> Optional[bytes]:
    try:
        h = {"User-Agent": USER_AGENT}
        if headers:
            h.update(headers)
        req = urllib.request.Request(url, headers=h)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except Exception:
        return None


def _http_get_json(url: str, headers: dict | None = None) -> Optional[dict]:
    import json as _json
    raw = _http_get(url, headers=headers)
    if not raw:
        return None
    try:
        return _json.loads(raw)
    except Exception:
        return None


def _image_size(raw: bytes) -> tuple[int, int]:
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(raw))
        return im.size
    except Exception:
        return (1200, 630)


# ============================================================
# Quality gates
# ============================================================
def _qualidade_minima(raw: bytes, min_lado: int = 1100) -> bool:
    """Rejeita imagens muito pequenas ou corrompidas. min_lado é o menor lado."""
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(raw))
        w, h = im.size
        return min(w, h) >= min_lado
    except Exception:
        return False


def _tem_texto_evidente(raw: bytes) -> bool:
    """Heurística leve: imagens com aspecto muito quadrado e alta variação
    de contraste na faixa central tendem a ser cards com texto. Sem OCR,
    é só um filtro suave — vamos confiar no prompt 'no text' da geração."""
    return False  # placeholder — pode evoluir pra OCR via tesseract


# ============================================================
# Estratégia 1 — og:image da fonte original
# ============================================================
def _extrair_og_image(url_pagina: str) -> Optional[bytes]:
    """Busca a og:image declarada na página fonte. Retorna bytes ou None."""
    raw = _http_get(url_pagina, timeout=10)
    if not raw:
        return None
    html = raw.decode("utf-8", "ignore")[:200_000]
    patterns = [
        r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']',
        r'<meta\s+content=["\']([^"\']+)["\']\s+property=["\']og:image["\']',
        r'<meta\s+name=["\']twitter:image["\']\s+content=["\']([^"\']+)["\']',
    ]
    img_url = None
    for pat in patterns:
        m = re.search(pat, html, re.IGNORECASE)
        if m:
            img_url = m.group(1)
            break
    if not img_url:
        return None
    if img_url.startswith("//"):
        img_url = "https:" + img_url
    elif img_url.startswith("/"):
        u = urllib.parse.urlparse(url_pagina)
        img_url = f"{u.scheme}://{u.netloc}{img_url}"
    data = _http_get(img_url, timeout=12)
    if not data or len(data) < 8000:
        return None
    # Fix 2026-06-06: fotos de redação local raramente passam de 720p
    # (og típico: 1200x675, 1280x720, 899x506). O gate de 900px rejeitava
    # praticamente TODO og:image real e a cascata caía no gradiente liso
    # (posts FB/IG "chapados"). O _smart_crop já faz upscale LANCZOS para o
    # formato alvo, então 500px de menor lado é suficiente.
    if not _qualidade_minima(data, min_lado=500):
        return None
    return data


# ============================================================
# Estratégia 2 — Pexels (free tier)
# ============================================================
def _buscar_pexels(query: str, orientation: str = "landscape") -> Optional[dict]:
    """Retorna {bytes, fonte_credito, fonte_url} ou None."""
    key = os.getenv("PEXELS_API_KEY", "").strip()
    if not key:
        return None
    q = urllib.parse.quote(query)
    data = _http_get_json(
        f"https://api.pexels.com/v1/search?query={q}&per_page=8"
        f"&orientation={orientation}&size=large",
        headers={"Authorization": key},
    )
    if not data or not data.get("photos"):
        return None
    # Pega o primeiro que passar no quality gate
    for photo in data["photos"]:
        src_url = (photo["src"].get("large2x") or photo["src"].get("original")
                   or photo["src"].get("large"))
        raw = _http_get(src_url, timeout=20)
        if not raw or not _qualidade_minima(raw, min_lado=1100):
            continue
        return {
            "bytes": raw,
            "fonte_credito": f"Foto: {photo.get('photographer', 'Pexels')} via Pexels",
            "fonte_url": photo.get("url"),
        }
    return None


# ============================================================
# Estratégia 3 — Unsplash
# ============================================================
def _buscar_unsplash(query: str, orientation: str = "landscape") -> Optional[dict]:
    key = os.getenv("UNSPLASH_ACCESS_KEY", "").strip()
    if not key:
        return None
    q = urllib.parse.quote(query)
    data = _http_get_json(
        f"https://api.unsplash.com/search/photos?query={q}&per_page=8"
        f"&orientation={orientation}",
        headers={"Authorization": f"Client-ID {key}"},
    )
    if not data or not data.get("results"):
        return None
    for photo in data["results"]:
        src_url = photo["urls"].get("regular") or photo["urls"].get("full")
        raw = _http_get(src_url, timeout=20)
        if not raw or not _qualidade_minima(raw, min_lado=1100):
            continue
        photographer = photo.get("user", {}).get("name", "Unsplash")
        return {
            "bytes": raw,
            "fonte_credito": f"Foto: {photographer} / Unsplash",
            "fonte_url": photo.get("links", {}).get("html"),
        }
    return None


# ============================================================
# Estratégia 3b — Openverse + Wikimedia Commons (NOVO 2026-06-06)
# Fontes 100% gratuitas e SEM API key. Decisão Donário 2026-06-06:
# sem recarga do Gemini, esta é a rede de segurança antes do gradiente.
# Openverse indexa imagens CC; filtramos license_type=commercial e
# montamos crédito com autor + licença (atribuição obrigatória).
# ============================================================
def _buscar_openverse(query: str) -> Optional[dict]:
    q = urllib.parse.quote(query)
    data = _http_get_json(
        f"https://api.openverse.org/v1/images/?q={q}&license_type=commercial"
        f"&page_size=10&filter_dead=true&mature=false",
        headers={"User-Agent": USER_AGENT},
    )
    if not data or not data.get("results"):
        return None
    tentativas = 0
    for ph in data["results"]:
        w, h = ph.get("width") or 0, ph.get("height") or 0
        if w and h and (min(w, h) < 500 or w < h):  # paisagem, lado mínimo 500
            continue
        # Prefere a versão 'thumbnail' (menor, download rápido) quando ela
        # ainda for grande o bastante; senão usa a original.
        src = ph.get("url")
        if not src:
            continue
        # Limita o nº de downloads grandes por query (teto de 45s do bash Cowork)
        if tentativas >= 1:
            break
        tentativas += 1
        raw = _http_get(src, timeout=8)
        if not raw or not _qualidade_minima(raw, min_lado=500):
            continue
        autor = ph.get("creator") or "Openverse"
        lic = (ph.get("license") or "cc").upper()
        return {
            "bytes": raw,
            "fonte_credito": f"Foto: {autor} / Openverse ({lic})",
            "fonte_url": ph.get("foreign_landing_url") or src,
        }
    return None


def _buscar_wikimedia(query: str) -> Optional[dict]:
    q = urllib.parse.quote(query)
    data = _http_get_json(
        "https://commons.wikimedia.org/w/api.php?action=query&format=json"
        f"&generator=search&gsrsearch={q}%20filetype:bitmap&gsrnamespace=6"
        "&gsrlimit=10&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=1600",
        headers={"User-Agent": USER_AGENT},
    )
    pages = ((data or {}).get("query") or {}).get("pages") or {}
    candidatos = sorted(pages.values(), key=lambda p: p.get("index", 99))
    for p in candidatos:
        infos = p.get("imageinfo") or []
        if not infos:
            continue
        ii = infos[0]
        w, h = ii.get("width") or 0, ii.get("height") or 0
        if min(w, h) < 500 or w < h:
            continue
        src = ii.get("thumburl") or ii.get("url")
        raw = _http_get(src, timeout=18)
        if not raw or not _qualidade_minima(raw, min_lado=500):
            continue
        meta = ii.get("extmetadata") or {}
        autor = re.sub(r"<[^>]+>", "", (meta.get("Artist") or {}).get("value", "")).strip() or "Wikimedia Commons"
        lic = (meta.get("LicenseShortName") or {}).get("value", "CC")
        return {
            "bytes": raw,
            "fonte_credito": f"Foto: {autor[:60]} / Wikimedia Commons ({lic})",
            "fonte_url": ii.get("descriptionurl") or src,
        }
    return None


def _buscar_acervo_livre(queries: list[str]) -> Optional[dict]:
    """Openverse primeiro (curadoria melhor), Wikimedia como reforço.

    Limita às 2 primeiras queries para acotar o tempo total (teto de 45s
    do bash do Cowork) — cada download de acervo pode ser pesado.
    """
    qs = list(queries)[:2]
    # Wikimedia primeiro: devolve thumb já dimensionada (iiurlwidth=1600),
    # download rápido — cabe melhor no teto de 45s do bash Cowork.
    for q in qs:
        r = _buscar_wikimedia(q)
        if r:
            return r
    for q in qs:
        r = _buscar_openverse(q)
        if r:
            return r
    return None


# ============================================================
# Âncora regional Sul-RS + negativos (Donário 2026-06-16)
# ============================================================
# Conceito aprovado: TEMA primeiro, com ambientação inconfundivelmente do Sul
# do RS / Costa Doce; cidade reforçada na legenda/alt text. NUNCA imagem com
# lugar distante, outro país, ou elementos com texto/idioma não-português
# (banners, placas, adesivagem de carro, faixas). O prompt da IA fecha SEMPRE
# com a âncora regional e a lista de negativos abaixo.
_ANCORA_SUL = (
    "Scene set in the rural interior of Rio Grande do Sul, southern Brazil "
    "(Costa Doce / Pampa region). Authentic southern-Brazilian atmosphere: "
    "local Brazilian people, Brazilian small-town architecture and landscape, "
    "natural daylight, documentary editorial photojournalism, photo-realistic, "
    "wide-angle composition."
)
_NEGATIVOS_SUL = (
    "Absolutely no text, no captions, no letters, no words, no signage, "
    "no banners, no posters, no billboards, no car decals or vehicle wraps, "
    "no license plates, no logos, no watermarks, no writing of any kind. "
    "Do NOT depict foreign countries, foreign cities, USA, Europe, Asia, "
    "deserts, skyscrapers, English or Spanish signs, or any non-Brazilian "
    "setting."
)


def _cidade_display(cidade: str) -> str:
    """Nome limpo da cidade para reforço no prompt (sem sufixo de região)."""
    base = (cidade or "").split("/")[0].split(" - ")[0].strip()
    return base


def _prompt_ancorado_sul(prompt_imagem: str, cidade: str = "") -> str:
    """Monta o prompt final de geração SEMPRE ancorado no Sul do RS.

    tema (prompt_imagem) -> ambientação obrigatória do Sul -> negativos.
    A cidade entra como reforço textual ('near <cidade>, RS'), mas o peso
    visual é o tema + a estética regional (decisão Donário: tema primeiro).
    """
    cid = _cidade_display(cidade)
    ref_cidade = f" The setting resembles the town of {cid}, Rio Grande do Sul, Brazil." if cid else ""
    base = (prompt_imagem or "").strip().rstrip(".")
    return f"{base}. {_ANCORA_SUL}{ref_cidade} {_NEGATIVOS_SUL}"


# ============================================================
# OCR — filtro anti-texto / anti-estrangeiro (Donário 2026-06-16)
# ============================================================
# Donário: rejeitar imagens com banners, placas, adesivagem ou qualquer texto
# (que normalmente denuncia outro país/idioma). Usamos OCR (tesseract) para
# detectar texto embutido na imagem; se houver volume relevante de caracteres,
# a imagem é rejeitada — vale para foto de stock, og:image e acervo livre.
# A imagem gerada por IA já vem sem texto (prompt 'no text'), então o filtro
# protege principalmente as fontes de FOTO real.
def _texto_na_imagem(raw: bytes) -> int:
    """Retorna a quantidade aproximada de caracteres alfabéticos detectados
    por OCR na imagem. 0 se OCR indisponível ou imagem sem texto."""
    try:
        import pytesseract
        from PIL import Image
        im = Image.open(io.BytesIO(raw))
        if im.mode != "RGB":
            im = im.convert("RGB")
        # Reduz para acelerar o OCR (texto de placa/banner é grande o bastante)
        im.thumbnail((1000, 1000))
        txt = pytesseract.image_to_string(im, lang="por+eng")
        # Conta só letras (ignora ruído de pontuação/algarismos isolados)
        letras = re.sub(r"[^A-Za-zÀ-ÿ]", "", txt)
        return len(letras)
    except Exception:
        return 0


def _imagem_com_texto_demais(raw: bytes, limite: int = 12) -> bool:
    """True se a imagem tem texto embutido acima do limite (banner/placa/
    adesivagem/idioma estrangeiro). Limite baixo e tolerante a ruído de OCR."""
    return _texto_na_imagem(raw) >= limite


# ============================================================
# Estratégia 0 — IA gratuita Pollinations (FLUX) — PRIMÁRIA
# (Donário 2026-06-16: fonte primária, ancorada no Sul-RS, sem custo/sem chave)
# ============================================================
def _gerar_via_pollinations(prompt_imagem: str, cidade: str = "") -> Optional[dict]:
    """Gera imagem 16:9 via Pollinations.ai (FLUX) — grátis, sem API key.

    Endpoint: GET https://image.pollinations.ai/prompt/<prompt>?...
    Parâmetros: width/height (16:9), model=flux, nologo=true, seed estável.
    O prompt é SEMPRE ancorado no Sul-RS com negativos (sem texto/estrangeiro).
    Opcional: POLLINATIONS_TOKEN no .env (sk_) remove rate limit no servidor.
    """
    import hashlib
    prompt_final = _prompt_ancorado_sul(prompt_imagem, cidade)
    seed0 = int(hashlib.sha1(prompt_final.encode("utf-8")).hexdigest(), 16) % 100000
    token = os.getenv("POLLINATIONS_TOKEN", "").strip()

    # Até 3 tentativas (Donário 2026-06-16): OCR rígido na PRÓPRIA imagem
    # gerada — se o FLUX alucinar texto legível (placa, banner, adesivagem,
    # idioma estrangeiro), regenera com outra seed. Limite baixo (8) é mais
    # sensível; aceita ~1 regeração extra quando houver dúvida. Rabisco
    # ilegível não é pego pelo OCR e é tolerado.
    ultimo = None
    for tent in range(3):
        seed = (seed0 + tent * 4242) % 100000
        params = {"width": "1600", "height": "900",
                  "model": "flux", "nologo": "true", "seed": str(seed)}
        if token:
            params["token"] = token
        url = ("https://image.pollinations.ai/prompt/"
               + urllib.parse.quote(prompt_final)
               + "?" + urllib.parse.urlencode(params))
        raw = _http_get(url, timeout=40)
        if not raw or len(raw) < 15000:
            print("[buscar_imagem] Pollinations: resposta vazia/pequena")
            continue
        if raw[:3] != b"\xff\xd8\xff" and raw[:8] != b"\x89PNG\r\n\x1a\n" and raw[8:12] != b"WEBP":
            print("[buscar_imagem] Pollinations: payload não é imagem")
            continue
        ultimo = raw
        n_txt = _texto_na_imagem(raw)
        if n_txt < 8:
            return {"bytes": raw, "fonte_credito": "Imagem ilustrativa — IA (FLUX)", "fonte_url": ""}
        print(f"[buscar_imagem] Pollinations: texto legível ({n_txt} chars) detectado, regenerando (tent {tent+1}/3)")
    # Aceita a última como melhor esforço (variantes seguem sem overlay de texto SulTV)
    if ultimo:
        return {"bytes": ultimo, "fonte_credito": "Imagem ilustrativa — IA (FLUX)", "fonte_url": ""}
    return None


# ============================================================
# Estratégia 4 — Gemini Imagen 3
# ============================================================
def _gerar_via_gemini(prompt_imagem: str, cidade: str = "") -> Optional[dict]:
    """Gera imagem (landscape 16:9) via Imagen 4 do Google AI Studio.

    Modelo padrão: imagen-4.0-generate-001 (qualidade alta, ~3s).
    Alternativas via IMAGE_GEN_MODEL_GEMINI:
      - imagen-4.0-fast-generate-001 (rápido, menor custo)
      - imagen-4.0-ultra-generate-001 (qualidade premium)
    """
    api_key = os.getenv("GEMINI_API_KEY", "").strip() or os.getenv("GOOGLE_API_KEY", "").strip()
    if not api_key:
        return None
    model = os.getenv("IMAGE_GEN_MODEL_GEMINI", "imagen-4.0-generate-001").strip()
    import json as _json
    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        f"models/{model}:predict?key={api_key}"
    )
    body = _json.dumps({
        "instances": [{
            "prompt": _prompt_ancorado_sul(prompt_imagem, cidade),
        }],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "16:9",
            "safetyFilterLevel": "block_only_high",
            "personGeneration": "allow_adult",
        },
    }).encode("utf-8")
    try:
        req = urllib.request.Request(
            url, data=body, method="POST",
            headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
        )
        with urllib.request.urlopen(req, timeout=90) as r:
            payload = _json.loads(r.read())
        # Resposta: predictions[0].bytesBase64Encoded
        pred = payload.get("predictions", [{}])[0]
        b64 = pred.get("bytesBase64Encoded")
        if not b64:
            return None
        raw = base64.b64decode(b64)
        if len(raw) < 20000:
            return None
        return {
            "bytes": raw,
            "fonte_credito": f"Imagem ilustrativa — Gemini Imagen 4 ({model})",
            "fonte_url": "",
        }
    except urllib.error.HTTPError as e:
        print(f"[buscar_imagem] Gemini HTTP {e.code}: {e.read()[:200].decode('utf-8', 'ignore')}")
    except Exception as e:
        print(f"[buscar_imagem] Gemini falhou: {e}")
    return None


# ============================================================
# Estratégia 5 — OpenAI (gpt-image-1 ou dall-e-3)
# ============================================================
def _gerar_via_openai(prompt_imagem: str, cidade: str = "") -> Optional[dict]:
    """Gera imagem via OpenAI. Tenta gpt-image-1 primeiro, fallback dall-e-3."""
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        return None
    model = os.getenv("IMAGE_GEN_MODEL_OPENAI", "gpt-image-1").strip()
    prompt_completo = _prompt_ancorado_sul(prompt_imagem, cidade)
    import json as _json
    for tentativa_model in (model, "dall-e-3"):
        body_dict = {
            "model": tentativa_model,
            "prompt": prompt_completo,
            "n": 1,
        }
        if tentativa_model == "gpt-image-1":
            body_dict["size"] = "1536x1024"  # landscape
            body_dict["quality"] = "high"
        else:  # dall-e-3
            body_dict["size"] = "1792x1024"
            body_dict["quality"] = "standard"
            body_dict["response_format"] = "url"
        body = _json.dumps(body_dict).encode("utf-8")
        try:
            req = urllib.request.Request(
                "https://api.openai.com/v1/images/generations",
                data=body, method="POST",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                    "User-Agent": USER_AGENT,
                },
            )
            with urllib.request.urlopen(req, timeout=90) as r:
                payload = _json.loads(r.read())
            d = payload["data"][0]
            if d.get("b64_json"):
                raw = base64.b64decode(d["b64_json"])
            else:
                raw = _http_get(d["url"], timeout=30)
            if raw and len(raw) > 20000:
                return {
                    "bytes": raw,
                    "fonte_credito": f"Imagem ilustrativa — OpenAI ({tentativa_model})",
                    "fonte_url": "",
                }
        except urllib.error.HTTPError as e:
            print(f"[buscar_imagem] OpenAI ({tentativa_model}) HTTP {e.code}: "
                  f"{e.read()[:200].decode('utf-8', 'ignore')}")
        except Exception as e:
            print(f"[buscar_imagem] OpenAI ({tentativa_model}) falhou: {e}")
    return None


# ============================================================
# Estratégia 6 — gradiente SulTV liso (sem texto)
# ============================================================
def _fundo_sultv_liso() -> dict:
    """Gera um PNG 1600x900 com gradiente oficial SulTV — SEM TEXTO."""
    try:
        from imagens import gerar_gradiente_oficial
        grad = gerar_gradiente_oficial(1600, 900, vertical=False)
        buf = io.BytesIO()
        grad.save(buf, format="PNG", optimize=True)
        return {
            "bytes": buf.getvalue(),
            "fonte_credito": "Arte: SulTV",
            "fonte_url": "",
        }
    except Exception:
        from PIL import Image
        im = Image.new("RGB", (1600, 900), (22, 104, 151))
        buf = io.BytesIO()
        im.save(buf, format="PNG", optimize=True)
        return {"bytes": buf.getvalue(), "fonte_credito": "Arte: SulTV", "fonte_url": ""}


# ============================================================
# Smart crop por formato
# ============================================================
def _smart_crop(raw: bytes, target_w: int, target_h: int) -> bytes:
    """Recorta + redimensiona preservando o centro da imagem.

    Algoritmo: calcula a maior área central que respeite o aspect-ratio alvo,
    recorta e redimensiona via LANCZOS. Saída sempre JPEG quality 88 (~150KB)
    pra economizar upload no Wix Media e dar bom tradeoff qualidade/tamanho.
    """
    from PIL import Image
    im = Image.open(io.BytesIO(raw))
    if im.mode != "RGB":
        im = im.convert("RGB")
    src_w, src_h = im.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        # Source mais largo — corta laterais
        new_w = int(src_h * target_ratio)
        left = (src_w - new_w) // 2
        box = (left, 0, left + new_w, src_h)
    else:
        # Source mais alto — corta topo/base
        new_h = int(src_w / target_ratio)
        top = (src_h - new_h) // 2
        box = (0, top, src_w, top + new_h)
    im = im.crop(box).resize((target_w, target_h), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=88, optimize=True, progressive=True)
    return buf.getvalue()


def gerar_variantes_por_formato(raw: bytes,
                                 formatos: list[str] | None = None) -> dict:
    """Recebe a imagem base e devolve dict {nome_formato: bytes_jpeg}.

    Default: gera wix_cover (1600x900), fb_feed (1200x630) e ig_feed (1080x1350).
    """
    formatos = formatos or ["wix_cover", "fb_feed", "ig_feed"]
    saida = {}
    for nome in formatos:
        if nome not in FORMATOS:
            print(f"[variantes] formato desconhecido: {nome}")
            continue
        try:
            w, h = FORMATOS[nome]
            saida[nome] = _smart_crop(raw, w, h)
        except Exception as e:
            print(f"[variantes] erro em {nome}: {e}")
    return saida


# ============================================================
# Cascata principal — escolhe estratégia por contexto
# ============================================================
def _cascata_para(tag_principal: str, cidade: str) -> list[str]:
    """Devolve a ordem de estratégias para esta matéria.

    Política de imagem regional (Donário 2026-06-16 — conceito atualizado):
    - FONTE PRIMÁRIA = IA generativa gratuita ancorada no Sul-RS (Pollinations
      FLUX). O `prompt_ia` é travado com a âncora regional ("interior do RS /
      Costa Doce") + negativos (sem texto, sem placas, sem país estrangeiro),
      então a imagem reflete o TEMA com ambientação inconfundivelmente gaúcha.
      Isso elimina a origem das fotos "gringas" (stock anglo / og genérico).
    - og:image da fonte e fotos de acervo entram só como REDE DE SEGURANÇA,
      e SEMPRE passam pelo filtro anti-texto/anti-estrangeiro (OCR). Qualquer
      imagem com banner, placa, adesivagem ou idioma não-PT é rejeitada.
    - Quando não há imagem segura e relevante: foto temática neutra do Sul
      (acervo livre com query PT + âncora regional); último recurso, card
      gráfico SulTV (gradiente, sem texto).
    - Gemini/OpenAI permanecem como reforço de IA caso haja créditos (hoje
      desativados); também já vêm ancorados no Sul-RS.
    """
    return ["ia_pollinations", "ia_gemini", "ia_openai",
            "og", "acervo_livre", "pexels", "unsplash", "gradiente"]


# ============================================================
# API pública
# ============================================================
def obter_imagem_limpa(*, url_fonte: str = "",
                       titulo: str = "",
                       palavras_chave: list[str] | None = None,
                       tag_principal: str = "",
                       cidade: str = "",
                       descricao_imagem: str = "",
                       briefing_visual: dict | None = None,
                       gerar_variantes: bool = True,
                       formatos_alvo: list[str] | None = None) -> dict:
    """Retorna dict completo com bytes da imagem base + variantes por formato.

    Estrutura de retorno:
      {
        bytes: ...,                # imagem base (a maior disponível)
        fonte_credito: "Foto: ...",
        fonte_url: "https://...",
        alt_text: "descrição rica em pt-BR",
        width, height,
        origem: "og_image_fonte" | "pexels" | "unsplash" | "gemini_imagen4" |
                "openai_gpt_image" | "openai_dalle" | "gradiente_sultv",
        variantes: {
          wix_cover: bytes_jpeg_1600x900,
          fb_feed:   bytes_jpeg_1200x630,
          ig_feed:   bytes_jpeg_1080x1350,
        },
      }

    `briefing_visual` (opcional, recomendado) é dict com:
      - descricao_pt: prompt visual rico em pt-BR (vira alt_text e query)
      - query_en: lista de queries em inglês para Pexels/Unsplash
      - evitar: lista do que NÃO pode aparecer (pessoas, marcas, texto)
      - prompt_ia: prompt completo em inglês para Gemini/OpenAI

    Se não houver briefing_visual, o fallback é montado a partir de
    descricao_imagem + palavras_chave + tag_principal + cidade.
    """
    palavras_chave = palavras_chave or []
    bv = briefing_visual or {}

    # --- Resolve prompts a partir do briefing visual ou do fallback ---
    descricao = bv.get("descricao_pt") or descricao_imagem or titulo
    cid_disp = _cidade_display(cidade)

    # Queries para FOTO real (og/acervo/stock — rede de segurança). Privilegia
    # PT + âncora regional ("Rio Grande do Sul Brasil") — Wikimedia Commons tem
    # bom acervo BR em PT; o que vem em inglês entra só como reforço.
    queries_en = bv.get("query_en") or []
    partes_pt = []
    if tag_principal:
        partes_pt.append(tag_principal.replace("_", " "))
    if palavras_chave:
        partes_pt.extend(palavras_chave[:2])
    base_pt = " ".join(partes_pt).strip() or (descricao[:60] if descricao else titulo)
    ancora_pt = (f"{cid_disp} Rio Grande do Sul" if cid_disp else "Rio Grande do Sul Brasil")
    queries_foto = [f"{base_pt} {ancora_pt}".strip(), f"{base_pt} Brasil".strip()]
    queries_foto += [f"{q} Brazil".strip() for q in queries_en[:2]]

    # Prompt da IA = TEMA (a âncora regional + negativos são adicionados dentro
    # dos geradores por _prompt_ancorado_sul, então aqui vai só o tema/cena).
    prompt_ia = (bv.get("prompt_ia") or descricao
                 + (". Avoid: " + ", ".join(bv["evitar"]) if bv.get("evitar") else ""))

    def _foto_ok(raw: bytes) -> bool:
        """Foto real só é aceita se NÃO tiver texto embutido (banner/placa/
        adesivagem/idioma estrangeiro) — filtro OCR (Donário 2026-06-16)."""
        if _imagem_com_texto_demais(raw):
            print("[buscar_imagem] foto rejeitada: texto/idioma embutido (anti-estrangeiro)")
            return False
        return True

    # --- Cascata ---
    ordem = _cascata_para(tag_principal, cidade)
    resultado = None
    origem = ""

    for estrategia in ordem:
        if resultado:
            break
        try:
            if estrategia == "ia_pollinations":
                if os.getenv("POLLINATIONS_OFF", "").strip() not in ("1", "true", "True"):
                    r = _gerar_via_pollinations(prompt_ia, cidade)
                    if r:
                        resultado = r
                        origem = "pollinations_flux"
            elif estrategia == "og" and url_fonte and not any(
                    d in url_fonte.lower() for d in ("instagram.com", "facebook.com", "fb.watch")):
                og = _extrair_og_image(url_fonte)
                if og and _foto_ok(og):
                    resultado = {"bytes": og, "fonte_credito": "",
                                 "fonte_url": url_fonte}
                    origem = "og_image_fonte"
            elif estrategia == "pexels":
                for q in queries_foto:
                    r = _buscar_pexels(q)
                    if r and _foto_ok(r["bytes"]):
                        resultado = r
                        origem = "pexels"
                        break
            elif estrategia == "unsplash":
                for q in queries_foto:
                    r = _buscar_unsplash(q)
                    if r and _foto_ok(r["bytes"]):
                        resultado = r
                        origem = "unsplash"
                        break
            elif estrategia == "ia_gemini":
                primary = os.getenv("IMAGE_GEN_PRIMARY", "gemini").lower()
                if primary != "openai":
                    r = _gerar_via_gemini(prompt_ia, cidade)
                    if r:
                        resultado = r
                        origem = "gemini_imagen4"
            elif estrategia == "ia_openai":
                r = _gerar_via_openai(prompt_ia, cidade)
                if r:
                    resultado = r
                    origem = ("openai_gpt_image"
                              if "gpt-image" in r["fonte_credito"]
                              else "openai_dalle")
            elif estrategia == "acervo_livre":
                r = _buscar_acervo_livre(queries_foto)
                if r and _foto_ok(r["bytes"]):
                    resultado = r
                    origem = ("openverse" if "Openverse" in r["fonte_credito"]
                              else "wikimedia_commons")
            elif estrategia == "gradiente":
                resultado = _fundo_sultv_liso()
                origem = "gradiente_sultv"
        except Exception as e:
            print(f"[buscar_imagem] estratégia '{estrategia}' levantou: {e}")

    if not resultado:
        resultado = _fundo_sultv_liso()
        origem = "gradiente_sultv"

    raw_base = resultado["bytes"]
    w, h = _image_size(raw_base)
    alt_text = (bv.get("descricao_pt") or descricao_imagem
                or f"{titulo} — {cidade}".strip(" —"))

    out = {
        "bytes": raw_base,
        "fonte_credito": resultado.get("fonte_credito", ""),
        "fonte_url": resultado.get("fonte_url", ""),
        "alt_text": alt_text[:240],
        "width": w,
        "height": h,
        "origem": origem,
    }

    if gerar_variantes:
        try:
            out["variantes"] = gerar_variantes_por_formato(raw_base, formatos_alvo)
        except Exception as e:
            print(f"[buscar_imagem] falha ao gerar variantes: {e}")
            out["variantes"] = {}
    return out


# ============================================================
# CLI utilitária pra testes
# ============================================================
if __name__ == "__main__":
    import sys, json as _json
    if len(sys.argv) < 2:
        print("Uso: python3 buscar_imagem_limpa.py <descricao_imagem> [url_fonte]")
        sys.exit(1)
    desc = sys.argv[1]
    url = sys.argv[2] if len(sys.argv) > 2 else ""
    out = obter_imagem_limpa(
        descricao_imagem=desc, url_fonte=url,
        cidade="Arambaré", tag_principal="politica_local",
    )
    base = "/tmp/test_imagem_limpa"
    with open(f"{base}_base.jpg", "wb") as f:
        f.write(out.pop("bytes"))
    for nome, b in out.get("variantes", {}).items():
        with open(f"{base}_{nome}.jpg", "wb") as f:
            f.write(b)
    out["variantes"] = {k: f"{len(v)//1024}KB" for k, v in out.get("variantes", {}).items()}
    print(_json.dumps(out, ensure_ascii=False, indent=2))
    print(f"\nImagens em {base}_*.jpg")
