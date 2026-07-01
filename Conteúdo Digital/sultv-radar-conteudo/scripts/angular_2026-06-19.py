#!/usr/bin/env python3
"""
angular_2026-06-19.py — angulação editorial + redação (cowork-faz-tudo).
Decisões editoriais Claude na sessão para a pauta de 2026-06-19.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-19"


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

    # IDX 0 — Copa Prefeito de Cristal volta sábado (Cristal, esporte) — PUBLICAR
    "2eac2f6cebf64e843cf46c36ea8a00003737d43a": {
        "cidade": "Cristal",
        "tag_principal": "esporte",
        "titulo_sultv": "Copa Prefeito de Cristal retorna neste sábado com três jogos no Complexo Danilo Ribeiro Braga",
        "chamada_faixa": "Copa Prefeito de Cristal volta no sábado",
        "subtitulo": "Competição de futebol amador movimenta o esporte local com três partidas marcadas para este sábado (20) em Cristal.",
        "lead": "A Copa Prefeito de Cristal volta a movimentar o esporte amador do município neste sábado (20), com três jogos programados para o Complexo Esportivo Danilo Ribeiro Braga. A rodada acontece após o adiamento das partidas anteriores e recoloca a competição no calendário esportivo de Cristal, na região da Costa Doce.",
        "ganchos_3": [
            "Copa Prefeito de Cristal retorna neste sábado (20)",
            "Três jogos marcados no Complexo Danilo Ribeiro Braga",
            "Competição amadora reúne equipes de Cristal e região"
        ],
        "angulo_editorial": "Esporte amador em cidade-núcleo (Cristal/Costa Doce) — pauta comunitária positiva que valoriza o futebol local e mobiliza torcedores e famílias no fim de semana. Sem viés partidário, fato concreto com data e local definidos.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria Municipal de Esporte de Cristal"],
        "lead_materia_longa": "A Copa Prefeito de Cristal volta a movimentar o esporte amador do município neste sábado (20), com três jogos programados para o Complexo Esportivo Danilo Ribeiro Braga.",
        "post_instagram": {
            "caption": "O futebol amador de Cristal está de volta. A Copa Prefeito de Cristal retoma a disputa neste sábado (20) com três jogos no Complexo Danilo Ribeiro Braga, depois do adiamento da rodada anterior. É dia de reunir a família, torcer pela equipe do bairro e prestigiar o esporte local da Costa Doce.",
            "hashtags": ["#Cristal", "#CostaDoce", "#FutebolAmador", "#CopaPrefeito", "#EsporteLocal", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A bola volta a rolar em Cristal.",
            "desenvolvimento_45s": "A Copa Prefeito de Cristal retorna neste sábado com três jogos no Complexo Esportivo Danilo Ribeiro Braga. A rodada acontece após o adiamento das partidas anteriores e promete movimentar o fim de semana esportivo do município. A competição reúne equipes amadoras da cidade e da região, valorizando o futebol de base e a integração das comunidades de Cristal.",
            "fechamento_8s": "Fim de semana de futebol na Costa Doce.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental animado"
        },
        "tag_thumbnail": "Futebol amador em Cristal",
        "briefing_visual": {
            "descricao_pt": "Campo de futebol amador de várzea em cidade pequena do interior do Rio Grande do Sul, gramado e traves, sem rostos identificáveis, luz de fim de tarde",
            "query_en": ["amateur football pitch small town", "grassroots soccer field goal post", "community football match brazil"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos", "uniformes legíveis"],
            "prompt_ia": "Amateur grassroots football field in a small town in southern Brazil, green pitch and goal posts, late afternoon light, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento esportivo concreto, com data e local, em cidade-núcleo (Cristal) — pauta comunitária de fim de semana de alto apelo regional"
    },

    # IDX 4 — Arambaré Nota Técnica arborização/poda (Arambaré, serviço) — PUBLICAR
    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": {
        "titulo_sultv": "Arambaré publica nota técnica com orientações sobre poda de árvores e arborização urbana",
        "chamada_faixa": "Arambaré orienta sobre poda de árvores",
        "subtitulo": "Prefeitura divulga diretrizes para o manejo correto da arborização urbana e o período mais indicado para a poda no município.",
        "lead": "A Prefeitura de Arambaré publicou nesta semana uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município. O documento, divulgado em 18 de junho, busca orientar moradores e responsáveis por imóveis sobre os procedimentos corretos para a conservação das árvores e a segurança da cidade, na região da Costa Doce.",
        "ganchos_3": [
            "Arambaré divulga nota técnica sobre poda de árvores",
            "Inverno é o período mais indicado para a poda",
            "Orientações valem para arborização urbana de toda a cidade"
        ],
        "angulo_editorial": "Serviço público de utilidade imediata em cidade-núcleo (Arambaré) — pauta de meio ambiente urbano e segurança, com fonte institucional (prefeitura). Tom orientativo, sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Arambaré", "Secretaria de Meio Ambiente de Arambaré"],
        "lead_materia_longa": "A Prefeitura de Arambaré publicou nesta semana uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município, divulgada em 18 de junho.",
        "post_instagram": {
            "caption": "Arambaré divulgou uma nota técnica com orientações sobre poda de árvores e manejo da arborização urbana. O inverno é justamente o período mais indicado para podar, quando a árvore entra em dormência. Quem precisa cuidar das árvores do pátio ou da calçada deve seguir as diretrizes da prefeitura para garantir segurança e a saúde das plantas.",
            "hashtags": ["#Arambaré", "#CostaDoce", "#ArborizaçãoUrbana", "#MeioAmbiente", "#Serviço", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Atenção, moradores de Arambaré.",
            "desenvolvimento_45s": "A Prefeitura de Arambaré publicou uma nota técnica com orientações sobre a poda de árvores e o manejo da arborização urbana. O documento orienta moradores e responsáveis por imóveis sobre os procedimentos corretos, lembrando que o inverno é o período mais indicado para a poda, quando as árvores entram em dormência. Seguir as diretrizes garante a segurança da cidade e a saúde da arborização.",
            "fechamento_8s": "Cidade mais segura e arborizada.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Poda de árvores em Arambaré",
        "briefing_visual": {
            "descricao_pt": "Trabalhador podando galhos de uma árvore em rua arborizada de cidade pequena no Sul do Brasil, sem rosto identificável, dia claro",
            "query_en": ["tree pruning urban street worker", "trimming tree branches town", "urban tree maintenance brazil"],
            "evitar": ["rosto identificável", "marcas", "texto", "logos"],
            "prompt_ia": "Worker pruning the branches of a tree on a tree-lined street in a small southern Brazilian town, face not visible, clear daylight, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público concreto e atual (18/06) em cidade-núcleo (Arambaré), fonte institucional — utilidade direta para a audiência"
    },

    # IDX 14 — Südoktoberfest São Lourenço (SLS, cultura/turismo) — PUBLICAR
    "9a0afe0a71110324f476128af3e817babce239d4": {
        "titulo_sultv": "Südoktoberfest abre contagem regressiva em São Lourenço do Sul com lançamento oficial e concurso da corte",
        "chamada_faixa": "Südoktoberfest abre contagem em São Lourenço",
        "subtitulo": "Tradicional festa de cultura germânica inicia os preparativos com lançamento oficial e a escolha da corte que representará o evento.",
        "lead": "A Südoktoberfest entrou na contagem regressiva em São Lourenço do Sul com o lançamento oficial da próxima edição e a abertura do concurso que vai escolher a corte da festa. Um dos principais eventos culturais da Costa Doce, a celebração da tradição germânica começa a mobilizar a cidade e a região na preparação para receber moradores e visitantes.",
        "ganchos_3": [
            "Südoktoberfest inicia contagem regressiva em São Lourenço do Sul",
            "Lançamento oficial marca o começo dos preparativos",
            "Concurso vai escolher a corte que representa a festa"
        ],
        "angulo_editorial": "Cultura e turismo em cidade-núcleo (São Lourenço do Sul) — a Südoktoberfest é patrimônio cultural da Costa Doce e gera impacto econômico no comércio, na hotelaria e no turismo regional. Pauta positiva, comunitária e de forte identidade local.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Comissão organizadora da Südoktoberfest", "Secretaria de Turismo de São Lourenço do Sul"],
        "lead_materia_longa": "A Südoktoberfest entrou na contagem regressiva em São Lourenço do Sul com o lançamento oficial da próxima edição e a abertura do concurso que vai escolher a corte da festa.",
        "post_instagram": {
            "caption": "Começou a contagem regressiva para a Südoktoberfest! São Lourenço do Sul deu largada aos preparativos com o lançamento oficial da festa e o concurso que vai escolher a corte. Uma das maiores celebrações da cultura germânica da Costa Doce promete movimentar a cidade, o comércio e o turismo da região. Bora se preparar?",
            "hashtags": ["#SãoLourençoDoSul", "#Südoktoberfest", "#CostaDoce", "#CulturaGermânica", "#Turismo", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A festa mais alemã da Costa Doce vem aí.",
            "desenvolvimento_45s": "A Südoktoberfest abriu a contagem regressiva em São Lourenço do Sul. Com o lançamento oficial da próxima edição e a abertura do concurso da corte, a cidade começa a se preparar para uma das maiores celebrações da cultura germânica da região. O evento movimenta o comércio, a hotelaria e o turismo, reforçando a identidade e a economia da Costa Doce.",
            "fechamento_8s": "São Lourenço se prepara para a festa.",
            "cta_5s": "Fique por dentro no SulTV.",
            "trilha_sugerida": "instrumental festivo"
        },
        "tag_thumbnail": "Südoktoberfest São Lourenço",
        "briefing_visual": {
            "descricao_pt": "Decoração de festa de cultura germânica com bandeirinhas azuis e brancas e tonéis de chopp em pavilhão, ambiente festivo, sem rostos identificáveis",
            "query_en": ["oktoberfest decoration beer barrels", "german festival bunting blue white", "bavarian festival hall"],
            "evitar": ["rostos identificáveis", "marcas de cerveja legíveis", "texto", "logos"],
            "prompt_ia": "German heritage festival decoration with blue and white bunting and wooden beer barrels in a festive pavilion, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento cultural-turístico de grande identidade em cidade-núcleo (São Lourenço do Sul) — impacto econômico e comunitário; fato concreto (lançamento + concurso da corte)"
    },

    # IDX 16 — Cristal limpeza Av Passo do Mendonça (Cristal, serviço) — PUBLICAR
    "804da2cbe08274dd604274d8db6acc48cc218fed": {
        "tag_principal": "comunidade",
        "titulo_sultv": "Avenida Passo do Mendonça recebe serviços de limpeza e reorganização em Cristal",
        "chamada_faixa": "Cristal finaliza melhorias na Passo do Mendonça",
        "subtitulo": "Ações no canteiro central concluem as melhorias da via após a pavimentação, qualificando um dos principais corredores do município.",
        "lead": "A Avenida Passo do Mendonça, em Cristal, recebe serviços de limpeza e reorganização do canteiro central. As ações fazem parte da etapa de finalização das melhorias realizadas após a pavimentação da via, um dos principais corredores urbanos do município, na região da Costa Doce.",
        "ganchos_3": [
            "Avenida Passo do Mendonça passa por limpeza e reorganização",
            "Ações concluem as melhorias após a pavimentação",
            "Canteiro central recebe atenção em Cristal"
        ],
        "angulo_editorial": "Serviço e infraestrutura urbana em cidade-núcleo (Cristal/Costa Doce) — pauta de utilidade local que mostra a conclusão de obra estruturante; tom institucional, sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria de Obras de Cristal"],
        "lead_materia_longa": "A Avenida Passo do Mendonça, em Cristal, recebe serviços de limpeza e reorganização do canteiro central, em etapa de finalização das melhorias realizadas após a pavimentação da via.",
        "post_instagram": {
            "caption": "A Avenida Passo do Mendonça, em Cristal, está recebendo serviços de limpeza e reorganização do canteiro central. As ações finalizam as melhorias feitas após a pavimentação de um dos principais corredores da cidade. Mais um trecho urbano qualificado para quem circula por Cristal todos os dias.",
            "hashtags": ["#Cristal", "#CostaDoce", "#Infraestrutura", "#Serviço", "#ObrasUrbanas", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal qualifica mais uma avenida.",
            "desenvolvimento_45s": "A Avenida Passo do Mendonça, em Cristal, recebe serviços de limpeza e reorganização do canteiro central. As ações fazem parte da finalização das melhorias realizadas após a pavimentação da via, um dos principais corredores urbanos do município. O trabalho qualifica a circulação e melhora o aspecto de uma das avenidas mais movimentadas da cidade.",
            "fechamento_8s": "Mais uma via requalificada na Costa Doce.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Obras em Cristal",
        "briefing_visual": {
            "descricao_pt": "Avenida urbana recém-pavimentada com canteiro central em cidade pequena do Sul do Brasil, dia claro, sem rostos identificáveis",
            "query_en": ["newly paved urban avenue median", "small town main avenue brazil", "street landscaping median strip"],
            "evitar": ["rostos identificáveis", "placas legíveis", "marcas", "texto", "logos"],
            "prompt_ia": "Newly paved urban avenue with a landscaped central median in a small southern Brazilian town, clear daylight, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço/infraestrutura concreto em cidade-núcleo (Cristal) — conclusão de obra estruturante de utilidade local"
    },

    # IDX 22 — Onda de frio polar na semana (RS/Sul, clima/agro) — PUBLICAR
    "892cde7b48dd63105d731d9788fe695189b3109d": {
        "tag_principal": "clima",
        "titulo_sultv": "Massa de ar polar traz semana de madrugadas de muito frio e risco de geada no Sul",
        "chamada_faixa": "Semana de frio intenso e geada no Sul",
        "subtitulo": "Ingresso de ar de origem polar derruba as temperaturas e eleva o risco de geada, com impacto direto nas lavouras da Costa Doce.",
        "lead": "O Sul do Brasil enfrenta uma semana de madrugadas de muito frio, com temperaturas que não eram registradas desde meados de maio. O ingresso de uma massa de ar de origem polar sobre a região derruba os termômetros e eleva o risco de geada, exigindo atenção redobrada dos produtores rurais da Costa Doce e de todo o Rio Grande do Sul.",
        "ganchos_3": [
            "Massa de ar polar derruba as temperaturas no Sul",
            "Risco de geada exige atenção nas lavouras",
            "Frio mais intenso desde meados de maio"
        ],
        "angulo_editorial": "Clima de serviço com impacto agrícola direto — frio intenso e geada afetam lavouras de inverno e exigem cuidados com plantas, animais e pessoas. Pauta de utilidade para a audiência rural e urbana de todo o RS. Sem atribuição a veículo de comunicação.",
        "fontes_complementares_sugeridas": ["Emater/RS", "Defesa Civil do RS", "Sala de Situação do RS"],
        "lead_materia_longa": "O Sul do Brasil enfrenta uma semana de madrugadas de muito frio, com temperaturas que não eram registradas desde meados de maio, por conta do ingresso de uma massa de ar de origem polar sobre a região.",
        "post_instagram": {
            "caption": "Prepare o agasalho: o Sul entra numa semana de madrugadas de muito frio, com o ingresso de uma massa de ar polar e risco de geada. No campo, a atenção é redobrada — a geada pode atingir lavouras e pastagens. Proteja plantas sensíveis, os animais e também as pessoas mais vulneráveis ao frio.",
            "hashtags": ["#Clima", "#Frio", "#Geada", "#RioGrandeDoSul", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O frio polar chegou com tudo no Sul.",
            "desenvolvimento_45s": "Uma massa de ar de origem polar avança sobre o Sul do Brasil e traz uma semana de madrugadas de muito frio, com temperaturas que não eram registradas desde meados de maio. O risco de geada aumenta e exige atenção redobrada no campo, onde lavouras de inverno e pastagens podem ser atingidas. A orientação é proteger plantas sensíveis, os animais e as pessoas mais vulneráveis ao frio.",
            "fechamento_8s": "Semana de frio intenso na Costa Doce.",
            "cta_5s": "Previsão completa no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Frio e geada no Sul",
        "briefing_visual": {
            "descricao_pt": "Lavoura coberta por geada ao amanhecer no interior do Rio Grande do Sul, capim e folhas com cristais de gelo, luz dourada, sem pessoas",
            "query_en": ["frost covered field sunrise", "frozen grass crop frost morning", "winter frost farmland"],
            "evitar": ["pessoas", "marcas", "texto", "logos"],
            "prompt_ia": "A crop field covered in frost at sunrise in rural southern Brazil, grass and leaves coated with ice crystals, golden morning light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima de serviço com impacto agrícola direto (geada) para toda a audiência do RS — pauta atual e de utilidade; redigida sem citar veículo"
    },

    # ===================== REBAIXAR =====================
    "610aa137e5df4573db449c757f0592d1a66467bd": _skip(
        "REBAIXAR", "Crime em Caxias do Sul (Serra), fora do núcleo de cobertura Sul-RS/Costa Doce; sem âncora regional e tema policial sensível — vira nota interna"),
    "088841c8efb87debf6dec7e24d529afa585011e8": _skip(
        "REBAIXAR", "Conteúdo de tecnologia nacional/agregado sem qualquer âncora regional Sul-RS; cidade atribuída (Tapes) é artefato da fonte"),
    "abeda0f5ae70098c9e77dc3369d81c0a463928f1": _skip(
        "REBAIXAR", "Vagas nacionais de empresa de telecom, sem âncora Sul-RS; geolocalização (Tapes) é erro de mapeamento da fonte"),
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "REBAIXAR", "Inscrições de cursos de abril/2026 — conteúdo defasado (provável prazo encerrado); republicar como serviço atual seria impreciso"),
    "4a19f3b447abaaef75271b2e2dbf1a33ae46591b": _skip(
        "REBAIXAR", "Reunião institucional com pauta vaga ('possíveis ações'), sem fato concreto fechado; baixo valor noticioso para matéria"),
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": _skip(
        "REBAIXAR", "Nota urbana sem descrição substantiva e redundante com a matéria da Av. Passo do Mendonça (mesma cidade no dia); evita sobre-indexar Cristal"),
    "6b4b313181b5fe182604e79854da742800687843": _skip(
        "REBAIXAR", "Conteúdo sobre Teutônia/Bento (Vale do Taquari/Serra), fora do núcleo; descrição mistura várias pautas, alto risco de imprecisão"),
    "0c78bd0cc00e7d0302fc635b3fdbfbd510252753": _skip(
        "REBAIXAR", "Concurso com classificações de 13 de maio — conteúdo defasado; sem novidade para a data de hoje"),
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "REBAIXAR", "Debate político-partidário sensível (plebiscito/privatização de estatais), apenas manifestações sem fato concluído — guardrail de política partidária"),
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR", "Audiência procedural sobre destinação de recursos, com data aparentemente defasada (29); baixo apelo e risco de desatualização"),
    "a6683f9edcfc9c862dd9febe7d25aba45d237a5d": _skip(
        "REBAIXAR", "Pauta internacional (ciclone na Copa do Mundo) sem âncora regional Sul-RS"),
    "b0889a9f85770aca01833915dbfe96c99e135c06": _skip(
        "REBAIXAR", "Previsão referente a quarta-feira (17), já superada; substituída pela matéria da onda de frio da semana"),
    "3b5074e66b1d09eda1f8dc861b2bcf3f9a9fd4a4": _skip(
        "REBAIXAR", "Clima do Centro do Brasil (Centro-Oeste/Sudeste), fora do recorte Sul-RS"),
    "10ecbe665aec1d1df677b64e8269a3a8da82defa": _skip(
        "REBAIXAR", "Minicurso acadêmico de nicho (preservação de acervos) em Santa Maria, baixo apelo de audiência ampla — fica como post se houver espaço"),
    "1ab67688e26543136e7ed7276d644140d4d339f6": _skip(
        "REBAIXAR", "Exposição acadêmica de nicho em Santa Maria, fora do núcleo e de baixo apelo amplo"),
    "00dae8a9584ce334db72038fb9d6be7e693bd2dd": _skip(
        "REBAIXAR", "Obra de gás de longo prazo em Venâncio Aires (Vale do Rio Pardo), fora do núcleo e sem fato imediato"),
    "4bb5156d22f64917a874c5b6008a3f76f58791fd": _skip(
        "REBAIXAR", "Dica agro evergreen (poda/plantio) redundante com a matéria de arborização de Arambaré publicada hoje"),
    "6de3e215b8ca03a1a6d3ef6a7d5d0450bb96682c": _skip(
        "REBAIXAR", "Tema de saúde sensível (casos de meningite) em Bento Gonçalves, fora do núcleo — guardrail de saúde; não publicar"),
    "7df2ecb4f938d2b200dc230b928b75d50a0b1cc3": _skip(
        "REBAIXAR", "Decisão macroeconômica nacional (Selic) sem fato ou recorte específico do Sul-RS"),

    # ===================== BLOQUEAR =====================
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR", "Edital de penalidade procedural (Nº 001/2026, 30/03) — documento administrativo, não é matéria"),
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR", "Edital procedural de abertura de prazo (Nº 002/2026) — documento administrativo, não é matéria"),
    "2ca9c6c05b652779fe1185d698a6d67e649d2e53": _skip(
        "BLOQUEAR", "Título é cabeçalho de seção raspado ('Secretaria... Velejaço solidário') — fragmento sem corpo noticioso"),
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": _skip(
        "BLOQUEAR", "Aviso administrativo genérico (revisão de contracheques) raspado como cabeçalho de seção — não é matéria"),
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR", "Aviso de audiência pública procedural, sem detalhamento — cabeçalho/edital, não é matéria"),
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR", "Aviso procedural sobre emissão de notas fiscais (05/05) — documento administrativo defasado, não é matéria"),
}


MATERIAS = {

    "2eac2f6cebf64e843cf46c36ea8a00003737d43a": """### Título ###
