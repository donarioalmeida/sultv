#!/usr/bin/env python3
"""
angular_2026-06-21.py — angulação editorial + redação (cowork-faz-tudo).
Decisões editoriais Claude na sessão para a pauta de 2026-06-21.
Regra 12 INEGOCIÁVEL: nenhum texto menciona veículos/portais/rádios/jornais.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-21"


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

    # IDX 0 — Liga Feminina de Combate ao Câncer de Camaquã 40 anos (Camaquã, comunidade) — PUBLICAR
    "afdf6218ab7085cf383e86deefa5f40a87987f87": {
        "titulo_sultv": "Liga Feminina de Combate ao Câncer de Camaquã completa 40 anos com sede própria",
        "chamada_faixa": "Liga de Combate ao Câncer faz 40 anos",
        "subtitulo": "Entidade conclui sede própria, amplia o atendimento aos assistidos e prepara programação para marcar quatro décadas de atuação em Camaquã.",
        "lead": "São 40 anos de trabalho voluntário ao lado de quem mais precisa. A Liga Feminina de Combate ao Câncer de Camaquã, na região da Costa Doce, chega a quatro décadas de atuação com a conclusão de sua sede própria e a ampliação do atendimento aos assistidos.",
        "ganchos_3": [
            "Liga Feminina de Combate ao Câncer de Camaquã completa 40 anos",
            "Entidade concluiu a construção de sua sede própria",
            "Ampliação do atendimento marca as quatro décadas de atuação"
        ],
        "angulo_editorial": "Comunidade e solidariedade em cidade-núcleo (Camaquã/Costa Doce). Marco institucional positivo de entidade de apoio social, com fato concreto (sede própria concluída). Não é conteúdo médico (sem diagnóstico/prescrição) — é trajetória institucional e voluntariado. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Liga Feminina de Combate ao Câncer de Camaquã", "Prefeitura de Camaquã"],
        "lead_materia_longa": "São 40 anos de trabalho voluntário ao lado de quem mais precisa. A Liga Feminina de Combate ao Câncer de Camaquã, na região da Costa Doce, chega a quatro décadas de atuação com a conclusão de sua sede própria.",
        "post_instagram": {
            "caption": "Quarenta anos de acolhimento. A Liga Feminina de Combate ao Câncer de Camaquã chega às quatro décadas de atuação com uma conquista histórica: a conclusão de sua sede própria. Ao longo desses anos, a entidade ampliou o atendimento e se tornou referência de apoio e solidariedade para as famílias da Costa Doce. Uma história construída por mãos voluntárias, que segue firme ao lado de quem precisa.",
            "hashtags": ["#Camaquã", "#CostaDoce", "#Solidariedade", "#Comunidade", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Quarenta anos de acolhimento em Camaquã.",
            "desenvolvimento_45s": "A Liga Feminina de Combate ao Câncer de Camaquã completa 40 anos de atuação e celebra a conclusão da sua sede própria. Ao longo de quatro décadas, a entidade ampliou o atendimento aos assistidos e se consolidou como referência de apoio e solidariedade para as famílias da Costa Doce. O trabalho voluntário acolhe quem enfrenta o tratamento e mostra a força da comunidade quando se une por uma causa.",
            "fechamento_8s": "Camaquã celebra quatro décadas de solidariedade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental emotivo suave"
        },
        "tag_thumbnail": "Liga de Combate ao Câncer, 40 anos",
        "briefing_visual": {
            "descricao_pt": "Laço cor-de-rosa de combate ao câncer sobre fundo neutro, ou fachada simples de uma sede de entidade comunitária em cidade do interior do Rio Grande do Sul, sem pessoas e sem rostos",
            "query_en": ["pink ribbon cancer support", "community center building exterior", "volunteer charity solidarity"],
            "evitar": ["pacientes", "rostos identificáveis", "ambiente hospitalar explícito", "marcas", "logos", "texto"],
            "prompt_ia": "A soft pink awareness ribbon resting on a neutral surface with warm natural light, symbol of community cancer support, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Marco institucional comunitário em cidade-núcleo (Camaquã), fato concreto (sede própria). Não é conteúdo médico — trajetória de voluntariado e solidariedade."
    },

    # IDX 1 — Conselho Municipal de Inovação de Camaquã (Camaquã, inovação) — PUBLICAR
    "b19a7c0521b9e9bca8fbc770a59fdf2b644f4a67": {
        "titulo_sultv": "Conselho Municipal de Inovação de Camaquã quer ampliar participação da comunidade",
        "chamada_faixa": "Camaquã fortalece conselho de inovação",
        "subtitulo": "Nova gestão destaca a criação do Fundo Municipal de Inovação e a aproximação com escolas, empresas e universidades.",
        "lead": "Camaquã quer transformar inovação em política pública permanente. O Conselho Municipal de Inovação da cidade, na região da Costa Doce, definiu como prioridade ampliar a participação da comunidade e fortalecer projetos locais, com destaque para a criação do Fundo Municipal de Inovação.",
        "ganchos_3": [
            "Conselho Municipal de Inovação de Camaquã amplia a participação da comunidade",
            "Nova gestão destaca a criação do Fundo Municipal de Inovação",
            "Aproximação com escolas, empresas e universidades é prioridade"
        ],
        "angulo_editorial": "Inovação e digitalização em cidade-núcleo (Camaquã) — pauta totalmente alinhada ao posicionamento editorial da SulTV. Fato concreto e institucional (conselho, fundo municipal). Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Conselho Municipal de Inovação de Camaquã", "Prefeitura de Camaquã"],
        "lead_materia_longa": "Camaquã quer transformar inovação em política pública permanente. O Conselho Municipal de Inovação da cidade, na região da Costa Doce, definiu como prioridade ampliar a participação da comunidade e fortalecer projetos locais.",
        "post_instagram": {
            "caption": "Inovação que nasce no interior. O Conselho Municipal de Inovação de Camaquã quer ampliar a participação da comunidade e fortalecer projetos locais, com destaque para a criação do Fundo Municipal de Inovação e a aproximação com escolas, empresas e universidades. É o tipo de iniciativa que mostra que tecnologia e desenvolvimento também acontecem na Costa Doce, conectando talentos a desafios reais da região.",
            "hashtags": ["#Camaquã", "#CostaDoce", "#Inovação", "#Tecnologia", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Inovação vira prioridade em Camaquã.",
            "desenvolvimento_45s": "O Conselho Municipal de Inovação de Camaquã definiu como prioridade ampliar a participação da comunidade e fortalecer projetos locais. Entre os destaques estão a criação do Fundo Municipal de Inovação e a aproximação com escolas, empresas e universidades, incentivando o desenvolvimento de soluções para desafios da cidade. É a prova de que tecnologia e empreendedorismo também têm lugar no interior da Costa Doce.",
            "fechamento_8s": "Camaquã aposta na inovação como política pública.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental tecnológico otimista"
        },
        "tag_thumbnail": "Conselho de Inovação de Camaquã",
        "briefing_visual": {
            "descricao_pt": "Reunião de trabalho em ambiente moderno com pessoas de costas diante de painel de ideias, ou mesa com notebook e post-its representando um ecossistema de inovação no interior do RS, sem rostos identificáveis",
            "query_en": ["innovation workshop collaboration", "startup meeting notebook ideas", "people brainstorming office"],
            "evitar": ["rostos identificáveis", "marcas", "logos de empresas", "texto legível"],
            "prompt_ia": "A bright modern coworking space with a laptop, sticky notes and idea boards symbolizing local innovation, no people faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Inovação em cidade-núcleo (Camaquã), 100% alinhado ao posicionamento editorial SulTV. Fato concreto institucional, fonte primária."
    },

    # IDX 2 — Bandas de Tapes e Sentinela do Sul reconhecidas por maestro (Tapes, cultura) — PUBLICAR
    "4d84d73fbe84b729ff39aaf941f9080399410131": {
        "titulo_sultv": "Bandas de Tapes e Sentinela do Sul recebem reconhecimento de maestro campeão mundial",
        "chamada_faixa": "Bandas da Costa Doce ganham reconhecimento",
        "subtitulo": "Corporações musicais dos dois municípios tiveram o desempenho elogiado pelo maestro campeão mundial Rogério Wanderley Brito.",
        "lead": "O talento musical da Costa Doce ganhou reconhecimento de peso. As bandas municipais de Tapes e Sentinela do Sul, no Sul do Rio Grande do Sul, foram elogiadas pelo desempenho artístico pelo maestro campeão mundial Rogério Wanderley Brito.",
        "ganchos_3": [
            "Bandas de Tapes e Sentinela do Sul são reconhecidas por maestro",
            "Elogio veio do maestro campeão mundial Rogério Wanderley Brito",
            "Trabalho de formação musical valoriza a cultura da Costa Doce"
        ],
        "angulo_editorial": "Cultura em cidades-núcleo (Tapes e Sentinela do Sul). Pauta positiva que valoriza a formação musical local, com referência nominal a autoridade artística (fonte primária). Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Tapes", "Prefeitura de Sentinela do Sul"],
        "lead_materia_longa": "O talento musical da Costa Doce ganhou reconhecimento de peso. As bandas municipais de Tapes e Sentinela do Sul, no Sul do Rio Grande do Sul, foram elogiadas pelo desempenho artístico pelo maestro campeão mundial Rogério Wanderley Brito.",
        "post_instagram": {
            "caption": "Talento da Costa Doce reconhecido lá fora. As bandas municipais de Tapes e Sentinela do Sul receberam o elogio do maestro campeão mundial Rogério Wanderley Brito pelo desempenho artístico. É a prova de que o trabalho de formação musical feito no interior do Sul do Rio Grande do Sul tem qualidade de sobra. Orgulho para as duas cidades e para quem acredita na cultura local.",
            "hashtags": ["#Tapes", "#SentineladoSul", "#CostaDoce", "#Cultura", "#Música", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Música da Costa Doce reconhecida.",
            "desenvolvimento_45s": "As bandas municipais de Tapes e Sentinela do Sul receberam o reconhecimento do maestro campeão mundial Rogério Wanderley Brito pelo desempenho artístico. O elogio coroa um trabalho de formação musical que se destaca em duas cidades do Sul do Rio Grande do Sul. As corporações são espaço de aprendizado para crianças e jovens e patrimônio cultural das comunidades, mostrando que o talento do interior tem reconhecimento de sobra.",
            "fechamento_8s": "Cultura que faz a Costa Doce orgulhosa.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental orquestral animado"
        },
        "tag_thumbnail": "Bandas de Tapes reconhecidas",
        "briefing_visual": {
            "descricao_pt": "Instrumentos de sopro de banda municipal — trompete, trombone, clarinete — em destaque, ou apresentação de banda em praça de cidade do interior do RS, sem rostos identificáveis",
            "query_en": ["brass band instruments", "marching band trumpet", "municipal band performance"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Close-up of polished brass band instruments such as trumpet and trombone resting before a performance, warm light, no people faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura em cidades-núcleo (Tapes e Sentinela do Sul), pauta positiva com reconhecimento de autoridade artística. Forte apelo regional."
    },

    # IDX 3 — Cursos gratuitos Cerro Grande do Sul com bolsa permanência (Tapes/CGS, serviço) — PUBLICAR
    "dd7df59af3392ccb9037aa29aab34324cac79b5c": {
        "titulo_sultv": "Cerro Grande do Sul abre inscrições para cursos gratuitos de qualificação com bolsa permanência",
        "chamada_faixa": "Cursos gratuitos com bolsa em Cerro Grande do Sul",
        "subtitulo": "Secretaria Municipal do Trabalho, Cidadania e Assistência Social oferece dois cursos gratuitos com auxílio para os participantes.",
        "lead": "Quem busca qualificação na Costa Doce tem uma nova oportunidade. A Prefeitura de Cerro Grande do Sul abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes, em iniciativa conduzida pela Secretaria Municipal do Trabalho, Cidadania e Assistência Social.",
        "ganchos_3": [
            "Cerro Grande do Sul abre inscrições para cursos gratuitos",
            "Cursos contam com bolsa permanência para os participantes",
            "Iniciativa amplia a empregabilidade e a renda na Costa Doce"
        ],
        "angulo_editorial": "Serviço e desenvolvimento social em município da Costa Doce. Pauta utilitária de alto valor para a audiência (qualificação gratuita + auxílio). Fonte primária institucional (secretaria municipal). Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal do Trabalho, Cidadania e Assistência Social de Cerro Grande do Sul", "Prefeitura de Cerro Grande do Sul"],
        "lead_materia_longa": "Quem busca qualificação na Costa Doce tem uma nova oportunidade. A Prefeitura de Cerro Grande do Sul abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes.",
        "post_instagram": {
            "caption": "Capacitação gratuita e com auxílio. Cerro Grande do Sul abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes. A iniciativa é conduzida pela Secretaria Municipal do Trabalho, Cidadania e Assistência Social e busca ampliar a empregabilidade e a renda da população. Vale conferir os requisitos e prazos junto à secretaria, porque vagas assim costumam ter procura alta.",
            "hashtags": ["#CerroGrandedoSul", "#CostaDoce", "#Qualificação", "#Trabalho", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cursos gratuitos na Costa Doce.",
            "desenvolvimento_45s": "Cerro Grande do Sul abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes. A iniciativa é conduzida pela Secretaria Municipal do Trabalho, Cidadania e Assistência Social e tem como objetivo ampliar a empregabilidade e a renda da população. A bolsa permanência ajuda quem mais precisa a concluir a formação, reduzindo a evasão e o custo do deslocamento.",
            "fechamento_8s": "Oportunidade de qualificação na Costa Doce.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental otimista"
        },
        "tag_thumbnail": "Cursos gratuitos em Cerro Grande do Sul",
        "briefing_visual": {
            "descricao_pt": "Mãos em curso de qualificação profissional — bancada com ferramentas ou sala de aula de capacitação no interior do RS, sem rostos identificáveis",
            "query_en": ["vocational training workshop hands", "professional course classroom", "skills training tools"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Hands of a learner working at a vocational training bench with tools, bright practical classroom, no faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de alto valor (qualificação gratuita com auxílio) em município da Costa Doce, fonte primária institucional."
    },

    # IDX 4 — Arambaré Nota Técnica poda/arborização (Arambaré, serviço) — PUBLICAR
    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": {
        "titulo_sultv": "Arambaré publica Nota Técnica com orientações sobre poda e manejo da arborização urbana",
        "chamada_faixa": "Arambaré orienta poda de árvores",
        "subtitulo": "Documento da Prefeitura de Arambaré reúne orientações sobre o manejo correto da arborização urbana e a poda de árvores no município.",
        "lead": "A arborização urbana de Arambaré ganhou um guia oficial. A Prefeitura de Arambaré, cidade-núcleo da SulTV na Costa Doce, publicou uma Nota Técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município.",
        "ganchos_3": [
            "Arambaré publica Nota Técnica sobre arborização urbana",
            "Documento orienta o manejo correto e a poda de árvores",
            "Medida organiza o cuidado com as árvores no município"
        ],
        "angulo_editorial": "Serviço público e meio ambiente em cidade-núcleo (Arambaré). Pauta utilitária e institucional, fonte primária (prefeitura). Orienta o morador sobre conduta correta. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Arambaré", "Secretaria de Meio Ambiente de Arambaré"],
        "lead_materia_longa": "A arborização urbana de Arambaré ganhou um guia oficial. A Prefeitura de Arambaré, cidade-núcleo da SulTV na Costa Doce, publicou uma Nota Técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município.",
        "post_instagram": {
            "caption": "Cuidar das árvores também tem regra. A Prefeitura de Arambaré publicou uma Nota Técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município. O documento ajuda o morador a entender quando e como podar de forma correta, preservando a vegetação e a segurança nas vias. Arborização bem cuidada é sombra, qualidade do ar e cidade mais bonita para todos.",
            "hashtags": ["#Arambaré", "#CostaDoce", "#MeioAmbiente", "#Arborização", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Arambaré orienta a poda de árvores.",
            "desenvolvimento_45s": "A Prefeitura de Arambaré publicou uma Nota Técnica com orientações sobre o manejo da arborização urbana e a poda de árvores. O documento organiza o cuidado com a vegetação na cidade e ajuda o morador a entender quando e como podar de forma correta. A poda feita do jeito certo preserva a árvore, evita riscos nas vias e mantém a cidade mais verde e segura.",
            "fechamento_8s": "Arborização cuidada é qualidade de vida.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Arambaré orienta poda de árvores",
        "briefing_visual": {
            "descricao_pt": "Rua arborizada de cidade pequena do litoral lagunar do Rio Grande do Sul com árvores podadas e copas verdes, sem pessoas e sem rostos",
            "query_en": ["tree lined street urban", "tree pruning city", "green street trees brazil"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto", "motosserra em uso perigoso"],
            "prompt_ia": "A tree-lined urban street in a small southern Brazil lakeside town with healthy pruned trees and green canopy, daytime, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público e meio ambiente em cidade-núcleo (Arambaré), fonte primária (prefeitura). Pauta utilitária para o morador."
    },

    # IDX 8 — São Lourenço gestão recebe Sesc/Senac/Sindilojas (São Lourenço, economia) — PUBLICAR (nota_curta)
    "4a19f3b447abaaef75271b2e2dbf1a33ae46591b": {
        "titulo_sultv": "Gestão de São Lourenço do Sul recebe Sesc, Senac e Sindilojas para alinhar ações na cidade",
        "chamada_faixa": "São Lourenço articula ações com Sesc e Senac",
        "subtitulo": "Encontro reuniu representantes do Sesc Camaquã, do Senac e do Sindilojas para alinhar possíveis ações no município.",
        "lead": "São Lourenço do Sul busca novas parcerias para o comércio e os serviços. A gestão municipal recebeu representantes do Sesc Camaquã, do Senac e do Sindilojas para alinhar possíveis ações na cidade, na região da Costa Doce.",
        "ganchos_3": [
            "São Lourenço do Sul recebe Sesc, Senac e Sindilojas",
            "Encontro alinha possíveis ações para o município",
            "Parcerias miram o comércio e a qualificação local"
        ],
        "angulo_editorial": "Economia e desenvolvimento em cidade-núcleo (São Lourenço do Sul). Fato institucional concreto (encontro com entidades nomeadas), fonte primária (prefeitura). Formato nota curta — pauta de articulação. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Sindilojas", "Senac-RS", "Sesc-RS"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Articulação para movimentar a economia. A gestão de São Lourenço do Sul recebeu representantes do Sesc Camaquã, do Senac e do Sindilojas para alinhar possíveis ações na cidade. Encontros assim aproximam o poder público das entidades do comércio e da qualificação profissional, abrindo caminho para parcerias que fortalecem os serviços e geram oportunidades na Costa Doce.",
            "hashtags": ["#SãoLourençodoSul", "#CostaDoce", "#Economia", "#Comércio", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Parcerias em São Lourenço do Sul.",
            "desenvolvimento_45s": "A gestão de São Lourenço do Sul recebeu representantes do Sesc Camaquã, do Senac e do Sindilojas para alinhar possíveis ações na cidade. O encontro aproxima o poder público das entidades ligadas ao comércio e à qualificação profissional, abrindo caminho para parcerias que podem fortalecer os serviços e gerar novas oportunidades para a população da Costa Doce.",
            "fechamento_8s": "São Lourenço aposta em parcerias.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental corporativo leve"
        },
        "tag_thumbnail": "São Lourenço articula parcerias",
        "briefing_visual": {
            "descricao_pt": "Aperto de mãos ou mesa de reunião institucional em prédio público de cidade do interior do RS, representando parceria entre entidades, sem rostos identificáveis",
            "query_en": ["business handshake partnership", "institutional meeting table", "agreement cooperation office"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "A professional handshake over a meeting table symbolizing institutional partnership, neutral office setting, no faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Economia/desenvolvimento em cidade-núcleo (São Lourenço do Sul), fato institucional com entidades nomeadas. Post social.",
        "formato_sugerido": "post_instagram"
    },

    # IDX 13 — Cristal Rua Camaquã preparação calçamento (Cristal, obras) — PUBLICAR
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": {
        "titulo_sultv": "Rua Camaquã, em Cristal, recebe preparação para obras de calçamento",
        "chamada_faixa": "Cristal prepara calçamento da Rua Camaquã",
        "subtitulo": "Prefeitura de Cristal iniciou os serviços de preparação do terreno para o calçamento da Rua Camaquã.",
        "lead": "Mais uma rua de Cristal entra na fila do calçamento. A Prefeitura de Cristal, na região da Costa Doce, iniciou os serviços de preparação da Rua Camaquã para as futuras obras de pavimentação.",
        "ganchos_3": [
            "Rua Camaquã, em Cristal, recebe preparação para calçamento",
            "Serviços de terraplenagem antecedem a pavimentação",
            "Obra melhora a mobilidade no município"
        ],
        "angulo_editorial": "Obras e mobilidade urbana em cidade-núcleo (Cristal). Pauta de serviço, fonte primária (prefeitura). Concreto e de interesse direto do morador. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria de Obras de Cristal"],
        "lead_materia_longa": "Mais uma rua de Cristal entra na fila do calçamento. A Prefeitura de Cristal, na região da Costa Doce, iniciou os serviços de preparação da Rua Camaquã para as futuras obras de pavimentação.",
        "post_instagram": {
            "caption": "Cristal avança com mais calçamento. A Prefeitura iniciou os serviços de preparação da Rua Camaquã para as futuras obras de pavimentação. A etapa de terraplenagem antecede o calçamento e é o primeiro passo para melhorar a mobilidade, reduzir a poeira e a lama e valorizar a região. Obra de infraestrutura é qualidade de vida que chega ao dia a dia do morador.",
            "hashtags": ["#Cristal", "#CostaDoce", "#Obras", "#Infraestrutura", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Mais calçamento em Cristal.",
            "desenvolvimento_45s": "A Prefeitura de Cristal iniciou os serviços de preparação da Rua Camaquã para as futuras obras de calçamento. A etapa de terraplenagem é o primeiro passo da pavimentação e melhora a base da via. Quando concluída, a obra reduz a poeira e a lama, facilita o deslocamento de moradores e veículos e valoriza toda a região. Infraestrutura urbana é qualidade de vida que aparece no dia a dia.",
            "fechamento_8s": "Cristal investe em mobilidade urbana.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Calçamento da Rua Camaquã em Cristal",
        "briefing_visual": {
            "descricao_pt": "Rua de terra sendo preparada para calçamento com máquina de terraplenagem em cidade pequena do interior do RS, sem rostos identificáveis",
            "query_en": ["road construction earthworks small town", "street paving preparation", "cobblestone paving work"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "An unpaved street being prepared for cobblestone paving in a small southern Brazil town, construction earthworks and machinery, no people faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Obra urbana concreta em cidade-núcleo (Cristal), fonte primária (prefeitura). Interesse direto do morador."
    },

    # IDX 14 — Südoktoberfest São Lourenço contagem regressiva (São Lourenço, cultura/turismo) — PUBLICAR
    "9a0afe0a71110324f476128af3e817babce239d4": {
        "titulo_sultv": "Südoktoberfest abre contagem regressiva com lançamento oficial e concurso da corte",
        "chamada_faixa": "Südoktoberfest abre contagem regressiva",
        "subtitulo": "Tradicional festa de cultura germânica de São Lourenço do Sul iniciou a preparação com lançamento oficial e concurso para a corte.",
        "lead": "Uma das maiores festas da cultura germânica do Sul gaúcho já tem a engrenagem em movimento. A Südoktoberfest, de São Lourenço do Sul, na Costa Doce, abriu a contagem regressiva com o lançamento oficial e o concurso para a escolha da corte.",
        "ganchos_3": [
            "Südoktoberfest abre contagem regressiva em São Lourenço do Sul",
            "Lançamento oficial dá largada à preparação da festa",
            "Concurso vai escolher a corte do evento"
        ],
        "angulo_editorial": "Cultura e turismo em cidade-núcleo (São Lourenço do Sul). Evento tradicional de forte apelo regional e econômico (movimenta hotelaria, comércio e gastronomia). Pauta positiva. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Comissão organizadora da Südoktoberfest"],
        "lead_materia_longa": "Uma das maiores festas da cultura germânica do Sul gaúcho já tem a engrenagem em movimento. A Südoktoberfest, de São Lourenço do Sul, na Costa Doce, abriu a contagem regressiva com o lançamento oficial e o concurso para a escolha da corte.",
        "post_instagram": {
            "caption": "A festa já começou a ser construída. A Südoktoberfest, de São Lourenço do Sul, abriu a contagem regressiva com o lançamento oficial e o concurso para a escolha da corte. Celebração da cultura germânica que é marca registrada da Costa Doce, o evento movimenta a economia local, atrai visitantes e reúne tradição, música e gastronomia. Prepare a agenda: vem festa boa por aí.",
            "hashtags": ["#SãoLourençodoSul", "#Südoktoberfest", "#CostaDoce", "#Cultura", "#Turismo", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A Südoktoberfest começou a contagem regressiva.",
            "desenvolvimento_45s": "A Südoktoberfest, de São Lourenço do Sul, abriu a contagem regressiva com o lançamento oficial e o concurso para a escolha da corte. Tradicional celebração da cultura germânica na Costa Doce, a festa é um dos eventos mais aguardados da região. Além de preservar costumes, música e gastronomia, o evento movimenta a economia local, aquece a hotelaria e o comércio e atrai visitantes de todo o Rio Grande do Sul.",
            "fechamento_8s": "Tradição e economia em São Lourenço do Sul.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental festivo alemão"
        },
        "tag_thumbnail": "Südoktoberfest abre contagem regressiva",
        "briefing_visual": {
            "descricao_pt": "Elementos de festa de cultura germânica — canecas de chope, decoração azul e branca, acordeão — em festa típica do Sul do RS, sem rostos identificáveis",
            "query_en": ["oktoberfest beer mugs decoration", "german festival bavarian", "accordion folk festival"],
            "evitar": ["rostos identificáveis", "marcas de cerveja", "logos", "texto", "excesso de álcool"],
            "prompt_ia": "Festive German heritage celebration elements such as beer mugs and blue-white decorations on a wooden table, warm festival atmosphere, no people faces, no brand logos, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura e turismo em cidade-núcleo (São Lourenço do Sul), evento tradicional de forte apelo regional e econômico."
    },

    # IDX 20 — MetSul primeiro amanhecer inverno -4ºC (RS, clima) — PUBLICAR
    "055873b031808b741b618cba95d17d541d948a3e": {
        "titulo_sultv": "Primeiro amanhecer do inverno registra frio de 4ºC abaixo de zero no Sul gaúcho",
        "chamada_faixa": "Inverno começa com -4ºC no Sul",
        "subtitulo": "Início do inverno astronômico, neste domingo (21), trouxe mínimas abaixo de zero em várias regiões do Rio Grande do Sul.",
        "lead": "O inverno começou mostrando a que veio. O primeiro amanhecer do inverno astronômico, que teve início às 5h25 deste domingo (21), foi marcado por frio intenso e mínimas abaixo de zero no Rio Grande do Sul, com registro de até -4ºC no Sul gaúcho.",
        "ganchos_3": [
            "Primeiro amanhecer do inverno registra até -4ºC no Sul gaúcho",
            "Inverno astronômico começou às 5h25 deste domingo (21)",
            "Frio intenso traz mínimas abaixo de zero no Rio Grande do Sul"
        ],
        "angulo_editorial": "Clima e serviço — pauta estadual com forte ancoragem no Sul gaúcho (área de cobertura SulTV). Fato concreto, recente, dado quantitativo. Relevante para o produtor rural (geada) e para a população urbana. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Emater/RS", "Defesa Civil RS"],
        "lead_materia_longa": "O inverno começou mostrando a que veio. O primeiro amanhecer do inverno astronômico, que teve início às 5h25 deste domingo (21), foi marcado por frio intenso e mínimas abaixo de zero no Rio Grande do Sul, com registro de até -4ºC no Sul gaúcho.",
        "post_instagram": {
            "caption": "O inverno chegou pra valer. O primeiro amanhecer do inverno astronômico, neste domingo (21), trouxe frio intenso e mínimas abaixo de zero no Rio Grande do Sul, com registro de até -4ºC no Sul gaúcho. O frio forte pede atenção redobrada com a saúde, com os animais e com as lavouras, onde a geada pode afetar a produção. Agasalho na mão e cuidado com quem é mais sensível ao frio.",
            "hashtags": ["#RioGrandedoSul", "#Inverno", "#Frio", "#Clima", "#Geada", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O inverno chegou com frio de -4ºC.",
            "desenvolvimento_45s": "O primeiro amanhecer do inverno astronômico, que começou às 5h25 deste domingo, foi marcado por frio intenso e mínimas abaixo de zero no Rio Grande do Sul, com registro de até quatro graus negativos no Sul gaúcho. O frio forte pede atenção com a saúde, com os animais e com as lavouras, onde a geada pode afetar a produção. A semana segue com madrugadas geladas em boa parte do estado.",
            "fechamento_8s": "Atenção redobrada com o frio no Sul.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental invernal suave"
        },
        "tag_thumbnail": "Inverno começa com -4ºC no Sul",
        "briefing_visual": {
            "descricao_pt": "Campo coberto de geada ao amanhecer no Sul do Rio Grande do Sul, capim branco de gelo e sol baixo no horizonte, sem pessoas",
            "query_en": ["frost field sunrise", "frozen grass winter morning", "frost rural landscape"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto", "neve de montanha estrangeira"],
            "prompt_ia": "A rural field covered in white morning frost at sunrise in southern Brazil, low golden sun on the horizon, frozen grass, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima de serviço com ancoragem regional Sul gaúcho, dado quantitativo concreto (-4ºC), relevante para produtor rural (geada) e população urbana."
    },

    # IDX 24 — UFSM usina solar autossuficiência (Santa Maria, inovação/energia) — PUBLICAR
    "45918557b425ac5a5aa05a3264a94d0abb447dc7": {
        "titulo_sultv": "Com usina solar de 910 painéis, campus da UFSM atinge autossuficiência energética",
        "chamada_faixa": "Usina solar dá autossuficiência a campus da UFSM",
        "subtitulo": "Estrutura com 910 painéis fotovoltaicos é a primeira a abastecer integralmente um campus da universidade no Rio Grande do Sul.",
        "lead": "São 910 painéis fotovoltaicos transformando sol em independência energética. Com a entrada em operação de uma usina solar, um campus da Universidade Federal de Santa Maria (UFSM) atingiu a autossuficiência energética — a primeira estrutura a abastecer integralmente um campus da instituição no Rio Grande do Sul.",
        "ganchos_3": [
            "Usina solar de 910 painéis dá autossuficiência a campus da UFSM",
            "É a primeira estrutura a abastecer integralmente um campus da universidade",
            "Energia limpa reduz custos e emissões no Rio Grande do Sul"
        ],
        "angulo_editorial": "Inovação, energia limpa e sustentabilidade no Rio Grande do Sul — pauta alinhada ao posicionamento editorial da SulTV (tecnologia + agro + futuro). Fato concreto e quantitativo, fonte primária (universidade). Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Universidade Federal de Santa Maria (UFSM)"],
        "lead_materia_longa": "São 910 painéis fotovoltaicos transformando sol em independência energética. Com a entrada em operação de uma usina solar, um campus da Universidade Federal de Santa Maria (UFSM) atingiu a autossuficiência energética — a primeira estrutura a abastecer integralmente um campus da instituição no Rio Grande do Sul.",
        "post_instagram": {
            "caption": "Sol que vira energia e economia. Com a entrada em operação de uma usina solar de 910 painéis fotovoltaicos, um campus da UFSM atingiu a autossuficiência energética — o primeiro a abastecer integralmente um campus da universidade. A iniciativa mostra o caminho da energia limpa para reduzir custos e emissões, um exemplo de inovação e sustentabilidade que inspira o agro e as cidades do Rio Grande do Sul.",
            "hashtags": ["#SantaMaria", "#EnergiaSolar", "#Inovação", "#Sustentabilidade", "#RioGrandedoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Energia solar movendo um campus inteiro.",
            "desenvolvimento_45s": "Com a entrada em operação de uma usina solar de 910 painéis fotovoltaicos, um campus da Universidade Federal de Santa Maria atingiu a autossuficiência energética. É a primeira estrutura a abastecer integralmente um campus da instituição no Rio Grande do Sul. A iniciativa reduz custos e emissões e mostra o potencial da energia limpa, um caminho que interessa também ao agro e às cidades que buscam sustentabilidade.",
            "fechamento_8s": "Inovação e energia limpa no RS.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental tecnológico otimista"
        },
        "tag_thumbnail": "Usina solar dá autossuficiência a campus",
        "briefing_visual": {
            "descricao_pt": "Vista ampla de fileiras de painéis solares fotovoltaicos sob céu azul no interior do Rio Grande do Sul, sem pessoas",
            "query_en": ["solar panels farm field", "photovoltaic array blue sky", "solar energy installation"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Wide view of rows of photovoltaic solar panels under a clear blue sky in southern Brazil, clean energy installation, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Inovação e energia limpa no RS, alinhado ao posicionamento editorial SulTV. Fato concreto e quantitativo (910 painéis), fonte primária (universidade).",
        "formato_sugerido": "materia_longa"
    },

    # ===== REBAIXAR =====
    # IDX 5 — Arambaré cursos gratuitos (16 abril) — REBAIXAR (notícia antiga, ~2 meses)
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "REBAIXAR", "Conteúdo defasado (publicado em 16 de abril, ~2 meses). Inscrições provavelmente encerradas — vira nota interna."),
    # IDX 11 — Barra do Ribeiro Velejaço solidário — REBAIXAR (título truncado, sem corpo)
    "93d8797025ffe98d7c47bb3b29fd426a9dec54b2": _skip(
        "REBAIXAR", "Título truncado de cabeçalho de seção e sem corpo aproveitável — sem condições de matéria; vira nota interna."),
    # IDX 12 — Barra do Ribeiro servidores contracheques — (BLOQUEAR abaixo, procedural)
    # IDX 15 — Rodeio Artístico Lajeado/Enart — REBAIXAR (Vale do Taquari, fora do núcleo Costa Doce)
    "cb740c1e97caad530e0f26886145af0f31bbed77": _skip(
        "REBAIXAR", "Evento em Lajeado (Vale do Taquari), fora da área-núcleo da Costa Doce — sem âncora regional forte."),
    # IDX 16 — Cristal Av Passo do Mendonça limpeza — REBAIXAR (2º item de obras de Cristal, evita repetição)
    "804da2cbe08274dd604274d8db6acc48cc218fed": _skip(
        "REBAIXAR", "Segundo item de serviço urbano de Cristal no mesmo dia — para evitar repetição, prevalece o calçamento da Rua Camaquã; vira nota."),
    # IDX 17 — Pelotas concurso magistério (13 maio) — REBAIXAR (procedural + defasado)
    "0c78bd0cc00e7d0302fc635b3fdbfbd510252753": _skip(
        "REBAIXAR", "Resultado de concurso com data de maio — procedural e defasado; vira nota interna."),
    # IDX 18 — ALERS concessões/privatizações/PPPs — REBAIXAR (estadual, viés político)
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "REBAIXAR", "Debate legislativo estadual sobre concessões/privatizações com viés político-partidário — fora do escopo editorial; descartado da publicação."),
    # IDX 19 — ALERS Funcriança destinação recursos — REBAIXAR (estadual técnico, sem âncora núcleo)
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR", "Pauta técnica estadual sem âncora em cidade-núcleo — baixo apelo para a audiência regional; vira nota."),
    # IDX 22 — MetSul quarta frio e geada — REBAIXAR (clima duplicado)
    "b0889a9f85770aca01833915dbfe96c99e135c06": _skip(
        "REBAIXAR", "Pauta de clima duplicada — o frio do início do inverno já é a matéria de clima do dia; vira nota."),
    # IDX 23 — MetSul semana de madrugadas frias — REBAIXAR (clima duplicado)
    "892cde7b48dd63105d731d9788fe695189b3109d": _skip(
        "REBAIXAR", "Pauta de clima duplicada — consolidada na matéria do primeiro amanhecer do inverno; vira nota."),
    # IDX 25 — UFSM minicurso coleções musealizadas — REBAIXAR (acadêmico de nicho)
    "10ecbe665aec1d1df677b64e8269a3a8da82defa": _skip(
        "REBAIXAR", "Minicurso acadêmico de nicho, baixo apelo para a audiência ampla — vira post."),
    # IDX 26 — Venâncio Aires apostas premiadas — REBAIXAR (fora do núcleo, leve)
    "e0d0dea1242b86e974476f1a79179a408edccaeb": _skip(
        "REBAIXAR", "Premiação de loteria em Venâncio Aires (Vale do Taquari), fora do núcleo e de baixo valor editorial — vira post."),
    # IDX 28 — Bento Gonçalves Grupo Tholl — REBAIXAR (Serra, fora do núcleo)
    "3303bd756d041efbdd09329cb79d692ab1c0f186": _skip(
        "REBAIXAR", "Evento cultural na Serra (Bento Gonçalves), fora da área-núcleo da Costa Doce — vira post."),

    # ===== BLOQUEAR =====
    # IDX 6 — Chuvisca EDITAL DE PENALIDADE — BLOQUEAR (edital procedural)
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR", "Edital de penalidade — documento procedural administrativo, não é pauta jornalística."),
    # IDX 7 — Chuvisca EDITAL Nº 002/2026 perímetro urbano — BLOQUEAR (edital procedural)
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR", "Edital de prazo para requerimentos — documento procedural administrativo."),
    # IDX 9 — Sentinela do Sul AVISO DE AUDIÊNCIA PÚBLICA — BLOQUEAR (aviso procedural sem substância)
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR", "Aviso de audiência pública sem conteúdo substantivo (apenas o cabeçalho) — procedural."),
    # IDX 10 — Sentinela do Sul EMISSÃO DE NOTAS FISCAIS — BLOQUEAR (procedural + defasado)
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR", "Comunicado administrativo procedural (emissor nacional de NF), com data de maio — defasado e sem valor de pauta."),
    # IDX 12 — Barra do Ribeiro servidores revisem contracheques — BLOQUEAR (título de seção administrativa)
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": _skip(
        "BLOQUEAR", "Comunicado administrativo interno (revisão de contracheques) — título de seção, sem valor de pauta."),
    # IDX 21 — MetSul ciclone tropical Copa do Mundo — BLOQUEAR (internacional/esporte distante)
    "a6683f9edcfc9c862dd9febe7d25aba45d237a5d": _skip(
        "BLOQUEAR", "Pauta internacional/esportiva (ciclone na Copa do Mundo), sem âncora regional no Sul-RS."),
    # IDX 27 — Venâncio Aires PRF apreende maconha Lajeado — BLOQUEAR (crime fora núcleo, drogas)
    "a113b03cadb243d98e220586440297eff38981b5": _skip(
        "BLOQUEAR", "Apreensão de drogas em Lajeado (Vale do Taquari), fora da área-núcleo — sem âncora regional Costa Doce."),
    # IDX 29 — Bento Gonçalves Brasil x Haiti Copa — BLOQUEAR (esporte nacional/internacional)
    "aa37bd78ee0d26f86c207bb19fea7723b444aea7": _skip(
        "BLOQUEAR", "Resultado de jogo da Seleção na Copa do Mundo — esporte nacional/internacional, sem âncora regional."),
}


MATERIAS = {

    "afdf6218ab7085cf383e86deefa5f40a87987f87": """### Título ###
