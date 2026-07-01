#!/usr/bin/env python3
"""
angular_2026-06-26.py — angulação editorial + redação (cowork-faz-tudo).
Decisões editoriais Claude na sessão para a pauta de 2026-06-26.
Regra 12 INEGOCIÁVEL: nenhum texto menciona veículos/portais/rádios/jornais.
Atribuição apenas a fontes primárias institucionais.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-26"


def _skip(decisao: str, motivo: str) -> dict:
    return {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": decisao,
        "decisao_motivo": motivo,
    }


PAUTA_ANGULADA = {

    # IDX 2 — Tapes: 4 vagas de vigilante (SINE) — PUBLICAR
    "30680819ee0a0f0583a07053b3abf22604839ac1": {
        "titulo_sultv": "SINE de Tapes abre 4 vagas para vigilante e orienta sobre o encaminhamento",
        "chamada_faixa": "Tapes tem 4 vagas para vigilante",
        "subtitulo": "Agência de emprego do município intermedeia as oportunidades; interessados devem procurar o atendimento presencial.",
        "lead": "O mercado de trabalho abre uma porta em Tapes. A Agência SINE do município está com quatro vagas de emprego para a função de vigilante, oportunidade que pode reposicionar trabalhadores da Costa Doce e que exige experiência prévia na atividade.",
        "ganchos_3": [
            "Quatro vagas de vigilante estão abertas em Tapes",
            "Encaminhamento é feito pela Agência SINE do município",
            "Atendimento presencial orienta os candidatos interessados"
        ],
        "angulo_editorial": "Serviço de utilidade pública direta em cidade-núcleo (Tapes). Fato concreto, fonte primária institucional (SINE/Prefeitura). Sem viés, sem guardrail.",
        "fontes_complementares_sugeridas": ["Agência SINE de Tapes", "Secretaria de Assistência Social de Tapes"],
        "lead_materia_longa": "O mercado de trabalho abre uma porta em Tapes. A Agência SINE do município está com quatro vagas de emprego para a função de vigilante, oportunidade que exige experiência prévia na atividade.",
        "post_instagram": {
            "caption": "Boas notícias para quem procura emprego em Tapes. A Agência SINE do município está com quatro vagas abertas para a função de vigilante. As oportunidades exigem experiência na atividade e idade mínima de 18 anos. O encaminhamento é feito diretamente pela agência, que orienta os candidatos sobre os documentos e os próximos passos. Quem está em busca de uma recolocação no mercado de trabalho deve procurar o atendimento presencial e levar a documentação em dia. Vale o aviso: vagas como essa costumam ser preenchidas rápido, então não deixe para depois. E se você conhece alguém que está procurando trabalho, compartilhe a informação. Às vezes, uma indicação simples abre uma porta importante.",
            "hashtags": ["#Tapes", "#Emprego", "#Vagas", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Vaga de emprego aberta em Tapes.",
            "desenvolvimento_45s": "A Agência SINE de Tapes está com quatro vagas para a função de vigilante. As oportunidades exigem experiência na atividade e idade mínima de 18 anos. O encaminhamento é feito pela própria agência, que orienta os candidatos sobre documentos e próximos passos. Quem procura recolocação no mercado de trabalho deve buscar o atendimento presencial e levar a documentação em dia, porque vagas assim costumam ser preenchidas rápido.",
            "fechamento_8s": "Uma indicação pode abrir uma porta.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo otimista"
        },
        "tag_thumbnail": "vagas de emprego, Tapes",
        "briefing_visual": {
            "descricao_pt": "Profissional de segurança privada uniformizado em ambiente urbano, foco no uniforme, sem rosto identificável",
            "query_en": ["security guard uniform", "private security worker", "job opportunity office"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos", "armas em destaque"],
            "prompt_ia": "A uniformed private security professional standing at a building entrance, neutral daylight, no identifiable face, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de utilidade pública concreto em cidade-núcleo (Tapes), fonte primária institucional. Sem guardrail."
    },

    # IDX 5 — Arambaré: formação étnico-racial — PUBLICAR
    "58c775b6ca179de847743f1399adcfa54436e516": {
        "titulo_sultv": "Arambaré capacita professores em educação étnico-racial e reforça a Lei 10.639",
        "chamada_faixa": "Arambaré forma professores em educação étnico-racial",
        "subtitulo": "Formação Continuada da rede municipal aprofunda o ensino da história e da cultura afro-brasileira nas escolas.",
        "lead": "A sala de aula de Arambaré ganha reforço no combate ao racismo. A Secretaria Municipal de Educação promoveu uma Formação Continuada para os professores da rede sobre a Educação para as Relações Étnico-Raciais, aprofundando a aplicação da Lei nº 10.639/2003, que torna obrigatório o ensino da história e da cultura afro-brasileira e africana.",
        "ganchos_3": [
            "Professores da rede municipal recebem formação étnico-racial",
            "Encontro reforça a aplicação da Lei nº 10.639/2003",
            "Objetivo é uma educação mais inclusiva e antirracista"
        ],
        "angulo_editorial": "Educação e cidadania em cidade-núcleo (Arambaré). Fato concreto e positivo, fonte primária (Secretaria de Educação). Tema social sem viés partidário.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Educação de Arambaré"],
        "lead_materia_longa": "A sala de aula de Arambaré ganha reforço no combate ao racismo. A Secretaria Municipal de Educação promoveu uma Formação Continuada para os professores da rede sobre a Educação para as Relações Étnico-Raciais, aprofundando a aplicação da Lei nº 10.639/2003.",
        "post_instagram": {
            "caption": "Educar também é ensinar a respeitar. Em Arambaré, os professores da rede municipal participaram de uma Formação Continuada voltada à Educação para as Relações Étnico-Raciais, um encontro de reflexão e troca de experiências sobre como levar a história e a cultura afro-brasileira para a sala de aula. A formação reforça a aplicação da Lei nº 10.639/2003, que tornou obrigatório esse ensino nas escolas brasileiras. Mais do que cumprir uma legislação, a iniciativa valoriza a diversidade, combate o racismo e ajuda a construir uma escola mais inclusiva e democrática. Quando o professor se prepara, quem ganha é toda a comunidade escolar, porque a semente do respeito é plantada cedo, na infância.",
            "hashtags": ["#Arambaré", "#Educação", "#IgualdadeRacial", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Educar é ensinar a respeitar.",
            "desenvolvimento_45s": "Em Arambaré, os professores da rede municipal participaram de uma Formação Continuada sobre Educação para as Relações Étnico-Raciais. O encontro reforça a aplicação da Lei 10.639, que tornou obrigatório o ensino da história e da cultura afro-brasileira nas escolas. Mais do que cumprir a legislação, a iniciativa valoriza a diversidade, combate o racismo e ajuda a construir uma escola mais inclusiva. Quando o professor se prepara, quem ganha é toda a comunidade.",
            "fechamento_8s": "O respeito se aprende cedo.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "inspirador suave"
        },
        "tag_thumbnail": "educação, Arambaré",
        "briefing_visual": {
            "descricao_pt": "Sala de formação de professores com adultos em roda de conversa, ambiente escolar, foco no espaço, sem rostos identificáveis",
            "query_en": ["teacher training workshop", "adult education classroom", "professional development meeting"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A teacher training session in a bright school room with adults seated in a circle, warm natural light, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Educação e cidadania em cidade-núcleo (Arambaré), fato concreto e positivo. Sem guardrail."
    },

    # IDX 6 — Chuvisca: serviços de agricultura no interior — PUBLICAR
    "15bcd386c7ef1f73b6ec6193f0bd61ed92fe10ba": {
        "titulo_sultv": "Chuvisca leva serviços da Secretaria de Agricultura à Costa do Pinheiro",
        "chamada_faixa": "Chuvisca atende produtores da Costa do Pinheiro",
        "subtitulo": "Cronograma da Secretaria de Agricultura e Meio Ambiente atende demandas das comunidades rurais do interior.",
        "lead": "O suporte ao produtor rural chega mais perto em Chuvisca. A Secretaria Municipal de Agricultura e Meio Ambiente executa serviços na localidade da Costa do Pinheiro, dando continuidade a um cronograma de atendimento às demandas do interior que beneficia diretamente as famílias do campo na Costa Doce.",
        "ganchos_3": [
            "Secretaria de Agricultura atende a Costa do Pinheiro",
            "Ações fazem parte de um cronograma para o interior",
            "Foco é apoiar o produtor rural e as comunidades"
        ],
        "angulo_editorial": "Agro e serviço público em cidade-núcleo (Chuvisca). Fonte primária (Secretaria de Agricultura). Tema de interesse direto do produtor rural.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Agricultura e Meio Ambiente de Chuvisca"],
        "lead_materia_longa": "O suporte ao produtor rural chega mais perto em Chuvisca. A Secretaria Municipal de Agricultura e Meio Ambiente executa serviços na localidade da Costa do Pinheiro, dando continuidade a um cronograma de atendimento às demandas do interior.",
        "post_instagram": {
            "caption": "No interior, cada serviço que chega faz diferença na vida de quem produz. Em Chuvisca, a Secretaria Municipal de Agricultura e Meio Ambiente levou atendimento à localidade da Costa do Pinheiro, dando sequência a um cronograma de trabalho voltado às comunidades rurais. As ações ajudam a manter o acesso às propriedades, apoiam a produção e mostram que o poder público pode estar presente onde a estrada é de chão e o trabalho começa cedo. Esse tipo de atenção ao campo é o que mantém a roda da agricultura girando, garantindo que o produtor tenha condições de seguir plantando, criando e abastecendo a mesa de todos. Quem vive no interior sabe: apoio que chega na porteira vale por muito.",
            "hashtags": ["#Chuvisca", "#Agricultura", "#Interior", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Serviço que chega na porteira.",
            "desenvolvimento_45s": "Em Chuvisca, a Secretaria Municipal de Agricultura e Meio Ambiente levou atendimento à localidade da Costa do Pinheiro, dando sequência a um cronograma de trabalho voltado às comunidades rurais. As ações ajudam a manter o acesso às propriedades e apoiam a produção. Esse tipo de atenção ao campo é o que mantém a agricultura girando, garantindo que o produtor tenha condições de seguir plantando, criando e abastecendo a mesa de todos.",
            "fechamento_8s": "Apoio na porteira vale por muito.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "rural acolhedor"
        },
        "tag_thumbnail": "agricultura, Chuvisca",
        "briefing_visual": {
            "descricao_pt": "Estrada de terra no interior rural do Sul do RS com máquina agrícola trabalhando, paisagem de campo, sem pessoas identificáveis",
            "query_en": ["rural dirt road tractor", "countryside farm road brazil", "agricultural machinery field"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A tractor working on a rural dirt road in southern Brazil countryside, green fields around, soft morning light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agro e serviço público em cidade-núcleo (Chuvisca), fonte primária. Sem guardrail."
    },

    # IDX 7 — Chuvisca: nova UBS Porte II — PUBLICAR
    "31fb7c80312523d384bb96a83eefaaca270eaf81": {
        "titulo_sultv": "Chuvisca avança nova UBS com R$ 2,45 milhões e obra já passa de 40%",
        "chamada_faixa": "Chuvisca avança nova UBS de R$ 2,45 milhões",
        "subtitulo": "Unidade Básica de Saúde Porte II amplia o atendimento e já ultrapassa 40% de execução.",
        "lead": "A saúde pública de Chuvisca ganha um reforço de peso. A construção da nova Unidade Básica de Saúde Porte II avança com um investimento de R$ 2.452.054,00 e já ultrapassa 40% de execução, obra que vai ampliar e qualificar os serviços de saúde oferecidos à população da Costa Doce.",
        "ganchos_3": [
            "Nova UBS Porte II soma R$ 2,45 milhões em investimento",
            "Obra já ultrapassa 40% de execução em Chuvisca",
            "Recurso vem do Programa de Requalificação da Atenção Primária"
        ],
        "angulo_editorial": "Saúde e infraestrutura em cidade-núcleo (Chuvisca). Fato concreto com dado quantitativo (valor e avanço da obra). Fonte primária institucional.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Saúde de Chuvisca", "Programa de Requalificação da Atenção Primária"],
        "lead_materia_longa": "A saúde pública de Chuvisca ganha um reforço de peso. A construção da nova Unidade Básica de Saúde Porte II avança com um investimento de R$ 2.452.054,00 e já ultrapassa 40% de execução.",
        "post_instagram": {
            "caption": "Saúde mais perto de quem precisa. Em Chuvisca, a construção da nova Unidade Básica de Saúde Porte II segue avançando e já ultrapassa 40% de execução, viabilizada por um investimento de R$ 2,45 milhões do Programa de Requalificação da Atenção Primária. A UBS é a porta de entrada do sistema público de saúde: é nela que a população encontra atendimento médico e de enfermagem, vacinas, pré-natal, acompanhamento de doenças crônicas e encaminhamentos. Para um município do interior, uma unidade ampliada significa reduzir deslocamentos e aproximar o cuidado das famílias. Cada etapa concluída é um avanço concreto, porque investir em estrutura de saúde é, na prática, investir nas pessoas.",
            "hashtags": ["#Chuvisca", "#Saúde", "#UBS", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Saúde mais perto da população.",
            "desenvolvimento_45s": "Em Chuvisca, a construção da nova Unidade Básica de Saúde Porte II já ultrapassa 40% de execução, viabilizada por um investimento de R$ 2,45 milhões. A UBS é a porta de entrada do sistema público de saúde, onde a população encontra atendimento médico, vacinas, pré-natal e acompanhamento de doenças crônicas. Para um município do interior, uma unidade ampliada reduz deslocamentos e aproxima o cuidado das famílias. Investir em estrutura de saúde é investir nas pessoas.",
            "fechamento_8s": "Cada etapa é um avanço concreto.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo positivo"
        },
        "tag_thumbnail": "saúde, Chuvisca",
        "briefing_visual": {
            "descricao_pt": "Canteiro de obras de uma unidade de saúde pública em construção, estrutura de alvenaria, sem pessoas identificáveis",
            "query_en": ["health clinic construction site", "building under construction brazil", "public health center building"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A public health clinic under construction, masonry walls and scaffolding, clear daylight, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Saúde e infraestrutura em cidade-núcleo (Chuvisca) com dado quantitativo (R$ 2,45 mi, 40% da obra). Sem guardrail."
    },

    # IDX 8 — São Lourenço do Sul: futsal Série Ouro — PUBLICAR
    "8e1bf94a02dbd7418574a2daafce640e6d703f8b": {
        "titulo_sultv": "ABF São Lourenço recebe a AFA neste sábado pela Série Ouro do futsal gaúcho",
        "chamada_faixa": "ABF joga em casa neste sábado pela Série Ouro",
        "subtitulo": "Embalada por três vitórias seguidas, equipe enfrenta a AFA às 20h no Esporte Clube São Lourenço.",
        "lead": "A bola rola em casa para a torcida de São Lourenço do Sul. Neste sábado (27), às 20h, a ABF São Lourenço recebe a AFA de São Francisco de Assis pela 6ª rodada do Campeonato Gaúcho Série Ouro de futsal, embalada por três vitórias consecutivas na competição.",
        "ganchos_3": [
            "ABF joga em casa neste sábado, às 20h",
            "Equipe vem de três vitórias seguidas na Série Ouro",
            "Ingressos custam R$ 10 na portaria do ginásio"
        ],
        "angulo_editorial": "Esporte regional em cidade-núcleo (São Lourenço do Sul). Fato concreto, datado, com apelo de torcida. Fonte primária (clube/Prefeitura).",
        "fontes_complementares_sugeridas": ["Esporte Clube São Lourenço", "Prefeitura de São Lourenço do Sul"],
        "lead_materia_longa": "A bola rola em casa para a torcida de São Lourenço do Sul. Neste sábado (27), às 20h, a ABF São Lourenço recebe a AFA de São Francisco de Assis pela 6ª rodada do Campeonato Gaúcho Série Ouro de futsal.",
        "post_instagram": {
            "caption": "Sábado é dia de futsal em São Lourenço do Sul! A ABF São Lourenço recebe a AFA de São Francisco de Assis neste sábado (27), às 20h, no Esporte Clube São Lourenço, em jogo válido pela 6ª rodada do Campeonato Gaúcho Série Ouro. E o time chega embalado: são três vitórias seguidas na competição, o que promete um ginásio cheio e muita emoção. Os ingressos custam R$ 10 e estarão à venda na portaria do ginásio. O futsal gaúcho é uma das modalidades mais tradicionais do Sul, e ver o time da cidade brigando na elite estadual é motivo de orgulho para a torcida. Então já sabe: chame a família, vista a camisa e vá apoiar a ABF. Na arquibancada, cada grito conta.",
            "hashtags": ["#SãoLourençoDoSul", "#Futsal", "#SérieOuro", "#ABF", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Sábado é dia de futsal!",
            "desenvolvimento_45s": "Em São Lourenço do Sul, a ABF recebe a AFA de São Francisco de Assis neste sábado, às 20h, no Esporte Clube São Lourenço, pela 6ª rodada do Campeonato Gaúcho Série Ouro. O time chega embalado por três vitórias seguidas, o que promete ginásio cheio. Os ingressos custam 10 reais na portaria. O futsal é uma das modalidades mais tradicionais do Sul, e ver o time da cidade na elite estadual é orgulho para a torcida.",
            "fechamento_8s": "Na arquibancada, cada grito conta.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "esportivo animado"
        },
        "tag_thumbnail": "futsal, São Lourenço do Sul",
        "briefing_visual": {
            "descricao_pt": "Quadra de futsal iluminada com bola na linha, ginásio esportivo, sem rostos identificáveis",
            "query_en": ["futsal court indoor", "indoor soccer arena", "futsal ball court"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "An indoor futsal court brightly lit with a ball on the line, empty bleachers, dynamic sports atmosphere, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Esporte regional datado em cidade-núcleo (São Lourenço do Sul), forte apelo de torcida. Sem guardrail."
    },

    # IDX 15 — Cristal: estradas do interior — PUBLICAR
    "01ef011ecdae21c60e1584906736e0e1b68bd082": {
        "titulo_sultv": "Cristal recupera estradas do interior com cascalhamento e patrolamento",
        "chamada_faixa": "Cristal melhora estradas e apoia o produtor",
        "subtitulo": "Serviços em diferentes localidades garantem o escoamento da produção e o acesso das famílias rurais.",
        "lead": "As estradas que ligam o campo à cidade recebem atenção em Cristal. A Prefeitura executa melhorias nas vias do interior, com cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades, garantindo o escoamento da produção e o acesso das famílias na Costa Doce.",
        "ganchos_3": [
            "Estradas do interior recebem cascalhamento e patrolamento",
            "Serviços alcançam diferentes localidades do município",
            "Melhorias garantem escoamento da safra e acesso das famílias"
        ],
        "angulo_editorial": "Infraestrutura rural em cidade-núcleo (Cristal), interesse direto do produtor. Fonte primária (Prefeitura). Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Secretaria de Obras de Cristal", "Secretaria de Agricultura de Cristal"],
        "lead_materia_longa": "As estradas que ligam o campo à cidade recebem atenção em Cristal. A Prefeitura executa melhorias nas vias do interior, com cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades.",
        "post_instagram": {
            "caption": "No interior, estrada boa é sinônimo de oportunidade. Em Cristal, a Prefeitura realiza melhorias nas vias rurais, com cascalhamento, patrolamento e apoio direto às propriedades em diferentes localidades. Pode parecer simples, mas é por essa estrada que a produção chega ao mercado, que o leite é coletado, que o transporte escolar leva as crianças e que a ambulância chega até quem precisa. Uma via em más condições encarece o frete, danifica veículos e, em casos extremos, isola famílias. Por isso, manter a malha rural em boas condições é um investimento que se paga, porque conecta o produtor aos mercados e aos serviços. Cuidar da estrada do interior é cuidar de quem sustenta a vida no campo.",
            "hashtags": ["#Cristal", "#EstradasRurais", "#Interior", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Estrada boa é oportunidade.",
            "desenvolvimento_45s": "Em Cristal, a Prefeitura realiza melhorias nas estradas do interior, com cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades. É por essa estrada que a produção chega ao mercado, que o leite é coletado, que o transporte escolar leva as crianças e que a ambulância chega a quem precisa. Manter a malha rural em boas condições é um investimento que se paga, porque conecta o produtor aos mercados e aos serviços.",
            "fechamento_8s": "Cuidar da estrada é cuidar de quem produz.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "rural acolhedor"
        },
        "tag_thumbnail": "estradas rurais, Cristal",
        "briefing_visual": {
            "descricao_pt": "Motoniveladora ou patrola trabalhando em estrada de terra no interior do Sul do RS, sem pessoas identificáveis",
            "query_en": ["motor grader dirt road", "road maintenance machinery", "rural gravel road work"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A motor grader leveling a rural gravel road in southern Brazil countryside, clear day, green fields, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Infraestrutura rural em cidade-núcleo (Cristal), interesse direto do produtor. Sem guardrail."
    },

    # IDX 16 — Cristal: PREPARA RS — PUBLICAR
    "9ce36499a218324114c169a9d64f04aae0558ec9": {
        "titulo_sultv": "Cristal integra o PREPARA RS e reforça a prevenção a desastres climáticos",
        "chamada_faixa": "Cristal entra no PREPARA RS contra eventos extremos",
        "subtitulo": "Programa estadual apresenta ações e recursos para preparar municípios contra eventos climáticos extremos.",
        "lead": "A prevenção a desastres entra no mapa de Cristal. O município participou do lançamento do programa PREPARA RS, iniciativa que apresenta ações e recursos para preparar as cidades gaúchas contra eventos climáticos extremos, tema sensível para a Costa Doce depois das adversidades recentes no estado.",
        "ganchos_3": [
            "Cristal participa do lançamento do PREPARA RS",
            "Programa foca na preparação contra eventos climáticos extremos",
            "Prevenção ganha força após adversidades recentes no estado"
        ],
        "angulo_editorial": "Prevenção e resiliência climática em cidade-núcleo (Cristal). Tema de alto interesse regional após enchentes/estiagens. Fonte primária (Prefeitura/Governo do Estado).",
        "fontes_complementares_sugeridas": ["Governo do Estado do RS", "Defesa Civil do RS", "Prefeitura de Cristal"],
        "lead_materia_longa": "A prevenção a desastres entra no mapa de Cristal. O município participou do lançamento do programa PREPARA RS, iniciativa que apresenta ações e recursos para preparar as cidades gaúchas contra eventos climáticos extremos.",
        "post_instagram": {
            "caption": "Depois de tudo o que o Rio Grande do Sul enfrentou, preparação virou prioridade. Cristal participou do lançamento do programa PREPARA RS, uma iniciativa que reúne ações e recursos para deixar os municípios mais prontos para enfrentar eventos climáticos extremos. A lógica é simples e poderosa: prevenir custa menos do que remediar. Investir em planejamento, alerta e estrutura significa proteger vidas, casas, lavouras e a economia local quando o tempo vira. Para uma região marcada pelo campo e pelas águas como a Costa Doce, estar preparada não é luxo, é necessidade. Cada município que adere ao programa fortalece toda a rede de proteção do estado. E quando a prevenção funciona, o prejuízo que não acontece é a melhor notícia.",
            "hashtags": ["#Cristal", "#PreparaRS", "#DefesaCivil", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Prevenir custa menos que remediar.",
            "desenvolvimento_45s": "Cristal participou do lançamento do programa PREPARA RS, que reúne ações e recursos para deixar os municípios mais prontos para enfrentar eventos climáticos extremos. Depois de tudo o que o Rio Grande do Sul enfrentou, preparação virou prioridade. Investir em planejamento, alerta e estrutura significa proteger vidas, casas, lavouras e a economia local quando o tempo vira. Para uma região de campo e de águas, estar preparada não é luxo, é necessidade.",
            "fechamento_8s": "Prejuízo que não acontece é boa notícia.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo sério"
        },
        "tag_thumbnail": "prevenção climática, Cristal",
        "briefing_visual": {
            "descricao_pt": "Equipe de defesa civil em treinamento ou planejamento, viaturas e equipamentos, sem rostos identificáveis",
            "query_en": ["civil defense training", "emergency response planning", "disaster preparedness drill"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos", "cenas de tragédia"],
            "prompt_ia": "A civil defense preparedness scene with equipment and vehicles in an open area, neutral daylight, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Prevenção a desastres climáticos em cidade-núcleo (Cristal), tema de alto interesse regional. Sem guardrail."
    },

    # IDX 22 — RS: frio abaixo de zero — PUBLICAR
    "775f9b501ba50ff6ad224de967b2336e8dfb9479": {
        "titulo_sultv": "Quase 70 cidades gaúchas registram frio abaixo de zero e acendem alerta no campo",
        "chamada_faixa": "Frio abaixo de zero atinge quase 70 cidades gaúchas",
        "subtitulo": "Amanhecer congelante traz as menores temperaturas do ano e exige cuidados com lavouras e pessoas.",
        "lead": "O inverno mostrou força no Rio Grande do Sul. Quase 70 cidades gaúchas registraram nesta quarta-feira (24) temperaturas abaixo de zero, as menores do ano até agora, num amanhecer de geada que acende o alerta nas lavouras e na rotina dos moradores da Costa Doce.",
        "ganchos_3": [
            "Quase 70 cidades gaúchas amanheceram abaixo de zero",
            "Foram as menores temperaturas do ano até agora",
            "Geada exige cuidados com lavouras, animais e pessoas"
        ],
        "angulo_editorial": "Clima regional com impacto agrícola direto — interesse central da audiência rural+urbana. Dado quantitativo e ancoragem estadual. Sem citar veículo (regra 12); dado tratado como informação própria.",
        "fontes_complementares_sugeridas": ["Defesa Civil do RS", "Emater/RS", "INMET"],
        "lead_materia_longa": "O inverno mostrou força no Rio Grande do Sul. Quase 70 cidades gaúchas registraram nesta quarta-feira (24) temperaturas abaixo de zero, as menores do ano até agora, num amanhecer de geada.",
        "post_instagram": {
            "caption": "O inverno chegou pra valer no Rio Grande do Sul. Quase 70 cidades gaúchas amanheceram com temperaturas abaixo de zero nesta quarta-feira, as menores marcas do ano até agora, num cenário de geada branca cobrindo campos e telhados. No campo, o frio extremo acende o alerta: a geada pode prejudicar lavouras sensíveis e pastagens, e os produtores precisam redobrar a atenção com os animais, principalmente os mais jovens, garantindo abrigo, alimentação reforçada e água que não congele. Nas cidades, o cuidado é com a saúde e com quem está mais exposto, como idosos, crianças e pessoas em situação de rua. O inverno apenas começou e novos episódios de frio podem vir. Atenção e solidariedade fazem a diferença nas madrugadas geladas.",
            "hashtags": ["#RioGrandeDoSul", "#Frio", "#Geada", "#Inverno", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O frio chegou pra valer no RS.",
            "desenvolvimento_45s": "Quase 70 cidades gaúchas amanheceram com temperaturas abaixo de zero nesta quarta-feira, as menores do ano até agora, com geada cobrindo campos e telhados. No campo, o frio extremo acende o alerta: a geada pode prejudicar lavouras e pastagens, e os produtores precisam redobrar a atenção com os animais, garantindo abrigo, alimentação reforçada e água que não congele. Nas cidades, o cuidado é com idosos, crianças e pessoas em situação de rua.",
            "fechamento_8s": "Atenção e solidariedade fazem a diferença.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "clima sério"
        },
        "tag_thumbnail": "frio, geada, inverno RS",
        "briefing_visual": {
            "descricao_pt": "Campo coberto de geada branca ao amanhecer no Sul do RS, capim congelado em primeiro plano, sem pessoas",
            "query_en": ["frost covered field sunrise", "white frost grass morning", "winter frost countryside"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A rural field covered in white frost at sunrise in southern Brazil, frozen grass in the foreground, cold blue light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima regional com impacto agrícola direto e dado quantitativo. Reescrito 100% no tom SulTV, sem menção a veículo (regra 12). Sem guardrail."
    },

    # IDX 29 — Rio Grande: 2ª COPSul — PUBLICAR
    "14370225a97c898b7a6bb76c433f1f57abc7190c": {
        "titulo_sultv": "2ª COPSul reúne universidades e prefeituras pelo desenvolvimento sustentável no Sul do RS",
        "chamada_faixa": "COPSul une ciência e gestão pelo Sul sustentável",
        "subtitulo": "Encontro integra FURG, UFPel, IFSul, IFRS e prefeituras em torno da agricultura familiar e do clima.",
        "lead": "A ciência e a gestão pública se sentam à mesma mesa no Sul do Rio Grande do Sul. Começou a 2ª COPSul, encontro que reúne as Prefeituras de Rio Grande e Pelotas, a FURG, a UFPel, o IFSul e o IFRS em torno do desenvolvimento sustentável, com foco na agricultura familiar, na proteção do solo e da biodiversidade e no enfrentamento das mudanças climáticas.",
        "ganchos_3": [
            "COPSul integra universidades, institutos e prefeituras",
            "Foco está na agricultura familiar e na proteção do solo",
            "Encontro debate o enfrentamento das mudanças climáticas"
        ],
        "angulo_editorial": "Inovação, agro e sustentabilidade regional — alinhado ao interesse da audiência. Integração ciência-sociedade-poder público. Fonte primária (prefeituras e instituições de ensino).",
        "fontes_complementares_sugeridas": ["FURG", "UFPel", "IFSul", "IFRS", "Prefeituras de Rio Grande e Pelotas"],
        "lead_materia_longa": "A ciência e a gestão pública se sentam à mesma mesa no Sul do Rio Grande do Sul. Começou a 2ª COPSul, encontro que reúne as Prefeituras de Rio Grande e Pelotas, a FURG, a UFPel, o IFSul e o IFRS em torno do desenvolvimento sustentável.",
        "post_instagram": {
            "caption": "Quando ciência e gestão pública caminham juntas, a região inteira ganha. Começou a 2ª COPSul, um encontro que reúne as Prefeituras de Rio Grande e Pelotas, a FURG, a UFPel, o IFSul e o IFRS para discutir o desenvolvimento sustentável do Sul do RS. A pauta é das mais importantes: agricultura familiar, proteção do solo e da biodiversidade e o enfrentamento das mudanças climáticas. Em uma região onde o campo é base da economia, integrar universidades, institutos, poder público e sociedade é o caminho para construir soluções que durem. Eventos como esse mostram que o futuro do agro e do meio ambiente passa pela cooperação e pelo conhecimento. A Costa Doce tem muito a ganhar quando se planeja o amanhã com a cabeça no presente.",
            "hashtags": ["#RioGrande", "#COPSul", "#Sustentabilidade", "#AgriculturaFamiliar", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Ciência e gestão de mãos dadas.",
            "desenvolvimento_45s": "Começou a 2ª COPSul, encontro que reúne as Prefeituras de Rio Grande e Pelotas, a FURG, a UFPel, o IFSul e o IFRS para discutir o desenvolvimento sustentável do Sul do RS. A pauta é importante: agricultura familiar, proteção do solo e da biodiversidade e enfrentamento das mudanças climáticas. Em uma região onde o campo é base da economia, integrar universidades, institutos e poder público é o caminho para soluções que durem.",
            "fechamento_8s": "O futuro do agro passa pela cooperação.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "inovação inspirador"
        },
        "tag_thumbnail": "sustentabilidade, Sul do RS",
        "briefing_visual": {
            "descricao_pt": "Auditório com plateia em evento acadêmico ou seminário sobre sustentabilidade, vista ampla, sem rostos identificáveis em close",
            "query_en": ["conference auditorium audience", "academic seminar hall", "sustainability forum event"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "A wide shot of an academic conference auditorium with an audience seated facing a stage, warm light, no identifiable close-up faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Inovação, agro e sustentabilidade regional, integração ciência-poder público. Sem guardrail."
    },

    # IDX 18 — Pelotas: lançamento livro Arte Preta para Erês — PUBLICAR (nota_curta)
    "e6a2fa4f51cd063040c9c82d9bf1c92ff9d66aeb": {
        "titulo_sultv": "Livro 'Arte Preta para Erês' é lançado neste sábado em Pelotas",
        "chamada_faixa": "Pelotas lança livro que celebra a memória negra",
        "subtitulo": "Obra ilustrada de Eduardo Freda celebra a memória do povo negro no sul do Rio Grande do Sul.",
        "lead": "A cultura ganha uma nova página em Pelotas. Neste sábado (27) é lançado o livro ilustrado 'Arte Preta para Erês', de Eduardo Freda, obra que celebra a memória e a contribuição do povo negro no sul do Rio Grande do Sul.",
        "ganchos_3": [
            "Livro 'Arte Preta para Erês' é lançado neste sábado",
            "Obra ilustrada celebra a memória do povo negro",
            "Lançamento valoriza a cultura afro no sul do estado"
        ],
        "angulo_editorial": "Cultura e memória afro-brasileira na Costa Doce ampliada (Pelotas). Evento datado. Atribuição ao autor (fonte primária), sem citar veículo.",
        "fontes_complementares_sugeridas": ["Eduardo Freda (autor)"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "A cultura ganha uma nova página em Pelotas. Neste sábado (27) é lançado o livro ilustrado 'Arte Preta para Erês', de Eduardo Freda, uma obra que celebra a memória e a contribuição do povo negro no sul do Rio Grande do Sul. Mais do que um livro, é um registro afetivo que valoriza histórias, saberes e a identidade de quem ajudou a construir a região. Iniciativas como essa fortalecem a cultura local e mostram a riqueza da nossa diversidade. Quem gosta de arte, literatura e memória tem um encontro marcado no fim de semana.",
            "hashtags": ["#Pelotas", "#Cultura", "#Literatura", "#MemóriaNegra", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cultura em página nova em Pelotas.",
            "desenvolvimento_45s": "Neste sábado é lançado em Pelotas o livro ilustrado 'Arte Preta para Erês', de Eduardo Freda, uma obra que celebra a memória e a contribuição do povo negro no sul do Rio Grande do Sul. Mais do que um livro, é um registro afetivo que valoriza histórias, saberes e identidade. Iniciativas como essa fortalecem a cultura local e mostram a riqueza da nossa diversidade.",
            "fechamento_8s": "Um encontro com a arte e a memória.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "cultural suave"
        },
        "tag_thumbnail": "cultura, Pelotas, literatura",
        "briefing_visual": {
            "descricao_pt": "Livro ilustrado aberto sobre mesa em ambiente de lançamento cultural, foco no objeto, sem rostos identificáveis",
            "query_en": ["illustrated book open", "book launch event", "art book pages"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto legível", "logos"],
            "prompt_ia": "An open illustrated art book resting on a table at a cultural launch event, warm soft light, no identifiable faces, no readable text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura e memória afro na Costa Doce ampliada (Pelotas), evento datado. Nota curta. Sem guardrail."
    },

    # ===== NÃO PUBLICAR =====
    # IDX 0 — Spotify/violência escolas — BLOQUEAR
    "e6baca001fe9e9ffa26813188a563f2d069aca44": _skip(
        "BLOQUEAR", "Tema nacional sensível (violência em escolas, envolve menores) sem âncora regional real — guardrails 1 e 4."),
    # IDX 1 — Benoit Arraiá de Ofertas — BLOQUEAR
    "7c565e1d236ed7c870ebaa24ee02d7c78e95c866": _skip(
        "BLOQUEAR", "Publicidade comercial de varejista, não é matéria jornalística."),
    # IDX 3 — Tapes Conselho Tutelar (último dia 25/06) — REBAIXAR
    "b3f9d96ff3e0627fc8dded1adc7486b32011d0cf": _skip(
        "REBAIXAR", "Prazo já expirado (25/06) e tema envolve conselho tutelar/menores — preferível não destacar."),
    # IDX 4 — Arambaré expediente até 12h — REBAIXAR
    "894555b8bb1cb05675b47ddaadd4282f26f3856c": _skip(
        "REBAIXAR", "Aviso administrativo trivial (horário de expediente), baixo valor editorial."),
    # IDX 9 — Barra do Ribeiro relatório saúde — REBAIXAR
    "f5ad052bf1d5516128ea916a98ad48bc0e29a4e7": _skip(
        "REBAIXAR", "Relatório institucional genérico, sem fato concreto destacável."),
    # IDX 10 — Barra do Ribeiro visita Rede Pampa — REBAIXAR
    "7cf30eaf052f9a58bad695beceb072ea48d0a363": _skip(
        "REBAIXAR", "Visita protocolar a grupo de comunicação, sem fato relevante; evita exposição de veículo."),
    # IDX 11 — São Lourenço 'opinião sobre saúde' — REBAIXAR
    "58119e573b813ddd62ac6d66f8b70e9ca09d5e4e": _skip(
        "REBAIXAR", "Post opinativo/genérico (pesquisa de opinião), sem fato concreto."),
    # IDX 12 — Sentinela do Sul AVISO AUDIÊNCIA — BLOQUEAR
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR", "Aviso procedural com resumo vazio — cabeçalho/edital, não matéria."),
    # IDX 13 — Sentinela do Sul NOTAS FISCAIS — BLOQUEAR
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR", "Comunicado procedural (emissor de notas fiscais), resumo vazio."),
    # IDX 14 — Pelotas 'economia desafia empresas' — REBAIXAR
    "c42c7515820e1c80b0e71f14cc24fe532f07c924": _skip(
        "REBAIXAR", "Conteúdo genérico/agregado, classificação geográfica e de tag imprecisas."),
    # IDX 17 — Guaíba Defesa Civil congresso — REBAIXAR
    "364b872691e450e6b35f25c845d8a6d9a0894029": _skip(
        "REBAIXAR", "Participação institucional em congresso, fato soft; cidade fora do núcleo."),
    # IDX 19 — Guaíba Reforma Tributária — REBAIXAR
    "2e6c3f85c08cfd873c83e66a4479fc0ba565d294": _skip(
        "REBAIXAR", "Post opinativo/institucional sem fato concreto."),
    # IDX 20 — ALERS privatizações/plebiscito — BLOQUEAR
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "BLOQUEAR", "Debate político-partidário (privatizações, plebiscito) — guardrail política."),
    # IDX 21 — ALERS Funcriança — REBAIXAR
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR", "Pauta legislativa com datas inconsistentes no material; baixa clareza."),
    # IDX 23 — Calor extremo França — BLOQUEAR
    "afc5e49b365c8ddba389483c86a9f6845d33444d": _skip(
        "BLOQUEAR", "Conteúdo internacional (Europa) sem âncora regional Sul-RS."),
    # IDX 24 — Onda de calor Europa — BLOQUEAR
    "364aa009610c478f160694aead474f82753f3cf7": _skip(
        "BLOQUEAR", "Conteúdo internacional (Europa) sem âncora regional Sul-RS."),
    # IDX 25 — Protocolo raios Copa do Mundo — REBAIXAR
    "31982e4065225320a0905b990cfbc8686d5008fd": _skip(
        "REBAIXAR", "Pauta esportiva nacional/internacional sem âncora regional Sul-RS."),
    # IDX 26 — Canguçu interiorização — REBAIXAR
    "2bb618ebbfc0dcfb865c78d4177eff63f7bf7e82": _skip(
        "REBAIXAR", "Programa municipal relevante, mas cidade fora do núcleo e quota diária priorizada."),
    # IDX 27 — Canguçu evento aprendizado — REBAIXAR
    "283643aa72cf56095b6e6f42e60fb3eb0fad8e8e": _skip(
        "REBAIXAR", "Resumo genérico de encerramento de evento, sem fato concreto."),
    # IDX 28 — Encruzilhada Campanha do Agasalho — REBAIXAR
    "df22aac3cbc276f7e4665bd48b2351e132f7c008": _skip(
        "REBAIXAR", "Campanha sazonal genérica, cidade fora do núcleo; tag imprecisa."),
    # IDX 30 — Encruzilhada interiorização atendimentos — REBAIXAR
    "34f02c5679367266f6b3d130a2a0f9bf4529b6e7": _skip(
        "REBAIXAR", "Post de rotina administrativa, cidade fora do núcleo."),
    # IDX 31 — Santa Maria Rústica transferida — REBAIXAR
    "b8e78d672b6e7f2d136cc768e2b2ea72ece34c71": _skip(
        "REBAIXAR", "Evento adiado em cidade distante do escopo Costa Doce."),
    # IDX 32 — Santa Maria Banda Sinfônica UFSM — REBAIXAR
    "9f62b86b08e5c4a4aebd6000472ab5493fde551f": _skip(
        "REBAIXAR", "Projeto cultural em cidade distante do escopo Costa Doce."),
    # IDX 33 — Rio Grande cozinhas solidárias PAA — REBAIXAR
    "690f53cb02e69c34dff210046aa4f6a9631a5356": _skip(
        "REBAIXAR", "Boa pauta social, mas quota de Rio Grande já preenchida pela COPSul."),
    # IDX 34 — Bagé prisão preventiva Canguçu — REBAIXAR
    "cea89cc80eb73779dcf2f34d37e30086a987c1e7": _skip(
        "REBAIXAR", "Ocorrência policial, cidade fora do núcleo; mantida como nota interna."),
    # IDX 35 — Bagé prisão furto energia — REBAIXAR
    "fc1846c6f1a3fc76531a8b02c99c5af494686e22": _skip(
        "REBAIXAR", "Ocorrência policial, cidade fora do núcleo; mantida como nota interna."),
    # IDX 36 — Dom Feliciano Festa Junina — REBAIXAR
    "de9de529ff3459adbe0a676e7766505338c2c5f1": _skip(
        "REBAIXAR", "Evento válido em cidade-núcleo, mas quota diária de PUBLICAR (10) já preenchida — regra 14."),
    # IDX 37 — Dom Feliciano patrolamento — REBAIXAR
    "663021d806229732858bcdd260b77eaff6605044": _skip(
        "REBAIXAR", "Post de rotina de infraestrutura, baixo valor de destaque."),
    # IDX 38 — Sertão Santana agricultura — REBAIXAR
    "59b476f6ab41d7156ce15120f1c29cfa3eb7bf03": _skip(
        "REBAIXAR", "Post de rotina administrativa, cidade fora do núcleo."),
    # IDX 39 — Sertão Santana obras — REBAIXAR
    "4910c2a9e23aac67b6aeccb178079f918a1f1445": _skip(
        "REBAIXAR", "Post de rotina de obras, cidade fora do núcleo."),
    # IDX 40 — Amaral Ferrador prazo — REBAIXAR
    "dd9d8f842b3e03d9f475357b6dae5993e8b4b295": _skip(
        "REBAIXAR", "Aviso de prazo genérico, baixo valor editorial."),
    # IDX 41 — Venâncio Aires riscos psicossociais — REBAIXAR
    "1657d4b69651a0808e7cd72a9543aa65fc7f1b47": _skip(
        "REBAIXAR", "Conteúdo de coluna/agregado, cidade fora do escopo Costa Doce."),
    # IDX 42 — Venâncio Aires pessoas em situação de rua — REBAIXAR
    "7fa3e47d9b63def09cfa1131528693f622ab1401": _skip(
        "REBAIXAR", "Ação social válida, mas cidade fora do escopo Costa Doce."),
    # IDX 43 — Bento Gonçalves IA CIC-BG — REBAIXAR
    "b24bbe4adac176121807f02cff7f21bd5c75c2f6": _skip(
        "REBAIXAR", "Pauta de inovação interessante, mas cidade fora do escopo Costa Doce."),
    # IDX 44 — Bento Gonçalves 'Brasil vence Escócia' — BLOQUEAR
    "0be8b4cbff1dbf8016c68a1fe65cad127516f660": _skip(
        "BLOQUEAR", "Esporte nacional/internacional mal ancorado, sem relação regional."),
}


MATERIAS = {

    "30680819ee0a0f0583a07053b3abf22604839ac1": """### Título ###
