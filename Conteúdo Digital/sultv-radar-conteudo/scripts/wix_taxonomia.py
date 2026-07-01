#!/usr/bin/env python3
"""
wix_taxonomia.py — categorias e tags do blog SulTV (Wix Blog v3).

Mantém um mapa hardcoded das 26 categorias existentes em www.sultv.com.br
(coletado em 2026-05-16 via GET /blog/v3/categories) + funções pra mapear
o resultado editorial do Radar (tag_principal + cidade) em `categoryIds[]`,
e helpers pra resolver/criar tags.

Site ID: ab93469c-1450-47a2-876a-ba33b9d2f921
"""
from __future__ import annotations
import os
import re
import requests
from typing import Optional

WIX_API_BASE = "https://www.wixapis.com/blog/v3"

# ============================================================
# Categorias hardcoded (snapshot 2026-05-16)
# ============================================================
# Toda categoria do blog SulTV. Atualizar manualmente quando criar nova
# categoria no painel Wix (ou rodar `python3 scripts/wix_taxonomia.py --sync`).
CATEGORIES: dict[str, str] = {
    "agro":                 "99134766-a541-48d1-9354-0d82956a9cb4",
    "clima":                "897ff1a4-f3ec-4e30-9bc8-59de315fbf73",
    "camaquã":              "b40b508b-e342-4ac2-b2f6-00510e67a1e5",
    "arambaré":             "1444b700-dedb-4d49-8dd3-693e5546ac7e",
    "economia":             "6c5f74c2-0cbe-48d8-989d-84e31cad5b46",
    "tapes":                "12ef55f8-3121-4488-a4e0-6e1b63af6d65",
    "cristal":              "b6fac84e-f8d8-4dad-b8ff-023f0a78f4c6",
    "política":             "aaec403e-8c59-48cd-94f9-6adb4f210659",
    "segurança":            "5d421465-fbf8-41d1-a528-0c71614bec68",
    "chuvisca":             "043edf6d-92e7-4c94-a7b5-167cb8fff5e8",
    "esporte":              "53ea3da8-163a-44a7-82a3-43a9ea53f6e6",
    "são lourenço do sul":  "629d0f3c-b13c-475d-8953-04914a2c87d1",
    "saúde e bem-estar":    "543f024f-ef34-4030-b1c9-dc26d3555bad",
    "dom feliciano":        "41d57a69-257d-4bfb-8a3f-f5d0b7fb31e6",
    "agenda e cultura":     "07ac087b-a8b9-42da-95ad-3370d3d8a35e",
    "educação":             "f6dadb90-a7f8-4e00-9297-65c9c2b76490",
    "trânsito":             "0b2c6a28-8799-488c-857b-98a667301033",
    "vida de ctg":          "74677bcc-09ae-44a9-a037-a450695efffc",
    "internacional":        "0ea7d305-7f22-49cd-9aff-f1bf3e342e7d",
    "inovação":             "c0b8f7f0-dd5e-4455-9195-9b44ff4cefe4",
    "justiça":              "2f8e1058-9d4c-4aae-b01b-ed404447a76e",
    "televisão":            "d0760e8d-4aa7-4fcb-b6df-e203feab526f",
    "tecnologia":           "d12c1ff8-6102-4cce-a0cd-3889ba3e92e2",
    "rio grande do sul":    "423cae08-cf79-45ac-9e70-33c959c8b2b9",
}


# ============================================================
# Mapa: tag_principal editorial → categoria Wix
# ============================================================
TAG_TO_CATEGORY: dict[str, str] = {
    # Trânsito e segurança
    "transito":           "trânsito",
    "acidente":           "trânsito",
    "policia":            "segurança",
    "crime":              "segurança",
    "seguranca":          "segurança",
    # Clima
    "clima":              "clima",
    # Agro
    "agro":               "agro",
    "safra":              "agro",
    "mercado":            "agro",
    "pecuaria":           "agro",
    "cooperativa":        "agro",
    "lavoura":            "agro",
    # Política / governo
    "politica":           "política",
    "politica_local":     "política",
    "governo_estadual":   "política",
    "governo_municipal":  "política",
    "politica_agro":      "política",
    # Comunidade / eventos
    "evento":             "agenda e cultura",
    "cultura":            "agenda e cultura",
    "comunidade":         "agenda e cultura",
    # Esporte
    "esporte":            "esporte",
    # Educação
    "educacao":           "educação",
    # Infraestrutura / serviço urbano
    "infraestrutura":     "economia",      # fallback — pode virar cidade quando houver
    "servico_urbano":     "economia",
    # Saúde
    "saude":              "saúde e bem-estar",
    # Economia
    "economia_local":     "economia",
    # Tecnologia / inovação
    "tecnologia":         "tecnologia",
    "inovacao":           "inovação",
    "pesquisa":           "tecnologia",
    # Justiça
    "justiça":            "justiça",
    "justica":            "justiça",
    # Tradicionalismo
    "tradicionalismo":    "vida de ctg",
    "ctg":                "vida de ctg",
}


