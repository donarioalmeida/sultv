#!/usr/bin/env python3
"""
angular_2026-06-24.py — angulação editorial + redação (cowork-faz-tudo).
Decisões editoriais Claude na sessão para a pauta de 2026-06-24.
Regra 12 INEGOCIÁVEL: nenhum texto menciona veículos/portais/rádios/jornais.
Atribuição apenas a fontes primárias institucionais.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-24"


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

    # IDX 0 — INSS amplia biometria (Camaquã) — PUBLICAR
    "10bf0cd9c375743e5d520e49a20fec647849b75a": {
        "titulo_sultv": "INSS amplia exigência de biometria para benefícios; veja o que muda para o segurado",
        "chamada_faixa": "Biometria do INSS muda regras para segurados",
        "subtitulo": "Novas regras ampliam o cadastro biométrico na concessão de benefícios; segurados da Costa Doce devem manter o cadastro em dia.",
        "lead": "Quem depende de um benefício previdenciário precisa ficar atento. O Instituto Nacional do Seguro Social ampliou a exigência de cadastro biométrico para a concessão de benefícios, mudança que atinge diretamente os segurados de Camaquã e de toda a Costa Doce e exige atenção para evitar atrasos na liberação do pagamento.",
        "ganchos_3": [
            "INSS amplia exigência de biometria na concessão de benefícios",
            "Mudança atinge segurados de Camaquã e região",
            "Manter o cadastro em dia evita atrasos no pagamento"
        ],
        "angulo_editorial": "Serviço de utilidade pública de alto alcance para a audiência. Fato concreto e institucional (INSS). Ângulo regional: impacto direto sobre segurados da Costa Doce. Sem viés partidário. Atribuição apenas ao INSS.",
        "fontes_complementares_sugeridas": ["INSS — Instituto Nacional do Seguro Social", "Agências da Previdência Social no Sul do RS"],
        "lead_materia_longa": "Quem depende de um benefício previdenciário precisa ficar atento. O Instituto Nacional do Seguro Social ampliou a exigência de cadastro biométrico para a concessão de benefícios, mudança que atinge diretamente os segurados de Camaquã e de toda a Costa Doce.",
        "post_instagram": {
            "caption": "Atenção, segurado: o INSS ampliou a exigência de biometria para a concessão de benefícios. A mudança vale para quem vai pedir aposentadoria, pensão e outros benefícios, e tem como objetivo dar mais segurança e reduzir fraudes. Para a população da Costa Doce, o recado é simples: manter os dados em dia evita dor de cabeça e atrasos na hora de liberar o pagamento. Antes de dar entrada em qualquer benefício, vale conferir a situação do cadastro e reunir os documentos necessários. Informação no tempo certo é o que garante o direito sem surpresas.",
            "hashtags": ["#INSS", "#Camaquã", "#CostaDoce", "#Previdência", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Atenção, segurado do INSS.",
            "desenvolvimento_45s": "O Instituto Nacional do Seguro Social ampliou a exigência de cadastro biométrico para a concessão de benefícios. A mudança vale para quem vai pedir aposentadoria, pensão e outros benefícios, e tem como objetivo dar mais segurança e reduzir fraudes. Para a população de Camaquã e da Costa Doce, o recado é manter os dados em dia, conferir a situação do cadastro e reunir a documentação antes de dar entrada. Assim, o benefício é liberado sem atrasos.",
            "fechamento_8s": "Cadastro em dia, direito garantido.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo sóbrio"
        },
        "tag_thumbnail": "INSS biometria, benefícios",
        "briefing_visual": {
            "descricao_pt": "Fachada de uma agência da Previdência Social no interior do Rio Grande do Sul, atendimento ao público, sem rostos identificáveis",
            "query_en": ["social security office building", "government service counter brazil", "public office facade documents"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Exterior of a public social security service office in a small Brazilian town, neutral institutional building, daytime, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de utilidade pública de alto alcance, fato institucional do INSS com impacto direto sobre segurados da Costa Doce. Cidade-núcleo (Camaquã)."
    },

    # IDX 1 — Jardel Garcia / Clic Cast (Camaquã) — BLOQUEAR (promoção de programa de veículo)
    "a12103a607e35c3ecd2762477e9049bb889551c9": _skip(
        "BLOQUEAR", "Divulgação de podcast/programa de veículo de comunicação. Regra 12 — nenhuma promoção de produto editorial de terceiros."),

    # IDX 2 — Affair de Ana Castela / javalis (Tapes) — REBAIXAR
    "864c17a43f606d0da71336f8c01882c64619a3f9": _skip(
        "REBAIXAR", "Enquadramento de celebridade/influenciador, tom sensacionalista e sem âncora concreta em cidade-núcleo. Controle de javali é insumo agro, mas a pauta não se sustenta."),

    # IDX 3 — iPhone 17 Pro Mercado Livre (Tapes) — BLOQUEAR (conteúdo comercial/anúncio)
    "a8e46f6dbf592402c99b5ed89b1f156d1401f468": _skip(
        "BLOQUEAR", "Conteúdo comercial/anúncio de e-commerce nacional, sem valor jornalístico regional."),

    # IDX 4 — Arambaré Nota Técnica poda de árvores — PUBLICAR
    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": {
        "titulo_sultv": "Arambaré publica nota técnica com orientações para a poda de árvores na cidade",
        "chamada_faixa": "Arambaré orienta sobre poda e arborização urbana",
        "subtitulo": "Diretoria de Meio Ambiente divulga a Nota Técnica nº 01/2026 com diretrizes para o manejo da arborização urbana.",
        "lead": "O cuidado com as árvores da cidade ganhou regras claras em Arambaré. A Diretoria Municipal de Meio Ambiente publicou a Nota Técnica nº 01/2026, que reúne orientações sobre o manejo da arborização urbana e a poda de árvores no município, na orla da Lagoa dos Patos, para que moradores e equipes públicas atuem de forma segura e correta.",
        "ganchos_3": [
            "Nota Técnica nº 01/2026 orienta o manejo da arborização urbana",
            "Documento define como fazer a poda de árvores no município",
            "Objetivo é conciliar segurança, paisagem urbana e meio ambiente"
        ],
        "angulo_editorial": "Serviço de utilidade pública em cidade-núcleo, com fonte primária institucional (Diretoria de Meio Ambiente). Fato concreto, orienta o cidadão e previne acidentes. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Diretoria Municipal de Meio Ambiente de Arambaré", "Prefeitura de Arambaré"],
        "lead_materia_longa": "O cuidado com as árvores da cidade ganhou regras claras em Arambaré. A Diretoria Municipal de Meio Ambiente publicou a Nota Técnica nº 01/2026, que reúne orientações sobre o manejo da arborização urbana e a poda de árvores no município.",
        "post_instagram": {
            "caption": "Poda de árvore tem hora e jeito certo de ser feita. Em Arambaré, a Diretoria Municipal de Meio Ambiente publicou uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município. O objetivo é conciliar a segurança das pessoas, a preservação da paisagem e o cuidado com o meio ambiente, evitando podas irregulares que prejudicam as árvores e a cidade. Antes de mexer na vegetação, vale conhecer as regras e procurar orientação. Árvore bem cuidada é qualidade de vida para todo mundo.",
            "hashtags": ["#Arambaré", "#MeioAmbiente", "#ArborizaçãoUrbana", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Poda de árvore tem regra.",
            "desenvolvimento_45s": "Em Arambaré, a Diretoria Municipal de Meio Ambiente publicou a Nota Técnica nº 01/2026, com orientações sobre o manejo da arborização urbana e a poda de árvores no município. O objetivo é conciliar a segurança das pessoas, a preservação da paisagem e o cuidado com o meio ambiente, evitando podas irregulares que prejudicam as árvores e a cidade. Antes de mexer na vegetação, o morador deve conhecer as regras e procurar orientação.",
            "fechamento_8s": "Árvore cuidada é cidade melhor.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "ambiente leve"
        },
        "tag_thumbnail": "arborização urbana, Arambaré",
        "briefing_visual": {
            "descricao_pt": "Rua arborizada de cidade pequena no Sul do Brasil com árvores frondosas e calçada, equipe de poda ao fundo, sem rostos identificáveis",
            "query_en": ["tree lined street small town", "urban tree pruning", "green street trees brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A quiet tree-lined street in a small southern Brazilian town, leafy green trees along the sidewalk, soft daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço institucional em cidade-núcleo (Arambaré), fonte primária Diretoria de Meio Ambiente, orientação concreta de utilidade pública."
    },

    # IDX 5 — Arambaré cursos gratuitos (abril) — REBAIXAR
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "REBAIXAR", "Segundo item de Arambaré no dia; conteúdo de abril com prazo provavelmente encerrado. Priorizada a nota técnica de arborização."),

    # IDX 6 — Chuvisca edital penalidade — BLOQUEAR
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR", "Edital de penalidade procedural, corpo vazio, sem valor editorial. Guardrail de título procedural."),

    # IDX 7 — Chuvisca edital perímetro urbano — BLOQUEAR
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR", "Edital procedural de prazo administrativo, corpo vazio. Guardrail de título procedural."),

    # IDX 8 — São Lourenço gestão recebe Sesc/Senac/Sindilojas — PUBLICAR
    "4a19f3b447abaaef75271b2e2dbf1a33ae46591b": {
        "titulo_sultv": "São Lourenço do Sul articula parcerias com Sesc, Senac e Sindilojas para novas ações",
        "chamada_faixa": "São Lourenço busca parcerias para cultura e capacitação",
        "subtitulo": "Gestão municipal recebe representantes de Sesc, Senac e Sindilojas para alinhar ações de cultura, educação e qualificação.",
        "lead": "A busca por novas oportunidades movimentou a administração de São Lourenço do Sul. A gestão municipal recebeu representantes do Sesc, do Senac e do Sindilojas para alinhar possíveis ações conjuntas nas áreas de cultura, educação e capacitação, em mais um passo para ampliar serviços à comunidade da Costa Doce.",
        "ganchos_3": [
            "Gestão municipal recebe Sesc, Senac e Sindilojas",
            "Reunião alinha ações de cultura, educação e capacitação",
            "Parcerias podem ampliar serviços à comunidade"
        ],
        "angulo_editorial": "Cidade-núcleo, fonte primária institucional (Prefeitura). Articulação concreta para trazer cultura, educação e qualificação ao município. Pauta de desenvolvimento local, sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Secretaria Municipal de Educação, Cultura e Desporto"],
        "lead_materia_longa": "A busca por novas oportunidades movimentou a administração de São Lourenço do Sul. A gestão municipal recebeu representantes do Sesc, do Senac e do Sindilojas para alinhar possíveis ações conjuntas nas áreas de cultura, educação e capacitação.",
        "post_instagram": {
            "caption": "Parceria que pode render boas oportunidades para São Lourenço do Sul. A gestão municipal recebeu representantes do Sesc, do Senac e do Sindilojas para alinhar possíveis ações nas áreas de cultura, educação e capacitação profissional. Articulações como essa abrem portas para cursos, eventos e serviços que chegam diretamente à comunidade, fortalecendo o comércio, o trabalho e a vida cultural da cidade. Quando o poder público e as entidades caminham juntos, quem ganha é a população da Costa Doce.",
            "hashtags": ["#SãoLourençoDoSul", "#Educação", "#Capacitação", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Novas parcerias em São Lourenço do Sul.",
            "desenvolvimento_45s": "A gestão municipal recebeu representantes do Sesc, do Senac e do Sindilojas para alinhar possíveis ações conjuntas nas áreas de cultura, educação e capacitação profissional. Articulações como essa abrem caminho para cursos, eventos e serviços que chegam diretamente à comunidade, fortalecendo o comércio, o trabalho e a vida cultural da cidade. Quando poder público e entidades caminham juntos, quem ganha é a população da Costa Doce.",
            "fechamento_8s": "Parceria que vira oportunidade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "corporativo otimista"
        },
        "tag_thumbnail": "São Lourenço do Sul, parcerias",
        "briefing_visual": {
            "descricao_pt": "Reunião institucional em sala de prefeitura no interior gaúcho, mesa com representantes, ambiente formal, sem rostos identificáveis em primeiro plano",
            "query_en": ["business meeting table office", "town hall meeting room", "institutional roundtable brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A formal institutional meeting room in a small Brazilian city hall, conference table and chairs, neutral daylight, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cidade-núcleo (São Lourenço do Sul), fonte primária institucional, articulação concreta de desenvolvimento local em cultura, educação e capacitação."
    },

    # IDX 9 — Sentinela aviso de audiência pública — BLOQUEAR (título genérico/cabeçalho)
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR", "Título genérico/cabeçalho ('Aviso de Audiência Pública') sem detalhe, data ou corpo. Guardrail de título procedural."),

    # IDX 10 — Sentinela emissão de notas fiscais — REBAIXAR
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "REBAIXAR", "Comunicado procedural sobre emissor nacional de notas fiscais, datado de maio. Segundo item de Sentinela do Sul."),

    # IDX 11 — Barra do Ribeiro Conferência de Saúde — BLOQUEAR (cabeçalho de seção malformado)
    "a6d042be95d54d6ef82415d825a77afc9d6fa43d": _skip(
        "BLOQUEAR", "Título é cabeçalho de seção malformado ('Secretaria Municipal da Saúde 8 Conferencia...'), sem corpo. Guardrail de título procedural."),

    # IDX 12 — Barra do Ribeiro Velejaço solidário — BLOQUEAR (cabeçalho de seção malformado)
    "93d8797025ffe98d7c47bb3b29fd426a9dec54b2": _skip(
        "BLOQUEAR", "Título é cabeçalho de seção malformado ('Secretaria Municipal do Turismo... 6 Velejaço solidário'), sem detalhe nem data."),

    # IDX 13 — Cristal Rua Camaquã calçamento — PUBLICAR
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": {
        "titulo_sultv": "Rua Camaquã, em Cristal, recebe preparação para obras de calçamento",
        "chamada_faixa": "Cristal prepara calçamento da Rua Camaquã",
        "subtitulo": "Serviços iniciais abrem caminho para a pavimentação da via, que deve melhorar o trânsito e o acesso dos moradores.",
        "lead": "Mais uma rua de Cristal entra na fila do asfalto. A Rua Camaquã começou a receber os serviços de preparação para as obras de calçamento, etapa que antecede a pavimentação e promete melhorar o trânsito, o escoamento da água da chuva e o acesso dos moradores na cidade da Costa Doce.",
        "ganchos_3": [
            "Rua Camaquã recebe preparação para o calçamento",
            "Etapa antecede a pavimentação da via",
            "Obra melhora trânsito e acesso dos moradores"
        ],
        "angulo_editorial": "Serviço urbano concreto em cidade-núcleo (segunda camada), fonte primária Prefeitura. Infraestrutura é pauta de alto interesse local. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria Municipal de Obras de Cristal"],
        "lead_materia_longa": "Mais uma rua de Cristal entra na fila do asfalto. A Rua Camaquã começou a receber os serviços de preparação para as obras de calçamento, etapa que antecede a pavimentação e promete melhorar o trânsito e o acesso dos moradores.",
        "post_instagram": {
            "caption": "Boas notícias para os moradores da Rua Camaquã, em Cristal. A via começou a receber os serviços de preparação para as obras de calçamento, etapa que antecede a pavimentação. Quando a obra ficar pronta, o resultado aparece no dia a dia: trânsito mais fácil, menos poeira e barro, melhor escoamento da água da chuva e mais conforto para quem mora e circula pela região. Calçamento é daquelas melhorias que transformam a rotina de um bairro inteiro. Obra que avança é cidade que melhora.",
            "hashtags": ["#Cristal", "#Infraestrutura", "#Calçamento", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal prepara mais uma obra.",
            "desenvolvimento_45s": "A Rua Camaquã começou a receber os serviços de preparação para as obras de calçamento, etapa que antecede a pavimentação da via. Quando a obra ficar pronta, o resultado aparece no dia a dia: trânsito mais fácil, menos poeira e barro, melhor escoamento da água da chuva e mais conforto para quem mora e circula pela região. Calçamento é daquelas melhorias que transformam a rotina de um bairro inteiro.",
            "fechamento_8s": "Obra que avança é cidade que melhora.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "construtivo otimista"
        },
        "tag_thumbnail": "calçamento, Cristal",
        "briefing_visual": {
            "descricao_pt": "Rua de terra recebendo preparação para pavimentação em cidade pequena do interior gaúcho, máquina e paralelepípedos, sem rostos identificáveis",
            "query_en": ["road paving preparation street", "cobblestone street construction", "small town road works brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A dirt street being prepared for paving in a small southern Brazilian town, construction machinery and cobblestones, daytime, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço urbano concreto (infraestrutura) em cidade-núcleo, fonte primária Prefeitura de Cristal. Alto interesse local."
    },

    # IDX 14 — São Lourenço COMDICA inscrições — REBAIXAR
    "933dc8abb332f937491cc1145b1c43547b949fa4": _skip(
        "REBAIXAR", "Edital procedural de eleição de conselho (COMDICA). Segundo item de São Lourenço; priorizada a articulação de parcerias."),

    # IDX 15 — Cristal Av. Passo do Mendonça limpeza — REBAIXAR
    "804da2cbe08274dd604274d8db6acc48cc218fed": _skip(
        "REBAIXAR", "Segundo item de Cristal no dia; tema de obras viárias já contemplado pela pauta da Rua Camaquã."),

    # IDX 16 — Pelotas concurso magistério (13 maio) — REBAIXAR
    "0c78bd0cc00e7d0302fc635b3fdbfbd510252753": _skip(
        "REBAIXAR", "Conteúdo datado de 13 de maio, prazo já vencido. Segundo item de Pelotas; priorizada a assistência jurídica."),

    # IDX 17 — Pelotas assistência jurídica mulheres — PUBLICAR
    "0c098914e41195a34303db07b3d2f5776f787f04": {
        "titulo_sultv": "Pelotas amplia assistência jurídica a mulheres em situação de violência",
        "chamada_faixa": "Pelotas amplia apoio jurídico a mulheres",
        "subtitulo": "Serviço reforça o acesso à orientação e à defesa legal para mulheres que buscam proteção no município.",
        "lead": "O apoio a quem precisa de proteção ganhou reforço em Pelotas. A Prefeitura ampliou o serviço de assistência jurídica voltado a mulheres em situação de violência, medida que fortalece o acesso à orientação e à defesa legal e amplia a rede de acolhimento no município, na Costa Doce ampliada.",
        "ganchos_3": [
            "Assistência jurídica a mulheres é ampliada em Pelotas",
            "Serviço reforça orientação e defesa legal",
            "Medida fortalece a rede de proteção e acolhimento"
        ],
        "angulo_editorial": "Serviço público de proteção, fonte primária Prefeitura. Pauta sensível tratada de forma institucional e positiva (ampliação de direito/serviço), sem identificar vítimas. Alto valor social.",
        "fontes_complementares_sugeridas": ["Prefeitura de Pelotas", "Secretaria responsável pela política para mulheres em Pelotas"],
        "lead_materia_longa": "O apoio a quem precisa de proteção ganhou reforço em Pelotas. A Prefeitura ampliou o serviço de assistência jurídica voltado a mulheres em situação de violência, medida que fortalece o acesso à orientação e à defesa legal no município.",
        "post_instagram": {
            "caption": "Mais apoio para quem precisa de proteção. Pelotas ampliou o serviço de assistência jurídica voltado a mulheres em situação de violência, reforçando o acesso à orientação e à defesa legal. Iniciativas como essa fortalecem a rede de acolhimento e mostram que pedir ajuda é um direito, com caminhos seguros e gratuitos para quem busca proteção. Informar sobre esses serviços é também uma forma de cuidar da comunidade. Nenhuma mulher precisa enfrentar essa situação sozinha.",
            "hashtags": ["#Pelotas", "#RedeDeProteção", "#AssistênciaJurídica", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Mais proteção em Pelotas.",
            "desenvolvimento_45s": "A Prefeitura ampliou o serviço de assistência jurídica voltado a mulheres em situação de violência, reforçando o acesso à orientação e à defesa legal. Iniciativas como essa fortalecem a rede de acolhimento e mostram que pedir ajuda é um direito, com caminhos seguros e gratuitos para quem busca proteção. Informar sobre esses serviços é também uma forma de cuidar de toda a comunidade.",
            "fechamento_8s": "Nenhuma mulher precisa estar sozinha.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "sóbrio e acolhedor"
        },
        "tag_thumbnail": "assistência jurídica, Pelotas",
        "briefing_visual": {
            "descricao_pt": "Balcão de atendimento jurídico ou social institucional, mãos sobre documentos e mesa, ambiente acolhedor, sem rostos identificáveis",
            "query_en": ["legal aid desk documents", "social service counter help", "lawyer office paperwork hands"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A welcoming legal aid service desk with documents and hands on a table, soft daylight, supportive institutional setting, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público de proteção em Pelotas, fonte primária Prefeitura, ampliação de direito tratada de forma institucional e sem identificar vítimas."
    },

    # IDX 18 — ALERS concessões/privatizações (2019) — BLOQUEAR
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "BLOQUEAR", "Conteúdo datado de 2019 (desatualizado) e de teor político-partidário (plebiscito/privatização). Guardrail política partidária + freshness."),

    # IDX 19 — ALERS Funcriança (2019) — BLOQUEAR
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "BLOQUEAR", "Conteúdo datado de 2019, totalmente desatualizado. Sem valor editorial atual."),

    # IDX 20 — Produtores RS / renegociação de dívidas — PUBLICAR (agro regional)
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "titulo_sultv": "Produtores do RS acompanham com apreensão a renegociação das dívidas rurais",
        "chamada_faixa": "Produtores do RS aguardam renegociação de dívidas",
        "subtitulo": "Setor teme ficar sem acesso ao crédito rural para a próxima safra enquanto a renegociação tramita.",
        "lead": "A próxima safra começa a ser planejada sob tensão no campo gaúcho. Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação das dívidas rurais, temerosos de ficar sem acesso ao crédito necessário para o plantio, um impasse que mexe diretamente com a economia do interior e da Costa Doce.",
        "ganchos_3": [
            "Produtores do RS temem ficar sem crédito para a próxima safra",
            "Renegociação das dívidas rurais segue em tramitação",
            "Impasse afeta a economia do interior gaúcho"
        ],
        "angulo_editorial": "Pauta agro de alto interesse para o público SulTV, com impacto econômico regional. Tema de crédito rural e endividamento — econômico, não partidário. Atribuição a fontes primárias (lideranças do setor, Congresso). Retrabalhado integralmente no tom da Redação.",
        "fontes_complementares_sugeridas": ["Lideranças do setor produtivo do RS", "Federações e entidades da agricultura", "Tramitação no Congresso Nacional"],
        "lead_materia_longa": "A próxima safra começa a ser planejada sob tensão no campo gaúcho. Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação das dívidas rurais, temerosos de ficar sem acesso ao crédito necessário para o plantio.",
        "post_instagram": {
            "caption": "O campo gaúcho vive dias de tensão. Produtores rurais do Rio Grande do Sul acompanham com apreensão a renegociação das dívidas rurais, com receio de ficar sem acesso ao crédito necessário para a próxima safra. Depois de anos marcados por adversidades climáticas, muitos produtores dependem dessa renegociação para reorganizar as contas e seguir plantando. O crédito rural é o combustível que mantém a produção de alimentos girando e a economia do interior de pé. É um tema que vai muito além da porteira: afeta o emprego, o comércio e a vida de toda a região.",
            "hashtags": ["#Agro", "#RioGrandeDoSul", "#CréditoRural", "#Safra", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tensão no campo gaúcho.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a renegociação das dívidas rurais, com receio de ficar sem acesso ao crédito necessário para a próxima safra. Depois de anos marcados por adversidades climáticas, muitos dependem dessa renegociação para reorganizar as contas e seguir plantando. O crédito rural é o combustível que mantém a produção de alimentos girando e a economia do interior de pé.",
            "fechamento_8s": "Um tema que vai além da porteira.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "sóbrio com tensão leve"
        },
        "tag_thumbnail": "crédito rural, safra RS",
        "briefing_visual": {
            "descricao_pt": "Lavoura de grãos no Rio Grande do Sul com trator ao fundo, paisagem rural ao amanhecer, sem rostos identificáveis",
            "query_en": ["soybean field tractor brazil", "grain farm landscape sunrise", "rural farmland south brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Wide shot of a grain farm field in southern Brazil at sunrise, a tractor in the distance, golden light, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta agro de alto interesse regional e impacto econômico no interior gaúcho. Tema de crédito rural (econômico, não partidário), retrabalhado sem citar veículos."
    },

    # IDX 21 — Vinhos vencidos apreendidos (RS) — REBAIXAR
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": _skip(
        "REBAIXAR", "Conteúdo de maio (desatualizado), tom sensacionalista, sem âncora em cidade-núcleo específica."),

    # IDX 22 — 630kg alimentos impróprios (RS) — REBAIXAR
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": _skip(
        "REBAIXAR", "Conteúdo de maio (desatualizado), sem âncora regional específica da Costa Doce."),

    # IDX 23 — MetSul calor Europa — REBAIXAR
    "364aa009610c478f160694aead474f82753f3cf7": _skip(
        "REBAIXAR", "Pauta internacional (Europa) sem âncora Sul-RS. Guardrail conteúdo internacional sem relevância regional."),

    # IDX 24 — UFSM socioeducativo — REBAIXAR
    "f416e9043073570b4cd5ffa367c31d6affad3db1": _skip(
        "REBAIXAR", "Atividade acadêmica em Santa Maria, baixo interesse para o núcleo. Envolve sistema socioeducativo — manter como nota interna."),

    # IDX 25 — UFSM Feira do Livro cadastro — REBAIXAR
    "f0fde321c4466a55dcefddc0c960c6e231a4e791": _skip(
        "REBAIXAR", "Chamada procedural de cadastro de atividades, cidade fora do núcleo. Baixa prioridade."),

    # IDX 26 — Recupera RS Rural / Unisc (Venâncio Aires) — REBAIXAR
    "6bc79b898a948867c4c666647e5dea12f18187cd": _skip(
        "REBAIXAR", "Evento em cidade distante do núcleo (Venâncio Aires), score baixo. Insumo agro, mas sem âncora na Costa Doce."),

    # IDX 27 — Concurso Mato Leitão — REBAIXAR
    "0d4256147da1324c350fabd3e0e8bd4cbb36da6d": _skip(
        "REBAIXAR", "Comunicado procedural de concurso em cidade distante do núcleo. Baixo interesse."),

    # IDX 28 — Criança/padre Cascavel — BLOQUEAR (menor + fora do RS)
    "b305618c655ad21bb0b43b867e4c49bcccf09b9d": _skip(
        "BLOQUEAR", "Conteúdo viral envolvendo criança e ocorrido em Cascavel/PR (fora do RS). Guardrail menores + sem âncora regional."),

    # IDX 29 — CDL Mulher Bento Gonçalves — REBAIXAR
    "1580d8e98454a5d8094381c8643694eae0e09a85": _skip(
        "REBAIXAR", "Evento de negócios em Bento Gonçalves (serra, fora do núcleo Sul-RS), score baixo."),
}


MATERIAS = {

    "10bf0cd9c375743e5d520e49a20fec647849b75a": """### Título ###
