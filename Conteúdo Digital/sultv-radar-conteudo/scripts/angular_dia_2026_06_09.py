#!/usr/bin/env python3
"""
angular_dia_2026_06_09.py — angulação editorial + redação (cowork-faz-tudo).

Pauta de 2026-06-09. Lê state/aprovadas_2026-06-09.json, gera
state/pauta_2026-06-09.json + state/materias_2026-06-09/<id_hash>.md.
Regra 12 aplicada: NENHUMA menção a veículos/portais; só fontes primárias
institucionais. Quota máx 10 PUBLICAR.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-09"


def _skip(decisao: str, motivo: str) -> dict:
    return {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "", "decisao_final": decisao, "decisao_motivo": motivo,
    }


PAUTA_ANGULADA = {
    # 0 — Maestro multicampeão reconhece bandas de Tapes e Sentinela — PUBLICAR
    "ce87e878ba5048a6f108ee5191b838ce7ecb89df": {
        "tag_principal": "cultura",
        "titulo_sultv": "Bandas de Tapes e Sentinela do Sul recebem reconhecimento de maestro multicampeão mundial",
        "chamada_faixa": "Bandas de Tapes e Sentinela ganham reconhecimento internacional",
        "subtitulo": "Trabalho musical da Região Centro-Sul do RS foi destacado por um dos maiores nomes da regência, dando visibilidade ao esforço de músicos da Costa Doce.",
        "lead": "O trabalho desenvolvido por bandas musicais de Tapes e Sentinela do Sul recebeu o reconhecimento de um maestro multicampeão mundial, dando projeção ao esforço cultural mantido por músicos da Região Centro-Sul do Rio Grande do Sul.",
        "ganchos_3": [
            "Bandas de Tapes e Sentinela do Sul ganham reconhecimento internacional",
            "Maestro multicampeão mundial destaca a qualidade do trabalho musical",
            "Cultura da Costa Doce ganha visibilidade além das fronteiras do RS",
        ],
        "angulo_editorial": "Cultura regional positiva na Costa Doce — valorização do trabalho de bandas de duas cidades-núcleo (Tapes e Sentinela do Sul). Pauta de orgulho comunitário, tom institucional celebrativo.",
        "fontes_complementares_sugeridas": ["Secretarias de Cultura de Tapes e Sentinela do Sul", "Regentes das bandas locais"],
        "lead_materia_longa": "O trabalho desenvolvido por bandas musicais de Tapes e Sentinela do Sul recebeu o reconhecimento de um maestro multicampeão mundial.",
        "post_instagram": {
            "caption": "Orgulho da Costa Doce! As bandas musicais de Tapes e Sentinela do Sul receberam o reconhecimento de um maestro multicampeão mundial. É o talento da Região Centro-Sul do RS cruzando fronteiras e mostrando a força da cultura do interior gaúcho.",
            "hashtags": ["#Tapes", "#SentinelaDoSul", "#Cultura", "#Música", "#CostaDoce", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Música do interior ganha o mundo.",
            "desenvolvimento_45s": "As bandas musicais de Tapes e Sentinela do Sul receberam o reconhecimento de um maestro multicampeão mundial, que destacou a qualidade do trabalho desenvolvido na Região Centro-Sul do Rio Grande do Sul. O reconhecimento dá visibilidade ao esforço de músicos e regentes que mantêm viva a tradição das bandas nas cidades da Costa Doce, muitas vezes formando jovens e mantendo a cultura local.",
            "fechamento_8s": "Talento gaúcho que cruza fronteiras.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental orquestral inspirador",
        },
        "tag_thumbnail": "Cultura no Sul",
        "briefing_visual": {
            "descricao_pt": "Banda musical com instrumentos de sopro tocando em apresentação ao ar livre em cidade do interior do Sul do Brasil, sem rostos identificáveis em close",
            "query_en": ["brass band performance outdoor", "marching band instruments", "community wind band concert"],
            "evitar": ["rosto identificável em close", "marcas", "texto", "logos"],
            "prompt_ia": "A community wind band with brass and woodwind instruments performing outdoors in a small southern Brazilian town, warm afternoon light, no readable text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura positiva em duas cidades-núcleo (Tapes e Sentinela do Sul), fato concreto de reconhecimento, sem guardrail",
    },

    # 1 — Quadrangular Final da Bocha em Sertão Santana — REBAIXAR
    "1fe0147cd164ce3ecbfa00f8075c9954c4ae2a58": {
        **_skip("REBAIXAR", "Esporte amador de baixo impacto editorial fora das cidades-núcleo; vira nota interna"),
        "titulo_sultv": "Quadrangular final de bocha movimenta Sertão Santana",
        "tag_principal": "esporte",
    },

    # 2 — Bandas Tapes/Sentinela (duplicata do item 0) — REBAIXAR
    "78bac7e6e4c1f383c988ac8455c5bcc5cac1eaee": {
        **_skip("REBAIXAR", "Mesma pauta do reconhecimento das bandas já selecionada para PUBLICAR (evita conteúdo duplicado)"),
        "titulo_sultv": "Reconhecimento às bandas de Tapes e Sentinela do Sul (duplicata)",
        "tag_principal": "cultura",
    },

    # 3 — Cursos gratuitos Arambaré (data abril) — REBAIXAR
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": {
        **_skip("REBAIXAR", "Conteúdo defasado (inscrições anunciadas em abril/2026, provavelmente encerradas); título com concatenação de scraping"),
        "titulo_sultv": "Arambaré ofertou cursos gratuitos de qualificação profissional",
        "tag_principal": "educacao",
    },

    # 4 — Plataforma de Pesca Arambaré (data janeiro) — REBAIXAR
    "7328151d0f689699ca147e00ec7ffb87008ee51e": {
        **_skip("REBAIXAR", "Conteúdo defasado (anúncio de janeiro/2026); título com concatenação de scraping"),
        "titulo_sultv": "Arambaré anunciou reconstrução da Plataforma de Pesca",
        "tag_principal": "infraestrutura",
    },

    # 5 — Preso por descumprir prisão domiciliar São Lourenço — PUBLICAR
    "6cdde572c3587fe83a27846957bbd81b7db8ddbf": {
        "tag_principal": "policia",
        "titulo_sultv": "Polícia Civil prende homem por descumprir prisão domiciliar em São Lourenço do Sul",
        "chamada_faixa": "Homem é preso por descumprir prisão domiciliar",
        "subtitulo": "Ação ocorreu na tarde de segunda-feira (8); suspeito de 66 anos foi detido por não cumprir as condições impostas pela Justiça.",
        "lead": "A Polícia Civil prendeu, na tarde desta segunda-feira (8), um homem de 66 anos em São Lourenço do Sul por descumprir as condições da prisão domiciliar a que estava submetido por decisão da Justiça.",
        "ganchos_3": [
            "Homem de 66 anos preso por descumprir prisão domiciliar",
            "Ação da Polícia Civil ocorreu na tarde de segunda (8)",
            "Descumprimento de medida judicial pode levar à prisão",
        ],
        "angulo_editorial": "Segurança na Costa Doce (São Lourenço do Sul, cidade-núcleo). Fato concreto e fresco de ação policial, sem vítima identificada, sem expor dados pessoais do detido. Tom institucional.",
        "fontes_complementares_sugeridas": ["Polícia Civil RS", "Delegacia de São Lourenço do Sul"],
        "lead_materia_longa": "A Polícia Civil prendeu, na tarde desta segunda-feira (8), um homem de 66 anos em São Lourenço do Sul por descumprir as condições da prisão domiciliar.",
        "post_instagram": {
            "caption": "Em São Lourenço do Sul, a Polícia Civil prendeu na tarde de segunda-feira (8) um homem de 66 anos por descumprir as condições da prisão domiciliar imposta pela Justiça. O descumprimento de medidas judiciais pode resultar na conversão para prisão.",
            "hashtags": ["#SãoLourençoDoSul", "#Segurança", "#PolíciaCivil", "#CostaDoce", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Prisão em São Lourenço do Sul.",
            "desenvolvimento_45s": "A Polícia Civil prendeu na tarde de segunda-feira um homem de 66 anos em São Lourenço do Sul por descumprir as condições da prisão domiciliar a que estava submetido. Quem cumpre prisão domiciliar precisa respeitar regras como permanecer na residência e não se ausentar sem autorização judicial. O descumprimento dessas condições pode levar à conversão da medida em prisão, como ocorreu neste caso.",
            "fechamento_8s": "Justiça mantém as regras da medida.",
            "cta_5s": "Veja no SulTV.",
            "trilha_sugerida": "instrumental sóbrio",
        },
        "tag_thumbnail": "Segurança na Costa Doce",
        "briefing_visual": {
            "descricao_pt": "Viatura da Polícia Civil em rua de cidade do interior do Sul do Brasil, luz do dia, sem pessoas identificáveis",
            "query_en": ["police car brazil street", "civil police vehicle daytime", "law enforcement patrol car"],
            "evitar": ["rostos identificáveis", "pessoas detidas", "marcas", "texto", "logos"],
            "prompt_ia": "A civil police patrol car parked on a street of a small southern Brazilian town, daytime, no people visible, no text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Ação policial concreta e fresca em cidade-núcleo (São Lourenço do Sul), sem vítima identificada nem tragédia",
    },

    # 6 — Edital de penalidade Chuvisca — BLOQUEAR
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": {
        **_skip("BLOQUEAR", "Edital administrativo procedural, sem conteúdo editorial publicável"),
        "titulo_sultv": "Edital de penalidade — Chuvisca",
    },

    # 7 — Edital perímetro urbano Chuvisca — BLOQUEAR
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": {
        **_skip("BLOQUEAR", "Edital administrativo procedural (abertura de prazo para requerimentos), formato de edital"),
        "titulo_sultv": "Edital de ampliação do perímetro urbano — Chuvisca",
    },

    # 8 — Aviso de audiência pública Sentinela — BLOQUEAR
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": {
        **_skip("BLOQUEAR", "Aviso procedural sem corpo de notícia (cabeçalho de comunicado)"),
        "titulo_sultv": "Aviso de audiência pública — Sentinela do Sul",
    },

    # 9 — Emissão de notas fiscais Sentinela — BLOQUEAR
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": {
        **_skip("BLOQUEAR", "Comunicado administrativo procedural sem valor editorial"),
        "titulo_sultv": "Emissão de notas fiscais pelo emissor nacional — Sentinela do Sul",
    },

    # 10 — Secretaria Administração / contracheques Barra do Ribeiro — BLOQUEAR
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": {
        **_skip("BLOQUEAR", "Cabeçalho de seção administrativa capturado pelo scraper, sem matéria"),
        "titulo_sultv": "Servidores — revisão de contracheques — Barra do Ribeiro",
    },

    # 11 — Lei fogos com estampido proibidos Barra do Ribeiro — PUBLICAR
    "6d583901d0b2623e718e91c071da59f2069c1522": {
        "tag_principal": "meio_ambiente",
        "titulo_sultv": "Barra do Ribeiro proíbe fogos de artifício com estampido por lei municipal",
        "chamada_faixa": "Barra do Ribeiro proíbe fogos com estampido",
        "subtitulo": "Lei Municipal nº 2850/2025 veda o uso de fogos barulhentos no município; medida protege animais e pessoas sensíveis a ruídos.",
        "lead": "Barra do Ribeiro proíbe o uso de fogos de artifício com estampido em todo o território do município, conforme a Lei Municipal nº 2850/2025. A medida ganha relevância às vésperas das festas juninas, período de maior uso de artefatos pirotécnicos.",
        "ganchos_3": [
            "Lei municipal proíbe fogos de artifício com estampido em Barra do Ribeiro",
            "Medida protege animais, idosos e pessoas sensíveis a ruídos",
            "Regra ganha destaque às vésperas das festas juninas",
        ],
        "angulo_editorial": "Serviço e cidadania na Costa Doce (Barra do Ribeiro, cidade do entorno núcleo). Lei concreta e atual, com forte gancho sazonal (festas juninas em junho) e apelo ao bem-estar animal — tema sensível para o público rural e urbano.",
        "fontes_complementares_sugeridas": ["Prefeitura de Barra do Ribeiro", "Câmara de Vereadores de Barra do Ribeiro", "Secretaria de Agricultura e Meio Ambiente"],
        "lead_materia_longa": "Barra do Ribeiro proíbe o uso de fogos de artifício com estampido em todo o município, conforme a Lei Municipal nº 2850/2025.",
        "post_instagram": {
            "caption": "Atenção em Barra do Ribeiro: a Lei Municipal nº 2850/2025 proíbe fogos de artifício com estampido em todo o município. A regra protege animais, idosos, autistas e pessoas sensíveis a ruídos — e ganha ainda mais importância no período das festas juninas. Prefira os fogos sem barulho.",
            "hashtags": ["#BarraDoRibeiro", "#BemEstarAnimal", "#FestasJuninas", "#CostaDoce", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Fogos barulhentos estão proibidos.",
            "desenvolvimento_45s": "Em Barra do Ribeiro, a Lei Municipal nº 2850/2025 proíbe o uso de fogos de artifício com estampido em todo o município. A medida tem como objetivo proteger animais, idosos, pessoas autistas e quem é sensível a ruídos altos. Com a chegada das festas juninas, época de maior uso de fogos, a recomendação é optar pelos modelos sem barulho, que oferecem o mesmo efeito visual sem o estresse causado pelo estampido.",
            "fechamento_8s": "Festa com respeito a quem sente o barulho.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental leve",
        },
        "tag_thumbnail": "Lei em Barra do Ribeiro",
        "briefing_visual": {
            "descricao_pt": "Cão assustado deitado em ambiente doméstico durante a noite, sem pessoas, ou fogos de artifício silenciosos coloridos no céu",
            "query_en": ["fireworks colorful night sky", "scared dog hiding home", "silent fireworks display"],
            "evitar": ["pessoas identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Colorful fireworks lighting up the night sky over a small Brazilian town, distant view, no text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Lei municipal concreta com forte gancho sazonal (festas juninas) e apelo de bem-estar animal; serviço de utilidade pública",
    },

    # 12 — Rua Camaquã preparação obras calçamento Cristal — PUBLICAR
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": {
        "tag_principal": "infraestrutura",
        "titulo_sultv": "Cristal prepara Rua Camaquã para obras de calçamento",
        "chamada_faixa": "Rua Camaquã recebe preparo para calçamento",
        "subtitulo": "Serviços iniciais antecedem a pavimentação da via; obra integra o pacote de melhorias urbanas do município da Costa Doce.",
        "lead": "A Rua Camaquã, em Cristal, recebe os serviços de preparação que antecedem as obras de calçamento, etapa que faz parte do pacote de melhorias na infraestrutura urbana conduzido pela administração municipal.",
        "ganchos_3": [
            "Rua Camaquã recebe preparação para obras de calçamento",
            "Etapa antecede a pavimentação definitiva da via",
            "Obra integra o pacote de melhorias urbanas de Cristal",
        ],
        "angulo_editorial": "Infraestrutura urbana em cidade-núcleo (Cristal). Obra concreta de pavimentação, pauta de serviço com impacto direto na mobilidade da comunidade. Tom institucional.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria de Obras de Cristal"],
        "lead_materia_longa": "A Rua Camaquã, em Cristal, recebe os serviços de preparação que antecedem as obras de calçamento.",
        "post_instagram": {
            "caption": "Em Cristal, a Rua Camaquã já recebe os serviços de preparação que antecedem o calçamento. A pavimentação faz parte do pacote de melhorias urbanas do município e promete mais conforto e mobilidade para os moradores da via.",
            "hashtags": ["#Cristal", "#Infraestrutura", "#Obras", "#CostaDoce", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Mais uma rua vai ser calçada em Cristal.",
            "desenvolvimento_45s": "A Rua Camaquã, em Cristal, recebe os serviços de preparação que antecedem as obras de calçamento. Essa etapa inicial é fundamental para garantir a qualidade e a durabilidade da pavimentação, que faz parte do pacote de melhorias na infraestrutura urbana do município. Obras como essa impactam diretamente o dia a dia dos moradores, melhorando a mobilidade, reduzindo a poeira e a lama e valorizando os imóveis da região.",
            "fechamento_8s": "Infraestrutura que muda o cotidiano.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental otimista",
        },
        "tag_thumbnail": "Obras em Cristal",
        "briefing_visual": {
            "descricao_pt": "Rua de terra em preparação para calçamento em cidade pequena do interior do Sul do Brasil, máquinas e paralelepípedos, sem pessoas identificáveis",
            "query_en": ["cobblestone street paving construction", "road preparation small town", "street paving work machinery"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A dirt street being prepared for cobblestone paving in a small southern Brazilian town, construction machinery and paving stones, daytime, no readable text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Obra de infraestrutura concreta em cidade-núcleo (Cristal); serviço com impacto direto na mobilidade",
    },

    # 13 — Gripe / vacinação São Lourenço — REBAIXAR (saúde sensível)
    "899bb47685f7a8c58004147039ee940d434025bd": {
        **_skip("REBAIXAR", "Tema de saúde sensível envolvendo crianças; tratado com cautela como nota interna em vez de matéria, conforme guardrails"),
        "titulo_sultv": "São Lourenço do Sul reforça apelo por vacinação infantil contra a gripe",
        "tag_principal": "saude",
    },

    # 14 — Selo Prata Amigo da Vacina São Lourenço — REBAIXAR
    "4ceb630b463e5a73d241cc134657509620995c00": {
        **_skip("REBAIXAR", "Tema de vacinação infantil (saúde sensível) e resumo vazio; mesma cidade/tema do item anterior"),
        "titulo_sultv": "São Lourenço do Sul conquista selo prata 'Amigo da Vacina'",
        "tag_principal": "saude",
    },

    # 15 — Av Passo do Mendonça limpeza Cristal — REBAIXAR
    "804da2cbe08274dd604274d8db6acc48cc218fed": {
        **_skip("REBAIXAR", "Quota de 2 itens/cidade já preenchida por Cristal com pauta de maior impacto (calçamento); serviço menor de limpeza"),
        "titulo_sultv": "Avenida Passo do Mendonça recebe limpeza e reorganização em Cristal",
        "tag_principal": "infraestrutura",
    },

    # 16 — Move Motos crédito federal — REBAIXAR
    "db4f4e0f8cb7a01ce709a3fbb9067727512774c6": {
        **_skip("REBAIXAR", "Pauta nacional (linha de crédito federal) sem âncora regional no Sul do RS"),
        "titulo_sultv": "Governo federal prepara linha de crédito para motociclistas de aplicativos",
        "tag_principal": "economia",
    },

    # 17 — Enem 2026 prazo prorrogado — PUBLICAR
    "2bd93ab1af26abfdff1907281f46ca72b220cce5": {
        "tag_principal": "educacao",
        "titulo_sultv": "Inscrições do Enem 2026 são prorrogadas até esta sexta-feira (12)",
        "chamada_faixa": "Enem 2026: inscrição vai até sexta (12)",
        "subtitulo": "Novo prazo dá mais tempo aos estudantes; concluintes da rede pública também precisam confirmar a participação.",
        "lead": "As inscrições para o Exame Nacional do Ensino Médio (Enem) 2026 foram prorrogadas até esta sexta-feira (12), ampliando o prazo para que estudantes de todo o país garantam a participação na principal porta de entrada para o ensino superior.",
        "ganchos_3": [
            "Prazo de inscrição do Enem 2026 vai até sexta-feira (12)",
            "Concluintes da rede pública precisam confirmar a participação",
            "Enem é a principal porta de entrada para o ensino superior",
        ],
        "angulo_editorial": "Serviço de utilidade pública com prazo (urgência) e alto interesse para estudantes do Sul do RS. Embora a pauta seja nacional, o caráter de serviço com data próxima a torna útil para a audiência regional.",
        "fontes_complementares_sugeridas": ["Inep", "Ministério da Educação", "Página oficial do Enem"],
        "lead_materia_longa": "As inscrições para o Exame Nacional do Ensino Médio (Enem) 2026 foram prorrogadas até esta sexta-feira (12).",
        "post_instagram": {
            "caption": "Quem vai fazer o Enem 2026 tem até esta sexta-feira (12) para se inscrever — o prazo foi prorrogado. Concluintes da rede pública também precisam confirmar a participação. Não deixe para a última hora: garanta a sua vaga na principal porta de entrada para a faculdade.",
            "hashtags": ["#Enem2026", "#Educação", "#Vestibular", "#Estudantes", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Atenção, estudante: o prazo do Enem mudou.",
            "desenvolvimento_45s": "As inscrições para o Enem 2026 foram prorrogadas e agora vão até esta sexta-feira, dia 12. O novo prazo dá mais tempo para quem ainda não se inscreveu garantir a participação no exame, que é a principal porta de entrada para universidades públicas e privadas do país. Os estudantes concluintes da rede pública também precisam confirmar sua participação dentro do prazo. A orientação é não deixar para a última hora, já que a alta procura pode sobrecarregar o sistema nos dias finais.",
            "fechamento_8s": "Prazo final: sexta-feira, dia 12.",
            "cta_5s": "Compartilhe com quem vai fazer o Enem.",
            "trilha_sugerida": "instrumental dinâmico",
        },
        "tag_thumbnail": "Enem 2026",
        "briefing_visual": {
            "descricao_pt": "Estudante usando notebook para fazer inscrição online em ambiente de estudo, mãos no teclado, sem rosto identificável",
            "query_en": ["student online registration laptop", "studying notebook hands keyboard", "high school exam preparation"],
            "evitar": ["rosto identificável", "marcas", "texto", "logos"],
            "prompt_ia": "A student's hands typing on a laptop to complete an online registration at a study desk with notebooks, no face visible, daylight, no text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de utilidade pública com prazo iminente (sexta-feira); alto interesse para estudantes do Sul do RS",
    },

    # 18 — Audiência concessões/PPP ALERS — REBAIXAR
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": {
        **_skip("REBAIXAR", "Manifestação de parlamentares sobre concessões/privatizações tem teor político-partidário sensível; sem âncora nas cidades-núcleo"),
        "titulo_sultv": "Parlamentares debatem concessões e privatizações em audiência em Pelotas",
        "tag_principal": "politica",
    },

    # 19 — Funcriança ALERS — REBAIXAR
    "49348b06a39337d964518e54a7715142418ea220": {
        **_skip("REBAIXAR", "Pauta procedural sobre legislação de destinação de recursos; baixo apelo direto à audiência regional"),
        "titulo_sultv": "Campanha orienta sobre destinação de recursos ao Funcriança",
        "tag_principal": "politica",
    },

    # 20 — Frio fora de época — PUBLICAR
    "76f9e23500770062ad601dc315f86d2926860844": {
        "tag_principal": "clima",
        "titulo_sultv": "Frio fora de época derruba temperaturas e inverte o mapa do Brasil",
        "chamada_faixa": "Frio inverte o mapa: Sudeste e Nordeste gelados",
        "subtitulo": "Massa de ar frio fez cidades de Minas Gerais e da Bahia registrarem temperaturas mais baixas que municípios do Sul nos últimos dias.",
        "lead": "Uma massa de ar frio provocou uma inversão no mapa das temperaturas do Brasil nos últimos dias: cidades de Minas Gerais e até da Bahia registraram marcas mais baixas que muitos municípios da Região Sul, fenômeno que chama a atenção pela intensidade fora do comum.",
        "ganchos_3": [
            "Cidades de MG e BA mais frias que municípios do Sul",
            "Massa de ar frio inverte o mapa das temperaturas do país",
            "Frio fora do comum exige atenção no campo e nas cidades",
        ],
        "angulo_editorial": "Clima/tempo de interesse direto para o público rural e urbano do RS — frio afeta lavouras, rebanhos e a rotina das cidades. Pauta de serviço e curiosidade meteorológica, sem alarmismo.",
        "fontes_complementares_sugeridas": ["Estações meteorológicas do RS", "Inmet", "Emater/RS-Ascar"],
        "lead_materia_longa": "Uma massa de ar frio provocou uma inversão no mapa das temperaturas do Brasil nos últimos dias, com cidades de Minas Gerais e da Bahia mais frias que municípios da Região Sul.",
        "post_instagram": {
            "caption": "O mapa do frio virou de cabeça para baixo! Nos últimos dias, cidades de Minas Gerais e até da Bahia registraram temperaturas mais baixas que muitos municípios do Sul. A massa de ar frio mostra que o inverno chega forte — atenção redobrada com as lavouras, os animais e a saúde da família.",
            "hashtags": ["#Clima", "#Frio", "#Inverno", "#Tempo", "#RioGrandeDoSul", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "O mapa do frio virou de ponta-cabeça.",
            "desenvolvimento_45s": "Uma massa de ar frio provocou uma inversão curiosa no mapa das temperaturas do Brasil. Nos últimos dias, cidades de Minas Gerais e até da Bahia registraram marcas mais baixas que muitos municípios da Região Sul. O fenômeno chama a atenção pela intensidade fora do comum e serve de alerta: o frio exige cuidados com as lavouras sensíveis à geada, com o rebanho e com a saúde, especialmente de crianças e idosos. A orientação é acompanhar as previsões e se preparar para as madrugadas mais geladas.",
            "fechamento_8s": "Inverno chega com força no país.",
            "cta_5s": "Acompanhe o tempo no SulTV.",
            "trilha_sugerida": "instrumental atmosférico",
        },
        "tag_thumbnail": "Frio no Brasil",
        "briefing_visual": {
            "descricao_pt": "Campo rural ao amanhecer com geada branca sobre a vegetação no Sul do Brasil, neblina, sem pessoas",
            "query_en": ["frost field sunrise countryside", "frozen grass winter morning", "cold foggy rural landscape"],
            "evitar": ["pessoas identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A rural field at sunrise covered in white frost with mist over the vegetation in southern Brazil, cold winter morning, no people, no text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima de interesse direto ao público rural e urbano do RS; fenômeno concreto, pauta de serviço sem alarmismo",
    },

    # 21 — Produtores RS dívidas Senado — PUBLICAR
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "tag_principal": "agro",
        "titulo_sultv": "Produtores do RS acompanham com apreensão a votação da renegociação de dívidas no Senado",
        "chamada_faixa": "Produtores do RS temem travar a renegociação de dívidas",
        "subtitulo": "Setor teme ficar sem acesso ao crédito rural para a próxima safra caso a proposta não avance no Senado.",
        "lead": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas no Senado. O receio do setor é ficar sem acesso ao crédito rural necessário para custear a próxima safra caso a proposta não seja aprovada.",
        "ganchos_3": [
            "Produtores do RS temem que renegociação de dívidas não avance",
            "Acesso ao crédito da próxima safra está no centro da preocupação",
            "Setor pressiona por aprovação no Senado",
        ],
        "angulo_editorial": "Agro — tema central para o produtor gaúcho, atingido por estiagens e enchentes recentes. Crédito rural e endividamento são pauta de sobrevivência econômica. Tom institucional, sem partidarização.",
        "fontes_complementares_sugeridas": ["Senado Federal", "Farsul", "Federações e sindicatos rurais do RS", "Ministério da Agricultura"],
        "lead_materia_longa": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas no Senado, temendo ficar sem crédito para a próxima safra.",
        "post_instagram": {
            "caption": "A renegociação de dívidas dos produtores rurais está no centro das atenções do agro gaúcho. O setor, castigado por anos de estiagem e por enchentes, teme ficar sem acesso ao crédito rural da próxima safra caso a proposta não avance no Senado. É uma pauta de sobrevivência para o campo do RS.",
            "hashtags": ["#Agro", "#CréditoRural", "#RioGrandeDoSul", "#Produtores", "#Safra", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "O campo gaúcho está em alerta.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas no Senado. Depois de anos marcados por estiagens e pelas enchentes que atingiram o estado, muitos produtores estão endividados e temem ficar sem acesso ao crédito rural necessário para plantar a próxima safra. A aprovação da proposta é vista pelo setor como essencial para garantir fôlego financeiro e manter a atividade produtiva, que sustenta boa parte da economia do interior gaúcho.",
            "fechamento_8s": "Crédito rural é pauta de sobrevivência.",
            "cta_5s": "Acompanhe o agro no SulTV.",
            "trilha_sugerida": "instrumental sóbrio",
        },
        "tag_thumbnail": "Agro em alerta",
        "briefing_visual": {
            "descricao_pt": "Lavoura de soja ou colheitadeira em campo no Rio Grande do Sul ao entardecer, sem pessoas identificáveis",
            "query_en": ["soybean field harvest brazil", "combine harvester farm sunset", "rural farmland south brazil"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A wide view of a soybean field with a harvester working at sunset in southern Brazil, golden light, no readable text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agro de alto interesse para o produtor gaúcho; crédito rural e endividamento são pauta econômica central, tratada sem partidarização",
    },

    # 22 — Vinhos vencidos apreendidos (dup de 23) — REBAIXAR
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": {
        **_skip("REBAIXAR", "Mesmo eixo (fiscalização de alimentos impróprios no RS) do item selecionado para PUBLICAR; evita redundância"),
        "titulo_sultv": "Fiscalização apreende vinhos vencidos em estabelecimentos gaúchos",
        "tag_principal": "seguranca",
    },

    # 23 — 630 kg alimentos impróprios — PUBLICAR
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": {
        "tag_principal": "seguranca",
        "titulo_sultv": "Força-tarefa apreende 630 kg de alimentos impróprios para consumo no RS",
        "chamada_faixa": "Força-tarefa apreende 630 kg de alimentos impróprios",
        "subtitulo": "Ação de fiscalização recolheu carnes, ovos, amendoim, iogurtes e pães de cinco estabelecimentos gaúchos.",
        "lead": "Uma força-tarefa de fiscalização apreendeu 630 quilos de alimentos impróprios para consumo em cinco estabelecimentos do Rio Grande do Sul. Entre os produtos recolhidos estavam carnes, ovos, amendoim, iogurtes e pães fora das condições adequadas de armazenamento.",
        "ganchos_3": [
            "630 kg de alimentos impróprios apreendidos em cinco estabelecimentos",
            "Carnes, ovos, iogurtes e pães estavam fora das condições de consumo",
            "Fiscalização reforça a importância de checar a procedência dos alimentos",
        ],
        "angulo_editorial": "Segurança alimentar e defesa do consumidor no RS — pauta de utilidade que orienta o público a verificar validade e procedência. Fonte primária institucional (órgãos de fiscalização), tom informativo.",
        "fontes_complementares_sugeridas": ["Ministério Público do RS", "Vigilância Sanitária", "Procon-RS"],
        "lead_materia_longa": "Uma força-tarefa de fiscalização apreendeu 630 quilos de alimentos impróprios para consumo em cinco estabelecimentos do Rio Grande do Sul.",
        "post_instagram": {
            "caption": "Uma força-tarefa de fiscalização apreendeu 630 kg de alimentos impróprios para consumo em cinco estabelecimentos gaúchos — entre eles carnes, ovos, amendoim, iogurtes e pães fora das condições adequadas. Fica o alerta ao consumidor: confira sempre a validade, a procedência e as condições de armazenamento dos produtos.",
            "hashtags": ["#SegurançaAlimentar", "#Consumidor", "#RioGrandeDoSul", "#Fiscalização", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Alerta na mesa do consumidor gaúcho.",
            "desenvolvimento_45s": "Uma força-tarefa de fiscalização apreendeu 630 quilos de alimentos impróprios para consumo em cinco estabelecimentos do Rio Grande do Sul. Entre os produtos recolhidos estavam carnes, ovos, amendoim, iogurtes e pães armazenados fora das condições adequadas, o que representa risco à saúde de quem consome. O caso reforça a importância de o consumidor verificar a data de validade, a procedência e as condições de conservação dos alimentos na hora da compra, e de denunciar aos órgãos de fiscalização sempre que identificar irregularidades.",
            "fechamento_8s": "Atenção redobrada na hora das compras.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental informativo",
        },
        "tag_thumbnail": "Fiscalização no RS",
        "briefing_visual": {
            "descricao_pt": "Prateleira de mercado com produtos alimentícios sendo inspecionados, sem pessoas identificáveis, ambiente de comércio",
            "query_en": ["food safety inspection supermarket", "grocery shelf products", "health inspection food store"],
            "evitar": ["rostos identificáveis", "marcas reconhecíveis", "texto", "logos"],
            "prompt_ia": "A supermarket shelf with food products during a health inspection, neutral lighting, no people, no readable brand text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Segurança alimentar e defesa do consumidor no RS; fato concreto com número oficial, fonte institucional",
    },

    # 24 — Programa de Inovação UFSM — PUBLICAR (post_instagram)
    "35af87f20801bf0f5e4c5cd9db47c64c5f34d2fe": {
        "tag_principal": "inovacao",
        "titulo_sultv": "Programa de Inovação da UFSM promove novos encontros em junho",
        "chamada_faixa": "UFSM amplia diálogo sobre inovação em junho",
        "subtitulo": "Atividades da Proinova buscam fortalecer a cultura de inovação dentro da universidade gaúcha.",
        "lead": "O Programa de Inovação da Universidade Federal de Santa Maria (UFSM) realiza novos encontros em junho, com o objetivo de fortalecer o diálogo sobre inovação na comunidade acadêmica.",
        "ganchos_3": [
            "Proinova promove novos encontros sobre inovação em junho",
            "Atividades integram a programação de inovação da UFSM em 2026",
            "Iniciativa aproxima universidade, pesquisa e empreendedorismo",
        ],
        "angulo_editorial": "Inovação e ciência no RS — alinhado ao foco editorial em digitalização e inovação. Pauta leve de agenda, ideal para post de redes sociais. Santa Maria fora das cidades-núcleo, por isso formato post.",
        "fontes_complementares_sugeridas": ["Proinova/UFSM", "Pró-Reitoria de inovação da UFSM"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "A inovação está em movimento na UFSM! O Programa de Inovação da universidade (Proinova) promove novos encontros em junho para fortalecer o diálogo sobre o tema na comunidade acadêmica. É a ciência gaúcha aproximando pesquisa, empreendedorismo e tecnologia — combustível para o futuro do RS.",
            "hashtags": ["#UFSM", "#Inovação", "#Ciência", "#SantaMaria", "#RioGrandeDoSul", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Inovação em pauta na universidade.",
            "desenvolvimento_45s": "O Programa de Inovação da UFSM realiza novos encontros em junho, com o objetivo de fortalecer o diálogo sobre inovação na comunidade acadêmica. As atividades integram a programação da Proinova para 2026 e aproximam estudantes, pesquisadores e empreendedores em torno de temas que moldam o futuro, como tecnologia, transferência de conhecimento e novos negócios.",
            "fechamento_8s": "Ciência e inovação caminham juntas no RS.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental tecnológico leve",
        },
        "tag_thumbnail": "Inovação na UFSM",
        "briefing_visual": {
            "descricao_pt": "Auditório universitário com plateia em palestra sobre inovação, vista ampla, sem rostos identificáveis em close",
            "query_en": ["university lecture innovation event", "auditorium audience presentation", "tech conference students"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "A university auditorium with an audience attending an innovation talk, wide view, no identifiable faces, no text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Inovação e ciência alinhadas ao foco editorial; formato post por estar fora das cidades-núcleo",
    },

    # 25 — Desligamento energia UFSM — REBAIXAR
    "dcfd17474044e2827bca1fd7dde014fbebdee9dc": {
        **_skip("REBAIXAR", "Aviso de serviço interno (desligamento de energia em campus) de interesse restrito; fora das cidades-núcleo"),
        "titulo_sultv": "UFSM terá desligamento programado de energia no campus sede",
        "tag_principal": "infraestrutura",
    },

    # 26 — Jornada IFSul Venâncio — REBAIXAR
    "d9eba05c474ae5aba81ad2d59a44b4bb51d7284b": {
        **_skip("REBAIXAR", "Evento acadêmico local em cidade fora do núcleo (Venâncio Aires); baixo apelo regional Sul-RS"),
        "titulo_sultv": "Jornada Científica de Gestão e Negócios abre no IFSul Venâncio",
        "tag_principal": "evento",
    },

    # 27 — Corsan esgoto Venâncio — REBAIXAR
    "bb570de60f4f75d96f2226449b6fe1cc9e8633c9": {
        **_skip("REBAIXAR", "Serviço local pontual (atendimento de bairro) em cidade fora do núcleo"),
        "titulo_sultv": "Atendimento orienta moradores sobre obras de esgoto em Venâncio Aires",
        "tag_principal": "infraestrutura",
    },

    # 28 — Fenavinho corte Bento — REBAIXAR
    "9976d2bdb035b0316b7568fa8ac7a717457e6893": {
        **_skip("REBAIXAR", "Evento da Serra Gaúcha, distante das cidades-núcleo e da Costa Doce"),
        "titulo_sultv": "Fenavinho elege nova corte em Bento Gonçalves",
        "tag_principal": "evento",
    },

    # 29 — Furto celular ExpoBento — REBAIXAR
    "ff10e0171513712a3dceaea472f8e761a4ca8a43": {
        **_skip("REBAIXAR", "Ocorrência policial menor na Serra Gaúcha, região distante das cidades-núcleo"),
        "titulo_sultv": "Homem é preso por furto de celular na ExpoBento",
        "tag_principal": "crime",
    },
}


MATERIAS = {
    "ce87e878ba5048a6f108ee5191b838ce7ecb89df": """### Título ###
