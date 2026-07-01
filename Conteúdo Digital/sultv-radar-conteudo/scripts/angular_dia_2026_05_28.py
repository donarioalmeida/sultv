#!/usr/bin/env python3
"""
angular_dia_2026_05_28.py — angulação editorial Claude na sessão cowork.
Pauta de 2026-05-28: 14 aprovadas -> 6 PUBLICAR, 6 REBAIXAR, 2 BLOQUEAR.
1 matéria longa (Funrigs R$17,6M Polar - patrimônio histórico de Estrela).
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-05-28"


PAUTA_ANGULADA = {
    # 1. Arambaré cursos gratuitos — REBAIXAR (já publicado em edição anterior)
    "e370728cabf9868c99ea7f3a5323d444ac76d0dd": {
        "titulo_sultv": "Arambaré abre inscrições para cursos gratuitos de qualificação profissional",
        "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Já consta no histórico de publicações (edição anterior) — dedup, não republicar"
    },

    # 2. Funrigs aprova R$17,6 mi para Polar (Estrela) — PUBLICAR materia_longa
    "ce00dfb362b40b4a6243f148b3be176263ad51cf": {
        "titulo_sultv": "Funrigs aprova R$ 17,6 milhões para restaurar prédio da Polar, em Estrela",
        "subtitulo": "Conselho do Funrigs libera aporte para a primeira etapa da recuperação do complexo histórico do Vale do Taquari.",
        "lead": "O Conselho do Funrigs aprovou aporte de R$ 17,6 milhões para a primeira etapa da restauração do prédio da Polar, em Estrela. O recurso viabiliza a recuperação de um dos complexos históricos mais relevantes do Vale do Taquari e dá início a obras estruturantes no patrimônio gaúcho.",
        "ganchos_3": [
            "R$ 17,6 milhões liberados pelo Funrigs",
            "Primeira etapa da restauração da Polar",
            "Patrimônio histórico do Vale do Taquari preservado"
        ],
        "angulo_editorial": "Política cultural estadual com fato concreto e impacto regional — recuperação de patrimônio histórico do RS com peso simbólico e econômico para o Vale do Taquari. Pauta institucional, sem viés partidário.",
        "fontes_complementares_sugeridas": ["Grupo A Hora", "Sedac RS", "Prefeitura de Estrela", "Iphae"],
        "lead_materia_longa": "O Conselho do Funrigs aprovou aporte de R$ 17,6 milhões para a primeira etapa da restauração do prédio da Polar, em Estrela, marcando o início das obras de recuperação de um dos principais conjuntos históricos do Vale do Taquari.",
        "post_instagram": {
            "caption": "O Funrigs aprovou R$ 17,6 milhões para a primeira etapa da restauração do prédio da Polar, em Estrela. O recurso viabiliza a recuperação de um dos patrimônios históricos mais relevantes do Vale do Taquari.",
            "hashtags": ["#Estrela", "#ValeDoTaquari", "#Funrigs", "#PatrimônioHistórico", "#SulTV", "#RioGrandeDoSul"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "R$ 17,6 mi para restaurar a Polar.",
            "desenvolvimento_45s": "O Conselho do Funrigs aprovou aporte de R$ 17,6 milhões para a primeira etapa da restauração do prédio histórico da Polar, em Estrela. O recurso viabiliza a recuperação de um dos complexos mais simbólicos do Vale do Taquari e dá início a obras estruturantes no patrimônio gaúcho. A Polar é referência arquitetônica do município e a restauração busca preservar a identidade urbana, gerar atratividade turística e devolver à comunidade um espaço de uso público qualificado.",
            "fechamento_8s": "Patrimônio do Vale do Taquari recebe novo fôlego.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "institucional sóbria"
        },
        "tag_thumbnail": "Polar restaurada em Estrela",
        "briefing_visual": {
            "descricao_pt": "Fachada de prédio histórico de tijolos aparentes no estilo industrial gaúcho, arquitetura preservada, dia claro, sem pessoas",
            "query_en": ["historic brick brewery building", "industrial heritage architecture brazil", "old brewery facade restoration"],
            "evitar": ["pessoas com rosto visível", "marcas modernas", "texto legível", "logos"],
            "prompt_ia": "Historic red brick industrial building facade in southern Brazil, late 19th century brewery architecture, preserved heritage, daylight, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato concreto de política cultural estadual com impacto regional — patrimônio histórico do Vale do Taquari"
    },

    # 3. Cristal — Av. Passo do Mendonça — REBAIXAR (já publicado)
    "804da2cbe08274dd604274d8db6acc48cc218fed": {
        "titulo_sultv": "Avenida Passo do Mendonça recebe serviços de limpeza e reorganização",
        "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Já consta no histórico de publicações (edição anterior) — dedup, não republicar"
    },

    # 4. Pelotas — Vida Ativa Dia do Desafio — PUBLICAR post (cabeçalho retitulado)
    "bfc5030d4ae2052836f0cefe29a30caeb951d4ca": {
        "titulo_sultv": "Vida Ativa leva aula de ritmos e ginástica para o Dia do Desafio do Sesc, em Pelotas",
        "subtitulo": "Programa municipal reuniu participantes em atividade física aberta à população durante a ação nacional do Sesc.",
        "lead": "O programa Vida Ativa, da Prefeitura de Pelotas, levou aula de ritmos e ginástica para o Dia do Desafio do Sesc, mobilizando integrantes do projeto e a população em atividades físicas abertas. A ação reforça a política municipal de incentivo ao movimento e à saúde nas comunidades.",
        "ganchos_3": [
            "Vida Ativa no Dia do Desafio do Sesc",
            "Ritmos e ginástica abertos à população",
            "Saúde e movimento como política pública em Pelotas"
        ],
        "angulo_editorial": "Pauta de comunidade e serviço urbano em Pelotas — projeto municipal consolidado de atividade física conectado a uma ação nacional do Sesc. Pauta leve, positiva, alinhada à audiência da Costa Doce.",
        "fontes_complementares_sugeridas": ["Prefeitura de Pelotas", "Sesc RS"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "O programa Vida Ativa, da Prefeitura de Pelotas, levou aula de ritmos e ginástica para o Dia do Desafio do Sesc. Movimento, saúde e comunidade em ação nas ruas de Pelotas.",
            "hashtags": ["#Pelotas", "#VidaAtiva", "#DiaDoDesafio", "#Sesc", "#SulTV", "#CostaDoce"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Pelotas em movimento.",
            "desenvolvimento_45s": "O programa Vida Ativa, da Prefeitura de Pelotas, levou aula de ritmos e ginástica para o Dia do Desafio do Sesc, mobilizando integrantes do projeto e a população em atividades físicas abertas. A ação faz parte da campanha nacional do Sesc que estimula 15 minutos de atividade física no dia, e reforça a política municipal de saúde, lazer e bem-estar nos bairros.",
            "fechamento_8s": "Saúde começa no movimento de cada dia.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "energética leve"
        },
        "tag_thumbnail": "Pelotas no Dia do Desafio",
        "briefing_visual": {
            "descricao_pt": "Grupo praticando ginástica e ritmos ao ar livre em praça urbana, vista ampla sem rostos identificáveis, clima de comunidade",
            "query_en": ["outdoor group fitness class plaza", "community exercise public square", "people exercising city park"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "Wide shot of a community outdoor group exercise class in a city plaza in southern Brazil, sunny day, sense of movement and community, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Título scrapeado era cabeçalho de seção; re-titulado para o fato real — serviço municipal de Pelotas, item novo no histórico"
    },

    # 5. Cristal — ponto facultativo Corpus Christi — REBAIXAR (já publicado)
    "f627cc1c2a9732aca6846189a5bfb42f1535d1d3": {
        "titulo_sultv": "Decreto estabelece ponto facultativo nos dias 04 e 05 de junho em Cristal",
        "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Já consta no histórico de publicações (edição anterior) — dedup, não republicar"
    },

    # 6. INFORMAÇÕES AGROPECUÁRIAS (Emater) — BLOQUEAR (cabeçalho)
    "e914edb4101909198de490e19b4ee3ebeb063e57": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Título é cabeçalho de seção (informativo conjuntural Emater) e resumo é feed dump sem fato único ancorável"
    },

    # 7. Defesa Civil — alerta de granizo no Centro — PUBLICAR post
    "427ec442c2076f9cb003b8f1f25c15418f35e4cd": {
        "titulo_sultv": "Defesa Civil emite alerta para tempestades com granizo no Rio Grande do Sul",
        "subtitulo": "Aviso vale para diferentes regiões do estado; orientação é redobrar a atenção e proteger lavouras e animais.",
        "lead": "A Defesa Civil do Rio Grande do Sul emitiu alerta para tempestades acompanhadas de granizo em diferentes regiões do estado. O aviso pede atenção redobrada da população e dos produtores rurais, com risco de danos a lavouras, telhados e à rede elétrica.",
        "ganchos_3": [
            "Alerta de granizo em vigor no RS",
            "Risco para lavouras e estruturas rurais",
            "Defesa Civil orienta prevenção"
        ],
        "angulo_editorial": "Pauta de serviço e clima de interesse direto para a audiência rural e urbana do RS — alerta meteorológico oficial com utilidade pública imediata.",
        "fontes_complementares_sugeridas": ["Defesa Civil RS", "MetSul", "Inmet"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Atenção: a Defesa Civil emitiu alerta para tempestades com granizo em regiões do Rio Grande do Sul. Produtores e moradores devem redobrar os cuidados — proteja lavouras, animais e equipamentos.",
            "hashtags": ["#DefesaCivilRS", "#Granizo", "#ClimaRS", "#SulTV", "#AgroRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Alerta de granizo no RS.",
            "desenvolvimento_45s": "A Defesa Civil do Rio Grande do Sul emitiu alerta para tempestades com granizo em diferentes regiões do estado. O aviso pede atenção redobrada da população e dos produtores rurais, com risco de danos a lavouras, telhados e à rede elétrica. A orientação é evitar áreas abertas durante a tempestade, proteger animais e equipamentos e acompanhar as atualizações dos órgãos oficiais.",
            "fechamento_8s": "Redobre os cuidados nas próximas horas.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "tensão leve"
        },
        "tag_thumbnail": "Alerta de granizo no RS",
        "briefing_visual": {
            "descricao_pt": "Céu de tempestade carregado sobre campo agrícola no Rio Grande do Sul, nuvens escuras de granizo ao fundo, sem pessoas",
            "query_en": ["hail storm clouds farmland", "dark storm sky rural field", "severe weather over crops"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Dramatic dark storm clouds gathering over an agricultural field in southern Brazil, threatening hail weather, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Alerta meteorológico oficial com utilidade pública direta para audiência rural e urbana do RS"
    },

    # 8. Defesa Civil — segundo alerta de granizo (Vales) — REBAIXAR (duplicata)
    "a8bd7bb3fbb5c3f6eacb24ea4fafbf4f6fc0a52e": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Duplicata do alerta de granizo da Defesa Civil já contemplado em outro item PUBLICAR"
    },

    # 9. Fotos do Flickr (Farsul) — BLOQUEAR (cabeçalho)
    "54da86550dbad394c36708a7a9c2f7ad94d48e38": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Agregador de fotos do Flickr (Farsul, parceiro) — cabeçalho de seção, não é matéria"
    },

    # 10. Fetag-RS e Seduc — Plano Estadual de Educação — REBAIXAR (sem substância)
    "9fe4f7079b8f79b3731f3c1c677312cf5d10cf40": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Resumo apenas com 'Ver mais >' — sem substância textual suficiente para angulação"
    },

    # 11. Orgulho venâncio-airense (coluna Mateando) — REBAIXAR (opinião/coluna)
    "f1783f51e744f361c32418d39aaeaa08956ab3ca": {
        "titulo_sultv": "Venâncio Aires debate marca de lugar como estratégia de desenvolvimento",
        "subtitulo": "Painel do Gente & Negócios 2026, em parceria com o Grupo Folha do Mate, discutiu identidade e potencialidades do município.",
        "lead": "O projeto Gente & Negócios 2026, do Grupo Folha do Mate, estreou na AABB de Venâncio Aires com painel sobre marca de lugar como estratégia de desenvolvimento. O debate colocou em pauta a identidade venâncio-airense, ancorada no chimarrão e nas potencialidades do município gaúcho.",
        "ganchos_3": [
            "Gente & Negócios 2026 estreia em Venâncio",
            "Marca de lugar como estratégia de desenvolvimento",
            "Identidade ancorada no chimarrão"
        ],
        "angulo_editorial": "Economia regional e branding territorial — pauta de inovação no desenvolvimento municipal, conectada ao agro (chimarrão/erva-mate). Tema alinhado à agenda de inovação e marketing regional.",
        "fontes_complementares_sugeridas": ["Folha do Mate", "Grupo Folha do Mate", "ACI Venâncio Aires"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Venâncio Aires colocou em pauta a marca de lugar como estratégia de desenvolvimento. O painel do Gente & Negócios 2026, do Grupo Folha do Mate, discutiu a identidade ancorada no chimarrão e o que torna o município único.",
            "hashtags": ["#VenâncioAires", "#MarcaDeLugar", "#DesenvolvimentoRegional", "#Chimarrão", "#SulTV", "#AgroRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Venâncio discute identidade.",
            "desenvolvimento_45s": "O projeto Gente & Negócios 2026, do Grupo Folha do Mate, estreou em Venâncio Aires com painel sobre marca de lugar como estratégia de desenvolvimento. O debate colocou em pauta a identidade venâncio-airense, ancorada no chimarrão e nas potencialidades do município. A discussão sobre branding territorial ganha força no interior gaúcho como caminho para atrair investimento, turismo e valor para a produção local.",
            "fechamento_8s": "A identidade do território vira motor econômico.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental contemporânea"
        },
        "tag_thumbnail": "Marca de lugar em Venâncio",
        "briefing_visual": {
            "descricao_pt": "Cuia de chimarrão tradicional sobre mesa rústica de madeira em ambiente gaúcho típico, foco no objeto, sem pessoas",
            "query_en": ["traditional chimarrao mate gourd", "yerba mate cup wooden table", "brazilian mate culture still life"],
            "evitar": ["pessoas com rosto visível", "marcas comerciais legíveis", "texto", "logos"],
            "prompt_ia": "Traditional Brazilian chimarrão mate gourd with silver bombilla on a rustic wooden table, warm lighting, gaucho cultural atmosphere, no people, no text, editorial still life style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta de desenvolvimento regional e branding territorial — alinhada à agenda de inovação SulTV"
    },

    # 12. Uma identidade para Venâncio Aires — REBAIXAR (duplicata do #11)
    "1f93a5175ea47417d73fb50868a35ccf7f8f49ba": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Duplicata da matéria do Gente & Negócios 2026 já contemplada em outro item PUBLICAR"
    },

    # 13. Mutirão Bertolini em Bento Gonçalves — PUBLICAR post
    "dd77e763a82aa6956ae5d43649c6abc8bc31e87a": {
        "titulo_sultv": "Grupo Bertolini realiza mutirão de vagas de emprego em Bento Gonçalves",
        "subtitulo": "Ação ocorre no dia 28 de maio, na Uniftec, com oportunidades nas áreas de indústria e logística.",
        "lead": "O Grupo Bertolini promove mutirão presencial de vagas de emprego em Bento Gonçalves, nesta quinta-feira, 28 de maio, das 13h15 às 17h, na Uniftec. As oportunidades são em indústria e logística, em empresas do grupo na Serra Gaúcha.",
        "ganchos_3": [
            "Mutirão de empregos hoje em Bento Gonçalves",
            "Vagas em indústria e logística",
            "Ação acontece na Uniftec, das 13h15 às 17h"
        ],
        "angulo_editorial": "Pauta de serviço, economia e emprego no interior gaúcho — fato concreto e com urgência (hoje) para a audiência da Serra.",
        "fontes_complementares_sugeridas": ["Serranossa", "Grupo Bertolini", "Uniftec"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Mutirão de empregos hoje, 28 de maio, em Bento Gonçalves: o Grupo Bertolini oferece vagas em indústria e logística, das 13h15 às 17h, na Uniftec.",
            "hashtags": ["#BentoGonçalves", "#Emprego", "#SerraGaúcha", "#GrupoBertolini", "#SulTV", "#Vagas"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Mutirão de empregos em Bento.",
            "desenvolvimento_45s": "O Grupo Bertolini promove mutirão presencial de vagas de emprego em Bento Gonçalves, nesta quinta-feira, 28 de maio, das 13h15 às 17h, na Uniftec. As oportunidades são em indústria e logística, em empresas do grupo na Serra Gaúcha. A ação concentra entrevistas e seleção no mesmo local, encurtando o processo entre o candidato e a contratação. É uma boa janela para quem busca recolocação no setor industrial gaúcho.",
            "fechamento_8s": "Hoje, das 13h15 às 17h, na Uniftec.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "ritmo otimista"
        },
        "tag_thumbnail": "Mutirão de empregos em Bento",
        "briefing_visual": {
            "descricao_pt": "Sala ampla de seleção de empregos em ambiente corporativo, mesas e cadeiras organizadas, ambiente neutro, sem rostos identificáveis",
            "query_en": ["job fair hiring event hall", "interview room corporate setting", "career recruitment empty hall"],
            "evitar": ["rostos identificáveis", "marcas comerciais legíveis", "texto", "logos"],
            "prompt_ia": "Wide view of a job fair recruitment hall with neatly arranged tables and chairs ready for interviews, modern corporate setting, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta de serviço com urgência (hoje) — emprego e economia da Serra Gaúcha"
    },

    # 14. Mutirão Tacchini em Bento Gonçalves — PUBLICAR post
    "0e8e5f39bb7355780b810da22de3a7c48eb976b6": {
        "titulo_sultv": "Tacchini Saúde realiza mutirão para preencher 50 vagas em Bento Gonçalves",
        "subtitulo": "Seleção ocorre em 10 de junho, no Hospital Tacchini, com oportunidades para diferentes áreas da saúde.",
        "lead": "O Tacchini Saúde realizará, no dia 10 de junho, mutirão de entrevistas para preencher 50 vagas em Bento Gonçalves. A ação ocorre das 12h às 17h, no Hospital Tacchini, com acesso pela Rua Saldanha Marinho.",
        "ganchos_3": [
            "Tacchini abre 50 vagas em Bento Gonçalves",
            "Mutirão de entrevistas em 10 de junho",
            "Seleção no próprio Hospital Tacchini"
        ],
        "angulo_editorial": "Pauta de serviço e economia da Serra Gaúcha — geração de emprego no setor de saúde com agenda definida. Útil para a audiência regional.",
        "fontes_complementares_sugeridas": ["Serranossa", "Tacchini Saúde", "Hospital Tacchini"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Tacchini Saúde abre 50 vagas em Bento Gonçalves: mutirão de entrevistas no dia 10 de junho, das 12h às 17h, no Hospital Tacchini. Acesso pela Rua Saldanha Marinho.",
            "hashtags": ["#BentoGonçalves", "#TacchiniSaúde", "#Emprego", "#SerraGaúcha", "#SulTV", "#Saúde"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "50 vagas no Tacchini.",
            "desenvolvimento_45s": "O Tacchini Saúde realizará no dia 10 de junho um mutirão de entrevistas para preencher 50 vagas em Bento Gonçalves. A ação ocorre das 12h às 17h, no Hospital Tacchini, com acesso pela Rua Saldanha Marinho. O processo seletivo concentra triagem e entrevistas no mesmo local, acelerando o caminho entre o candidato e a contratação. É uma janela importante para quem busca oportunidade no setor de saúde da Serra.",
            "fechamento_8s": "Dia 10 de junho, das 12h às 17h.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "institucional confiante"
        },
        "tag_thumbnail": "Tacchini abre 50 vagas",
        "briefing_visual": {
            "descricao_pt": "Corredor de hospital moderno e organizado em ambiente clínico, luz natural, foco em arquitetura e ambiente profissional, sem rostos identificáveis",
            "query_en": ["modern hospital corridor", "clean clinical interior", "healthcare facility hallway"],
            "evitar": ["rostos identificáveis", "pacientes", "marcas comerciais", "texto", "logos"],
            "prompt_ia": "Wide view of a clean, modern hospital corridor with natural light, professional healthcare environment, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Geração de emprego no setor de saúde da Serra — pauta de serviço com agenda definida"
    },
}


MATERIAS = {
    "ce00dfb362b40b4a6243f148b3be176263ad51cf": """### Título ###
