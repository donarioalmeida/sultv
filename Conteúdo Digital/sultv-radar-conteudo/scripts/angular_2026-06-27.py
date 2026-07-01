#!/usr/bin/env python3
"""
angular_2026-06-27.py — angulação editorial + redação (cowork-faz-tudo).
Decisões editoriais Claude na sessão para a pauta de 2026-06-27.
Regra 12 INEGOCIÁVEL: nenhum texto menciona veículos/portais/rádios/jornais.
Atribuição apenas a fontes primárias institucionais.
Quota: máximo 10 PUBLICAR (regra 14).
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-27"


def _skip(decisao: str, motivo: str, titulo: str = "") -> dict:
    return {
        "titulo_sultv": titulo, "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": decisao,
        "decisao_motivo": motivo,
    }


PAUTA_ANGULADA = {

    # IDX 0 — Camaquã: tempo no fim de semana — PUBLICAR (núcleo, oportuno)
    "e37450da327ccf4b05690c92043f1e958b833e12": {
        "titulo_sultv": "Camaquã tem sábado de sol e tempo firme antes da chuva chegar no domingo",
        "chamada_faixa": "Camaquã: sol no sábado, chuva no domingo",
        "subtitulo": "Fim de semana começa estável e com predomínio de sol; a virada do tempo deve trazer pancadas de chuva já no domingo.",
        "lead": "O sábado é de aproveitar o tempo aberto em Camaquã. A previsão aponta um dia de tempo firme, com céu limpo e predomínio de sol no município, condição que deve durar até o início do domingo, quando a chegada de uma frente úmida traz de volta a possibilidade de chuva.",
        "ganchos_3": [
            "Sábado tem sol e tempo firme em Camaquã",
            "A virada do tempo chega no domingo com chuva",
            "Frente úmida muda o cenário no fim de semana"
        ],
        "angulo_editorial": "Serviço de utilidade pública direta em cidade-núcleo (Camaquã), oportuno para o próprio dia. Sem viés, sem guardrail.",
        "fontes_complementares_sugeridas": ["Boletim meteorológico regional"],
        "lead_materia_longa": "O sábado é de aproveitar o tempo aberto em Camaquã. A previsão aponta um dia de tempo firme, com céu limpo e predomínio de sol no município, condição que deve durar até o início do domingo.",
        "post_instagram": {
            "caption": "Pode tirar a roupa do varal e fazer aquele programa ao ar livre: o sábado em Camaquã é de tempo firme, com céu limpo e predomínio de sol. As condições seguem estáveis ao longo do dia, sem previsão de chuva, num respiro em meio à sequência de frio que tomou conta do Rio Grande do Sul nas últimas semanas. A virada, no entanto, já tem hora marcada. A partir do domingo, uma frente úmida se aproxima da região e devolve ao mapa a possibilidade de pancadas de chuva, com aumento da nebulosidade e queda na sensação de tempo seco. Quem tem planos para o fim de semana ganha um aliado no sábado e deve ficar de olho na mudança a partir do dia seguinte. Aproveite o sol enquanto ele dura.",
            "hashtags": ["#Camaquã", "#Previsão", "#CostaDoce", "#RioGrandedoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O tempo no fim de semana em Camaquã.",
            "desenvolvimento_45s": "O sábado é de tempo firme em Camaquã, com céu limpo e predomínio de sol ao longo do dia. As condições seguem estáveis, sem previsão de chuva, num respiro em meio à sequência de frio das últimas semanas no Rio Grande do Sul. A mudança já tem hora: a partir do domingo, uma frente úmida se aproxima da região e devolve ao mapa a possibilidade de pancadas de chuva, com aumento da nebulosidade.",
            "fechamento_8s": "Aproveite o sol enquanto ele dura.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "leve e ensolarada"
        },
        "tag_thumbnail": "previsão do tempo, Camaquã",
        "briefing_visual": {
            "descricao_pt": "Céu azul de inverno com sol sobre paisagem urbana de cidade do interior do Rio Grande do Sul, sem pessoas",
            "query_en": ["blue winter sky sun", "clear sky small town brazil", "sunny day rural town"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A clear blue winter sky with bright sun over a small southern Brazilian town, calm and stable weather, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço meteorológico oportuno em cidade-núcleo (Camaquã). Fato concreto, sem guardrail."
    },

    # IDX 1 — Camaquã: expediente reduzido jogo do Brasil seg 29 — PUBLICAR (núcleo, serviço)
    "fca7c3b2a464c1917e53e9c9c40b00e454567e5d": {
        "titulo_sultv": "Camaquã terá expediente reduzido e aulas suspensas na segunda por jogo do Brasil",
        "chamada_faixa": "Camaquã muda horário por jogo do Brasil",
        "subtitulo": "Repartições municipais terão funcionamento especial e as aulas da tarde ficam suspensas na segunda-feira, dia 29.",
        "lead": "A Seleção Brasileira mexe com a rotina de Camaquã. A Prefeitura confirmou expediente reduzido nas repartições municipais e a suspensão das aulas no turno da tarde na próxima segunda-feira, dia 29, em razão da partida do Brasil pela Copa do Mundo, organizando o funcionamento dos serviços públicos em torno do horário do jogo.",
        "ganchos_3": [
            "Prefeitura terá expediente reduzido na segunda-feira",
            "Aulas da tarde ficam suspensas no dia do jogo",
            "Funcionamento dos serviços é ajustado à partida do Brasil"
        ],
        "angulo_editorial": "Serviço de utilidade pública direta em cidade-núcleo (Camaquã), com data definida e impacto sobre a rotina dos moradores. Fonte primária institucional (Prefeitura). Sem guardrail.",
        "fontes_complementares_sugeridas": ["Prefeitura de Camaquã", "Secretaria Municipal de Educação de Camaquã"],
        "lead_materia_longa": "A Seleção Brasileira mexe com a rotina de Camaquã. A Prefeitura confirmou expediente reduzido nas repartições municipais e a suspensão das aulas no turno da tarde na próxima segunda-feira, dia 29, em razão da partida do Brasil pela Copa do Mundo.",
        "post_instagram": {
            "caption": "A bola vai rolar e a rotina de Camaquã se ajusta a ela. A Prefeitura definiu um horário especial de funcionamento para a próxima segunda-feira, dia 29, em razão da partida da Seleção Brasileira pela Copa do Mundo. As repartições municipais terão expediente reduzido e as aulas do turno da tarde ficam suspensas, permitindo que servidores, estudantes e suas famílias acompanhem o jogo. Medidas como essa fazem parte de um movimento nacional em torno das partidas do Brasil em Copas, quando o país praticamente para para torcer. Vale o aviso para quem precisa de algum serviço público na cidade: programe-se e resolva as pendências antes do horário do jogo, evitando a porta fechada. Anote a data, organize a agenda e prepare a torcida. Na segunda, é Brasil em campo.",
            "hashtags": ["#Camaquã", "#CopaDoMundo", "#Brasil", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Camaquã muda o horário por causa do jogo do Brasil.",
            "desenvolvimento_45s": "A Prefeitura de Camaquã definiu um horário especial de funcionamento para a próxima segunda-feira, dia 29, em razão da partida da Seleção Brasileira pela Copa do Mundo. As repartições municipais terão expediente reduzido e as aulas do turno da tarde ficam suspensas, permitindo que servidores, estudantes e famílias acompanhem o jogo. Quem precisa de algum serviço público deve se programar e resolver as pendências antes do horário da partida.",
            "fechamento_8s": "Na segunda, é Brasil em campo.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "animada e patriótica"
        },
        "tag_thumbnail": "Copa do Mundo, Camaquã",
        "briefing_visual": {
            "descricao_pt": "Prédio público municipal com bandeira do Brasil ao vento, clima de Copa do Mundo, sem pessoas identificáveis",
            "query_en": ["brazil flag building", "city hall brazil flag", "world cup brazil street"],
            "evitar": ["pessoas com rosto visível", "marcas comerciais", "texto", "logos"],
            "prompt_ia": "A municipal public building with a Brazilian flag waving, world cup atmosphere, daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de utilidade pública com data definida em cidade-núcleo (Camaquã), fonte primária institucional. Sem guardrail."
    },

    # IDX 13 — São Lourenço do Sul: decreto horário Copa — PUBLICAR (núcleo, serviço)
    "6efbfa9389c4b51a10c5e9449458fa3c97f3b5aa": {
        "titulo_sultv": "São Lourenço do Sul define horário excepcional de expediente durante a Copa do Mundo",
        "chamada_faixa": "São Lourenço ajusta expediente na Copa",
        "subtitulo": "Decreto municipal estabelece o funcionamento das repartições públicas nos dias de jogos da Seleção Brasileira.",
        "lead": "São Lourenço do Sul também acerta o relógio com a Copa. O Município publicou decreto que estabelece horário excepcional de expediente nas repartições públicas municipais nos dias de partidas da Seleção Brasileira, ajustando o atendimento ao público para que servidores e moradores possam acompanhar os jogos.",
        "ganchos_3": [
            "Decreto define horário especial nas repartições municipais",
            "Mudança vale para os dias de jogos do Brasil",
            "Atendimento ao público é reorganizado durante a Copa"
        ],
        "angulo_editorial": "Serviço de utilidade pública em cidade-núcleo (São Lourenço do Sul), fonte primária institucional (Decreto municipal). Fato concreto e atual. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul"],
        "lead_materia_longa": "São Lourenço do Sul também acerta o relógio com a Copa. O Município publicou decreto que estabelece horário excepcional de expediente nas repartições públicas municipais nos dias de partidas da Seleção Brasileira.",
        "post_instagram": {
            "caption": "Em São Lourenço do Sul, a agenda da Copa do Mundo entrou para o diário oficial. O Município publicou um decreto que estabelece horário excepcional de expediente nas repartições públicas municipais nos dias de jogos da Seleção Brasileira. Na prática, o atendimento ao público é reorganizado para que servidores e moradores possam acompanhar as partidas, num gesto que se repete em diversas cidades durante os Mundiais. O recado é simples para quem depende de algum serviço da Prefeitura: confira o horário antes de se deslocar e resolva as pendências com antecedência, evitando a porta fechada nos dias de jogo. Organize a rotina, separe a camiseta e prepare a torcida. A Costa Doce também entra em campo junto com o Brasil.",
            "hashtags": ["#SãoLourençodoSul", "#CopaDoMundo", "#CostaDoce", "#RioGrandedoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "São Lourenço muda o expediente na Copa.",
            "desenvolvimento_45s": "O Município de São Lourenço do Sul publicou um decreto que estabelece horário excepcional de expediente nas repartições públicas municipais nos dias de jogos da Seleção Brasileira. O atendimento ao público é reorganizado para que servidores e moradores possam acompanhar as partidas. Quem depende de algum serviço da Prefeitura deve conferir o horário antes de se deslocar e resolver as pendências com antecedência.",
            "fechamento_8s": "A Costa Doce entra em campo junto.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "animada e patriótica"
        },
        "tag_thumbnail": "Copa do Mundo, São Lourenço do Sul",
        "briefing_visual": {
            "descricao_pt": "Fachada de prédio público municipal em cidade do interior gaúcho com bandeira do Brasil, clima de Copa, sem pessoas identificáveis",
            "query_en": ["brazilian flag public building", "city hall facade brazil", "world cup brazil flag street"],
            "evitar": ["pessoas com rosto visível", "marcas comerciais", "texto", "logos"],
            "prompt_ia": "Facade of a municipal public building in a southern Brazilian town with a Brazilian flag, world cup atmosphere, daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de utilidade pública em cidade-núcleo (São Lourenço do Sul), fonte primária institucional. Sem guardrail."
    },

    # IDX 14 — Cristal: melhorias em estradas do interior — PUBLICAR (núcleo, concreto)
    "01ef011ecdae21c60e1584906736e0e1b68bd082": {
        "titulo_sultv": "Cristal reforça estradas do interior com cascalhamento e patrolamento",
        "chamada_faixa": "Cristal melhora estradas do interior",
        "subtitulo": "Serviços de cascalhamento, patrolamento e apoio às propriedades rurais avançam por diferentes localidades do município.",
        "lead": "As estradas que ligam o campo à cidade ganham atenção em Cristal. A Prefeitura realiza um pacote de melhorias nas vias do interior do município, com serviços de cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades, trabalho que facilita o escoamento da produção e o dia a dia de quem vive no meio rural.",
        "ganchos_3": [
            "Estradas do interior de Cristal recebem melhorias",
            "Serviços incluem cascalhamento e patrolamento",
            "Apoio às propriedades rurais chega a várias localidades"
        ],
        "angulo_editorial": "Infraestrutura rural em cidade-núcleo (Cristal), fato concreto com impacto direto na produção e na vida do campo. Fonte primária institucional (Prefeitura). Sem guardrail.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria Municipal de Obras de Cristal"],
        "lead_materia_longa": "As estradas que ligam o campo à cidade ganham atenção em Cristal. A Prefeitura realiza um pacote de melhorias nas vias do interior do município, com serviços de cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades.",
        "post_instagram": {
            "caption": "Quem vive no campo sabe: estrada boa é sinônimo de produção que escoa e de gente que vai e vem com segurança. Em Cristal, as vias do interior estão recebendo um pacote de melhorias, com serviços de cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades do município. O trabalho atende uma demanda histórica de quem mora e produz longe do centro. Estradas bem conservadas reduzem o desgaste dos veículos, facilitam o transporte de safras e insumos, garantem o acesso de ônibus escolares e ambulâncias e aproximam o produtor dos serviços essenciais. Mais do que cascalho e máquina, é a zona rural ganhando condições de seguir movimentando a economia da região. Um investimento que chega onde a comunidade precisa: na estrada de cada dia.",
            "hashtags": ["#Cristal", "#Agro", "#EstradasRurais", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal melhora as estradas do interior.",
            "desenvolvimento_45s": "A Prefeitura de Cristal está realizando um pacote de melhorias nas estradas do interior do município, com serviços de cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades. O trabalho atende uma demanda histórica de quem vive e produz longe do centro. Estradas bem conservadas facilitam o transporte de safras e insumos, garantem o acesso de ônibus escolares e ambulâncias e aproximam o produtor dos serviços essenciais.",
            "fechamento_8s": "Investimento que chega na estrada de cada dia.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "campo e trabalho"
        },
        "tag_thumbnail": "estradas rurais, Cristal",
        "briefing_visual": {
            "descricao_pt": "Estrada rural de chão com cascalho sendo nivelada por patrola/motoniveladora no interior gaúcho, sem rosto identificável",
            "query_en": ["rural gravel road grading", "motor grader dirt road", "countryside road maintenance brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A rural gravel road being graded by a motor grader in the southern Brazilian countryside, working machinery, daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Infraestrutura rural concreta em cidade-núcleo (Cristal), fonte primária institucional. Sem guardrail."
    },

    # IDX 4 — Arambaré: nota técnica poda/arborização — PUBLICAR (núcleo, serviço)
    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": {
        "titulo_sultv": "Arambaré publica nota técnica com orientações sobre poda e arborização urbana",
        "chamada_faixa": "Arambaré orienta sobre poda de árvores",
        "subtitulo": "Documento da Diretoria de Meio Ambiente reúne diretrizes para o manejo correto das árvores na cidade.",
        "lead": "O verde das ruas de Arambaré ganha um manual de cuidados. A Prefeitura, por meio da Diretoria Municipal de Meio Ambiente, publicou a Nota Técnica nº 01/2026 com orientações sobre o manejo da arborização urbana e a poda de árvores, documento que organiza as boas práticas e esclarece a população sobre como proceder de forma correta e segura.",
        "ganchos_3": [
            "Nota técnica orienta o manejo da arborização urbana",
            "Documento detalha como fazer a poda de forma correta",
            "Diretoria de Meio Ambiente reúne as boas práticas"
        ],
        "angulo_editorial": "Serviço de utilidade pública e meio ambiente em cidade-núcleo (Arambaré), fonte primária institucional (Diretoria de Meio Ambiente). Fato concreto e orientativo. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Diretoria Municipal de Meio Ambiente de Arambaré", "Prefeitura de Arambaré"],
        "lead_materia_longa": "O verde das ruas de Arambaré ganha um manual de cuidados. A Prefeitura, por meio da Diretoria Municipal de Meio Ambiente, publicou a Nota Técnica nº 01/2026 com orientações sobre o manejo da arborização urbana e a poda de árvores.",
        "post_instagram": {
            "caption": "Árvore na cidade é sombra, é ar mais limpo e é qualidade de vida, mas também pede cuidado e manejo correto. Pensando nisso, Arambaré publicou uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores, elaborada pela Diretoria Municipal de Meio Ambiente. O documento organiza as boas práticas e esclarece a população sobre como proceder na hora de podar, evitando danos às plantas, riscos à rede elétrica e cortes irregulares. A medida ajuda o morador a entender quando e como agir, em quais casos é preciso autorização e qual o papel do poder público nesse processo. Cuidar da arborização é cuidar da cidade inteira: das calçadas, das casas e do clima local. Quem tiver dúvidas deve procurar a Diretoria de Meio Ambiente antes de pegar a serra.",
            "hashtags": ["#Arambaré", "#MeioAmbiente", "#Arborização", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Arambaré orienta sobre a poda de árvores.",
            "desenvolvimento_45s": "A Prefeitura de Arambaré, por meio da Diretoria Municipal de Meio Ambiente, publicou uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores. O documento organiza as boas práticas e esclarece a população sobre como proceder, evitando danos às plantas, riscos à rede elétrica e cortes irregulares. A medida ajuda o morador a entender quando e como agir e em quais casos é preciso autorização.",
            "fechamento_8s": "Cuidar da árvore é cuidar da cidade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "leve e ambiental"
        },
        "tag_thumbnail": "arborização urbana, Arambaré",
        "briefing_visual": {
            "descricao_pt": "Árvores em rua arborizada de cidade pequena do interior gaúcho, foco nas copas verdes, sem pessoas identificáveis",
            "query_en": ["tree lined street small town", "urban trees pruning", "green street trees brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A tree-lined street in a small southern Brazilian town, green canopies over the sidewalk, daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de utilidade pública e meio ambiente em cidade-núcleo (Arambaré), fonte primária institucional. Sem guardrail."
    },

    # IDX 2 — Chuvisca: organização dos atendimentos de fonoaudiologia — PUBLICAR (núcleo, serviço/acesso)
    "039fa52e365e6c812a99ca228536b63e7dbf902a": {
        "titulo_sultv": "Chuvisca organiza atendimentos de fonoaudiologia para ampliar o acesso da população",
        "chamada_faixa": "Chuvisca amplia acesso à fonoaudiologia",
        "subtitulo": "Secretaria de Saúde estrutura os atendimentos na unidade de Saúde Mental para atender mais moradores.",
        "lead": "O acesso à saúde dá um passo a mais em Chuvisca. A Prefeitura, por meio da Secretaria Municipal de Saúde, organizou os atendimentos de fonoaudiologia realizados na unidade de Saúde Mental do município, medida que busca ampliar o alcance do serviço e garantir que mais moradores sejam atendidos de forma estruturada.",
        "ganchos_3": [
            "Atendimentos de fonoaudiologia são organizados em Chuvisca",
            "Serviço acontece na unidade de Saúde Mental do município",
            "Objetivo é ampliar o acesso da população"
        ],
        "angulo_editorial": "Serviço público de saúde (organização e acesso, não orientação médica) em cidade-núcleo (Chuvisca), fonte primária institucional (Secretaria de Saúde). Sem diagnóstico nem prescrição — sem guardrail de saúde.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Saúde de Chuvisca", "Prefeitura de Chuvisca"],
        "lead_materia_longa": "O acesso à saúde dá um passo a mais em Chuvisca. A Prefeitura, por meio da Secretaria Municipal de Saúde, organizou os atendimentos de fonoaudiologia realizados na unidade de Saúde Mental do município.",
        "post_instagram": {
            "caption": "Em Chuvisca, o atendimento de fonoaudiologia ganhou nova organização para chegar a mais gente. A Secretaria Municipal de Saúde estruturou os atendimentos realizados na unidade de Saúde Mental do município, com o objetivo de ampliar o acesso da população ao serviço. A fonoaudiologia tem papel importante em todas as idades, do acompanhamento do desenvolvimento da fala na infância à reabilitação de adultos, e contar com esse atendimento na rede pública faz diferença para muitas famílias. Organizar a agenda e os fluxos de atendimento ajuda a reduzir filas, evitar deslocamentos desnecessários e garantir que quem precisa seja acolhido. Para saber como agendar e quais são os critérios, o morador deve procurar a unidade de saúde do município. Cuidar do acesso é cuidar das pessoas.",
            "hashtags": ["#Chuvisca", "#Saúde", "#Fonoaudiologia", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Chuvisca amplia o acesso à fonoaudiologia.",
            "desenvolvimento_45s": "A Secretaria Municipal de Saúde de Chuvisca organizou os atendimentos de fonoaudiologia realizados na unidade de Saúde Mental do município, com o objetivo de ampliar o acesso da população ao serviço. A fonoaudiologia tem papel importante em todas as idades, e contar com esse atendimento na rede pública faz diferença para muitas famílias. Organizar a agenda ajuda a reduzir filas e garantir o acolhimento de quem precisa.",
            "fechamento_8s": "Cuidar do acesso é cuidar das pessoas.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "acolhedora e leve"
        },
        "tag_thumbnail": "saúde pública, Chuvisca",
        "briefing_visual": {
            "descricao_pt": "Unidade básica de saúde municipal no interior gaúcho, fachada ou recepção, sem pacientes identificáveis",
            "query_en": ["public health clinic facade", "community health center brazil", "health unit reception"],
            "evitar": ["pessoas com rosto visível", "pacientes identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Facade of a small municipal public health unit in the southern Brazilian countryside, daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público de saúde (acesso/organização, não orientação clínica) em cidade-núcleo (Chuvisca), fonte primária institucional. Sem guardrail."
    },

    # IDX 15 — Cristal: lançamento do PREPARA RS — PUBLICAR (núcleo, prevenção climática)
    "9ce36499a218324114c169a9d64f04aae0558ec9": {
        "titulo_sultv": "Cristal participa do lançamento do PREPARA RS, programa de prevenção a eventos climáticos",
        "chamada_faixa": "Cristal no PREPARA RS contra extremos do clima",
        "subtitulo": "Iniciativa estadual apresenta ações e recursos para preparar os municípios diante de eventos climáticos extremos.",
        "lead": "Diante de um clima cada vez mais imprevisível, a prevenção entra na agenda de Cristal. O município participou do lançamento do PREPARA RS, programa que apresenta ações de prevenção e recursos para preparar as cidades gaúchas diante de eventos climáticos extremos, tema que ganhou urgência no Rio Grande do Sul nos últimos anos.",
        "ganchos_3": [
            "Cristal participa do lançamento do PREPARA RS",
            "Programa foca na prevenção a eventos climáticos extremos",
            "Municípios recebem ações e recursos de preparação"
        ],
        "angulo_editorial": "Prevenção e resiliência climática em cidade-núcleo (Cristal), tema de forte relevância regional após eventos extremos no RS. Fonte primária institucional (Prefeitura / programa estadual). Sem viés partidário, sem guardrail.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Governo do Estado do Rio Grande do Sul"],
        "lead_materia_longa": "Diante de um clima cada vez mais imprevisível, a prevenção entra na agenda de Cristal. O município participou do lançamento do PREPARA RS, programa que apresenta ações de prevenção e recursos para preparar as cidades gaúchas diante de eventos climáticos extremos.",
        "post_instagram": {
            "caption": "Depois de tantos eventos extremos no Rio Grande do Sul, prevenir deixou de ser opção e virou prioridade. Foi nesse espírito que Cristal participou do lançamento do PREPARA RS, programa que apresenta ações de prevenção e disponibiliza recursos para preparar os municípios diante de eventos climáticos extremos. A ideia é simples e poderosa: sair do modo reação e entrar no modo planejamento. Isso significa mapear áreas de risco, organizar planos de contingência, estruturar a defesa civil e capacitar equipes antes que a próxima enchente, estiagem ou temporal chegue. Para uma cidade do interior, estar dentro de um programa assim é ganhar apoio técnico e financeiro para proteger vidas e o patrimônio das famílias. O clima mudou, e a melhor resposta é estar preparado. Prevenção salva.",
            "hashtags": ["#Cristal", "#PreparaRS", "#Clima", "#DefesaCivil", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal aposta na prevenção climática.",
            "desenvolvimento_45s": "O município de Cristal participou do lançamento do PREPARA RS, programa que apresenta ações de prevenção e disponibiliza recursos para preparar os municípios diante de eventos climáticos extremos. Depois de tantos eventos no Rio Grande do Sul, a ideia é sair do modo reação e entrar no modo planejamento: mapear áreas de risco, organizar planos de contingência e estruturar a defesa civil antes que o próximo temporal ou estiagem chegue.",
            "fechamento_8s": "Prevenção salva vidas e patrimônio.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "séria e mobilizadora"
        },
        "tag_thumbnail": "prevenção climática, Cristal",
        "briefing_visual": {
            "descricao_pt": "Equipe de defesa civil ou paisagem de rio do interior gaúcho remetendo a prevenção de desastres, sem rosto identificável",
            "query_en": ["civil defense team", "flood prevention river", "emergency preparedness rural"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos", "cenas de tragédia com vítimas"],
            "prompt_ia": "A calm river landscape near a small southern Brazilian town suggesting flood prevention and preparedness, daylight, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Prevenção e resiliência climática em cidade-núcleo (Cristal), tema de alta relevância regional. Fonte primária institucional. Sem guardrail."
    },

    # IDX 21 — RS: quase 70 cidades com frio abaixo de zero — PUBLICAR (regional, clima)
    "775f9b501ba50ff6ad224de967b2336e8dfb9479": {
        "titulo_sultv": "Onda de frio leva quase 70 cidades gaúchas a registrar temperaturas abaixo de zero",
        "chamada_faixa": "Quase 70 cidades gaúchas abaixo de zero",
        "subtitulo": "Amanhecer congelante marcou as menores temperaturas do ano em boa parte do Rio Grande do Sul.",
        "lead": "O Rio Grande do Sul amanheceu congelando. Quase 70 cidades gaúchas registraram temperaturas abaixo de zero em um dos amanheceres mais frios do ano, episódio que marcou as menores mínimas de 2026 em diversas localidades e exigiu cuidados redobrados no campo e na cidade.",
        "ganchos_3": [
            "Quase 70 cidades gaúchas ficaram abaixo de zero",
            "Amanhecer registrou as menores temperaturas do ano",
            "Frio intenso exige cuidados no campo e na cidade"
        ],
        "angulo_editorial": "Clima regional de forte impacto na audiência rural e urbana do RS, com dado quantitativo concreto. Insumo meteorológico reformatado como conteúdo próprio, sem menção a veículo (regra 12). Sem guardrail.",
        "fontes_complementares_sugeridas": ["Estações meteorológicas do Rio Grande do Sul", "Emater/RS"],
        "lead_materia_longa": "O Rio Grande do Sul amanheceu congelando. Quase 70 cidades gaúchas registraram temperaturas abaixo de zero em um dos amanheceres mais frios do ano, episódio que marcou as menores mínimas de 2026 em diversas localidades.",
        "post_instagram": {
            "caption": "O cobertor não foi suficiente: o Rio Grande do Sul amanheceu congelando. Quase 70 cidades gaúchas registraram temperaturas abaixo de zero em um dos amanheceres mais frios do ano, com geada cobrindo campos e telhados em boa parte do estado. As mínimas marcaram os menores valores de 2026 em diversas localidades, reforçando o caráter rigoroso deste inverno. No campo, o frio extremo exige atenção dobrada: a geada pode comprometer pastagens e culturas sensíveis, e os animais precisam de abrigo e alimentação reforçada. Na cidade, o cuidado é com a saúde, especialmente de crianças e idosos, e com quem vive em situação de rua. Vale agasalhar bem, manter os ambientes aquecidos com segurança e ficar de olho na previsão. O inverno gaúcho chegou mostrando a que veio.",
            "hashtags": ["#RioGrandedoSul", "#Frio", "#Geada", "#Inverno", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O Rio Grande do Sul amanheceu congelando.",
            "desenvolvimento_45s": "Quase 70 cidades gaúchas registraram temperaturas abaixo de zero em um dos amanheceres mais frios do ano, com geada cobrindo campos e telhados em boa parte do estado. As mínimas marcaram os menores valores de 2026 em diversas localidades. No campo, o frio extremo exige atenção: a geada pode comprometer pastagens e culturas sensíveis, e os animais precisam de abrigo. Na cidade, o cuidado é com a saúde, especialmente de crianças, idosos e quem vive em situação de rua.",
            "fechamento_8s": "O inverno gaúcho chegou pra valer.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "fria e contemplativa"
        },
        "tag_thumbnail": "frio, geada, Rio Grande do Sul",
        "briefing_visual": {
            "descricao_pt": "Campo coberto de geada branca ao amanhecer no interior do Rio Grande do Sul, vegetação congelada, sem pessoas",
            "query_en": ["frost covered field sunrise", "white frost grass morning", "frozen pasture winter"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A field covered in white frost at sunrise in the southern Brazilian countryside, frozen grass, cold morning light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima regional de forte impacto (RS), dado concreto. Insumo reformatado como conteúdo próprio, sem menção a veículo. Sem guardrail."
    },

    # IDX 20 — RS: esclarecimento sobre ciclone no fim de semana — PUBLICAR (regional, serviço/anti-fake)
    "e40cfca61a2890d7a59df6e6447f68903f8c80eb": {
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Entenda o que é real sobre o ciclone previsto para o fim de semana no Rio Grande do Sul",
        "chamada_faixa": "Ciclone no fim de semana: o que é real",
        "subtitulo": "Sistema deve trazer chuva e vento, mas publicações com alertas exagerados circulam sem confirmação técnica.",
        "lead": "Entre o que é fato e o que é boato, vale separar bem as informações sobre o tempo no Rio Grande do Sul. Um sistema de baixa pressão deve trazer chuva e vento ao estado neste fim de semana, mas publicações com alertas exagerados, de tempestades catastróficas e ventos extremos, circulam sem qualquer respaldo técnico e merecem cautela.",
        "ganchos_3": [
            "Sistema traz chuva e vento ao RS no fim de semana",
            "Alertas exagerados circulam sem confirmação técnica",
            "Acompanhar fontes confiáveis evita pânico desnecessário"
        ],
        "angulo_editorial": "Serviço de utilidade pública e combate à desinformação climática, de alcance regional (RS) e oportuno para o próprio fim de semana. Insumo meteorológico reformatado como conteúdo próprio, sem menção a veículo (regra 12). Sem guardrail.",
        "fontes_complementares_sugeridas": ["Defesa Civil do Rio Grande do Sul", "Estações meteorológicas oficiais"],
        "lead_materia_longa": "Entre o que é fato e o que é boato, vale separar bem as informações sobre o tempo no Rio Grande do Sul. Um sistema de baixa pressão deve trazer chuva e vento ao estado neste fim de semana, mas publicações com alertas exagerados circulam sem qualquer respaldo técnico.",
        "post_instagram": {
            "caption": "Calma com o que circula por aí sobre o tempo no fim de semana. É verdade que um sistema de baixa pressão deve trazer chuva e vento ao Rio Grande do Sul nos próximos dias. Mas as publicações que falam em alerta vermelho, ventos de 100 km/h e tempestades catastróficas não têm respaldo técnico e acabam espalhando pânico sem necessidade. A recomendação é simples: acompanhe a previsão por fontes confiáveis e oficiais, como a Defesa Civil, e desconfie de mensagens alarmistas repassadas em redes sociais e grupos. Chuva e vento pedem cuidado, sim: evite áreas alagadas, garagens em terreno baixo e abrigos improvisados sob árvores. Mas informação de qualidade é o melhor guarda-chuva. Antes de compartilhar, confira. O boato corre rápido, mas a informação correta protege mais.",
            "hashtags": ["#RioGrandedoSul", "#Clima", "#DefesaCivil", "#FakeNews", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Ciclone no fim de semana: o que é real?",
            "desenvolvimento_45s": "Um sistema de baixa pressão deve trazer chuva e vento ao Rio Grande do Sul neste fim de semana. Mas as publicações que falam em alerta vermelho, ventos de 100 km/h e tempestades catastróficas não têm respaldo técnico e espalham pânico sem necessidade. A recomendação é acompanhar a previsão por fontes oficiais, como a Defesa Civil, e desconfiar de mensagens alarmistas. Chuva e vento pedem cuidado, mas informação de qualidade é o melhor guarda-chuva.",
            "fechamento_8s": "Antes de compartilhar, confira.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativa e tranquilizadora"
        },
        "tag_thumbnail": "clima, ciclone, Rio Grande do Sul",
        "briefing_visual": {
            "descricao_pt": "Céu carregado de nuvens de chuva sobre paisagem do interior gaúcho, clima de frente fria se aproximando, sem pessoas",
            "query_en": ["storm clouds approaching sky", "dark rain clouds countryside", "cloudy weather front"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos", "cenas de destruição"],
            "prompt_ia": "Heavy rain clouds approaching over the southern Brazilian countryside, an incoming weather front, dramatic but calm sky, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público e combate à desinformação climática, regional e oportuno. Insumo reformatado, sem menção a veículo. Sem guardrail."
    },

    # IDX 8 — São Lourenço do Sul: gestão recebe Sesc/Senac/Sindilojas — PUBLICAR (núcleo, economia/cultura)
    "4a19f3b447abaaef75271b2e2dbf1a33ae46591b": {
        "titulo_sultv": "São Lourenço do Sul articula ações com Sesc, Senac e Sindilojas para o município",
        "chamada_faixa": "São Lourenço alinha ações com Sesc e Senac",
        "subtitulo": "Gestão municipal recebe representantes das entidades para discutir parcerias em cultura, educação e comércio.",
        "lead": "Parcerias podem render novas oportunidades em São Lourenço do Sul. A gestão municipal recebeu representantes do Sesc, do Senac e do Sindilojas para alinhar possíveis ações no município, encontro voltado a articular iniciativas nas áreas de cultura, qualificação profissional e fortalecimento do comércio local.",
        "ganchos_3": [
            "Gestão municipal recebe Sesc, Senac e Sindilojas",
            "Encontro discute ações de cultura e qualificação",
            "Objetivo é fortalecer parcerias no município"
        ],
        "angulo_editorial": "Desenvolvimento econômico e cultural em cidade-núcleo (São Lourenço do Sul), fonte primária institucional (Prefeitura e entidades). Fato concreto e positivo, sem viés partidário. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Sesc/Senac", "Sindilojas"],
        "lead_materia_longa": "Parcerias podem render novas oportunidades em São Lourenço do Sul. A gestão municipal recebeu representantes do Sesc, do Senac e do Sindilojas para alinhar possíveis ações no município.",
        "post_instagram": {
            "caption": "Boas parcerias começam numa boa conversa. Em São Lourenço do Sul, a gestão municipal recebeu representantes do Sesc, do Senac e do Sindilojas para alinhar possíveis ações no município. O encontro mira iniciativas nas áreas de cultura, qualificação profissional e fortalecimento do comércio local, três frentes que, juntas, movimentam a economia e ampliam as oportunidades para a população. A aproximação do poder público com entidades como Sesc e Senac costuma abrir portas para cursos, eventos culturais e capacitação de trabalhadores, enquanto o diálogo com o Sindilojas reforça o comércio, que é uma das principais fontes de emprego e renda das cidades do interior. São articulações que nem sempre viram manchete, mas que preparam o terreno para projetos concretos. Quando setor público, sistema S e comércio remam juntos, quem ganha é a cidade.",
            "hashtags": ["#SãoLourençodoSul", "#Economia", "#Qualificação", "#Comércio", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "São Lourenço articula novas parcerias.",
            "desenvolvimento_45s": "A gestão municipal de São Lourenço do Sul recebeu representantes do Sesc, do Senac e do Sindilojas para alinhar possíveis ações no município. O encontro mira iniciativas em cultura, qualificação profissional e fortalecimento do comércio local. A aproximação do poder público com essas entidades costuma abrir portas para cursos, eventos culturais e capacitação de trabalhadores, enquanto o diálogo com o comércio reforça uma das principais fontes de emprego e renda do interior.",
            "fechamento_8s": "Quando todos remam juntos, a cidade ganha.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "otimista e institucional"
        },
        "tag_thumbnail": "parcerias, São Lourenço do Sul",
        "briefing_visual": {
            "descricao_pt": "Reunião institucional em sala com mesa e representantes, ambiente de prefeitura do interior gaúcho, sem rostos identificáveis",
            "query_en": ["business meeting table handshake", "institutional meeting room", "partnership agreement office"],
            "evitar": ["rostos identificáveis", "marcas comerciais", "texto", "logos"],
            "prompt_ia": "An institutional meeting around a table in a municipal government office, partnership discussion, daylight, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Desenvolvimento econômico e cultural em cidade-núcleo (São Lourenço do Sul), fonte primária institucional. Sem guardrail."
    },

    # ---------- REBAIXADAS ----------
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "REBAIXAR", "Conteúdo com data de origem antiga (abril/2026) — risco de informação desatualizada. Vira nota interna.",
        "Arambaré abre inscrições para cursos gratuitos de qualificação profissional"),
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "REBAIXAR", "Edital procedural (ampliação de perímetro urbano) — fato relevante, mas formato de edital. Nota interna.",
        "Chuvisca abre prazo para requerimentos sobre ampliação do perímetro urbano"),
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "REBAIXAR", "Comunicado procedural sobre emissão de notas fiscais. Baixo apelo editorial. Nota interna.",
        "Sentinela do Sul orienta sobre emissão de notas fiscais pelo emissor nacional"),
    "93d8797025ffe98d7c47bb3b29fd426a9dec54b2": _skip(
        "REBAIXAR", "Título capturado como cabeçalho de seção; evento (velejaço solidário) pouco detalhado. Nota interna.",
        "Barra do Ribeiro promove velejaço solidário"),
    "bd92711b7702c7c7df50a735bc52c15c8fa5e140": _skip(
        "REBAIXAR", "Pauta nacional (Censo Escolar) sem âncora regional Sul-RS. Nota interna.",
        "Censo Escolar: Brasil reduz índices de reprovação, abandono e atraso"),
    "0c78bd0cc00e7d0302fc635b3fdbfbd510252753": _skip(
        "REBAIXAR", "Concurso com classificação prevista para 13 de maio — data já passada/desatualizada. Nota interna.",
        "Concurso do Magistério Municipal de Pelotas divulga classificações finais"),
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "REBAIXAR", "Pauta parlamentar com viés político (concessões/privatizações/PPPs). Sensível à regra 7. Nota interna.",
        "Audiência em Pelotas debate concessões, privatizações e PPPs"),
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR", "Conteúdo técnico-parlamentar (destinação ao Funcriança) de baixo apelo para audiência ampla. Nota interna.",
        "Técnicos detalham destinação de recursos ao Funcriança"),

    # ---------- BLOQUEADAS ----------
    "d48e67cad304aef9b72e4bcf4e33cf9d5a2ea7d2": _skip(
        "BLOQUEAR", "Conteúdo promocional de loteria, sem âncora regional Sul-RS e com apelo comercial. Guardrail editorial.",
        "Quina de São João: O Sonho que Move o Brasil"),
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR", "Edital de penalidade — documento procedural sem valor de pauta jornalística.",
        "Edital de Publicação de Penalidade nº 001/2026"),
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR", "Aviso/edital procedural; título é cabeçalho de seção sem corpo informativo.",
        "Aviso de Audiência Pública"),
    "a6d042be95d54d6ef82415d825a77afc9d6fa43d": _skip(
        "BLOQUEAR", "Título capturado como cabeçalho de menu de seção ('Secretaria Municipal da Saúde'). Sem matéria.",
        "8ª Conferência Municipal de Saúde"),
    "afc5e49b365c8ddba389483c86a9f6845d33444d": _skip(
        "BLOQUEAR", "Pauta internacional (calor na França/Europa) sem qualquer âncora regional Sul-RS.",
        "Calor extremo atinge níveis jamais vistos na França e abala a Europa"),
    "364aa009610c478f160694aead474f82753f3cf7": _skip(
        "BLOQUEAR", "Pauta internacional (onda de calor na Europa) sem âncora regional Sul-RS.",
        "Brutal onda de calor destrói centenas de recordes na Europa"),

    # ---------- POSTS (score 5-6, formato post_instagram, viram nota interna) ----------
    "c85ac3696d7da10929f8082aeb17de1ac01c2a0e": _skip(
        "REBAIXAR", "Score editorial 6, formato post — fora da cota de matéria longa. Disponível como post.",
        "Jardim Botânico da UFSM inaugura pracinha voltada ao público infantil"),
    "9f62b86b08e5c4a4aebd6000472ab5493fde551f": _skip(
        "REBAIXAR", "Score editorial 6, formato post — fora da cota de matéria longa. Disponível como post.",
        "Banda Sinfônica da UFSM leva projeto 'Ouvir para crescer' a escolas"),
    "9c1188fb04e860d886f3342576732b4b3088b847": _skip(
        "REBAIXAR", "Score editorial 5, baixo apelo regional para matéria. Nota interna.",
        "Histórias das empresas de Venâncio Aires"),
    "a8f396bf0677a14ff11310170431f850dbc174cb": _skip(
        "REBAIXAR", "Score editorial 5, pauta econômica local de Venâncio Aires fora do eixo-núcleo. Nota interna.",
        "IPC Maps 2026 projeta estagnação da economia de Venâncio Aires"),
    "b24bbe4adac176121807f02cff7f21bd5c75c2f6": _skip(
        "REBAIXAR", "Score editorial 5, evento em Bento Gonçalves fora do eixo-núcleo. Nota interna.",
        "Competitividade na era da IA é tema de encontro em Bento Gonçalves"),
    "0be8b4cbff1dbf8016c68a1fe65cad127516f660": _skip(
        "BLOQUEAR", "Resultado esportivo nacional (Copa) sem âncora regional Sul-RS — duplica cobertura genérica.",
        "Brasil vence Escócia por 3 a 0 na Copa do Mundo"),
}


MATERIAS = {

    "e37450da327ccf4b05690c92043f1e958b833e12": """### Título ###
