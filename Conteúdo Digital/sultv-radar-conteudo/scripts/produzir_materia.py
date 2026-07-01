"""
produzir_materia.py — hook para matéria longa no Wix
=====================================================
Recebe MateriaPronta com lead_materia_longa + ângulo + ganchos
e cria um post no www.sultv.com.br via API do Wix Blog.

Tom institucional Redação SulTV (terceira pessoa, dado quantitativo no lead,
fonte com nome completo + sigla, fechamento prospectivo).
"""
from __future__ import annotations
import json
import os
import re
import uuid
import requests
from datetime import datetime


WIX_API = "https://www.wixapis.com/blog/v3/draft-posts"
WIX_POSTS_API = "https://www.wixapis.com/blog/v3/posts"


def _url_publica_do_post(post_id: str, headers: dict, fallback: str = "") -> str:
    """Resolve a URL PÚBLICA real (baseada no slug) de um post já publicado.

    BUG (Donário 2026-06-03): a URL era montada como /post/{post_id} (UUID), mas
    a URL pública do Wix Blog usa o SLUG do título (/post/<slug-do-titulo>), então
    o link compartilhado em FB/IG dava 404. Aqui consultamos o post publicado e
    usamos url.base + url.path (ou o slug). Pequeno retry porque o post recém
    publicado pode levar 1-2s para aparecer no endpoint de posts publicados.
    """
    from urllib.parse import quote
    import time
    for tentativa in range(3):
        try:
            r = requests.get(f"{WIX_POSTS_API}/{post_id}",
                             headers=headers, params={"fieldsets": "URL"}, timeout=20)
            if r.status_code == 200:
                post = r.json().get("post", {}) or {}
                url = post.get("url") or {}
                base = (url.get("base") or "https://www.sultv.com.br").rstrip("/")
                path = url.get("path") or ""
                slug = post.get("slug") or ""
                if path:
                    return base + quote(path, safe="/")
                if slug:
                    return f"{base}/post/{quote(slug, safe='')}"
        except Exception as e:
            print(f"[materia] _url_publica_do_post tentativa {tentativa+1} falhou: {e}")
        time.sleep(1.5)
    print(f"[materia] ⚠ não resolvi a URL pública (slug) de {post_id[:8]} — usando fallback")
    return fallback or f"https://www.sultv.com.br/post/{post_id}"


# ============================================================
# Prompt oficial Donário — reescrita estilo blog SulTV
# ============================================================
PROMPT_REDACAO_SULTV = """Aja como um editor jornalístico especializado em transformar entrevistas e reportagens em artigos para blog no estilo da SulTV. Sua tarefa é gerar um artigo de aproximadamente 1.500 caracteres (cerca de 2 ou 3 minutos de leitura), usando linguagem simples, clara, informativa e com contextualização regional da Zona Sul do Rio Grande do Sul.

Pense passo a passo e siga exatamente estas instruções:

1. Use o material bruto fornecido como base e reescreva o conteúdo em formato de artigo jornalístico informativo, com neutralidade, foco em precisão e sem adjetivação exagerada.
2. O artigo deve ter aproximadamente 1.500 caracteres. Revise o texto antes de entregar para garantir que está próximo dessa extensão.
3. O estilo deve seguir o padrão dos artigos do site www.sultv.com.br: linguagem simples, frases diretas, fluidez, clareza e foco no conteúdo.
4. O primeiro parágrafo deve contextualizar o tema e a região da Zona Sul do RS quando fizer sentido.
5. Identifique as palavras-chave mais relevantes do conteúdo e integre-as naturalmente ao artigo. Pelo menos uma das palavras-chave deve aparecer no título.
6. Evite repetições desnecessárias ao longo do texto.
7. Caso o material contenha dados, números ou falas importantes, incorpore-os de forma sintética e precisa.
8. Não faça menções ao processo de geração do texto, ao briefing interno (ângulo editorial, ganchos), nem ao fato de ser conteúdo curatorial. Escreva como artigo final pronto para o leitor.
9. Crie um título atrativo (evitando letras maiúsculas desnecessárias) e otimizado para SEO, pensado para maximizar cliques e alinhado ao conteúdo, conforme:
   a. Análise semântica para identificar tópicos centrais.
   b. Aplicação de fórmulas testadas de copywriting.
   c. Melhores práticas de SEO com palavras-chave de alto impacto para a audiência SulTV.
   d. Gatilhos de curiosidade, surpresa, urgência, novidade ou promessa, sem ser enganoso.
   e. Máximo 100 caracteres, palavras fortes no início, sem repetição de termos, evitando caixa-alta desnecessária.
10. Gere uma sugestão de legenda da foto com no máximo 120 caracteres.

REGRA INEGOCIÁVEL (Donário 2026-06-06) — NUNCA, JAMAIS mencionar fontes ou veículos de comunicação em NENHUM texto, título, chamada, legenda ou comentário: nada de portais, sites, rádios, jornais, emissoras, TVs ou plataformas de comunicação. PROIBIDO escrever "Com informações de...", "Segundo o portal/jornal/rádio X", "em entrevista à rádio Y", "mostra reportagem de Z" ou qualquer variação. O material coletado é insumo: retrabalhe e reformate 100% no tom de voz da SulTV, como conteúdo próprio da Redação SulTV. Atribuições só a fontes PRIMÁRIAS institucionais (prefeituras, secretarias, Corpo de Bombeiros, Polícia, Emater, entidades, autoridades nomeadas) — nunca a veículos de mídia. Se uma fala só existir citada por um veículo, incorpore a informação sem citar o veículo.

A resposta final DEVE seguir EXATAMENTE esta estrutura, com estes delimitadores literais (incluindo os ###):

### Título ###
[título otimizado]

### Artigo ###
[artigo com aproximadamente 1.500 caracteres em prosa contínua, sem subtítulos]

### Legenda sugerida ###
[legenda de até 120 caracteres]

### Palavras-chave ###
[lista separada por vírgulas das palavras-chave usadas]

A resposta deve começar imediatamente com "### Título ###". Quando eu enviar o material bruto, execute todas as etapas acima."""