Bandas de Tapes e Sentinela do Sul recebem reconhecimento de maestro multicampeão mundial

### Artigo ###
O trabalho desenvolvido por bandas musicais de Tapes e Sentinela do Sul recebeu o reconhecimento de um maestro multicampeão mundial, dando projeção ao esforço cultural mantido por músicos da Região Centro-Sul do Rio Grande do Sul. O gesto representa uma forma de validação para grupos que, em cidades de pequeno porte, sustentam com dedicação a tradição das bandas e a formação musical de crianças e jovens. As bandas têm papel que vai além das apresentações em datas cívicas e festas comunitárias. Elas funcionam como verdadeiras escolas de música, oferecendo aos jovens das cidades do interior a oportunidade de aprender um instrumento, desenvolver disciplina e ter acesso à cultura, muitas vezes sem custo. Em municípios como Tapes e Sentinela do Sul, esse trabalho é mantido com recursos modestos e muita persistência de regentes e voluntários. O reconhecimento de um nome de prestígio internacional da regência coloca em evidência a qualidade do que é produzido longe dos grandes centros e reforça a importância de valorizar e apoiar essas iniciativas. Para as comunidades, o reconhecimento é motivo de orgulho e um estímulo para que as bandas continuem crescendo, atraindo novos integrantes e mantendo viva uma tradição que faz parte da identidade cultural da Costa Doce e de todo o Rio Grande do Sul. O episódio também serve de inspiração para outros grupos da região, mostrando que o talento cultivado no interior pode alcançar repercussão muito além das fronteiras locais.