INSS amplia exigência de biometria para benefícios; veja o que muda para o segurado

### Artigo ###
Quem depende de um benefício previdenciário precisa ficar atento. O Instituto Nacional do Seguro Social ampliou a exigência de cadastro biométrico para a concessão de benefícios, mudança que atinge diretamente os segurados de Camaquã e de toda a Costa Doce e exige atenção para evitar atrasos na liberação do pagamento. A medida vale para diferentes pedidos feitos ao instituto, como aposentadorias, pensões e outros benefícios, e tem como objetivo dar mais segurança ao sistema e reduzir fraudes. A biometria funciona como uma camada extra de identificação. Ao confirmar quem é o segurado por meio de dados biométricos, o instituto busca garantir que o benefício chegue à pessoa certa, evitando golpes e uso indevido de documentos. Para o cidadão, isso significa um processo mais seguro, mas que exige cuidado redobrado com a regularidade do cadastro. Quem está com os dados desatualizados ou pendentes pode enfrentar demora na análise do pedido. Por isso, a orientação é simples e prática: antes de dar entrada em qualquer benefício, vale conferir a situação cadastral, reunir os documentos pessoais e verificar se a biometria já está registrada nas bases oficiais. Resolver essas pendências com antecedência evita idas e vindas e reduz o tempo de espera. No interior, onde muitas famílias dependem da renda previdenciária, a informação no tempo certo faz diferença. Aposentados, pensionistas e trabalhadores rurais que pretendem solicitar um benefício devem buscar orientação nas agências da Previdência Social e nos canais oficiais de atendimento. Manter o cadastro em dia é a melhor forma de garantir o direito sem surpresas. Em um momento de mudanças nas regras, estar bem informado é o que protege o segurado e assegura que o benefício seja concedido dentro do prazo.