Camaquã tem sábado de sol e tempo firme antes da chuva chegar no domingo

### Artigo ###
O sábado é de aproveitar o tempo aberto em Camaquã. A previsão aponta um dia de tempo firme, com céu limpo e predomínio de sol no município, condição que deve durar até o início do domingo, quando a chegada de uma frente úmida traz de volta a possibilidade de chuva. Depois de semanas marcadas pelo frio rigoroso que tomou conta do Rio Grande do Sul, o dia ensolarado funciona como um respiro para os moradores. É a oportunidade ideal para colocar a rotina em dia, estender a roupa no varal, cuidar do jardim ou simplesmente aproveitar um programa ao ar livre em família. As temperaturas seguem típicas do inverno gaúcho, com manhã fria e tarde mais amena sob o sol. A estabilidade, no entanto, tem prazo para acabar. A partir do domingo, a aproximação de um sistema úmido aumenta a nebulosidade sobre a região e devolve ao cenário a chance de pancadas de chuva, encerrando a sequência de tempo seco. Quem tem planos para o fim de semana ganha um aliado no sábado e deve se organizar pensando na virada do tempo no dia seguinte. Tarefas que dependem do tempo bom, como pintura, colheita de pequenos cultivos, eventos ao ar livre e deslocamentos pela zona rural, encontram nesta janela de sol a melhor condição dos próximos dias. Para o produtor rural da Costa Doce, acompanhar de perto a previsão é parte da rotina: a alternância entre dias firmes e a entrada de frentes úmidas influencia diretamente o planejamento das atividades no campo. A recomendação é aproveitar o sol enquanto ele dura e manter atenção ao avanço da chuva a partir de domingo, ajustando a agenda conforme a mudança. Em Camaquã, o fim de semana começa convidativo, com o céu aberto abrindo espaço para boas atividades antes de o tempo mudar.