### Legenda sugerida ###
Trabalho das bandas de Tapes e Sentinela do Sul ganha reconhecimento de maestro multicampeão mundial.

### Palavras-chave ###
Tapes, Sentinela do Sul, bandas musicais, cultura, música, Costa Doce, Região Centro-Sul, Rio Grande do Sul
""",

    "6cdde572c3587fe83a27846957bbd81b7db8ddbf": """### Título ###
Polícia Civil prende homem por descumprir prisão domiciliar em São Lourenço do Sul

### Artigo ###
A Polícia Civil prendeu, na tarde desta segunda-feira (8), um homem de 66 anos em São Lourenço do Sul por descumprir as condições da prisão domiciliar a que estava submetido por decisão da Justiça. A ação reforça o trabalho de monitoramento do cumprimento de medidas judiciais na região da Costa Doce. A prisão domiciliar é uma modalidade de cumprimento de pena ou de medida cautelar em que a pessoa permanece recolhida em sua residência, em vez de em uma unidade prisional. Quem está nessa condição precisa respeitar uma série de regras estabelecidas pela Justiça, como não se ausentar do endereço sem autorização, cumprir horários determinados e não cometer novas infrações. O descumprimento dessas condições é considerado uma violação que pode levar à revogação do benefício e à conversão da medida em prisão preventiva ou no recolhimento ao sistema prisional, como ocorreu neste caso. A atuação das forças de segurança no acompanhamento dessas medidas é fundamental para garantir que as decisões judiciais sejam efetivamente cumpridas, preservando tanto a aplicação da lei quanto a sensação de segurança da comunidade. A Polícia Civil orienta a população a colaborar com as investigações e a comunicar às autoridades situações que possam indicar o descumprimento de determinações judiciais. O caso segue os trâmites legais, e o detido ficará à disposição da Justiça.

