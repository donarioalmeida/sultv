"""
sultv-radar-conteudo — motor de curadoria com IA
=================================================
Orquestrador do Passo 3: classificação em massa, dedup semântico,
angulação editorial, guardrails e seleção do funil de produção.

Arquitetura completa do dia:
  Coleta (06:00) → Dedup (06:17) → Curadoria Haiku (06:20) → Score combinado (06:30)
  → Top 30 → Sonnet angulação top 20 (06:30) → Guardrails finais (06:31)
  → Persiste em Sheets (06:32) → Produção automática (06:35)

Dependências externas:
  - anthropic (pip)
  - voyageai (pip) — embeddings semânticos
  - python-Levenshtein (fallback rápido)
  - gspread + google-auth (Google Sheets)

Variáveis de ambiente esperadas:
  ANTHROPIC_API_KEY
  VOYAGE_API_KEY
  GOOGLE_SERVICE_ACCOUNT_JSON (path)
  SULTV_RADAR_SPREADSHEET_ID
"""

from __future__ import annotations
import hashlib
import json
import os
import re
from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse, urlunparse

import anthropic

# ============================================================
# Config
# ============================================================

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"
HAIKU_MODEL = "claude-haiku-4-5-20251001"
SONNET_MODEL = "claude-sonnet-4-6"

# Cache lazy dos prompts (lidos do disco apenas no primeiro uso)
_PROMPT_CACHE: dict[str, str] = {}

def _prompt(nome: str) -> str:
    if nome not in _PROMPT_CACHE:
        _PROMPT_CACHE[nome] = (PROMPTS_DIR / nome).read_text(encoding="utf-8")
    return _PROMPT_CACHE[nome]

QUOTA_DIARIA_PUBLICACAO = 10     # max matérias produzidas/dia (guardrail #14)
TOP_N_ANGULACAO = 20             # quantos passam pelo Sonnet
TOP_N_PERSISTIDO = 30            # quantos vão para Radar_Diario
DEDUP_THRESHOLD_HARD = 0.85      # acima → mesmo evento sem dúvida
DEDUP_THRESHOLD_LOW = 0.75       # abaixo → eventos diferentes
JANELA_DEDUP_HORAS = 48
JANELA_NOTICIA_VALIDA = 24       # guardrail #6: > 24h descarta

PESO_FONTE = 0.4
PESO_IA = 0.6

# ============================================================
# Modelo de dados
# ============================================================

@dataclass
class MateriaBruta:
    id_hash: str
    coletado_em: str
    bloco: str                # A, B, C, D
    fonte_id: int
    fonte_nome: str
    cidade: str
    titulo: str
    resumo: str
    url: str
    publicado_em: str
    score_fonte: int          # 5..25 do banco

@dataclass
class MateriaCurada(MateriaBruta):
    score_editorial: int = 0
    tag_principal: str = ""
    tags_secundarias: list[str] = field(default_factory=list)
    formato_sugerido: str = ""
    justificativa: str = ""
    alerta_guardrail: bool = False
    guardrail_motivo: str = ""
    score_combinado: float = 0.0
    fontes_relacionadas: list[str] = field(default_factory=list)

@dataclass
class MateriaPronta(MateriaCurada):
    titulo_sultv: str = ""
    subtitulo: str = ""
    lead: str = ""
    ganchos_3: list[str] = field(default_factory=list)
    angulo_editorial: str = ""
    fontes_complementares_sugeridas: list[str] = field(default_factory=list)
    roteiro_short_60s: dict = field(default_factory=dict)
    lead_materia_longa: str = ""
    post_instagram: dict = field(default_factory=dict)
    card_carrossel: dict = field(default_factory=dict)
    tag_thumbnail: str = ""
    # Chamada curta/SEO da faixa-legenda dos posts FB/IG. PRECISA ser campo do
    # dataclass, senão é descartado ao reconstruir MateriaPronta em fase_publicar
    # e a faixa cai no fallback que trunca o título (Donário 2026-05-30).
    chamada_faixa: str = ""
    decisao_final: str = ""           # PUBLICAR | BLOQUEAR | REBAIXAR | ALERTA_HUMANO
    decisao_motivo: str = ""
    # P0.2 — briefing visual escrito pelo Claude na fase 4 (2026-05-18)
    # Estrutura: {descricao_pt, query_en[], evitar[], prompt_ia}
    briefing_visual: dict = field(default_factory=dict)

