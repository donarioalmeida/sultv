---
name: sultv-radar-pauta-diaria
description: SulTV Radar — pauta diária 06:00 BRT no modo cowork-faz-tudo. Coleta com deadline rígido, classificação editorial rule-based em massa, angulação + guardrail final, redação no padrão SulTV, publicação Wix + Meta + Sheets. Sem chamada à API Anthropic — toda a parte de IA roda dentro da própria sessão Cowork. Use SEMPRE que o scheduled task `sultv-radar-pauta-diaria` disparar ou quando Donário pedir "roda a pauta do dia", "executa o radar SulTV", "produz o conteúdo de hoje", "pauta SulTV de hoje", "publica as matérias do dia".
---

> **Cópia sincronizada (29/05/2026)** do SKILL.md operante em `/Users/donariolopesdealmeida/Documents/Claude/Scheduled/sultv-radar-pauta-diaria/SKILL.md`. O que dispara às 06:00 BRT é o de `Documents/Claude/Scheduled/`. Manter as duas cópias em sincronia.

Rodar a pauta diária do SulTV Radar no fluxo **cowork-faz-tudo**: Claude faz toda a parte de IA dentro da própria sessão Cowork. Não chama `api.anthropic.com`. Não usa créditos pagos.

# Por quê

O pipeline original (radar_main.py) chamava Sonnet/Haiku via API. Em 2026-05-15 a estratégia mudou: o Cowork (Claude) executa a curadoria editorial dentro da sessão usando os scripts auxiliares bundled em `scripts/`. Resultado: zero custo de API e mais controle sobre o resultado.

O scheduled task que dispara este SKILL.md vive em `/Users/donariolopesdealmeida/Documents/Claude/Scheduled/sultv-radar-pauta-diaria/` e roda às 06:00 BRT todos os dias.

# Arquitetura

```
06:00 BRT  (scheduled task autônomo, Donário não está na sessão)
  └─> FASE 1 (bash, ~30s): coleta com deadline rígido
       → state/candidatos_<date>.json (~200 itens após dedup)
  └─> FASE 2 (bash, ~2s): classificação editorial rule-based em massa
       → state/curadas_<date>.json (com score_editorial, guardrails, formato)
  └─> FASE 3 (bash, ~1s): boost geográfico + quota 2/cidade
       → state/aprovadas_<date>.json (top 14-20 itens)
  └─> FASE 4 (Claude na sessão): angulação editorial + guardrail final + redação
       → state/pauta_<date>.json + state/materias_<date>/<id_hash>.md
  └─> FASE 5 (bash): publicação Wix Blog + Meta API + Sheets + e-mail
  └─> FASE 6 (Claude): verify + atualiza artefato cowork sultv-radar-pauta-dia
```

# Execução

## Pré-flight: ambiente Python

O sandbox Cowork tem `/sessions` frequentemente saturado por outras sessões. Por isso, **antes da primeira execução do dia**, prepare as dependências em `/tmp/pylibs`:

```bash
# Limpa caches antigos (libera ~600MB se houver)
rm -rf /tmp/pypkgs /tmp/pip-libs /tmp/edge-libs 2>/dev/null || true

# Instala deps em /tmp (não em /sessions/.local que está cheio)
mkdir -p /tmp/pylibs
PIP_CACHE_DIR=/tmp/pipcache TMPDIR=/tmp pip install --no-cache-dir --target=/tmp/pylibs \
  feedparser beautifulsoup4 requests python-dotenv voyageai gspread \
  google-auth google-auth-oauthlib pillow anthropic 2>&1 | tail -5

# Confere que feedparser e anthropic estão lá
ls /tmp/pylibs/ | grep -E "feedparser|anthropic|google|voyageai" | head -5
```

A partir daqui, **TODA execução Python usa `PYTHONPATH=/tmp/pylibs`**. Sem isso, dá `ModuleNotFoundError: feedparser`.

> **Nota operacional (29/05/2026):** se o `/tmp/pylibs` herdado de outra sessão estiver read-only (ownership `nobody`) ou incompleto (sem feedparser/bs4/dotenv), instale as deps num diretório próprio (`/tmp/mylibs`) e use `PYTHONPATH=/tmp/mylibs:/tmp/pylibs` em todas as fases.

## Passo 1 — Coleta com deadline rígido

O bash da sessão Cowork tem timeout de 45s. A coleta original (`cowork_pipeline.py --fase coleta`) pode ultrapassar isso porque o pior caso de 167 fontes com timeout 20s/cada estoura o orçamento. Use o coletor com deadline global:

```bash
cd "/Users/donariolopesdealmeida/Meu Drive/CONEX — Holding & Hub/02_SulTV/Conteúdo Digital/sultv-radar-conteudo"
COLETA_DEADLINE_S=25 timeout --preserve-status --signal=KILL 35 \
  env PYTHONPATH=/tmp/pylibs python3 -u scripts/coleta_deadline.py 2>&1 | tail -10
```

`scripts/coleta_deadline.py` (bundled neste repo):
- Encurta `coletor.TIMEOUT` para 4s por fonte (em vez dos 20s padrão)
- Roda 32 workers em paralelo
- Aborta tudo após `COLETA_DEADLINE_S` segundos e devolve o que conseguiu
- Aplica stop-list lexical + dedup por id_hash
- Escreve `state/candidatos_<date>.json` no formato esperado pelas fases seguintes

Resultado esperado: ~165 de 167 fontes concluídas, 250+ brutos, ~215 candidatos após dedup.

## Passo 2 — Classificação rule-based em massa

```bash
cd "/Users/donariolopesdealmeida/Meu Drive/CONEX — Holding & Hub/02_SulTV/Conteúdo Digital/sultv-radar-conteudo"
python3 scripts/classificar_cowork.py
```

