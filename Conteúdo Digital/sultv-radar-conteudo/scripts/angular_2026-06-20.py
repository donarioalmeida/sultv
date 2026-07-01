#!/usr/bin/env python3
"""
angular_2026-06-20.py — angulação editorial + redação (cowork-faz-tudo).
Decisões editoriais Claude na sessão para a pauta de 2026-06-20.
Regra 12 INEGOCIÁVEL: nenhum texto menciona veículos/portais/rádios/jornais.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-20"


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

    # IDX 0 — Acidente 3 veículos centro Camaquã (Camaquã, trânsito) — PUBLICAR
    "84295932f62a2688fa4ffe074cca173580476e3c": {
        "titulo_sultv": "Acidente entre três veículos é registrado no centro de Camaquã nesta sexta-feira",
        "chamada_faixa": "Acidente entre três veículos em Camaquã",
        "subtitulo": "Colisão mobilizou a Divisão Municipal de Trânsito na tarde desta sexta-feira (19), no centro da cidade.",
        "lead": "Um acidente envolvendo três veículos foi registrado na tarde desta sexta-feira (19) no centro de Camaquã, na região da Costa Doce. A Divisão Municipal de Trânsito foi acionada para atender a ocorrência e organizar o fluxo no local.",
        "ganchos_3": [
            "Acidente envolveu três veículos no centro de Camaquã",
            "Divisão Municipal de Trânsito foi acionada para a ocorrência",
            "Colisão aconteceu na tarde de sexta-feira (19)"
        ],
        "angulo_editorial": "Trânsito urbano em cidade-núcleo (Camaquã/Costa Doce). Fato concreto, recente, sem vítima identificada — pauta de serviço e alerta de segurança viária. Sem viés partidário, sem dramalhão.",
        "fontes_complementares_sugeridas": ["Divisão Municipal de Trânsito de Camaquã", "Prefeitura de Camaquã"],
        "lead_materia_longa": "Um acidente envolvendo três veículos foi registrado na tarde desta sexta-feira (19) no centro de Camaquã, na região da Costa Doce.",
        "post_instagram": {
            "caption": "Atenção, Camaquã. Um acidente envolvendo três veículos foi registrado na tarde desta sexta-feira (19) no centro da cidade. A Divisão Municipal de Trânsito foi acionada para atender a ocorrência e organizar o fluxo. Episódios assim reforçam a importância de redobrar a atenção ao volante, respeitar a sinalização e manter distância segura, especialmente nas vias movimentadas do centro.",
            "hashtags": ["#Camaquã", "#CostaDoce", "#Trânsito", "#SegurançaViária", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Acidente no centro de Camaquã.",
            "desenvolvimento_45s": "Um acidente envolvendo três veículos foi registrado na tarde desta sexta-feira no centro de Camaquã. A Divisão Municipal de Trânsito foi acionada para atender a ocorrência e organizar o fluxo no local. Casos como esse reforçam a importância de redobrar a atenção ao volante, respeitar a sinalização e manter a distância segura, principalmente nas vias mais movimentadas da cidade.",
            "fechamento_8s": "Atenção redobrada no trânsito da Costa Doce.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental tenso leve"
        },
        "tag_thumbnail": "Acidente no centro de Camaquã",
        "briefing_visual": {
            "descricao_pt": "Cruzamento urbano no centro de uma cidade pequena do interior do Rio Grande do Sul, asfalto e sinalização de trânsito, sem vítimas e sem rostos identificáveis",
            "query_en": ["urban street intersection brazil", "traffic city center small town", "road signs crossroad"],
            "evitar": ["vítimas", "sangue", "placas de carro legíveis", "rostos identificáveis", "logos", "texto"],
            "prompt_ia": "Urban street intersection in a small southern Brazil town center, asphalt and traffic signage, daytime, no people, no vehicles damaged, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Trânsito concreto e recente em cidade-núcleo (Camaquã), sem vítima identificada — pauta de serviço com fonte institucional"
    },

    # IDX 1 — Sindicato Trabalhadores Rurais de Camaquã 60 anos (Camaquã, comunidade/agro) — PUBLICAR
    "05cf0b995ff0f7c7b8d97071e5b4ab7de4361923": {
        "titulo_sultv": "Sindicato dos Trabalhadores Rurais de Camaquã completa 60 anos e recebe homenagem da Câmara",
        "chamada_faixa": "Sindicato rural de Camaquã faz 60 anos",
        "subtitulo": "Entidade que representa o produtor rural da Costa Doce foi homenageada pela Câmara de Vereadores ao marcar seis décadas de atuação.",
        "lead": "O Sindicato dos Trabalhadores Rurais de Camaquã completou 60 anos de atuação e foi homenageado pela Câmara de Vereadores do município, na região da Costa Doce. A entidade é uma das principais representantes do produtor rural da cidade, referência histórica em uma das maiores regiões produtoras de arroz do Rio Grande do Sul.",
        "ganchos_3": [
            "Sindicato dos Trabalhadores Rurais de Camaquã completa 60 anos",
            "Câmara de Vereadores presta homenagem à entidade",
            "Entidade é referência para o produtor rural da Costa Doce"
        ],
        "angulo_editorial": "Comunidade e agro em cidade-núcleo (Camaquã), polo produtor de arroz. Pauta institucional positiva, fonte primária (Câmara de Vereadores), forte conexão com a audiência rural e urbana da Costa Doce. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Câmara de Vereadores de Camaquã", "Sindicato dos Trabalhadores Rurais de Camaquã"],
        "lead_materia_longa": "O Sindicato dos Trabalhadores Rurais de Camaquã completou 60 anos de atuação e foi homenageado pela Câmara de Vereadores do município, na região da Costa Doce.",
        "post_instagram": {
            "caption": "São 60 anos ao lado de quem produz. O Sindicato dos Trabalhadores Rurais de Camaquã chega às seis décadas de atuação e foi homenageado pela Câmara de Vereadores do município. A entidade é uma das principais vozes do produtor rural da Costa Doce, em uma das maiores regiões produtoras de arroz do Rio Grande do Sul. Seis décadas de história ao lado do homem do campo.",
            "hashtags": ["#Camaquã", "#CostaDoce", "#AgroRS", "#ProdutorRural", "#Arroz", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Seis décadas ao lado do produtor.",
            "desenvolvimento_45s": "O Sindicato dos Trabalhadores Rurais de Camaquã completou 60 anos de atuação e recebeu homenagem da Câmara de Vereadores. A entidade é uma das principais representantes do produtor rural da cidade, em uma das maiores regiões produtoras de arroz do Rio Grande do Sul. São seis décadas defendendo os interesses do campo e fortalecendo a agricultura familiar e empresarial da Costa Doce.",
            "fechamento_8s": "Camaquã celebra a história do campo.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental emotivo"
        },
        "tag_thumbnail": "Sindicato rural de Camaquã, 60 anos",
        "briefing_visual": {
            "descricao_pt": "Lavoura de arroz alagada no Sul do Rio Grande do Sul ao amanhecer, vista ampla, sem pessoas, representando a tradição rural de Camaquã",
            "query_en": ["rice paddy field brazil aerial", "flooded rice field sunrise", "agriculture landscape south brazil"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Wide view of a flooded rice paddy at sunrise in southern Brazil, golden light reflecting on the water, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Marco institucional do agro em cidade-núcleo (Camaquã), fonte primária (Câmara) — forte apelo para a audiência rural e urbana da Costa Doce"
    },

    # IDX 2 — Bandas de Tapes e Sentinela do Sul reconhecidas por maestro (Tapes, cultura) — PUBLICAR
    "4d84d73fbe84b729ff39aaf941f9080399410131": {
        "titulo_sultv": "Bandas de Tapes e Sentinela do Sul recebem reconhecimento de maestro campeão mundial",
        "chamada_faixa": "Bandas de Tapes ganham reconhecimento",
        "subtitulo": "Corporações musicais da Costa Doce tiveram o desempenho elogiado pelo maestro campeão mundial Rogério Wanderley Brito.",
        "lead": "As bandas municipais de Tapes e Sentinela do Sul, na região da Costa Doce, receberam o reconhecimento do maestro campeão mundial Rogério Wanderley Brito pelo desempenho artístico. O resultado coroa um trabalho de formação musical que vem se destacando em duas cidades-núcleo do Sul do Rio Grande do Sul.",
        "ganchos_3": [
            "Bandas de Tapes e Sentinela do Sul são reconhecidas por maestro",
            "Elogio veio do maestro campeão mundial Rogério Wanderley Brito",
            "Trabalho artístico valoriza a cultura da Costa Doce"
        ],
        "angulo_editorial": "Cultura em cidades-núcleo (Tapes e Sentinela do Sul). Pauta positiva que valoriza a formação musical local, com referência nominal a autoridade artística. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Tapes", "Prefeitura de Sentinela do Sul"],
        "lead_materia_longa": "As bandas municipais de Tapes e Sentinela do Sul, na região da Costa Doce, receberam o reconhecimento do maestro campeão mundial Rogério Wanderley Brito pelo desempenho artístico.",
        "post_instagram": {
            "caption": "Talento da Costa Doce reconhecido lá fora. As bandas municipais de Tapes e Sentinela do Sul receberam o elogio do maestro campeão mundial Rogério Wanderley Brito pelo desempenho artístico. É a prova de que o trabalho de formação musical feito no interior do Sul do Rio Grande do Sul tem qualidade de sobra. Orgulho para as duas cidades e para quem acredita na cultura local.",
            "hashtags": ["#Tapes", "#SentineladoSul", "#CostaDoce", "#Cultura", "#Música", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Talento da Costa Doce reconhecido.",
            "desenvolvimento_45s": "As bandas municipais de Tapes e Sentinela do Sul receberam o reconhecimento do maestro campeão mundial Rogério Wanderley Brito pelo desempenho artístico. O resultado coroa um trabalho de formação musical que vem se destacando em duas cidades da Costa Doce e valoriza o esforço de músicos, professores e famílias que mantêm viva a tradição das bandas no interior gaúcho.",
            "fechamento_8s": "A cultura local em destaque.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental orquestral"
        },
        "tag_thumbnail": "Bandas de Tapes reconhecidas",
        "briefing_visual": {
            "descricao_pt": "Banda municipal com instrumentos de sopro em apresentação ao ar livre no interior do Rio Grande do Sul, foco nos instrumentos, sem rostos identificáveis",
            "query_en": ["brass band instruments outdoor", "marching band trumpet", "town band performance"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto", "uniformes legíveis"],
            "prompt_ia": "Municipal brass band performing outdoors in a small Brazilian town, focus on wind instruments and music stands, warm light, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura positiva em duas cidades-núcleo (Tapes e Sentinela do Sul), com reconhecimento de autoridade artística nomeada"
    },

    # IDX 3 — Cerro Grande do Sul cursos gratuitos com bolsa (segunda camada, serviço) — PUBLICAR
    "dd7df59af3392ccb9037aa29aab34324cac79b5c": {
        "cidade": "Cerro Grande do Sul",
        "titulo_sultv": "Cerro Grande do Sul abre inscrições para cursos gratuitos de qualificação com bolsa permanência",
        "chamada_faixa": "Cerro Grande do Sul abre cursos gratuitos",
        "subtitulo": "Prefeitura oferece duas formações gratuitas de qualificação profissional com auxílio bolsa permanência para os participantes.",
        "lead": "A Prefeitura de Cerro Grande do Sul, na região da Costa Doce, abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes. A iniciativa, conduzida pela Secretaria Municipal do Trabalho, Cidadania e Assistência Social, busca ampliar a empregabilidade e a renda da população local.",
        "ganchos_3": [
            "Cerro Grande do Sul abre cursos gratuitos de qualificação",
            "Participantes recebem bolsa permanência",
            "Iniciativa amplia empregabilidade e renda no município"
        ],
        "angulo_editorial": "Serviço público de utilidade imediata na Costa Doce ampliada. Pauta de trabalho, renda e qualificação, com fonte primária (prefeitura). Tom orientativo e útil. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cerro Grande do Sul", "Secretaria Municipal do Trabalho, Cidadania e Assistência Social"],
        "lead_materia_longa": "A Prefeitura de Cerro Grande do Sul, na região da Costa Doce, abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes.",
        "post_instagram": {
            "caption": "Chance de qualificação em Cerro Grande do Sul. A Prefeitura abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes. A ação é da Secretaria Municipal do Trabalho, Cidadania e Assistência Social e busca ampliar a empregabilidade e a renda da população. Quem busca capacitação tem aqui uma boa oportunidade na Costa Doce.",
            "hashtags": ["#CerroGrandedoSul", "#CostaDoce", "#Qualificação", "#Trabalho", "#Cursos", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cursos gratuitos em Cerro Grande do Sul.",
            "desenvolvimento_45s": "A Prefeitura de Cerro Grande do Sul abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes. A iniciativa é da Secretaria Municipal do Trabalho, Cidadania e Assistência Social e busca ampliar a empregabilidade e a renda da população. Para quem procura capacitação e novas oportunidades, é uma chance concreta de avançar na carreira sem custo.",
            "fechamento_8s": "Oportunidade de renda na Costa Doce.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental otimista"
        },
        "tag_thumbnail": "Cursos gratuitos em Cerro Grande do Sul",
        "briefing_visual": {
            "descricao_pt": "Sala de aula de curso profissionalizante com mesas, cadeiras e materiais, ambiente vazio e organizado, no interior do Rio Grande do Sul",
            "query_en": ["vocational training classroom", "empty workshop classroom", "professional course room"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Empty vocational training classroom with desks and learning materials in a small Brazilian town, natural light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de utilidade pública (qualificação + bolsa) na Costa Doce ampliada, fonte primária — útil para trabalho e renda"
    },

    # IDX 4 — Arambaré nota técnica poda/arborização (Arambaré, serviço) — PUBLICAR
    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": {
        "titulo_sultv": "Arambaré publica nota técnica com orientações sobre poda de árvores e arborização urbana",
        "chamada_faixa": "Arambaré orienta sobre poda de árvores",
        "subtitulo": "Prefeitura divulga diretrizes para o manejo correto da arborização urbana e o período mais indicado para a poda no município.",
        "lead": "A Prefeitura de Arambaré publicou em 18 de junho uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município, na região da Costa Doce. O documento orienta moradores e responsáveis por imóveis sobre os procedimentos corretos para a conservação das árvores e a segurança da cidade.",
        "ganchos_3": [
            "Arambaré divulga nota técnica sobre poda de árvores",
            "Inverno é o período mais indicado para a poda",
            "Orientações valem para a arborização urbana de toda a cidade"
        ],
        "angulo_editorial": "Serviço público de utilidade imediata em cidade-núcleo (Arambaré) — meio ambiente urbano e segurança, com fonte institucional (prefeitura). Tom orientativo, sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Arambaré", "Secretaria de Meio Ambiente de Arambaré"],
        "lead_materia_longa": "A Prefeitura de Arambaré publicou em 18 de junho uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município, na região da Costa Doce.",
        "post_instagram": {
            "caption": "Atenção, Arambaré. A Prefeitura publicou uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores. O inverno é justamente o período mais indicado para a poda, época em que muitas espécies entram em dormência e respondem melhor à intervenção. Manejo correto significa árvores mais saudáveis, menos risco de queda de galhos e mais segurança na cidade.",
            "hashtags": ["#Arambaré", "#CostaDoce", "#MeioAmbiente", "#PodaDeÁrvores", "#ArborizaçãoUrbana", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Época certa de podar as árvores.",
            "desenvolvimento_45s": "A Prefeitura de Arambaré publicou uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores. O inverno é o período mais indicado para a poda, época em que muitas espécies respondem melhor à intervenção, com menos estresse para a planta. Fazer a poda de forma técnica e na estação certa reduz riscos, prolonga a vida das árvores e evita problemas como a queda de galhos sobre a fiação e as calçadas.",
            "fechamento_8s": "Cidade mais verde e mais segura.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Poda de árvores em Arambaré",
        "briefing_visual": {
            "descricao_pt": "Rua arborizada de cidade pequena do interior do Rio Grande do Sul, árvores nas calçadas no inverno, sem pessoas e sem rostos identificáveis",
            "query_en": ["tree lined street small town", "urban trees sidewalk winter", "city street trees brazil"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Tree-lined residential street in a small southern Brazil town during winter, bare and leafy trees along the sidewalk, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público de utilidade imediata em cidade-núcleo (Arambaré), fonte institucional, fato recente (18/06)"
    },

    # IDX 13 — Cristal Rua Camaquã calçamento (Cristal, infra/serviço) — PUBLICAR
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": {
        "titulo_sultv": "Rua Camaquã recebe preparação para obras de calçamento em Cristal",
        "chamada_faixa": "Cristal prepara calçamento da Rua Camaquã",
        "subtitulo": "Município inicia os trabalhos preparatórios para a pavimentação de mais uma via, ampliando a infraestrutura urbana.",
        "lead": "A Prefeitura de Cristal, na região da Costa Doce, iniciou os trabalhos de preparação da Rua Camaquã para as obras de calçamento. A intervenção integra o conjunto de melhorias de infraestrutura urbana do município e antecede a pavimentação da via.",
        "ganchos_3": [
            "Rua Camaquã recebe preparação para calçamento em Cristal",
            "Obras ampliam a infraestrutura urbana do município",
            "Intervenção antecede a pavimentação da via"
        ],
        "angulo_editorial": "Infraestrutura urbana em cidade-núcleo (Cristal). Pauta de serviço e melhoria concreta para a comunidade, com fonte primária (prefeitura). Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria de Obras de Cristal"],
        "lead_materia_longa": "A Prefeitura de Cristal, na região da Costa Doce, iniciou os trabalhos de preparação da Rua Camaquã para as obras de calçamento.",
        "post_instagram": {
            "caption": "Mais infraestrutura para Cristal. A Prefeitura iniciou os trabalhos de preparação da Rua Camaquã para as obras de calçamento. A intervenção antecede a pavimentação da via e integra o conjunto de melhorias urbanas do município. Ruas calçadas significam mais mobilidade, menos poeira e barro e mais qualidade de vida para os moradores da Costa Doce.",
            "hashtags": ["#Cristal", "#CostaDoce", "#Infraestrutura", "#Calçamento", "#Obras", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Mais uma rua calçada em Cristal.",
            "desenvolvimento_45s": "A Prefeitura de Cristal iniciou os trabalhos de preparação da Rua Camaquã para as obras de calçamento. A intervenção antecede a pavimentação da via e integra o conjunto de melhorias de infraestrutura urbana do município. Para os moradores, calçamento significa mais mobilidade, menos poeira e barro nos dias de chuva e mais valorização do bairro.",
            "fechamento_8s": "Infraestrutura que muda o dia a dia.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental progressivo"
        },
        "tag_thumbnail": "Obras de calçamento em Cristal",
        "briefing_visual": {
            "descricao_pt": "Rua de terra em preparação para calçamento em cidade pequena do interior do Rio Grande do Sul, máquinas de obra ao fundo, sem rostos identificáveis",
            "query_en": ["road paving works small town", "street construction earthworks", "cobblestone paving brazil"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Unpaved street being prepared for cobblestone paving in a small southern Brazil town, construction earthworks, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Obra de infraestrutura concreta em cidade-núcleo (Cristal), fonte primária — serviço de interesse direto da comunidade"
    },

    # IDX 14 — Südoktoberfest São Lourenço do Sul (SLS, evento/cultura) — PUBLICAR
    "9a0afe0a71110324f476128af3e817babce239d4": {
        "titulo_sultv": "Südoktoberfest abre contagem regressiva em São Lourenço do Sul com lançamento oficial e concurso da corte",
        "chamada_faixa": "Südoktoberfest começa a ser preparada em SLS",
        "subtitulo": "Cidade dá início aos preparativos de uma das maiores celebrações da cultura germânica da Costa Doce.",
        "lead": "A Südoktoberfest entrou na contagem regressiva em São Lourenço do Sul, na região da Costa Doce, com o lançamento oficial da próxima edição e a abertura do concurso que vai escolher a corte da festa. O evento é um dos principais cartões de visita do município e mobiliza moradores, entidades e o setor produtivo.",
        "ganchos_3": [
            "Südoktoberfest tem lançamento oficial em São Lourenço do Sul",
            "Concurso vai escolher a corte da festa",
            "Celebração é referência da cultura germânica na Costa Doce"
        ],
        "angulo_editorial": "Evento e cultura em cidade-núcleo (São Lourenço do Sul). Pauta positiva de turismo, economia e identidade germânica da região. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Comissão organizadora da Südoktoberfest"],
        "lead_materia_longa": "A Südoktoberfest entrou na contagem regressiva em São Lourenço do Sul, na região da Costa Doce, com o lançamento oficial da próxima edição e a abertura do concurso que vai escolher a corte da festa.",
        "post_instagram": {
            "caption": "Começou a contagem regressiva! A Südoktoberfest teve o lançamento oficial da próxima edição em São Lourenço do Sul, com a abertura do concurso que vai escolher a corte da festa. Uma das maiores celebrações da cultura germânica da Costa Doce mobiliza moradores, entidades e o setor produtivo. Música, dança, gastronomia e tradição vêm aí.",
            "hashtags": ["#SãoLourençodoSul", "#Südoktoberfest", "#CostaDoce", "#CulturaGermânica", "#Turismo", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A Südoktoberfest está chegando.",
            "desenvolvimento_45s": "A Südoktoberfest entrou na contagem regressiva em São Lourenço do Sul, com o lançamento oficial da próxima edição e a abertura do concurso que vai escolher a corte da festa. Uma das maiores celebrações da cultura germânica da Costa Doce mobiliza moradores, entidades e o setor produtivo, com reflexos no comércio, na hotelaria e na gastronomia da região.",
            "fechamento_8s": "Tradição alemã no coração da Costa Doce.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental festivo"
        },
        "tag_thumbnail": "Südoktoberfest em São Lourenço do Sul",
        "briefing_visual": {
            "descricao_pt": "Cena de festa típica alemã com canecas de chope, decoração em azul e branco e elementos da cultura germânica, sem rostos identificáveis",
            "query_en": ["oktoberfest beer mugs decoration", "german festival bavarian decor", "beer stein celebration"],
            "evitar": ["rostos identificáveis", "marcas comerciais de cerveja", "logos", "texto"],
            "prompt_ia": "German-style festival scene with beer mugs and blue and white Bavarian decorations, festive atmosphere, no identifiable faces, no brand logos, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Grande evento cultural e turístico em cidade-núcleo (São Lourenço do Sul) — forte apelo regional e econômico"
    },

    # IDX 17 — PAA do pêssego Pelotas / Conab (Pelotas, agro) — PUBLICAR
    "432ff4abed47d24811d571b4e7d30367701cb576": {
        "titulo_sultv": "Pelotas recebe a Conab para lançamento do PAA do pêssego",
        "chamada_faixa": "Pelotas lança PAA do pêssego com a Conab",
        "subtitulo": "Programa de Aquisição de Alimentos volta-se à fruticultura, símbolo da economia rural da região.",
        "lead": "A Prefeitura de Pelotas, na região Sul do Rio Grande do Sul, recebeu representantes da Companhia Nacional de Abastecimento (Conab) para o lançamento do Programa de Aquisição de Alimentos (PAA) voltado ao pêssego. A fruta é um dos principais símbolos da economia rural da região, referência nacional na produção de conservas.",
        "ganchos_3": [
            "Pelotas lança o PAA do pêssego com a Conab",
            "Programa fortalece a fruticultura da região",
            "Pêssego é símbolo da economia rural pelotense"
        ],
        "angulo_editorial": "Agro e política pública em Pelotas (Costa Doce ampliada). Pauta econômica positiva, fonte primária (prefeitura e Conab), ligada à fruticultura, atividade icônica da região. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Pelotas", "Companhia Nacional de Abastecimento (Conab)"],
        "lead_materia_longa": "A Prefeitura de Pelotas, na região Sul do Rio Grande do Sul, recebeu representantes da Companhia Nacional de Abastecimento (Conab) para o lançamento do Programa de Aquisição de Alimentos (PAA) voltado ao pêssego.",
        "post_instagram": {
            "caption": "Boa notícia para quem vive da fruticultura. Pelotas recebeu a Conab para o lançamento do PAA do pêssego, programa que fortalece a produção e garante mercado para a fruta que é símbolo da economia rural da região. O pêssego pelotense, referência nacional em conservas, ganha mais um caminho de comercialização e valorização do produtor local.",
            "hashtags": ["#Pelotas", "#AgroRS", "#Pêssego", "#Fruticultura", "#PAA", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O pêssego de Pelotas em destaque.",
            "desenvolvimento_45s": "A Prefeitura de Pelotas recebeu representantes da Conab para o lançamento do Programa de Aquisição de Alimentos voltado ao pêssego. A fruta é um dos principais símbolos da economia rural da região, referência nacional na produção de conservas. O programa fortalece a fruticultura, garante mercado para o produtor e valoriza uma das atividades mais tradicionais do Sul do Rio Grande do Sul.",
            "fechamento_8s": "Mais valor para o produtor da região.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental otimista"
        },
        "tag_thumbnail": "PAA do pêssego em Pelotas",
        "briefing_visual": {
            "descricao_pt": "Pessegueiros carregados de pêssegos maduros em pomar do Sul do Rio Grande do Sul, frutas em close, sem pessoas",
            "query_en": ["peach orchard ripe peaches", "peaches on tree close up", "peach fruit harvest"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Peach orchard with ripe peaches on the trees in southern Brazil, close-up of the fruit, warm natural light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agro e política pública em Pelotas (Costa Doce ampliada), fonte primária (Conab) — fruticultura icônica da região"
    },

    # IDX 20 — Renegociação dívidas produtores RS / Senado (RS, agro) — PUBLICAR
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "cidade": "Rio Grande do Sul",
        "titulo_sultv": "Produtores do RS acompanham com apreensão a renegociação de dívidas rurais no Senado",
        "chamada_faixa": "Produtores do RS temem por dívidas rurais",
        "subtitulo": "Setor teme ficar sem acesso ao crédito rural para a próxima safra caso a renegociação não avance.",
        "lead": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas rurais no Senado. O setor teme ficar sem acesso ao crédito para a próxima safra caso a medida não seja aprovada, em um momento de margens apertadas no campo gaúcho.",
        "ganchos_3": [
            "Produtores do RS temem que renegociação de dívidas não avance",
            "Setor teme ficar sem crédito rural para a próxima safra",
            "Tema mobiliza o campo gaúcho neste fim de junho"
        ],
        "angulo_editorial": "Agro com âncora no RS — tema econômico (crédito rural e endividamento) de alto interesse para a audiência produtora gaúcha. Foco no impacto sobre a próxima safra, sem viés partidário e sem entrar em disputa de siglas.",
        "fontes_complementares_sugeridas": ["Federação da Agricultura do RS (Farsul)", "Senado Federal"],
        "lead_materia_longa": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas rurais no Senado, temendo ficar sem acesso ao crédito para a próxima safra.",
        "post_instagram": {
            "caption": "O campo gaúcho está atento. Produtores rurais do Rio Grande do Sul acompanham com apreensão a renegociação de dívidas rurais em tramitação no Senado. O receio é ficar sem acesso ao crédito para a próxima safra, num momento de margens apertadas. A definição é decisiva para o planejamento de quem vive da terra no Sul do país.",
            "hashtags": ["#AgroRS", "#CréditoRural", "#Safra", "#ProdutorRural", "#RioGrandedoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O campo gaúcho está apreensivo.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a renegociação de dívidas rurais em tramitação no Senado. O setor teme ficar sem acesso ao crédito rural para a próxima safra caso a medida não seja aprovada. A definição é decisiva para o planejamento de quem vive da terra, em um momento de margens apertadas no campo gaúcho.",
            "fechamento_8s": "Uma decisão que mexe com toda a lavoura.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sério"
        },
        "tag_thumbnail": "Dívidas rurais preocupam o RS",
        "briefing_visual": {
            "descricao_pt": "Lavoura de soja já colhida ou campo de grãos no Rio Grande do Sul sob céu nublado, vista ampla, sem pessoas, transmitindo apreensão econômica",
            "query_en": ["soybean field cloudy sky", "harvested grain field overcast", "farmland brazil dramatic sky"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Wide view of a soybean field under a cloudy sky in southern Brazil, somber light suggesting uncertainty, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agro com âncora explícita no RS, tema de crédito rural e safra — altíssimo interesse para a audiência produtora gaúcha"
    },

    # IDX 29 — Inverno começa domingo, chuva acima da média no RS (clima, serviço) — PUBLICAR (post)
    "06a14eba7c40b44807869b5ff07bb4aa5db6416a": {
        "cidade": "Rio Grande do Sul",
        "titulo_sultv": "Inverno começa neste domingo no RS com previsão de chuva acima da média",
        "chamada_faixa": "Inverno chega ao RS com mais chuva",
        "subtitulo": "Estação começa às 5h25 deste domingo (21), com temperaturas menos rigorosas e maior volume de chuva.",
        "lead": "O inverno começa oficialmente às 5h25 deste domingo (21) no Rio Grande do Sul. A estação deve ter temperaturas menos rigorosas, porém com volume de chuva acima da média no estado, cenário que pede atenção do campo e das cidades.",
        "ganchos_3": [
            "Inverno começa às 5h25 deste domingo (21)",
            "Chuva deve ficar acima da média no RS",
            "Temperaturas devem ser menos rigorosas na estação"
        ],
        "angulo_editorial": "Clima e serviço de alcance estadual — pauta de utilidade direta para a audiência rural e urbana, no fim de semana de virada da estação. Tom informativo, sem dramalhão.",
        "fontes_complementares_sugeridas": ["Instituto Nacional de Meteorologia (Inmet)", "Defesa Civil do RS"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Prepare o agasalho e o guarda-chuva. O inverno começa oficialmente às 5h25 deste domingo (21) no Rio Grande do Sul. A estação deve trazer temperaturas menos rigorosas, mas com volume de chuva acima da média no estado. Para o campo e para as cidades, é hora de redobrar a atenção com o planejamento das atividades e com as áreas sujeitas a alagamento. Fique de olho na previsão da sua região.",
            "hashtags": ["#RioGrandedoSul", "#Inverno", "#Clima", "#Chuva", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O inverno está chegando.",
            "desenvolvimento_45s": "O inverno começa oficialmente às 5h25 deste domingo no Rio Grande do Sul. A estação deve ter temperaturas menos rigorosas, mas com volume de chuva acima da média no estado. Para o campo, isso pede atenção no planejamento das atividades; para as cidades, atenção redobrada com áreas sujeitas a alagamento. Vale acompanhar a previsão da sua região nos próximos dias.",
            "fechamento_8s": "Estação mais chuvosa pela frente.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental calmo"
        },
        "tag_thumbnail": "Inverno chuvoso no RS",
        "briefing_visual": {
            "descricao_pt": "Paisagem rural do Rio Grande do Sul em dia de inverno com céu nublado e neblina sobre o campo, sem pessoas",
            "query_en": ["winter foggy rural landscape", "cloudy field morning mist", "overcast countryside winter"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Rural landscape in southern Brazil on a winter morning with overcast sky and fog over the fields, cold atmosphere, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima de alcance estadual, serviço útil e oportuno na virada da estação — relevante para audiência rural e urbana"
    },

    # ---------------- REBAIXAR ----------------
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": {**_skip("REBAIXAR", "Conteúdo desatualizado (inscrições de abril/2026); Arambaré já contemplado por pauta mais recente"), "cidade": "Arambaré"},
    "4a19f3b447abaaef75271b2e2dbf1a33ae46591b": _skip("REBAIXAR", "Reunião administrativa de rotina, baixo valor noticioso e título corrompido pelo scraper"),
    "93d8797025ffe98d7c47bb3b29fd426a9dec54b2": _skip("REBAIXAR", "Título é cabeçalho de seção; conteúdo raso sobre evento pontual"),
    "804da2cbe08274dd604274d8db6acc48cc218fed": _skip("REBAIXAR", "Cidade-núcleo Cristal já contemplada por matéria de calçamento; quota por cidade priorizada"),
    "0c78bd0cc00e7d0302fc635b3fdbfbd510252753": _skip("REBAIXAR", "Conteúdo desatualizado (classificações de maio/2026)"),
    "49348b06a39337d964518e54a7715142418ea220": _skip("REBAIXAR", "Pauta procedural sobre campanha tributária, baixo apelo e tema sensível (fundo da criança)"),
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": _skip("REBAIXAR", "Pauta estadual ampla sem âncora em cidade-núcleo; tom sensacionalista"),
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": _skip("REBAIXAR", "Pauta estadual de fiscalização sem âncora regional específica"),
    "e6fff2725635f8da6e880c351f39276a44142f44": _skip("REBAIXAR", "Evento na Região Metropolitana (Esteio), fora do eixo Costa Doce; datas possivelmente vencidas"),
    "45918557b425ac5a5aa05a3264a94d0abb447dc7": _skip("REBAIXAR", "Santa Maria fora do eixo prioritário; score editorial baixo"),
    "10ecbe665aec1d1df677b64e8269a3a8da82defa": _skip("REBAIXAR", "Minicurso de nicho, baixo apelo para a audiência; cidade fora do eixo"),
    "b0ab462c9038524139a276afc3425216755fd943": _skip("REBAIXAR", "Venâncio Aires (Vales) fora do eixo prioritário; conteúdo promocional"),
    "7cb808cd687c13d1212ea730fc12bd8f806f6edb": _skip("REBAIXAR", "Conteúdo promocional de revista; cidade fora do eixo"),

    # ---------------- BLOQUEAR ----------------
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip("BLOQUEAR", "Edital procedural e desatualizado (penalidade nº 001/2026, 30/03/2026)"),
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip("BLOQUEAR", "Edital procedural (abertura de prazo para requerimentos)"),
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip("BLOQUEAR", "Título é aviso/cabeçalho de seção (Aviso de Audiência Pública), conteúdo procedural"),
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip("BLOQUEAR", "Comunicado administrativo procedural e desatualizado (notas fiscais, 05/05/2026)"),
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": _skip("BLOQUEAR", "Comunicado administrativo procedural (contracheques de servidores)"),
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip("BLOQUEAR", "Guardrail política partidária (plebiscito de privatização, manifestação de parlamentares)"),
    "bee75181a89fe43958a221ea578a2be9e230d8a7": _skip("BLOQUEAR", "Esporte de região distante (Serra/Bento Gonçalves), fora do eixo Sul-RS"),
}


MATERIAS = {

    "84295932f62a2688fa4ffe074cca173580476e3c": """### Título ###