# ============================================================
# Util
# ============================================================

def canonical_url(url: str) -> str:
    p = urlparse(url.lower().strip())
    qs = "&".join(q for q in (p.query or "").split("&")
                  if not q.startswith(("utm_", "fbclid", "gclid", "ref=")))
    return urlunparse((p.scheme, p.netloc, p.path.rstrip("/"), "", qs, ""))

def url_hash(url: str) -> str:
    return hashlib.sha1(canonical_url(url).encode()).hexdigest()

def load_prompt(name: str) -> str:
    return (PROMPTS_DIR / name).read_text(encoding="utf-8")

# ============================================================
# Camada 1 — dedup por hash de URL
# ============================================================

def dedup_por_hash(itens: list[MateriaBruta], hashes_recentes: set[str]) -> list[MateriaBruta]:
    visto = set(hashes_recentes)
    out = []
    for it in itens:
        if it.id_hash in visto:
            continue
        visto.add(it.id_hash)
        out.append(it)
    return out

# ============================================================
# Camada 2 + 3 — dedup semântico (embeddings + LLM desempate)
# ============================================================

def dedup_semantico(
    itens: list[MateriaBruta],
    base_recente: list[tuple[MateriaBruta, list[float]]],
    embed_fn,
    llm_judge_fn,
) -> dict[str, list[MateriaBruta]]:
    """
    Retorna dict {representante_id: [matérias do mesmo evento]}.
    """
    eventos: dict[str, list[MateriaBruta]] = {}

    titles = [it.titulo for it in itens]
    embs = embed_fn(titles)

    # Index simples por similaridade — em produção, usar FAISS ou pgvector
    for it, emb in zip(itens, embs):
        match_id, sim = _melhor_match(emb, base_recente)
        if match_id is None or sim < DEDUP_THRESHOLD_LOW:
            eventos[it.id_hash] = [it]
        elif sim >= DEDUP_THRESHOLD_HARD:
            eventos.setdefault(match_id, []).append(it)
        else:
            # zona cinza — aciona Haiku
            base_item = next(b for b, _ in base_recente if b.id_hash == match_id)
            mesmo = llm_judge_fn(it, base_item)
            if mesmo:
                eventos.setdefault(match_id, []).append(it)
            else:
                eventos[it.id_hash] = [it]
    return eventos


def _melhor_match(emb, base):
    if not base:
        return None, 0.0
    best_id, best_sim = None, 0.0
    for it_b, emb_b in base:
        sim = _cosine(emb, emb_b)
        if sim > best_sim:
            best_id, best_sim = it_b.id_hash, sim
    return best_id, best_sim


def _cosine(a, b):
    import math
    dot = sum(x*y for x, y in zip(a, b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(y*y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)

# ============================================================
# Curadoria Haiku — classificação em massa
# ============================================================

def curar_haiku(client: anthropic.Anthropic, item: MateriaBruta, prompt_system: str | None = None) -> dict:
    if prompt_system is None:
        prompt_system = _prompt("01_classificacao_massa.md")
    user_msg = (
        f"TÍTULO: {item.titulo}\n"
        f"RESUMO: {item.resumo[:500]}\n"
        f"FONTE: {item.fonte_nome} (score_fonte: {item.score_fonte}/25, bloco: {item.bloco})\n"
        f"CIDADE: {item.cidade}\n"
        f"DATA: {item.publicado_em}\n"
        f"URL: {item.url}\n"
    )
    resp = client.messages.create(
        model=HAIKU_MODEL,
        max_tokens=200,
        temperature=0.2,
        system=prompt_system,
        messages=[{"role": "user", "content": user_msg}],
    )
    txt = resp.content[0].text.strip()
    return _safe_json(txt)


def _safe_json(text: str) -> dict:
    """Extrai o primeiro objeto JSON válido do texto, mesmo que venha com explicação ao redor."""
    if not text:
        return {}
    # Remove code fences markdown
    text = re.sub(r"```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```", "", text)
    text = text.strip()
    # Tenta parse direto
    try:
        return json.loads(text)
    except Exception:
        pass
    # Procura primeiro { ... } balanceado
    start = text.find("{")
    if start == -1:
        return {}
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(text)):
        c = text[i]
        if esc:
            esc = False
            continue
        if c == "\\":
            esc = True
            continue
        if c == '"':
            in_str = not in_str
            continue
        if in_str:
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[start:i+1])
                except Exception:
                    return {}
    return {}

