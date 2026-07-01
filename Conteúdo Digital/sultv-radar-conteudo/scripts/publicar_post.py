"""
publicar_post.py — Instagram + Facebook via Meta Graph API
============================================================
Recebe MateriaPronta com post_instagram OU card_carrossel preenchido
e publica como post (single image) ou carrossel.

Tom institucional Redação SulTV (terceira pessoa, CTA tipo
"Análise completa em www.sultv.com.br" — nunca "salva esse vídeo").
"""
from __future__ import annotations
import json
import os
import requests
from datetime import datetime


META_GRAPH = "https://graph.facebook.com/v20.0"


def _ig_account_id() -> str:
    """ID da conta Instagram Business da SulTV (cacheado em env)."""
    return os.environ["META_IG_BUSINESS_ID"]


def _fb_page_id() -> str:
    return os.environ["META_FB_PAGE_ID"]


def _token() -> str:
    return os.environ["META_LONG_LIVED_TOKEN"]


# Emoji de gancho por tag editorial (usado só no IG, onde emoji puxa o olho).
_EMOJI_TAG = {
    "agro": "🌾", "economia": "💰", "mercado": "💰", "politica_local": "🏛️",
    "seguranca": "🚨", "saude": "🏥", "clima": "🌧️", "tecnologia": "⚙️",
    "evento": "📅", "cultura": "🎭", "esporte": "⚽", "outro": "📣",
}


def _link_artigo(m) -> str:
    """URL específica da matéria no site, se existir, para o CTA do post.

    Preenchida pelo orquestrador (fase_publicar) após publicar a matéria, ou
    pela angulação via campo `url_artigo`. Sem isso, o CTA não inventa link.
    """
    return (getattr(m, "url_artigo", "") or "").strip()


def _formatar_caption(m, rede: str = "ig", link_artigo: str = "") -> str:
    """Monta a legenda do post, com variação por rede e gancho no início.

    Correção/melhoria Donário 2026-05-21:
      1. Corpo = `post_instagram.caption` (texto completo da angulação) →
         fallback `linha_1_hook` + `corpo_3_linhas` → lead/subtítulo/título.
         (Antes o corpo era DESCARTADO e sobrava só o CTA + hashtags.)
      2. Gancho front-load: o IG ganha um emoji-âncora por tag no início da
         1ª linha (cultura de scroll-stop); o FB fica em texto limpo.
      3. CTA inteligente:
         - link específico da matéria, se houver (em vez da home genérica);
         - senão "Análise completa em www.sultv.com.br" só quando há matéria
           longa/nota publicável;
         - senão assinatura de marca.
      4. Hashtags: IG leva todas; FB no máx. 3 (lá não rendem e poluem).
    """
    p = getattr(m, "post_instagram", None) or {}
    rede = (rede or "ig").lower()

    # 1. Corpo
    corpo = (p.get("caption") or "").strip()
    if not corpo:
        partes = [(p.get("linha_1_hook") or "").strip()]
        partes += [l.strip() for l in (p.get("corpo_3_linhas") or []) if l and l.strip()]
        corpo = "\n".join(x for x in partes if x).strip()
    if not corpo:
        corpo = ((getattr(m, "lead", "") or getattr(m, "subtitulo", "")
                  or getattr(m, "titulo_sultv", "")) or "").strip()

    # 2. Gancho — só no IG, e só se o texto ainda não abre com emoji.
    if rede == "ig" and corpo:
        primeiro = corpo[:1]
        if primeiro.isalnum() or primeiro in "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÂÊÔÃÕÇ":
            emoji = _EMOJI_TAG.get(getattr(m, "tag_principal", ""), "📣")
            corpo = f"{emoji} {corpo}"

    # 3. CTA
    link = (link_artigo or _link_artigo(m)).strip()
    cta = (p.get("cta") or "").strip()
    if link:
        cta = f"Leia a matéria completa: {link}"
    elif not cta:
        if getattr(m, "formato_sugerido", "") in ("materia_longa", "nota_curta"):
            cta = "Análise completa em www.sultv.com.br"
        else:
            cta = "📺 Redação SulTV — a nossa região se vê."

    credito = (getattr(m, "credito_foto", "") or "").strip()

    hashtags = [h for h in (p.get("hashtags") or []) if h]
    if rede == "fb":
        hashtags = hashtags[:3]   # FB: poucas tags, foco em texto + link

    blocos = [corpo]
    if credito:
        blocos += ["", credito]
    if cta:
        blocos += ["", cta]
    if hashtags:
        blocos += ["", " ".join(hashtags)]
    return "\n".join(blocos).strip()