Acidente entre três veículos é registrado no centro de Camaquã nesta sexta-feira

### Artigo ###
Um acidente envolvendo três veículos foi registrado na tarde desta sexta-feira (19) no centro de Camaquã, na região da Costa Doce. A Divisão Municipal de Trânsito foi acionada para atender a ocorrência e organizar o fluxo de veículos no local. As colisões aconteceram em uma das áreas de maior circulação da cidade, onde o tráfego costuma ser intenso no fim de tarde, quando aumenta o deslocamento de moradores e o movimento do comércio. Ocorrências dessa natureza no perímetro central reforçam a importância de manter a atenção redobrada ao volante, sobretudo nos horários de pico. Respeitar a sinalização, reduzir a velocidade nas vias mais movimentadas e manter a distância de segurança são atitudes simples que ajudam a evitar acidentes e a preservar vidas. O centro de Camaquã concentra estabelecimentos comerciais, serviços e repartições, o que torna o espaço de convivência entre veículos e pedestres ainda mais sensível. A presença da Divisão Municipal de Trânsito nesses momentos é fundamental para garantir o atendimento rápido, restabelecer a ordem na via e orientar os condutores. A segurança viária é uma responsabilidade compartilhada entre o poder público e os motoristas. Pequenas mudanças de comportamento no trânsito, como a atenção aos cruzamentos e o cuidado com o pedestre, fazem diferença direta na redução de ocorrências. Em uma cidade que cresce e movimenta a economia da Costa Doce, manter o trânsito seguro é parte essencial da qualidade de vida da população.

