#!/usr/bin/env python3
"""
angular_2026-06-22.py — angulação editorial + redação (cowork-faz-tudo).
Decisões editoriais Claude na sessão para a pauta de 2026-06-22.
Regra 12 INEGOCIÁVEL: nenhum texto menciona veículos/portais/rádios/jornais.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-22"


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

    # IDX 0 — Festa de São João 2026 movimenta Camaquã (Camaquã, evento) — PUBLICAR
    "1c32d88ed265b7288cb6e7799fbce8666cb0ac3a": {
        "titulo_sultv": "Festa de São João 2026 reúne milhares na Prainha, em Camaquã",
        "chamada_faixa": "São João 2026 lota a Prainha em Camaquã",
        "subtitulo": "Programação no Complexo Poliesportivo Ruy de Castro Netto movimenta o município da Costa Doce e reúne público de toda a região.",
        "lead": "Milhares de pessoas tomaram a Prainha neste fim de semana. A Festa de São João 2026 movimenta Camaquã, na região da Costa Doce, com programação no Complexo Poliesportivo Ruy de Castro Netto e shows que reuniram público de toda a região.",
        "ganchos_3": [
            "Festa de São João 2026 reúne milhares em Camaquã",
            "Programação acontece no Complexo Poliesportivo Ruy de Castro Netto, a Prainha",
            "Evento movimenta o comércio e o turismo da Costa Doce"
        ],
        "angulo_editorial": "Evento cultural de grande porte em cidade-núcleo (Camaquã/Costa Doce). Fato concreto, festa tradicional junina, alto impacto comunitário e econômico. Sem viés partidário. Reenquadrar no tempo correto: a festa movimentou o município no fim de semana e segue na semana de São João.",
        "fontes_complementares_sugeridas": ["Prefeitura de Camaquã", "Secretaria Municipal de Cultura de Camaquã"],
        "lead_materia_longa": "Milhares de pessoas tomaram a Prainha neste fim de semana. A Festa de São João 2026 movimenta Camaquã, na região da Costa Doce, com programação no Complexo Poliesportivo Ruy de Castro Netto.",
        "post_instagram": {
            "caption": "A tradição junina tomou conta de Camaquã. A Festa de São João 2026 reuniu milhares de pessoas na Prainha, o Complexo Poliesportivo Ruy de Castro Netto, com shows, comidas típicas e muita animação. Mais do que uma festa, o evento movimenta o comércio, o turismo e a cultura da Costa Doce, reunindo famílias de toda a região em torno de uma das celebrações mais queridas do calendário gaúcho.",
            "hashtags": ["#Camaquã", "#SãoJoão", "#CostaDoce", "#Cultura", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A tradição junina tomou conta de Camaquã.",
            "desenvolvimento_45s": "A Festa de São João 2026 reuniu milhares de pessoas na Prainha, o Complexo Poliesportivo Ruy de Castro Netto, em Camaquã. Com shows, comidas típicas e muita animação, a celebração movimentou o município da Costa Doce e atraiu público de toda a região. Eventos como esse fortalecem o calendário cultural do interior, aquecem o comércio local e reúnem as famílias em torno de uma das tradições mais queridas do Rio Grande do Sul.",
            "fechamento_8s": "Camaquã vive a maior festa junina da Costa Doce.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "forró instrumental animado"
        },
        "tag_thumbnail": "Festa de São João, Camaquã",
        "briefing_visual": {
            "descricao_pt": "Festa junina à noite com bandeirinhas coloridas, fogueira e barracas iluminadas em praça do interior do Rio Grande do Sul, sem rostos identificáveis",
            "query_en": ["festa junina brazil bunting", "rural night festival lights", "bonfire june festival brazil"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "A lively Brazilian June festival at night with colorful bunting flags, a warm bonfire and illuminated food stalls in a small-town square, festive atmosphere, no recognizable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento cultural de grande porte em cidade-núcleo (Camaquã). Fato concreto, alto impacto comunitário e econômico. Reenquadrado no tempo correto."
    },

    # IDX 1 — duplicata São João Camaquã — REBAIXAR
    "921d03d5295483e8dff2b9b8f163798032d2c349": _skip(
        "REBAIXAR", "Duplicata da Festa de São João de Camaquã (já publicada no item principal)."),

    # IDX 2 — Bandas de Tapes e Sentinela do Sul (Tapes, cultura) — PUBLICAR
    "4d84d73fbe84b729ff39aaf941f9080399410131": {
        "titulo_sultv": "Bandas de Tapes e Sentinela do Sul recebem reconhecimento de maestro campeão mundial",
        "chamada_faixa": "Bandas da Costa Doce ganham reconhecimento",
        "subtitulo": "Corporações musicais dos dois municípios têm o desempenho artístico elogiado pelo maestro campeão mundial Rogério Wanderley Brito.",
        "lead": "O talento musical da Costa Doce ganhou reconhecimento de peso. As bandas municipais de Tapes e Sentinela do Sul, no Sul do Rio Grande do Sul, foram elogiadas pelo desempenho artístico pelo maestro campeão mundial Rogério Wanderley Brito.",
        "ganchos_3": [
            "Bandas de Tapes e Sentinela do Sul são reconhecidas por maestro campeão mundial",
            "Corporações musicais são patrimônio cultural dos municípios",
            "Reconhecimento valoriza a formação musical no interior gaúcho"
        ],
        "angulo_editorial": "Cultura e formação musical em cidade-núcleo (Tapes) e segunda camada (Sentinela do Sul). Fato concreto e positivo (reconhecimento externo). Valoriza talento do interior. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Tapes", "Prefeitura de Sentinela do Sul"],
        "lead_materia_longa": "O talento musical da Costa Doce ganhou reconhecimento de peso. As bandas municipais de Tapes e Sentinela do Sul, no Sul do Rio Grande do Sul, foram elogiadas pelo desempenho artístico pelo maestro campeão mundial Rogério Wanderley Brito.",
        "post_instagram": {
            "caption": "O talento da Costa Doce foi reconhecido bem longe daqui. As bandas municipais de Tapes e Sentinela do Sul tiveram o desempenho artístico elogiado pelo maestro campeão mundial Rogério Wanderley Brito. Mais do que conjuntos musicais, essas corporações são espaços de formação para crianças e jovens, e patrimônio cultural de duas cidades que mantêm viva uma tradição que atravessa gerações.",
            "hashtags": ["#Tapes", "#SentinelaDoSul", "#CostaDoce", "#Cultura", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O talento da Costa Doce foi reconhecido bem longe daqui.",
            "desenvolvimento_45s": "As bandas municipais de Tapes e Sentinela do Sul tiveram o desempenho artístico elogiado pelo maestro campeão mundial Rogério Wanderley Brito. Mais do que conjuntos musicais, essas corporações são espaços de formação para crianças e jovens e patrimônio cultural dos municípios. Manter bandas ativas no interior exige dedicação, e o resultado aparece nas datas cívicas, festas e eventos que reúnem a comunidade em torno da música.",
            "fechamento_8s": "O interior gaúcho mostra a sua força cultural.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "banda marcial instrumental"
        },
        "tag_thumbnail": "Bandas de Tapes e Sentinela do Sul",
        "briefing_visual": {
            "descricao_pt": "Instrumentos de banda marcial (trompete, tuba, tambor) em apresentação ao ar livre no interior, sem rostos identificáveis em primeiro plano",
            "query_en": ["marching band brass instruments", "municipal band performance", "brass band trumpet outdoor"],
            "evitar": ["rostos identificáveis em close", "marcas", "logos", "texto"],
            "prompt_ia": "Brass and percussion instruments of a municipal marching band during an outdoor performance in a small Brazilian town, warm afternoon light, focus on the instruments, no recognizable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura em cidade-núcleo (Tapes) e segunda camada (Sentinela do Sul). Fato concreto e positivo. Sem guardrail."
    },

    # IDX 3 — Cerro Grande do Sul cursos gratuitos (mercado/serviço) — PUBLICAR
    "dd7df59af3392ccb9037aa29aab34324cac79b5c": {
        "titulo_sultv": "Cerro Grande do Sul abre inscrições para cursos gratuitos com bolsa permanência",
        "chamada_faixa": "Cerro Grande do Sul oferece cursos gratuitos",
        "subtitulo": "Dois cursos de qualificação profissional estão com inscrições abertas e oferecem bolsa permanência aos participantes.",
        "lead": "Quem busca qualificação tem uma nova oportunidade na Costa Doce. Cerro Grande do Sul, na região Sul do Rio Grande do Sul, abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes.",
        "ganchos_3": [
            "Cerro Grande do Sul abre inscrições para cursos gratuitos",
            "Cursos oferecem bolsa permanência aos participantes",
            "Qualificação profissional amplia oportunidades na Costa Doce"
        ],
        "angulo_editorial": "Serviço público útil em cidade da Costa Doce. Fato concreto (inscrições abertas, cursos gratuitos, bolsa permanência). Jornalismo de serviço, alto interesse para a audiência regional. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cerro Grande do Sul", "Secretaria Municipal do Trabalho, Cidadania e Assistência Social"],
        "lead_materia_longa": "Quem busca qualificação tem uma nova oportunidade na Costa Doce. Cerro Grande do Sul abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes.",
        "post_instagram": {
            "caption": "Oportunidade de qualificação na Costa Doce. Cerro Grande do Sul está com inscrições abertas para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes. Iniciativas como essa ampliam o acesso à formação, abrem portas no mercado de trabalho e ajudam a fixar talentos na região. Vale a pena ficar de olho no prazo e garantir a vaga.",
            "hashtags": ["#CerroGrandeDoSul", "#CostaDoce", "#Qualificação", "#Emprego", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Oportunidade de qualificação na Costa Doce.",
            "desenvolvimento_45s": "Cerro Grande do Sul abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes. A iniciativa amplia o acesso à formação, abre portas no mercado de trabalho e ajuda a fixar talentos na região. Para quem quer se qualificar sem custo e ainda contar com apoio para permanecer no curso, vale ficar atento ao prazo de inscrição e garantir a vaga.",
            "fechamento_8s": "Qualificação gratuita movimenta o interior gaúcho.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "corporativo otimista leve"
        },
        "tag_thumbnail": "Cursos gratuitos, Cerro Grande do Sul",
        "briefing_visual": {
            "descricao_pt": "Sala de aula ou oficina de qualificação profissional com mesas e materiais de curso, ambiente de aprendizado, sem rostos identificáveis em close",
            "query_en": ["vocational training classroom", "professional course workshop", "adult education hands learning"],
            "evitar": ["rostos identificáveis em close", "marcas", "logos", "texto"],
            "prompt_ia": "A bright vocational training classroom or workshop with tables, tools and learning materials ready for a professional course, hopeful atmosphere, no recognizable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Jornalismo de serviço de alto interesse regional (Costa Doce). Fato concreto (inscrições abertas, bolsa permanência). Sem guardrail."
    },

    # IDX 4 — Arambaré Nota Técnica poda/arborização (politica_local/serviço) — PUBLICAR
    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": {
        "titulo_sultv": "Arambaré publica nota técnica com orientações sobre poda e arborização urbana",
        "chamada_faixa": "Arambaré orienta sobre poda de árvores",
        "subtitulo": "Documento da Diretoria Municipal de Meio Ambiente apresenta diretrizes para o manejo correto da arborização e a poda de árvores no município.",
        "lead": "Arambaré quer árvores mais saudáveis e cidade mais segura. A Prefeitura do município, na orla da Lagoa dos Patos, publicou a Nota Técnica nº 01/2026, com orientações sobre o manejo da arborização urbana e a poda correta de árvores.",
        "ganchos_3": [
            "Arambaré publica nota técnica sobre arborização urbana",
            "Documento orienta o manejo e a poda correta de árvores",
            "Diretrizes buscam segurança e preservação ambiental no município"
        ],
        "angulo_editorial": "Serviço público e meio ambiente em cidade-núcleo (Arambaré). Fato concreto e institucional (nota técnica publicada). Orienta a população sobre conduta correta. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Arambaré", "Diretoria Municipal de Meio Ambiente de Arambaré"],
        "lead_materia_longa": "Arambaré quer árvores mais saudáveis e cidade mais segura. A Prefeitura do município, na orla da Lagoa dos Patos, publicou a Nota Técnica nº 01/2026, com orientações sobre o manejo da arborização urbana e a poda correta de árvores.",
        "post_instagram": {
            "caption": "Árvore bem cuidada é cidade mais segura e mais verde. A Prefeitura de Arambaré publicou uma nota técnica com orientações sobre o manejo da arborização urbana e a poda correta de árvores. O documento ajuda moradores a entenderem como agir, evitando podas inadequadas que prejudicam as plantas e a paisagem. Uma medida simples, que une preservação ambiental e segurança no dia a dia do município.",
            "hashtags": ["#Arambaré", "#MeioAmbiente", "#CostaDoce", "#Arborização", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Árvore bem cuidada é cidade mais segura.",
            "desenvolvimento_45s": "A Prefeitura de Arambaré publicou uma nota técnica com orientações sobre o manejo da arborização urbana e a poda correta de árvores. O documento ajuda os moradores a entenderem como agir, evitando podas inadequadas que prejudicam as plantas e a paisagem. A medida une preservação ambiental e segurança, dois cuidados que fazem diferença no dia a dia de uma cidade que vive à beira da Lagoa dos Patos.",
            "fechamento_8s": "Arambaré aposta no cuidado com o verde urbano.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "acústico tranquilo natureza"
        },
        "tag_thumbnail": "Arborização urbana, Arambaré",
        "briefing_visual": {
            "descricao_pt": "Árvores em rua arborizada de cidade pequena à beira de lago no Rio Grande do Sul, copa verde sob céu claro, sem pessoas",
            "query_en": ["tree lined street small town", "urban tree pruning", "green street trees brazil"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "A peaceful tree-lined street in a small lakeside Brazilian town with healthy green canopies under clear sky, emphasis on urban trees, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público e meio ambiente em cidade-núcleo (Arambaré). Fato concreto e institucional. Sem guardrail."
    },

    # IDX 5 — Arambaré cursos (datado abril/2026) — BLOQUEAR
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "BLOQUEAR", "Conteúdo datado de 16 de abril de 2026 — fora da janela de atualidade do radar diário."),

    # IDX 6 — Edital de penalidade Chuvisca — BLOQUEAR
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR", "Edital procedural (publicação de penalidade) datado de março/2026 — sem valor editorial."),

    # IDX 7 — Edital perímetro urbano Chuvisca — BLOQUEAR
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR", "Edital procedural (abertura de prazo para requerimentos) — formato de aviso oficial, sem valor editorial."),

    # IDX 8 — São Lourenço reunião Sesc/Senac (12 jun, datado) — REBAIXAR
    "4a19f3b447abaaef75271b2e2dbf1a33ae46591b": _skip(
        "REBAIXAR", "Reunião administrativa de alinhamento datada de 12/06 — sem fato novo e fora da janela mais quente."),

    # IDX 9 — Aviso de audiência pública Sentinela — BLOQUEAR
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR", "Título é cabeçalho de aviso oficial (Audiência Pública), procedural e sem corpo informativo."),

    # IDX 10 — Notas fiscais emissor nacional (05/05, datado/procedural) — BLOQUEAR
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR", "Aviso procedural sobre emissão de notas fiscais datado de 05/05 — sem valor editorial."),

    # IDX 11 — Barra do Ribeiro 'Velejaço solidário' (cabeçalho de seção) — BLOQUEAR
    "93d8797025ffe98d7c47bb3b29fd426a9dec54b2": _skip(
        "BLOQUEAR", "Fragmento de cabeçalho de seção da secretaria — título quebrado sem matéria."),

    # IDX 12 — Barra do Ribeiro contracheques (cabeçalho de seção) — BLOQUEAR
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": _skip(
        "BLOQUEAR", "Fragmento de cabeçalho de seção da secretaria — aviso administrativo sem matéria."),

    # IDX 13 — Cristal obras de calçamento Rua Camaquã (serviço) — PUBLICAR
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": {
        "titulo_sultv": "Cristal prepara a Rua Camaquã para receber obras de calçamento",
        "chamada_faixa": "Cristal avança no calçamento da Rua Camaquã",
        "subtitulo": "Serviços de preparação do terreno marcam o início dos trabalhos para a pavimentação de mais uma via do município.",
        "lead": "Mais uma rua de Cristal vai ganhar calçamento. A Prefeitura do município, na região da Costa Doce, iniciou os serviços de preparação da Rua Camaquã para receber as obras de pavimentação.",
        "ganchos_3": [
            "Cristal prepara a Rua Camaquã para obras de calçamento",
            "Serviços de preparação antecedem a pavimentação da via",
            "Investimento melhora a mobilidade e o dia a dia dos moradores"
        ],
        "angulo_editorial": "Infraestrutura e serviço público em cidade-núcleo (Cristal). Fato concreto (preparação para obra de calçamento). Melhoria direta na vida dos moradores. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria Municipal de Obras de Cristal"],
        "lead_materia_longa": "Mais uma rua de Cristal vai ganhar calçamento. A Prefeitura do município, na região da Costa Doce, iniciou os serviços de preparação da Rua Camaquã para receber as obras de pavimentação.",
        "post_instagram": {
            "caption": "Mais infraestrutura para Cristal. A Prefeitura iniciou os serviços de preparação da Rua Camaquã para receber as obras de calçamento. A pavimentação melhora a mobilidade, facilita o acesso dos moradores e valoriza o entorno. Obras assim, que vão chegando bairro a bairro, mostram que o desenvolvimento do interior também se constrói no chão das ruas.",
            "hashtags": ["#Cristal", "#CostaDoce", "#Infraestrutura", "#Obras", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Mais infraestrutura para Cristal.",
            "desenvolvimento_45s": "A Prefeitura de Cristal iniciou os serviços de preparação da Rua Camaquã para receber as obras de calçamento. A pavimentação melhora a mobilidade, facilita o acesso dos moradores e valoriza o entorno. Obras de calçamento que chegam rua a rua mostram que o desenvolvimento do interior também se constrói no chão da cidade, com impacto direto no dia a dia de quem mora por ali.",
            "fechamento_8s": "Cristal segue pavimentando o futuro.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "corporativo otimista leve"
        },
        "tag_thumbnail": "Obras de calçamento, Cristal",
        "briefing_visual": {
            "descricao_pt": "Rua de terra em preparação para calçamento com paralelepípedos empilhados e máquina de obra em cidade do interior, sem rostos identificáveis",
            "query_en": ["cobblestone street paving", "road construction small town", "street pavement work brazil"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "A dirt street being prepared for cobblestone paving with stacked pavers and construction equipment in a small Brazilian town, work in progress, no recognizable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Infraestrutura e serviço público em cidade-núcleo (Cristal). Fato concreto (obra de calçamento). Sem guardrail."
    },

    # IDX 14 — São Lourenço Südoktoberfest lançamento (evento) — PUBLICAR
    "9a0afe0a71110324f476128af3e817babce239d4": {
        "titulo_sultv": "Südoktoberfest abre contagem regressiva com lançamento oficial em São Lourenço do Sul",
        "chamada_faixa": "Südoktoberfest aquece São Lourenço do Sul",
        "subtitulo": "Município da Costa Doce prepara uma das maiores festas de tradição germânica do Sul, com lançamento oficial e concurso da corte.",
        "lead": "A festa germânica mais aguardada da Costa Doce já tem data marcada. São Lourenço do Sul deu início à contagem regressiva para a Südoktoberfest, com lançamento oficial do evento e a abertura do concurso para a escolha da corte.",
        "ganchos_3": [
            "Südoktoberfest abre contagem regressiva em São Lourenço do Sul",
            "Lançamento oficial marca a preparação da festa germânica",
            "Concurso da corte é uma das tradições do evento"
        ],
        "angulo_editorial": "Evento cultural e turístico de tradição germânica em cidade-núcleo (São Lourenço do Sul). Fato concreto (lançamento oficial, concurso da corte). Forte apelo regional e econômico. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Comissão organizadora da Südoktoberfest"],
        "lead_materia_longa": "A festa germânica mais aguardada da Costa Doce já tem data marcada. São Lourenço do Sul deu início à contagem regressiva para a Südoktoberfest, com lançamento oficial do evento e a abertura do concurso para a escolha da corte.",
        "post_instagram": {
            "caption": "A contagem regressiva começou! São Lourenço do Sul deu o pontapé oficial na preparação da Südoktoberfest, uma das maiores festas de tradição germânica do Sul, com lançamento do evento e o concurso da corte. Mais do que música, dança e gastronomia típica, a festa movimenta o turismo, o comércio e celebra a herança cultural que faz parte da identidade da Costa Doce.",
            "hashtags": ["#SãoLourençoDoSul", "#Südoktoberfest", "#CostaDoce", "#Cultura", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A contagem regressiva começou.",
            "desenvolvimento_45s": "São Lourenço do Sul deu o pontapé oficial na preparação da Südoktoberfest, uma das maiores festas de tradição germânica do Sul. O lançamento do evento veio acompanhado do concurso para escolha da corte, um dos rituais mais tradicionais da festa. Com música, dança e gastronomia típica, a Südoktoberfest movimenta o turismo e o comércio e celebra a herança cultural que faz parte da identidade da Costa Doce.",
            "fechamento_8s": "São Lourenço se prepara para a sua maior festa.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "música germânica festiva"
        },
        "tag_thumbnail": "Südoktoberfest, São Lourenço do Sul",
        "briefing_visual": {
            "descricao_pt": "Festa de tradição germânica com canecas de chope, decoração azul e branca e ambiente festivo, sem rostos identificáveis em close",
            "query_en": ["oktoberfest beer steins decoration", "german festival celebration", "bavarian festival blue white"],
            "evitar": ["rostos identificáveis em close", "marcas comerciais de cerveja", "logos", "texto"],
            "prompt_ia": "A festive German-tradition celebration with beer steins, blue and white decorations and warm festival lighting, joyful atmosphere, no recognizable faces, no brand logos, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento cultural e turístico em cidade-núcleo (São Lourenço do Sul). Fato concreto (lançamento, concurso da corte). Sem guardrail."
    },

    # IDX 15 — Cristal Av. Passo do Mendonça limpeza — REBAIXAR (segunda de Cristal)
    "804da2cbe08274dd604274d8db6acc48cc218fed": _skip(
        "REBAIXAR", "Segunda pauta de Cristal no dia (quota 2/cidade já usada com a obra de calçamento, mais relevante)."),

    # IDX 16 — Guaíba Casa da Primeira Infância + Instituto CMPC — PUBLICAR
    "612f8ebbdad53caf48452e5c9639e704c8fe29ff": {
        "titulo_sultv": "Guaíba firma cooperação para fortalecer o cuidado com a primeira infância",
        "chamada_faixa": "Guaíba reforça o cuidado na primeira infância",
        "subtitulo": "Termo de cooperação prevê encontros com famílias e capacitação de equipes para apoiar o desenvolvimento infantil no município.",
        "lead": "Guaíba aposta nos primeiros anos de vida para construir um futuro melhor. A Prefeitura, por meio da Casa da Primeira Infância, firmou um termo de cooperação com o Instituto CMPC para ampliar as ações voltadas ao desenvolvimento infantil e ao apoio às famílias.",
        "ganchos_3": [
            "Guaíba firma cooperação para a primeira infância",
            "Parceria prevê 15 encontros com famílias no segundo semestre",
            "Capacitação das equipes fortalece o atendimento no município"
        ],
        "angulo_editorial": "Política pública social positiva em cidade da região metropolitana sul (Guaíba). Fato concreto e institucional (termo de cooperação, metas definidas). Foco no desenvolvimento infantil e apoio a famílias — abordagem institucional, sem exposição de menores. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Guaíba", "Casa da Primeira Infância de Guaíba", "Instituto CMPC"],
        "lead_materia_longa": "Guaíba aposta nos primeiros anos de vida para construir um futuro melhor. A Prefeitura, por meio da Casa da Primeira Infância, firmou um termo de cooperação com o Instituto CMPC para ampliar as ações voltadas ao desenvolvimento infantil e ao apoio às famílias.",
        "post_instagram": {
            "caption": "Cuidar dos primeiros anos de vida é investir no futuro. Guaíba firmou um termo de cooperação entre a Casa da Primeira Infância e o Instituto CMPC para fortalecer o desenvolvimento infantil e apoiar as famílias do município. A parceria prevê encontros ao longo do segundo semestre e a capacitação das equipes que atuam no atendimento. Um trabalho que começa cedo e acompanha quem mais precisa.",
            "hashtags": ["#Guaíba", "#PrimeiraInfância", "#RioGrandeDoSul", "#Família", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cuidar dos primeiros anos é investir no futuro.",
            "desenvolvimento_45s": "Guaíba firmou um termo de cooperação entre a Casa da Primeira Infância e o Instituto CMPC para fortalecer o desenvolvimento infantil e apoiar as famílias do município. A parceria prevê encontros com as famílias ao longo do segundo semestre e a capacitação das equipes que atuam no atendimento. Um trabalho que começa cedo, fortalece as habilidades parentais e acompanha quem mais precisa nos diferentes territórios da cidade.",
            "fechamento_8s": "Guaíba investe na base do desenvolvimento.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental suave acolhedor"
        },
        "tag_thumbnail": "Primeira infância, Guaíba",
        "briefing_visual": {
            "descricao_pt": "Brinquedos infantis de madeira e materiais educativos sobre mesa em ambiente acolhedor, símbolo do cuidado com a primeira infância, sem crianças identificáveis",
            "query_en": ["wooden toys early childhood", "child development education materials", "preschool play room"],
            "evitar": ["crianças identificáveis", "rostos", "marcas", "logos", "texto"],
            "prompt_ia": "Wooden educational toys and soft learning materials arranged on a table in a warm, welcoming early-childhood room, symbol of child development care, no children, no faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Política social positiva (primeira infância) em Guaíba. Fato concreto e institucional. Abordagem sem exposição de menores. Sem guardrail."
    },

    # IDX 17 — Guaíba saúde post vago — REBAIXAR
    "00c9643cb9f090d0136fcde0c5f35de0487b25c6": _skip(
        "REBAIXAR", "Post genérico de ação de saúde sem fato concreto novo — material insuficiente para matéria."),

    # IDX 18/19 — Editais leilão Pelotas — BLOQUEAR
    "963f49dc559eccf819962f5e3c2f9299e4caa3a5": _skip(
        "BLOQUEAR", "Edital de leilão extrajudicial — aviso procedural, sem valor editorial."),
    "03637a3c75e7b6197da98649547bebcf71f642ac": _skip(
        "BLOQUEAR", "Duplicata de edital de leilão extrajudicial — procedural, sem valor editorial."),

    # IDX 20 — ALERS concessões/PPP — REBAIXAR (política)
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "REBAIXAR", "Manifestação de parlamentares sobre concessões/PPPs — risco de viés político-partidário (guardrail)."),

    # IDX 21 — ALERS Funcriança — REBAIXAR (política/menores)
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR", "Detalhamento técnico-legislativo (Funcriança) — política e tema que envolve menores, fora do perfil de matéria leve."),

    # IDX 22 — Renegociação de dívidas rurais RS (agro) — PUBLICAR
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "titulo_sultv": "Produtores do RS acompanham com apreensão a renegociação de dívidas rurais",
        "chamada_faixa": "Renegociação de dívidas preocupa o produtor",
        "subtitulo": "Setor agropecuário gaúcho teme ficar sem acesso ao crédito rural para a próxima safra e acompanha a tramitação da renegociação.",
        "lead": "A preocupação tira o sono de quem vive da terra no Rio Grande do Sul. Produtores rurais gaúchos acompanham com apreensão a tramitação da renegociação de dívidas, com receio de ficar sem acesso ao crédito rural para a próxima safra.",
        "ganchos_3": [
            "Produtores do RS temem perder acesso ao crédito rural",
            "Renegociação de dívidas é decisiva para a próxima safra",
            "Setor agropecuário acompanha a tramitação com apreensão"
        ],
        "angulo_editorial": "Agro de alto interesse para a audiência rural e urbana do RS. Fato concreto e econômico (renegociação de dívidas, crédito rural, próxima safra). Tema de política agrícola — não partidário, sem siglas nem candidatos. Pauta-âncora do estado, fortemente alinhada ao público da SulTV.",
        "fontes_complementares_sugeridas": ["Federação da Agricultura do RS (Farsul)", "sindicatos rurais", "cooperativas agropecuárias"],
        "lead_materia_longa": "A preocupação tira o sono de quem vive da terra no Rio Grande do Sul. Produtores rurais gaúchos acompanham com apreensão a tramitação da renegociação de dívidas, com receio de ficar sem acesso ao crédito rural para a próxima safra.",
        "post_instagram": {
            "caption": "A preocupação tira o sono de quem vive da terra. Produtores rurais do Rio Grande do Sul acompanham com apreensão a renegociação de dívidas, temendo ficar sem acesso ao crédito rural para a próxima safra. Depois de anos marcados por adversidades climáticas, o tema é decisivo para a continuidade da atividade no campo. O setor segue atento à tramitação, na expectativa de uma solução que dê fôlego ao produtor.",
            "hashtags": ["#Agro", "#RioGrandeDoSul", "#CréditoRural", "#Safra", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A preocupação tira o sono de quem vive da terra.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a renegociação de dívidas, temendo ficar sem acesso ao crédito rural para a próxima safra. Depois de anos marcados por adversidades climáticas, o tema é decisivo para a continuidade da atividade no campo. Sem crédito, o produtor enfrenta dificuldade para plantar, e a insegurança se espalha por toda a cadeia. O setor segue atento à tramitação, na expectativa de uma solução que dê fôlego a quem produz.",
            "fechamento_8s": "O campo gaúcho espera por uma definição.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental tenso reflexivo"
        },
        "tag_thumbnail": "Renegociação de dívidas, agro RS",
        "briefing_visual": {
            "descricao_pt": "Lavoura de soja ou campo agrícola do Rio Grande do Sul ao amanhecer, com trator ao fundo, sem pessoas, transmitindo o peso da atividade rural",
            "query_en": ["soybean field brazil sunrise", "agriculture tractor field", "rural farm crop landscape"],
            "evitar": ["rostos identificáveis", "marcas de maquinário", "logos", "texto"],
            "prompt_ia": "A wide soybean field in southern Brazil at sunrise with a tractor in the distance, contemplative rural mood, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agro de alto interesse estadual (crédito rural, próxima safra). Fato concreto e econômico. Política agrícola não-partidária, sem siglas. Sem guardrail."
    },

    # IDX 23/24 — fiscalização RS — REBAIXAR
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": _skip(
        "REBAIXAR", "Fiscalização pontual sem âncora regional clara nas cidades-núcleo — vira nota interna."),
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": _skip(
        "REBAIXAR", "Apreensão de alimentos sem âncora regional nas cidades-núcleo — material para nota, não matéria."),

    # IDX 25 — Frio -4ºC primeiro amanhecer do inverno (clima RS) — PUBLICAR
    "055873b031808b741b618cba95d17d541d948a3e": {
        "titulo_sultv": "Primeiro amanhecer do inverno traz frio intenso e -4ºC no Sul gaúcho",
        "chamada_faixa": "Inverno chega com -4ºC no Sul gaúcho",
        "subtitulo": "O início do inverno astronômico foi marcado por mínimas abaixo de zero em várias regiões do Rio Grande do Sul.",
        "lead": "O inverno chegou mostrando a que veio. O primeiro amanhecer da estação no Rio Grande do Sul foi marcado por frio intenso e mínimas abaixo de zero, com registro de até 4ºC negativos no Sul gaúcho.",
        "ganchos_3": [
            "Primeiro amanhecer do inverno registra -4ºC no Sul do RS",
            "Frio intenso marca o início da estação no estado",
            "Temperaturas negativas exigem cuidados com a saúde e a lavoura"
        ],
        "angulo_editorial": "Clima de alto interesse para a audiência rural e urbana do RS. Fato concreto e quantitativo (frio recorde, -4ºC, início do inverno). Impacto direto no campo (geada) e no dia a dia da população. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["meteorologistas", "Defesa Civil do RS", "Emater/RS"],
        "lead_materia_longa": "O inverno chegou mostrando a que veio. O primeiro amanhecer da estação no Rio Grande do Sul foi marcado por frio intenso e mínimas abaixo de zero, com registro de até 4ºC negativos no Sul gaúcho.",
        "post_instagram": {
            "caption": "O inverno chegou mostrando a que veio. O primeiro amanhecer da estação no Rio Grande do Sul registrou frio intenso e mínimas abaixo de zero, com até 4ºC negativos no Sul gaúcho. Além do desconforto, o frio extremo acende o alerta para os cuidados com a saúde e para os efeitos da geada nas lavouras. É hora de se agasalhar bem e ficar de olho na previsão.",
            "hashtags": ["#Inverno", "#RioGrandeDoSul", "#Frio", "#Clima", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O inverno chegou mostrando a que veio.",
            "desenvolvimento_45s": "O primeiro amanhecer da estação no Rio Grande do Sul registrou frio intenso e mínimas abaixo de zero, com até 4ºC negativos no Sul gaúcho. Além do desconforto, o frio extremo acende o alerta para os cuidados com a saúde, especialmente de crianças e idosos, e para os efeitos da geada nas lavouras. No campo, o produtor precisa redobrar a atenção. Na cidade, vale se agasalhar bem e acompanhar a previsão para os próximos dias.",
            "fechamento_8s": "O Sul gaúcho entra no inverno com frio de verdade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental clima frio atmosférico"
        },
        "tag_thumbnail": "Frio intenso, inverno no RS",
        "briefing_visual": {
            "descricao_pt": "Campo coberto de geada branca ao amanhecer no Sul do Rio Grande do Sul, com luz dourada do sol nascente, sem pessoas",
            "query_en": ["frost covered field sunrise", "winter frost grass morning", "frozen pasture cold morning"],
            "evitar": ["pessoas", "marcas", "logos", "texto"],
            "prompt_ia": "A field covered in white frost at sunrise in southern Brazil, golden light hitting frozen grass, crisp winter atmosphere, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima de alto interesse estadual. Fato concreto e quantitativo (-4ºC, início do inverno). Impacto no campo e na população. Sem guardrail."
    },

    # IDX 26 — Canguçu Feirinha de Adoção (comunidade/animal) — PUBLICAR
    "d34d0d8b1eaaab0ffc538db4148f0b463131afce": {
        "titulo_sultv": "Feira de adoção reforça o cuidado e a proteção animal em Canguçu",
        "chamada_faixa": "Canguçu promove feira de adoção animal",
        "subtitulo": "Edição realizada na Praça Dr. Francisco Carlos dos Santos uniu voluntários e poder público em torno da causa animal.",
        "lead": "O cuidado com os animais ganhou as ruas de Canguçu. Mais uma edição da Feirinha de Adoção foi realizada na Praça Dr. Francisco Carlos dos Santos, reunindo voluntários e poder público em torno da proteção animal no município.",
        "ganchos_3": [
            "Feira de adoção movimenta a Praça Dr. Francisco Carlos dos Santos",
            "Iniciativa une voluntários e poder público pela causa animal",
            "Novos cercados vão reforçar a estrutura das próximas feiras"
        ],
        "angulo_editorial": "Comunidade e causa animal em Canguçu (região Sul/Costa Doce ampliada). Fato concreto e positivo (feira realizada, doação de cercados). Engajamento alto, tema afetivo e familiar. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Canguçu", "Núcleo da Causa Animal de Canguçu", "grupo Amigo de Pelo"],
        "lead_materia_longa": "O cuidado com os animais ganhou as ruas de Canguçu. Mais uma edição da Feirinha de Adoção foi realizada na Praça Dr. Francisco Carlos dos Santos, reunindo voluntários e poder público em torno da proteção animal no município.",
        "post_instagram": {
            "caption": "Adotar é um ato de amor. Canguçu realizou mais uma edição da Feirinha de Adoção na Praça Dr. Francisco Carlos dos Santos, reunindo voluntários e poder público pela causa animal. Na ocasião, o grupo Amigo de Pelo recebeu cercados que vão ajudar na estrutura das próximas feiras. Iniciativas assim dão uma nova chance a quem espera por um lar e fortalecem a rede de proteção animal no município.",
            "hashtags": ["#Canguçu", "#AdoçãoAnimal", "#CausaAnimal", "#Comunidade", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Adotar é um ato de amor.",
            "desenvolvimento_45s": "Canguçu realizou mais uma edição da Feirinha de Adoção na Praça Dr. Francisco Carlos dos Santos, reunindo voluntários e poder público em torno da causa animal. Na ocasião, o grupo Amigo de Pelo recebeu cercados que vão ajudar na estrutura das próximas feiras. Iniciativas como essa dão uma nova chance a animais que esperam por um lar e fortalecem a rede de proteção animal, mostrando o poder da mobilização da comunidade.",
            "fechamento_8s": "Canguçu mostra que cuidar é coisa de todos.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental leve afetivo"
        },
        "tag_thumbnail": "Feira de adoção, Canguçu",
        "briefing_visual": {
            "descricao_pt": "Cães e gatos para adoção em uma praça do interior, ambiente de feira de adoção animal ao ar livre, sem rostos humanos identificáveis",
            "query_en": ["pet adoption fair dogs", "rescue dogs adoption event", "shelter pets outdoor"],
            "evitar": ["rostos humanos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Friendly rescue dogs and cats ready for adoption at an outdoor pet adoption fair in a small-town square, warm hopeful mood, no recognizable human faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Comunidade e causa animal em Canguçu. Fato concreto e positivo (feira, doação de cercados). Tema afetivo de alto engajamento. Sem guardrail."
    },

    # IDX 27/28 — Rio Grande posts — REBAIXAR
    "d68776fd739bd1467f612957ec9133b34e19ff72": _skip(
        "REBAIXAR", "Post de registro de evento já ocorrido — material para post, não matéria longa."),
    "7e624f46fec90519b0eeab3cd51c12e2229e599c": _skip(
        "REBAIXAR", "Post comemorativo (aniversário de APA) — efeméride leve, vira post se houver espaço."),

    # IDX 29/30 — Santa Maria posts — REBAIXAR
    "6c556811702675ae018b753405f2f8acb182cb44": _skip(
        "REBAIXAR", "Post de ação pontual de saúde em shopping — fora das cidades-núcleo, material para post."),
    "0b4c3f17bf2fcb078b66ea09667157a93ba1a5e2": _skip(
        "REBAIXAR", "Aviso de mutirão do CadÚnico — serviço pontual fora das cidades-núcleo."),

    # IDX 31/32 — Dom Feliciano Expo — REBAIXAR / BLOQUEAR
    "e58fa913fec8f3d63c9e94eba4c1a2bba93b75a6": _skip(
        "REBAIXAR", "Inscrições para Expo Dom Feliciano — serviço pontual, vira post no slot da cidade-núcleo."),
    "06e824b463b5e0a0bba7df47501bb18ee80d47ca": _skip(
        "BLOQUEAR", "Duplicata do aviso de inscrições da Expo Dom Feliciano."),

    # IDX 33 — Apostas Trilegal Venâncio — REBAIXAR
    "e0d0dea1242b86e974476f1a79179a408edccaeb": _skip(
        "REBAIXAR", "Premiação de loteria fora das cidades-núcleo — baixo valor editorial regional."),

    # IDX 34 — PRF maconha Lajeado — REBAIXAR
    "a113b03cadb243d98e220586440297eff38981b5": _skip(
        "REBAIXAR", "Apreensão de droga em região distante (Vale do Taquari) — fora do foco geográfico e tema sensível."),

    # IDX 35 — Inadimplência alta RS — REBAIXAR
    "a1a09385daece83ee02f54c756f3b29269168909": _skip(
        "REBAIXAR", "Indicador econômico estadual genérico sem âncora regional — material para post/nota."),

    # IDX 36 — Bento fondue/vinho — REBAIXAR
    "c78fe29d81cb6422afc4b39b33a3fd2ee8074177": _skip(
        "REBAIXAR", "Pauta gastronômica da Serra, fora do foco geográfico Costa Doce/Sul."),
}


MATERIAS = {

    "1c32d88ed265b7288cb6e7799fbce8666cb0ac3a": """### Título ###