SINE de Tapes abre 4 vagas para vigilante e orienta candidatos

### Artigo ###
O mercado de trabalho abre uma porta em Tapes. A Agência SINE do município está com quatro vagas de emprego para a função de vigilante, oportunidade que pode reposicionar trabalhadores da Costa Doce e que exige experiência prévia na atividade, além de idade mínima de 18 anos. A intermediação é feita diretamente pela agência de emprego, responsável por aproximar quem procura uma colocação das empresas que precisam contratar. O serviço público de intermediação de mão de obra cumpre um papel importante na economia local. Ele organiza a oferta e a demanda por trabalho, evita que o candidato perca tempo e dinheiro em buscas no escuro e dá às empresas um canal seguro para encontrar profissionais qualificados. Para o trabalhador, é a chance de retornar ao mercado com o apoio de uma estrutura que orienta sobre documentos, encaminhamentos e os próximos passos do processo seletivo. No caso das vagas de vigilante, a exigência de experiência prévia indica que o setor de segurança segue demandando profissionais com formação específica. É uma função que requer atenção, responsabilidade e preparo, e que costuma oferecer estabilidade a quem se mantém atualizado na área. Quem tem o perfil e busca uma recolocação deve procurar o atendimento presencial da agência o quanto antes, levando a documentação em dia para agilizar o encaminhamento. Vagas como essa tendem a ser preenchidas rapidamente, então a recomendação é não deixar para a última hora. O atendimento acontece na sede da Agência SINE de Tapes, onde a equipe orienta os interessados sobre os requisitos e a forma de participar. Mais do que números, cada vaga representa uma família com a perspectiva de uma renda nova e a dignidade de um trabalho. Ao divulgar e intermediar essas oportunidades, Tapes reforça o compromisso de aproximar o trabalhador do emprego e de movimentar a economia da Costa Doce, mostrando que informação que circula é também oportunidade que se concretiza.