Liga Feminina de Combate ao Câncer de Camaquã completa 40 anos com sede própria

### Artigo ###
São 40 anos de trabalho voluntário ao lado de quem mais precisa. A Liga Feminina de Combate ao Câncer de Camaquã, na região da Costa Doce, chega a quatro décadas de atuação com a conclusão de sua sede própria e a ampliação do atendimento aos assistidos. O marco coroa uma trajetória construída por mãos voluntárias, que fizeram da entidade uma referência de apoio e solidariedade no município. Ao longo desses anos, a Liga se firmou como um ponto de acolhimento para famílias que enfrentam um dos momentos mais delicados da vida. O trabalho da entidade vai além do amparo material: oferece escuta, companhia e orientação a quem percorre a jornada do tratamento, fortalecendo o senso de comunidade em torno de uma causa que toca a todos. A conquista da sede própria representa um salto de organização e perenidade. Com espaço adequado, a entidade amplia a capacidade de atendimento, organiza melhor as ações e garante continuidade ao trabalho que depende da dedicação de voluntárias e do apoio da população. Para marcar as quatro décadas, a Liga prepara uma programação especial, que celebra a história construída e reafirma o compromisso com os próximos anos. A trajetória da entidade é também a história de solidariedade de Camaquã, uma cidade que aprendeu a se mobilizar pelo próximo. Iniciativas como essa mostram a força do voluntariado e a importância de valorizar quem se dedica, de forma silenciosa e constante, a cuidar das pessoas. Aos 40 anos, a Liga Feminina de Combate ao Câncer renova o convite para que a comunidade siga ao seu lado, sustentando uma rede de apoio que faz diferença real na vida de muitas famílias da Costa Doce.

