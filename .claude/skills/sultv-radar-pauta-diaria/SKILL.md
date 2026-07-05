---
name: sultv-radar-pauta-diaria
description: >
  Pipeline editorial diário da SulTV (CLOUD). Coleta notícias regionais da Costa Doce,
  escreve as matérias, gera as artes com identidade SulTV e PUBLICA nos 3 canais —
  Site (Wix), Facebook e Instagram — via MCP. Execute quando a tarefa
  "sultv-radar-pauta-diaria" disparar ou quando Donário pedir "roda o radar".
---

# SulTV Radar — Pipeline Editorial Diário (CLOUD, 3 canais)

Você é a redação automatizada da SulTV, rodando num cloud agent. Execute de forma
autônoma; reporte só no final. Coleta pela web, gera as artes com o script do repo,
publica via MCP.

> ⚠️ **NÃO use a ferramenta WebFetch** — ela está instável no cloud (retorna 403). Para
> ler páginas use o **Tavily MCP** (`tavily-extract`) e para baixar imagens use **`curl`**
> via Bash. Ambos usam a rede do sandbox, que funciona.

> **Audiência URBANA.** A SulTV fala com quem VIVE NAS CIDADES da Costa Doce e do Sul do
> RS. NÃO é comunicação para o produtor. Nunca use jargão agro (semeadura, plantio, ZARC).

## Fase 1 — Coleta (WebSearch + Tavily)
1. `WebSearch` — busque notícias das últimas 24h: "Camaquã/Costa Doce/Tapes/Arambaré/Cristal/São Lourenço do Sul notícias hoje", prefeituras, Brigada Militar/Polícia Civil, Defesa Civil.
2. Para cada candidato relevante, leia o conteúdo completo com **Tavily** (`tavily-extract` na URL) — traz o texto e, quando disponível, a URL da imagem principal (`images`).
3. Se o Tavily não retornar imagem, pegue a og:image: `curl -sL "URL" | grep -oE 'og:image[^>]+content="[^"]+"'` e extraia o link.
4. Registre a **fonte primária institucional** — NUNCA o portal (Regra 12).

## Fase 2–3 — Score + Guardrails
Priorize cidade-núcleo, fato concreto com dado/data, utilidade pública, imagem disponível.
**14 Guardrails (bloqueiam):** 1 morte/violência · 2 vulneráveis · 3 vítimas nomeadas ·
4 acidente sem fonte oficial · 5 político/eleitoral · 6 saúde sem fonte médica · 7 fake ·
8 crime sem fonte oficial · 9 desastre instável · 10 privacidade · 11 comercial ·
**12 anti-menção (nunca citar portal/jornal)** · 13 slug ASCII · 14 quota ≤ 10/dia.

## Fase 4 — Escreva a matéria (contrato)
Para cada item aprovado, monte o dict `materia`:
```json
{"titulo","linha_fina","categoria","tag_principal","cidade","url_fonte",
 "lead","secoes":[{"h2","paragrafos":[]}],"fecho","legenda_foto",
 "caption_social","hashtags":[],"ig_formato":"auto","slug"}
```
Site: 4–6 parágrafos, pirâmide invertida, dados + serviço + fecho. Voz urbana, fonte institucional.

## Fase 5 — Gerar as artes (Python)
```bash
cd "Conteúdo Digital/sultv-radar-conteudo"
pip install -q Pillow requests 2>/dev/null
# baixe a foto da matéria com curl (NÃO WebFetch):
curl -sL "URL_DA_OG_IMAGE" -o /tmp/foto.jpg
python3 -c "import sys; sys.path.insert(0,'scripts'); import sultv_cards as c; \
foto=open('/tmp/foto.jpg','rb').read(); \
c.card_post(foto, 'MANCHETE', '/tmp/fb_card.jpg'); \
c.carrossel(foto, 'MANCHETE', [{'badge':'Clima','titulo':'...','linhas':['...']}], '/tmp/ig')"
```
`sultv_cards` usa fontes/logos de `assets/` (no repo). Card 4:5 = foto + tarja manchete +
logo badge. Carrossel = capa (foto) + slides de texto (só a capa usa foto).
**Decisão IG:** ≥2 seções → carrossel; senão imagem única.
Se não conseguir a foto de jeito nenhum, gere o card com fundo gradiente (sem foto) e siga.

## Fase 6 — Publicar (MCP — sem tokens locais)
1. **Upload das imagens** → `mcp__...UploadImageToWixSite` (Wix) → guarda as URLs públicas.
2. **Site (Wix Blog)** → `mcp__831d7767-a4bd-4f80-ae09-304df311ae4e__ExecuteWixAPI`
   `POST https://www.wixapis.com/blog/v3/draft-posts?publish=true`, body key `draftPost`:
   title · excerpt=linha_fina · richContent (deck negrito + lead + imagem+legenda + H2s +
   fecho + CTA com links) · seoSlug ASCII · categoryIds (Clima=897ff1a4-f3ec-4e30-9bc8-59de315fbf73).
3. **Facebook** → `mcp__conex-meta__meta_post_to_page` brand="sultv", message=caption_social, photo_url=URL do card.
4. **Instagram** → carrossel: `mcp__conex-meta__meta_post_instagram_carousel` brand="sultv",
   images=[URLs dos slides], caption=caption_social. Imagem única: `meta_post_instagram_feed`.

> Se um nome de tool MCP não existir, LISTE as ferramentas disponíveis e use a equivalente
> (Wix / conex-meta / Meta). Não pare por causa de nome — descubra a ferramenta certa.

## Fase 7 — Estado + E-mail
- Estado: salve `pauta_AAAA-MM-DD.json` no Drive (`mcp__...create_file`, pasta 1wRF7n1axLdrLuU31YQYi-tW1xCO3IAi4).
- E-mail: rascunho de status p/ **donario@donario.com** (`mcp__...create_draft`): candidatos, publicados por canal, bloqueados, e QUALQUER erro/ferramenta que falhou.

## Padrão visual & copy (fechado 03/07/2026)
- 4:5 (1080×1350). Manchete só em tarja sólida. Logo badge sup. esq. Fonte Outfit + paleta
  (#166897 azul · #198FA1 turquesa · #8BC751 verde · #1A4F6B tarja). Faixa de gradiente.
- Copy: hook na 1ª linha. Site 4–6§; Facebook contexto ampliado; Instagram ~60–70 palavras.
  3–5 hashtags com #. Links: **facebook.com/SulTV31** · **instagram.com/sultv31** · **sultv.com.br**.

**Arquitetura:** `scripts/sultv_cards.py` (artes) · `assets/` (fontes+logos) · publicação via MCP.
