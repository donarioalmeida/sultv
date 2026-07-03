#!/usr/bin/env python3
"""
sultv_cards.py — Gerador de artes SulTV para redes sociais.
================================================================
Padrão fechado com Donário (03/07/2026). Dois produtos:

  1. card_post()  → card único (Facebook e Instagram-imagem-única):
       foto real + tarja de manchete no rodapé + logo badge (sup. esq.), 4:5.

  2. carrossel()  → carrossel Instagram (formato #1 em engajamento):
       slide 1 = capa com foto (mesmo estilo do card)
       slides 2..N = conteúdo em template da marca (badge, manchete azul,
                     bullets, faixa de gradiente, símbolo "S", contador)
       slide final = CTA (logo + site + @sultv31)
     Só a capa precisa de foto — resolve a escassez de banco de imagens.

Regras de marca aplicadas (Brand Kit SulTV v1.0):
  - Fonte Outfit; paleta oficial (#166897 / #198FA1 / #8BC751 / #1A4F6B ...)
  - Manchete SEMPRE em tarja/caixa sólida (nunca solta sobre a foto)
  - Logo badge branco arredondado no canto superior esquerdo
  - Gradiente oficial (turquesa→verde) em faixas/divisores
  - Formato 4:5 (1080x1350) — recomendado pela Meta para feed
"""
from __future__ import annotations
import io
import os
from PIL import Image, ImageDraw, ImageFont

# ============================================================
# Caminhos de assets — resolve do REPO (assets/) OU do Mac (Brand Kit)
# ============================================================
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO_ASSETS = os.path.normpath(os.path.join(_HERE, "..", "assets"))  # scripts/../assets
BASE = os.path.expanduser("~/Meu Drive/CONEX — Holding & Hub/02_SulTV")
BK = f"{BASE}/Marketing e Marca/MKT - Marca/Brand_Kit_SulTV_v1"

def _asset(repo_sub: str, mac_full: str) -> str:
    """Prioriza o asset empacotado no repo (cloud); cai pro Brand Kit local (Mac)."""
    p = os.path.join(_REPO_ASSETS, repo_sub)
    return p if os.path.exists(p) else mac_full

F_BOLD = _asset("fonts/Outfit-Bold.ttf",     f"{BK}/03_Tipografia/Outfit_Fonts/Outfit-Bold.ttf")
F_SEMI = _asset("fonts/Outfit-SemiBold.ttf", f"{BK}/03_Tipografia/Outfit_Fonts/Outfit-SemiBold.ttf")
F_REG  = _asset("fonts/Outfit-Regular.ttf",  f"{BK}/03_Tipografia/Outfit_Fonts/Outfit-Regular.ttf")
LOGO_GRAD    = _asset("logos/01_SulTV_HOR_gradiente_1500px.png",   f"{BK}/09_Logos todos /01_SulTV_HOR_gradiente_1500px.png")
LOGO_VERT_BR = _asset("logos/08_SulTV_VERT_branco_2000px.png",     f"{BK}/09_Logos todos /08_SulTV_VERT_branco_2000px.png")
SIMB_GRAD    = _asset("logos/12_SulTV_simbolo_gradiente_1500px.png", f"{BK}/09_Logos todos /12_SulTV_simbolo_gradiente_1500px.png")
SIMB_BR      = _asset("logos/13_SulTV_simbolo_branco_800px.png",   f"{BK}/09_Logos todos /13_SulTV_simbolo_branco_800px.png")
LOGO_SQ      = _asset("logos/SULTV_quadrado_vertical_alpha.png",   f"{BASE}/Conteúdo Digital/sultv-radar-conteudo/references/SULTV_quadrado_vertical_alpha.png")

# ============================================================
# Paleta oficial
# ============================================================
AZUL   = (22, 104, 151)    # #166897 Azul Profundo
TURQ   = (25, 143, 161)    # #198FA1 Turquesa
VERDE  = (139, 199, 81)    # #8BC751 Verde-Limão
PRETO  = (15, 27, 38)      # #0F1B26 Preto Editorial
CINZA  = (107, 119, 133)   # #6B7785 Cinza Editorial
BRANCO = (255, 255, 255)
AZUL_TARJA = (26, 79, 107)   # #1A4F6B tarja de manchete
AZUL_CLARO = (146, 214, 227) # #92D6E3 auxiliar

W, H = 1080, 1350   # 4:5
MX = 76             # margem lateral

