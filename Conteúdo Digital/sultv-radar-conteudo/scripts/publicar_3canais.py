#!/usr/bin/env python3
"""
publicar_3canais.py — Orquestrador de publicação SulTV (Site + Facebook + Instagram).
=====================================================================================
Padrão fechado com Donário (03/07/2026). Recebe UMA matéria estruturada e publica:

  📰 SITE (Wix Blog): título + linha fina + lead + imagem + H2 + fecho + CTA social.
  📘 FACEBOOK: card (foto + tarja manchete + logo) + legenda contexto ampliado.
  📱 INSTAGRAM: carrossel OU imagem única (decisão por pauta) + legenda 60-70 palavras.

Contrato da matéria (dict):
{
  "titulo": "...",                      # manchete SEO
  "linha_fina": "...",                  # 1 frase (deck), abaixo do título
  "categoria": "Clima",                 # editoria (badge)
  "tag_principal": "clima",             # p/ categoria Wix
  "cidade": "",                         # opcional
  "url_fonte": "https://...",           # de onde extrair a og:image (Regra 12: NUNCA citada no texto)
  "lead": "1º parágrafo (5W+H)",
  "secoes": [{"h2": "...", "paragrafos": ["...", "..."]}],
  "fecho": "parágrafo de fecho",
  "legenda_foto": "legenda da imagem (<=120)",
  "caption_social": "legenda p/ Face e Insta (hook+contexto+CTA)",
  "hashtags": ["Clima", "CostaDoce", "SulTV"],
  "ig_formato": "auto"|"carrossel"|"unica",
  "ig_slides": [{"badge","titulo","linhas"}]   # usados se carrossel
}

Regra de decisão IG (auto): carrossel quando há >=2 seções com dados/tópicos
(desdobramento); imagem única para fato pontual.

CTA/links oficiais: site sultv.com.br · Facebook facebook.com/SulTV31 · Instagram instagram.com/sultv31
"""
from __future__ import annotations
import os
import sys
import time
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import produzir_materia as pm
import sultv_cards as cards

FB_URL = "https://www.facebook.com/SulTV31/"
IG_URL = "https://www.instagram.com/sultv31/"
SITE = "sultv.com.br"
SCRATCH = "/tmp/sultv_3canais"

def _env():
    """Carrega .env do radar (idempotente)."""
    envf = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.exists(envf):
        for line in open(envf):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k, v)

# ============================================================
# SITE (Wix) — richContent enriquecido
# ============================================================
def _heading(txt):
    return {"type": "HEADING", "id": pm._node_id(), "nodes": [pm._text_node(txt)],
            "headingData": {"level": 2, "textStyle": {"textAlignment": "AUTO"}}}

def _tlink(txt, url):
    return {"type": "TEXT", "id": pm._node_id(), "nodes": [],
            "textData": {"text": txt, "decorations": [
                {"type": "LINK", "linkData": {"link": {"url": url, "target": "BLANK"}}},
                {"type": "BOLD", "fontWeightValue": 700}]}}

def _build_richcontent(m: dict, cover: dict | None) -> dict:
    nodes = []
    # linha fina (deck em negrito)
    nodes.append({"type": "PARAGRAPH", "id": pm._node_id(),
                  "nodes": [pm._text_node(m["linha_fina"], bold=True)],
                  "paragraphData": {"textStyle": {"textAlignment": "AUTO"}}})
    # lead
    pm._append_block(nodes, pm._paragraph(m["lead"]))
    # imagem + legenda (logo após o lead)
    if cover and cover.get("id"):
        pm._append_block(nodes, pm._image_node(cover["id"], cover["url"],
                         cover.get("width") or 1200, cover.get("height") or 675,
                         (m.get("legenda_foto") or m["titulo"])[:140]))
        if m.get("legenda_foto"):
            nodes.append(pm._caption_node(m["legenda_foto"]))
    # seções (H2 + parágrafos)
    for sec in m.get("secoes", []):
        pm._append_block(nodes, _heading(sec["h2"]))
        for p in sec["paragrafos"]:
            pm._append_block(nodes, pm._paragraph(p))
    # fecho
    if m.get("fecho"):
        pm._append_block(nodes, pm._paragraph(m["fecho"]))
    # CTA social com links
    pm._append_block(nodes, {"type": "PARAGRAPH", "id": pm._node_id(), "nodes": [
        pm._text_node("📱 Gostou? Acompanhe a SulTV no "),
        _tlink("Facebook", FB_URL), pm._text_node(" e no "), _tlink("Instagram", IG_URL),
        pm._text_node(" para receber as próximas notícias da sua região.")
    ], "paragraphData": {"textStyle": {"textAlignment": "AUTO"}}})
    return {"nodes": nodes}