Festa de São João 2026 reúne milhares na Prainha, em Camaquã

### Artigo ###
Milhares de pessoas tomaram a Prainha neste fim de semana. A Festa de São João 2026 movimenta Camaquã, na região da Costa Doce, com programação no Complexo Poliesportivo Ruy de Castro Netto, mais conhecido como Prainha, e shows que reuniram público de toda a região. A tradição junina é uma das mais queridas do calendário gaúcho, e em Camaquã ganha proporções de grande evento. Durante a festa, comidas típicas, música e atrações para todas as idades transformam o espaço em ponto de encontro de famílias, que aproveitam as noites de junho para celebrar uma das datas mais simbólicas do ano. Mais do que diversão, eventos desse porte têm um peso concreto na economia local. O movimento aquece o comércio, gera oportunidades para empreendedores, ambulantes e artistas da região e atrai visitantes que se hospedam, consomem e conhecem a cidade. O turismo de eventos vem se firmando como uma vocação do interior, e festas tradicionais como a de São João ajudam a colocar municípios da Costa Doce no mapa cultural do estado. A escolha da Prainha como palco reforça o caráter popular da celebração, em um espaço amplo e familiar, capaz de receber grande público com segurança. A cada edição, a festa renova laços comunitários e fortalece o sentimento de pertencimento que une os moradores. Em tempos em que o calendário de eventos disputa a atenção do público, a Festa de São João de Camaquã mostra a força das tradições que resistem ao tempo. É a cultura popular cumprindo o seu papel: reunir gente, movimentar a cidade e celebrar a identidade do Rio Grande do Sul.