### Legenda sugerida ###
Liga Feminina de Combate ao Câncer de Camaquã celebra 40 anos com a conclusão da sede própria e a ampliação do atendimento.

### Palavras-chave ###
Liga Feminina de Combate ao Câncer, Camaquã, 40 anos, voluntariado, solidariedade, Costa Doce, comunidade
""",

    "b19a7c0521b9e9bca8fbc770a59fdf2b644f4a67": """### Título ###
Conselho Municipal de Inovação de Camaquã quer ampliar participação da comunidade

### Artigo ###
Camaquã quer transformar inovação em política pública permanente. O Conselho Municipal de Inovação da cidade, na região da Costa Doce, definiu como prioridade ampliar a participação da comunidade e fortalecer projetos locais, com destaque para a criação do Fundo Municipal de Inovação. A nova gestão do conselho aposta na aproximação com escolas, empresas e universidades como caminho para estimular o desenvolvimento de soluções voltadas aos desafios do município. A medida acompanha um movimento que ganha força no interior do Rio Grande do Sul: o de tratar inovação e tecnologia não como temas distantes dos grandes centros, mas como ferramentas concretas de desenvolvimento regional. Ao envolver a comunidade, o conselho busca identificar problemas reais da cidade e conectar quem tem ideias a quem pode executá-las. A criação do Fundo Municipal de Inovação é um passo estratégico. Um fundo dedicado dá previsibilidade ao financiamento de projetos, permite apoiar iniciativas de empreendedores e estudantes e sinaliza que o município está disposto a investir em tecnologia, empreendedorismo e qualificação. A aproximação com escolas e universidades, por sua vez, ajuda a formar talentos e a reter jovens na região. O fortalecimento do ecossistema de inovação tende a gerar efeitos que vão além da tecnologia. Iniciativas desse tipo estimulam novos negócios, modernizam o setor produtivo, agregam valor ao agro e aos serviços e abrem oportunidades de emprego e renda. Para uma cidade-núcleo da Costa Doce, apostar na inovação é também apostar no próprio futuro. Ao ampliar a participação da comunidade, o conselho reforça que o desenvolvimento se constrói de forma coletiva, ouvindo quem vive a cidade e quer ajudar a transformá-la.