### Legenda sugerida ###
Homem de 66 anos é preso em São Lourenço do Sul por descumprir as condições da prisão domiciliar.

### Palavras-chave ###
São Lourenço do Sul, prisão domiciliar, Polícia Civil, segurança, Costa Doce, medida judicial, Rio Grande do Sul
""",

    "6d583901d0b2623e718e91c071da59f2069c1522": """### Título ###
Barra do Ribeiro proíbe fogos de artifício com estampido por lei municipal

### Artigo ###
Barra do Ribeiro proíbe o uso de fogos de artifício com estampido em todo o território do município, conforme a Lei Municipal nº 2850/2025. A medida ganha relevância às vésperas das festas juninas, período tradicionalmente marcado pelo maior uso de artefatos pirotécnicos. A legislação acompanha um movimento que vem se espalhando por cidades de todo o país, voltado a reduzir o impacto do barulho dos fogos sobre quem é mais sensível a ruídos intensos. Entre os mais afetados estão os animais domésticos e silvestres, que entram em pânico com o estampido e podem fugir, se machucar ou sofrer crises de estresse. Pessoas autistas, idosos, bebês e veteranos de guerra também figuram entre os grupos que mais sofrem com os estouros. A proibição não impede a realização de festas e celebrações: o que a lei veda é o uso dos modelos que produzem barulho. No mercado já existem alternativas, como os fogos de efeito apenas visual, que iluminam o céu sem o ruído do estampido, garantindo a beleza do espetáculo sem o estresse para os mais vulneráveis. O descumprimento da norma pode resultar em penalidades previstas na legislação municipal. Para as autoridades, o cumprimento da regra depende sobretudo da conscientização da comunidade, especialmente em datas de grande circulação de fogos, como as festas juninas, a virada do ano e comemorações esportivas. A orientação aos moradores é dar preferência aos fogos silenciosos e respeitar a convivência com os vizinhos e seus animais.