# Cache da reescrita para evitar chamar Sonnet 2x na mesma matéria
_REESCRITA_CACHE: dict[str, dict] = {}


def _parse_resposta_sonnet(texto: str) -> dict:
    """Extrai os 4 blocos delimitados por ### Título ###, ### Artigo ### etc."""
    out = {"titulo": "", "artigo": "", "legenda": "", "keywords": []}
    # Pattern flexível: captura cada seção até a próxima
    secoes = re.split(r'###\s*([^#]+?)\s*###\s*\n?', texto)
    # secoes vai ser: ['', 'Título', 'conteúdo', 'Artigo', 'conteúdo', ...]
    i = 1
    while i < len(secoes) - 1:
        nome = secoes[i].strip().lower()
        conteudo = secoes[i + 1].strip()
        if 'título' in nome or 'titulo' in nome:
            out['titulo'] = conteudo.split('\n')[0].strip()
        elif 'artigo' in nome:
            out['artigo'] = conteudo
        elif 'legenda' in nome:
            out['legenda'] = conteudo.split('\n')[0].strip()[:120]
        elif 'palavra' in nome:
            kw = conteudo.replace('\n', ',').split(',')
            out['keywords'] = [k.strip().lstrip('-•').strip() for k in kw if k.strip()]
        i += 2
    return out


def _reescrever_via_sonnet(m) -> dict | None:
    """Chama Sonnet com o prompt oficial Donário. Retorna {titulo, artigo, legenda, keywords}."""
    cache_key = getattr(m, 'id_hash', '')
    if cache_key and cache_key in _REESCRITA_CACHE:
        return _REESCRITA_CACHE[cache_key]

    if not os.getenv('ANTHROPIC_API_KEY', '').strip():
        print('[materia] ANTHROPIC_API_KEY ausente — pulando reescrita Sonnet')
        return None

    try:
        import anthropic
    except Exception as e:
        print(f'[materia] anthropic não instalada ({e}) — pulando reescrita')
        return None

    # Monta material bruto a partir dos campos do radar
    bruto_partes = [f"TÍTULO ATUAL: {m.titulo_sultv}"]
    if getattr(m, 'subtitulo', ''):
        bruto_partes.append(f"SUBTÍTULO: {m.subtitulo}")
    if getattr(m, 'cidade', ''):
        bruto_partes.append(f"CIDADE: {m.cidade}")
    if getattr(m, 'fonte_nome', ''):
        bruto_partes.append(f"FONTE: {m.fonte_nome}")
    bruto_partes.append('')
    if getattr(m, 'lead_materia_longa', ''):
        bruto_partes.append(f"LEAD JORNALÍSTICO:\n{m.lead_materia_longa}")
    if getattr(m, 'angulo_editorial', ''):
        bruto_partes.append(f"\nÂNGULO EDITORIAL (apenas direcionamento, NÃO reproduza literalmente):\n{m.angulo_editorial}")
    if getattr(m, 'ganchos_3', None):
        bruto_partes.append(f"\nGANCHOS POSSÍVEIS:\n" + '\n'.join(f'- {g}' for g in m.ganchos_3))

    material = '\n'.join(bruto_partes)

    try:
        client = anthropic.Anthropic()
        resp = client.messages.create(
            model='claude-sonnet-4-5',
            max_tokens=2500,
            system=PROMPT_REDACAO_SULTV,
            messages=[{'role': 'user', 'content': material}],
        )
        texto = resp.content[0].text
    except Exception as e:
        print(f'[materia] Sonnet falhou ({e}) — usando fallback texto puro')
        return None

    out = _parse_resposta_sonnet(texto)
    if not out.get('artigo'):
        print(f'[materia] Parse Sonnet falhou — primeiros 200 chars: {texto[:200]}')
        return None

    if cache_key:
        _REESCRITA_CACHE[cache_key] = out
    return out


def _node_id() -> str:
    return str(uuid.uuid4())[:8]


def _text_node(txt: str, bold: bool = False, italic: bool = False) -> dict:
    decorations = []
    if bold:
        decorations.append({"type": "BOLD", "fontWeightValue": 700})
    if italic:
        decorations.append({"type": "ITALIC"})
    return {
        "type": "TEXT", "id": _node_id(), "nodes": [],
        "textData": {"text": txt, "decorations": decorations},
    }