### Legenda sugerida ###
Acidente entre três veículos mobiliza a Divisão Municipal de Trânsito no centro de Camaquã nesta sexta-feira (19).

### Palavras-chave ###
acidente Camaquã, trânsito, centro de Camaquã, Costa Doce, segurança viária, Divisão Municipal de Trânsito
""",

    "05cf0b995ff0f7c7b8d97071e5b4ab7de4361923": """### Título ###
Sindicato dos Trabalhadores Rurais de Camaquã completa 60 anos e recebe homenagem da Câmara

### Artigo ###
O Sindicato dos Trabalhadores Rurais de Camaquã completou 60 anos de atuação e foi homenageado pela Câmara de Vereadores do município, na região da Costa Doce. A entidade é uma das principais representantes do produtor rural da cidade, em uma das maiores regiões produtoras de arroz do Rio Grande do Sul. O marco de seis décadas reconhece uma trajetória de defesa dos interesses do campo. Ao longo desse período, o sindicato acompanhou as transformações da agricultura local, da modernização das lavouras às mudanças nas políticas de crédito e às exigências de um setor cada vez mais competitivo e tecnológico. A homenagem da Câmara de Vereadores valoriza não apenas a instituição, mas todo o conjunto de famílias que vivem da terra na região. O trabalho de representação sindical é essencial para articular reivindicações, apoiar o produtor em questões previdenciárias e trabalhistas e fortalecer a organização da categoria diante dos desafios do agronegócio. Camaquã tem na produção agrícola um dos pilares da sua economia. O arroz cultivado na região abastece mercados e gera renda e emprego, sustentando uma cadeia produtiva que envolve desde a lavoura até o comércio e os serviços. Nesse cenário, entidades com história consolidada cumprem um papel estratégico de articulação entre o campo e as instâncias de decisão. Ao chegar aos 60 anos, o sindicato reafirma seu compromisso com o futuro da atividade rural. A celebração olha para o passado com orgulho, mas também projeta os próximos desafios de um setor que segue como motor de desenvolvimento da Costa Doce.