### Legenda sugerida ###
INSS amplia a exigência de biometria na concessão de benefícios; segurado deve manter o cadastro em dia.

### Palavras-chave ###
INSS, biometria, benefícios, Camaquã, Previdência Social, segurado, Costa Doce
""",

    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": """### Título ###
Arambaré publica nota técnica com orientações para a poda de árvores na cidade

### Artigo ###
O cuidado com as árvores da cidade ganhou regras claras em Arambaré. A Diretoria Municipal de Meio Ambiente publicou a Nota Técnica nº 01/2026, que reúne orientações sobre o manejo da arborização urbana e a poda de árvores no município, na orla da Lagoa dos Patos, para que moradores e equipes públicas atuem de forma segura e correta. O documento orienta como proceder diante da necessidade de podar ou manejar árvores em vias e espaços públicos, evitando intervenções irregulares. A arborização urbana é mais do que estética. As árvores ajudam a reduzir a temperatura nas ruas, oferecem sombra, melhoram a qualidade do ar e compõem a paisagem que dá identidade às cidades. Por outro lado, quando malcuidadas, podem oferecer riscos, como galhos que ameaçam a fiação elétrica ou a segurança de pedestres. Por isso, a poda precisa seguir critérios técnicos, e não ser feita de qualquer maneira. A nota técnica busca justamente equilibrar esses interesses. Ao definir orientações claras, o município pretende preservar as árvores saudáveis, conduzir podas necessárias da forma adequada e evitar cortes indevidos que prejudicam a vegetação e o meio ambiente. O morador que identificar a necessidade de uma poda deve procurar a Diretoria de Meio Ambiente antes de agir por conta própria, garantindo que o serviço seja autorizado e bem executado. Iniciativas como essa fortalecem a consciência ambiental na comunidade. Cuidar das árvores é cuidar da qualidade de vida de todos, da temperatura agradável nas ruas ao conforto de quem caminha pela cidade. Ao publicar a nota técnica, Arambaré reafirma o compromisso de aliar o desenvolvimento urbano à preservação ambiental, mostrando que crescimento e respeito à natureza podem caminhar juntos na Costa Doce.