def _paragraph(txt: str) -> dict:
    """Parágrafo simples (prosa contínua)."""
    return {
        "type": "PARAGRAPH", "id": _node_id(),
        "nodes": [_text_node(txt)] if txt else [],
        "paragraphData": {"textStyle": {"textAlignment": "AUTO"}},
    }


def _paragraph_legenda(txt: str) -> dict:
    """Legenda em itálico, fonte menor (estilo 'Foto: ...')."""
    return {
        "type": "PARAGRAPH", "id": _node_id(),
        "nodes": [_text_node(txt, italic=True)],
        "paragraphData": {"textStyle": {"textAlignment": "AUTO"}},
    }


def _blank_paragraph() -> dict:
    """Parágrafo vazio — usado como respiro visual entre blocos de conteúdo
    no Wix (regra editorial Donário: sempre uma linha em branco depois de
    cada parágrafo, inclusive antes/depois de imagens)."""
    return {
        "type": "PARAGRAPH", "id": _node_id(),
        "nodes": [],
        "paragraphData": {"textStyle": {"textAlignment": "AUTO"}},
    }


def _append_block(nodes: list, novo: dict) -> None:
    """Anexa um nó de conteúdo (parágrafo, imagem, etc.) ao corpo do post,
    inserindo automaticamente uma linha em branco ANTES dele se já houver
    conteúdo prévio. Garante separação visual em todas as transições."""
    if nodes:
        nodes.append(_blank_paragraph())
    nodes.append(novo)


def _image_node(image_id: str, url: str, width: int, height: int,
                 alt_text: str) -> dict:
    """Nó IMAGE para inserir imagem inline no corpo do post.

    IMPORTANTE: o schema Ricos NÃO aceita `caption` como propriedade do imageData
    — a legenda precisa ser um nó CAPTION SEPARADO (renderizado abaixo), criado
    via _caption_node() logo após este nó IMAGE.
    """
    return {
        "type": "IMAGE", "id": _node_id(),
        "nodes": [],
        "imageData": {
            "containerData": {
                "width": {"size": "CONTENT"},
                "alignment": "CENTER",
                "textWrap": True,
            },
            "image": {
                "src": {"id": image_id, "url": url},
                "width": width or 1200,
                "height": height or 630,
            },
            "altText": alt_text,
            "disableExpand": False,
            "disableDownload": False,
        },
    }


def _caption_node(texto: str) -> dict:
    """Nó CAPTION (legenda) — renderizado ABAIXO da imagem como bloco separado.

    O Wix Blog Ricos define CAPTION como um tipo de nó próprio (não como
    propriedade do IMAGE). O texto da legenda vai como TEXT filho.
    Estilo italic discreto fica a cargo do tema do blog.
    """
    return {
        "type": "PARAGRAPH", "id": _node_id(),
        "nodes": [_text_node(texto, italic=True)],
        "paragraphData": {"textStyle": {"textAlignment": "CENTER"}},
    }


def _split_em_paragrafos(texto: str, max_len: int = 600) -> list[str]:
    """Quebra prosa longa em parágrafos respeitando frases. Cada bloco ~max_len chars."""
    if not texto:
        return []
    # Já tem parágrafos explícitos?
    blocos = [b.strip() for b in texto.split('\n\n') if b.strip()]
    if len(blocos) > 1:
        return blocos
    # Senão quebra em sentenças e agrupa
    import re as _re
    sentencas = _re.split(r'(?<=[.!?])\s+', texto.strip())
    paragrafos = []
    atual = ''
    for s in sentencas:
        if not s:
            continue
        if len(atual) + len(s) + 1 <= max_len:
            atual = (atual + ' ' + s).strip()
        else:
            if atual:
                paragrafos.append(atual)
            atual = s
    if atual:
        paragrafos.append(atual)
    return paragrafos