`scripts/classificar_cowork.py` encoda a régua editorial completa (`prompts/01_classificacao_massa.md` + `prompts/04_guardrails_classifier.md`):

**Score editorial 1–10:**
- +4 pts cidade-núcleo (Camaquã, Tapes, Arambaré)
- +3 pts segunda camada (Cristal, Chuvisca, São Lourenço)
- +2 pts Pelotas (Costa Doce ampliada)
- +1 pt outras cidades RS
- –3 pts conteúdo Brasil/internacional sem âncora regional
- +1 pt fato concreto (verbos: aprova/abre/lança/inaugura)
- +1 pt fonte com score_fonte ≥ 22

**Guardrails automáticos (alerta_guardrail=true, score=1, descartar):**
- Tragédia com vítima identificada (nome próprio + verbos de morte)
- Política partidária (eleição, candidato, sigla de partido)
- Saúde médica (diagnóstico, prescrição, tratamento)
- Conteúdo envolvendo menores
- Religioso/místico
- Crítica direta a parceiros (Canal Rural, Farsul, Cotrijal, CCGL, ABMRA, Ventiur, Anlab, Tecnopuc)
- Título genérico/vazio (< 15 chars ou em stop-list de menu)

**Formato sugerido:**
- score ≥ 9 → materia_longa
- score 7–8 + tag (notícia/política/segurança/comunidade núcleo) → materia_longa
- score 7–8 + tag (trânsito/acidente/saúde/serviço urbano) → nota_curta
- score 4–6 → post_instagram
- score ≤ 3 ou guardrail → descartar

Saída: `state/curadas_<date>.json` com 215 itens classificados em ~1s.

> **Quando uma classificação ad-hoc do Claude faz sentido?** Quando o volume cai (≤ 30 itens) e há tempo, Claude pode classificar item por item lendo `state/candidatos_<date>.json` direto na sessão. Para o volume diário (~200 itens), o classificador rule-based é mais rápido e suficientemente preciso. **NÃO chame `anthropic.Anthropic()` em código Python** — quebra a regra cowork-faz-tudo.

## Passo 3 — Aprovação (boost geo + quota)

```bash
cd "/Users/donariolopesdealmeida/Meu Drive/CONEX — Holding & Hub/02_SulTV/Conteúdo Digital/sultv-radar-conteudo"
timeout 30 env PYTHONPATH=/tmp/pylibs python3 -u scripts/cowork_pipeline.py --fase aprovar 2>&1 | tail -10
```

Aplica boost geográfico final + quota máxima 2/cidade. Gera `state/aprovadas_<date>.json` com ~14 itens (típico).

## Passo 4 — Angulação + redação (Claude na sessão)

**Esta é a parte que exige julgamento editorial humano-like.** Claude lê `state/aprovadas_<date>.json` e produz `state/pauta_<date>.json` + `state/materias_<date>/<id_hash>.md`.

Para cada um dos ~14 aprovados, decida `decisao_final`:

| Decisão | Quando | Output |
|---|---|---|
| `PUBLICAR` | Fato concreto, regional Sul-RS, fonte confiável, sem guardrail | Angulação completa + matéria longa (se materia_longa) |
| `REBAIXAR` | Pauta nacional sem âncora Sul-RS, conteúdo agregado/confuso, item duplicado-ish | Angulação leve, sem matéria longa, vira nota interna |
| `BLOQUEAR` | Título é cabeçalho de seção (ex.: "Assistência Social", "Fotos do Flickr"), edital procedural, esporte de região distante, qualquer guardrail novo identificado na angulação | Sem angulação, motivo no campo `decisao_motivo` |
| `ALERTA_HUMANO` | Parceiro estratégico em contexto sensível, dúvida sobre regra 5/7/14 | Email para Donário antes de publicar |

**Quota: máximo 10 PUBLICAR/dia (regra 14).** Excedeu → vira REBAIXAR.

### Estrutura de `state/pauta_<date>.json`

```json
{
  "data": "YYYY-MM-DD",
  "gerado_em": "...iso...",
  "total": 14,
  "pauta": [
    {
      "id_hash": "...", "titulo": "...", "cidade": "...", "fonte_nome": "...",
      "score_editorial": 9, "score_combinado": 17.8, "tag_principal": "...",
      "formato_sugerido": "materia_longa",
      "titulo_sultv": "...", "subtitulo": "...", "lead": "...",
      "chamada_faixa": "...(chamada curta/SEO p/ a faixa-legenda dos posts FB/IG; uppercase no render; até ~8 palavras)",
      "ganchos_3": ["...", "...", "..."],
      "angulo_editorial": "...",
      "fontes_complementares_sugeridas": ["..."],
      "lead_materia_longa": "...",
      "post_instagram": {"caption": "...", "hashtags": ["...", "..."]},
      "roteiro_short_60s": {"abertura_2s": "...", "desenvolvimento_45s": "...", "fechamento_8s": "...", "cta_5s": "...", "trilha_sugerida": "..."},
      "tag_thumbnail": "...",
      "decisao_final": "PUBLICAR",
      "decisao_motivo": "..."
    }
  ]
}
```

### Estrutura das matérias longas

Para cada PUBLICAR + materia_longa (até 10), escreva `state/materias_<date>/<id_hash>.md` no formato literal do `PROMPT_REDACAO_SULTV` (em `scripts/produzir_materia.py` linhas 25–59):

```
### Título ###
[título otimizado SEO, até 100 chars]

### Artigo ###
[artigo em prosa contínua, ~1.500 caracteres, sem subtítulos]

### Legenda sugerida ###
[legenda até 120 chars]

### Palavras-chave ###
[lista separada por vírgulas]
```

**Tom**: terceira pessoa institucional, audiência rural+urbana RS, contexto Costa Doce / Sul do RS. Sem "salva esse vídeo", sem "te conto", sem primeira pessoa. Lead começa com dado quantitativo + ancoragem regional.