### Legenda sugerida ###
Arambaré publica a Nota Técnica nº 01/2026 com orientações sobre a poda de árvores e o manejo da arborização urbana.

### Palavras-chave ###
Arambaré, poda de árvores, arborização urbana, meio ambiente, nota técnica, Costa Doce, Lagoa dos Patos
""",

    "4a19f3b447abaaef75271b2e2dbf1a33ae46591b": """### Título ###
São Lourenço do Sul articula parcerias com Sesc, Senac e Sindilojas para novas ações

### Artigo ###
A busca por novas oportunidades movimentou a administração de São Lourenço do Sul. A gestão municipal recebeu representantes do Sesc, do Senac e do Sindilojas para alinhar possíveis ações conjuntas nas áreas de cultura, educação e capacitação, em mais um passo para ampliar os serviços oferecidos à comunidade da Costa Doce. O encontro reuniu o poder público e entidades que atuam fortemente na qualificação profissional, no comércio e na promoção cultural, abrindo caminho para iniciativas que podem chegar diretamente à população. Parcerias como essa têm um peso concreto no interior. Quando a prefeitura se aproxima de instituições como o Senac, voltado à educação profissional, e o Sesc, ligado à cultura, ao lazer e ao bem-estar, surge a possibilidade de trazer cursos, oficinas, eventos e serviços que dificilmente o município ofereceria sozinho. Já a aproximação com o Sindilojas conecta essas ações ao comércio local, fortalecendo quem gera emprego e renda na cidade. O alinhamento de ideias é o primeiro passo para transformar intenções em resultados. A partir dessas conversas, podem nascer programas de capacitação para jovens e adultos, atividades culturais para as famílias e ações que estimulem o desenvolvimento econômico. Tudo isso contribui para que a população tenha acesso a mais oportunidades sem precisar se deslocar para os grandes centros. Investir em articulação institucional é também investir no futuro do município. Cidades que constroem parcerias sólidas conseguem ampliar serviços, atrair iniciativas e melhorar a qualidade de vida da comunidade. Ao receber Sesc, Senac e Sindilojas, São Lourenço do Sul mostra disposição para somar esforços e busca abrir novas portas para a sua gente, reforçando a vocação de desenvolvimento da Costa Doce.