### Legenda sugerida ###
Lei Municipal nº 2850/2025 proíbe fogos com estampido em Barra do Ribeiro; alternativa são os fogos silenciosos.

### Palavras-chave ###
Barra do Ribeiro, fogos de artifício, lei municipal, bem-estar animal, festas juninas, estampido, Costa Doce
""",

    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": """### Título ###
Cristal prepara Rua Camaquã para obras de calçamento

### Artigo ###
A Rua Camaquã, em Cristal, recebe os serviços de preparação que antecedem as obras de calçamento, etapa que faz parte do pacote de melhorias na infraestrutura urbana conduzido pela administração municipal. Os trabalhos iniciais são fundamentais para garantir a qualidade e a durabilidade da futura pavimentação. Antes de assentar o calçamento, é preciso preparar o leito da via, realizar a terraplenagem, ajustar o nivelamento e organizar o escoamento da água da chuva. Essa fase, muitas vezes pouco visível para quem passa pelo local, determina o desempenho da rua ao longo dos anos e evita problemas como buracos, acúmulo de água e desgaste precoce. Obras de pavimentação têm impacto direto no dia a dia da comunidade. Uma rua calçada melhora a mobilidade de moradores, pedestres e veículos, reduz a poeira no tempo seco e a lama nos períodos de chuva, facilita o acesso de serviços essenciais, como ambulâncias e coleta de lixo, e valoriza os imóveis do entorno. Em municípios de pequeno porte como Cristal, na região da Costa Doce, esse tipo de investimento costuma ser muito aguardado pelos moradores e representa um avanço importante na qualidade de vida urbana. A administração municipal deve informar o cronograma de execução da obra e eventuais interdições temporárias na via durante os trabalhos. A recomendação aos moradores é redobrar a atenção ao trafegar pela região enquanto durarem os serviços.

