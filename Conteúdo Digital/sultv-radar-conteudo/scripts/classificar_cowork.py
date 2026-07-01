#!/usr/bin/env python3
"""
classificar_cowork.py — Classificação em massa rule-based.

Encoda a régua editorial SulTV (prompts/01_classificacao_massa.md) +
guardrails (prompts/04_guardrails_classifier.md) em regras determinísticas.
Lê state/candidatos_<date>.json e escreve state/curadas_<date>.json.

Usado pelo fluxo cowork-faz-tudo no lugar da chamada à API Anthropic.
"""
from __future__ import annotations
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ============================================================
# Hierarquia geográfica (Manual de Marca v1.5)
# ============================================================
NUCLEO_1 = {"camaquã", "camaqua", "tapes", "arambaré", "arambare"}
NUCLEO_2 = {"cristal", "chuvisca", "são lourenço do sul", "sao lourenco do sul", "slt", "sls",
            "sentinela do sul", "barra do ribeiro", "guaíba", "guaiba"}
NUCLEO_3 = {"pelotas"}
RS_GERAL = {"rs", "rio grande do sul", "porto alegre", "porto alegre/rs", "poa", "santa maria",
            "caxias", "rio grande", "bento gonçalves", "bento goncalves", "novo hamburgo",
            "são leopoldo", "sao leopoldo", "venâncio aires", "venancio aires", "passo fundo",
            "canoas", "viamão", "viamao", "gramado", "lajeado", "santa cruz do sul",
            "uruguaiana", "santiago", "cruz alta", "santa rosa", "ijuí", "ijui", "carazinho",
            "vale do sinos", "metade sul", "costa doce", "serra gaúcha", "serra gaucha",
            "fronteira-sul", "fronteira oeste", "campanha"}

# ============================================================
# Termos que indicam tragédia/guardrail
# ============================================================
TRAGEDIA_KW = [
    r"\bmort[eo]s?\b", r"\bmorre[mu]?\b", r"\bvítim[ao]s\b", r"\bvitimas?\b",
    r"\bfalec\w*", r"\bóbito", r"\bobito",
    r"\bcadáver", r"\bcadaver", r"\bcorpo\b",
    r"\batropelad[ao]", r"\bsuic[íi]di[ao]",
]
MENORES_KW = [r"\bcrianç[ao]s?\b", r"\bcrianca", r"\bmenor de \d+ anos?\b",
              r"\badolescente", r"\bbeb[êe]s?\b", r"\bestudante de \d+ anos?\b"]
PARTIDARIA_KW = [r"\beleiç", r"\beleicao", r"\bvotaç", r"\bcandidat[oa]s?\b",
                 r"\bpt\b", r"\bpsdb\b", r"\bmdb\b", r"\bpsl\b", r"\bnovo\b",
                 r"\bbolsonari\w*", r"\blul[aism]+", r"\bgovernador\b",
                 r"\bsenador\b", r"\bdeputad[oa]s?\b", r"\bcâmara federal",
                 r"\bcamara federal", r"\bcongresso nacional"]
SAUDE_MEDICA_KW = [r"\bdiagnóstic", r"\bdiagnostic", r"\bprescriç", r"\bprescric",
                   r"\btratamento médico", r"\btratamento medico",
                   r"\bremédio\b", r"\bremedio\b", r"\bmedicament\w+\b"]
RELIGIOSO_KW = [r"\bigreja\b", r"\bcatólic", r"\bcatolic", r"\bevangélic",
                r"\bevangelic", r"\bumband", r"\bcandombl", r"\bmilagre",
                r"\bnossa senhora", r"\bjesus cristo", r"\bsanto\b"]
PARCEIROS_KW = [r"canal rural", r"\bfarsul\b", r"\bcotrijal\b", r"\bccgl\b",
                r"\babmra\b", r"\bventiur\b", r"\banlab\b", r"\btecnopuc\b", r"\bsultv\b"]

