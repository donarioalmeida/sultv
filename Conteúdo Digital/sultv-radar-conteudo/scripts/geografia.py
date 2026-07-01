"""
geografia.py — boost de score por cidade-alvo + quota de diversidade
=====================================================================
Aplicação direta do Manual de Marca SulTV v1.5 — região de influência oficial
do canal, em ordem de prioridade:
  1. Camaquã (sede)
  2. Tapes
  3. Arambaré
  4. Cristal
  5. Chuvisca
  6. São Lourenço do Sul
  7. Pelotas

Pautas nacionais agro / fontes "Brasil"-"RS" sem ângulo regional recebem
PENALIDADE — a SulTV é afiliada do Canal Rural, mas o foco é regional urbano.

Camada A: boost positivo para as 7 cidades-núcleo
Camada B: penalidade negativa para "brasil"/"rs" sem cidade-núcleo
Camada C: quota máxima de matérias por cidade/dia (default 2)
Camada D: cap de matérias "Brasil"/"RS" no top-20 (default 4)
"""
from __future__ import annotations

# ============================================================
# Cidades-alvo SulTV — hierarquia oficial do Manual de Marca v1.5
# Boost é somado ao score_combinado APÓS o Haiku
# ============================================================
CIDADES_PRIORITARIAS: dict[str, float] = {
    # Núcleo 1 — sede + Costa Doce mais próxima
    "camaquã": 4.0,
    "camaqua": 4.0,
    "tapes": 4.0,
    "arambaré": 4.0,
    "arambare": 4.0,
    # Núcleo 2 — Costa Doce e Sul próximos
    "cristal": 3.0,
    "chuvisca": 3.0,
    "são lourenço do sul": 3.0,
    "sao lourenço do sul": 3.0,
    "são lourenco do sul": 3.0,
    "sao lourenco do sul": 3.0,
    "são lourenço": 3.0,
    "sao lourenço": 3.0,
    "são lourenco": 3.0,
    "sao lourenco": 3.0,
    # Costa Doce / rota da laguna até Porto Alegre (Donário 2026-06-01)
    "sentinela do sul": 3.0,
    "barra do ribeiro": 3.0,
    "guaíba": 2.5,
    "guaiba": 2.5,
    # Núcleo 3 — maior cidade da Metade Sul
    "pelotas": 2.0,
}

# Penalidade para conteúdo "Brasil"-"RS" sem ângulo regional explícito
# (aplicada para frear pautas nacionais agro genéricas)
PENALIDADE_NACIONAL: dict[str, float] = {
    "brasil": -2.0,
    "rs": -1.0,
    "rs interior": -1.0,
    "rs metropolitana": -1.0,
}

# Quota máxima de matérias por cidade/dia (após boost, antes do Sonnet)
QUOTA_POR_CIDADE = 2

# Cap máximo de matérias "Brasil"/"RS" sem cidade-núcleo no funil top-20
# (impede que mercado/agro nacional ocupe a pauta inteira)
CAP_NACIONAL_NO_TOP = 4


def normalizar_cidade(cidade: str) -> str:
    """
    Normaliza a string de cidade que vem do banco_fontes.json.
    Exemplos:
      'Pelotas/RS'           → 'pelotas'
      'Camaquã/Costa Doce'   → 'camaquã'
      'São Lourenço do Sul'  → 'são lourenço do sul'
      'RS'                   → 'rs'  (não-cidade — boost 0)
    """
    if not cidade:
        return ""
    return cidade.lower().split("/")[0].strip()


def boost_cidade(cidade: str) -> float:
    """Retorna o boost (positivo, negativo ou 0) para a cidade.

    - Núcleo SulTV (Camaquã→Pelotas) → boost positivo (2.0 a 4.0)
    - "Brasil" / "RS" sem ângulo → penalidade negativa (-2.0 a -1.0)
    - Resto → 0
    """
    norm = normalizar_cidade(cidade)
    if norm in CIDADES_PRIORITARIAS:
        return CIDADES_PRIORITARIAS[norm]
    if norm in PENALIDADE_NACIONAL:
        return PENALIDADE_NACIONAL[norm]
    return 0.0


def aplicar_boost_geografico(materias: list) -> list:
    """
    Aplica boost (positivo OU negativo) ao score_combinado de cada matéria.
    Mutação in-place + retorna a lista (mesmas instâncias).

    Após o boost, ordena por score_combinado decrescente.
    """
    for m in materias:
        boost = boost_cidade(getattr(m, "cidade", "") or "")
        if boost:
            m.score_combinado = round(m.score_combinado + boost, 2)
    materias.sort(key=lambda m: m.score_combinado, reverse=True)
    return materias


def aplicar_quota_diversidade(
    materias: list,
    max_por_cidade: int = QUOTA_POR_CIDADE,
    cap_nacional: int = CAP_NACIONAL_NO_TOP,
) -> list:
    """
    Filtra a lista mantendo no máximo `max_por_cidade` matérias por cidade-núcleo
    e no máximo `cap_nacional` matérias "Brasil"/"RS" no funil — para impedir que
    pauta nacional agro tome conta do top-20.

    Pressupõe que `materias` já está ordenada por score_combinado decrescente.
    """
    visto: dict[str, int] = {}
    nacional_count = 0
    out = []
    cidades_amplas = ("", "rs", "brasil", "rs interior", "rs metropolitana",
                      "centro-sul", "porto alegre/centro-sul")
    for m in materias:
        cidade = normalizar_cidade(getattr(m, "cidade", "") or "")
        if cidade in cidades_amplas:
            # Cap explícito para conteúdo nacional/RS sem cidade-núcleo
            if nacional_count >= cap_nacional:
                continue
            nacional_count += 1
            out.append(m)
            continue
        usados = visto.get(cidade, 0)
        if usados >= max_por_cidade:
            continue
        visto[cidade] = usados + 1
        out.append(m)
    return out


def relatorio_distribuicao(materias: list) -> dict[str, int]:
    """Para debug/log. Conta matérias por cidade normalizada."""
    out: dict[str, int] = {}
    for m in materias:
        c = normalizar_cidade(getattr(m, "cidade", "") or "") or "(sem cidade)"
        out[c] = out.get(c, 0) + 1
    return dict(sorted(out.items(), key=lambda kv: -kv[1]))


if __name__ == "__main__":
    # Smoke test rápido — pesos calibrados pelo Manual de Marca v1.5
    casos = [
        ("Camaquã/Costa Doce", 4.0),
        ("Tapes", 4.0),
        ("Arambaré", 4.0),
        ("Cristal", 3.0),
        ("Chuvisca", 3.0),
        ("São Lourenço do Sul", 3.0),
        ("Pelotas/RS", 2.0),
        ("Porto Alegre", 0.0),
        ("RS", -1.0),
        ("Brasil", -2.0),
        ("", 0.0),
    ]
    for cidade, esperado in casos:
        b = boost_cidade(cidade)
        ok = "✅" if b == esperado else "❌"
        print(f"{ok} boost_cidade({cidade!r}) = {b} (esperado {esperado})")