### Legenda sugerida ###
Sindicato dos Trabalhadores Rurais de Camaquã chega aos 60 anos e é homenageado pela Câmara de Vereadores.

### Palavras-chave ###
Sindicato dos Trabalhadores Rurais de Camaquã, Camaquã, 60 anos, produtor rural, agro, arroz, Costa Doce
""",

    "4d84d73fbe84b729ff39aaf941f9080399410131": """### Título ###
Bandas de Tapes e Sentinela do Sul recebem reconhecimento de maestro campeão mundial

### Artigo ###
As bandas municipais de Tapes e Sentinela do Sul, na região da Costa Doce, receberam o reconhecimento do maestro campeão mundial Rogério Wanderley Brito pelo desempenho artístico. O elogio coroa um trabalho de formação musical que vem se destacando em duas cidades do Sul do Rio Grande do Sul. As corporações musicais são patrimônios culturais dos municípios. Mais do que conjuntos artísticos, elas representam um espaço de formação para crianças, jovens e adultos, que encontram na música uma oportunidade de aprendizado, disciplina e convivência. O reconhecimento de uma autoridade do meio confirma a qualidade desse esforço coletivo. Manter bandas ativas no interior exige dedicação de músicos, professores, famílias e poder público. O resultado aparece nas apresentações em datas cívicas, festas comunitárias e eventos culturais, momentos em que as corporações ganham as ruas e reúnem a população em torno de uma tradição que atravessa gerações. O destaque alcançado por Tapes e Sentinela do Sul valoriza a cultura produzida longe dos grandes centros e mostra que o talento da Costa Doce tem reconhecimento que ultrapassa as fronteiras da região. É também um estímulo para que novos integrantes se aproximem das bandas e para que o investimento na formação musical tenha continuidade. A música é um elo poderoso de identidade e pertencimento. Ao serem reconhecidas por seu desempenho, as bandas dos dois municípios reforçam a importância de preservar e apoiar as iniciativas culturais que fortalecem as comunidades do interior gaúcho.