### Legenda sugerida ###
Conselho Municipal de Inovação de Camaquã prioriza a participação da comunidade e a criação do Fundo Municipal de Inovação.

### Palavras-chave ###
Conselho Municipal de Inovação, Camaquã, inovação, Fundo Municipal de Inovação, tecnologia, Costa Doce, desenvolvimento
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
Cerro Grande do Sul abre inscrições para cursos gratuitos de qualificação com bolsa permanência

### Artigo ###
Quem busca qualificação na Costa Doce tem uma nova oportunidade. A Prefeitura de Cerro Grande do Sul abriu inscrições para dois cursos gratuitos de qualificação profissional, com bolsa permanência para os participantes. A iniciativa é conduzida pela Secretaria Municipal do Trabalho, Cidadania e Assistência Social e tem como objetivo ampliar a empregabilidade e a renda da população local. A oferta de capacitação gratuita é uma ferramenta importante de desenvolvimento social e econômico. Ao qualificar a mão de obra do município, a medida prepara os trabalhadores para novas oportunidades, atende a demandas do mercado e contribui para reduzir as desigualdades de acesso à formação profissional. O diferencial da bolsa permanência merece destaque. O auxílio ajuda a garantir que os participantes consigam concluir os cursos, reduzindo a evasão provocada por dificuldades financeiras e custos de deslocamento. É um incentivo concreto para que a qualificação chegue a quem mais precisa, transformando a boa intenção em resultado efetivo. Programas como esse fortalecem a economia local a partir das pessoas. Trabalhadores mais capacitados têm melhores condições de conquistar emprego, empreender e aumentar a renda familiar, movimentando o comércio e os serviços do município. Para o poder público, investir em qualificação é semear desenvolvimento de médio e longo prazo, com retorno que se espalha por toda a comunidade. A recomendação é que os interessados verifiquem os requisitos, prazos e a forma de inscrição junto à secretaria responsável. Iniciativas de qualificação costumam ter vagas limitadas, e a procura tende a ser alta justamente pelo caráter gratuito e pelo apoio oferecido aos participantes ao longo da formação.