### Legenda sugerida ###
Camaquã tem sábado de tempo firme e sol; a partir do domingo, uma frente úmida traz de volta a possibilidade de chuva.

### Palavras-chave ###
Camaquã, previsão do tempo, fim de semana, sol, chuva, Costa Doce, Rio Grande do Sul
""",

    "fca7c3b2a464c1917e53e9c9c40b00e454567e5d": """### Título ###
Camaquã terá expediente reduzido e aulas suspensas na segunda por jogo do Brasil

### Artigo ###
A Seleção Brasileira mexe com a rotina de Camaquã. A Prefeitura confirmou expediente reduzido nas repartições municipais e a suspensão das aulas no turno da tarde na próxima segunda-feira, dia 29, em razão da partida do Brasil pela Copa do Mundo. A medida organiza o funcionamento dos serviços públicos em torno do horário do jogo, permitindo que servidores, estudantes e suas famílias acompanhem a Seleção em campo. A decisão acompanha um movimento que se repete em todo o país a cada Copa do Mundo, quando o Brasil praticamente para para torcer. Em jogos da Seleção, é comum que prefeituras, escolas e órgãos públicos ajustem seus horários, conciliando o atendimento essencial à população com o clima de festa e união que as partidas despertam. Para o morador de Camaquã, o aviso é importante e exige um pouco de planejamento. Quem precisa de algum serviço nas repartições municipais deve se programar para resolver as pendências antes do horário especial, evitando o deslocamento até uma porta fechada. No caso das escolas, as famílias devem ficar atentas à suspensão das aulas da tarde, organizando a rotina das crianças e dos adolescentes para o dia. Mais do que uma simples mudança de horário, a iniciativa reconhece o peso que a Copa do Mundo tem na vida das cidades brasileiras. O futebol, nesses momentos, deixa de ser apenas esporte e vira ponto de encontro: reúne vizinhos, aproxima gerações e pinta as ruas de verde e amarelo. Em Camaquã, a recomendação é anotar a data, organizar a agenda e preparar a torcida. Na segunda-feira, com expediente reduzido e aulas da tarde suspensas, a cidade se prepara para acompanhar mais um capítulo da Seleção Brasileira na Copa do Mundo.

