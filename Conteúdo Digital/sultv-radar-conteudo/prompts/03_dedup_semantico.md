# Dedup semântico — pipeline e prompt de desempate

## Estratégia em 3 camadas

### Camada 1 — Hash exato da URL canônica
- Aplicado SEMPRE primeiro, antes de qualquer chamada IA.
- Normaliza URL (remove utm_*, fragmento, trailing slash, lowercase do host).
- Hash SHA1 — se já existe na base nas últimas 7 dias, descarta.
- **Custo:** zero (Python local).
- **Pega:** ~30% das duplicatas (republicações, RSS duplicado, caches).

### Camada 2 — Embedding de título + clustering
- Para cada matéria que passou da Camada 1, gera embedding do título (Voyage AI ou OpenAI text-embedding-3-small).
- Compara com embeddings das últimas 48h via cosine similarity.
- Threshold: **similaridade ≥ 0.85** = mesmo evento.
- Se encontrar match, agrupa matérias num "evento" e mantém a com `score_fonte` mais alto como representante.
- Demais entram como `fontes_relacionadas` da matéria principal.
- **Custo:** ~US$ 0.50/mês (Voyage embeddings cobram por token).
- **Pega:** ~50% adicional das duplicatas (mesmo fato, fontes diferentes).

### Camada 3 — Desempate por LLM (apenas casos limítrofes)
- Quando similaridade fica entre **0.75 e 0.85** (zona cinza), aciona Haiku para julgar.
- Haiku decide: "É o mesmo evento?" sim/não.
- **Custo:** ~US$ 0.50/mês (poucas chamadas).
- **Pega:** ~10% adicional, casos sutis.

**Resultado esperado:** de 500 itens brutos coletados/dia → ~250 itens deduplicados → top 30 vão para curadoria angulação.

---

## Prompt da Camada 3 — Desempate (Haiku)

**Modelo:** `claude-haiku-4-5-20251001`
**Temperatura:** 0
**Max tokens:** 50
**Quando:** chamado pontualmente quando cosine similarity ∈ [0.75, 0.85]

### System

Você é um classificador binário. Sua única tarefa é decidir se duas notícias falam do MESMO EVENTO real, ainda que com palavras diferentes. Responda apenas em JSON. Não explique.

**Regras:**
- "Mesmo evento" = mesmo fato no mundo real, mesma data, mesmos protagonistas. Pode ser republicação, follow-up curto ou cobertura de outra fonte.
- "Eventos diferentes" = mesmo tema mas fatos distintos (ex.: 2 acidentes na mesma BR no mesmo dia, ou 2 colheitas em municípios diferentes).
- Em dúvida, responda `false` (preferir falso negativo a falso positivo).

### User

```
NOTÍCIA A: {titulo_a}  |  Resumo: {resumo_a_100chars}  |  Fonte: {fonte_a}  |  Data: {data_a}
NOTÍCIA B: {titulo_b}  |  Resumo: {resumo_b_100chars}  |  Fonte: {fonte_b}  |  Data: {data_b}
```

### Output

```json
{"mesmo_evento": true}
```
ou
```json
{"mesmo_evento": false}
```

### Exemplos few-shot

**Exemplo 1 — mesmo evento:**
```
A: Arroz do RS atinge recorde de 7,8 t/ha na Metade Sul, diz IRGA  |  Fonte: IRGA  |  2026-04-30
B: Safra de arroz gaúcha bate marca histórica de produtividade  |  Fonte: Canal Rural  |  2026-04-30
→ {"mesmo_evento": true}
```

**Exemplo 2 — eventos diferentes:**
```
A: Acidente na BR-116 em Camaquã deixa 2 feridos  |  2026-04-30
B: Acidente na BR-290 perto de Eldorado bloqueia faixa  |  2026-04-30
→ {"mesmo_evento": false}
```

**Exemplo 3 — follow-up (mesmo evento):**
```
A: Defesa Civil RS emite alerta de geada para Serra  |  2026-04-29
B: Geada na Serra Gaúcha confirma alerta da Defesa Civil  |  2026-04-30
→ {"mesmo_evento": true}
```

---

## Pseudocódigo do pipeline

```python
def dedup_pipeline(items_24h, base_48h):
    # Camada 1
    seen_hashes = set()
    layer_1 = []
    for it in items_24h:
        h = sha1(canonical_url(it.url))
        if h not in seen_hashes:
            seen_hashes.add(h)
            layer_1.append(it)

    # Camada 2
    embeddings = batch_embed([it.titulo for it in layer_1])
    layer_2 = []
    eventos = {}
    for it, emb in zip(layer_1, embeddings):
        match = find_best_match(emb, base_48h.embeddings, threshold=0.75)
        if match is None:
            layer_2.append(it)
            eventos[it.id] = [it]
        elif match.similarity >= 0.85:
            # mesmo evento, sem ambiguidade
            eventos[match.id].append(it)
        else:
            # zona cinza — Camada 3
            decision = haiku_judge(it, match.item)
            if decision["mesmo_evento"]:
                eventos[match.id].append(it)
            else:
                layer_2.append(it)
                eventos[it.id] = [it]

    # Para cada evento, mantém o representante (maior score_fonte)
    representantes = []
    for evento_id, group in eventos.items():
        rep = max(group, key=lambda x: x.score_fonte)
        rep.fontes_relacionadas = [x.id for x in group if x != rep]
        representantes.append(rep)

    return representantes
```

---

## Threshold tuning — recomendado em produção

- Comece com threshold **0.85**.
- Audite manualmente 30 amostras por semana durante o primeiro mês.
- Se taxa de falsos positivos > 5%, suba threshold para 0.88.
- Se taxa de falsos negativos > 10%, desça para 0.82.
- Threshold por bloco temático pode ser diferente: clima costuma ter títulos mais parecidos (subir threshold), trânsito costuma ter títulos genéricos (descer threshold).