### Legenda sugerida ###
Cerro Grande do Sul abre inscrições para dois cursos gratuitos de qualificação profissional com bolsa permanência.

### Palavras-chave ###
Cerro Grande do Sul, cursos gratuitos, qualificação profissional, bolsa permanência, trabalho, renda, Costa Doce
""",

    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": """### Título ###
Arambaré publica Nota Técnica com orientações sobre poda e manejo da arborização urbana

### Artigo ###
A arborização urbana de Arambaré ganhou um guia oficial. A Prefeitura de Arambaré, cidade-núcleo da Costa Doce, publicou uma Nota Técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município. O documento organiza o cuidado com a vegetação nas vias públicas e ajuda o morador a entender quando e como agir de forma correta. A arborização das cidades cumpre um papel que vai muito além do visual. As árvores oferecem sombra, ajudam a reduzir a temperatura, melhoram a qualidade do ar, abrigam a fauna e tornam os espaços urbanos mais agradáveis. Cuidar desse patrimônio, no entanto, exige técnica: uma poda malfeita pode comprometer a saúde da árvore, gerar riscos de queda de galhos e até prejudicar a rede elétrica e a circulação. Ao publicar orientações claras, a administração municipal busca padronizar condutas e evitar intervenções inadequadas. A Nota Técnica funciona como referência tanto para as equipes que atuam na manutenção quanto para os moradores que precisam lidar com árvores em frente às suas residências. Saber a quem recorrer, em que época podar e quais cuidados tomar evita problemas e preserva a vegetação. A medida também reforça a importância de tratar a arborização como política pública permanente, e não como ação pontual. O equilíbrio entre o desenvolvimento urbano e a preservação das árvores é um desafio constante das cidades, e a orientação à população é parte essencial desse trabalho. Para os moradores de Arambaré, a recomendação é consultar as orientações da prefeitura antes de qualquer intervenção e buscar a secretaria responsável em caso de dúvidas. Uma cidade bem arborizada é mais bonita, mais fresca e com mais qualidade de vida para todos.