# ============================================================
# Tag mapping
# ============================================================
TAG_PATTERNS = [
    ("transito", [r"trânsito", r"transito", r"acidente", r"colis[aã]o", r"engarrafa", r"BR-\d+",
                  r"rodovia", r"rodoviária", r"semáforo", r"semaforo", r"sinaleira"]),
    ("policia", [r"polícia civil", r"policia civil", r"polícia militar", r"policia militar",
                 r"operação policial", r"operacao policial", r"delegacia", r"investigaç",
                 r"prisão\b", r"prisao\b", r"prende[uw]", r"prendido", r"presa"]),
    ("crime", [r"furto", r"roubo", r"assalto", r"narcotráfico", r"narcotrafico",
               r"tráfico", r"trafico\b", r"contrabando", r"facção", r"faccao"]),
    ("seguranca", [r"segurança pública", r"seguranca publica", r"bombeiros", r"brigada militar"]),
    ("clima", [r"clima\b", r"chuva", r"tempestade", r"temporal", r"granizo", r"geada",
               r"seca\b", r"estiagem", r"previs[ãa]o do tempo", r"defesa civil", r"frente fria",
               r"frente quente", r"alagamento", r"enchente", r"inundação", r"inundacao",
               r"vendaval"]),
    ("agro", [r"\bagro\b", r"\bsafra\b", r"\bpec[uú]ária\b", r"\bpecuaria\b",
              r"\bsoja\b", r"\barroz\b", r"\bmilho\b", r"\btrigo\b", r"\bcafé\b",
              r"\bgado\b", r"\bleite\b", r"\bbovin", r"\bsuín", r"\bfrango",
              r"\bcooperativa\b", r"\bemater\b", r"\birga\b", r"\bagricultura\b",
              r"plantio", r"colheita", r"hectare"]),
    ("safra", [r"\bsafra\b", r"plantio", r"colheita", r"produtividade"]),
    ("mercado", [r"cotaç", r"bolsa\b", r"chicago", r"futuros?\b", r"hedge",
                 r"merca\w+ futur", r"commod[íi]ti"]),
    ("politica_local", [r"câmara municipal", r"camara municipal", r"vereador",
                        r"prefeitura", r"prefeito", r"sessão da câmara",
                        r"sessao da camara", r"audiência pública", r"audiencia publica"]),
    ("governo_estadual", [r"governo do estado", r"governo do rs", r"governo gaúcho",
                          r"governo gaucho", r"secretaria estadual", r"palácio piratini",
                          r"palacio piratini"]),
    ("evento", [r"festa\b", r"festival", r"feira\b", r"expo\b", r"semana de",
                r"encontro", r"congresso\b", r"colóquio"]),
    ("cultura", [r"cultura\b", r"teatro", r"museu", r"orquestra", r"cinema",
                 r"livro\b", r"literário", r"artista"]),
    ("esporte", [r"esporte", r"futebol", r"jogo\b", r"campeonato", r"copa\b",
                 r"olímpico", r"olimpico", r"competiç"]),
    ("educacao", [r"educação", r"educacao", r"escola\b", r"universidade",
                  r"ufrgs", r"ufpel", r"unijuí", r"unijui", r"furg"]),
    ("infraestrutura", [r"infraestrutura", r"obra\b", r"ponte\b", r"asfalt",
                        r"saneamento", r"esgoto", r"abastecimento de água"]),
    ("saude", [r"saúde", r"saude", r"hospital", r"sus\b", r"posto de saúde",
               r"posto de saude", r"vacin"]),
    ("servico_urbano", [r"transporte público", r"transporte publico", r"ônibus",
                        r"onibus", r"iluminação pública", r"iluminacao publica",
                        r"coleta de lixo", r"limpeza urbana"]),
    ("economia_local", [r"economia local", r"comércio", r"comercio", r"varejo",
                        r"shopping", r"supermercado"]),
    ("tecnologia", [r"agtech", r"startup", r"inovação", r"inovacao", r"tecnologia",
                    r"inteligência artificial", r"inteligencia artificial", r"IA\b",
                    r"plataforma digital", r"app\b"]),
    ("inovacao", [r"inovação", r"inovacao", r"startup", r"acelera"]),
    ("comunidade", [r"comunidade", r"morador", r"bairro", r"vizinhança"]),
    ("pesquisa", [r"pesquisa", r"estudo\b", r"levantamento", r"sondagem", r"embrapa"]),
    ("cooperativa", [r"cooperativa", r"cooperado"]),
]

