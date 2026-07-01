# -*- coding: utf-8 -*-
"""Angulação + redação da pauta 2026-05-27 (Claude na sessão Cowork).
Lê state/aprovadas_2026-05-27.json, aplica decisões editoriais e escreve
state/pauta_2026-05-27.json + state/materias_2026-05-27/<id_hash>.md.
"""
import json, os, unicodedata
from pathlib import Path

DATE = "2026-05-27"
ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"
MAT_DIR = STATE / f"materias_{DATE}"
MAT_DIR.mkdir(parents=True, exist_ok=True)

aprovadas = json.loads((STATE / f"aprovadas_{DATE}.json").read_text(encoding="utf-8"))["aprovadas"]


def _norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return s


# ---------------------------------------------------------------------------
# Angulação dos itens PUBLICAR (keyed por substring do título original)
# ---------------------------------------------------------------------------
ARAMBARE = {
    "titulo_sultv": "Arambaré abre inscrições para cursos gratuitos de qualificação profissional",
    "subtitulo": "Município da Costa Doce aposta em formação de mão de obra local; vagas são limitadas",
    "lead": "A Prefeitura de Arambaré abriu inscrições para uma nova rodada de cursos gratuitos de qualificação profissional, ação que reforça a aposta do município da Costa Doce em formar mão de obra local e ampliar oportunidades de renda.",
    "ganchos_3": [
        "Cidade-núcleo da Costa Doce investe em capital humano",
        "Gratuidade derruba a barreira do custo da capacitação",
        "Qualificação dialoga com turismo, pesca e produção rural locais",
    ],
    "angulo_editorial": "Desenvolvimento econômico de cidade-núcleo: qualificação profissional como política de empregabilidade em município de pequeno porte do Sul do RS.",
    "fontes_complementares_sugeridas": ["Secretaria municipal responsável pelos cursos", "Sistema S (Senac/Senai) regional"],
    "formato_sugerido": "materia_longa",
    "post_instagram": {
        "caption": "Arambaré abriu inscrições para cursos gratuitos de qualificação profissional. Uma chance de capacitação sem custo para quem quer entrar ou voltar ao mercado de trabalho na Costa Doce. Corre que as vagas são limitadas. 👉 Saiba mais no site da SulTV.",
        "hashtags": ["Arambaré", "CostaDoce", "qualificaçãoprofissional", "cursosgratuitos", "SulTV", "RioGrandedoSul"],
    },
    "roteiro_short_60s": {
        "abertura_2s": "Arambaré: curso de graça pra qualificar.",
        "desenvolvimento_45s": "A prefeitura abriu inscrições para cursos gratuitos de qualificação profissional. A ideia é formar mão de obra local e ampliar a renda numa cidade que vive de turismo, pesca e campo. Sem custo, mais gente acessa a formação.",
        "fechamento_8s": "Vagas limitadas — procure a prefeitura.",
        "cta_5s": "Mais detalhes no site da SulTV.",
        "trilha_sugerida": "Instrumental otimista, leve",
    },
    "tag_thumbnail": "EDUCAÇÃO",
    "briefing_visual": {
        "descricao_pt": "Oficina de curso profissionalizante em cidade pequena do litoral sul do RS, adultos aprendendo um ofício, ambiente claro, sem rostos em close",
        "query_en": ["vocational training workshop", "adult professional course", "people learning trade skills classroom"],
        "evitar": ["logos", "texto", "marcas", "rostos identificáveis em primeiro plano"],
        "prompt_ia": "Wide shot of a bright vocational training workshop in a small southern Brazilian coastal town, adults learning practical trade skills, natural light, no faces in close-up, no text, editorial photojournalism style",
    },
    "_md": """### Título ###
Arambaré abre inscrições para cursos gratuitos de qualificação profissional

### Artigo ###
A Prefeitura de Arambaré abriu inscrições para uma nova rodada de cursos gratuitos de qualificação profissional, ação que reforça a aposta do município da Costa Doce em formar mão de obra local e ampliar oportunidades de renda para os moradores. A iniciativa é voltada a jovens e adultos que buscam ingressar ou se recolocar no mercado de trabalho e dialoga diretamente com a vocação econômica de uma cidade que combina turismo de veraneio, pesca artesanal e produção rural às margens da Lagoa dos Patos.

Localizada no Sul do Rio Grande do Sul, Arambaré convive com uma sazonalidade marcada pela alta temporada de verão, quando o fluxo de visitantes pressiona o comércio e os serviços. Programas de qualificação como o agora anunciado tendem a preparar trabalhadores para essas janelas de maior demanda e, ao mesmo tempo, oferecem alternativas de ocupação fora do período de pico.

A gratuidade é o ponto central da proposta. Ao eliminar a barreira do custo, a prefeitura amplia o acesso à formação técnica para quem normalmente não teria como pagar por capacitação. Esse tipo de política costuma ter efeito direto sobre a empregabilidade em municípios de pequeno porte, onde a oferta privada de cursos é limitada.

Os interessados devem procurar a administração municipal para confirmar prazos, vagas disponíveis e a relação completa de cursos ofertados, já que as inscrições têm período definido. A recomendação é não deixar para a última hora, dada a procura habitual por iniciativas gratuitas desse tipo em cidades da região.

A medida se soma a outras ações recentes da gestão local voltadas ao desenvolvimento de Arambaré, que vem buscando equilibrar a infraestrutura turística com investimentos em capital humano, caminho considerado decisivo para a sustentação econômica de longo prazo dos municípios da Costa Doce.

### Legenda sugerida ###
Arambaré abre inscrições para cursos gratuitos de qualificação profissional; as vagas são limitadas. (Foto: ilustrativa)

### Palavras-chave ###
cursos gratuitos Arambaré, qualificação profissional, Costa Doce, emprego, Arambaré RS, capacitação
""",
}