### Legenda sugerida ###
Gestão municipal de São Lourenço do Sul recebe Sesc, Senac e Sindilojas para alinhar ações de cultura, educação e capacitação.

### Palavras-chave ###
São Lourenço do Sul, Sesc, Senac, Sindilojas, capacitação, cultura, Costa Doce
""",

    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": """### Título ###
Rua Camaquã, em Cristal, recebe preparação para obras de calçamento

### Artigo ###
Mais uma rua de Cristal entra na fila do asfalto. A Rua Camaquã começou a receber os serviços de preparação para as obras de calçamento, etapa que antecede a pavimentação e promete melhorar o trânsito, o escoamento da água da chuva e o acesso dos moradores na cidade da Costa Doce. Os trabalhos iniciais incluem a organização do terreno e os ajustes necessários para que a via fique pronta para receber o calçamento, dando início a uma transformação aguardada por quem vive na região. O calçamento de uma rua muda a rotina de todo um bairro. Vias pavimentadas reduzem a poeira no tempo seco e o barro nos dias de chuva, facilitam a passagem de veículos e pedestres e tornam mais simples o acesso de serviços essenciais, como coleta de lixo, transporte e atendimento de emergência. É uma melhoria que se sente no dia a dia e valoriza os imóveis da vizinhança. Obras de infraestrutura como essa também trazem ganhos para a cidade como um todo. Ruas em melhores condições reduzem o desgaste dos veículos, melhoram o escoamento das águas pluviais e ajudam a prevenir alagamentos e buracos que costumam surgir nas vias de terra. Cada nova rua calçada representa um passo no desenvolvimento urbano do município. Para os moradores da Rua Camaquã, a expectativa é de que a obra avance e traga, em breve, mais conforto e qualidade de vida. Investimentos em pavimentação fazem parte do esforço contínuo de melhorar a estrutura das cidades do interior. Ao preparar a Rua Camaquã para o calçamento, Cristal reforça o compromisso com a infraestrutura urbana e atende a uma demanda concreta de quem vive e circula pela região da Costa Doce.