def _build_rich_content(m, cover: dict | None = None,
                         reescrita: dict | None = None) -> dict:
    """Monta richContent estilo blog SulTV — prosa contínua via Sonnet (prompt Donário).

    Se houver reescrita Sonnet, usa o artigo gerado. Caso contrário, fallback ao lead.
    Estrutura: parágrafo(s) iniciais + imagem inline (com legenda Sonnet) + parágrafo(s) finais.
    """
    nodes = []

    # Parágrafos do artigo Sonnet (preferido) ou fallback ao lead
    if reescrita and reescrita.get('artigo'):
        paragrafos = _split_em_paragrafos(reescrita['artigo'], max_len=600)
    else:
        lead = getattr(m, 'lead_materia_longa', '') or getattr(m, 'lead', '') or ''
        paragrafos = _split_em_paragrafos(lead, max_len=600)

    # Distribui imagem no meio do texto: depois do 1º (curto) ou 2º parágrafo
    img_inserida = False
    posicao_img = 1 if len(paragrafos) <= 3 else 2

    def _img_e_caption():
        """Devolve (img_node, caption_node | None). Caption só se houver texto."""
        alt = _alt_text_seo(m, cover, reescrita)
        img = _image_node(
            image_id=cover['id'], url=cover['url'],
            width=cover.get('width') or 1200,
            height=cover.get('height') or 630,
            alt_text=alt,
        )
        # Legenda preferencialmente do Sonnet/Donário (linha 'Legenda sugerida').
        # Senão usa subtítulo da matéria + crédito da fonte.
        legenda = (reescrita or {}).get('legenda', '').strip()
        if not legenda:
            sub = (getattr(m, 'subtitulo', '') or '').strip()
            credito = cover.get('fonte_credito') or \
                      (f"Foto: {m.fonte_nome}" if getattr(m, 'fonte_nome', '') else '')
            legenda = (sub + (f" — {credito}" if sub and credito else credito or sub)).strip(" —")
        cap = _caption_node(legenda) if legenda else None
        return img, cap

    for i, p in enumerate(paragrafos):
        _append_block(nodes, _paragraph(p))
        if not img_inserida and (i + 1) == posicao_img and cover and cover.get('id'):
            img, cap = _img_e_caption()
            _append_block(nodes, img)
            if cap:
                # Caption logo abaixo da imagem, sem _blank_paragraph entre eles
                nodes.append(cap)
            img_inserida = True

    # Garante que a imagem foi inserida (caso o post seja muito curto)
    if not img_inserida and cover and cover.get('id'):
        img, cap = _img_e_caption()
        _append_block(nodes, img)
        if cap:
            nodes.append(cap)

    return {"nodes": nodes}


# ============================================================
# SEO data (aba Básico, Rede Social, Assistente do Wix Blog)
# ============================================================

def _palavra_chave_principal(titulo: str) -> str:
    """Extrai palavra-chave principal do título (primeiras palavras significativas).

    Usa as 2-4 primeiras palavras do título excluindo stop words. A palavra-chave
    retornada SEMPRE aparece literalmente no título (requisito SEO Donário).
    """
    stop = {'a','o','os','as','e','é','de','do','da','dos','das','no','na','nos','nas',
            'em','um','uma','uns','umas','para','por','com','sem','que','se','ao','aos',
            'à','às','já','também','mas','ou','e/ou'}
    palavras = []
    for w in titulo.split():
        wl = w.strip('.,;:!?').lower()
        if wl and wl not in stop:
            palavras.append(w.strip('.,;:!?'))
        if len(palavras) >= 4:
            break
    return ' '.join(palavras).strip()


def _focus_keyword(m, reescrita: dict | None) -> str:
    """Define a palavra-chave principal (focus keyword da aba Assistente).

    Estratégia:
    1. Se Sonnet/Donário gerou `keywords[]`, pega a primeira que aparece no título
    2. Senão usa a palavra-chave significativa extraída do título
    Garantia: a focus keyword SEMPRE consta no título (caso contrário SEO Wix
    sinaliza warning amarelo na aba Assistente).
    """
    titulo = (reescrita or {}).get('titulo') or m.titulo_sultv
    titulo_lc = titulo.lower()
    kws = (reescrita or {}).get('keywords') or []
    for kw in kws:
        kw_clean = kw.strip().lower()
        if kw_clean and kw_clean in titulo_lc:
            return kw.strip()
    # Fallback: primeira palavra significativa do título
    return _palavra_chave_principal(titulo)


def _alt_text_seo(m, cover: dict | None, reescrita: dict | None = None) -> str:
    """Texto alternativo (alt text) da imagem para a aba Geral do Wix.

    Regra Donário (2026-05-21): este campo deve SEMPRE estar preenchido com
    algo relevante para SEO em relação à imagem. Estratégia:

    1. Base = descrição VISUAL da imagem (o que a foto mostra) —
       `cover['alt_text']` (vindo de briefing_visual.descricao_pt / busca de
       imagem). É a melhor prática tanto de acessibilidade quanto de
       indexação de imagem pelo Google.
    2. Fallback em cascata: briefing_visual.descricao_pt → subtítulo → título.
    3. Enriquecimento SEO: garante que a focus keyword e a cidade apareçam
       (sem duplicar), reforçando a relevância da imagem para a busca.
    4. Nunca vazio; normaliza espaços; limite ~155 chars (boa prática de alt).
    """
    cover = cover or {}
    base = (cover.get('alt_text') or '').strip()
    if not base:
        bv = getattr(m, 'briefing_visual', None) or {}
        base = (bv.get('descricao_pt') or '').strip()
    if not base:
        base = (getattr(m, 'subtitulo', '') or '').strip()
    if not base:
        base = (getattr(m, 'titulo_sultv', '') or getattr(m, 'titulo', '') or '').strip()

    base_lc = base.lower()
    extras = []
    try:
        focus = _focus_keyword(m, reescrita)
    except Exception:
        focus = ''
    if focus and focus.lower() not in base_lc:
        extras.append(focus)
    cidade = (getattr(m, 'cidade', '') or '').strip()
    if cidade and cidade.lower() not in base_lc and \
       cidade.lower() not in ' '.join(extras).lower():
        extras.append(cidade)

    alt = f"{base} — {', '.join(extras)}" if extras else base
    alt = ' '.join(alt.split())          # normaliza espaços/quebras
    alt = alt[:155].strip(" —,")
    # Garantia final: nunca devolve string vazia
    return alt or (getattr(m, 'titulo_sultv', '') or 'Imagem SulTV')[:155]


