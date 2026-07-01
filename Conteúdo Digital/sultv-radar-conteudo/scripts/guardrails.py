"""
guardrails.py — stop-list e classifier de segurança editorial
==============================================================
Camada PRÉ-IA (regex + stop-list). Camada PÓS-IA está no curador.guardrail_final().

As 14 regras estão em references/guardrails_editoriais.md.
Aqui implementamos a primeira filtragem barata: barra termos óbvios antes de gastar token.
"""
from __future__ import annotations
import re

# ============================================================
# Stop-list (ordem importa: específico → genérico)
# ============================================================

STOP_TERMS_HARD = [
    # Política partidária declarada
    r"\bPT\b", r"\bPL\b", r"\bMDB\b", r"\bPSDB\b", r"\bPSOL\b", r"\bPP\b", r"\bPDT\b",
    r"\bRepublicanos\b", r"\bUnião Brasil\b", r"\bPSB\b", r"\bPRTB\b",
    r"\bBolsonaro\b", r"\bLula\b", r"\bMoro\b",
    # Conteúdo religioso/místico
    r"\bhoróscopo\b", r"\bsigno\b", r"\btarô\b", r"\boráculo\b",
    # Crime sem contexto agro/local com identificação grave
    # (não bloqueamos crime regional — tratado pela IA)
]

STOP_TERMS_SOFT = [
    # Marketing puro / publi-disfarçada
    r"compre agora", r"oferta imperdível", r"link na bio", r"clique e ganhe",
    r"código de desconto", r"frete grátis hoje",
]

# Entidades parceiras — qualquer matéria CRÍTICA bate alerta_humano (não bloqueia direto)
PARCEIROS_SENSIVEIS = [
    "canal rural", "sultv", "farsul", "cotrijal", "ccgl", "abmra",
    "ventiur", "anlab", "tecnopuc",
]


def passa_stop_list(texto: str) -> bool:
    """True se o texto passa (não bate em stop-list HARD). False se bate."""
    if not texto:
        return False
    t = texto.lower()
    for pat in STOP_TERMS_HARD:
        if re.search(pat, texto, re.IGNORECASE):
            return False
    return True


def detecta_critica_a_parceiro(texto: str) -> str | None:
    """Devolve nome do parceiro se o texto sugere crítica direta. None se não detecta."""
    t = texto.lower()
    sinais_negativos = ["fraude", "denúncia", "operação", "indiciado", "preso",
                        "irregularidade", "investigação", "esquema", "queda"]
    for parceiro in PARCEIROS_SENSIVEIS:
        if parceiro in t and any(neg in t for neg in sinais_negativos):
            return parceiro
    return None


def detecta_marketing_puro(texto: str) -> bool:
    """True se o texto parece publi-disfarçada."""
    if not texto:
        return False
    return sum(1 for pat in STOP_TERMS_SOFT if re.search(pat, texto, re.IGNORECASE)) >= 2