CRISTAL_AVENIDA = {
    "titulo_sultv": "Cristal conclui melhorias na Avenida Passo do Mendonça com limpeza do canteiro central",
    "subtitulo": "Serviços encerram pacote de obras iniciado com a pavimentação da via",
    "lead": "A Prefeitura de Cristal concluiu a etapa final das melhorias na Avenida Passo do Mendonça, com serviços de limpeza e reorganização do canteiro central que encerram o pacote de obras iniciado com a pavimentação da via.",
    "ganchos_3": [
        "Obra estruturante entregue na segunda camada da Costa Doce",
        "Pavimentação somada a paisagismo urbano",
        "Via melhor conservada valoriza imóveis e facilita escoamento",
    ],
    "angulo_editorial": "Qualificação do espaço urbano em município de pequeno porte do Sul do RS; mobilidade e valorização como pauta local de forte repercussão.",
    "fontes_complementares_sugeridas": ["Secretaria municipal de Obras de Cristal"],
    "formato_sugerido": "materia_longa",
    "post_instagram": {
        "caption": "Cristal finalizou as melhorias na Avenida Passo do Mendonça: depois da pavimentação, veio a limpeza e a reorganização do canteiro central. Mais segurança e organização para quem circula pelo centro da cidade. 👉 Leia no site da SulTV.",
        "hashtags": ["Cristal", "CostaDoce", "obras", "pavimentação", "SulTV", "RioGrandedoSul"],
    },
    "roteiro_short_60s": {
        "abertura_2s": "Cristal entrega avenida renovada.",
        "desenvolvimento_45s": "A Avenida Passo do Mendonça recebeu limpeza e reorganização do canteiro central, fechando o pacote que começou com a pavimentação. Em cidade pequena, via boa é mais que trânsito: valoriza imóvel, ajuda o escoamento e dá cara de cuidado ao centro.",
        "fechamento_8s": "Obra concluída no centro de Cristal.",
        "cta_5s": "Detalhes no site da SulTV.",
        "trilha_sugerida": "Instrumental neutro, urbano",
    },
    "tag_thumbnail": "OBRAS",
    "briefing_visual": {
        "descricao_pt": "Avenida pavimentada com canteiro central recém-organizado em cidade pequena do interior do RS, dia ensolarado, sem pessoas identificáveis",
        "query_en": ["newly paved avenue median", "small town street landscaping brazil", "urban road central median"],
        "evitar": ["pessoas com rosto visível", "placas com nomes", "logos", "texto"],
        "prompt_ia": "Wide editorial shot of a freshly paved avenue with a newly landscaped central median in a small interior town in southern Brazil, sunny day, no people, no text, editorial photojournalism style",
    },
    "_md": """### Título ###
Cristal conclui melhorias na Avenida Passo do Mendonça com limpeza do canteiro central

### Artigo ###
A Prefeitura de Cristal concluiu a etapa final das melhorias na Avenida Passo do Mendonça, com serviços de limpeza e reorganização do canteiro central que encerram o pacote de obras iniciado com a pavimentação da via. A intervenção dá acabamento a um dos corredores urbanos do município, situado na segunda camada da região da Costa Doce, no Sul do Rio Grande do Sul.

Segundo a administração municipal, as ações no canteiro central fazem parte da finalização das melhorias após a pavimentação da avenida. Esse tipo de obra costuma combinar duas frentes: a estrutura, com a pavimentação que melhora o tráfego e reduz os custos de manutenção de veículos, e o paisagismo urbano, responsável por organizar o espaço público e transmitir sensação de cuidado à cidade.

Para municípios de pequeno porte como Cristal, intervenções viárias têm peso que vai além da mobilidade. Vias pavimentadas e bem conservadas valorizam os imóveis no entorno, facilitam o escoamento da produção rural e melhoram o acesso a serviços essenciais. A reorganização do canteiro central, em particular, tende a impactar a percepção de quem circula diariamente pela avenida.

A conclusão da obra reforça a agenda de qualificação do espaço urbano que a gestão municipal vem perseguindo. Em cidades da região, a pavimentação de avenidas estruturantes é frequentemente uma das principais demandas da população, e a entrega desse tipo de melhoria costuma ter forte repercussão local.

A expectativa é de que o corredor, agora com pavimentação e paisagismo concluídos, ofereça mais segurança e fluidez ao trânsito, além de contribuir para a organização visual do centro de Cristal.

### Legenda sugerida ###
Cristal finaliza melhorias na Avenida Passo do Mendonça com limpeza e reorganização do canteiro central.

### Palavras-chave ###
Avenida Passo do Mendonça, Cristal RS, pavimentação, obras urbanas, Costa Doce, mobilidade
""",
}