def _build_seo_data(m, cover: dict | None, reescrita: dict | None = None) -> dict:
    """Monta seoData para Wix Blog v3 (aba Básico + Rede Social + Assistente).

    Estrutura final:
    - seoData.tags[] — Open Graph, Twitter cards, meta description, meta keywords
    - seoData.settings.keywords[] — focus keyword da aba ASSISTENTE
      [{term: <focus>, isMain: true, origin: "RADAR_SULTV"}]

    A meta descrição (campo `tags` com name=description) DEVE conter a focus keyword
    — checado e ajustado aqui.
    """
    titulo = (reescrita or {}).get('titulo') or m.titulo_sultv
    descricao = (getattr(m, 'subtitulo', '') or '').strip()
    if not descricao:
        descricao = (getattr(m, 'lead', '') or '')[:155].strip()

    # Focus keyword: SEMPRE consta no título (validação interna)
    focus = _focus_keyword(m, reescrita)

    # Garante que a meta description inclui a focus keyword. Se não incluir,
    # prepende-a de forma natural ("<focus> — <descrição>").
    if focus and focus.lower() not in descricao.lower():
        descricao = f"{focus} — {descricao}".strip(" —")
    if len(descricao) > 160:
        descricao = descricao[:157].rstrip() + "..."

    # Palavras-chave secundárias (Sonnet) + focus
    kws = (reescrita or {}).get('keywords') or []
    meta_keywords = ', '.join([focus] + [k for k in kws[:4] if k.lower() != focus.lower()])

    # Imagem para social cards (og:image, twitter:image)
    img_url = (cover or {}).get('url', '')

    tags = []
    # Aba Básico — meta description + meta keywords
    if descricao:
        tags.append({"type": "meta",
                     "props": {"name": "description", "content": descricao[:160]}})
    if meta_keywords:
        tags.append({"type": "meta",
                     "props": {"name": "keywords", "content": meta_keywords}})

    # Aba Rede Social — Open Graph
    tags.append({"type": "meta",
                 "props": {"property": "og:title", "content": titulo[:90]}})
    if descricao:
        tags.append({"type": "meta",
                     "props": {"property": "og:description", "content": descricao[:200]}})
    if img_url:
        tags.append({"type": "meta",
                     "props": {"property": "og:image", "content": img_url}})
    tags.append({"type": "meta",
                 "props": {"property": "og:type", "content": "article"}})

    # Twitter cards
    tags.append({"type": "meta",
                 "props": {"name": "twitter:card", "content": "summary_large_image"}})
    tags.append({"type": "meta",
                 "props": {"name": "twitter:title", "content": titulo[:90]}})
    if descricao:
        tags.append({"type": "meta",
                     "props": {"name": "twitter:description", "content": descricao[:200]}})
    if img_url:
        tags.append({"type": "meta",
                     "props": {"name": "twitter:image", "content": img_url}})

    # Aba Assistente — focus keyword (settings.keywords[isMain=true])
    settings = {}
    if focus:
        settings = {
            "keywords": [
                {"term": focus[:80], "isMain": True, "origin": "RADAR_SULTV"}
            ]
        }

    out = {"tags": tags}
    if settings:
        out["settings"] = settings
    return out


def _slug_ascii(titulo: str) -> str:
    """Slug ASCII para o Wix (REGRA Donário 2026-06-07): NUNCA usar acentos no slug.

    Ex.: 'Atleta de Camaquã conquista título...' -> 'atleta-de-camaqua-conquista-titulo-...'
    Remove acentos (NFKD), minúsculas, troca não-alfanumérico por hífen,
    colapsa hífens e limita a ~80 chars cortando em fronteira de palavra.
    """
    import unicodedata as _ud
    import re as _re
    s = _ud.normalize("NFKD", titulo or "")
    s = "".join(c for c in s if not _ud.combining(c))
    s = _re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    s = _re.sub(r"-{2,}", "-", s)
    if len(s) > 80:
        s = s[:80].rsplit("-", 1)[0]
    return s