### Legenda sugerida ###
Prefeitura de Arambaré publica Nota Técnica com orientações sobre o manejo da arborização urbana e a poda de árvores.

### Palavras-chave ###
Arambaré, Nota Técnica, arborização urbana, poda de árvores, meio ambiente, Costa Doce, serviço público
""",

    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": """### Título ###
Rua Camaquã, em Cristal, recebe preparação para obras de calçamento

### Artigo ###
Mais uma rua de Cristal entra na fila do calçamento. A Prefeitura de Cristal, na região da Costa Doce, iniciou os serviços de preparação da Rua Camaquã para as futuras obras de pavimentação. A etapa atual, de organização e nivelamento do terreno, é o primeiro passo de um processo que melhora a base da via e prepara o trecho para receber o calçamento. As obras de pavimentação têm impacto direto no dia a dia da população. Uma rua calçada reduz a poeira no tempo seco e a lama nos períodos de chuva, facilita o deslocamento de moradores e veículos, melhora o acesso de serviços essenciais e valoriza os imóveis da região. Para quem vive na localidade, a chegada do calçamento representa mais conforto e dignidade. O investimento em infraestrutura urbana é também um sinal de planejamento. A preparação adequada do terreno antes da pavimentação é fundamental para garantir a durabilidade da obra e evitar problemas futuros, como afundamentos e acúmulo de água. Executar cada etapa com cuidado é o que assegura que o recurso público se traduza em uma estrutura sólida e duradoura. Obras como essa costumam atender a antigas demandas das comunidades. A pavimentação de vias é uma das reivindicações mais frequentes dos moradores do interior, justamente por mudar de forma concreta a rotina de quem precisa transitar diariamente por ruas sem calçamento. Com a preparação da Rua Camaquã, Cristal avança em sua agenda de melhorias urbanas. A expectativa é que, concluída a pavimentação, a via ofereça mais segurança e qualidade de vida aos moradores, somando-se ao conjunto de obras que transformam aos poucos a infraestrutura do município.