CRISTAL_PONTO = {
    "titulo_sultv": "Cristal terá ponto facultativo nos dias 4 e 5 de junho por causa de Corpus Christi",
    "subtitulo": "Decreto suspende atendimento nas repartições municipais; serviços essenciais seguem em plantão",
    "lead": "A Prefeitura de Cristal estabeleceu, por decreto, ponto facultativo nas repartições municipais nos dias 4 e 5 de junho, em razão do feriado de Corpus Christi.",
    "ganchos_3": [
        "Feriadão prolongado para servidores e moradores",
        "Serviços essenciais seguem em plantão",
        "Resolva demandas presenciais antes do dia 4",
    ],
    "angulo_editorial": "Serviço urbano: informação prática sobre funcionamento dos órgãos públicos de cidade do Sul do RS no feriado de Corpus Christi.",
    "fontes_complementares_sugeridas": ["Decreto municipal de Cristal"],
    "formato_sugerido": "nota_curta",
    "post_instagram": {
        "caption": "Atenção, Cristal: as repartições municipais terão ponto facultativo nos dias 4 e 5 de junho por causa do feriado de Corpus Christi. Serviços essenciais seguem em plantão. Resolva o que for presencial antes do dia 4. 👉 Detalhes no site da SulTV.",
        "hashtags": ["Cristal", "CorpusChristi", "feriado", "serviçopúblico", "SulTV", "CostaDoce"],
    },
    "roteiro_short_60s": {
        "abertura_2s": "Cristal: feriadão de Corpus Christi.",
        "desenvolvimento_45s": "A prefeitura decretou ponto facultativo nos dias 4 e 5 de junho. As repartições municipais fecham, mas os serviços essenciais seguem em plantão. Quem precisa de atendimento presencial deve resolver antes do dia 4.",
        "fechamento_8s": "Fique atento ao funcionamento dos serviços.",
        "cta_5s": "Mais no site da SulTV.",
        "trilha_sugerida": "Instrumental informativo, curto",
    },
    "tag_thumbnail": "SERVIÇO",
    "briefing_visual": {
        "descricao_pt": "Fachada de prédio da prefeitura de cidade pequena do interior do RS em dia tranquilo, rua calma, sem pessoas",
        "query_en": ["small city hall building brazil", "quiet town street holiday", "municipal government building facade"],
        "evitar": ["logos", "texto", "pessoas identificáveis", "símbolos partidários"],
        "prompt_ia": "Editorial wide shot of a small municipal government building facade in a quiet interior town of southern Brazil on a holiday, calm empty street, no people, no text, editorial photojournalism style",
    },
    "_md": """### Título ###
Cristal terá ponto facultativo nos dias 4 e 5 de junho por causa de Corpus Christi

### Artigo ###
A Prefeitura de Cristal estabeleceu, por decreto, ponto facultativo nas repartições municipais nos dias 4 e 5 de junho, em razão do feriado de Corpus Christi. Com a medida, o atendimento ao público nos órgãos da administração municipal ficará suspenso na quinta-feira (4) e na sexta-feira (5), formando um feriado prolongado para servidores e moradores do município, no Sul do Rio Grande do Sul.

Serviços considerados essenciais devem seguir funcionando em regime de plantão, conforme escala definida por cada secretaria. A recomendação à população é resolver demandas que dependam de atendimento presencial antes do dia 4, evitando contratempos durante o período.

O ponto facultativo na sexta-feira, emendado ao feriado de Corpus Christi na quinta, é prática comum entre prefeituras gaúchas e costuma impactar agendamentos, prazos e o expediente do comércio local. Moradores de Cristal devem ficar atentos a eventuais alterações no funcionamento dos serviços públicos durante esses dias.

### Legenda sugerida ###
Repartições de Cristal terão ponto facultativo nos dias 4 e 5 de junho por causa de Corpus Christi.

### Palavras-chave ###
Cristal, ponto facultativo, Corpus Christi, feriado junho, serviços públicos
""",
}