### Legenda sugerida ###
A Festa de São João 2026 reuniu milhares de pessoas na Prainha, em Camaquã, movimentando a cultura e o comércio da Costa Doce.

### Palavras-chave ###
Festa de São João, Camaquã, Prainha, Costa Doce, tradição junina, cultura, turismo de eventos
""",

    "4d84d73fbe84b729ff39aaf941f9080399410131": """### Título ###
Bandas de Tapes e Sentinela do Sul recebem reconhecimento de maestro campeão mundial

### Artigo ###
O talento musical da Costa Doce ganhou reconhecimento de peso. As bandas municipais de Tapes e Sentinela do Sul, no Sul do Rio Grande do Sul, foram elogiadas pelo desempenho artístico pelo maestro campeão mundial Rogério Wanderley Brito. O reconhecimento coroa um trabalho de formação musical que vem se destacando em duas cidades do interior gaúcho. As corporações musicais são patrimônios culturais dos municípios. Mais do que conjuntos artísticos, elas representam um espaço de formação para crianças, jovens e adultos, que encontram na música uma oportunidade de aprendizado, disciplina e convivência. O elogio de uma autoridade do meio confirma a qualidade desse esforço coletivo, sustentado ao longo do tempo por músicos, professores, famílias e poder público. Manter bandas ativas no interior exige dedicação e continuidade. O resultado aparece nas apresentações em datas cívicas, festas comunitárias e eventos culturais, momentos em que as corporações ganham as ruas e reúnem a população em torno de uma tradição que atravessa gerações. Para as duas cidades, ver o trabalho reconhecido fora de seus limites é motivo de orgulho e de estímulo. O destaque alcançado por Tapes e Sentinela do Sul valoriza a cultura produzida longe dos grandes centros e mostra que o talento da Costa Doce tem reconhecimento que ultrapassa as fronteiras da região. É também um convite para que novos integrantes se aproximem das bandas e para que o investimento na formação musical tenha continuidade. A música é um elo poderoso de identidade e pertencimento. Ao terem o desempenho reconhecido, as bandas dos dois municípios reforçam a importância de preservar e apoiar as iniciativas culturais que fortalecem as comunidades do interior gaúcho.