### Legenda sugerida ###
A Rua Camaquã, em Cristal, recebe os serviços de preparação para as obras de calçamento e pavimentação.

### Palavras-chave ###
Cristal, Rua Camaquã, calçamento, pavimentação, infraestrutura, obras, Costa Doce
""",

    "0c098914e41195a34303db07b3d2f5776f787f04": """### Título ###
Pelotas amplia assistência jurídica a mulheres em situação de violência

### Artigo ###
O apoio a quem precisa de proteção ganhou reforço em Pelotas. A Prefeitura ampliou o serviço de assistência jurídica voltado a mulheres em situação de violência, medida que fortalece o acesso à orientação e à defesa legal e amplia a rede de acolhimento no município, na Costa Doce ampliada. Com a ampliação, mais mulheres passam a contar com atendimento especializado para esclarecer dúvidas, conhecer seus direitos e receber o suporte necessário em momentos delicados. O acesso à orientação jurídica é uma peça fundamental da rede de proteção. Muitas mulheres que enfrentam situações de violência não sabem quais caminhos seguir, quais medidas podem solicitar ou como funcionam os mecanismos legais de defesa. Um serviço gratuito e qualificado ajuda a romper esse desconhecimento, oferecendo segurança para que cada uma possa tomar decisões com o apoio adequado. Iniciativas como essa se somam a outros serviços de acolhimento e mostram a importância de uma rede integrada. Quando orientação jurídica, atendimento social e canais de denúncia funcionam de forma articulada, fica mais fácil garantir proteção e encaminhar cada caso da maneira correta. O fortalecimento desses serviços é um investimento direto na segurança e na dignidade das mulheres. Divulgar a existência desse atendimento também é parte do trabalho. Quanto mais a comunidade conhece os serviços disponíveis, mais mulheres conseguem buscar ajuda no momento em que precisam. A informação chega a vizinhas, familiares e amigas, ampliando o alcance da proteção. Ao ampliar a assistência jurídica, Pelotas reforça o compromisso com a rede de enfrentamento à violência e lembra que pedir ajuda é um direito, com caminhos seguros e gratuitos à disposição de quem busca proteção.