# Mapa: substring no título original -> (decisao, payload_de_angulacao_ou_motivo)
PUBLICAR = {
    "arambare abre inscricoes": ARAMBARE,
    "avenida passo do mendonca": CRISTAL_AVENIDA,
    "ponto facultativo": CRISTAL_PONTO,
}

REBAIXAR = {
    "corsan organiza planos": "Pauta de saneamento ancorada no Vale do Taquari, fora do eixo Sul-RS/Costa Doce; resumo agregado com várias matérias misturadas. Vira nota interna.",
    "fetag-rs e seduc-rs": "Pauta estadual sem âncora Sul-RS; resumo agregado com temas politicamente sensíveis (mobilização, denúncias). Vira nota interna.",
    "saude mental no trabalho": "Norma trabalhista nacional sem âncora regional Sul-RS; classificação de cidade/tag imprecisa.",
    "vacinacao da gripe": "Serviço de saúde de Venâncio Aires, fora do eixo Sul-RS/Costa Doce; tema saúde tratado com cautela.",
    "estatua da liberdade": "Evento promocional de varejo em Garibaldi (Serra Gaúcha), fora do eixo Sul-RS; conteúdo essencialmente publicitário.",
    "operacao do mprs": "Operação policial/MP em Caxias do Sul (Serra), fora do eixo Sul-RS; pauta criminal sensível.",
}

BLOQUEAR = {
    "assistencia social": "Título é cabeçalho de seção do portal, não matéria; conteúdo real (conferência de segurança alimentar) não foi capturado de forma publicável.",
    "fotos do flickr": "Título é cabeçalho de galeria de fotos do site da Farsul, não matéria.",
    "informacoes agropecuarias": "Título é cabeçalho de seção do portal Emater, não matéria.",
    "avisos e alertas em vigor": "Cabeçalho de seção da Defesa Civil; alertas referem-se a Centro/Norte do RS, fora do eixo Sul-RS.",
    "avisos e alertas / dicas": "Cabeçalho de seção duplicado; alertas de granizo em Vales/Norte, fora do eixo Sul-RS.",
}


def decide(item):
    t = _norm(item["titulo"])
    for k, payload in PUBLICAR.items():
        if k in t:
            return "PUBLICAR", payload, ""
    for k, motivo in REBAIXAR.items():
        if k in t:
            return "REBAIXAR", None, motivo
    for k, motivo in BLOQUEAR.items():
        if k in t:
            return "BLOQUEAR", None, motivo
    return "REBAIXAR", None, "Item sem ângulo regional claro; rebaixado por padrão."


pauta = []
n_pub = n_reb = n_blo = n_md = 0
for item in aprovadas:
    decisao, payload, motivo = decide(item)
    entry = dict(item)  # carrega campos base
    entry["decisao_final"] = decisao
    if decisao == "PUBLICAR":
        n_pub += 1
        for kk, vv in payload.items():
            if kk == "_md":
                (MAT_DIR / f"{item['id_hash']}.md").write_text(vv, encoding="utf-8")
                n_md += 1
            else:
                entry[kk] = vv
        entry["decisao_motivo"] = "Fato concreto, cidade do Sul-RS, fonte confiável, sem guardrail."
    else:
        entry["decisao_motivo"] = motivo
        if decisao == "REBAIXAR":
            n_reb += 1
        else:
            n_blo += 1
    pauta.append(entry)

# Ordena: PUBLICAR primeiro, depois por score_combinado
ordem = {"PUBLICAR": 0, "ALERTA_HUMANO": 1, "REBAIXAR": 2, "BLOQUEAR": 3}
pauta.sort(key=lambda m: (ordem.get(m["decisao_final"], 9), -m.get("score_combinado", 0)))

import datetime
out = {
    "data": DATE,
    "gerado_em": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "total": len(pauta),
    "pauta": pauta,
}
(STATE / f"pauta_{DATE}.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[angular] pauta escrita: {len(pauta)} itens | PUBLICAR={n_pub} REBAIXAR={n_reb} BLOQUEAR={n_blo} | matérias .md={n_md}")
print(f"[angular] -> {STATE / f'pauta_{DATE}.json'}")