### Legenda sugerida ###
Bandas de Tapes e Sentinela do Sul têm o desempenho artístico reconhecido pelo maestro campeão mundial Rogério Wanderley Brito.

### Palavras-chave ###
bandas de Tapes, Sentinela do Sul, cultura, música, Costa Doce, corporação musical, reconhecimento
""",

    "dd7df59af3392ccb9037aa29aab34324cac79b5c": """### Título ###
Cerro Grande do Sul abre inscrições para cursos gratuitos com bolsa permanência

### Artigo ###
Quem busca qualificação tem uma nova oportunidade na Costa Doce. Cerro Grande do Sul, na região Sul do Rio Grande do Sul, abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes. A iniciativa é conduzida pela Secretaria Municipal do Trabalho, Cidadania e Assistência Social e amplia o acesso à formação no município. Cursos gratuitos de qualificação têm um papel decisivo no interior. Eles permitem que jovens e adultos desenvolvam novas habilidades, melhorem o currículo e aumentem as chances de conquistar uma vaga no mercado de trabalho, sem que o custo seja um obstáculo. A oferta de bolsa permanência reforça essa lógica, ao ajudar o participante a se manter no curso até o fim, reduzindo a evasão e garantindo que o esforço se transforme em conclusão. Investir em qualificação é investir no desenvolvimento da própria cidade. Mão de obra mais preparada atrai negócios, fortalece o comércio e os serviços, agrega valor às atividades locais e contribui para fixar talentos na região, evitando que as pessoas precisem se deslocar para os grandes centros em busca de oportunidades. Para quem tem interesse, o caminho é simples: ficar atento ao período de inscrição e procurar a secretaria responsável para garantir a vaga. Iniciativas como essa mostram que a qualificação profissional não é privilégio dos grandes centros e pode chegar com força às cidades da Costa Doce. Ao abrir portas para a formação, Cerro Grande do Sul reforça que educação e trabalho caminham juntos na construção de um futuro melhor para a comunidade.