### Legenda sugerida ###
Prefeitura de Camaquã terá expediente reduzido e aulas da tarde suspensas na segunda-feira, dia 29, por causa do jogo do Brasil na Copa.

### Palavras-chave ###
Camaquã, Copa do Mundo, Seleção Brasileira, expediente, aulas suspensas, serviço público, Costa Doce
""",

    "6efbfa9389c4b51a10c5e9449458fa3c97f3b5aa": """### Título ###
São Lourenço do Sul define horário excepcional de expediente durante a Copa do Mundo

### Artigo ###
São Lourenço do Sul também acerta o relógio com a Copa. O Município publicou o Decreto nº 7.014, que estabelece horário excepcional de expediente nas repartições públicas municipais nos dias de partidas da Seleção Brasileira na Copa do Mundo. A norma ajusta o atendimento ao público para que servidores e moradores possam acompanhar os jogos, conciliando o funcionamento dos serviços essenciais com o clima de torcida que toma conta do país. A iniciativa segue um padrão observado em diversas cidades brasileiras durante os Mundiais. Em jogos da Seleção, prefeituras e órgãos públicos costumam reorganizar os horários de funcionamento, garantindo que os serviços indispensáveis sigam disponíveis enquanto se cria espaço para que a comunidade vivencie esse momento de união em torno do futebol. Para a população de São Lourenço do Sul, o decreto traz um recado prático. Quem depende de algum serviço da Prefeitura nos dias de jogo deve conferir o novo horário antes de se deslocar, organizando-se para resolver demandas com antecedência e evitando contratempos. A formalização da medida por meio de decreto dá segurança jurídica e transparência ao ajuste, deixando claro a servidores e cidadãos como ficará o atendimento. A Copa do Mundo tem esse poder de mobilizar cidades inteiras, e a Costa Doce não fica de fora. Mais do que esporte, as partidas da Seleção viram ponto de encontro entre familiares, vizinhos e amigos, pintando as ruas e os comércios de verde e amarelo. Ao publicar o decreto, São Lourenço do Sul organiza sua rotina para participar dessa festa sem deixar de lado o compromisso com o serviço público. A recomendação aos moradores é simples: acompanhar o horário definido, programar a agenda e preparar a torcida para acompanhar o Brasil em campo.