### Legenda sugerida ###
Bandas de Tapes e Sentinela do Sul têm o desempenho artístico reconhecido pelo maestro campeão mundial Rogério Wanderley Brito.

### Palavras-chave ###
bandas de Tapes, Sentinela do Sul, cultura, música, Costa Doce, corporação musical, reconhecimento
""",

    "dd7df59af3392ccb9037aa29aab34324cac79b5c": """### Título ###
Cerro Grande do Sul abre inscrições para cursos gratuitos de qualificação com bolsa permanência

### Artigo ###
A Prefeitura de Cerro Grande do Sul, na região da Costa Doce, abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes. A iniciativa é conduzida pela Secretaria Municipal do Trabalho, Cidadania e Assistência Social e tem como objetivo ampliar a empregabilidade e a renda da população local. A oferta de capacitação gratuita é uma ferramenta importante de desenvolvimento social e econômico. Ao qualificar a mão de obra do município, a medida prepara os trabalhadores para novas oportunidades, atende a demandas do mercado e contribui para reduzir as desigualdades de acesso à formação profissional. O diferencial da bolsa permanência merece destaque. O auxílio ajuda a garantir que os participantes consigam concluir os cursos, reduzindo a evasão provocada por dificuldades financeiras e custos de deslocamento. É um incentivo concreto para que a qualificação chegue a quem mais precisa. Programas como esse fortalecem a economia local a partir das pessoas. Trabalhadores mais capacitados têm melhores condições de conquistar emprego, empreender e aumentar a renda familiar, movimentando o comércio e os serviços do município. Para o poder público, investir em qualificação é semear desenvolvimento de médio e longo prazo. A recomendação é que os interessados verifiquem os requisitos, prazos e a forma de inscrição junto à secretaria responsável. Iniciativas de qualificação costumam ter vagas limitadas, e a procura tende a ser alta justamente pelo caráter gratuito e pelo apoio oferecido aos participantes ao longo da formação.