### Briefing visual — obrigatório em todo item PUBLICAR (NOVO em 2026-05-18, P0.2)

Para cada item com `decisao_final = PUBLICAR`, o Claude precisa adicionar um dict `briefing_visual` no JSON da pauta, com 4 campos. O pipeline (`buscar_imagem_limpa.obter_imagem_limpa`) usa esses 4 campos para escolher a melhor imagem na cascata. Sem `briefing_visual`, cai num fallback genérico que costuma trazer fotos pouco relevantes.

```json
"briefing_visual": {
  "descricao_pt": "Plantação de arroz inundada ao amanhecer no Sul do RS, vista aérea, sem pessoas",
  "query_en": ["rice paddy aerial brazil", "flooded rice field sunrise"],
  "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
  "prompt_ia": "Aerial wide shot of a flooded rice paddy at sunrise in southern Brazil, golden light reflecting on water, no people, no text, editorial photojournalism style"
}
```

Regras para preencher:
- **`descricao_pt`**: o que a foto deve mostrar, em pt-BR, com cidade e elementos visuais concretos. Vira `alt_text` da imagem e query natural. Evite descrição abstrata ("notícia importante") — diga "campo de soja", "auditório com plateia", "rua de paralelepípedos no centro histórico de Pelotas".
- **`query_en`**: 2-3 queries curtas em inglês — usadas só como reforço nas fontes de FOTO (acervo/stock). O pipeline já monta as queries principais em **português + âncora regional** (cidade + "Rio Grande do Sul"). Termos visuais (objetos, cenas, paisagens), não conceitos abstratos.
- **`evitar`**: tudo que a foto NÃO pode ter — nomes próprios, pessoas identificáveis em pautas sensíveis, logos de marcas, texto/legendas embutidas.
- **`prompt_ia`**: 1-2 frases em inglês descrevendo **só o TEMA/cena**. NÃO precisa repetir âncora regional nem "no text" — o pipeline adiciona automaticamente a âncora do Sul do RS (`_ANCORA_SUL`) + os negativos (`_NEGATIVOS_SUL`: sem texto, placa, banner, adesivagem, país estrangeiro). Prefira enquadramento de **paisagem/ambiente** a close-ups de veículos/placas (a IA pode alucinar texto nesses casos).

**Conceito de imagem (Donário 2026-06-16):** TEMA primeiro, com ambientação inconfundivelmente do Sul do RS / Costa Doce; a cidade é reforçada na legenda e no `alt_text`, não obrigatoriamente "estampada" na foto. A **fonte primária é IA gratuita Pollinations (FLUX)**, sempre ancorada no Sul-RS — isso elimina fotos "gringas". og:image/stock/acervo entram só como rede de segurança e passam por **filtro OCR anti-texto/anti-estrangeiro**: qualquer foto com banner, placa, adesivagem ou idioma não-PT é rejeitada. Sem imagem segura → foto temática neutra do Sul → último recurso card SulTV (gradiente, sem texto). Para desligar a IA: `POLLINATIONS_OFF=1` no `.env`. Token opcional `POLLINATIONS_TOKEN` (sk_) remove rate limit.

### Chamada da faixa-legenda (`chamada_faixa`) — para todo item PUBLICAR (NOVO em 2026-05-29)

Para cada item `PUBLICAR`, escreva também `chamada_faixa`: uma **chamada curta/SEO** (até ~8 palavras) que será renderizada em caixa-alta dentro da faixa-legenda dos posts FB/IG (ver Regra 8). Deve ser punchy e conter a palavra-chave principal. Na falta do campo, `publicar_post._chamada_faixa()` encurta o `titulo_sultv` automaticamente, mas o ideal é o controle editorial explícito.

### Atalho: bundle `scripts/angular_cowork.py`

`scripts/angular_cowork.py` é um esqueleto onde Claude pode encodar as decisões + textos diretamente em código Python e rodar uma única vez. Use quando há muitos itens semelhantes — copiar o dicionário `PAUTA_ANGULADA` do dia anterior e ajustar os textos costuma economizar tempo.

```bash
# Depois de editar PAUTA_ANGULADA e MATERIAS no script com o conteúdo do dia:
python3 scripts/angular_cowork.py
```

Saída: `state/pauta_<date>.json` + N arquivos `.md` em `state/materias_<date>/`.

## Passo 5 — Publicação

```bash
cd "/Users/donariolopesdealmeida/Meu Drive/CONEX — Holding & Hub/02_SulTV/Conteúdo Digital/sultv-radar-conteudo"
timeout 40 env PYTHONPATH=/tmp/pylibs python3 -u scripts/cowork_pipeline.py --fase publicar 2>&1 | tail -30
```

Faz, nesta ordem:
1. Escreve na aba `Radar_Diario` do Google Sheets (pode falhar — ver Failure modes)
2. Publica matérias longas no Wix Blog (lê `state/materias_<date>/*.md`)
3. Publica posts no Facebook + Instagram via Meta Graph API
4. Envia e-mail de status para donario@donario.com

### Protocolo de publicação no Wix (atualizado 2026-05-16)

Cada matéria é montada com **imagem limpa + SEO completo + categorias + tags + revisão pré-publicação**. O fluxo está bundlado em `scripts/produzir_materia.py` + `scripts/wix_taxonomia.py` + `scripts/buscar_imagem_limpa.py`. Comportamento esperado:

**Imagem (sem texto sobreposto).** A capa e a imagem inline NÃO recebem mais o título burned in. A função `_gerar_e_subir_capa` chama `buscar_imagem_limpa.obter_imagem_limpa()` que tenta, em cascata (conceito Donário 2026-06-16 — TEMA primeiro, ancorado no Sul-RS, zero marcador estrangeiro):
1. **IA gratuita Pollinations (FLUX)** — FONTE PRIMÁRIA, sem chave/sem custo; prompt travado em "interior do RS / Costa Doce" + negativos (sem texto/placa/banner/adesivagem/país estrangeiro). Regenera 1x se o FLUX alucinar texto legível (OCR).
2. Gemini Imagen / 3. OpenAI — reforço de IA (só se houver `GEMINI_API_KEY`/`OPENAI_API_KEY`; já ancorados no Sul-RS)
4. `og:image` da fonte — passa por **filtro OCR anti-texto/anti-estrangeiro** (rejeita banner/placa/idioma não-PT)
5. Acervo livre (Wikimedia/Openverse) com query **PT + âncora regional**, filtrado por OCR
6. Pexels/Unsplash (precisa key) — filtrados por OCR
7. Gradiente/card SulTV liso (sem texto) — último recurso

Nenhuma chave é obrigatória: a IA primária (Pollinations) cobre todas as pautas sem custo. `POLLINATIONS_OFF=1` desliga a IA; `POLLINATIONS_TOKEN` (sk_) remove rate limit no servidor.

**Legenda da imagem.** Vai como **nó CAPTION SEPARADO** logo abaixo do nó IMAGE no corpo do post (centralizado, itálico) — o Wix Ricos ignora o campo `caption` dentro de `imageData`. O texto da legenda é: subtítulo da matéria + crédito da foto, ou a "Legenda sugerida" do bloco do prompt SulTV. Nunca aparece em cima da imagem.

**SEO — aba Básico + Rede Social.** Já preenchido via `seoData.tags[]`: meta description (≤160 chars, sempre contém a focus keyword), keywords, Open Graph (og:title, og:description, og:image, og:type=article) e Twitter cards (summary_large_image).

**SEO — aba Assistente (focus keyword).** Vai em `seoData.settings.keywords[]` no formato `[{term: <focus>, isMain: true, origin: "RADAR_SULTV"}]`. A focus keyword:
- É escolhida via `_focus_keyword()`: prefere `keywords[]` do prompt SulTV se aparecerem no título; senão extrai as primeiras palavras significativas do título (excluindo stop words).
- **SEMPRE consta no título** — se não constar, prepende automaticamente.
- **SEMPRE consta na meta description** — ajustada para incluir a focus se estiver ausente.

**SEO — AltText da imagem.** O `media.altText` (cover) e o `imageData.altText` (inline) usam a descrição visual gerada pelo prompt (`obter_imagem_limpa.alt_text`) ou, em fallback, o subtítulo / título da matéria. Sempre descreve o que está na foto, não o tema do artigo.

**Configurações — Categorias.** O Wix Blog SulTV tem 24 categorias mapeadas em `wix_taxonomia.CATEGORIES` (snapshot 2026-05-16). A função `categorias_para_materia(tag_principal, cidade, tags_secundarias)` decide automaticamente:
- 1 categoria temática (Trânsito, Agro, Política, Segurança, Saúde, Economia, etc.) baseada em `tag_principal`
- 1 categoria geográfica se a cidade for cidade-núcleo (Camaquã, Tapes, Arambaré, Cristal, Chuvisca, São Lourenço, Dom Feliciano)
- Adiciona "Rio Grande do Sul" quando a tag é estadual e a cidade não é núcleo
- Até 1 categoria extra via `tags_secundarias` (máximo 3 no total)

Quando a Donário criar nova categoria no painel Wix, rodar `python3 scripts/wix_taxonomia.py --sync` e atualizar o dict `CATEGORIES` no arquivo.

**Configurações — Tags.** As tags são criadas on-the-fly via `tags_ids_para_materia()`. Fonte: `post_instagram.hashtags` (já curado na angulação) + até 5 keywords do prompt SulTV. Cada label é normalizado (sem `#`, ≤50 chars), procurado por `GET /blog/v3/tags`, e criado com `POST /blog/v3/tags` se não existir. Cache local em memória pra evitar listagens repetidas.

**Dedup pré-publicação (PONTO CRÍTICO — Donário 2026-05-16).** Antes de criar o draft e o cover, `wix_dedup.checar_duplicata(m, titulo)` valida que a matéria não é duplicata. Faz **duas verificações** em cascata e para na primeira positiva:

1. **Histórico local persistente** — `state/historico_publicacoes.json` (append-only). Contém id_hash da fonte, URL canônica, título original, título normalizado e post_id Wix de TODA matéria que o Radar já publicou. Match em:
   - `id_hash` idêntico (mesma URL fonte do mesmo dia)
   - `url_fonte` canônica idêntica (mesma URL após remover utm_/fbclid/etc.)
   - `titulo_normalizado` idêntico nos últimos 365 dias (lowercase, sem acentos, sem stopwords, espaços colapsados)
2. **Consulta online ao Wix Blog** — `POST /blog/v3/posts/query` com filtro `title`:
   - `$eq` (exato, case-sensitive)
   - `$startsWith` (prefixo de 50 chars — pega variações de caixa no final)
   - `$contains` fuzzy (4-6 palavras significativas do segmento central) — confirmado com sobreposição ≥ 4 palavras na normalização para evitar falso positivo

Se qualquer das duas reportar duplicata, **o draft não é criado, a foto não é gerada, e a função retorna a URL existente**. Isso evita conta dupla de tags/categorias no Wix, dupla geração de imagem, e principalmente conteúdo duplicado indexado pelo Google.

Caso especial: se Donário deletar manualmente uma matéria publicada (via Wix Editor), o histórico local ainda mantém a entrada. A consulta online ao Wix retornará 0 resultados, mas o histórico local bloqueia a republicação. Para forçar republicação, remover a linha correspondente em `state/historico_publicacoes.json`.

Após sucesso no `POST /publish`, `wix_dedup.registrar_publicacao(m, post_id, post_url)` faz append no histórico — esse passo é não-opcional para que o dedup futuro funcione.