# ============================================================
# Mapa: cidade → categoria Wix (cidades-núcleo)
# ============================================================
CIDADE_TO_CATEGORY: dict[str, str] = {
    "camaquã":               "camaquã",
    "camaqua":               "camaquã",
    "tapes":                 "tapes",
    "arambaré":              "arambaré",
    "arambare":              "arambaré",
    "cristal":               "cristal",
    "chuvisca":              "chuvisca",
    "são lourenço do sul":   "são lourenço do sul",
    "sao lourenco do sul":   "são lourenço do sul",
    "dom feliciano":         "dom feliciano",
}


def _norm(s: str) -> str:
    return (s or "").strip().lower()


# ============================================================
# API pública
# ============================================================

def category_id_for_tag(tag_principal: str) -> Optional[str]:
    """Retorna o categoryId da categoria temática que melhor casa com tag_principal.

    Ex.: tag_principal='politica_local' → categoryId de 'política'.
    Retorna None se não houver mapeamento.
    """
    label = TAG_TO_CATEGORY.get(_norm(tag_principal))
    return CATEGORIES.get(label) if label else None


def category_id_for_cidade(cidade: str) -> Optional[str]:
    """Retorna o categoryId da categoria geográfica da cidade (se for cidade-núcleo).

    Cidades fora do mapa (Bento Gonçalves, Venâncio Aires, Pelotas etc.) retornam
    None — recomendado adicionar 'Rio Grande do Sul' nesses casos.
    """
    # Cidade pode vir com sufixo de região (ex.: "Camaquã/Costa Doce", "Santa Maria/RS").
    # Normaliza removendo o que vier após "/" ou " - " antes do lookup do núcleo.
    raw = _norm(cidade)
    base = raw.split("/")[0].split(" - ")[0].strip()
    label = CIDADE_TO_CATEGORY.get(raw) or CIDADE_TO_CATEGORY.get(base)
    return CATEGORIES.get(label) if label else None


def category_id_for_rs() -> str:
    """Atalho para a categoria 'Rio Grande do Sul'."""
    return CATEGORIES["rio grande do sul"]


def categorias_para_materia(tag_principal: str, cidade: str,
                             tags_secundarias: list[str] | None = None) -> list[str]:
    """Decide as categorias da matéria a partir do output do classificador.

    Estratégia:
    - 1 categoria temática (Trânsito, Agro, Política, etc.) baseada em tag_principal
    - 1 categoria geográfica se a cidade for cidade-núcleo
    - Se a cidade NÃO for núcleo e a tag temática for 'agro'/'política'/'segurança',
      adiciona também 'Rio Grande do Sul' como categoria estadual
    - Tags secundárias podem adicionar 1 categoria extra se forem relevantes

    Returns: lista única de categoryIds (até 3 itens).
    """
    out = []

    cat_tag = category_id_for_tag(tag_principal)
    if cat_tag:
        out.append(cat_tag)

    cat_cid = category_id_for_cidade(cidade)
    if cat_cid:
        out.append(cat_cid)
    else:
        # Cidade fora do núcleo + tag temática estadual → adiciona "Rio Grande do Sul"
        if tag_principal in ("agro", "safra", "mercado", "politica", "politica_local",
                              "governo_estadual", "seguranca", "policia"):
            out.append(category_id_for_rs())

    # Tags secundárias úteis
    for ts in (tags_secundarias or []):
        cat_extra = category_id_for_tag(ts)
        if cat_extra and cat_extra not in out:
            out.append(cat_extra)
        if len(out) >= 3:
            break

    # Garantia: toda matéria precisa de pelo menos 1 categoria (regra 9 / _revisar_draft).
    # Se nada casou (tag fora do mapa + cidade fora do núcleo), cai em "Rio Grande do Sul".
    if not out:
        out.append(category_id_for_rs())

    return out


