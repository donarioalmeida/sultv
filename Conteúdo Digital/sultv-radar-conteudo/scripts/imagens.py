#!/usr/bin/env python3
"""
imagens.py — geração visual SulTV-branded para o Radar.

Reusa o padrão oficial documentado em
/Marketing e Marca/Template_Thumb_Editorial_SulTV.md (28/04/2026).

Funções principais:
  - extrair_og_image(url) -> bytes | None
  - gerar_thumb_branded(titulo, formato, frame_bytes=None, kicker=None) -> bytes (PNG)
  - gerar_card_carrossel(numero, total, titulo, texto, formato='1080x1350') -> bytes (PNG)

Formatos suportados:
  - '1200x630'  → capa Wix Blog
  - '1080x1080' → post Instagram quadrado
  - '1080x1350' → post Instagram retrato + carrossel
  - '1280x720'  → thumb YouTube editorial
"""
from __future__ import annotations
import io
import os
import re
import urllib.request
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# ============================================================
# Cores oficiais — Brand Kit SulTV v1.0 (paleta_SulTV.json)
# ============================================================
AZUL_PROFUNDO = (22, 104, 151)   # #166897 — institucional dominante
TURQUESA      = (25, 143, 161)   # #198FA1 — gradiente, digital
VERDE_LIMAO   = (139, 199, 81)   # #8BC751 — acento, CTA
AZUL_CLARO    = (146, 214, 227)  # #92D6E3
PRETO_EDIT    = (15, 27, 38)     # #0F1B26 — texto/fundo escuro
CINZA_EDIT    = (107, 119, 133)  # #6B7785
BRANCO        = (255, 255, 255)
PRETO         = (0, 0, 0)

# Aliases preservados para compatibilidade
AZUL_PETROLEO = AZUL_PROFUNDO  # legado
LARANJA_SULTV = VERDE_LIMAO    # legado — pílulas usam verde-limão


FORMATOS = {
    '1200x630':  (1200, 630),    # Wix Blog cover
    '1080x1080': (1080, 1080),   # IG square
    '1080x1350': (1080, 1350),   # IG portrait + carrossel
    '1280x720':  (1280, 720),    # YouTube thumb
}


# ============================================================
# Brand Kit assets — paths absolutos do Mac
# ============================================================
BRAND_KIT_BASE = '/Users/donariolopesdealmeida/Meu Drive/CONEX — Holding & Hub/02_SulTV/Marketing e Marca/MKT - Marca/Brand_Kit_SulTV_v1'
SANDBOX_BASE = '/sessions/practical-stoic-turing/mnt/Brand_Kit_SulTV_v1'


def _brand_path(*parts) -> str:
    """Resolve para o Mac local OU sandbox, conforme onde está rodando."""
    for base in (BRAND_KIT_BASE, SANDBOX_BASE):
        p = os.path.join(base, *parts)
        if os.path.exists(p):
            return p
    return os.path.join(BRAND_KIT_BASE, *parts)