Copa Prefeito de Cristal retorna neste sábado com três jogos no Complexo Danilo Ribeiro Braga

### Artigo ###
A Copa Prefeito de Cristal volta a movimentar o esporte amador do município neste sábado (20), com três jogos programados para o Complexo Esportivo Danilo Ribeiro Braga. A rodada acontece após o adiamento das partidas previstas anteriormente e recoloca a competição no calendário esportivo de Cristal, na região da Costa Doce. A disputa é uma das mais tradicionais do município e reúne equipes amadoras formadas por moradores de diferentes bairros e comunidades, transformando os fins de semana em encontros que vão muito além do futebol. Para as famílias, a Copa Prefeito é também uma oportunidade de lazer e de convivência, com torcedores acompanhando os jogos e prestigiando os times da própria vizinhança. O futebol amador cumpre um papel importante na vida social do interior gaúcho. Além de incentivar a prática esportiva e os hábitos saudáveis entre jovens e adultos, competições como essa fortalecem o sentimento de pertencimento e movimentam o comércio local nos dias de partida. O retorno da rodada após o adiamento é aguardado pelos atletas, que voltam a campo em busca de pontos e de boas posições na tabela. Com três jogos em sequência, o Complexo Danilo Ribeiro Braga deve receber bom público neste sábado, em mais um capítulo de uma competição que se consolidou como referência do esporte comunitário em Cristal. A expectativa é de jogos disputados e de uma tarde de integração entre as comunidades do município.