### Legenda sugerida ###
Rua Camaquã, em Cristal, recebe preparação que antecede as obras de calçamento, parte das melhorias urbanas do município.

### Palavras-chave ###
Cristal, Rua Camaquã, calçamento, pavimentação, infraestrutura urbana, obras, Costa Doce, mobilidade
""",

    "2bd93ab1af26abfdff1907281f46ca72b220cce5": """### Título ###
Inscrições do Enem 2026 são prorrogadas até esta sexta-feira (12)

### Artigo ###
As inscrições para o Exame Nacional do Ensino Médio (Enem) 2026 foram prorrogadas até esta sexta-feira (12), ampliando o prazo para que estudantes de todo o país garantam a participação na principal porta de entrada para o ensino superior. O novo prazo beneficia quem ainda não havia concluído o processo e dá fôlego extra a estudantes que estavam organizando a documentação ou a forma de pagamento da taxa. A inscrição é feita pela Página do Participante, no sistema oficial do exame, onde o candidato também escolhe a cidade de prova e indica eventuais necessidades de atendimento especializado. Um ponto que merece atenção é a situação dos estudantes concluintes da rede pública: mesmo aqueles que têm direito à isenção da taxa precisam confirmar a participação dentro do prazo, sob pena de perder a vaga no exame. A confirmação é uma etapa obrigatória e independe da isenção já concedida. O Enem é utilizado como critério de seleção por universidades públicas e privadas de todo o país, por meio de programas de acesso ao ensino superior e de financiamento estudantil, além de servir como porta de entrada para instituições no exterior. Por isso, a recomendação dos especialistas em educação é não deixar a inscrição para os últimos minutos, já que a alta procura pode sobrecarregar o sistema nos momentos finais do prazo. Os estudantes interessados devem reunir os documentos necessários e concluir o cadastro o quanto antes para assegurar a participação na edição deste ano.