# ============================================================
# Helpers de Tags (criação on-the-fly)
# ============================================================

_TAG_CACHE: dict[str, str] = {}  # label_lower → tagId


def _wix_headers() -> dict:
    token = os.getenv("WIX_SITE_TOKEN", "").strip()
    if not token or token.endswith("...") or len(token) < 30:
        return {}
    h = {"Authorization": token, "Content-Type": "application/json"}
    site_id = os.getenv("WIX_SITE_ID", "").strip()
    if site_id:
        h["wix-site-id"] = site_id
    return h


def _carregar_tags_cache():
    """Lista todas as tags do blog e popula o cache local."""
    if _TAG_CACHE:
        return
    h = _wix_headers()
    if not h:
        return
    try:
        r = requests.get(f"{WIX_API_BASE}/tags", headers=h, timeout=15,
                          params={"paging.limit": 100})
        r.raise_for_status()
        for tag in r.json().get("tags", []):
            _TAG_CACHE[_norm(tag["label"])] = tag["id"]
    except Exception as e:
        print(f"[wix_taxonomia] Falha ao listar tags: {e}")


def _slugify_tag(label: str) -> str:
    s = _norm(label)
    s = re.sub(r"[^a-z0-9à-ú\-\s]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s[:50] or "tag"


def get_or_create_tag(label: str) -> Optional[str]:
    """Retorna tagId existente ou cria uma nova tag com o label. Cacheia."""
    if not label:
        return None
    label = label.strip()
    if not label:
        return None
    if len(label) > 50:
        label = label[:50]

    key = _norm(label)
    if not _TAG_CACHE:
        _carregar_tags_cache()
    if key in _TAG_CACHE:
        return _TAG_CACHE[key]

    h = _wix_headers()
    if not h:
        return None
    # NOTA: a API /blog/v3/tags não aceita wrapper {"tag":{...}} — campos direto na raiz
    body = {"label": label, "slug": _slugify_tag(label), "language": "pt"}
    try:
        r = requests.post(f"{WIX_API_BASE}/tags", headers=h, json=body, timeout=15)
        if r.status_code == 409:
            # Conflict → outro processo criou; revarre cache
            _carregar_tags_cache()
            return _TAG_CACHE.get(key)
        r.raise_for_status()
        tid = r.json()["tag"]["id"]
        _TAG_CACHE[key] = tid
        print(f"[wix_taxonomia] Tag criada: '{label}' → {tid}")
        return tid
    except Exception as e:
        print(f"[wix_taxonomia] Falha ao criar tag '{label}': {e}")
        return None


def tags_ids_para_materia(labels: list[str]) -> list[str]:
    """Resolve uma lista de labels em tagIds, criando os que faltarem.

    Aceita strings duplicadas/normalizadas — devolve uma lista única e ordenada
    de IDs válidos.
    """
    out = []
    vistos = set()
    for lbl in labels:
        if not lbl:
            continue
        lbl_clean = lbl.lstrip("#").strip()
        k = _norm(lbl_clean)
        if k in vistos:
            continue
        vistos.add(k)
        tid = get_or_create_tag(lbl_clean)
        if tid:
            out.append(tid)
    return out


# ============================================================
# Sync utility (atualiza o mapa CATEGORIES rodando contra a API)
# ============================================================

def sync_categorias() -> dict[str, str]:
    """Roda GET /blog/v3/categories e devolve o dict atualizado. Não escreve em disco."""
    h = _wix_headers()
    if not h:
        raise RuntimeError("WIX_SITE_TOKEN ausente — não dá pra sincronizar")
    r = requests.get(f"{WIX_API_BASE}/categories", headers=h, timeout=15)
    r.raise_for_status()
    return {_norm(c["label"]): c["id"] for c in r.json().get("categories", [])}


if __name__ == "__main__":
    import sys, json as _json
    if "--sync" in sys.argv:
        cats = sync_categorias()
        print(_json.dumps(cats, ensure_ascii=False, indent=2))
    else:
        print(f"Categorias bundled: {len(CATEGORIES)}")
        for label, cid in CATEGORIES.items():
            print(f"  {label:<28} → {cid}")