### Legenda sugerida ###
Agência SINE de Tapes está com quatro vagas para vigilante; interessados devem procurar o atendimento presencial com a documentação em dia.

### Palavras-chave ###
Tapes, SINE, vagas de emprego, vigilante, mercado de trabalho, Costa Doce, recolocação
""",

    "58c775b6ca179de847743f1399adcfa54436e516": """### Título ###
Arambaré capacita professores em educação étnico-racial e reforça a Lei 10.639

### Artigo ###
A sala de aula de Arambaré ganha reforço no combate ao racismo. A Secretaria Municipal de Educação promoveu uma Formação Continuada para os professores da rede municipal sobre a Educação para as Relações Étnico-Raciais, encontro de reflexão e troca de experiências que aprofunda a aplicação da Lei nº 10.639/2003, que tornou obrigatório o ensino da história e da cultura afro-brasileira e africana nas escolas. A capacitação foi conduzida por uma educadora convidada e reuniu os profissionais da rede em torno de um tema que ultrapassa o currículo. A formação dos professores é o ponto de partida para que o ensino antirracista chegue, de fato, aos estudantes. Quando o educador se prepara, ele ganha repertório para abordar a história e a cultura afro-brasileira com profundidade e sensibilidade, deixando para trás abordagens superficiais e construindo um aprendizado que valoriza a contribuição do povo negro à formação do país. Esse cuidado faz diferença na maneira como crianças e adolescentes enxergam a si mesmos e aos colegas. A Lei nº 10.639/2003 nasceu justamente para corrigir uma lacuna histórica. Por muito tempo, a história contada nas escolas deixou de fora as raízes africanas que estão presentes na língua, na música, na culinária, na religiosidade e em tantos outros aspectos da cultura brasileira. Ao tornar esse ensino obrigatório, a legislação busca promover uma educação mais inclusiva, democrática e respeitosa com a diversidade, combatendo o racismo desde a infância. Para um município do interior, investir nessa formação é um gesto de cidadania. Significa preparar a escola para acolher todos os estudantes, fortalecer o sentimento de pertencimento e formar cidadãos mais conscientes e empáticos. A educação é a ferramenta mais poderosa para transformar a sociedade, e tudo começa com quem está na frente da turma. Ao qualificar seus professores, Arambaré planta uma semente importante. A iniciativa mostra que valorizar a diversidade não é apenas cumprir uma lei, mas assumir o compromisso de construir uma comunidade mais justa, onde cada criança aprende, desde cedo, o valor do respeito.