### Legenda sugerida ###
Cerro Grande do Sul está com inscrições abertas para dois cursos gratuitos de qualificação profissional, com bolsa permanência.

### Palavras-chave ###
Cerro Grande do Sul, cursos gratuitos, qualificação profissional, bolsa permanência, emprego, Costa Doce, trabalho
""",

    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": """### Título ###
Arambaré publica nota técnica com orientações sobre poda e arborização urbana

### Artigo ###
Arambaré quer árvores mais saudáveis e cidade mais segura. A Prefeitura do município, na orla da Lagoa dos Patos, publicou a Nota Técnica nº 01/2026, com orientações sobre o manejo da arborização urbana e a poda correta de árvores. O documento, elaborado pela Diretoria Municipal de Meio Ambiente, busca orientar a população e padronizar condutas em um tema que, embora pareça simples, exige cuidado técnico. A arborização urbana cumpre funções essenciais. As árvores proporcionam sombra, ajudam a regular a temperatura, abrigam a fauna e compõem a paisagem que dá identidade às cidades à beira da lagoa. Por outro lado, a poda feita de forma inadequada pode comprometer a saúde da planta, gerar riscos de queda de galhos e até trazer problemas de segurança para moradores e para a rede elétrica. Por isso, ter diretrizes claras faz diferença. A nota técnica orienta sobre como e quando podar, quais práticas devem ser evitadas e a importância de respeitar o desenvolvimento natural das espécies. Com a informação correta, o morador se torna um aliado da preservação, contribuindo para uma cidade mais verde e organizada. Medidas como essa revelam um cuidado de longo prazo com o ambiente urbano. Preservar e manejar bem a arborização é também valorizar a qualidade de vida e o potencial turístico de um município que tem na natureza um de seus maiores patrimônios. Ao tornar pública a orientação, Arambaré reforça o compromisso com o equilíbrio entre o crescimento da cidade e a proteção do meio ambiente, convidando a comunidade a participar desse cuidado no dia a dia.