### Legenda sugerida ###
Prazo de inscrição do Enem 2026 vai até sexta-feira (12); concluintes da rede pública também precisam confirmar participação.

### Palavras-chave ###
Enem 2026, inscrições, prazo prorrogado, ensino superior, educação, estudantes, vestibular, rede pública
""",

    "76f9e23500770062ad601dc315f86d2926860844": """### Título ###
Frio fora de época derruba temperaturas e inverte o mapa do Brasil

### Artigo ###
Uma massa de ar frio provocou uma inversão curiosa no mapa das temperaturas do Brasil nos últimos dias: cidades de Minas Gerais e até da Bahia registraram marcas mais baixas que muitos municípios da Região Sul, fenômeno que chama a atenção pela intensidade fora do comum para o período. A situação acontece quando uma massa de ar frio avança pelo interior do continente e atinge com força as áreas de maior altitude do Sudeste e do Centro-Oeste, enquanto o Sul fica sob a influência de um ar um pouco mais ameno em parte dos dias. Em regiões serranas de Minas Gerais e da Bahia, a combinação de altitude, céu limpo e baixa umidade favorece a perda de calor durante a noite, derrubando as temperaturas para perto ou abaixo dos registros gaúchos. Para o Rio Grande do Sul, episódios de frio intenso exigem cuidados em várias frentes. No campo, a geada é uma ameaça para lavouras sensíveis e para pastagens, podendo afetar a produção e a alimentação do rebanho. Os produtores costumam acompanhar de perto as previsões para proteger culturas e animais nas madrugadas mais frias. Nas cidades, o frio acentua os riscos à saúde, especialmente para crianças, idosos e pessoas com doenças respiratórias, e aumenta a procura por agasalhos e abrigo para a população em situação de rua. A orientação é acompanhar a evolução das condições do tempo, manter-se aquecido e redobrar a atenção com os mais vulneráveis enquanto durar a onda de frio.