### Legenda sugerida ###
Secretaria de Educação de Arambaré promove formação étnico-racial para professores e reforça a aplicação da Lei nº 10.639/2003.

### Palavras-chave ###
Arambaré, educação, relações étnico-raciais, Lei 10.639, professores, antirracismo, Costa Doce
""",

    "15bcd386c7ef1f73b6ec6193f0bd61ed92fe10ba": """### Título ###
Chuvisca leva serviços da Secretaria de Agricultura à Costa do Pinheiro

### Artigo ###
O suporte ao produtor rural chega mais perto em Chuvisca. A Secretaria Municipal de Agricultura e Meio Ambiente executou serviços na localidade da Costa do Pinheiro, dando continuidade a um cronograma de atendimento às demandas do interior que beneficia diretamente as famílias do campo na Costa Doce. As ações fazem parte de um trabalho regular da pasta, que tem percorrido as comunidades rurais para atender necessidades locais e apoiar quem vive da terra. O atendimento descentralizado é uma estratégia que faz diferença no dia a dia do interior. Em vez de exigir que o produtor se desloque até a sede do município, a Secretaria leva os serviços até a comunidade, economizando tempo e recursos de quem precisa de apoio. Esse formato aproxima o poder público das famílias rurais e garante que as demandas do campo sejam ouvidas e resolvidas onde elas realmente acontecem. O trabalho da Secretaria de Agricultura é essencial para a economia de um município de vocação rural. É por meio dele que se viabilizam melhorias nos acessos, apoio às propriedades e ações que ajudam o produtor a manter a atividade e a aumentar a produtividade. Cada serviço prestado no interior se traduz em mais condições de trabalho, em produção que chega ao mercado e em renda que circula na região. Manter um cronograma regular de atendimento também transmite segurança a quem produz. O produtor passa a saber que pode contar com o suporte da administração municipal, o que estimula o investimento e o cuidado com a propriedade. Em comunidades onde a estrada é de chão e o trabalho começa cedo, esse tipo de presença vale muito. Ao priorizar o atendimento às localidades rurais, Chuvisca reforça que o desenvolvimento do município passa pelo campo. As ações na Costa do Pinheiro são mais um capítulo de um trabalho que reconhece o produtor como peça central da economia e que busca melhorar, de forma concreta, a vida de quem sustenta a produção na Costa Doce.