**Revisão pré-publicação.** Antes de chamar `POST /publish`, `_revisar_draft()` valida:
- Título não-vazio e ≤100 chars
- Pelo menos 1 parágrafo de texto não-vazio
- Pelo menos 1 imagem (cover ou inline)
- Pelo menos 1 categoria
- Focus keyword preenchida
- Meta description contém a focus keyword

Se algum critério falhar, o draft **NÃO é publicado** — fica no Wix Editor como rascunho com a URL `https://manage.wix.com/dashboard/<site_id>/blog/draft/<post_id>` para Donário revisar manualmente. Os avisos aparecem no log da fase publicar.

### Protocolo de publicação FB/IG — faixa-legenda (atualizado 2026-05-29)

Os posts de IMAGEM no Facebook e Instagram passam a sair com a **faixa-legenda padrão @sultv31** (aprovado por Donário 2026-05-29). Fluxo em `scripts/publicar_post.py::_gerar_e_subir_imagens_post`:
1. `obter_imagem_limpa(..., gerar_variantes=True, formatos_alvo=['fb_feed','ig_feed'])` devolve as variantes LIMPAS (smart-crop por formato).
2. `_chamada_faixa(m)` resolve a chamada curta/SEO (campo `chamada_faixa` da pauta; fallback encurta `titulo_sultv`).
3. `imagens.aplicar_faixa_legenda(variante, chamada)` é aplicada sobre `fb_feed` e `ig_feed` antes do upload ao Wix Media.

Faixa: compacta, sobreposta no terço inferior (foto visível acima e abaixo), Azul Profundo #166897 translúcido + fio Verde-Limão #8BC751 no topo + logo SulTV branco (HOR-BRANCA) à esquerda + chamada em caixa-alta (Outfit Bold) **centralizada** à direita. **Sem selo "30 Anos", sem crédito de foto.** A **capa do Wix permanece LIMPA** (a faixa é só FB/IG). Brand Kit: `Marketing e Marca/MKT - Marca/Brand_Kit_SulTV_v1`.

**Revisão obrigatória (emenda 2026-05-30).** `aplicar_faixa_legenda` agora garante: logo SEMPRE presente (cascata `_logo_para_faixa`: Brand Kit → watermark do acervo → wordmark "SulTV"), chamada SEMPRE coerente (`sanitizar_chamada` remove preposição/artigo pendurado no fim) e texto SEMPRE centralizado. `revisar_faixa_legenda(chamada, logo_origem, linhas)` valida os três e loga avisos. **`chamada_faixa` foi adicionado ao dataclass `MateriaPronta`** — antes era descartado na reconstrução em `fase_publicar`, fazendo a faixa cair no fallback que truncava o título (causa do bug "ESCOLA … PLACAS SOLARES DA" em 30/05). Regressão: `scripts/teste_faixa_revisao.py`.

### Outras notas operacionais da publicação

**Importante**: a publicação NÃO é idempotente — se algo der erro no meio, NÃO rerode `--fase publicar` sem antes verificar quais itens já foram publicados (vai duplicar no Wix/FB). Em caso de falha parcial, edite os logs manualmente e/ou publique caso a caso (ver `scripts/publicar_so_pendentes_<date>.py` — publica só um item por id_hash, respeitando o limite de 45s do bash).

Se o bash der timeout no meio da publicação (a sessão Cowork tem 45s por chamada), grave manualmente o log final:

```python
import json
from datetime import datetime, timezone
entry = {
  "ts": datetime.now(timezone.utc).isoformat(), "stage": "cowork_publicar",
  "pauta_total": 14, "publicar": 5,
  "materias_publicadas": 3, "posts_publicados": 1, "posts_falhas": 1,
  "shorts_descartados": 0, "sheets_ok": False,
  "materias_urls": ["https://www.sultv.com.br/post/..."],
}
with open("logs/<date>.json", "a") as f:
    f.write(json.dumps(entry, ensure_ascii=False) + "\n")
```

## Passo 6 — Verify + atualizar artefato

```bash
cd "/Users/donariolopesdealmeida/Meu Drive/CONEX — Holding & Hub/02_SulTV/Conteúdo Digital/sultv-radar-conteudo"
timeout 20 env PYTHONPATH=/tmp/pylibs python3 -u scripts/cowork_pipeline.py --fase verify 2>&1 | tail -10
```

Depois atualize o artefato Cowork `sultv-radar-pauta-dia` lendo `state/pauta_<date>.json` + os URLs retornados na publicação. O HTML do dia anterior em `/Users/donariolopesdealmeida/Documents/Claude/Artifacts/sultv-radar-pauta-dia/index.html` serve de template — basta atualizar:
- Data no header e título
- Funil do dia (Pauta / Publicar / Rebaixar / Bloquear / Matérias Wix / Posts FB / Posts IG)
- Tabela de itens com Score / Título / Formato / Tag / Decisão / Link Wix
- Bloco de alertas (Sheets, IG, disco, token Meta)

Use `mcp__cowork__update_artifact` com o id `sultv-radar-pauta-dia` e o HTML novo escrito em `/Users/donariolopesdealmeida/Library/Application Support/Claude/local-agent-mode-sessions/<id>/local_<id>/outputs/sultv-radar-pauta-<date>.html`.

# Regras absolutas (não relaxar sem aprovação explícita de Donário)