### Legenda sugerida ###
Prefeitura de Cristal inicia a preparação da Rua Camaquã para as futuras obras de calçamento.

### Palavras-chave ###
Cristal, Rua Camaquã, calçamento, pavimentação, obras, infraestrutura, Costa Doce
""",

    "9a0afe0a71110324f476128af3e817babce239d4": """### Título ###
Südoktoberfest abre contagem regressiva com lançamento oficial e concurso da corte

### Artigo ###
Uma das maiores festas da cultura germânica do Sul gaúcho já tem a engrenagem em movimento. A Südoktoberfest, de São Lourenço do Sul, na Costa Doce, abriu a contagem regressiva com o lançamento oficial do evento e o concurso para a escolha da corte. A largada antecipada mostra o tamanho da preparação que envolve uma celebração desse porte. Tradicional na região, a Südoktoberfest é mais do que uma festa: é uma vitrine da identidade cultural de São Lourenço do Sul, cidade marcada pela forte herança dos imigrantes alemães. A programação costuma reunir música, dança, gastronomia típica e tradições preservadas ao longo de gerações, atraindo moradores e visitantes de todo o Rio Grande do Sul. O lançamento oficial dá início à fase de mobilização, em que comissões, voluntários e parceiros se organizam para garantir a realização do evento. Já o concurso da corte é um dos momentos mais aguardados, por envolver a comunidade na escolha das representantes que serão o rosto da festa e ajudarão a divulgá-la. Além do valor cultural, a Südoktoberfest tem peso econômico relevante. Eventos desse tipo aquecem a hotelaria, a gastronomia, o comércio e os serviços, gerando renda e emprego temporário e projetando a cidade como destino turístico. Para São Lourenço do Sul, a festa é um motor que movimenta a economia e reforça a marca do município. Ao abrir a contagem regressiva, a organização sinaliza que a tradição segue viva e que a cidade já se prepara para receber mais uma edição. Para quem aprecia cultura, música e boa mesa, fica o convite para acompanhar os próximos passos e reservar a agenda para uma das celebrações mais queridas da Costa Doce.