def _build_post_body(m, cover: dict | None) -> dict:
    """Monta body completo da matéria longa para Wix Blog v3 (estilo blog SulTV).

    Chama Sonnet com prompt oficial Donário para reescrever em prosa jornalística
    de ~1.500 caracteres + título SEO + legenda + palavras-chave.
    """
    # 1. Reescrita Sonnet (idempotente via cache)
    reescrita = _reescrever_via_sonnet(m)

    # 2. Título: usa o do Sonnet quando disponível
    titulo = (reescrita or {}).get('titulo') or m.titulo_sultv

    member_id = os.getenv('WIX_MEMBER_ID', '').strip()
    body = {
        "title": titulo,
        "excerpt": (getattr(m, 'subtitulo', '') or '').strip(),
        "richContent": _build_rich_content(m, cover=cover, reescrita=reescrita),
        "seoData": _build_seo_data(m, cover, reescrita=reescrita),
        # REGRA (Donário 2026-06-07): slug sempre ASCII, sem acentos.
        "seoSlug": _slug_ascii(titulo),
    }
    if member_id:
        body["memberId"] = member_id

    # Categorias e tags via wix_taxonomia (mapa hardcoded + helper)
    try:
        from wix_taxonomia import categorias_para_materia, tags_ids_para_materia
        cat_ids = categorias_para_materia(
            tag_principal=getattr(m, 'tag_principal', ''),
            cidade=getattr(m, 'cidade', ''),
            tags_secundarias=list(getattr(m, 'tags_secundarias', []) or []),
        )
        if cat_ids:
            body["categoryIds"] = cat_ids

        # Hashtags vêm do post_instagram.hashtags (já curado pela angulação) +
        # palavras-chave do Sonnet (top 5)
        post_ig = getattr(m, 'post_instagram', {}) or {}
        hashtag_labels = list(post_ig.get('hashtags', []) or [])
        for kw in (reescrita or {}).get('keywords', [])[:5]:
            if kw and kw not in hashtag_labels:
                hashtag_labels.append(kw)
        tag_ids = tags_ids_para_materia(hashtag_labels[:10])
        if tag_ids:
            body["tagIds"] = tag_ids
    except Exception as e:
        print(f"[materia] Falha ao montar categorias/tags ({e}) — seguindo sem")

    # Capa com alt text descritivo + SEO (vai pra aba Geral do Wix).
    # Donário 2026-05-21: alt text SEMPRE preenchido e relevante p/ SEO da imagem.
    if cover and cover.get('id'):
        alt_capa = _alt_text_seo(m, cover, reescrita)
        body["media"] = {
            "wixMedia": {
                "image": {
                    "id": cover['id'],
                    "url": cover['url'],
                    "width": cover.get('width') or 1200,
                    "height": cover.get('height') or 630,
                    "altText": alt_capa,
                }
            },
            "displayed": True,
            "custom": False,
        }

    return body


def _revisar_draft(draft: dict, cover: dict | None = None) -> dict:
    """Checa que o draft post está pronto para publicação.

    Critérios (instrução Donário 2026-05-16):
    - Título não-vazio e ≤ 100 chars
    - Texto do artigo presente (richContent.nodes com pelo menos 1 PARAGRAPH não-vazio)
    - Imagem (cover ou IMAGE node no corpo) — sem texto sobreposto
    - Pelo menos 1 categoria preenchida (categoryIds)
    - Focus keyword preenchida (seoData.settings.keywords[isMain=true])
    - Meta description contém a focus keyword

    Retorna {ok: bool, avisos: [str]}.
    """
    avisos = []

    titulo = (draft.get("title") or "").strip()
    if not titulo:
        avisos.append("titulo vazio")
    elif len(titulo) > 100:
        avisos.append(f"titulo com {len(titulo)} chars > 100")

    nodes = ((draft.get("richContent") or {}).get("nodes") or [])
    paragrafos_com_texto = [
        n for n in nodes if n.get("type") == "PARAGRAPH"
        and any((c.get("textData", {}) or {}).get("text", "").strip()
                for c in n.get("nodes", []))
    ]
    if not paragrafos_com_texto:
        avisos.append("artigo sem parágrafos com texto")

    image_nodes_corpo = [n for n in nodes if n.get("type") == "IMAGE"]
    image_node_no_corpo = bool(image_nodes_corpo)
    cover_img = ((draft.get("media") or {}).get("wixMedia", {}).get("image", {}))
    cover_id = cover_img.get("id")
    if not (image_node_no_corpo or cover_id):
        avisos.append("sem imagem (cover nem inline)")

    # Donário 2026-05-21: toda imagem precisa de alt text (aba Geral) preenchido p/ SEO.
    if cover_id and not (cover_img.get("altText") or "").strip():
        avisos.append("capa sem alt text (aba Geral)")
    for n in image_nodes_corpo:
        if not ((n.get("imageData") or {}).get("altText") or "").strip():
            avisos.append("imagem inline sem alt text")
            break

    cat_ids = draft.get("categoryIds") or []
    if not cat_ids:
        avisos.append("sem categoria")

    seo = draft.get("seoData") or {}
    keywords = ((seo.get("settings") or {}).get("keywords") or [])
    focus = next((k.get("term") for k in keywords if k.get("isMain")), "")
    if not focus:
        avisos.append("sem focus keyword na aba Assistente")
    else:
        meta_desc = ""
        for tag in (seo.get("tags") or []):
            props = tag.get("props") or {}
            if props.get("name") == "description":
                meta_desc = props.get("content", "")
                break
        if focus.lower() not in meta_desc.lower():
            avisos.append(f"meta description sem a focus keyword '{focus}'")

    return {"ok": not avisos, "avisos": avisos}


_WIX_PLACEHOLDERS = ("ist1.ey...", "ist1.ey", "your-token", "")


def _wix_token_valido() -> str | None:
    t = os.getenv("WIX_SITE_TOKEN", "").strip()
    if not t or t in _WIX_PLACEHOLDERS or t.endswith("...") or len(t) < 30:
        return None
    return t


def _drafts_dir():
    override = os.environ.get("DRAFTS_MATERIAS_DIR", "").strip()
    if override:
        return override
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(os.path.dirname(project_root), "Materias_Radar")