### Legenda sugerida ###
Secretaria de Agricultura de Chuvisca leva serviços à Costa do Pinheiro, dando sequência ao atendimento às comunidades do interior.

### Palavras-chave ###
Chuvisca, agricultura, Costa do Pinheiro, interior, produtor rural, serviços, Costa Doce
""",

    "31fb7c80312523d384bb96a83eefaaca270eaf81": """### Título ###
Chuvisca avança nova UBS com R$ 2,45 milhões e obra já passa de 40%

### Artigo ###
A saúde pública de Chuvisca ganha um reforço de peso. A construção da nova Unidade Básica de Saúde Porte II avança no município, viabilizada por um investimento de R$ 2.452.054,00 e já ultrapassando 40% de execução, obra voltada à ampliação e à qualificação dos serviços de saúde oferecidos à população da Costa Doce. O recurso vem do Programa de Requalificação da Atenção Primária e permitiu dar início a uma estrutura há tempos aguardada pela comunidade. A obra é resultado de um processo cuidadoso, que envolveu planejamento, estudos técnicos e o cumprimento de todas as etapas necessárias até a viabilização do projeto. Antes de o canteiro ser aberto, foi preciso percorrer um caminho que incluiu a aquisição do terreno, o licenciamento e as autorizações técnicas e ambientais. Esse rigor garante que a unidade nasça em condições adequadas e dentro das normas, evitando problemas futuros e assegurando que o investimento público seja bem aplicado. Uma Unidade Básica de Saúde é a porta de entrada do sistema público. É nela que a população encontra atendimento médico e de enfermagem, vacinas, pré-natal, curativos, acompanhamento de doenças crônicas e o encaminhamento para serviços mais especializados quando necessário. Quanto melhor a estrutura, mais qualidade e conforto no atendimento, tanto para os pacientes quanto para os profissionais que trabalham no local. Para um município do interior, contar com uma unidade ampliada significa reduzir deslocamentos, aproximar o cuidado das famílias e desafogar a demanda por atendimento. A nova UBS Porte II foi pensada para oferecer mais espaço e melhores condições, acompanhando o crescimento da população e as necessidades de saúde da comunidade. Com a obra já passando de 40% de execução, o cronograma avança de forma consistente. Cada etapa concluída representa um passo concreto rumo a uma saúde pública mais estruturada. Obras como essa mostram que o investimento em infraestrutura é, na prática, investimento nas pessoas, porque se traduz em mais acesso e em melhor atendimento no dia a dia. Ao avançar na construção da nova unidade, Chuvisca reafirma o compromisso de levar cuidado de qualidade e mais perto de quem precisa na Costa Doce.