### Legenda sugerida ###
Südoktoberfest, de São Lourenço do Sul, abre a contagem regressiva com lançamento oficial e concurso da corte.

### Palavras-chave ###
Südoktoberfest, São Lourenço do Sul, cultura germânica, festa, turismo, Costa Doce, concurso da corte
""",

    "055873b031808b741b618cba95d17d541d948a3e": """### Título ###
Primeiro amanhecer do inverno registra frio de 4ºC abaixo de zero no Sul gaúcho

### Artigo ###
O inverno começou mostrando a que veio. O primeiro amanhecer do inverno astronômico, que teve início às 5h25 deste domingo (21), foi marcado por frio intenso e mínimas abaixo de zero no Rio Grande do Sul, com registro de até 4ºC abaixo de zero no Sul gaúcho. A chegada da estação mais fria do ano se fez sentir logo nas primeiras horas, com termômetros despencando em várias regiões do estado. O frio rigoroso é típico do período, mas exige atenção redobrada da população. As temperaturas negativas representam riscos à saúde, sobretudo para idosos, crianças e pessoas em situação de vulnerabilidade. Manter-se agasalhado, evitar a exposição prolongada ao frio e cuidar do aquecimento dos ambientes são medidas importantes para atravessar os dias mais gelados com segurança. No campo, o frio acende o sinal de alerta para a geada. A formação de gelo sobre a vegetação pode afetar lavouras e pastagens, comprometendo a produção e exigindo cuidados específicos dos produtores. Para a pecuária, as baixas temperaturas também demandam atenção com os animais, principalmente os mais jovens e sensíveis, que precisam de abrigo e alimentação adequada. O frio intenso costuma vir acompanhado de tempo firme e céu aberto, condições que favorecem justamente as madrugadas mais geladas, quando o calor se dissipa com mais facilidade. A tendência é de que os dias seguintes mantenham o padrão de manhãs frias em boa parte do Rio Grande do Sul. Diante do cenário, a recomendação é simples e vale para todos: redobrar o cuidado com a saúde, proteger quem é mais sensível ao frio, abrigar os animais e acompanhar as condições do tempo para se planejar. O inverno está apenas começando, e o Sul já sente o seu rigor.

### Legenda sugerida ###
Primeiro amanhecer do inverno traz mínimas abaixo de zero no Rio Grande do Sul, com até -4ºC no Sul gaúcho.

### Palavras-chave ###
inverno, frio, Rio Grande do Sul, Sul gaúcho, geada, clima, temperaturas negativas
""",

    "45918557b425ac5a5aa05a3264a94d0abb447dc7": """### Título ###
Com usina solar de 910 painéis, campus da UFSM atinge autossuficiência energética

### Artigo ###
São 910 painéis fotovoltaicos transformando sol em independência energética. Com a entrada em operação de uma usina solar, um campus da Universidade Federal de Santa Maria (UFSM) atingiu a autossuficiência energética — a primeira estrutura a abastecer integralmente um campus da instituição no Rio Grande do Sul. O marco coloca a universidade na vanguarda da transição para fontes de energia limpa. A iniciativa tem valor simbólico e prático. Com a geração própria de energia, o campus reduz a dependência da rede convencional, diminui custos com a conta de luz e corta emissões de gases de efeito estufa, contribuindo para metas de sustentabilidade. O investimento se paga ao longo do tempo e libera recursos que podem ser direcionados a outras prioridades da instituição. A energia solar fotovoltaica vem ganhando espaço no Rio Grande do Sul, estado de forte tradição agrícola e com grande potencial para a geração distribuída. Propriedades rurais, agroindústrias, escolas e prédios públicos têm encontrado na tecnologia uma forma de reduzir gastos e ganhar autonomia, especialmente em regiões onde a energia representa um peso importante no custo de produção. O exemplo da universidade tem efeito multiplicador. Ao demonstrar que é possível abastecer integralmente uma estrutura de grande porte com energia limpa, a iniciativa serve de referência para outras instituições, empresas e produtores que avaliam investir em geração própria. O conhecimento gerado e a experiência acumulada também podem se transformar em pesquisa, ensino e extensão, beneficiando a formação de profissionais. A autossuficiência energética conquistada pelo campus é um sinal dos tempos. Em um cenário de busca por sustentabilidade e eficiência, unir inovação, economia e responsabilidade ambiental deixa de ser uma promessa distante para se tornar realidade concreta no Rio Grande do Sul.

### Legenda sugerida ###
Usina solar de 910 painéis fotovoltaicos torna um campus da UFSM autossuficiente em energia, o primeiro da universidade no RS.

### Palavras-chave ###
UFSM, usina solar, energia fotovoltaica, autossuficiência energética, energia limpa, sustentabilidade, Rio Grande do Sul
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