def find_font(weight: str = 'Bold') -> str:
    """Carrega fonte Outfit do Brand Kit. Fallback Poppins/DejaVu."""
    primary = _brand_path('03_Tipografia', 'Outfit_Fonts', f'Outfit-{weight}.ttf')
    if os.path.exists(primary):
        return primary
    fallbacks = {
        'Bold': [
            '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf',
            '/Library/Fonts/Poppins-Bold.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        ],
        'SemiBold': [
            '/usr/share/fonts/truetype/google-fonts/Poppins-SemiBold.ttf',
            '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        ],
        'Regular': [
            '/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf',
            '/Library/Fonts/Poppins-Regular.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        ],
        'Light': [
            '/usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        ],
    }
    for p in fallbacks.get(weight, []):
        if os.path.exists(p):
            return p
    return find_font('Bold') if weight != 'Bold' else '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def find_font_bold() -> str:
    return find_font('Bold')


def find_font_regular() -> str:
    return find_font('Regular')


# Logo cache
_LOGO_CACHE = {}


def carregar_logo(variante: str = 'HOR-BRANCA', tamanho_x: int = 4) -> Optional[Image.Image]:
    """Carrega logo SulTV PNG do Brand Kit. variante: HOR-BRANCA|HOR-PRETA|VERT-BRANCA etc."""
    cache_key = f'{variante}@{tamanho_x}x'
    if cache_key in _LOGO_CACHE:
        return _LOGO_CACHE[cache_key]
    p = _brand_path('01_Logos por formatos', 'PNG_HD', f'SULTV_{variante}@{tamanho_x}x.png')
    if not os.path.exists(p):
        return None
    try:
        img = Image.open(p).convert('RGBA')
        _LOGO_CACHE[cache_key] = img
        return img
    except Exception:
        return None


def gerar_gradiente_oficial(w: int, h: int, vertical: bool = False) -> Image.Image:
    """Gradiente oficial SulTV: Turquesa → Verde-Limão (horizontal por padrão)."""
    grad = Image.new('RGB', (w, h), TURQUESA)
    pixels = grad.load()
    if vertical:
        for y in range(h):
            t = y / max(1, h - 1)
            r = int(TURQUESA[0] * (1 - t) + VERDE_LIMAO[0] * t)
            g = int(TURQUESA[1] * (1 - t) + VERDE_LIMAO[1] * t)
            b = int(TURQUESA[2] * (1 - t) + VERDE_LIMAO[2] * t)
            for x in range(w):
                pixels[x, y] = (r, g, b)
    else:
        for x in range(w):
            t = x / max(1, w - 1)
            r = int(TURQUESA[0] * (1 - t) + VERDE_LIMAO[0] * t)
            g = int(TURQUESA[1] * (1 - t) + VERDE_LIMAO[1] * t)
            b = int(TURQUESA[2] * (1 - t) + VERDE_LIMAO[2] * t)
            for y in range(h):
                pixels[x, y] = (r, g, b)
    return grad


# ---------- OG image fetching ----------

def extrair_og_image(url: str, timeout: int = 10) -> Optional[bytes]:
    """Tenta baixar a imagem og:image da fonte. Retorna bytes JPEG/PNG ou None."""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 SulTV-Radar/1.0',
        })
        with urllib.request.urlopen(req, timeout=timeout) as r:
            html = r.read(200_000).decode('utf-8', 'ignore')
    except Exception:
        return None

    # Regex simples para og:image (cobre 90% dos casos)
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

    # Resolve relativos
    if img_url.startswith('//'):
        img_url = 'https:' + img_url
    elif img_url.startswith('/'):
        from urllib.parse import urlparse
        u = urlparse(url)
        img_url = f'{u.scheme}://{u.netloc}{img_url}'

    try:
        req = urllib.request.Request(img_url, headers={
            'User-Agent': 'Mozilla/5.0 SulTV-Radar/1.0',
        })
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read(8_000_000)
        # Sanity check: precisa parecer imagem
        if len(data) < 1000:
            return None
        return data
    except Exception:
        return None


# ---------- Helpers de texto ----------

def auto_fit_lines(draw, text: str, font_path: str, max_w: int,
                   start_size: int = 60, min_size: int = 20,
                   max_lines: int = 4) -> Tuple[list, ImageFont.FreeTypeFont]:
    """Quebra texto em N linhas com a maior fonte que cabe."""
    words = text.split()
    for size in range(start_size, min_size - 1, -2):
        font = ImageFont.truetype(font_path, size)
        # Greedy line breaking
        lines = []
        current = ''
        for w in words:
            tentative = (current + ' ' + w).strip()
            bbox = draw.textbbox((0, 0), tentative, font=font)
            if bbox[2] - bbox[0] <= max_w:
                current = tentative
            else:
                if current:
                    lines.append(current)
                current = w
        if current:
            lines.append(current)
        if len(lines) <= max_lines:
            return lines, font
    return text.split()[:max_lines], ImageFont.truetype(font_path, min_size)


# ---------- Frame loader ----------

def _carregar_frame(frame_bytes: Optional[bytes]) -> Optional[Image.Image]:
    if not frame_bytes:
        return None
    try:
        img = Image.open(io.BytesIO(frame_bytes)).convert('RGB')
        # Sanity: imagem útil precisa ter pelo menos 400x300
        if img.size[0] < 400 or img.size[1] < 300:
            return None
        return img
    except Exception:
        return None


def _crop_para_aspecto(src: Image.Image, w: int, h: int) -> Image.Image:
    """Center crop da imagem fonte para o aspect ratio alvo."""
    target_ratio = w / h
    sw, sh = src.size
    cur_ratio = sw / sh
    if cur_ratio > target_ratio:
        new_w = int(sh * target_ratio)
        left = (sw - new_w) // 2
        cropped = src.crop((left, 0, left + new_w, sh))
    else:
        new_h = int(sw / target_ratio)
        top = (sh - new_h) // 2
        cropped = src.crop((0, top, sw, top + new_h))
    return cropped.resize((w, h), Image.LANCZOS)


# ---------- Geração principal ----------

def _aplicar_logo(canvas: Image.Image, posicao: str = 'rodape', altura_pct: float = 0.06):
    """Cola o logo SulTV (PNG transparente) no canvas. posicao: rodape | topo_dir | topo_esq."""
    W, H = canvas.size
    logo = carregar_logo('HOR-BRANCA', 4) or carregar_logo('HOR-BRANCA', 2)
    if logo is None:
        return
    # Redimensiona pelo alvo de altura
    target_h = max(40, int(H * altura_pct))
    ratio = target_h / logo.height
    target_w = int(logo.width * ratio)
    logo_resized = logo.resize((target_w, target_h), Image.LANCZOS)
    # Posicionamento
    margin = max(20, int(W * 0.025))
    if posicao == 'rodape':
        # Centralizado horizontalmente, próximo ao rodapé (acima da listra)
        stripe_h = max(12, int(H * 0.025))
        x = (W - target_w) // 2
        y = H - stripe_h - target_h - max(10, int(H * 0.02))
    elif posicao == 'topo_dir':
        x = W - target_w - margin
        y = margin
    elif posicao == 'topo_esq':
        x = margin
        y = margin
    else:
        x, y = margin, margin
    canvas.paste(logo_resized, (x, y), logo_resized)


def _aplicar_listra_gradiente(canvas: Image.Image, altura_px: Optional[int] = None,
                               posicao: str = 'rodape'):
    """Listra horizontal com gradiente oficial Turquesa → Verde-Limão."""
    W, H = canvas.size
    if altura_px is None:
        altura_px = max(12, int(H * 0.025))
    grad = gerar_gradiente_oficial(W, altura_px, vertical=False)
    if posicao == 'rodape':
        canvas.paste(grad, (0, H - altura_px))
    else:
        canvas.paste(grad, (0, 0))


def _aplicar_fundo_foto(canvas: Image.Image, frame_bytes: Optional[bytes],
                         escurecimento: float = 0.65, blur_radius: int = 20):
    """Cola og:image como fundo escurecido com blur. Se não houver, usa gradient oficial."""
    W, H = canvas.size
    src = _carregar_frame(frame_bytes)
    if src is not None:
        bg = _crop_para_aspecto(src, W, H).filter(ImageFilter.GaussianBlur(radius=blur_radius))
        bg = Image.blend(bg, Image.new('RGB', (W, H), PRETO_EDIT), escurecimento)
        canvas.paste(bg, (0, 0))
    else:
        # Fallback: gradient oficial vertical Turquesa→Verde-Limão escurecido
        grad = gerar_gradiente_oficial(W, H, vertical=True)
        grad = Image.blend(grad, Image.new('RGB', (W, H), PRETO_EDIT), 0.55)
        canvas.paste(grad, (0, 0))


def gerar_thumb_branded(titulo: str, formato: str = '1200x630',
                        frame_bytes: Optional[bytes] = None,
                        kicker: Optional[str] = None,
                        cobranding: str = 'REDAÇÃO SulTV') -> bytes:
    """Gera thumb SulTV-branded em PNG. Sempre usa foto contextual (og:image) quando disponível.

    Layout (Brand Kit v1.0):
    - Fundo: og:image com blur 20px + escurecimento 65% sobre Preto Editorial
    - Frame central 9:16 (em formatos horizontais 1200x630/1280x720)
    - Caixa título: Azul Profundo #166897 com borda Verde-Limão #8BC751
    - Kicker (opcional): pílula Verde-Limão acima da caixa
    - Logo SULTV_HOR-BRANCA no rodapé centralizado
    - Listra rodapé: gradiente oficial Turquesa→Verde-Limão
    """
    if formato not in FORMATOS:
        raise ValueError(f'Formato inválido: {formato}')
    W, H = FORMATOS[formato]
    canvas = Image.new('RGB', (W, H), PRETO_EDIT)

    # 1. Fundo: foto escurecida ou gradient
    _aplicar_fundo_foto(canvas, frame_bytes, escurecimento=0.55, blur_radius=22)

    # 2. Frame central 9:16 (apenas em formatos horizontais quando há foto)
    src = _carregar_frame(frame_bytes)
    if src is not None and formato in ('1200x630', '1280x720'):
        center_h = int(H * 0.94)
        center_w = int(center_h * 9 / 16)
        cropped = _crop_para_aspecto(src, center_w, center_h)
        canvas.paste(cropped, ((W - center_w) // 2, (H - center_h) // 2))

    draw = ImageDraw.Draw(canvas)
    font_path = find_font_bold()

    # 3. Caixa de título
    box_max_w = int(W * 0.84)
    start_size = int(H * 0.085) if formato in ('1080x1080', '1080x1350') else int(H * 0.075)
    lines, font = auto_fit_lines(draw, titulo, font_path, box_max_w,
                                  start_size=start_size, min_size=20, max_lines=4)

    line_h = int(font.size * 1.30)
    box_inner_pad_y = max(14, int(font.size * 0.45))
    box_inner_pad_x = max(22, int(font.size * 0.6))
    box_h = line_h * len(lines) + box_inner_pad_y * 2
    box_w = box_max_w + box_inner_pad_x * 2

    if formato in ('1080x1080', '1080x1350'):
        box_y1 = (H - box_h) // 2 + int(H * 0.05)
    else:
        stripe_h = max(12, int(H * 0.025))
        # Espaço pro logo no rodapé
        logo_block = int(H * 0.06) + max(10, int(H * 0.02))
        box_y1 = H - stripe_h - logo_block - 20 - box_h

    box_x1 = (W - box_w) // 2
    box_x2 = box_x1 + box_w
    box_y2 = box_y1 + box_h

    # Caixa Azul Profundo #166897 com borda Verde-Limão
    draw.rounded_rectangle((box_x1, box_y1, box_x2, box_y2),
                           radius=22, fill=AZUL_PROFUNDO,
                           outline=VERDE_LIMAO, width=4)

    # Kicker (pílula verde-limão acima)
    if kicker:
        font_kicker = ImageFont.truetype(font_path, max(18, int(font.size * 0.42)))
        kbbox = draw.textbbox((0, 0), kicker.upper(), font=font_kicker)
        kw, kh = kbbox[2] - kbbox[0], kbbox[3] - kbbox[1]
        kx = (W - kw) // 2
        ky = box_y1 - kh - 18
        draw.rounded_rectangle((kx - 18, ky - 7, kx + kw + 18, ky + kh + 9),
                                radius=8, fill=VERDE_LIMAO)
        draw.text((kx, ky), kicker.upper(), font=font_kicker, fill=PRETO_EDIT)

    # Texto centralizado
    y_text = box_y1 + box_inner_pad_y
    for ln in lines:
        bbox = draw.textbbox((0, 0), ln, font=font)
        tw = bbox[2] - bbox[0]
        x_text = box_x1 + (box_w - tw) // 2
        draw.text((x_text, y_text), ln, font=font, fill=BRANCO)
        y_text += line_h

    # 4. Logo SulTV (rodapé, acima da listra)
    _aplicar_logo(canvas, posicao='rodape', altura_pct=0.06)

    # 5. Listra rodapé com gradiente oficial
    _aplicar_listra_gradiente(canvas)

    buf = io.BytesIO()
    canvas.save(buf, format='PNG', optimize=True)
    return buf.getvalue()


# ---------- Carrossel (cards info, sem foto) ----------

def gerar_card_carrossel(numero: int, total: int, titulo: str, texto: str,
                          formato: str = '1080x1350',
                          frame_bytes: Optional[bytes] = None) -> bytes:
    """Card de carrossel COM foto de fundo (og:image escurecida) + título + texto.

    Sempre usa frame_bytes como fundo (Brand Kit pede "sempre com imagem").
    Se frame_bytes for None, usa gradient oficial.
    """
    if formato not in FORMATOS:
        raise ValueError(f'Formato inválido: {formato}')
    W, H = FORMATOS[formato]

    canvas = Image.new('RGB', (W, H), PRETO_EDIT)
    # 1. Fundo: foto escurecida bem mais (cards têm muito texto)
    _aplicar_fundo_foto(canvas, frame_bytes, escurecimento=0.72, blur_radius=18)

    draw = ImageDraw.Draw(canvas)
    font_bold = find_font_bold()
    font_semi = find_font('SemiBold')
    font_reg = find_font_regular()

    # Header: numero/total + indicador
    fnum = ImageFont.truetype(font_bold, int(W * 0.045))
    nt = f'{numero:02d} / {total:02d}'
    # Pílula verde-limão para o número
    bb = draw.textbbox((0, 0), nt, font=fnum)
    nw, nh = bb[2] - bb[0], bb[3] - bb[1]
    nx = int(W * 0.07)
    ny = int(H * 0.07)
    draw.rounded_rectangle((nx - 18, ny - 8, nx + nw + 18, ny + nh + 10),
                            radius=10, fill=VERDE_LIMAO)
    draw.text((nx, ny), nt, font=fnum, fill=PRETO_EDIT)

    # Título do card (área central superior)
    titulo_y = int(H * 0.22)
    titulo_max_w = int(W * 0.86)
    lines_t, font_t = auto_fit_lines(
        draw, titulo, font_bold, titulo_max_w,
        start_size=int(W * 0.075), min_size=int(W * 0.04), max_lines=3)
    line_h_t = int(font_t.size * 1.22)
    for ln in lines_t:
        bbox = draw.textbbox((0, 0), ln, font=font_t)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, titulo_y), ln, font=font_t, fill=BRANCO)
        titulo_y += line_h_t

    # Linha separadora gradient
    sep_y = titulo_y + 36
    sep_w = int(W * 0.40)
    sep_x = (W - sep_w) // 2
    grad_strip = gerar_gradiente_oficial(sep_w, 4)
    canvas.paste(grad_strip, (sep_x, sep_y))

    # Texto do card (corpo) — Outfit SemiBold
    texto_y = sep_y + 50
    texto_max_w = int(W * 0.84)
    lines_x, font_x = auto_fit_lines(
        draw, texto, font_semi, texto_max_w,
        start_size=int(W * 0.038), min_size=int(W * 0.025), max_lines=8)
    line_h_x = int(font_x.size * 1.45)
    for ln in lines_x:
        bbox = draw.textbbox((0, 0), ln, font=font_x)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, texto_y), ln, font=font_x, fill=BRANCO)
        texto_y += line_h_x

    # Logo SulTV no rodapé (pequeno, canto esquerdo)
    logo = carregar_logo('HOR-BRANCA', 4) or carregar_logo('HOR-BRANCA', 2)
    if logo:
        target_h = max(30, int(H * 0.035))
        ratio = target_h / logo.height
        logo_resized = logo.resize((int(logo.width * ratio), target_h), Image.LANCZOS)
        canvas.paste(logo_resized,
                     (int(W * 0.07), H - target_h - max(30, int(H * 0.04))),
                     logo_resized)

    # Indicador "deslize" no rodapé direito
    if numero < total:
        seta = '→ DESLIZE'
        fb = ImageFont.truetype(font_bold, int(W * 0.028))
        bb = draw.textbbox((0, 0), seta, font=fb)
        sw, sh = bb[2] - bb[0], bb[3] - bb[1]
        draw.text((W - sw - int(W * 0.07), H - sh - max(30, int(H * 0.045))),
                  seta, font=fb, fill=VERDE_LIMAO)

    # Listra inferior com gradiente
    _aplicar_listra_gradiente(canvas, altura_px=max(8, int(H * 0.012)))

    buf = io.BytesIO()
    canvas.save(buf, format='PNG', optimize=True)
    return buf.getvalue()