def publicar_site(m: dict, dry=False) -> dict:
    """Publica no Wix Blog. Retorna {url, post_id, cover}."""
    token = pm._wix_token_valido()
    if not token:
        return {"erro": "sem token Wix"}
    headers = {"Authorization": token, "Content-Type": "application/json"}
    site_id = os.getenv("WIX_SITE_ID", "").strip()
    if site_id:
        headers["wix-site-id"] = site_id

    # objeto compatível com _gerar_e_subir_capa (usa og:image da fonte, sem overlay)
    from types import SimpleNamespace
    mm = SimpleNamespace(titulo_sultv=m["titulo"], subtitulo=m["linha_fina"],
                         tag_principal=m.get("tag_principal", ""), cidade=m.get("cidade", ""),
                         url=m.get("url_fonte", ""), id_hash=m.get("slug", m["titulo"])[:24],
                         fonte_nome="", briefing_visual={})
    cover = None if dry else pm._gerar_e_subir_capa(mm)

    body = {
        "title": m["titulo"],
        "excerpt": m["linha_fina"],
        "richContent": _build_richcontent(m, cover),
        "seoSlug": pm._slug_ascii(m["titulo"]),
    }
    member_id = os.getenv("WIX_MEMBER_ID", "").strip()
    if member_id:
        body["memberId"] = member_id
    try:
        from wix_taxonomia import categorias_para_materia
        cats = categorias_para_materia(tag_principal=m.get("tag_principal", ""),
                                       cidade=m.get("cidade", ""), tags_secundarias=[])
        if cats:
            body["categoryIds"] = cats
    except Exception as e:
        print(f"[site] categorias falharam: {e}")
    if cover and cover.get("id"):
        body["media"] = {"wixMedia": {"image": {"id": cover["id"], "url": cover["url"],
                         "width": cover.get("width") or 1200, "height": cover.get("height") or 675,
                         "altText": (m.get("legenda_foto") or m["titulo"])[:140]}},
                         "displayed": True, "custom": False}
    if dry:
        return {"dry": True, "richcontent_nodes": len(body["richContent"]["nodes"]),
                "categoryIds": body.get("categoryIds"), "slug": body["seoSlug"]}

    r = requests.post(f"{pm.WIX_API}?publish=true", headers=headers, json={"draftPost": body}, timeout=40)
    r.raise_for_status()
    draft = r.json()["draftPost"]
    pid = draft["id"]
    url = pm._url_publica_do_post(pid, headers, fallback=f"https://www.{SITE}/post/{body['seoSlug']}")
    return {"url": url, "post_id": pid, "cover": cover}

# ============================================================
# FACEBOOK
# ============================================================
def publicar_facebook(m: dict, foto_bytes: bytes, dry=False) -> dict:
    os.makedirs(SCRATCH, exist_ok=True)
    card = cards.card_post(foto_bytes, m["titulo"], f"{SCRATCH}/fb_card.jpg")
    msg = m["caption_social"]
    if dry:
        return {"dry": True, "card": card, "msg_len": len(msg)}
    token = os.getenv("META_LONG_LIVED_TOKEN", "").strip()
    page = os.getenv("META_FB_PAGE_ID", "").strip()
    with open(card, "rb") as img:
        r = requests.post(f"https://graph.facebook.com/v19.0/{page}/photos",
                          data={"message": msg, "access_token": token},
                          files={"source": img}, timeout=40)
    d = r.json()
    return {"post_id": d.get("post_id") or d.get("id"), "status": r.status_code}

# ============================================================
# INSTAGRAM
# ============================================================
def _decidir_formato_ig(m: dict) -> str:
    if m.get("ig_formato") in ("carrossel", "unica"):
        return m["ig_formato"]
    # auto: carrossel se há >=2 seções com tópicos (desdobramento)
    secoes = m.get("secoes", [])
    return "carrossel" if len(secoes) >= 2 else "unica"

def _ig_publish_graph(image_urls: list, caption: str) -> dict:
    """Publica no IG via Graph API (container + publish). 1 img = feed; 2+ = carrossel."""
    token = os.getenv("META_LONG_LIVED_TOKEN", "").strip()
    ig = os.getenv("META_IG_BUSINESS_ID", "").strip()
    base = f"https://graph.facebook.com/v19.0/{ig}"
    if len(image_urls) == 1:
        c = requests.post(f"{base}/media", data={"image_url": image_urls[0],
                          "caption": caption, "access_token": token}, timeout=40).json()
        cid = c["id"]
    else:
        children = []
        for u in image_urls:
            r = requests.post(f"{base}/media", data={"image_url": u, "is_carousel_item": "true",
                              "access_token": token}, timeout=40).json()
            children.append(r["id"])
        c = requests.post(f"{base}/media", data={"media_type": "CAROUSEL",
                          "children": ",".join(children), "caption": caption,
                          "access_token": token}, timeout=40).json()
        cid = c["id"]
    time.sleep(2)  # container precisa processar
    pub = requests.post(f"{base}/media_publish", data={"creation_id": cid,
                        "access_token": token}, timeout=40).json()
    return pub