# cor do badge por editoria
BADGE_COR = {
    "NOTÍCIA": AZUL, "CLIMA": TURQ, "SEGURANÇA": AZUL, "ECONOMIA": AZUL,
    "COMUNIDADE": VERDE, "ESPORTE": TURQ, "SAÚDE": TURQ, "EDUCAÇÃO": AZUL,
    "SERVIÇO": VERDE, "AGRO": VERDE, "CULTURA": TURQ,
}

# ============================================================
# Helpers de texto
# ============================================================
def _wrap(d, t, f, mw):
    ws, ls, cur = t.split(), [], ""
    for w in ws:
        tt = (cur + " " + w).strip()
        if d.textbbox((0, 0), tt, font=f)[2] <= mw:
            cur = tt
        else:
            if cur:
                ls.append(cur)
            cur = w
    if cur:
        ls.append(cur)
    return ls

def _fit(d, t, mw, fp, start, mn, ml):
    for s in range(start, mn - 1, -2):
        f = ImageFont.truetype(fp, s)
        ls = _wrap(d, t, f, mw)
        if len(ls) <= ml:
            return ls, f
    return _wrap(d, t, ImageFont.truetype(fp, mn), mw)[:ml], ImageFont.truetype(fp, mn)

def _grad_bar(canvas, h=14, y=0):
    """Faixa de gradiente oficial turquesa→verde (horizontal)."""
    bar = Image.new("RGB", (W, h), TURQ)
    px = bar.load()
    for x in range(W):
        r = x / (W - 1)
        px_col = tuple(int(TURQ[i] + (VERDE[i] - TURQ[i]) * r) for i in range(3))
        for yy in range(h):
            px[x, yy] = px_col
    canvas.paste(bar, (0, y))

def _crop_45(src):
    """Center-crop inteligente para 4:5."""
    tw, th = W, H
    sw, sh = src.size
    tr, cr = tw / th, sw / sh
    if cr > tr:
        nw = int(sh * tr); left = (sw - nw) // 2
        src = src.crop((left, 0, left + nw, sh))
    else:
        nh = int(sw / tr); top = (sh - nh) // 2
        src = src.crop((0, top, sw, top + nh))
    return src.resize((tw, th), Image.LANCZOS)