GUARDRAIL_VAZIO = [
    "últimas notícias", "ultimas noticias", "mais lidas", "leia mais",
    "ver mais", "veja também", "leia também", "leia mais",
]


def _has(text: str, patterns: list) -> bool:
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False


def _classify_tag(text: str) -> tuple[str, list[str]]:
    """Retorna (tag_principal, tags_secundarias) baseado em padrões."""
    matches = []
    for tag, patterns in TAG_PATTERNS:
        if _has(text, patterns):
            matches.append(tag)
    if not matches:
        return "outro", []
    return matches[0], matches[1:4]


def _classify_cidade_score(cidade: str, texto: str) -> tuple[int, str]:
    """Score baseado em cidade/texto. Retorna (boost, regiao)."""
    c = (cidade or "").lower().strip()
    t = texto.lower()

    def has_loc(loc_set: set) -> bool:
        if c in loc_set:
            return True
        return any(loc in t for loc in loc_set)

    if has_loc(NUCLEO_1):
        return 4, "nucleo_1"
    if has_loc(NUCLEO_2):
        return 3, "nucleo_2"
    if has_loc(NUCLEO_3):
        return 2, "nucleo_3"
    # RS geral
    for token in RS_GERAL:
        if token in t or c == token:
            return 1, "rs"
    # Brasil / Internacional
    if c in {"brasil", "internacional", "eua", "us", "europa"}:
        return -3, "fora"
    return -2, "indef"