1. Os 14 guardrails do `prompts/04_guardrails_classifier.md` não podem ser afrouxados.
2. Quota máxima 10 PUBLICAR por dia (regra 14).
3. Tom Redação SulTV — terceira pessoa institucional, sem primeira pessoa, sem "salva esse vídeo", sem dramalhão.
4. Audiência TV aberta canal 31 — majoritariamente urbana das principais cidades do RS.
5. YouTube descontinuado por decisão de 08/05/2026 — `roteiro_short_60s` continua sendo gerado para histórico, mas Shorts não são produzidos nem publicados.
6. **Não chamar a API Anthropic do código Python.** Todo o trabalho de IA é feito por Claude na sessão Cowork.
7. Publicação não é idempotente — em caso de falha parcial, NÃO rerode `--fase publicar` inteira.
8. **Imagem adequada por plataforma — capa Wix LIMPA, posts FB/IG com FAIXA-LEGENDA** (instrução Donário 2026-05-18 P0, **emendada em 2026-05-29**). Formatos: capa Wix 1600×900 (16:9 editorial), FB 1200×630 (1.91:1), IG 1080×1350 (4:5). Regras por destino:
   - **Capa e imagem inline do Wix: SEM texto sobreposto** (mantido). Nunca burned in; texto/chamada vão na caption / nó CAPTION. As funções `gerar_thumb_branded`, `gerar_post_simples`, `gerar_capa_carrossel` e `gerar_card_carrossel` NÃO são chamadas na publicação Wix.
   - **Posts de imagem no FB e IG: COM faixa-legenda padrão @sultv31** (novo, aprovado por Donário 2026-05-29). Após gerar as variantes limpas, `publicar_post._gerar_e_subir_imagens_post` chama `imagens.aplicar_faixa_legenda(variante, chamada)` em `fb_feed` e `ig_feed` antes do upload. A faixa é compacta, sobreposta no terço inferior (foto visível acima e abaixo), Azul Profundo #166897 translúcido + fio Verde-Limão #8BC751 no topo + **logo OFICIAL SulTV à esquerda (sobre chip branco arredondado, ver Regra 8.1)** + chamada curta/SEO (uppercase, Outfit Bold) à direita. **Sem selo "30 Anos" e sem crédito de foto.** A chamada vem do campo `chamada_faixa` da angulação (fase 4); na falta dele, `_chamada_faixa()` encurta o `titulo_sultv` (até ~8 palavras / 62 chars).
   - `buscar_imagem_limpa.gerar_variantes_por_formato()` segue fazendo o smart-crop centralizado e devolvendo as variantes; a faixa é aplicada por cima apenas nas variantes de rede social.
   - **REVISÃO OBRIGATÓRIA da faixa-legenda (Donário 2026-05-30):** toda faixa FB/IG precisa ter, sempre: **(1) logo SulTV presente**, **(2) chamada que faça sentido** (sem preposição/artigo pendurado no fim, ex.: nunca terminar em "da", "de", "e"), e **(3) texto centralizado** na área à direita do logo. Implementado em `imagens.aplicar_faixa_legenda` + `imagens.revisar_faixa_legenda`. Garantias: o logo vem de uma cascata `_logo_para_faixa()` (logo OFICIAL → Brand Kit HOR-BRANCA → wordmark textual "SulTV"), então **nunca falta**; a chamada passa por `imagens.sanitizar_chamada()`; o texto é renderizado centralizado. **`chamada_faixa` é campo do dataclass `MateriaPronta`** (senão é descartado em `fase_publicar`). Teste de regressão: `scripts/teste_faixa_revisao.py` (inclui o caso real do bug "...placas solares da"). Origem do logo aparece no log: `[faixa-legenda] logo origem: ...` (esperado: `brand_oficial`).

   - **8.1 — LOGO CORRETO DA FAIXA (Donário 2026-05-31).** O FB de 31/05 saiu com o logo ERRADO porque, no sandbox Cowork, o Brand Kit não está acessível (o `SANDBOX_BASE` apontava para um ID de sessão antigo) e a cascata caía no `code/shorts_skill_scripts/sultv_logo_watermark.png` — um logo desatualizado/incorreto. Correção: o logo oficial ("SULTV quadrado vertical" — marca "S" em gradiente turquesa→verde + wordmark SulTV) foi rasterizado e gravado em `references/SULTV_quadrado_vertical.png` (colorido) e `references/SULTV_quadrado_vertical_alpha.png` (fundo transparente). O `_logo_para_faixa()` agora **prioriza** esse logo via `_logo_oficial_path()` e o cola sobre um **chip branco arredondado** (`_logo_em_chip()`) para ficar legível sobre a faixa azul. O watermark antigo foi **descontinuado** da cascata. Para trocar o logo no futuro, substitua os PNGs em `references/` (a versão `_alpha` é a usada na faixa).
9. **Toda matéria publicada no Wix precisa**: imagem limpa + focus keyword (no título e na meta description) + AltText descrevendo a foto + categoria temática + categoria geográfica (quando núcleo) + tags. A função `_revisar_draft` bloqueia a publicação se faltar algum desses itens — nesse caso o draft fica no Wix Editor para revisão manual.
10. **NÃO publicar duplicatas (Donário 2026-05-16, crítico)**. Antes de criar qualquer draft, `wix_dedup.checar_duplicata()` valida contra (a) histórico local `state/historico_publicacoes.json` e (b) consulta online `POST /blog/v3/posts/query`. Se houver match em id_hash, URL canônica da fonte ou título normalizado nos últimos 365 dias, **o pipeline pula a matéria** e retorna a URL existente. Após cada publicação bem-sucedida, `registrar_publicacao()` faz append no histórico — esse passo é não-opcional.

# Contexto operacional