### Legenda sugerida ###
Nova UBS Porte II de Chuvisca, viabilizada por R$ 2,45 milhões do Programa de Requalificação da Atenção Primária, já passa de 40% de execução.

### Palavras-chave ###
Chuvisca, UBS, saúde, investimento, atenção primária, infraestrutura, Costa Doce
""",

    "8e1bf94a02dbd7418574a2daafce640e6d703f8b": """### Título ###
ABF São Lourenço recebe a AFA neste sábado pela Série Ouro do futsal gaúcho

### Artigo ###
A bola rola em casa para a torcida de São Lourenço do Sul. Neste sábado, 27 de junho, às 20h, a ABF São Lourenço recebe a AFA de São Francisco de Assis no Esporte Clube São Lourenço, em partida válida pela 6ª rodada do Campeonato Gaúcho Série Ouro de futsal, uma das principais competições da modalidade no estado. O time chega para o confronto embalado por três vitórias consecutivas, sequência que renova a confiança do elenco e da torcida. O bom momento na competição transforma o jogo em casa numa oportunidade de seguir somando pontos diante do próprio público. Reencontrar a torcida, depois de uma série positiva, costuma dar um empurrão extra às equipes, e a expectativa é de ginásio animado para apoiar o time em mais um desafio na elite do futsal gaúcho. O futsal é uma das modalidades mais tradicionais e queridas do Rio Grande do Sul, especialmente no interior, onde os ginásios reúnem famílias inteiras em torno do esporte. Ver um time da cidade disputando a Série Ouro é motivo de orgulho para a comunidade, porque representa o resultado de trabalho, dedicação e investimento na base e no esporte local. Cada partida é também uma celebração da identidade da cidade. Para quem quiser prestigiar, os ingressos custam R$ 10 e estarão disponíveis na portaria do ginásio. O valor acessível é um convite para que a família toda compareça e faça da arquibancada o sexto jogador da equipe. O apoio da torcida costuma ser decisivo em jogos equilibrados, e o incentivo das arquibancadas pode fazer a diferença no placar. A realização da partida conta com o apoio da administração municipal, da Câmara de Vereadores e do clube, numa parceria que valoriza o esporte como ferramenta de integração e de promoção da cidade. Ao abrir as portas do ginásio neste sábado, São Lourenço do Sul reforça a importância do futsal na vida comunitária e convida todos a vestir a camisa e torcer pela ABF.