### Legenda sugerida ###
Decreto municipal de São Lourenço do Sul define horário excepcional de expediente nas repartições públicas nos dias de jogos do Brasil na Copa.

### Palavras-chave ###
São Lourenço do Sul, Copa do Mundo, expediente, decreto, serviço público, Costa Doce, Seleção Brasileira
""",

    "01ef011ecdae21c60e1584906736e0e1b68bd082": """### Título ###
Cristal reforça estradas do interior com cascalhamento e patrolamento

### Artigo ###
As estradas que ligam o campo à cidade ganham atenção em Cristal. A Prefeitura realiza um pacote de melhorias nas vias do interior do município, com serviços de cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades. O trabalho atende uma demanda histórica de quem vive e produz longe do centro, facilitando o escoamento da produção e o deslocamento diário das famílias do meio rural. Estrada boa é mais do que conforto: é condição para a economia girar. Vias bem conservadas reduzem o desgaste de veículos e máquinas, diminuem o tempo de viagem e tornam mais seguro o transporte de safras, insumos, leite e animais. Para o produtor da região, isso significa menos prejuízo e mais previsibilidade na hora de levar a produção até os pontos de comercialização. O cascalhamento e o patrolamento, serviços executados nessa etapa, têm papel central nesse processo. O patrolamento nivela o leito da estrada, corrige buracos e melhora o escoamento da água das chuvas, enquanto o cascalhamento dá firmeza ao piso, evitando os atoleiros tão comuns nos períodos chuvosos. Juntas, as duas ações prolongam a vida útil das vias e reduzem a necessidade de reparos constantes. O alcance do trabalho a diferentes localidades reforça o caráter de serviço público que chega à ponta. Estradas rurais bem cuidadas garantem o acesso de ônibus escolares que levam crianças e adolescentes às aulas, de ambulâncias que atendem emergências no interior e de todos que precisam se deslocar até os serviços essenciais oferecidos na sede do município. Em uma região de forte vocação agrícola, manter a malha rural em boas condições é investir diretamente na qualidade de vida e na produção. Ao reforçar as estradas do interior, Cristal mostra que o desenvolvimento do município passa, antes de tudo, pelo caminho que leva até a porteira de cada propriedade.