def _grava_local_materia(m):
    local_dir = _drafts_dir()
    os.makedirs(local_dir, exist_ok=True)
    local = f"{local_dir}/{datetime.now().strftime('%Y-%m-%d')}_{m.id_hash[:8]}.json"
    body = _build_post_body(m, cover=None)
    body["_meta"] = {
        "data": datetime.now().isoformat(),
        "fonte": {"nome": m.fonte_nome, "url": m.url, "cidade": m.cidade},
        "score_combinado": m.score_combinado,
        "decisao_final": getattr(m, "decisao_final", ""),
        "tag_thumbnail": getattr(m, "tag_thumbnail", ""),
    }
    with open(local, "w", encoding="utf-8") as f:
        json.dump(body, f, ensure_ascii=False, indent=2)
    return local


def _gerar_e_subir_capa(m) -> dict | None:
    """Obtém uma imagem LIMPA (sem overlay de texto) e faz upload ao Wix Media.

    NOVO em 2026-05-16 (instrução Donário): a capa é uma foto real representativa,
    NÃO uma thumb branded com título sobreposto. Texto/chamada vão no nó CAPTION
    abaixo da imagem (no corpo do post) e na aba SEO do Wix.

    Estratégia em cascata (ver buscar_imagem_limpa.obter_imagem_limpa):
      1. og:image da fonte original
      2. Pexels API (PEXELS_API_KEY)
      3. Unsplash API (UNSPLASH_ACCESS_KEY)
      4. Geração via OpenAI DALL-E (OPENAI_API_KEY) — sem texto no prompt
      5. Gradiente SulTV liso (último fallback, ainda sem texto)

    Retorna {id, url, width, height, alt_text, fonte_credito, origem} ou None.
    """
    try:
        from imagens import upload_wix_media
        from buscar_imagem_limpa import obter_imagem_limpa
    except Exception as e:
        print(f"[materia] Sem módulos de imagem disponíveis ({e}) — pulando capa")
        return None

    # Monta query visual a partir do contexto editorial.
    # 'descricao_imagem' é o prompt natural do que a foto deve mostrar.
    # P0.2 — briefing_visual (se preenchido pelo Claude na fase 4) tem
    # precedência sobre o fallback construído a partir do subtítulo.
    sub = (getattr(m, 'subtitulo', '') or '').strip()
    desc_imagem = sub or m.titulo_sultv
    palavras_chave = []
    if getattr(m, 'tag_principal', ''):
        palavras_chave.append(m.tag_principal.replace('_', ' '))
    if getattr(m, 'cidade', ''):
        palavras_chave.append(m.cidade)

    bv = getattr(m, 'briefing_visual', None) or {}

    try:
        info_img = obter_imagem_limpa(
            url_fonte=getattr(m, 'url', ''),
            titulo=m.titulo_sultv,
            palavras_chave=palavras_chave,
            tag_principal=getattr(m, 'tag_principal', ''),
            cidade=getattr(m, 'cidade', ''),
            descricao_imagem=desc_imagem,
            briefing_visual=bv,
            gerar_variantes=True,
            formatos_alvo=['wix_cover'],
        )
    except Exception as e:
        print(f"[materia] Falha ao obter imagem limpa: {e}")
        return None

    print(f"[materia] Imagem origem={info_img['origem']} "
          f"({info_img['width']}x{info_img['height']}, "
          f"{len(info_img['bytes'])//1024}KB)")

    # P0.3 — usa variante 1600x900 (otimizada pra cover de blog editorial)
    # quando disponível; cai pra base se algo falhou no smart-crop.
    variantes = info_img.get('variantes', {})
    if variantes.get('wix_cover'):
        raw = variantes['wix_cover']
        mime, ext = 'image/jpeg', 'jpg'
    else:
        raw = info_img['bytes']
        mime = 'image/png'
        ext = 'png'
        if raw[:3] == b'\xff\xd8\xff':
            mime, ext = 'image/jpeg', 'jpg'

    fname = f"radar_{datetime.now().strftime('%Y%m%d')}_{m.id_hash[:8]}_cover.{ext}"
    info = upload_wix_media(raw, fname, mime_type=mime)
    if info and info.get('id'):
        # Mescla metadata da fonte para o SEO/AltText/legenda
        info['alt_text'] = info_img.get('alt_text') or m.titulo_sultv[:140]
        info['fonte_credito'] = info_img.get('fonte_credito', '')
        info['origem'] = info_img['origem']
        print(f"[materia] Foto anexada: {info['url']} (origem: {info['origem']})")
        return info
    print(f"[materia] Upload de foto falhou — postando sem capa")
    return None


def publicar_materia_com_texto(m, corpo_md: str):
    """Publica no Wix Blog usando texto já reescrito (modo cowork-faz-tudo).

    O `corpo_md` segue o mesmo formato do prompt oficial Donário:
        ### Título ###
        [título otimizado]

        ### Artigo ###
        [artigo em prosa contínua]

        ### Legenda sugerida ###
        [legenda até 120 chars]

        ### Palavras-chave ###
        [lista separada por vírgulas]

    A função:
    1. Parseia esses 4 blocos via _parse_resposta_sonnet (reutilizado)
    2. Injeta o resultado no cache _REESCRITA_CACHE
    3. Chama produzir_materia(m) que vai pegar do cache em vez de chamar Sonnet
    """
    reescrita = _parse_resposta_sonnet(corpo_md)
    if not reescrita.get("artigo"):
        print(f"[materia] Texto sem ### Artigo ### — pulando {getattr(m, 'titulo_sultv', '')[:60]}")
        return None
    cache_key = getattr(m, "id_hash", "") or str(uuid.uuid4())
    _REESCRITA_CACHE[cache_key] = reescrita
    return produzir_materia(m)