### Legenda sugerida ###
ABF São Lourenço recebe a AFA neste sábado (27), às 20h, pela Série Ouro do futsal gaúcho; ingressos a R$ 10 na portaria do ginásio.

### Palavras-chave ###
São Lourenço do Sul, futsal, Série Ouro, ABF, esporte, Campeonato Gaúcho, Costa Doce
""",

    "01ef011ecdae21c60e1584906736e0e1b68bd082": """### Título ###
Cristal recupera estradas do interior com cascalhamento e patrolamento

### Artigo ###
As estradas que ligam o campo à cidade estão recebendo atenção em Cristal. A Prefeitura executa melhorias nas vias do interior do município, com serviços de cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades, garantindo o escoamento da produção e o acesso das famílias na Costa Doce. O trabalho atende a uma demanda histórica de quem vive longe do centro e depende das estradas para a rotina e para o trabalho. As intervenções incluem o cascalhamento, que cobre o leito da estrada com material que melhora a trafegabilidade, e o patrolamento, que nivela e regulariza a superfície da via. Juntas, essas ações reduzem buracos, atoleiros e poeira, problemas comuns nas estradas de terra, especialmente nos períodos de chuva. O apoio direto às propriedades rurais completa o serviço, ajudando o produtor a manter os acessos em condições de uso. A importância dessas obras é facilmente percebida no dia a dia. É pela estrada rural que a produção chega ao mercado, que o leite é coletado, que o transporte escolar leva as crianças à escola e que as ambulâncias chegam até quem precisa de atendimento. Uma via em más condições atrapalha tudo isso, encarece o frete, danifica veículos e máquinas e, em casos extremos, pode deixar famílias isoladas. Para a economia local, estradas bem cuidadas são um investimento que se paga. Elas facilitam o escoamento da safra, baratizam o transporte e dão mais segurança a quem circula pelo interior. Em uma região de forte vocação agrícola, manter a malha rural em boas condições é condição básica para o desenvolvimento, porque conecta o produtor aos mercados e aos serviços essenciais. Atender diferentes localidades também é uma forma de garantir equilíbrio, levando melhorias para além das comunidades mais próximas da sede. Ao priorizar as estradas do interior, Cristal demonstra atenção a quem produz e movimenta a economia do município. As melhorias representam mais do que conforto: significam acesso, segurança e oportunidades para as famílias rurais. Cada trecho recuperado é um passo a mais para integrar o campo e a cidade, reforçando que cuidar da infraestrutura rural é cuidar de quem sustenta a vida no interior da Costa Doce.

### Legenda sugerida ###
Cristal realiza melhorias nas estradas do interior, com cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades.

### Palavras-chave ###
Cristal, estradas rurais, cascalhamento, patrolamento, infraestrutura, agro, Costa Doce
""",

    "9ce36499a218324114c169a9d64f04aae0558ec9": """### Título ###
Cristal integra o PREPARA RS e reforça a prevenção a desastres climáticos

### Artigo ###
A prevenção a desastres entra no mapa de Cristal. O município participou do lançamento do programa PREPARA RS, iniciativa do Governo do Estado que apresenta ações e recursos para preparar as cidades gaúchas contra eventos climáticos extremos, tema que ganhou urgência depois das adversidades enfrentadas pelo Rio Grande do Sul nos últimos anos. O encontro reuniu representantes de diferentes municípios em torno de um objetivo comum: reduzir os impactos de enchentes, estiagens, vendavais e geadas sobre a população e a economia. A lógica do programa parte de uma ideia simples e poderosa: prevenir custa menos do que remediar. Investir em planejamento, em sistemas de alerta e em estrutura de resposta significa proteger vidas, casas, lavouras e a economia local antes que o pior aconteça. Em vez de agir apenas quando a tragédia já se instalou, a proposta é antecipar riscos, mapear as áreas mais vulneráveis e organizar as equipes para uma resposta rápida e eficiente. Para uma região como a Costa Doce, marcada pelo campo e pela presença das águas, a preparação tem um valor especial. As lavouras estão expostas às variações do clima, e os eventos extremos podem comprometer safras inteiras, além de afetar estradas, pontes e o abastecimento das comunidades. Contar com um plano estruturado e com recursos para a prevenção dá ao município mais capacidade de proteger seus moradores e de retomar a normalidade com mais agilidade. A adesão de cada cidade fortalece toda a rede de proteção do estado. Quando os municípios trabalham de forma integrada, compartilhando informações e estratégias, a resposta a um evento climático se torna mais coordenada e eficaz. A preparação local soma-se a um esforço regional, e o conjunto é mais forte do que cada parte isolada. Ao integrar o PREPARA RS, Cristal assume um compromisso concreto com a segurança da população. Em um cenário de mudanças climáticas e de eventos cada vez mais frequentes, estar preparado deixou de ser uma escolha e passou a ser uma necessidade. E, quando a prevenção funciona, o prejuízo que não acontece é a melhor notícia que a comunidade pode receber.