### Legenda sugerida ###
Prefeitura de Cristal executa melhorias nas estradas do interior, com cascalhamento, patrolamento e apoio às propriedades rurais.

### Palavras-chave ###
Cristal, estradas rurais, cascalhamento, patrolamento, zona rural, agro, Costa Doce
""",

    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": """### Título ###
Arambaré publica nota técnica com orientações sobre poda e arborização urbana

### Artigo ###
O verde das ruas de Arambaré ganha um manual de cuidados. A Prefeitura, por meio da Diretoria Municipal de Meio Ambiente, publicou a Nota Técnica nº 01/2026 com orientações sobre o manejo da arborização urbana e a poda de árvores. O documento organiza as boas práticas e esclarece a população sobre como proceder de forma correta e segura, evitando danos às plantas, riscos à rede elétrica e cortes irregulares. A arborização urbana cumpre um papel que vai muito além do visual. As árvores das cidades oferecem sombra, ajudam a reduzir a temperatura nos dias quentes, melhoram a qualidade do ar, abrigam a fauna local e contribuem para o bem-estar de quem caminha pelas ruas. Cuidar desse patrimônio verde é, portanto, um compromisso coletivo, que envolve tanto o poder público quanto cada morador. A nota técnica nasce justamente para orientar essa convivência. A poda, quando feita de forma inadequada, pode comprometer a saúde da árvore, deixá-la vulnerável a pragas e doenças e até representar perigo, com a queda de galhos. Por isso, o documento esclarece em quais situações a intervenção é recomendada, como ela deve ser executada e qual o papel da Diretoria de Meio Ambiente na autorização e no acompanhamento dos serviços. Para o morador, a recomendação é clara: antes de pegar a serra ou contratar uma poda por conta própria, é importante procurar a Diretoria Municipal de Meio Ambiente para se informar sobre os procedimentos. Em muitos casos, a intervenção em árvores depende de autorização, e a orientação técnica evita problemas tanto para a vegetação quanto para a segurança das pessoas e do patrimônio. Ao publicar a nota técnica, Arambaré dá um passo importante na gestão do seu ambiente urbano. A iniciativa une informação, prevenção e responsabilidade, mostrando que cuidar das árvores é cuidar da cidade inteira, das calçadas às casas, do clima local à qualidade de vida de toda a comunidade.