def _logo_badge(canvas, x=40, y=40, size=140):
    logo = Image.open(LOGO_SQ).convert("RGBA")
    pad = 20; lw = size - pad * 2; lh = int(logo.height * (lw / logo.width))
    logo = logo.resize((lw, lh), Image.LANCZOS)
    card = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size, size], radius=24, fill=255)
    card.paste(logo, ((size - lw) // 2, (size - lh) // 2), logo)
    canvas.paste(card, (x, y), mask)

def _logo_grad(canvas, x=MX, y=None, th=80):
    logo = Image.open(LOGO_GRAD).convert("RGBA")
    tw = int(logo.width * (th / logo.height)); logo = logo.resize((tw, th), Image.LANCZOS)
    canvas.alpha_composite(logo, (x, y if y is not None else H - th - 70))

def _s_watermark(canvas, alpha=32, size=680):
    s = Image.open(SIMB_GRAD).convert("RGBA")
    tw = size; th = int(s.height * (tw / s.width)); s = s.resize((tw, th), Image.LANCZOS)
    a = s.split()[3].point(lambda v: int(v * alpha / 255)); s.putalpha(a)
    canvas.alpha_composite(s, (W - int(tw * 0.62), H - int(th * 0.60)))

def _contador(d, num, total, dark=False):
    txt = f"{num} / {total}"; f = ImageFont.truetype(F_BOLD, 30)
    b = d.textbbox((0, 0), txt, font=f); tw, th = b[2] - b[0], b[3] - b[1]
    x2 = W - MX; x1 = x2 - tw - 40; y1 = 60; y2 = y1 + th + 26
    d.rounded_rectangle([x1, y1, x2, y2], radius=(y2 - y1) // 2,
                        fill=(15, 27, 38, 150) if dark else AZUL_CLARO)
    d.text((x1 + 20, y1 + 13 - b[1]), txt, font=f, fill=BRANCO if dark else AZUL)

def _tarja_manchete(canvas, d, manchete):
    """Tarja azul no rodapé + borda de gradiente + manchete branca CAIXA ALTA."""
    ls, f = _fit(d, manchete.upper(), W - 120, F_BOLD, 64, 42, 3)
    lh = int(f.size * 1.16)
    th = 44 + len(ls) * lh + 96
    ty = H - th
    d.rectangle([0, ty, W, H], fill=AZUL_TARJA)
    _grad_bar(canvas, h=8, y=ty)
    y = ty + 44
    for ln in ls:
        b = d.textbbox((0, 0), ln, font=f)
        d.text(((W - (b[2] - b[0])) // 2, y - b[1]), ln, font=f, fill=BRANCO)
        y += lh
    return ty

# ============================================================
# 1) CARD ÚNICO — Facebook / Instagram-imagem-única
# ============================================================
def card_post(foto_bytes: bytes, manchete: str, out_path: str,
              arraste: bool = False) -> str:
    """Foto real + tarja de manchete + logo badge (4:5). Usado no Facebook e
    no Instagram quando o formato é imagem única. `arraste=True` acrescenta o
    indicador de swipe (só faz sentido em capa de carrossel)."""
    src = Image.open(io.BytesIO(foto_bytes)).convert("RGB")
    c = _crop_45(src).convert("RGBA")
    d = ImageDraw.Draw(c)
    _grad_bar(c, h=14, y=0)
    ty = _tarja_manchete(c, d, manchete)
    if arraste:
        sf = ImageFont.truetype(F_SEMI, 32); st = "arraste  →"
        b = d.textbbox((0, 0), st, font=sf)
        d.text(((W - (b[2] - b[0])) // 2, H - 58), st, font=sf, fill=(210, 230, 245))
    _logo_badge(c)
    c.convert("RGB").save(out_path, "JPEG", quality=92)
    return out_path

# ============================================================
# 2) CARROSSEL — Instagram
# ============================================================
def _slide_conteudo(badge, titulo, linhas, out, num, total):
    c = Image.new("RGBA", (W, H), (255, 255, 255, 255))
    # leve tom azul-claro no rodapé
    tint = Image.new("RGBA", (W, H), (0, 0, 0, 0)); td = ImageDraw.Draw(tint)
    for y in range(int(H * 0.72), H):
        a = int(26 * ((y - H * 0.72) / (H * 0.28)))
        td.line([(0, y), (W, y)], fill=(146, 214, 227, a))
    c = Image.alpha_composite(c, tint)
    _s_watermark(c)
    _grad_bar(c, h=14, y=0)
    d = ImageDraw.Draw(c)
    _contador(d, num, total)
    # badge
    bf = ImageFont.truetype(F_BOLD, 34); bt = badge.upper()
    bcor = BADGE_COR.get(bt, AZUL)
    bb = d.textbbox((0, 0), bt, font=bf); bw, bh = bb[2] - bb[0], bb[3] - bb[1]
    d.rounded_rectangle([MX, 64, MX + bw + 48, 64 + bh + 34], radius=7, fill=bcor)
    d.text((MX + 24, 64 + 17 - bb[1]), bt, font=bf, fill=BRANCO)
    # título
    ty = 64 + bh + 34 + 56
    tl, tf = _fit(d, titulo, W - MX * 2, F_BOLD, 74, 46, 3); tlh = int(tf.size * 1.12)
    for ln in tl:
        d.text((MX, ty), ln, font=tf, fill=AZUL); ty += tlh
    ty += 42
    # bullets (marcador gradiente verde+turquesa)
    lf = ImageFont.truetype(F_SEMI, 42)
    for item in linhas:
        d.ellipse([MX, ty + 13, MX + 20, ty + 33], fill=VERDE)
        d.ellipse([MX + 5, ty + 18, MX + 15, ty + 28], fill=TURQ)
        for ln in _wrap(d, item, lf, W - MX * 2 - 46):
            d.text((MX + 46, ty), ln, font=lf, fill=PRETO); ty += int(lf.size * 1.28)
        ty += 24
    _logo_grad(c)
    c.convert("RGB").save(out, "JPEG", quality=92)
    return out

def _slide_cta(out, num, total, titulo="Fique por dentro do que importa no Sul"):
    c = Image.new("RGBA", (W, H), AZUL + (255,))
    s = Image.open(SIMB_BR).convert("RGBA")
    tw = 720; th = int(s.height * (tw / s.width)); s = s.resize((tw, th), Image.LANCZOS)
    a = s.split()[3].point(lambda v: int(v * 22 / 255)); s.putalpha(a)
    c.alpha_composite(s, (W - int(tw * 0.55), H - int(th * 0.5)))
    _grad_bar(c, h=14, y=0)
    d = ImageDraw.Draw(c); _contador(d, num, total, dark=True)
    logo = Image.open(LOGO_VERT_BR).convert("RGBA"); tl = 300; twl = int(logo.width * (tl / logo.height))
    logo = logo.resize((twl, tl), Image.LANCZOS); c.alpha_composite(logo, ((W - twl) // 2, 170))
    d = ImageDraw.Draw(c)
    tf, f = _fit(d, titulo, W - MX * 2, F_BOLD, 62, 44, 2); ty = 560
    for ln in tf:
        b = d.textbbox((0, 0), ln, font=f)
        d.text(((W - (b[2] - b[0])) // 2, ty), ln, font=f, fill=BRANCO); ty += int(f.size * 1.15)
    ty += 44; sf = ImageFont.truetype(F_SEMI, 40)
    for ln in ["Leia a matéria completa no site", "sultv.com.br", "",
               "Siga @sultv31 no Instagram e Facebook"]:
        b = d.textbbox((0, 0), ln, font=sf); col = VERDE if "sultv.com.br" in ln else BRANCO
        d.text(((W - (b[2] - b[0])) // 2, ty), ln, font=sf, fill=col); ty += 54
    c.convert("RGB").save(out, "JPEG", quality=92)
    return out

def carrossel(foto_bytes: bytes, capa_manchete: str, slides: list, out_dir: str,
              prefixo: str = "slide") -> list:
    """Gera o carrossel completo. `slides` = lista de dicts
    {"badge": "Clima", "titulo": "...", "linhas": ["...","..."]}.
    Retorna a lista de caminhos na ordem (capa, conteúdo..., CTA)."""
    os.makedirs(out_dir, exist_ok=True)
    total = 1 + len(slides) + 1
    paths = []
    # capa
    p = os.path.join(out_dir, f"{prefixo}_1.jpg")
    src = Image.open(io.BytesIO(foto_bytes)).convert("RGB")
    c = _crop_45(src).convert("RGBA"); d = ImageDraw.Draw(c)
    _grad_bar(c, h=14, y=0); _contador(d, 1, total, dark=True)
    _tarja_manchete(c, d, capa_manchete)
    sf = ImageFont.truetype(F_SEMI, 32); st = "arraste  →"
    b = d.textbbox((0, 0), st, font=sf)
    d.text(((W - (b[2] - b[0])) // 2, H - 58), st, font=sf, fill=(210, 230, 245))
    _logo_badge(c)
    c.convert("RGB").save(p, "JPEG", quality=92); paths.append(p)
    # conteúdo
    for i, s in enumerate(slides, start=2):
        p = os.path.join(out_dir, f"{prefixo}_{i}.jpg")
        _slide_conteudo(s["badge"], s["titulo"], s["linhas"], p, i, total)
        paths.append(p)
    # CTA
    p = os.path.join(out_dir, f"{prefixo}_{total}.jpg")
    _slide_cta(p, total, total); paths.append(p)
    return paths


if __name__ == "__main__":
    # smoke test
    import sys
    S = "/private/tmp/claude-501/-Users-donariolopesdealmeida-Meu-Drive-CONEX---Holding---Hub/16e85611-2f63-4aef-8136-3ec54227d53f/scratchpad"
    foto = open(f"{S}/foto_materia.jpg", "rb").read()
    card_post(foto, "Julho terá mais chuva, frio e risco de temporais no RS",
              f"{S}/_test_card.jpg")
    paths = carrossel(foto, "Julho terá mais chuva, frio e risco de temporais no RS",
        [
            {"badge": "Clima", "titulo": "Como fica o mês",
             "linhas": ["Dias 7 a 9: ar polar e frio mais intenso",
                        "Dia 11: ciclone no litoral e risco de temporais",
                        "A partir do dia 12: nova massa de ar frio"]},
            {"badge": "Clima", "titulo": "Chuva acima da média",
             "linhas": ["Maiores volumes no Noroeste do estado",
                        "Sul e Sudoeste dentro do padrão",
                        "Temperaturas abaixo da média, frio na 1ª quinzena"]},
            {"badge": "Serviço", "titulo": "O que fazer nas cidades",
             "linhas": ["Guarda-chuva sempre à mão",
                        "Evite áreas alagáveis nas pancadas fortes",
                        "Acompanhe os alertas oficiais antes de sair"]},
        ],
        out_dir=f"{S}/_test_carousel")
    print("OK card:", f"{S}/_test_card.jpg")
    print("OK carrossel:", len(paths), "slides")