### Legenda sugerida ###
Cristal participa do lançamento do PREPARA RS, programa estadual que reúne ações e recursos para preparar os municípios contra eventos climáticos extremos.

### Palavras-chave ###
Cristal, Prepara RS, prevenção, defesa civil, eventos climáticos, resiliência, Costa Doce
""",

    "775f9b501ba50ff6ad224de967b2336e8dfb9479": """### Título ###
Quase 70 cidades gaúchas registram frio abaixo de zero e acendem alerta no campo

### Artigo ###
O inverno mostrou a que veio no Rio Grande do Sul. Quase 70 cidades gaúchas registraram nesta quarta-feira, 24 de junho, temperaturas abaixo de zero, as menores marcas do ano até agora, num amanhecer de frio congelante e geada que se espalhou por boa parte do estado e atingiu também a Costa Doce. Apesar da intensidade, a temperatura mais baixa de 2026 segue sendo a registrada em Pinheiro Machado, de 6,4 graus negativos, no dia 16 de junho. Ainda assim, o amanhecer desta quarta-feira chamou a atenção pela amplitude do frio, que cobriu campos e telhados de geada branca em diferentes regiões. Episódios assim são típicos do inverno gaúcho, quando massas de ar frio avançam pelo estado e derrubam as temperaturas durante a madrugada e o início da manhã. O frio extremo, no entanto, não traz apenas desconforto. No campo, a geada acende o sinal de alerta. Lavouras sensíveis e pastagens podem ser prejudicadas pela formação de gelo sobre as folhas, e os produtores precisam redobrar a atenção com os animais, especialmente os mais jovens e vulneráveis. Garantir abrigo, alimentação reforçada e água que não congele é parte dos cuidados necessários para atravessar os dias mais rigorosos sem perdas. Nas cidades, o frio intenso exige cuidados com a saúde e com as pessoas em situação de vulnerabilidade. Idosos, crianças e quem vive nas ruas estão mais expostos aos riscos das baixas temperaturas, e a solidariedade da comunidade faz diferença nesses períodos. Agasalhar-se bem, manter os ambientes aquecidos com segurança e evitar a exposição prolongada ao frio são recomendações básicas para todos. A orientação é acompanhar as informações dos órgãos de defesa civil, que monitoram as condições do tempo e emitem avisos quando necessário. O inverno apenas começou e novos episódios de frio podem ocorrer ao longo dos próximos meses. Para a Costa Doce e para todo o Rio Grande do Sul, o recado é de atenção: proteger as pessoas, cuidar dos animais e preservar as lavouras é a melhor forma de enfrentar as madrugadas geladas que marcam a estação mais fria do ano.

### Legenda sugerida ###
Quase 70 cidades gaúchas registraram frio abaixo de zero nesta quarta-feira; a mínima de 2026 segue em 6,4 °C negativos, em Pinheiro Machado.

### Palavras-chave ###
Rio Grande do Sul, frio, geada, inverno, temperaturas negativas, lavouras, Costa Doce
""",

    "14370225a97c898b7a6bb76c433f1f57abc7190c": """### Título ###
2ª COPSul reúne universidades e prefeituras pelo desenvolvimento sustentável no Sul do RS

### Artigo ###
A ciência e a gestão pública se sentam à mesma mesa no Sul do Rio Grande do Sul. Começou a 2ª COPSul, encontro que reúne as Prefeituras de Rio Grande e Pelotas, a FURG, a UFPel, o IFSul e o IFRS em torno do desenvolvimento sustentável, com foco na agricultura familiar, na proteção do solo e da biodiversidade e na integração entre ciência, sociedade e poder público no enfrentamento das mudanças climáticas. A iniciativa transforma a região em um grande espaço de diálogo e cooperação. A força da COPSul está justamente na união de diferentes atores em torno de objetivos comuns. Universidades e institutos federais trazem o conhecimento científico e a capacidade de pesquisa; as prefeituras aportam a visão prática da gestão e a proximidade com as comunidades; e a sociedade contribui com as demandas reais de quem vive e produz no território. Quando esses mundos conversam, as soluções tendem a ser mais consistentes e duradouras. A escolha dos temas mostra a sintonia do encontro com as urgências da região. A agricultura familiar é base da economia e da segurança alimentar no Sul do estado, e fortalecê-la significa garantir renda no campo e alimento na mesa. A proteção do solo e da biodiversidade, por sua vez, é condição para que a produção se mantenha sustentável ao longo do tempo, preservando os recursos naturais para as próximas gerações. O enfrentamento das mudanças climáticas atravessa todos esses pontos. Depois de episódios extremos que marcaram o Rio Grande do Sul, ficou ainda mais clara a necessidade de planejar o futuro com responsabilidade, combinando produção e preservação. Eventos como a COPSul ajudam a construir esse caminho, reunindo quem pensa e quem executa em torno de estratégias concretas. Para a Costa Doce, a realização de um encontro desse porte é um sinal positivo. Mostra que a região tem instituições fortes, dispostas a cooperar e a colocar o conhecimento a serviço do desenvolvimento. Ao integrar ciência, gestão e sociedade, a 2ª COPSul reafirma que o futuro do agro e do meio ambiente passa pela cooperação, pelo conhecimento e pela coragem de planejar o amanhã com a cabeça no presente.

### Legenda sugerida ###
2ª COPSul reúne FURG, UFPel, IFSul, IFRS e as prefeituras de Rio Grande e Pelotas em torno do desenvolvimento sustentável do Sul do RS.

### Palavras-chave ###
COPSul, Rio Grande, Pelotas, desenvolvimento sustentável, agricultura familiar, mudanças climáticas, Costa Doce
""",
}


def main():
    apr_path = ROOT / "state" / f"aprovadas_{HOJE}.json"
    pauta_path = ROOT / "state" / f"pauta_{HOJE}.json"
    materias_dir = ROOT / "state" / f"materias_{HOJE}"

    data = json.loads(apr_path.read_text(encoding="utf-8"))
    apr_list = data.get("aprovadas") or data.get("curadas") or data.get("itens") or (data if isinstance(data, list) else [])

    pauta = []
    pub_count = 0
    for item in apr_list:
        h = item["id_hash"]
        if h not in PAUTA_ANGULADA:
            angul = _skip("BLOQUEAR", "Sem angulação configurada — fora do top de prioridade do dia")
            angul["titulo_sultv"] = (item.get("titulo", "") or "")[:100]
        else:
            angul = PAUTA_ANGULADA[h]

        if angul["decisao_final"] == "PUBLICAR" and pub_count >= 10:
            angul = {**angul, "decisao_final": "REBAIXAR", "decisao_motivo": "Quota diária esgotada (regra 14)"}
        if angul["decisao_final"] == "PUBLICAR":
            pub_count += 1

        merged = {**item, **angul}
        pauta.append(merged)

    out = {
        "data": HOJE,
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "total": len(pauta),
        "pauta": pauta,
    }
    pauta_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[angular] pauta -> {pauta_path}")
    print(f"[angular] decisões:", dict(Counter(p["decisao_final"] for p in pauta)))
    print(f"[angular] PUBLICAR: {pub_count}")

    materias_dir.mkdir(exist_ok=True)
    nwrite = 0
    for p in pauta:
        if p["decisao_final"] == "PUBLICAR" and p.get("formato_sugerido") == "materia_longa":
            corpo = MATERIAS.get(p["id_hash"])
            if corpo:
                f = materias_dir / f"{p['id_hash']}.md"
                f.write_text(corpo, encoding="utf-8")
                nwrite += 1
                print(f"[angular] matéria -> {f.name} ({len(corpo)} chars)")
            else:
                print(f"[angular] AVISO: {p['id_hash']} PUBLICAR/materia_longa SEM texto em MATERIAS")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