### Legenda sugerida ###
Diretoria Municipal de Meio Ambiente de Arambaré publica nota técnica com orientações sobre manejo da arborização urbana e poda de árvores.

### Palavras-chave ###
Arambaré, meio ambiente, arborização urbana, poda de árvores, nota técnica, Costa Doce
""",

    "039fa52e365e6c812a99ca228536b63e7dbf902a": """### Título ###
Chuvisca organiza atendimentos de fonoaudiologia para ampliar o acesso da população

### Artigo ###
O acesso à saúde dá um passo a mais em Chuvisca. A Prefeitura, por meio da Secretaria Municipal de Saúde, organizou os atendimentos de fonoaudiologia realizados na unidade de Saúde Mental do município. A medida busca ampliar o alcance do serviço e garantir que mais moradores sejam atendidos de forma estruturada, com agenda e fluxos mais bem definidos. A fonoaudiologia ocupa um espaço importante na rede de cuidados de qualquer comunidade. A área acompanha o desenvolvimento da fala e da linguagem na infância, auxilia em questões de audição e voz e atua na reabilitação de pessoas de todas as idades, inclusive na recuperação de pacientes após determinadas condições de saúde. Contar com esse atendimento na rede pública faz diferença real para muitas famílias, especialmente em municípios do interior, onde nem sempre é fácil acessar profissionais especializados. Organizar os atendimentos significa, na prática, dar mais previsibilidade ao serviço. Com a agenda estruturada, é possível reduzir filas de espera, evitar deslocamentos desnecessários e assegurar que o morador encontre o atendimento quando precisa. Esse cuidado com a gestão do serviço público traduz uma preocupação em fazer com que os recursos disponíveis cheguem ao maior número possível de pessoas, de maneira justa e ordenada. A escolha de concentrar os atendimentos na unidade de Saúde Mental reforça uma visão integrada do cuidado, em que diferentes áreas da saúde dialogam para acolher o paciente de forma completa. Para a população, o recado é de que o serviço está disponível e mais bem organizado. Quem busca atendimento em fonoaudiologia deve procurar a unidade de saúde do município para se informar sobre como funciona o agendamento e quais são os critérios de acesso. Ao estruturar essa oferta, Chuvisca demonstra que ampliar o acesso à saúde não depende apenas de grandes investimentos: passa, muitas vezes, por organizar bem o que já existe, colocando o cuidado com as pessoas no centro das decisões.

### Legenda sugerida ###
Secretaria Municipal de Saúde de Chuvisca organiza os atendimentos de fonoaudiologia na unidade de Saúde Mental para ampliar o acesso da população.

### Palavras-chave ###
Chuvisca, saúde pública, fonoaudiologia, acesso à saúde, Secretaria de Saúde, Costa Doce
""",

    "9ce36499a218324114c169a9d64f04aae0558ec9": """### Título ###
Cristal participa do lançamento do PREPARA RS, programa de prevenção a eventos climáticos

### Artigo ###
Diante de um clima cada vez mais imprevisível, a prevenção entra na agenda de Cristal. O município participou do lançamento do PREPARA RS, programa que apresenta ações de prevenção e disponibiliza recursos para preparar as cidades gaúchas diante de eventos climáticos extremos. O tema ganhou urgência no Rio Grande do Sul nos últimos anos, marcados por enchentes, estiagens e temporais que deixaram cicatrizes em diversas regiões do estado. A proposta do programa é provocar uma mudança de postura: sair do modo reação e entrar no modo planejamento. Na prática, isso significa mapear áreas de risco, estruturar planos de contingência, fortalecer a defesa civil municipal e capacitar equipes antes que o próximo evento extremo aconteça. Em vez de correr atrás do prejuízo depois da tragédia, a ideia é antecipar-se a ela, reduzindo perdas humanas e materiais. Para uma cidade do interior como Cristal, integrar uma iniciativa desse porte representa acesso a apoio técnico e a recursos que dificilmente um município de pequeno porte conseguiria mobilizar sozinho. A prevenção depende de planejamento, equipamentos, treinamento e informação, e programas estaduais ajudam a colocar essas peças no lugar, fortalecendo a capacidade local de resposta. Os eventos climáticos recentes mostraram que nenhuma região está totalmente a salvo. Chuvas intensas podem provocar alagamentos e deslizamentos, enquanto longos períodos de estiagem afetam o abastecimento de água e a produção no campo, atingindo diretamente a economia e a vida das famílias. Estar preparado, nesse cenário, deixou de ser um diferencial e passou a ser uma necessidade. Ao participar do lançamento do PREPARA RS, Cristal sinaliza que entendeu o tamanho do desafio. Investir em prevenção é proteger vidas, preservar o patrimônio das famílias e dar mais segurança a toda a comunidade. O clima mudou, e a melhor resposta possível é chegar preparado para o que vier.