### Legenda sugerida ###
A Prefeitura de Arambaré publicou nota técnica com orientações para o manejo da arborização urbana e a poda correta de árvores.

### Palavras-chave ###
Arambaré, arborização urbana, poda de árvores, meio ambiente, nota técnica, Costa Doce, preservação
""",

    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": """### Título ###
Cristal prepara a Rua Camaquã para receber obras de calçamento

### Artigo ###
Mais uma rua de Cristal vai ganhar calçamento. A Prefeitura do município, na região da Costa Doce, iniciou os serviços de preparação da Rua Camaquã para receber as obras de pavimentação. A etapa antecede o calçamento e marca o avanço de mais um trecho na agenda de melhorias urbanas da cidade. A preparação do terreno é um passo fundamental. Antes da pavimentação, é preciso nivelar o solo, organizar o escoamento da água e garantir as condições para que o calçamento tenha qualidade e durabilidade. É um trabalho que não aparece tanto quanto a obra concluída, mas que define o resultado final e a vida útil da via. Para os moradores, o calçamento representa uma mudança concreta no dia a dia. Ruas pavimentadas reduzem a poeira no tempo seco e a lama nos dias de chuva, facilitam o trânsito de veículos e o deslocamento de pedestres, valorizam os imóveis do entorno e melhoram o acesso a casas, ao comércio e aos serviços. São ganhos que se sentem logo nos primeiros dias de uso. Obras de infraestrutura que chegam bairro a bairro mostram um modelo de desenvolvimento que se constrói no chão da cidade, atendendo demandas antigas das comunidades. Cada rua pavimentada é um passo a mais na qualidade de vida e na organização do espaço urbano. Ao preparar a Rua Camaquã para o calçamento, Cristal sinaliza continuidade no investimento em mobilidade e infraestrutura, um compromisso que impacta diretamente a rotina de quem vive no município.