def gerar_capa_carrossel(titulo_carrossel: str, total_cards: int,
                          formato: str = '1080x1350',
                          frame_bytes: Optional[bytes] = None) -> bytes:
    """Capa do carrossel (card 1 de N) com og:image como fundo escurecido."""
    if formato not in FORMATOS:
        raise ValueError(f'Formato inválido: {formato}')
    W, H = FORMATOS[formato]
    canvas = Image.new('RGB', (W, H), PRETO_EDIT)

    # 1. Fundo foto escurecida (capa fica mais "leve" pra dar destaque ao título)
    _aplicar_fundo_foto(canvas, frame_bytes, escurecimento=0.62, blur_radius=22)

    draw = ImageDraw.Draw(canvas)
    font_bold = find_font_bold()

    # Listra topo gradient
    grad_top = gerar_gradiente_oficial(W, max(8, int(H * 0.012)))
    canvas.paste(grad_top, (0, 0))

    # Indicador "CARROSSEL · N CARDS"
    finfo = ImageFont.truetype(font_bold, int(W * 0.026))
    info_text = f'CARROSSEL · {total_cards} CARDS'
    bb = draw.textbbox((0, 0), info_text, font=finfo)
    iw, ih = bb[2] - bb[0], bb[3] - bb[1]
    ix = int(W * 0.07)
    iy = int(H * 0.07)
    draw.rounded_rectangle((ix - 16, iy - 8, ix + iw + 16, iy + ih + 10),
                            radius=8, fill=VERDE_LIMAO)
    draw.text((ix, iy), info_text, font=finfo, fill=PRETO_EDIT)

    # Título grande centralizado
    titulo_max_w = int(W * 0.86)
    lines, font = auto_fit_lines(
        draw, titulo_carrossel, font_bold, titulo_max_w,
        start_size=int(W * 0.085), min_size=int(W * 0.045), max_lines=5)
    line_h = int(font.size * 1.18)
    total_h = line_h * len(lines)
    titulo_y = (H - total_h) // 2 - int(H * 0.04)
    for ln in lines:
        bbox = draw.textbbox((0, 0), ln, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, titulo_y), ln, font=font, fill=BRANCO)
        titulo_y += line_h

    # CTA "deslize"
    fcta = ImageFont.truetype(font_bold, int(W * 0.035))
    cta = '→ DESLIZE PARA VER OS CARDS'
    bb = draw.textbbox((0, 0), cta, font=fcta)
    cw, ch = bb[2] - bb[0], bb[3] - bb[1]
    cy = int(H * 0.82)
    cx = (W - cw) // 2
    draw.rounded_rectangle((cx - 24, cy - 12, cx + cw + 24, cy + ch + 14),
                            radius=12, fill=VERDE_LIMAO)
    draw.text((cx, cy), cta, font=fcta, fill=PRETO_EDIT)

    # Logo SulTV no rodapé
    _aplicar_logo(canvas, posicao='rodape', altura_pct=0.045)

    # Listra rodapé gradient
    _aplicar_listra_gradiente(canvas, altura_px=max(8, int(H * 0.012)))

    buf = io.BytesIO()
    canvas.save(buf, format='PNG', optimize=True)
    return buf.getvalue()