- **Driver**: scheduled task Cowork `sultv-radar-pauta-diaria`, cron `0 6 * * *`, todo dia 06:00 BRT.
- **Repo do pipeline**: `/Users/donariolopesdealmeida/Meu Drive/CONEX — Holding & Hub/02_SulTV/Conteúdo Digital/sultv-radar-conteudo/`
- **State persistente**: `state/{candidatos,curadas,aprovadas,pauta}_<date>.json` + `state/materias_<date>/*.md`
- **Logs**: `logs/<date>.json` (uma linha JSON por stage)
- **Credenciais em `.env`**: VOYAGE_API_KEY (opcional — só usado se quiser dedup semântico), GOOGLE_SERVICE_ACCOUNT_JSON, WIX_SITE_TOKEN, META_LONG_LIVED_TOKEN, META_FB_PAGE_ID=105995162382818, META_IG_BUSINESS_ID=17841457371532451, SMTP_*
- **Token Meta**: válido até 2026-08-10 (janela de 90 dias). Se faltar < 15 dias, sinalize na resposta.
- **Launchd local**: desinstalado em 15/05/2026, plist de backup em `launchd/com.sultv.radar.diario.plist`.
- **Scripts bundled neste pipeline**:
  - `scripts/coleta_deadline.py` — coleta com deadline (workaround pro bash 45s)
  - `scripts/classificar_cowork.py` — classificador rule-based
  - `scripts/angular_cowork.py` — esqueleto pra angulação + redação
  - `scripts/cowork_pipeline.py` — orquestrador das fases bash (--fase aprovar/publicar/verify)
  - `scripts/produzir_materia.py` — publicação Wix (não chamar direto). Inclui: revisão pré-publicação (`_revisar_draft`), focus keyword (`_focus_keyword`), nó CAPTION separado (`_caption_node`)
  - `scripts/wix_taxonomia.py` — mapa 24 categorias do blog SulTV + helper de tags (cria on-the-fly via API)
  - `scripts/wix_dedup.py` — **dedup pré-publicação crítico** (histórico local em `state/historico_publicacoes.json` + consulta online ao Wix)
  - `scripts/buscar_imagem_limpa.py` — pipeline de imagem SEM overlay (og:image → Pexels → Unsplash → DALL-E → gradiente SulTV)
  - `scripts/publicar_post.py` — publicação FB/IG (aplica `imagens.aplicar_faixa_legenda` nas variantes antes do upload — ver Regra 8)
  - `scripts/imagens.py` — assets de marca + `aplicar_faixa_legenda()` (faixa-legenda padrão @sultv31 dos posts FB/IG)
- **Imagens limpas — API keys (`.env`)** (atualizado 2026-05-18, P0):
  - `GEMINI_API_KEY` (recomendado, **gratuito** no Google AI Studio — Imagen 3 via `imagen-3.0-generate-002:predict`)
  - `OPENAI_API_KEY` (opcional, ~US$0.04/imagem — `gpt-image-1` com fallback `dall-e-3`)
  - `PEXELS_API_KEY` (opcional, free tier robusto)
  - `UNSPLASH_ACCESS_KEY` (opcional, free tier robusto)
  - `IMAGE_GEN_PRIMARY=gemini|openai` (qual gerador IA entra primeiro na cascata; default `gemini`)
  - `IMAGE_GEN_MODEL_OPENAI=gpt-image-1|dall-e-3` (modelo OpenAI; default `gpt-image-1`)

  Sem nenhuma key, o pipeline ainda publica usando og:image da fonte ou gradiente SulTV — mas cobertura de imagens reais cai drasticamente. **Recomendação**: começar só com `GEMINI_API_KEY` (grátis no AI Studio). Adicionar OpenAI/Pexels/Unsplash conforme necessidade.

  Para **cidades-núcleo SulTV** (Arambaré, Cristal, Tapes, Camaquã, Chuvisca, São Lourenço do Sul, Dom Feliciano), a cascata é reordenada: og → Gemini → OpenAI → Pexels → Unsplash → gradiente. Para outras pautas (agro, evento, economia): og → Pexels → Unsplash → Gemini → OpenAI → gradiente.

# Failure modes