### Legenda sugerida ###
A Prefeitura de Cristal iniciou a preparação da Rua Camaquã para receber as obras de calçamento, ampliando a infraestrutura urbana.

### Palavras-chave ###
Cristal, calçamento, obras, infraestrutura, pavimentação, Costa Doce, mobilidade urbana
""",

    "9a0afe0a71110324f476128af3e817babce239d4": """### Título ###
Südoktoberfest abre contagem regressiva com lançamento oficial em São Lourenço do Sul

### Artigo ###
A festa germânica mais aguardada da Costa Doce já tem data marcada. São Lourenço do Sul deu início à contagem regressiva para a Südoktoberfest, com lançamento oficial do evento e a abertura do concurso para a escolha da corte. O anúncio marca o começo da preparação de uma das maiores celebrações de tradição germânica do Sul do estado. A Südoktoberfest é um dos grandes símbolos culturais e turísticos do município. Com música, dança, gastronomia típica e a valorização da herança dos imigrantes, a festa atrai visitantes de várias regiões e movimenta a cidade durante os dias de programação. O concurso da corte, anunciado no lançamento, é uma das tradições mais queridas, envolvendo a comunidade na escolha das representantes que serão o rosto do evento. O impacto vai muito além das noites de festa. Eventos desse porte aquecem o comércio, a rede hoteleira, a gastronomia e os serviços, gerando renda e oportunidades para empreendedores locais. O turismo de eventos é hoje uma vocação consolidada de São Lourenço do Sul, e cada edição reforça o nome da cidade no calendário cultural do Rio Grande do Sul. Preservar e celebrar a tradição germânica é também manter viva uma parte importante da identidade da Costa Doce, transmitida de geração em geração. Ao abrir a contagem regressiva, o município convida moradores e visitantes a se prepararem para mais uma edição que promete reunir cultura, hospitalidade e a força de uma comunidade que tem orgulho de suas raízes.

### Legenda sugerida ###
São Lourenço do Sul abriu a contagem regressiva para a Südoktoberfest, com lançamento oficial do evento e o concurso da corte.

### Palavras-chave ###
Südoktoberfest, São Lourenço do Sul, festa germânica, cultura, turismo, Costa Doce, tradição
""",

    "612f8ebbdad53caf48452e5c9639e704c8fe29ff": """### Título ###
Guaíba firma cooperação para fortalecer o cuidado com a primeira infância