### Legenda sugerida ###
Pelotas amplia a assistência jurídica gratuita a mulheres em situação de violência, reforçando a rede de proteção.

### Palavras-chave ###
Pelotas, assistência jurídica, mulheres, rede de proteção, violência, acolhimento, Costa Doce
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS acompanham com apreensão a renegociação das dívidas rurais

### Artigo ###
A próxima safra começa a ser planejada sob tensão no campo gaúcho. Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação das dívidas rurais, temerosos de ficar sem acesso ao crédito necessário para o plantio, um impasse que mexe diretamente com a economia do interior e da Costa Doce. Depois de anos marcados por adversidades climáticas, que reduziram a produção e comprometeram a renda no campo, muitos produtores dependem dessa renegociação para reorganizar as contas e seguir produzindo. O crédito rural é o combustível que mantém a atividade agrícola em movimento. É com ele que o produtor compra sementes, insumos, combustível e tudo o que precisa para plantar e colher. Sem acesso a esse financiamento, o ciclo da produção fica ameaçado, com reflexos que vão além da porteira e atingem o comércio, os fornecedores e o emprego nas cidades do interior. Por isso, a definição sobre a renegociação é acompanhada de perto por quem vive da terra. A preocupação do setor é compreensível. Quando o produtor enfrenta dívidas acumuladas e ainda assim precisa investir na nova safra, a falta de uma solução pode significar a redução da área plantada ou até a interrupção da atividade. Isso impacta a oferta de alimentos, a economia regional e a permanência das famílias no campo. O endividamento rural é um tema que une produtores de diferentes regiões do Estado. O Rio Grande do Sul tem peso importante na produção nacional, e o que acontece com o crédito rural gaúcho repercute em toda a cadeia do agronegócio. Enquanto a renegociação tramita, o campo espera por respostas que tragam previsibilidade e permitam ao produtor planejar a próxima safra com mais tranquilidade e segurança.

### Legenda sugerida ###
Produtores do Rio Grande do Sul temem ficar sem crédito para a próxima safra enquanto a renegociação das dívidas rurais tramita.

### Palavras-chave ###
agro, Rio Grande do Sul, crédito rural, dívidas rurais, safra, produtores, renegociação
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