| Sintoma | Causa | Ação |
|---|---|---|
| `ModuleNotFoundError: feedparser` | Deps não instaladas em /tmp/pylibs | Rodar bloco "Pré-flight" acima |
| `No space left on device: /sessions/.../.local` | /sessions saturado por outras sessões | Instalar deps em /tmp/pylibs (ou /tmp/mylibs) com `--target=` |
| `/tmp/pylibs` read-only ou sem feedparser/bs4/dotenv | Diretório herdado de outra sessão (ownership nobody) | Instalar em `/tmp/mylibs` e usar `PYTHONPATH=/tmp/mylibs:/tmp/pylibs` |
| Bash timeout em --fase coleta (45s) | Coletor padrão usa timeout 20s/fonte, pode estourar | Usar `scripts/coleta_deadline.py` com COLETA_DEADLINE_S=25 |
| Fase coleta retorna < 50 itens | Múltiplas fontes quebradas no dia | Conferir `logs/<date>.json` por erros de scraping |
| Fase aprovar exit 2 | `state/curadas_<date>.json` não existe | Rodou pulou Passo 2 — rode `python3 scripts/classificar_cowork.py` |
| Fase publicar exit 2 | `state/pauta_<date>.json` não existe | Pulou Passo 4 — angule e gere a pauta antes de publicar |
| Wix HTTP 401 | WIX_SITE_TOKEN expirou | Renovar em developers.wix.com → ALERTA_HUMANO |
| Link da matéria nos posts FB/IG dá 404 / página vazia | A URL era montada como `/post/{post_id}` (UUID); a URL pública do Wix usa o SLUG do título | CORRIGIDO 2026-06-03 em `produzir_materia.py` (`_url_publica_do_post`): após `/publish`, consulta `GET /blog/v3/posts/{id}?fieldsets=URL` e usa `url.base+url.path` (slug). Ver RELEASE_NOTES_2026-06-03.md |
| Meta erro 190 OAuth | Token Meta expirou (válido até 2026-08-10) | Renovar via Graph API Explorer → ALERTA_HUMANO |
| Meta erro 10 (`Application does not have permission`) | App Meta sem escopo `instagram_content_publish` ou `pages_manage_posts` | Reabrir o app no Meta Developers e renovar permissões |
| Sheets falha "Service account não encontrada" | GOOGLE_SERVICE_ACCOUNT_JSON ausente no ambiente do sandbox Cowork | Esperado no sandbox — sinalize `sheets_ok=false` e siga, Donário atualiza manual |
| `[post] IG pulado` | META_IG_BUSINESS_ID vazio | Conferir `.env` — valor correto: `17841457371532451` |
| Itens "Assistência Social" / "Fotos do Flickr" / "INFORMAÇÕES AGROPECUÁRIAS" no top da pauta | Scraper pegou cabeçalho de seção como se fosse matéria | BLOQUEAR no passo 4 — não publicar |
| Matéria fica como rascunho não publicada no Wix | `_revisar_draft` reprovou (faltou imagem, categoria ou focus keyword) | Acessar `https://manage.wix.com/dashboard/<site_id>/blog/draft/<post_id>`, corrigir manualmente, publicar via painel |
| Capa volta a aparecer com título burned in | Algum caller chamou `gerar_thumb_branded` em vez de `obter_imagem_limpa` | Conferir que `_gerar_e_subir_capa` em `produzir_materia.py` está chamando `buscar_imagem_limpa.obter_imagem_limpa()` (não `imagens.gerar_thumb_branded`) |
| Post FB/IG SEM a faixa-legenda | `_chamada_faixa` devolveu vazio ou `aplicar_faixa_legenda` falhou | Conferir log `[post] faixa-legenda aplicada: "..."`; garantir `chamada_faixa`/`titulo_sultv` na pauta e Brand Kit acessível (logo + Outfit) |
| Faixa FB/IG SEM logo da SulTV | Brand Kit inacessível e sem fallback (bug pré-30/05) | Resolvido: `_logo_para_faixa()` cai no watermark `code/shorts_skill_scripts/sultv_logo_watermark.png` e, em último caso, wordmark "SulTV". Conferir log `[faixa-legenda] logo origem: ...`. Para fidelidade ao Brand Kit, montar `Marketing e Marca/.../Brand_Kit_SulTV_v1` |
| Chamada da faixa truncada / sem sentido (ex.: "...PLACAS SOLARES DA") | `chamada_faixa` não era campo do dataclass (descartado em `fase_publicar`) → fallback cortava o título em preposição | Resolvido: `chamada_faixa` é campo de `MateriaPronta` + `sanitizar_chamada()` remove preposição/artigo pendurado. Rodar `python3 scripts/teste_faixa_revisao.py` |
| Texto da faixa não centralizado | render usava `texto_x` fixo (alinhado à esquerda) | Resolvido: cada linha é centralizada na área à direita do logo em `aplicar_faixa_legenda` |
| Faixa sem logo / fonte fora do padrão | Brand Kit não resolvido no sandbox (path de sessão antiga) | Conferir que `imagens.BRAND_KIT_BASE`/`SANDBOX_BASE` apontam para o mount atual de `Marketing e Marca/.../Brand_Kit_SulTV_v1` |
| Imagem cai sempre no gradiente SulTV liso | API keys de Pexels/Unsplash/OpenAI ausentes E og:image da fonte não acessível | Adicionar `PEXELS_API_KEY` / `UNSPLASH_ACCESS_KEY` no `.env` |
| Tags criadas em duplicidade (versões com `#` e sem) | Cache local resetou e a normalização não removeu o `#` | Conferir `tags_ids_para_materia` em `wix_taxonomia.py` — `lstrip("#")` deve estar presente |
| Categoria nova criada no painel não aparece | Mapa `CATEGORIES` em `wix_taxonomia.py` está estático | Rodar `python3 scripts/wix_taxonomia.py --sync` e atualizar o dict manualmente |
| Matéria pulada com "DUPLICATA detectada" mas Donário quer publicar | Histórico local marcou (mesma URL fonte, mesmo título ou ID) | Editar `state/historico_publicacoes.json` removendo a entry, ou alterar `titulo_sultv` na pauta para algo distinto |
| Mesma URL fonte publicada duas vezes (raro) | Histórico vazio E consulta Wix falhou (timeout/auth) | Conferir `WIX_SITE_TOKEN` no `.env`; rodar `python3 scripts/wix_dedup.py --dump` para auditar últimas 10 entradas |
| Backfill faltando de execuções antigas | Histórico só nasceu em 16/05/2026 | Usar `wix_dedup.backfill_de_pauta(pauta_path, urls)` passando dict {id_hash: post_url} extraído dos logs |
| `[buscar_imagem] Gemini HTTP 429` | Quota AI Studio estourada (Imagen 3) | Trocar `IMAGE_GEN_PRIMARY=openai` no .env ou esperar reset da quota Google |
| `[buscar_imagem] OpenAI HTTP 401` | `OPENAI_API_KEY` inválida ou expirada | Renovar key em platform.openai.com/api-keys |
| Variantes saem com ~6KB e visual chapado (azul liso) | Caiu na 6ª estratégia (`gradiente_sultv`) — todas as anteriores falharam | Conferir API keys no `.env`, conferir cota Gemini/OpenAI, conferir se `og:image` da fonte está acessível |
| Post FB ou IG sai com proporção errada (cortado/borda) | Smart-crop falhou em `gerar_variantes_por_formato` ou variante específica não foi gerada | Conferir logs `[variantes] erro em <formato>:` e validar que a imagem base tem ao menos 1100px no menor lado |

# Observações pós-execução

Ao finalizar, sinalize na resposta:
- Quantas matérias longas foram publicadas e os URLs Wix
- Quantos posts FB/IG foram publicados (ou se IG falhou por permissão)
- Se Sheets falhou (`sheets_ok=false`)
- Se há item com `decisao_final = ALERTA_HUMANO` aguardando aprovação
- Status do token Meta (dias restantes até 2026-08-10)
- Status do disco /sessions se a coleta precisou rodar com deadline reduzido