# ============================================================
# Score combinado
# ============================================================

def score_combinado(score_fonte: int, score_editorial: int) -> float:
    """
    Normaliza score_fonte (5..25) → 0..10, score_editorial já em 0..10.
    Combinado em 0..10.
    """
    fonte_norm = (score_fonte - 5) / 2.0   # 5→0, 25→10
    return round(PESO_FONTE * fonte_norm + PESO_IA * score_editorial, 2)

# ============================================================
# Curadoria Sonnet — angulação editorial
# ============================================================

def angular_sonnet(client: anthropic.Anthropic, m: MateriaCurada, prompt_system: str | None = None) -> dict:
    if prompt_system is None:
        prompt_system = _prompt("02_angulacao_editorial.md")
    user_msg = (
        f"TÍTULO ORIGINAL: {m.titulo}\n"
        f"RESUMO: {m.resumo}\n"
        f"FONTE: {m.fonte_nome} ({m.url})\n"
        f"DATA: {m.publicado_em}\n"
        f"CIDADE: {m.cidade}\n"
        f"TAG PRINCIPAL: {m.tag_principal}\n"
        f"TAGS SECUNDÁRIAS: {', '.join(m.tags_secundarias)}\n"
        f"FORMATO SUGERIDO PELO HAIKU: {m.formato_sugerido}\n"
        f"JUSTIFICATIVA HAIKU: {m.justificativa}\n"
        f"SCORE_EDITORIAL: {m.score_editorial}/10\n"
        f"SCORE_FONTE: {m.score_fonte}/25\n"
    )
    resp = client.messages.create(
        model=SONNET_MODEL,
        max_tokens=4000,  # 1500 truncava JSON em ~70% dos casos (stop_reason=max_tokens)
        temperature=0.6,
        system=prompt_system,
        messages=[{"role": "user", "content": user_msg}],
    )
    txt = resp.content[0].text.strip()
    return _safe_json(txt)

# ============================================================
# Guardrail Classifier (fase final, pós-angulação)
# ============================================================

def guardrail_final(client: anthropic.Anthropic, m: MateriaPronta, quota_restante: int, prompt_system: str | None = None) -> dict:
    if prompt_system is None:
        prompt_system = _prompt("04_guardrails_classifier.md")
    user_msg = (
        f"TÍTULO PRODUZIDO: {m.titulo_sultv}\n"
        f"SUBTÍTULO: {m.subtitulo}\n"
        f"LEAD: {m.lead}\n"
        f"ÂNGULO EDITORIAL: {m.angulo_editorial}\n"
        f"TAG PRINCIPAL: {m.tag_principal}\n"
        f"DATA DA MATÉRIA ORIGINAL: {m.publicado_em}\n"
        f"QUOTA DIÁRIA RESTANTE: {quota_restante}/{QUOTA_DIARIA_PUBLICACAO}\n"
    )
    resp = client.messages.create(
        model=HAIKU_MODEL,
        max_tokens=400,
        temperature=0,
        system=prompt_system,
        messages=[
            {"role": "user", "content": user_msg},
            {"role": "assistant", "content": "{"},  # prefill força JSON puro
        ],
    )
    raw = resp.content[0].text.strip()
    # Reanexa o "{" do prefill se não veio na resposta
    if not raw.startswith("{"):
        raw = "{" + raw
    return _safe_json(raw)

# ============================================================
# Filtro de janela temporal (guardrail #6)
# ============================================================

def descarta_se_velho(item: MateriaBruta) -> bool:
    try:
        pub = datetime.fromisoformat(item.publicado_em.replace("Z", "+00:00"))
    except Exception:
        return False
    agora = datetime.now(timezone.utc)
    return (agora - pub) > timedelta(hours=JANELA_NOTICIA_VALIDA)

# ============================================================
# Orquestrador principal
# ============================================================