### Legenda sugerida ###
Copa Prefeito de Cristal retoma a disputa neste sábado (20) com três jogos no Complexo Danilo Ribeiro Braga.

### Palavras-chave ###
Copa Prefeito de Cristal, Cristal, futebol amador, esporte, Complexo Danilo Ribeiro Braga, Costa Doce, esporte comunitário
""",

    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": """### Título ###
Arambaré publica nota técnica com orientações sobre poda de árvores e arborização urbana

### Artigo ###
A Prefeitura de Arambaré publicou, em 18 de junho, uma nota técnica com orientações sobre o manejo da arborização urbana e a poda de árvores no município. O documento reúne diretrizes voltadas a moradores e responsáveis por imóveis, com o objetivo de orientar os procedimentos corretos para a conservação das árvores e a segurança da cidade, na região da Costa Doce. A iniciativa chega em um momento oportuno do calendário. O inverno é justamente o período mais indicado para a poda, época em que muitas espécies entram em dormência e respondem melhor à intervenção, com menor estresse para a planta e cicatrização mais eficiente dos cortes. Realizar a poda de forma técnica e na estação adequada reduz riscos, prolonga a vida das árvores e evita problemas como a queda de galhos sobre a fiação elétrica, calçadas e veículos. A arborização urbana traz benefícios diretos à qualidade de vida: oferece sombra, ameniza as temperaturas, contribui para a drenagem e valoriza o ambiente das ruas. Por isso, o manejo correto é uma responsabilidade compartilhada entre o poder público e a população. A orientação da prefeitura é que qualquer intervenção siga as diretrizes técnicas divulgadas e, quando necessário, conte com o acompanhamento dos setores responsáveis do município. A medida reforça o compromisso de Arambaré com a conservação do patrimônio verde da cidade e com a segurança de quem circula pelas vias urbanas, especialmente no período de maior incidência de ventos e instabilidades do inverno.