### Legenda sugerida ###
Cerro Grande do Sul abre inscrições para dois cursos gratuitos de qualificação profissional com bolsa permanência.

### Palavras-chave ###
Cerro Grande do Sul, cursos gratuitos, qualificação profissional, bolsa permanência, trabalho, renda, Costa Doce
""",

    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": """### Título ###
Arambaré publica nota técnica com orientações sobre poda de árvores e arborização urbana

### Artigo ###
A Prefeitura de Arambaré publicou, em 18 de junho, uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município, na região da Costa Doce. O documento reúne diretrizes voltadas a moradores e responsáveis por imóveis, com o objetivo de orientar os procedimentos corretos para a conservação das árvores e a segurança da cidade. A iniciativa chega em um momento oportuno do calendário. O inverno é justamente o período mais indicado para a poda, época em que muitas espécies entram em dormência e respondem melhor à intervenção, com menor estresse para a planta e cicatrização mais eficiente dos cortes. Realizar a poda de forma técnica e na estação adequada reduz riscos, prolonga a vida das árvores e evita problemas como a queda de galhos sobre a fiação elétrica, calçadas e veículos. A arborização urbana traz benefícios diretos à qualidade de vida: oferece sombra, ameniza as temperaturas, contribui para a drenagem e valoriza o ambiente das ruas. Por isso, o manejo correto é uma responsabilidade compartilhada entre o poder público e a população. A orientação da prefeitura é que qualquer intervenção siga as diretrizes técnicas divulgadas e, quando necessário, conte com o acompanhamento dos setores responsáveis do município. A medida reforça o compromisso de Arambaré com a conservação do patrimônio verde da cidade e com a segurança de quem circula pelas vias urbanas, especialmente no período de maior incidência de ventos e instabilidades do inverno.