Funrigs aprova R$ 17,6 milhões para restaurar prédio histórico da Polar em Estrela

### Artigo ###
O Conselho do Funrigs aprovou aporte de R$ 17,6 milhões para a primeira etapa da restauração do prédio da Polar, em Estrela, dando início a uma das obras de recuperação de patrimônio histórico mais relevantes do Vale do Taquari nos últimos anos. O recurso viabiliza as ações estruturantes da intervenção em um conjunto arquitetônico considerado símbolo da identidade industrial do município. A Polar é um dos edifícios mais lembrados da paisagem urbana de Estrela e carrega a memória de uma fase de expansão econômica e cultural da região. Sua preservação está no centro do debate sobre como o Rio Grande do Sul lida com o estoque de imóveis históricos que ainda resistem ao tempo, especialmente em cidades médias do interior, onde o tecido urbano original costuma ser ameaçado por demandas de modernização. O Funrigs, fundo estadual que financia projetos de proteção e revitalização do patrimônio cultural gaúcho, atua exatamente nessa fronteira: garantir que recursos públicos cheguem a obras de grande envergadura que não se sustentariam apenas com investimento privado ou municipal. A liberação dos R$ 17,6 milhões para a Polar consolida Estrela como destino prioritário dessa política nesta safra de aportes. A primeira etapa da restauração concentra ações de consolidação estrutural e recuperação dos elementos arquitetônicos mais sensíveis, preparando o conjunto para usos públicos e culturais nas fases seguintes. A expectativa do município e do conselho gestor é que o complexo restaurado se torne âncora de novos circuitos turísticos no Vale do Taquari, gerando movimento econômico, atratividade para visitantes e qualificação do espaço urbano. A iniciativa também sinaliza uma agenda mais ampla de retomada de obras em patrimônios históricos do Rio Grande do Sul, em diálogo com a necessidade de respostas estruturais para regiões duramente impactadas por eventos climáticos extremos nos últimos anos. Preservar, nesse contexto, é também planejar o futuro das cidades.