def rodar_curadoria(
    itens_brutos: list[MateriaBruta],
    base_recente: list[tuple[MateriaBruta, list[float]]],
    hashes_recentes: set[str],
    embed_fn,
    quota_restante: int,
) -> list[MateriaPronta]:
    client = anthropic.Anthropic()
    p1 = load_prompt("01_classificacao_massa.md")
    p2 = load_prompt("02_angulacao_editorial.md")
    p3 = load_prompt("03_dedup_semantico.md")  # apenas referência docstring
    p4 = load_prompt("04_guardrails_classifier.md")

    # 1. Filtro temporal
    fresh = [it for it in itens_brutos if not descarta_se_velho(it)]

    # 2. Dedup hash
    layer1 = dedup_por_hash(fresh, hashes_recentes)

    # 3. Dedup semântico
    def llm_judge(a: MateriaBruta, b: MateriaBruta) -> bool:
        prompt = (
            f"NOTÍCIA A: {a.titulo} | Resumo: {a.resumo[:100]} | Fonte: {a.fonte_nome} | Data: {a.publicado_em}\n"
            f"NOTÍCIA B: {b.titulo} | Resumo: {b.resumo[:100]} | Fonte: {b.fonte_nome} | Data: {b.publicado_em}"
        )
        resp = client.messages.create(
            model=HAIKU_MODEL,
            max_tokens=50,
            temperature=0,
            system=("Você é um classificador binário. Decide se duas notícias falam do MESMO EVENTO real. "
                    "Em dúvida, responda false. Apenas JSON: {\"mesmo_evento\": true|false}"),
            messages=[{"role": "user", "content": prompt}],
        )
        return _safe_json(resp.content[0].text).get("mesmo_evento", False)

    eventos = dedup_semantico(layer1, base_recente, embed_fn, llm_judge)

    # mantém representante (maior score_fonte) por evento
    representantes: list[MateriaBruta] = []
    for grupo in eventos.values():
        rep = max(grupo, key=lambda x: x.score_fonte)
        representantes.append(rep)

    # 4. Curadoria Haiku
    curadas: list[MateriaCurada] = []
    for it in representantes:
        c = curar_haiku(client, it, p1)
        if not c:
            continue
        m = MateriaCurada(
            **asdict(it),
            score_editorial=int(c.get("score_editorial", 0)),
            tag_principal=c.get("tag_principal", "outro"),
            tags_secundarias=c.get("tags_secundarias", []),
            formato_sugerido=c.get("formato_sugerido", "descartar"),
            justificativa=c.get("justificativa", ""),
            alerta_guardrail=bool(c.get("alerta_guardrail", False)),
            guardrail_motivo=c.get("guardrail_motivo", ""),
        )
        m.score_combinado = score_combinado(m.score_fonte, m.score_editorial)
        curadas.append(m)

    # 5. Filtra guardrail Haiku + descarte
    aprovadas = [m for m in curadas if not m.alerta_guardrail and m.formato_sugerido != "descartar"]
    aprovadas.sort(key=lambda m: m.score_combinado, reverse=True)

    # 6. Top N angulação Sonnet
    top = aprovadas[:TOP_N_ANGULACAO]

    prontas: list[MateriaPronta] = []
    for m in top:
        a = angular_sonnet(client, m, p2)
        if not a:
            continue
        mp = MateriaPronta(
            **asdict(m),
            titulo_sultv=a.get("titulo_sultv", m.titulo),
            subtitulo=a.get("subtitulo", ""),
            lead=a.get("lead", ""),
            ganchos_3=a.get("ganchos_3", []),
            angulo_editorial=a.get("angulo_editorial", ""),
            fontes_complementares_sugeridas=a.get("fontes_complementares_sugeridas", []),
            roteiro_short_60s=a.get("roteiro_short_60s", {}),
            lead_materia_longa=a.get("lead_materia_longa", ""),
            post_instagram=a.get("post_instagram", {}),
            card_carrossel=a.get("card_carrossel", {}),
            tag_thumbnail=a.get("tag_thumbnail", ""),
        )
        # 7. Guardrail final
        g = guardrail_final(client, mp, quota_restante, p4)
        mp.decisao_final = g.get("decisao", "BLOQUEAR")
        mp.decisao_motivo = g.get("explicacao_curta", "")
        prontas.append(mp)
        if mp.decisao_final == "PUBLICAR":
            quota_restante = max(0, quota_restante - 1)

    return prontas


if __name__ == "__main__":
    print("Use rodar_curadoria(...) — orquestrador chamado pela skill.")