### Legenda sugerida ###
Cristal participa do lançamento do PREPARA RS, programa estadual que reúne ações e recursos de prevenção a eventos climáticos extremos.

### Palavras-chave ###
Cristal, PREPARA RS, prevenção, eventos climáticos, defesa civil, Rio Grande do Sul, Costa Doce
""",

    "775f9b501ba50ff6ad224de967b2336e8dfb9479": """### Título ###
Onda de frio leva quase 70 cidades gaúchas a registrar temperaturas abaixo de zero

### Artigo ###
O Rio Grande do Sul amanheceu congelando. Quase 70 cidades gaúchas registraram temperaturas abaixo de zero em um dos amanheceres mais frios do ano, episódio que marcou as menores mínimas de 2026 em diversas localidades e cobriu campos e telhados de geada em boa parte do estado. O frio intenso reforça o caráter rigoroso deste inverno e exige cuidados redobrados no campo e na cidade. A geada que acompanha esses amanheceres congelantes é uma das maiores preocupações para quem vive da terra. Quando a temperatura despenca, culturas sensíveis e pastagens podem ser comprometidas, afetando a alimentação dos rebanhos e o calendário das atividades agrícolas. Para o produtor, é o momento de redobrar a atenção: proteger plantas mais vulneráveis, garantir abrigo e reforço na alimentação dos animais e acompanhar de perto a evolução das temperaturas nos próximos dias. Nas cidades, o frio extremo traz outros desafios. O cuidado com a saúde se torna prioridade, especialmente para os grupos mais vulneráveis, como crianças, idosos e pessoas com doenças respiratórias. Manter-se aquecido, evitar mudanças bruscas de temperatura e ventilar adequadamente os ambientes em que se usa aquecimento são recomendações simples, mas que fazem diferença. A atenção também precisa se voltar para quem está em situação de rua, para quem o frio rigoroso representa um risco real à vida. O episódio se soma a uma sequência de dias gelados que vem marcando o inverno gaúcho. As baixas temperaturas, embora típicas da estação no extremo sul do país, chamam a atenção pela intensidade e pela abrangência, atingindo simultaneamente dezenas de municípios. Acompanhar a previsão e adotar medidas de proteção é a melhor forma de enfrentar esse período. No campo e na cidade, o recado é o mesmo: o inverno chegou mostrando a que veio, e o cuidado com as pessoas, os animais e as lavouras deve estar no topo da lista de prioridades enquanto o frio rigoroso persistir sobre o Rio Grande do Sul.

### Legenda sugerida ###
Quase 70 cidades gaúchas registraram temperaturas abaixo de zero em um dos amanheceres mais frios do ano, com geada e cuidados redobrados no campo e na cidade.

### Palavras-chave ###
Rio Grande do Sul, frio, geada, inverno, temperaturas abaixo de zero, campo, saúde
""",

    "e40cfca61a2890d7a59df6e6447f68903f8c80eb": """### Título ###
Entenda o que é real sobre o ciclone previsto para o fim de semana no Rio Grande do Sul

### Artigo ###
Entre o que é fato e o que é boato, vale separar bem as informações sobre o tempo no Rio Grande do Sul. Um sistema de baixa pressão deve trazer chuva e vento ao estado neste fim de semana, mas publicações com alertas exagerados, que falam em tempestades catastróficas, alerta vermelho e ventos extremos, circulam sem qualquer respaldo técnico e merecem cautela. Saber distinguir a previsão responsável do alarmismo é essencial para enfrentar o período com tranquilidade e segurança. A formação de sistemas de baixa pressão e a passagem de frentes são fenômenos comuns no inverno gaúcho e fazem parte da dinâmica natural do tempo na região. Eles podem, sim, provocar chuva, rajadas de vento e queda de temperatura, condições que pedem atenção, mas que estão dentro do esperado para a estação. O problema surge quando informações distorcidas transformam uma previsão comum em pânico, exagerando números e criando uma sensação de catástrofe iminente que não corresponde à realidade. A desinformação climática tem efeitos concretos e prejudiciais. Mensagens alarmistas repassadas em redes sociais e grupos de aplicativos podem gerar medo desnecessário, sobrecarregar serviços de emergência e, no limite, fazer com que as pessoas deixem de levar a sério os alertas verdadeiramente importantes quando eles forem emitidos pelas autoridades competentes. Por isso, a recomendação é buscar informação de qualidade e confiar em fontes oficiais. Órgãos como a Defesa Civil acompanham permanentemente as condições do tempo e emitem alertas baseados em dados técnicos sempre que há risco real. Diante de chuva e vento, alguns cuidados básicos ajudam a evitar problemas: manter distância de áreas alagadas, não buscar abrigo sob árvores durante temporais, atenção a garagens e construções em terreno baixo e cuidado com objetos soltos que possam ser arremessados pelo vento. A informação correta, no entanto, segue sendo a melhor proteção. Antes de compartilhar mensagens alarmantes, vale conferir a origem e a veracidade do conteúdo. O boato corre rápido, mas é a informação responsável que de fato protege a população do Rio Grande do Sul.

### Legenda sugerida ###
Sistema de baixa pressão deve trazer chuva e vento ao RS no fim de semana, mas alertas exagerados que circulam não têm respaldo técnico; acompanhe fontes oficiais.

### Palavras-chave ###
Rio Grande do Sul, clima, ciclone, fim de semana, desinformação, Defesa Civil, chuva
""",

    "4a19f3b447abaaef75271b2e2dbf1a33ae46591b": """### Título ###
São Lourenço do Sul articula ações com Sesc, Senac e Sindilojas para o município

### Artigo ###
Parcerias podem render novas oportunidades em São Lourenço do Sul. A gestão municipal recebeu representantes do Sesc, do Senac e do Sindilojas para alinhar possíveis ações no município. O encontro foi voltado a articular iniciativas nas áreas de cultura, qualificação profissional e fortalecimento do comércio local, três frentes que, juntas, movimentam a economia e ampliam as oportunidades para a população. A aproximação entre o poder público e entidades como Sesc e Senac costuma abrir portas importantes. O Sesc tradicionalmente atua em projetos de cultura, lazer, esporte e ação social, enquanto o Senac é referência em educação profissional, com cursos que capacitam trabalhadores para o mercado. Quando essas instituições dialogam com a administração municipal, surgem possibilidades concretas de levar à comunidade eventos culturais, atividades formativas e qualificação que fazem diferença na vida das pessoas e na economia da cidade. O diálogo com o Sindilojas reforça outra dimensão estratégica: o comércio. Nas cidades do interior, o setor é uma das principais fontes de emprego e renda, e fortalecer os lojistas significa dar fôlego a toda a cadeia econômica local. Iniciativas conjuntas podem resultar em capacitação para comerciantes e funcionários, ações de incentivo ao consumo na cidade e estratégias para enfrentar desafios comuns ao varejo. Articulações como essa nem sempre ganham destaque no dia a dia, mas têm papel fundamental na construção do desenvolvimento. É no encontro entre setor público, sistema S e iniciativa privada que muitos projetos ganham viabilidade, somando recursos, conhecimento técnico e capacidade de execução. Reuniões de alinhamento são o primeiro passo para transformar boas intenções em ações concretas. Ao receber as entidades e buscar esse alinhamento, São Lourenço do Sul demonstra disposição para somar esforços em favor da comunidade. Quando setor público, sistema S e comércio remam na mesma direção, quem ganha é a cidade, com mais cultura, mais qualificação e uma economia local mais forte e preparada para crescer.

### Legenda sugerida ###
Gestão municipal de São Lourenço do Sul recebe representantes do Sesc, Senac e Sindilojas para alinhar ações em cultura, qualificação e comércio.

### Palavras-chave ###
São Lourenço do Sul, Sesc, Senac, Sindilojas, economia, qualificação, comércio, Costa Doce
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