### Legenda sugerida ###
Funrigs libera R$ 17,6 milhões para a primeira etapa de restauração do prédio histórico da Polar, em Estrela, no Vale do Taquari.

### Palavras-chave ###
Funrigs, Polar Estrela, Vale do Taquari, patrimônio histórico, restauração, Rio Grande do Sul, política cultural, Sedac RS
""",
}


def main():
    apr_path = ROOT / "state" / f"aprovadas_{HOJE}.json"
    pauta_path = ROOT / "state" / f"pauta_{HOJE}.json"
    materias_dir = ROOT / "state" / f"materias_{HOJE}"

    data = json.loads(apr_path.read_text(encoding="utf-8"))
    apr_list = data.get("aprovadas") or data.get("curadas") or []

    pauta = []
    pub_count = 0
    for item in apr_list:
        h = item["id_hash"]
        if h not in PAUTA_ANGULADA:
            print(f"[angular] sem angulação para {h} — bloqueando")
            angul = {
                "titulo_sultv": item.get("titulo", "")[:100],
                "subtitulo": "", "lead": "", "ganchos_3": [],
                "angulo_editorial": "", "fontes_complementares_sugeridas": [],
                "lead_materia_longa": "",
                "post_instagram": {}, "roteiro_short_60s": {},
                "tag_thumbnail": "",
                "decisao_final": "BLOQUEAR",
                "decisao_motivo": "Sem angulação configurada — descartado pelo guardrail",
            }
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

    from collections import Counter
    print(f"[angular] decisoes:", Counter(p["decisao_final"] for p in pauta))

    materias_dir.mkdir(exist_ok=True)
    nwrite = 0
    for p in pauta:
        if p["decisao_final"] == "PUBLICAR" and p["formato_sugerido"] == "materia_longa":
            corpo = MATERIAS.get(p["id_hash"])
            if corpo:
                f = materias_dir / f"{p['id_hash']}.md"
                f.write_text(corpo, encoding="utf-8")
                nwrite += 1
                print(f"[angular] materia -> {f.name} ({len(corpo)} chars)")
            else:
                print(f"[angular] AVISO: {p['id_hash']} eh PUBLICAR/materia_longa mas sem texto")
    print(f"[angular] {nwrite} materias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