### Legenda sugerida ###
Prefeitura de Arambaré divulga nota técnica com orientações para a poda de árvores e o manejo da arborização urbana.

### Palavras-chave ###
Arambaré, poda de árvores, arborização urbana, nota técnica, meio ambiente, Costa Doce, manejo de árvores
""",

    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": """### Título ###
Rua Camaquã recebe preparação para obras de calçamento em Cristal

### Artigo ###
A Prefeitura de Cristal, na região da Costa Doce, iniciou os trabalhos de preparação da Rua Camaquã para as obras de calçamento. A intervenção integra o conjunto de melhorias de infraestrutura urbana do município e antecede a pavimentação da via, etapa aguardada pelos moradores da região. A preparação do terreno é uma fase essencial de qualquer obra de calçamento. Antes da pavimentação, é preciso nivelar o solo, garantir a drenagem adequada e organizar o traçado da rua, assegurando que o investimento tenha durabilidade e qualidade. Esse cuidado técnico evita problemas futuros e amplia a vida útil da via. O calçamento traz impactos diretos no dia a dia da população. Ruas pavimentadas reduzem a poeira nos períodos de estiagem e o barro nos dias de chuva, melhoram o acesso de veículos e pedestres e facilitam a circulação de serviços essenciais, como a coleta de lixo e o atendimento de emergências. Além do ganho em mobilidade, a pavimentação valoriza os imóveis e contribui para o desenvolvimento dos bairros. As obras de infraestrutura urbana são parte importante do planejamento dos municípios do interior, que buscam ampliar a malha pavimentada e oferecer mais conforto e qualidade de vida aos moradores. Cada nova via calçada representa um avanço concreto para a comunidade. Com o início da preparação da Rua Camaquã, a expectativa é de que a pavimentação avance nas próximas etapas, integrando mais um trecho à rede de ruas calçadas de Cristal e atendendo a uma demanda dos moradores da região.