def _formatar_caption_ig(m) -> str:
    """Compat: legenda padrão (IG). Mantida para chamadas existentes."""
    return _formatar_caption(m, rede="ig")


_META_PLACEHOLDERS = ("EAAL...", "EAAL", "your-token", "")


def _meta_token_valido() -> str | None:
    t = os.getenv("META_LONG_LIVED_TOKEN", "").strip()
    if not t or t in _META_PLACEHOLDERS or t.endswith("...") or len(t) < 30:
        return None
    return t


def _drafts_dir():
    """Pasta de drafts. Override via env DRAFTS_POSTS_DIR. Default: ../Posts_Radar
    relativo ao projeto da skill (funciona tanto no Mac quanto no sandbox)."""
    override = os.environ.get("DRAFTS_POSTS_DIR", "").strip()
    if override:
        return override
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(os.path.dirname(project_root), "Posts_Radar")


def _grava_local(m):
    local_dir = _drafts_dir()
    os.makedirs(local_dir, exist_ok=True)
    local = f"{local_dir}/{datetime.now().strftime('%Y-%m-%d')}_{m.id_hash[:8]}.json"
    payload = {
        "data": datetime.now().isoformat(),
        "titulo_sultv": getattr(m, "titulo_sultv", ""),
        "subtitulo": getattr(m, "subtitulo", ""),
        "lead": getattr(m, "lead", ""),
        "tag_principal": m.tag_principal,
        "tag_thumbnail": getattr(m, "tag_thumbnail", ""),
        "instagram": getattr(m, "post_instagram", {}) or None,
        "carrossel": getattr(m, "card_carrossel", {}) or None,
        "caption_ig": _formatar_caption_ig(m) if getattr(m, "post_instagram", None) else None,
        "fonte": {"nome": m.fonte_nome, "url": m.url, "cidade": m.cidade},
        "score_combinado": m.score_combinado,
        "decisao_final": getattr(m, "decisao_final", ""),
    }
    with open(local, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return local


def _chamada_faixa(m) -> str:
    """Chamada curta/SEO para a faixa-legenda dos posts FB/IG (aprovado Donário 2026-05-29).

    Preferência: campo `chamada_faixa` da angulação → senão encurta o titulo_sultv
    para até ~8 palavras / ~62 chars no limite de palavra. tag_thumbnail é curto
    demais (rótulo) e fica como último recurso.
    """
    # Sanitiza qualquer chamada: colapsa espaços e remove preposição/artigo
    # pendurado no fim, evitando frases truncadas sem sentido
    # (ex.: "...PLACAS SOLARES DA"). Donário 2026-05-30.
    try:
        from imagens import sanitizar_chamada as _san
    except Exception:
        _stop = {'de', 'da', 'do', 'das', 'dos', 'e', 'a', 'o', 'as', 'os',
                 'para', 'pra', 'com', 'em', 'no', 'na', 'nos', 'nas', 'que',
                 'por', 'sem', 'sob', 'ao', 'aos', 'à', 'às', 'um', 'uma', 'ou'}
        def _san(s):
            pal = ' '.join((s or '').split()).split()
            while pal and pal[-1].lower().strip('.,;:…-') in _stop:
                pal.pop()
            return ' '.join(pal)

    cf = _san(getattr(m, 'chamada_faixa', '') or '')
    if cf:
        return cf
    titulo = (getattr(m, 'titulo_sultv', '') or getattr(m, 'titulo', '') or '').strip()
    if titulo:
        palavras = titulo.split()
        curta = palavras[0]
        for p in palavras[1:]:
            if len((curta + ' ' + p)) > 62 or len((curta + ' ' + p).split()) > 8:
                break
            curta += ' ' + p
        # remove preposição/artigo que tenha sobrado no corte
        return _san(curta.rstrip(' ,;:.'))
    return (getattr(m, 'tag_thumbnail', '') or '').strip()


def _gerar_e_subir_imagens_post(m) -> dict:
    """Obtém imagem LIMPA (sem overlay de texto) e gera variantes por rede.

    NOVO em 2026-05-18 (P0.1 — instrução Donário): nada mais de texto queimado
    em FB/IG. As imagens são fotos reais ou geradas por IA, com formato
    otimizado por plataforma (FB 1.91:1 / IG 4:5), e o texto vai apenas na
    caption do post.

    Retorna dict {fb_url, ig_url, alt_text, fonte_credito, origem}.
    Em caso de falha de upload, valores ficam None mas a estrutura é mantida.
    """
    try:
        from imagens import upload_wix_media, aplicar_faixa_legenda
        from buscar_imagem_limpa import obter_imagem_limpa
    except Exception as e:
        print(f"[post] Sem módulos de imagem ({e})")
        return {}

    # Briefing visual escrito pelo Claude na fase 4 (P0.2)
    bv = getattr(m, 'briefing_visual', None) or {}

    palavras_chave = []
    if getattr(m, 'tag_principal', ''):
        palavras_chave.append(m.tag_principal.replace('_', ' '))
    if getattr(m, 'cidade', ''):
        palavras_chave.append(m.cidade)

    sub = (getattr(m, 'subtitulo', '') or '').strip()
    desc_fallback = sub or getattr(m, 'titulo_sultv', '')

    try:
        info_img = obter_imagem_limpa(
            url_fonte=getattr(m, 'url', ''),
            titulo=getattr(m, 'titulo_sultv', ''),
            palavras_chave=palavras_chave,
            tag_principal=getattr(m, 'tag_principal', ''),
            cidade=getattr(m, 'cidade', ''),
            descricao_imagem=desc_fallback,
            briefing_visual=bv,
            gerar_variantes=True,
            formatos_alvo=['fb_feed', 'ig_feed'],
        )
    except Exception as e:
        print(f"[post] Falha ao obter imagem limpa: {e}")
        return {}

    print(f"[post] Imagem origem={info_img['origem']} "
          f"({info_img['width']}x{info_img['height']})")

    variantes = info_img.get('variantes', {})
    stamp = datetime.now().strftime('%Y%m%d')
    sid = m.id_hash[:8]

    # Faixa-legenda padrão @sultv31 (aprovado Donário 2026-05-29) — só FB/IG,
    # capa Wix permanece limpa. Chamada curta/SEO.
    chamada = _chamada_faixa(m)
    if chamada:
        for fmt in ('fb_feed', 'ig_feed'):
            if variantes.get(fmt):
                try:
                    variantes[fmt] = aplicar_faixa_legenda(variantes[fmt], chamada)
                except Exception as e:
                    print(f"[post] faixa-legenda falhou em {fmt}: {e} — usando imagem limpa")
        print(f"[post] faixa-legenda aplicada: \"{chamada}\"")

    saida = {
        'alt_text': info_img.get('alt_text', ''),
        'fonte_credito': info_img.get('fonte_credito', ''),
        'origem': info_img.get('origem', ''),
        'fb_url': None,
        'ig_url': None,
    }

    if variantes.get('fb_feed'):
        info = upload_wix_media(variantes['fb_feed'],
                                f'radar_{stamp}_{sid}_fb.jpg',
                                mime_type='image/jpeg')
        if info and info.get('url'):
            saida['fb_url'] = info['url']
            print(f"[post] FB image upload OK: {info['url']}")

    if variantes.get('ig_feed'):
        info = upload_wix_media(variantes['ig_feed'],
                                f'radar_{stamp}_{sid}_ig.jpg',
                                mime_type='image/jpeg')
        if info and info.get('url'):
            saida['ig_url'] = info['url']
            print(f"[post] IG image upload OK: {info['url']}")

    return saida


def _alt_text_post(m, img_info: dict | None = None) -> str:
    """Alt text de acessibilidade da imagem do post (FB).

    Reutiliza a mesma lógica do Blog Wix (`produzir_materia._alt_text_seo`):
    descrição visual da imagem + focus keyword + cidade, nunca vazio.
    O alt da imagem do post não tem `reescrita` (não é matéria longa), então
    parte do `alt_text` devolvido pela busca de imagem / briefing_visual.
    """
    img_info = img_info or {}
    cover = {'alt_text': img_info.get('alt_text', '')}
    try:
        from produzir_materia import _alt_text_seo
        return _alt_text_seo(m, cover, None)
    except Exception:
        # Fallback defensivo: descrição → título; nunca quebra a publicação.
        bv = getattr(m, 'briefing_visual', None) or {}
        base = (img_info.get('alt_text') or bv.get('descricao_pt')
                or getattr(m, 'titulo_sultv', '') or 'Imagem SulTV')
        cidade = (getattr(m, 'cidade', '') or '').strip()
        if cidade and cidade.lower() not in base.lower():
            base = f"{base} — {cidade}"
        return ' '.join(base.split())[:155]


def _publicar_facebook_page(image_url: str, caption: str, page_id: str, token: str,
                            alt_text: str = "") -> str | None:
    """Publica foto na Facebook Page. Retorna post_id ou None.

    alt_text (Donário 2026-05-21): texto alternativo de acessibilidade da foto.
    Vai no parâmetro `alt_text_custom` do endpoint /photos — lido por leitores
    de tela. Opcional; se vazio, publica normalmente sem o campo.
    """
    try:
        data = {'url': image_url, 'caption': caption,
                'published': 'true', 'access_token': token}
        if alt_text and alt_text.strip():
            data['alt_text_custom'] = alt_text.strip()[:1000]
        r = requests.post(
            f"{META_GRAPH}/{page_id}/photos",
            data=data,
            timeout=60,
        )
        r.raise_for_status()
        body = r.json()
        post_id = body.get('post_id') or body.get('id')
        if post_id:
            print(f"[fb] PUBLICADO: https://www.facebook.com/{post_id}")
        return post_id
    except requests.HTTPError as e:
        print(f"[fb] FALHA HTTP {e.response.status_code}: {e.response.text[:300]}")
        return None
    except Exception as e:
        print(f"[fb] FALHA: {e}")
        return None


def _publicar_facebook_album(image_urls: list, caption: str, page_id: str, token: str) -> str | None:
    """Publica álbum (carrossel) na Page. Cada foto é uploadada não-publicada,
    depois agrupada num post único com a primeira foto destacada."""
    if not image_urls:
        return None
    photo_ids = []
    for url in image_urls:
        try:
            r = requests.post(
                f"{META_GRAPH}/{page_id}/photos",
                data={'url': url, 'published': 'false', 'access_token': token},
                timeout=60,
            )
            r.raise_for_status()
            photo_ids.append(r.json().get('id'))
        except requests.HTTPError as e:
            print(f"[fb-album] upload foto falhou {e.response.status_code}: {e.response.text[:200]}")
            continue
    if not photo_ids:
        return None
    # Cria o feed post com attached_media
    try:
        attached = json.dumps([{'media_fbid': pid} for pid in photo_ids if pid])
        r = requests.post(
            f"{META_GRAPH}/{page_id}/feed",
            data={'message': caption, 'attached_media': attached,
                  'access_token': token},
            timeout=60,
        )
        r.raise_for_status()
        post_id = r.json().get('id')
        print(f"[fb] ÁLBUM PUBLICADO: https://www.facebook.com/{post_id}")
        return post_id
    except requests.HTTPError as e:
        print(f"[fb-album] FALHA feed HTTP {e.response.status_code}: {e.response.text[:300]}")
        return None
    except Exception as e:
        print(f"[fb-album] FALHA: {e}")
        return None


def _publicar_instagram_simples(image_url: str, caption: str, ig_id: str, token: str) -> str | None:
    """IG single image: cria container, aguarda o container ficar FINISHED e publica.

    Robustez (Donário 2026-06-01): o IG precisa baixar a imagem da URL do Wix antes
    de publicar. Se publicarmos rápido demais, retorna code 9007/subcode 2207027
    ('A mídia não está pronta — aguarde'). Agora consultamos status_code do container
    e só publicamos quando FINISHED, com retries no media_publish.
    """
    import time
    try:
        r = requests.post(
            f"{META_GRAPH}/{ig_id}/media",
            data={'image_url': image_url, 'caption': caption, 'access_token': token},
            timeout=60,
        )
        r.raise_for_status()
        creation_id = r.json().get('id')
        if not creation_id:
            return None

        # Aguarda o container ficar pronto (status_code: IN_PROGRESS -> FINISHED)
        for _ in range(8):
            try:
                st = requests.get(
                    f"{META_GRAPH}/{creation_id}",
                    params={'fields': 'status_code', 'access_token': token},
                    timeout=20,
                ).json().get('status_code')
            except Exception:
                st = None
            if st == 'FINISHED':
                break
            if st == 'ERROR':
                print('[ig] container retornou ERROR')
                return None
            time.sleep(3)

        # Publica, com retries no erro transitório de mídia não pronta
        last = None
        for tentativa in range(4):
            r2 = requests.post(
                f"{META_GRAPH}/{ig_id}/media_publish",
                data={'creation_id': creation_id, 'access_token': token},
                timeout=60,
            )
            if r2.status_code == 200:
                post_id = r2.json().get('id')
                print(f"[ig] PUBLICADO: id={post_id}")
                return post_id
            last = r2
            # 2207027 / 9007 = mídia ainda não pronta -> espera e tenta de novo
            if '2207027' in r2.text or '9007' in r2.text:
                time.sleep(4)
                continue
            break
        if last is not None:
            print(f"[ig] FALHA HTTP {last.status_code}: {last.text[:300]}")
        return None
    except requests.HTTPError as e:
        print(f"[ig] FALHA HTTP {e.response.status_code}: {e.response.text[:300]}")
        return None
    except Exception as e:
        print(f"[ig] FALHA: {e}")
        return None


def _publicar_instagram_carrossel(image_urls: list, caption: str, ig_id: str, token: str) -> str | None:
    """IG carrossel: cria N media containers (is_carousel_item=true), depois container CAROUSEL, publica."""
    if not image_urls:
        return None
    children = []
    for url in image_urls:
        try:
            r = requests.post(
                f"{META_GRAPH}/{ig_id}/media",
                data={'image_url': url, 'is_carousel_item': 'true',
                      'access_token': token},
                timeout=60,
            )
            r.raise_for_status()
            children.append(r.json().get('id'))
        except requests.HTTPError as e:
            print(f"[ig-carr] item falhou {e.response.status_code}: {e.response.text[:200]}")
    if len(children) < 2:
        print("[ig-carr] menos de 2 itens — abortando")
        return None
    try:
        r = requests.post(
            f"{META_GRAPH}/{ig_id}/media",
            data={'media_type': 'CAROUSEL', 'children': ','.join(children),
                  'caption': caption, 'access_token': token},
            timeout=60,
        )
        r.raise_for_status()
        creation_id = r.json().get('id')
        r2 = requests.post(
            f"{META_GRAPH}/{ig_id}/media_publish",
            data={'creation_id': creation_id, 'access_token': token},
            timeout=60,
        )
        r2.raise_for_status()
        post_id = r2.json().get('id')
        print(f"[ig] CARROSSEL PUBLICADO: id={post_id}")
        return post_id
    except requests.HTTPError as e:
        print(f"[ig-carr] FALHA HTTP {e.response.status_code}: {e.response.text[:300]}")
        return None
    except Exception as e:
        print(f"[ig-carr] FALHA: {e}")
        return None


def publicar_post(m, link_artigo: str = ""):
    """Pipeline completo: gera imagem(ns) → upload Wix Media → publica Facebook + IG.

    Comportamento:
    - Sempre publica em FB Page se token + page_id estiverem OK.
    - Publica em IG só se META_IG_BUSINESS_ID estiver setado (sem isso, IG fica fora).
    - Em qualquer falha, grava draft local.
    - `link_artigo` (opcional): URL específica da matéria no site; quando
      presente, o CTA do post linka direto pra ela em vez da home.
    - Legenda diferenciada por rede (FB texto+link / IG gancho+hashtags).
    """
    if not getattr(m, "post_instagram", None) and not getattr(m, "card_carrossel", None):
        print(f"[post] Sem post nem carrossel para {m.id_hash[:8]} — pulando")
        return None

    token = _meta_token_valido()
    if not token:
        local = _grava_local(m)
        print(f"[post] Sem token Meta válido — gravado local: {local}")
        return local

    page_id = os.getenv('META_FB_PAGE_ID', '').strip()
    ig_id = os.getenv('META_IG_BUSINESS_ID', '').strip()
    if not page_id and not ig_id:
        local = _grava_local(m)
        print(f"[post] Nem META_FB_PAGE_ID nem META_IG_BUSINESS_ID setados — gravado local: {local}")
        return local

    # 1. Gera + sobe imagens (variantes por formato — P0.3)
    img_info = _gerar_e_subir_imagens_post(m)
    if not img_info or (not img_info.get('fb_url') and not img_info.get('ig_url')):
        local = _grava_local(m)
        print(f"[post] Falha ao gerar/subir imagens — gravado local: {local}")
        return local

    caption_fb = _formatar_caption(m, rede="fb", link_artigo=link_artigo)
    caption_ig = _formatar_caption(m, rede="ig", link_artigo=link_artigo)
    alt_fb = _alt_text_post(m, img_info)
    resultados = []

    # 2. Facebook Page — usa variante 1200x630 (1.91:1, ideal feed)
    # alt_text_custom preenchido p/ acessibilidade (Donário 2026-05-21).
    if page_id and img_info.get('fb_url'):
        res = _publicar_facebook_page(img_info['fb_url'], caption_fb, page_id, token,
                                      alt_text=alt_fb)
        if res:
            resultados.append(f"fb:{res}")

    # 3. Instagram — usa variante 1080x1350 (4:5, máximo real estate feed)
    # NOTA: a API de publicação do Instagram (Content Publishing) NÃO expõe
    # campo de alt text/texto alternativo na criação do container — o alt do IG
    # só é editável manualmente no app. Por isso não há alt_text aqui.
    if ig_id and img_info.get('ig_url'):
        res = _publicar_instagram_simples(img_info['ig_url'], caption_ig, ig_id, token)
        if res:
            resultados.append(f"ig:{res}")
    elif not ig_id:
        print(f"[post] IG pulado (META_IG_BUSINESS_ID vazio — Instagram não conectado à Page ainda)")

    if not resultados:
        local = _grava_local(m)
        print(f"[post] Nada publicado — gravado local: {local}")
        return local

    return ' · '.join(resultados)