def publicar_instagram(m: dict, foto_bytes: bytes, dry=False) -> dict:
    os.makedirs(SCRATCH, exist_ok=True)
    fmt = _decidir_formato_ig(m)
    if fmt == "carrossel":
        slides = m.get("ig_slides") or [
            {"badge": s.get("h2_badge", m["categoria"]), "titulo": s["h2"],
             "linhas": s["paragrafos"]} for s in m.get("secoes", [])]
        paths = cards.carrossel(foto_bytes, m["titulo"], slides, out_dir=f"{SCRATCH}/ig")
    else:
        paths = [cards.card_post(foto_bytes, m["titulo"], f"{SCRATCH}/ig_single.jpg")]
    if dry:
        return {"dry": True, "formato": fmt, "slides": len(paths)}
    # hospedar imagens no Wix Media p/ URLs públicas
    from imagens import upload_wix_media
    urls = []
    for i, p in enumerate(paths, 1):
        info = upload_wix_media(open(p, "rb").read(), f"ig_{m.get('slug','post')}_{i}.jpg", mime_type="image/jpeg")
        urls.append(info["url"])
    pub = _ig_publish_graph(urls, m["caption_social"])
    return {"formato": fmt, "slides": len(paths), "publish": pub}

# ============================================================
# ORQUESTRADOR
# ============================================================
def publicar_materia(m: dict, dry=False) -> dict:
    _env()
    out = {"titulo": m["titulo"]}
    # 1. Site (primeiro — gera a foto/cover e a URL da matéria)
    print("📰 Publicando no SITE...")
    out["site"] = publicar_site(m, dry=dry)
    # obter og:image da fonte p/ Face e Insta (mesma foto do site)
    from imagens import extrair_og_image
    foto = extrair_og_image(m.get("url_fonte", ""), timeout=15) if m.get("url_fonte") else None
    if not foto:
        print("⚠️  sem og:image — Face/Insta serão pulados")
        return out
    # 2. Facebook
    print("📘 Publicando no FACEBOOK...")
    out["facebook"] = publicar_facebook(m, foto, dry=dry)
    # 3. Instagram
    print("📱 Publicando no INSTAGRAM...")
    out["instagram"] = publicar_instagram(m, foto, dry=dry)
    return out


if __name__ == "__main__":
    import json
    dry = "--dry-run" in sys.argv
    # matéria de teste (clima julho)
    materia = {
        "titulo": "Julho começa com frentes frias em sequência e chuva acima da média no RS",
        "linha_fina": "Meteorologia prevê entrada de ar polar, ciclone extratropical no litoral e risco de temporais ao longo do mês. Veja o que esperar e como se preparar na Costa Doce.",
        "categoria": "Clima", "tag_principal": "clima", "cidade": "",
        "url_fonte": "https://agenciagbc.com/2026/07/01/julho-tera-mais-chuva-e-frio-no-rs-com-risco-de-temporais-veja-o-que-a-meteorologia-preve-para-o-mes/",
        "lead": "O mês de julho começou com o tempo instável em todo o Rio Grande do Sul. A previsão dos principais centros de meteorologia aponta uma sucessão de frentes frias, entrada de ar polar e chuva acima da média na maior parte do estado — cenário que pede atenção de quem vive nas cidades da Costa Doce e do Sul gaúcho.",
        "secoes": [
            {"h2": "Como fica o tempo ao longo do mês",
             "paragrafos": ["Já nos primeiros dias, uma frente fria com ar polar derruba as temperaturas. Entre os dias 7 e 9, uma nova massa de ar polar mantém o frio intenso, e por volta do dia 11 um ciclone extratropical no litoral eleva o risco de temporais. A partir do dia 12, outra massa de ar frio chega ao estado."],
             "h2_badge": "Clima"},
            {"h2": "O que muda no dia a dia das cidades",
             "paragrafos": ["A combinação de chuva e temporais aumenta o risco de alagamentos em pontos baixos, transtornos no trânsito e quedas de energia. A orientação é manter o guarda-chuva à mão, evitar áreas alagáveis nas pancadas fortes e acompanhar os alertas oficiais antes de sair de casa."],
             "h2_badge": "Serviço"},
        ],
        "fecho": "A SulTV segue acompanhando a evolução do tempo na Costa Doce e no Sul do estado.",
        "legenda_foto": "Mês terá tempo instável no RS, com frio, chuva e risco de temporais.",
        "caption_social": "🌧️ Julho começou instável no Rio Grande do Sul — e o tempo não dá trégua nas próximas semanas. Frentes frias em sequência, ar polar e um ciclone no litoral por volta do dia 11 elevam o risco de temporais e chuva acima da média. Arraste para ver o que esperar e como se preparar na sua cidade. 📲 Matéria completa no site (link na bio).\n\n#Clima #CostaDoce #RioGrandeDoSul #SulTV",
        "hashtags": ["Clima", "CostaDoce", "SulTV"],
        "ig_formato": "auto",
        "slug": "julho-frentes-frias-teste",
    }
    res = publicar_materia(materia, dry=dry)
    print(json.dumps(res, ensure_ascii=False, indent=2))