### Legenda sugerida ###
Rua Camaquã recebe serviços de preparação para as obras de calçamento em Cristal.

### Palavras-chave ###
Cristal, Rua Camaquã, calçamento, pavimentação, infraestrutura urbana, obras, Costa Doce
""",

    "9a0afe0a71110324f476128af3e817babce239d4": """### Título ###
Südoktoberfest abre contagem regressiva em São Lourenço do Sul com lançamento oficial e concurso da corte

### Artigo ###
A Südoktoberfest entrou na contagem regressiva em São Lourenço do Sul. Com o lançamento oficial da próxima edição e a abertura do concurso que vai escolher a corte da festa, a cidade dá início aos preparativos para uma das maiores celebrações da cultura germânica da região da Costa Doce. O evento é um dos cartões de visita do município e mobiliza moradores, entidades e o setor produtivo ao longo de toda a organização. A escolha da corte é um dos momentos tradicionais da festa. As representantes selecionadas passam a ser embaixadoras da Südoktoberfest, presentes nos atos oficiais e na divulgação da celebração que resgata a herança dos imigrantes alemães que colonizaram a região. Essa identidade cultural, expressa na música, na dança, na gastronomia e nos trajes típicos, é um dos elementos que mais atraem visitantes e dão personalidade ao evento. O impacto da Südoktoberfest vai além da festa em si. A celebração movimenta a economia local, com reflexos no comércio, na hotelaria, na gastronomia e nos serviços de São Lourenço do Sul e dos municípios vizinhos. Durante o período do evento, a cidade recebe um fluxo expressivo de turistas, o que gera oportunidades para empreendedores e trabalhadores da região. Com o lançamento oficial, a expectativa da comunidade cresce. Os preparativos seguem nas próximas semanas, e a organização deve divulgar a programação completa à medida que a data se aproxima, mantendo viva uma das tradições mais marcantes da Costa Doce.

### Legenda sugerida ###
São Lourenço do Sul dá largada à Südoktoberfest com lançamento oficial e concurso da corte da festa.

### Palavras-chave ###
Südoktoberfest, São Lourenço do Sul, cultura germânica, turismo, Costa Doce, festa, corte, tradição
""",

    "432ff4abed47d24811d571b4e7d30367701cb576": """### Título ###
Pelotas recebe a Conab para lançamento do PAA do pêssego

### Artigo ###
A Prefeitura de Pelotas, na região Sul do Rio Grande do Sul, recebeu representantes da Companhia Nacional de Abastecimento (Conab) para o lançamento do Programa de Aquisição de Alimentos (PAA) voltado ao pêssego. A fruta é um dos principais símbolos da economia rural da região, referência nacional na produção de conservas. O Programa de Aquisição de Alimentos é uma política pública que conecta a produção da agricultura familiar a quem precisa de alimentos, garantindo a compra da produção e o abastecimento de instituições e famílias em situação de vulnerabilidade. Ao direcionar o programa ao pêssego, a iniciativa fortalece uma cadeia produtiva tradicional e estratégica para o município. A fruticultura é uma das marcas da identidade econômica de Pelotas e da região. O pêssego movimenta lavouras, agroindústrias e comércio, gerando emprego e renda no campo e na cidade. Programas de comercialização e aquisição ajudam a dar estabilidade ao produtor, que muitas vezes enfrenta oscilações de preço e dificuldades de escoamento da safra. A presença da Conab no lançamento reforça a articulação entre os entes públicos em torno da agricultura familiar. Esse tipo de parceria amplia o acesso dos produtores a mercados, valoriza a produção local e contribui para a segurança alimentar das comunidades atendidas. Para os fruticultores da região, iniciativas como o PAA do pêssego representam mais do que uma alternativa de venda: são um reconhecimento da importância da atividade e um incentivo para que a tradição da fruticultura pelotense continue forte, sustentando a economia rural do Sul do Rio Grande do Sul.

### Legenda sugerida ###
Pelotas recebe a Conab para o lançamento do PAA do pêssego, fortalecendo a fruticultura da região.

### Palavras-chave ###
Pelotas, pêssego, PAA, Conab, fruticultura, agricultura familiar, agro, Rio Grande do Sul
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS acompanham com apreensão a renegociação de dívidas rurais no Senado

### Artigo ###
Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas rurais no Senado. O setor teme ficar sem acesso ao crédito para a próxima safra caso a medida não seja aprovada, em um momento de margens apertadas no campo gaúcho. A questão do endividamento rural ganhou peso após anos marcados por adversidades climáticas e oscilações de preços, que afetaram a rentabilidade das lavouras no estado. Para muitos produtores, a renegociação das dívidas é vista como condição para manter as portas abertas e seguir investindo na produção. O crédito rural é o combustível da safra. É com ele que o produtor financia a compra de insumos, sementes, fertilizantes e o custeio da lavoura. Sem acesso a esse recurso, o planejamento do plantio fica comprometido, com reflexos diretos sobre a produção de alimentos e sobre toda a cadeia que depende do agronegócio. A apreensão do setor reflete a importância de regras claras e de soluções que ofereçam segurança ao produtor. O agronegócio é um dos principais motores da economia gaúcha, e dificuldades no campo se espalham por toda a cadeia, atingindo o comércio, a indústria e os serviços ligados à atividade. Enquanto a definição não vem, produtores e entidades de representação seguem atentos à tramitação. A expectativa do setor é de que se construa uma alternativa que permita renegociar os compromissos sem inviabilizar o acesso ao crédito, preservando a capacidade produtiva do campo e a renda de quem vive da terra no Rio Grande do Sul.

### Legenda sugerida ###
Produtores do RS temem ficar sem crédito para a próxima safra e acompanham a renegociação de dívidas no Senado.

### Palavras-chave ###
dívidas rurais, crédito rural, produtores RS, safra, agro, Senado, Rio Grande do Sul, agronegócio
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