def produzir_materia(m):
    """Publica no Wix Blog com capa SulTV-branded; grava localmente em fallback."""
    if not getattr(m, "lead_materia_longa", "") and not getattr(m, "lead", ""):
        print(f"[materia] Sem lead para {m.id_hash[:8]} — pulando")
        return None

    token = _wix_token_valido()
    if not token:
        local = _grava_local_materia(m)
        print(f"[materia] Sem token Wix válido — gravado local: {local}")
        return local

    headers = {"Authorization": token, "Content-Type": "application/json"}
    site_id = os.getenv("WIX_SITE_ID", "").strip()
    if site_id:
        headers["wix-site-id"] = site_id

    # ====== Dedup pré-publicação (ponto crítico Donário 2026-05-16) ======
    try:
        from wix_dedup import checar_duplicata
        # Recupera o título reescrito do Sonnet (se houver) sem chamar a API
        cache_key = getattr(m, "id_hash", "")
        reescrita_cache = _REESCRITA_CACHE.get(cache_key, {}) if cache_key else {}
        titulo_pub = (reescrita_cache.get("titulo") or
                      getattr(m, "titulo_sultv", "") or
                      getattr(m, "titulo", ""))
        duplicata = checar_duplicata(m, titulo_publicar=titulo_pub)
        if duplicata:
            print(f"[materia] ✗ DUPLICATA detectada via {duplicata['fonte']}"
                  f"/{duplicata['match']} — pulando publicação.")
            print(f"[materia]   já publicada: {duplicata.get('post_url')}")
            print(f"[materia]   título existente: "
                  f"{(duplicata.get('titulo_existente') or '')[:80]}")
            return duplicata.get("post_url")
    except Exception as e:
        print(f"[materia] Dedup pré-publicação falhou ({e}) — seguindo com publicação")

    # 1. Obtém imagem limpa + sobe ao Wix Media antes de criar o post
    cover = _gerar_e_subir_capa(m)

    # 2. Body do draft post (com cover já injetado em richContent + media + SEO)
    body = {"draftPost": _build_post_body(m, cover=cover)}

    try:
        r = requests.post(WIX_API, headers=headers, json=body, timeout=30)
        r.raise_for_status()
        draft = r.json()["draftPost"]
        post_id = draft["id"]

        # ===== Revisão pré-publicação =====
        # Checa que o draft tem texto + imagem + categorias + focus keyword.
        # FIX 2026-05-25 (BUG_revisar_draft_sem_paragrafos): o POST do Wix NÃO ecoa
        # richContent.nodes de volta, então validar a resposta `draft` acusava
        # falsamente "artigo sem parágrafos com texto" e parava toda matéria como
        # rascunho. Validamos o conteúdo ENVIADO (body["draftPost"]) + o id retornado.
        draft_para_revisar = {**body["draftPost"], "id": post_id}
        checagem = _revisar_draft(draft_para_revisar, cover=cover)
        if not checagem["ok"]:
            print(f"[materia] ⚠ revisão pré-publicação falhou: "
                  f"{', '.join(checagem['avisos'])}")
            print(f"[materia]   draft permanece NÃO publicado (id={post_id}) "
                  f"— inspecionar no Wix Editor antes de publicar manualmente.")
            return f"https://manage.wix.com/dashboard/{os.getenv('WIX_SITE_ID','')}/blog/draft/{post_id}"

        publish_url = f"{WIX_API}/{post_id}/publish"
        requests.post(publish_url, headers=headers, timeout=30)
        # FIX (Donário 2026-06-03): a URL pública usa o SLUG do título, não o UUID.
        # Resolve a URL real via API de posts; fallback no slug do draft; por último UUID.
        _fb = ""
        _slug_draft = (draft.get("slug") or "").strip()
        if _slug_draft:
            from urllib.parse import quote as _q
            _fb = f"https://www.sultv.com.br/post/{_q(_slug_draft, safe='')}"
        url_publicada = _url_publica_do_post(post_id, headers, fallback=_fb)
        print(f"[materia] PUBLICADA (revisão OK): {url_publicada}")

        # Registra no histórico para dedup futuro
        try:
            from wix_dedup import registrar_publicacao
            registrar_publicacao(
                m, post_id_wix=post_id, post_url=url_publicada,
                titulo_publicado=draft.get("title", ""),
            )
        except Exception as e:
            print(f"[materia] ⚠ Falha ao registrar no histórico: {e}")

        return url_publicada
    except requests.HTTPError as e:
        print(f"[materia] FALHA Wix HTTP {e.response.status_code}: "
              f"{e.response.text[:300]}")
        return None
    except Exception as e:
        print(f"[materia] FALHA Wix: {e}")
        return None