def classificar_item(item: dict) -> dict:
    titulo = (item.get("titulo") or "").strip()
    resumo = (item.get("resumo") or "").strip()
    cidade = item.get("cidade", "")
    score_fonte = int(item.get("score_fonte") or 0)
    texto = f"{titulo}\n{resumo}"
    texto_lc = texto.lower()

    # ===== Guardrails primeiro =====
    guardrail = False
    motivo = ""
    # 1. Tragédia com vítima identificada
    tem_tragedia = _has(texto, TRAGEDIA_KW)
    tem_nome_proprio = bool(re.search(r"\b[A-Z][a-zà-ú]+ [A-Z][a-zà-ú]+\b", texto))
    if tem_tragedia and (tem_nome_proprio or _has(texto, MENORES_KW) or
                        re.search(r"\b\d+ ano[s]?\b", texto)):
        guardrail = True
        motivo = "Tragédia com vítima identificada"
    # Menores envolvidos
    if _has(texto, MENORES_KW) and tem_tragedia:
        guardrail = True
        motivo = "Tragédia envolvendo menor"
    # Política partidária
    if _has(texto, PARTIDARIA_KW):
        guardrail = True
        motivo = motivo or "Política partidária"
    # Saúde médica
    if _has(texto, SAUDE_MEDICA_KW):
        guardrail = True
        motivo = motivo or "Conteúdo médico/saúde"
    # Religioso/místico
    if _has(texto, RELIGIOSO_KW):
        guardrail = True
        motivo = motivo or "Conteúdo religioso/místico"
    # Crítica a parceiros — só se a vibe é negativa
    if _has(texto, PARCEIROS_KW) and re.search(r"crise|escândalo|escandalo|polêmica|polemica|crítica|critica|denúncia|denuncia|alvo de", texto_lc):
        guardrail = True
        motivo = motivo or "Crítica/contexto sensível a parceiro estratégico"
    # Conteúdo institucional vazio
    if titulo.lower().strip() in GUARDRAIL_VAZIO or len(titulo) < 15:
        guardrail = True
        motivo = motivo or "Título genérico/vazio"

    # ===== Score base + boosts =====
    score = 4  # baseline

    # Boost geográfico
    geo_boost, regiao = _classify_cidade_score(cidade, texto)
    score += geo_boost

    # Fato concreto local (verbos + entidade)
    fato_concreto = bool(re.search(
        r"\b(aprov[ouae]|abre|abriu|lança|lancou|lançou|inaugura|conclui|"
        r"realiza|recebe|anuncia|divulga|publica|registra|libera|"
        r"sanciona|institui|cria|amplia|reduz|prorroga|adia)",
        texto_lc
    ))
    if fato_concreto:
        score += 1

    # Fonte de alta confiabilidade
    if score_fonte >= 22:
        score += 1
    elif score_fonte < 18:
        score -= 1

    # Penalização Brasil/Internacional
    if regiao == "fora":
        score = min(score, 3)

    # Mercado/cotação sem âncora regional
    if _has(texto, [r"chicago", r"USDA", r"\bfutur[oa]\b", r"bolsa de chicago"]) and regiao not in ("nucleo_1","nucleo_2","nucleo_3","rs"):
        score -= 2

    # Bloqueio guardrail rebaixa pra 1
    if guardrail:
        score = 1

    # Clamp
    score = max(1, min(10, score))

    # Tag
    tag_p, tags_s = _classify_tag(texto)

    # Format mapping
    if guardrail or score <= 3:
        formato = "descartar"
    elif score >= 9:
        formato = "materia_longa"
    elif score >= 7:
        if tag_p in {"transito", "acidente", "saude", "servico_urbano", "clima"}:
            formato = "nota_curta"
        elif tag_p in {"esporte", "cultura", "educacao"}:
            formato = "nota_curta"
        else:
            formato = "materia_longa"
    elif score >= 4:
        formato = "post_instagram"
    else:
        formato = "descartar"

    # Justificativa curta
    if guardrail:
        just = motivo[:80]
    elif regiao == "nucleo_1":
        just = "Fato em cidade-núcleo (Camaquã/Tapes/Arambaré)"
    elif regiao == "nucleo_2":
        just = "Fato na segunda camada Sul-RS"
    elif regiao == "nucleo_3":
        just = "Fato em Pelotas — Costa Doce ampliada"
    elif regiao == "rs":
        just = "Fato em outra cidade RS — ângulo regional"
    elif regiao == "fora":
        just = "Conteúdo nacional/internacional sem âncora regional"
    else:
        just = "Pertinência regional indeterminada"

    score_combinado = round(score_fonte * 0.4 + score * 0.6, 2)

    return {
        **item,
        "score_editorial": score,
        "tag_principal": tag_p,
        "tags_secundarias": tags_s,
        "formato_sugerido": formato,
        "justificativa": just,
        "alerta_guardrail": guardrail,
        "guardrail_motivo": motivo,
        "score_combinado": score_combinado,
    }


def main():
    hoje = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    in_path = ROOT / "state" / f"candidatos_{hoje}.json"
    out_path = ROOT / "state" / f"curadas_{hoje}.json"

    if len(sys.argv) > 1:
        in_path = Path(sys.argv[1])

    payload = json.loads(in_path.read_text(encoding="utf-8"))
    cands = payload.get("candidatos", [])
    print(f"[classificar] {len(cands)} candidatos lidos de {in_path}")

    curadas = [classificar_item(c) for c in cands]

    # Estatísticas
    from collections import Counter
    print(f"[classificar] Distribuição de score editorial:")
    print(Counter(c["score_editorial"] for c in curadas))
    print(f"[classificar] Por formato:")
    print(Counter(c["formato_sugerido"] for c in curadas))
    print(f"[classificar] Guardrails acionados: {sum(1 for c in curadas if c['alerta_guardrail'])}")

    out = {
        "data": hoje,
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "total": len(curadas),
        "curadas": curadas,
    }
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[classificar] -> {out_path}")


if __name__ == "__main__":
    main()
