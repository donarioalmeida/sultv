"""
dedup.py — pipeline de deduplicação em 3 camadas
=================================================
Camada 1: hash SHA1 da URL canônica (rápido, descarta ~30%)
Camada 2: embeddings + cosine similarity (descarta ~50% adicional)
Camada 3: Haiku desempate na zona cinza 0.75-0.85 (~10% adicional)

Em produção, base_recente vem do Sheets (ler_hashes_recentes do sheets_writer).
Embeddings via Voyage AI por padrão (recomendação Anthropic).
"""
from __future__ import annotations
import math
import os
from typing import Iterable

from curador import (
    MateriaBruta, DEDUP_THRESHOLD_HARD, DEDUP_THRESHOLD_LOW,
)

_voyage_client = None
_voyage_disabled_reason = None

_voyage_key = os.getenv("VOYAGE_API_KEY", "").strip()
# Considera key inválida se vazia, placeholder do template, ou muito curta
_VOYAGE_PLACEHOLDERS = ("pa-...", "pa-xxx", "your-key", "")
if not _voyage_key or _voyage_key in _VOYAGE_PLACEHOLDERS or _voyage_key.endswith("...") or len(_voyage_key) < 20:
    _voyage_disabled_reason = "VOYAGE_API_KEY ausente ou placeholder"
else:
    try:
        import voyageai
        _voyage_client = voyageai.Client()
    except ImportError:
        _voyage_disabled_reason = "voyageai não instalado"


def embed_titulos(titulos: list[str]) -> list[list[float]]:
    """Embeddings em batch. Voyage por padrão; fallback gracioso para zeros."""
    if not _voyage_client or not titulos:
        if _voyage_disabled_reason and titulos:
            print(f"[dedup] Voyage desabilitado ({_voyage_disabled_reason}); dedup só por hash de URL")
        return [[0.0] * 1024 for _ in titulos]
    try:
        res = _voyage_client.embed(titulos, model="voyage-3", input_type="document")
        return res.embeddings
    except Exception as e:
        print(f"[dedup] Voyage erro ({type(e).__name__}: {e}); fallback para dedup-só-por-hash")
        return [[0.0] * 1024 for _ in titulos]


def cosine(a: list[float], b: list[float]) -> float:
    if not a or not b:
        return 0.0
    dot = sum(x*y for x, y in zip(a, b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(y*y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def dedup_camada_1(itens: list[MateriaBruta], hashes_recentes: set[str]) -> list[MateriaBruta]:
    visto = set(hashes_recentes)
    out = []
    for it in itens:
        if it.id_hash in visto:
            continue
        visto.add(it.id_hash)
        out.append(it)
    return out


def dedup_camada_2_3(itens: list[MateriaBruta], base_embeddings: list[tuple[str, list[float]]]) -> list[MateriaBruta]:
    """Camada 2 + 3 combinadas. base_embeddings: [(hash_evento, embedding)] das últimas 48h."""
    if not itens:
        return []
    titulos = [it.titulo for it in itens]
    embs = embed_titulos(titulos)

    out = []
    eventos: dict[str, list[MateriaBruta]] = {}
    novos_emb: list[tuple[str, list[float]]] = []

    for it, emb in zip(itens, embs):
        best_id, best_sim = None, 0.0
        for h, eb in base_embeddings + novos_emb:
            sim = cosine(emb, eb)
            if sim > best_sim:
                best_id, best_sim = h, sim

        if best_id is None or best_sim < DEDUP_THRESHOLD_LOW:
            eventos[it.id_hash] = [it]
            novos_emb.append((it.id_hash, emb))
            out.append(it)
        elif best_sim >= DEDUP_THRESHOLD_HARD:
            eventos.setdefault(best_id, []).append(it)
        else:
            # zona cinza — em produção chamar Haiku desempate (omitido neste stub)
            # default conservador: tratar como mesmo evento
            eventos.setdefault(best_id, []).append(it)

    return out


def dedup_pipeline_completo(itens: list[MateriaBruta], hashes_recentes: set[str]) -> list[MateriaBruta]:
    layer1 = dedup_camada_1(itens, hashes_recentes)
    # Em produção: base_embeddings vem do Sheets/Postgres
    return dedup_camada_2_3(layer1, base_embeddings=[])