def gerar_post_simples(titulo: str, hook: str, corpo_linhas: list,
                        cta: str = '', formato: str = '1080x1350',
                        frame_bytes: Optional[bytes] = None) -> bytes:
    """Post Instagram simples (1 imagem) COM og:image escurecida como fundo.

    Layout: hook grande + corpo justificado + CTA pílula + logo SulTV.
    """
    W, H = FORMATOS[formato]
    canvas = Image.new('RGB', (W, H), PRETO_EDIT)

    # 1. Fundo foto escurecida
    _aplicar_fundo_foto(canvas, frame_bytes, escurecimento=0.70, blur_radius=20)

    draw = ImageDraw.Draw(canvas)
    font_bold = find_font_bold()
    font_semi = find_font('SemiBold')

    # Listra topo gradient
    grad_top = gerar_gradiente_oficial(W, max(8, int(H * 0.012)))
    canvas.paste(grad_top, (0, 0))

    # Pílula identificadora topo
    fbrand = ImageFont.truetype(font_bold, int(W * 0.024))
    brand_text = 'REDAÇÃO SulTV'
    bb = draw.textbbox((0, 0), brand_text, font=fbrand)
    bw, bh = bb[2] - bb[0], bb[3] - bb[1]
    bx = int(W * 0.07)
    by = int(H * 0.06)
    draw.rounded_rectangle((bx - 14, by - 6, bx + bw + 14, by + bh + 8),
                            radius=8, fill=VERDE_LIMAO)
    draw.text((bx, by), brand_text, font=fbrand, fill=PRETO_EDIT)

    # Hook grande
    hook_max_w = int(W * 0.86)
    lines_h, font_h = auto_fit_lines(
        draw, hook, font_bold, hook_max_w,
        start_size=int(W * 0.078), min_size=int(W * 0.042), max_lines=3)
    line_h_h = int(font_h.size * 1.22)
    y = int(H * 0.20)
    for ln in lines_h:
        bbox = draw.textbbox((0, 0), ln, font=font_h)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, y), ln, font=font_h, fill=BRANCO)
        y += line_h_h

    # Separador gradient
    y += 32
    sep_w = int(W * 0.40)
    sep_x = (W - sep_w) // 2
    grad_sep = gerar_gradiente_oficial(sep_w, 4)
    canvas.paste(grad_sep, (sep_x, y))
    y += 50

    # Corpo
    body_max_w = int(W * 0.84)
    body_text = ' '.join(corpo_linhas) if corpo_linhas else ''
    if body_text:
        lines_b, font_b = auto_fit_lines(
            draw, body_text, font_semi, body_max_w,
            start_size=int(W * 0.036), min_size=int(W * 0.024), max_lines=8)
        line_h_b = int(font_b.size * 1.42)
        for ln in lines_b:
            bbox = draw.textbbox((0, 0), ln, font=font_b)
            tw = bbox[2] - bbox[0]
            draw.text(((W - tw) // 2, y), ln, font=font_b, fill=BRANCO)
            y += line_h_b

    # CTA pílula verde-limão
    if cta:
        fcta = ImageFont.truetype(font_bold, int(W * 0.030))
        bb = draw.textbbox((0, 0), cta, font=fcta)
        cw, ch = bb[2] - bb[0], bb[3] - bb[1]
        cy = int(H * 0.83)
        cx = (W - cw) // 2
        draw.rounded_rectangle(
            (cx - 26, cy - 12, cx + cw + 26, cy + ch + 14),
            radius=12, fill=VERDE_LIMAO,
        )
        draw.text((cx, cy), cta, font=fcta, fill=PRETO_EDIT)

    # Logo SulTV no rodapé
    _aplicar_logo(canvas, posicao='rodape', altura_pct=0.045)

    # Listra rodapé gradient
    _aplicar_listra_gradiente(canvas, altura_px=max(8, int(H * 0.012)))

    buf = io.BytesIO()
    canvas.save(buf, format='PNG', optimize=True)
    return buf.getvalue()


# ---------- Faixa-legenda sobreposta (padrão @sultv31) ----------

# Preposições/artigos que não podem terminar uma chamada (frase pendurada).
_STOPWORDS_FIM = {
    'de', 'da', 'do', 'das', 'dos', 'e', 'a', 'o', 'as', 'os', 'para', 'pra',
    'com', 'em', 'no', 'na', 'nos', 'nas', 'que', 'por', 'sem', 'sob', 'ao',
    'aos', 'à', 'às', 'um', 'uma', 'uns', 'umas', 'ou', 'se', 'até', 'após',
    'sobre', 'entre', 'desde',
}


def sanitizar_chamada(chamada: str) -> str:
    """Garante que a chamada da faixa faça sentido: colapsa espaços e remove
    preposições/artigos pendurados no fim (evita 'PLACAS SOLARES DA')."""
    pal = ' '.join((chamada or '').split()).split()
    while pal and pal[-1].lower().strip('.,;:…-') in _STOPWORDS_FIM:
        pal.pop()
    return ' '.join(pal)


# Logo OFICIAL SulTV — "quadrado vertical" (correção Donário 2026-05-31).
# O watermark antigo (code/shorts_skill_scripts/sultv_logo_watermark.png) era o
# logo ERRADO e foi descontinuado. O logo correto fica em references/ e é colado
# sobre um chip branco arredondado para ficar legível na faixa azul.
def _logo_oficial_path() -> Optional[str]:
    """Path do logo oficial SulTV (quadrado vertical, fundo transparente)."""
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (
        os.path.join(here, '..', 'references', 'SULTV_quadrado_vertical_alpha.png'),
        os.path.join(here, 'references', 'SULTV_quadrado_vertical_alpha.png'),
        _brand_path('01_Logos por formatos', 'PNG_HD', 'SULTV_quadrado_vertical_alpha.png'),
    ):
        if os.path.exists(cand):
            return cand
    return None


def _logo_em_chip(logo_rgba: Image.Image, altura_alvo: int) -> Image.Image:
    """Coloca o logo colorido sobre um chip branco arredondado da altura alvo,
    garantindo legibilidade sobre a faixa Azul Profundo."""
    pad = max(2, int(altura_alvo * 0.12))
    inner_h = max(1, altura_alvo - 2 * pad)
    ratio = inner_h / logo_rgba.height
    inner_w = max(1, int(logo_rgba.width * ratio))
    logo_r = logo_rgba.resize((inner_w, inner_h), Image.LANCZOS)
    chip_w = inner_w + 2 * pad
    chip_h = altura_alvo
    mask = Image.new('L', (chip_w, chip_h), 0)
    radius = max(4, int(chip_h * 0.18))
    mdraw = ImageDraw.Draw(mask)
    try:
        mdraw.rounded_rectangle((0, 0, chip_w - 1, chip_h - 1), radius=radius, fill=255)
    except AttributeError:
        mdraw.rectangle((0, 0, chip_w - 1, chip_h - 1), fill=255)
    white = Image.new('RGBA', (chip_w, chip_h), (255, 255, 255, 255))
    transparente = Image.new('RGBA', (chip_w, chip_h), (0, 0, 0, 0))
    chip = Image.composite(white, transparente, mask)
    chip.paste(logo_r, (pad, pad), logo_r)
    return chip


def _logo_para_faixa(altura_alvo: int):
    """Carrega o logo SulTV para a faixa. Cascata (atualizada 2026-05-31):
    1) Logo OFICIAL 'quadrado vertical' (references/) sobre chip branco — CORRETO;
    2) Brand Kit HOR-BRANCA (logo branco), quando disponível;
    3) wordmark textual 'SulTV' — assim a marca NUNCA falta na faixa.
    Retorna (Image RGBA já redimensionada p/ altura_alvo, origem:str).
    """
    # 1) Logo oficial correto (prioritário em qualquer ambiente)
    p = _logo_oficial_path()
    if p:
        try:
            logo_rgba = Image.open(p).convert('RGBA')
            return _logo_em_chip(logo_rgba, altura_alvo), 'brand_oficial'
        except Exception:
            pass
    # 2) Brand Kit (logo branco horizontal) — já adequado p/ faixa escura
    logo = carregar_logo('HOR-BRANCA', 4) or carregar_logo('HOR-BRANCA', 2)
    if logo is not None:
        ratio = altura_alvo / logo.height
        logo = logo.resize((max(1, int(logo.width * ratio)), altura_alvo), Image.LANCZOS)
        return logo, 'brand_kit'
    # 3) Fallback final: wordmark 'SulTV' desenhado
    font_path = find_font_bold()
    f = ImageFont.truetype(font_path, int(altura_alvo * 0.92))
    tmp = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    bb = tmp.textbbox((0, 0), 'SulTV', font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    mark = Image.new('RGBA', (w + 8, altura_alvo), (0, 0, 0, 0))
    ImageDraw.Draw(mark).text((4 - bb[0], (altura_alvo - h) // 2 - bb[1]),
                              'SulTV', font=f, fill=(*BRANCO, 255))
    return mark, 'wordmark'


def revisar_faixa_legenda(chamada: str, logo_origem: str, linhas: list) -> tuple:
    """REVISÃO obrigatória da faixa-legenda (Donário 2026-05-30).

    Verifica, em TODA publicação FB/IG: (1) logo SulTV presente, (2) chamada faz
    sentido (não vazia, mín. 6 chars, não termina em preposição/artigo),
    (3) texto foi efetivamente renderizado. Retorna (ok: bool, motivos: list).
    """
    motivos = []
    txt = (chamada or '').strip()
    if not logo_origem:
        motivos.append('logo SulTV ausente')
    if len(txt) < 6:
        motivos.append('chamada vazia ou curta demais')
    elif txt.lower().strip('.,;:…-').split()[-1] in _STOPWORDS_FIM:
        motivos.append('chamada termina em palavra incompleta')
    if not linhas or not any((l or '').strip() for l in linhas):
        motivos.append('texto da legenda não renderizado')
    return (len(motivos) == 0, motivos)


def aplicar_faixa_legenda(image_bytes: bytes, chamada: str) -> bytes:
    """Sobrepõe a FAIXA-LEGENDA padrão SulTV sobre uma foto já no formato final.

    Aprovado por Donário em 2026-05-29 para os posts de IMAGEM no FB/IG do Radar.
    Layout (estilo @sultv31, exemplo Olimpíadas):
    - Foto nítida preenche o frame (foto visível acima E abaixo da faixa)
    - Faixa compacta no terço inferior: Azul Profundo #166897 translúcido
    - Fio Verde-Limão #8BC751 no topo da faixa
    - Logo SulTV branco à esquerda + chamada curta/SEO (uppercase) CENTRALIZADA
    - Sem crédito de foto, sem selo

    Garantias da revisão (Donário 2026-05-30):
      - logo SulTV SEMPRE presente (Brand Kit → watermark do acervo → wordmark);
      - chamada SEMPRE coerente (sanitizada, sem preposição pendurada);
      - texto SEMPRE centralizado na área à direita do logo.
    Funciona em qualquer proporção. NÃO é usada na capa do Wix (que fica limpa).
    """
    base = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    W, H = base.size
    canvas = base
    draw = ImageDraw.Draw(canvas, 'RGBA')
    font_path = find_font_bold()

    pad_x = int(W * 0.055)
    band_pad_y = int(H * 0.024)

    # Chamada sanitizada (faz sentido) + uppercase
    chamada_lp = sanitizar_chamada(chamada)
    chamada_up = chamada_lp.upper()

    # Área de texto: faixa INTEIRA (o logo saiu da faixa — Donário 2026-06-01).
    # O texto é CENTRALIZADO em toda a largura útil da faixa.
    area_x = pad_x
    area_w = W - 2 * pad_x
    lines, font = auto_fit_lines(
        draw, chamada_up, font_path, area_w,
        start_size=int(H * 0.040), min_size=22, max_lines=2,
    )
    line_h = int(font.size * 1.20)
    text_block_h = line_h * len(lines)

    content_h = text_block_h
    band_h = content_h + band_pad_y * 2

    # Terço inferior, com faixa de foto visível abaixo (~14%)
    band_y2 = int(H * 0.86)
    band_y1 = band_y2 - band_h

    fio_h = max(4, int(H * 0.005))
    draw.rectangle((0, band_y1 - fio_h, W, band_y1), fill=VERDE_LIMAO)
    draw.rectangle((0, band_y1, W, band_y2), fill=(*AZUL_PROFUNDO, 230))

    # Texto CENTRALIZADO na faixa inteira (horizontal e vertical).
    y_cursor = band_y1 + (band_h - text_block_h) // 2
    for ln in lines:
        lw = draw.textlength(ln, font=font)
        lx = area_x + (area_w - lw) / 2
        draw.text((lx, y_cursor), ln, font=font, fill=BRANCO)
        y_cursor += line_h

    # Logo SulTV no CANTO SUPERIOR ESQUERDO da imagem — fora da faixa-legenda
    # (correção Donário 2026-06-01). SEMPRE presente (cascata com fallback).
    logo_h_top = int(H * 0.085)
    logo, logo_origem = _logo_para_faixa(logo_h_top)
    max_logo_w = int(W * 0.20)
    if logo.width > max_logo_w:
        nh = max(1, int(logo.height * max_logo_w / logo.width))
        logo = logo.resize((max_logo_w, nh), Image.LANCZOS)
    margin_x = int(W * 0.035)
    margin_y = int(H * 0.035)
    canvas.paste(logo, (margin_x, margin_y), logo)

    # REVISÃO obrigatória — registra avisos se algo essencial faltar
    ok, motivos = revisar_faixa_legenda(chamada_lp, logo_origem, lines)
    if not ok:
        try:
            print('[faixa-legenda][REVISÃO] avisos: ' + '; '.join(motivos))
        except Exception:
            pass
    if logo_origem in ('watermark_acervo', 'wordmark'):
        try:
            print(f'[faixa-legenda] logo origem: {logo_origem} '
                  f'(logo oficial/Brand Kit indisponível — fallback)')
        except Exception:
            pass
    else:
        try:
            print(f'[faixa-legenda] logo origem: {logo_origem}')
        except Exception:
            pass

    buf = io.BytesIO()
    canvas.save(buf, format='JPEG', quality=92)
    return buf.getvalue()


# ---------- Upload Wix Media ----------

def upload_wix_media(image_bytes: bytes, filename: str,
                     mime_type: str = 'image/png') -> Optional[dict]:
    """Upload de imagem ao Wix Media. Retorna dict com {id, url, width, height} ou None.

    Usa WIX_SITE_TOKEN + WIX_SITE_ID do ambiente.
    Útil tanto para Wix Blog (coverMedia.id) quanto para Meta (image_url).
    """
    import json as _json
    tok = os.environ.get('WIX_SITE_TOKEN', '').strip()
    sid = os.environ.get('WIX_SITE_ID', '').strip()
    if not tok or not sid:
        return None
    try:
        # 1. Generate upload URL
        body = _json.dumps({'mimeType': mime_type, 'fileName': filename}).encode('utf-8')
        req = urllib.request.Request(
            'https://www.wixapis.com/site-media/v1/files/generate-upload-url',
            data=body,
            headers={'Authorization': tok, 'wix-site-id': sid, 'Content-Type': 'application/json'},
            method='POST',
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            upload_url = _json.loads(r.read())['uploadUrl']
        # 2. PUT image
        req2 = urllib.request.Request(
            upload_url, data=image_bytes,
            headers={'Content-Type': mime_type},
            method='PUT',
        )
        with urllib.request.urlopen(req2, timeout=60) as r:
            resp = _json.loads(r.read())
        f = resp.get('file', {})
        media = f.get('media', {}).get('image', {}).get('image', {})
        return {
            'id': f.get('id'),
            'url': f.get('url'),
            'width': media.get('width'),
            'height': media.get('height'),
            'filename': f.get('displayName'),
            'sizeInBytes': f.get('sizeInBytes'),
        }
    except urllib.error.HTTPError as e:
        print(f'[wix-media] HTTP {e.code}: {e.read()[:200].decode("utf-8","ignore")}')
        return None
    except Exception as e:
        print(f'[wix-media] {e.__class__.__name__}: {e}')
        return None


# ---------- CLI ----------

if __name__ == '__main__':
    import argparse, sys, json
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd')

    p1 = sub.add_parser('thumb')
    p1.add_argument('--titulo', required=True)
    p1.add_argument('--formato', default='1200x630', choices=list(FORMATOS.keys()))
    p1.add_argument('--frame-url', help='URL para extrair og:image')
    p1.add_argument('--kicker')
    p1.add_argument('--out', required=True)

    p2 = sub.add_parser('card')
    p2.add_argument('--numero', type=int, required=True)
    p2.add_argument('--total', type=int, required=True)
    p2.add_argument('--titulo', required=True)
    p2.add_argument('--texto', required=True)
    p2.add_argument('--formato', default='1080x1350')
    p2.add_argument('--out', required=True)

    args = ap.parse_args()
    if args.cmd == 'thumb':
        frame = None
        if args.frame_url:
            frame = extrair_og_image(args.frame_url)
            print(f"[og] {'OK' if frame else 'sem og:image'}", file=sys.stderr)
        data = gerar_thumb_branded(args.titulo, args.formato, frame_bytes=frame, kicker=args.kicker)
        with open(args.out, 'wb') as f:
            f.write(data)
        print(args.out)
    elif args.cmd == 'card':
        data = gerar_card_carrossel(args.numero, args.total, args.titulo, args.texto, formato=args.formato)
        with open(args.out, 'wb') as f:
            f.write(data)
        print(args.out)
    else:
        ap.print_help()