### Artigo ###
Guaíba aposta nos primeiros anos de vida para construir um futuro melhor. A Prefeitura, por meio da Casa da Primeira Infância, firmou um termo de cooperação com o Instituto CMPC para ampliar as ações voltadas ao desenvolvimento infantil e ao apoio às famílias do município. A parceria estrutura o trabalho em frentes complementares e dá mais consistência a um atendimento que começa cedo. Uma das frentes prevê a intervenção direta com famílias, com a realização de encontros ao longo do segundo semestre de 2026. A proposta é fortalecer as habilidades parentais na vida cotidiana, alcançando dezenas de famílias já acompanhadas pela Casa da Primeira Infância nos diferentes territórios da cidade. O foco está em apoiar quem cuida, oferecendo orientação e fortalecendo os vínculos no ambiente em que a criança cresce. Outra frente importante é a capacitação das equipes. Qualificar os profissionais que atuam no atendimento garante que o cuidado oferecido seja cada vez mais preparado e baseado em boas práticas. Investir em formação é multiplicar o impacto da política pública, já que cada profissional mais capacitado se traduz em melhor acolhimento às famílias. O cuidado com a primeira infância é hoje reconhecido como um dos investimentos mais estratégicos que um município pode fazer. Os primeiros anos de vida são decisivos para o desenvolvimento, e ações nessa fase produzem efeitos que se estendem por toda a trajetória da criança. Ao firmar a cooperação, Guaíba reforça o entendimento de que apoiar as famílias e qualificar o atendimento é semear, desde cedo, um futuro mais promissor para a comunidade.

### Legenda sugerida ###
Guaíba firmou termo de cooperação entre a Casa da Primeira Infância e o Instituto CMPC para fortalecer o desenvolvimento infantil.

### Palavras-chave ###
Guaíba, primeira infância, Casa da Primeira Infância, Instituto CMPC, desenvolvimento infantil, família, cooperação
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS acompanham com apreensão a renegociação de dívidas rurais

### Artigo ###
A preocupação tira o sono de quem vive da terra no Rio Grande do Sul. Produtores rurais gaúchos acompanham com apreensão a tramitação da renegociação de dívidas, com receio de ficar sem acesso ao crédito rural para a próxima safra. O tema é decisivo para a continuidade da atividade no campo e mobiliza o setor em todo o estado. O Rio Grande do Sul vem de anos especialmente difíceis. Sucessivas adversidades climáticas afetaram a produção, comprometeram a renda e deixaram muitos produtores endividados. Nesse cenário, a renegociação das dívidas aparece como uma das principais saídas para que o agricultor consiga reorganizar as finanças e voltar a investir na lavoura com mais segurança. O acesso ao crédito rural é o que viabiliza o plantio. Sem ele, o produtor enfrenta dificuldade para comprar sementes, insumos e tudo o que a safra exige. A insegurança em torno da renegociação, portanto, não fica restrita à porteira: ela se espalha por toda a cadeia, afetando o comércio de insumos, o transporte, as cooperativas e a economia das cidades que dependem do agro. O campo gaúcho pede previsibilidade. Mais do que um alívio pontual, o setor busca condições para planejar a próxima safra com tranquilidade, sabendo que poderá contar com financiamento para produzir. Enquanto a definição não vem, a apreensão permanece. O produtor segue atento a cada passo da tramitação, na expectativa de uma solução que dê fôlego a quem alimenta o estado e o país. A força do agro gaúcho depende, também, de regras claras e de apoio nos momentos mais delicados.

### Legenda sugerida ###
Produtores rurais do RS temem ficar sem crédito para a próxima safra e acompanham com apreensão a renegociação de dívidas.

### Palavras-chave ###
agro, Rio Grande do Sul, renegociação de dívidas, crédito rural, safra, produtores rurais, agricultura
""",

    "055873b031808b741b618cba95d17d541d948a3e": """### Título ###
Primeiro amanhecer do inverno traz frio intenso e -4ºC no Sul gaúcho

### Artigo ###
O inverno chegou mostrando a que veio. O primeiro amanhecer da estação no Rio Grande do Sul foi marcado por frio intenso e mínimas abaixo de zero, com registro de até 4ºC negativos no Sul gaúcho. O início do inverno astronômico confirmou a expectativa de uma manhã rigorosa em boa parte do estado. Temperaturas tão baixas exigem atenção redobrada. O frio extremo aumenta os riscos para a saúde, especialmente de crianças, idosos e pessoas com doenças respiratórias e cardíacas. Agasalhar-se bem, manter os ambientes aquecidos com segurança e redobrar os cuidados com quem é mais vulnerável são medidas simples que fazem diferença nos dias mais gelados. No campo, o frio intenso traz um alerta adicional. A geada, comum nesta época, pode afetar lavouras e pastagens, exigindo do produtor atenção ao manejo e ao planejamento das atividades. Ao mesmo tempo, o frio é parte do ciclo natural e necessário para diversas culturas e para o equilíbrio das estações no Sul do país. Para a população, o início do inverno também muda a rotina. Aumenta a procura por agasalhos, as noites pedem mais aconchego e o consumo de energia tende a subir. É o momento de redobrar a atenção com o conforto térmico em casa e nas estradas, onde a formação de geada pode tornar o piso escorregadio nas primeiras horas do dia. O Rio Grande do Sul é conhecido pelos invernos mais marcantes do país, e este ano a estação começou fiel à sua fama. Acompanhar a previsão e se preparar para a oscilação das temperaturas é a melhor forma de atravessar os próximos meses com segurança e tranquilidade.

### Legenda sugerida ###
O primeiro amanhecer do inverno registrou frio intenso e até 4ºC negativos no Sul do Rio Grande do Sul, com alerta para a geada.

### Palavras-chave ###
inverno, Rio Grande do Sul, frio intenso, geada, temperatura negativa, clima, Sul gaúcho
""",

    "d34d0d8b1eaaab0ffc538db4148f0b463131afce": """### Título ###
Feira de adoção reforça o cuidado e a proteção animal em Canguçu

### Artigo ###
O cuidado com os animais ganhou as ruas de Canguçu. Mais uma edição da Feirinha de Adoção foi realizada na Praça Dr. Francisco Carlos dos Santos, reunindo voluntários e poder público em torno da proteção animal no município. A iniciativa é promovida pelo grupo Amigo de Pelo, com o apoio do Núcleo da Causa Animal, vinculado à Secretaria Municipal de Agricultura, Pecuária, Cooperativismo e Recursos Hídricos. As feiras de adoção cumprem um papel importante. Elas aproximam a comunidade dos animais que esperam por um lar, dão visibilidade à causa e estimulam a adoção responsável, oferecendo uma nova chance a quem foi abandonado ou resgatado. Mais do que encontrar um novo dono, cada adoção representa um compromisso de cuidado, afeto e responsabilidade que transforma a vida do animal e da família que o acolhe. O evento contou com a presença de autoridades municipais, em um gesto que reforça a parceria entre o poder público e os grupos de voluntários. Na ocasião, o grupo Amigo de Pelo recebeu dois cercados, que vão auxiliar na estrutura e na organização das próximas feiras. O apoio prático faz diferença para quem dedica tempo e energia à causa, muitas vezes de forma voluntária e silenciosa. A proteção animal é uma pauta que mobiliza cada vez mais as comunidades do interior. Iniciativas como essa mostram que o cuidado com os animais é também um exercício de cidadania e de empatia, capaz de unir pessoas em torno de um objetivo comum. Ao realizar mais uma edição da Feirinha de Adoção, Canguçu reafirma que dar um lar a quem precisa é um gesto de amor que fortalece toda a sociedade.

### Legenda sugerida ###
Canguçu realizou mais uma Feirinha de Adoção na Praça Dr. Francisco Carlos dos Santos, reforçando a causa e a proteção animal.

### Palavras-chave ###
Canguçu, feira de adoção, causa animal, proteção animal, adoção responsável, comunidade, voluntariado
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
            print(f"[angular] sem angulação para {h} — bloqueando")
            angul = _skip("BLOQUEAR", "Sem angulação configurada — descartado pelo guardrail")
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