### Legenda sugerida ###
Massa de ar frio inverte o mapa do país: cidades de MG e BA ficam mais frias que municípios do Sul.

### Palavras-chave ###
frio, clima, inverno, temperatura, geada, tempo, Rio Grande do Sul, massa de ar frio
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS acompanham com apreensão a votação da renegociação de dívidas no Senado

### Artigo ###
Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas no Senado. O receio do setor é ficar sem acesso ao crédito rural necessário para custear a próxima safra caso a proposta não seja aprovada, situação que afetaria diretamente a capacidade de plantar e de manter a atividade produtiva. O endividamento do campo gaúcho é resultado de uma sequência de adversidades enfrentadas nos últimos anos. Estiagens severas comprometeram safras inteiras, reduzindo a renda dos produtores justamente quando os custos de produção, com insumos, combustíveis e financiamentos, seguiam elevados. A isso se somaram as enchentes que atingiram o estado, agravando ainda mais a situação financeira de muitas famílias rurais. Para quem vive da terra, o crédito rural é a ferramenta que viabiliza o ciclo produtivo: é com ele que o produtor compra sementes, fertilizantes e defensivos, custeia a operação e aguarda a colheita para quitar os compromissos. Quando o acesso a esse crédito fica ameaçado, toda a cadeia sente o impacto, das revendas de insumos ao comércio das cidades do interior, que depende da renda gerada no campo. Por isso, a renegociação das dívidas é vista pelo setor como uma medida de fôlego e de sobrevivência, capaz de evitar que produtores fiquem inadimplentes e percam o acesso a novos financiamentos. As entidades de representação do agro têm reforçado a importância da aprovação da proposta, enquanto os produtores aguardam uma definição que consideram decisiva para o planejamento da próxima safra.

### Legenda sugerida ###
Setor rural do RS teme ficar sem crédito para a próxima safra caso a renegociação de dívidas não avance no Senado.

### Palavras-chave ###
agro, crédito rural, renegociação de dívidas, Senado, produtores, safra, Rio Grande do Sul, endividamento
""",

    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": """### Título ###
Força-tarefa apreende 630 kg de alimentos impróprios para consumo no RS

### Artigo ###
Uma força-tarefa de fiscalização apreendeu 630 quilos de alimentos impróprios para consumo em cinco estabelecimentos do Rio Grande do Sul. Entre os produtos recolhidos estavam carnes, ovos, amendoim, iogurtes e pães que se encontravam fora das condições adequadas de armazenamento e conservação, representando risco à saúde de quem viesse a consumi-los. A ação integra o trabalho permanente dos órgãos de fiscalização para proteger o consumidor e garantir que os alimentos colocados à venda atendam às normas sanitárias. Esse tipo de operação costuma verificar a validade dos produtos, as condições de refrigeração, a higiene dos ambientes e a procedência das mercadorias. Quando são encontradas irregularidades graves, os produtos são apreendidos e descartados, e os estabelecimentos podem sofrer sanções que vão de advertências e multas até a interdição. A apreensão reforça a importância de o consumidor adotar cuidados básicos na hora das compras. Verificar a data de validade, observar a integridade das embalagens, checar se os produtos refrigerados estão devidamente conservados e desconfiar de preços muito abaixo do mercado são atitudes que ajudam a evitar o consumo de alimentos estragados. Em caso de suspeita de irregularidade, o consumidor pode acionar os órgãos de defesa do consumidor e a vigilância sanitária, que têm o papel de fiscalizar e responsabilizar os estabelecimentos. A segurança alimentar é uma responsabilidade compartilhada entre o poder público, os comerciantes e os próprios consumidores, e ações como essa cumprem o papel de retirar de circulação produtos que poderiam causar danos à saúde da população.

### Legenda sugerida ###
Fiscalização recolhe 630 kg de alimentos impróprios em cinco estabelecimentos gaúchos; consumidor deve checar validade e procedência.

### Palavras-chave ###
segurança alimentar, fiscalização, alimentos impróprios, consumidor, vigilância sanitária, Rio Grande do Sul, apreensão
""",
}


def main():
    apr_path = ROOT / "state" / f"aprovadas_{HOJE}.json"
    pauta_path = ROOT / "state" / f"pauta_{HOJE}.json"
    materias_dir = ROOT / "state" / f"materias_{HOJE}"

    data = json.loads(apr_path.read_text(encoding="utf-8"))
    apr_list = data.get("aprovadas") or data.get("curadas") or data.get("itens") or []

    pauta = []
    pub_count = 0
    for item in apr_list:
        h = item["id_hash"]
        if h not in PAUTA_ANGULADA:
            print(f"[angular] sem angulação para {h} — bloqueando")
            angul = _skip("BLOQUEAR", "Sem angulação configurada — descartado pelo guardrail")
            angul["titulo_sultv"] = item.get("titulo", "")[:100]
        else:
            angul = PAUTA_ANGULADA[h]

        if angul["decisao_final"] == "PUBLICAR" and pub_count >= 10:
            angul = {**angul, "decisao_final": "REBAIXAR", "decisao_motivo": "Quota diária esgotada"}
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
    print(f"[angular] decisões:", Counter(p["decisao_final"] for p in pauta))
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
                print(f"[angular] AVISO: {p['id_hash']} PUBLICAR/materia_longa SEM texto")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
