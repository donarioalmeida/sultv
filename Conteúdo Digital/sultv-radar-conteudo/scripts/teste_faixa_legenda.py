#!/usr/bin/env python3
"""teste_faixa_legenda.py — MOCKUP para aprovação de Donário (2026-05-29).

Aplica a FAIXA-LEGENDA padrão SulTV (estilo @sultv31) sobre a foto dos posts,
seguindo os exemplos enviados: foto nítida + faixa azul full-width com chamada
SEO em branco/uppercase + fio verde-limão + logo SulTV + listra gradiente.

NÃO publica nada. Apenas gera PNGs em outputs/ para revisão.
Não altera o pipeline automático (Regra 8 — imagem limpa — segue valendo no fluxo diário).
"""
from __future__ import annotations
import io, os, sys
from pathlib import Path
import requests
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import imagens as IM  # cores, fontes, logo, crop

# Corrige base do Brand Kit para o mount desta sessão (Outfit + logo branco)
_BK = "/sessions/nifty-gifted-meitner/mnt/Marketing e Marca/MKT - Marca/Brand_Kit_SulTV_v1"
IM.BRAND_KIT_BASE = _BK
IM.SANDBOX_BASE = _BK
IM._LOGO_CACHE.clear()

OUT = Path("/sessions/nifty-gifted-meitner/mnt/outputs")
OUT.mkdir(exist_ok=True)

W, H = 1080, 1350  # IG feed 4:5


def _baixar(url: str) -> bytes:
    r = requests.get(url, headers={"User-Agent": "SulTV-Radar/1.0"}, timeout=20)
    r.raise_for_status()
    return r.content


def gerar_faixa_legenda(foto_bytes: bytes, chamada: str, fonte_credito: str = "") -> bytes:
    """Wrapper de teste: faz smart-crop p/ 1080x1350 e chama a função OFICIAL
    do pipeline (imagens.aplicar_faixa_legenda) — fonte única de verdade.
    """
    src = Image.open(io.BytesIO(foto_bytes)).convert("RGB")
    cropped = IM._crop_para_aspecto(src, W, H)
    buf = io.BytesIO()
    cropped.save(buf, format="JPEG", quality=95)
    return IM.aplicar_faixa_legenda(buf.getvalue(), chamada)


POSTS = [
    {
        "slug": "la_pedras_altas",
        "chamada": "Cadeia da lã gaúcha se reúne em Pedras Altas",
        "foto_url": "https://static.wixstatic.com/media/04c4c0_11b1b2e0620148238cb97324a6e4df3a~mv2.jpg",
        "credito": "Gemini / Redação SulTV",
    },
    {
        "slug": "vale_dos_vinhedos",
        "chamada": "Vale dos Vinhedos quer R$ 27,5 milhões em infraestrutura",
        "foto_url": "https://static.wixstatic.com/media/04c4c0_3d8f7c705251433e89aa93dd99a2f35f~mv2.jpg",
        "credito": "Gemini / Redação SulTV",
    },
]


def main():
    for p in POSTS:
        try:
            foto = _baixar(p["foto_url"])
            origem = "wix"
        except Exception as e:
            print(f"[teste] download falhou ({e}); usando gradiente de fallback")
            foto = IM.gerar_gradiente_oficial(W, H, vertical=True).tobytes()
            origem = "fallback"
        out_bytes = gerar_faixa_legenda(foto, p["chamada"], p["credito"])
        dest = OUT / f"teste_faixa_{p['slug']}_1080x1350.jpg"
        dest.write_bytes(out_bytes)
        print(f"[teste] {p['slug']}: {dest} ({len(out_bytes)//1024} KB) origem_foto={origem}")


if __name__ == "__main__":
    main()