### Legenda sugerida ###
Prefeitura de Arambaré divulga nota técnica com orientações para a poda de árvores e o manejo da arborização urbana.

### Palavras-chave ###
Arambaré, poda de árvores, arborização urbana, nota técnica, meio ambiente, Costa Doce, manejo de árvores
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

    "804da2cbe08274dd604274d8db6acc48cc218fed": """### Título ###
Avenida Passo do Mendonça recebe serviços de limpeza e reorganização em Cristal

### Artigo ###
A Avenida Passo do Mendonça, em Cristal, recebe serviços de limpeza e reorganização do canteiro central. As ações fazem parte da etapa de finalização das melhorias realizadas após a pavimentação da via, um dos principais corredores urbanos do município, na região da Costa Doce. O trabalho dá os retoques finais em uma obra estruturante que muda a rotina de quem circula diariamente pela avenida. A pavimentação de vias urbanas é uma das demandas mais sentidas pela população das cidades do interior, por melhorar as condições de tráfego, reduzir a poeira e a lama em dias de chuva e qualificar o acesso a bairros, serviços e ao comércio. A conclusão dos serviços no canteiro central complementa esse esforço, devolvendo à comunidade uma via mais organizada, limpa e segura. A reorganização do canteiro também tem efeito sobre o aspecto visual e a valorização do entorno. Espaços bem cuidados no centro das avenidas contribuem para a paisagem urbana, ajudam na drenagem e podem abrigar arborização e ajardinamento que tornam o ambiente mais agradável. Para os moradores e comerciantes que vivem e trabalham ao longo da Passo do Mendonça, a finalização das melhorias representa um ganho concreto no dia a dia. A requalificação de corredores urbanos integra o conjunto de ações de infraestrutura que vêm transformando a mobilidade em Cristal, reforçando o cuidado com os espaços públicos e com a qualidade de vida na cidade.

### Legenda sugerida ###
Canteiro central da Avenida Passo do Mendonça recebe limpeza e reorganização, finalizando as melhorias da via em Cristal.

### Palavras-chave ###
Cristal, Avenida Passo do Mendonça, pavimentação, infraestrutura urbana, obras, Costa Doce, mobilidade
""",

    "892cde7b48dd63105d731d9788fe695189b3109d": """### Título ###
Massa de ar polar traz semana de madrugadas de muito frio e risco de geada no Sul

### Artigo ###
O Sul do Brasil enfrenta uma semana de madrugadas de muito frio, com temperaturas que não eram registradas desde meados de maio. O ingresso de uma massa de ar de origem polar sobre a região derruba os termômetros e eleva o risco de geada, exigindo atenção redobrada dos produtores rurais da Costa Doce e de todo o Rio Grande do Sul. O fenômeno é típico do auge do inverno, quando o ar frio e seco de origem polar avança sobre o continente e provoca quedas acentuadas de temperatura, especialmente nas madrugadas e no início das manhãs. Para o campo, a geada é o ponto de maior preocupação. O congelamento da água nas plantas pode danificar lavouras de inverno, hortaliças e pastagens, comprometendo a produção. A orientação aos produtores é acompanhar as previsões atualizadas e adotar medidas de proteção possíveis, como o manejo adequado de culturas sensíveis e o cuidado com os animais, que também sofrem com a queda brusca das temperaturas. O frio intenso exige cuidados igualmente na cidade. Pessoas idosas, crianças e quem tem doenças respiratórias estão entre os mais vulneráveis, e a recomendação é manter o agasalho adequado, evitar a exposição prolongada ao frio e redobrar a atenção com o aquecimento dentro de casa, sempre observando a segurança no uso de aquecedores. A previsão indica que as baixas temperaturas devem se manter ao longo dos próximos dias, mantendo o alerta para geadas em diversas regiões do estado. O acompanhamento diário das condições do tempo é a melhor forma de se preparar para os impactos dessa onda de frio no Sul.

### Legenda sugerida ###
Massa de ar polar traz frio intenso e risco de geada ao Sul nesta semana; atenção redobrada no campo e na cidade.

### Palavras-chave ###
frio, geada, massa de ar polar, Rio Grande do Sul, clima, inverno, lavouras, Costa Doce, previsão do tempo
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
            angul["titulo_sultv"] = item.get("titulo", "")[:100]
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
        if p["decisao_final"] == "PUBLICAR" and p["formato_sugerido"] == "materia_longa":
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
