#!/usr/bin/env python3
"""
angular_2026-06-16.py — angulação editorial + redação (cowork-faz-tudo).
Lê state/aprovadas_2026-06-16.json, gera
state/pauta_2026-06-16.json + state/materias_2026-06-16/<id_hash>.md.

Regra 12 (INEGOCIÁVEL): nenhum texto menciona veículos/portais/rádios/jornais.
Material coletado é insumo, reformatado 100% no tom Redação SulTV.
"""
from __future__ import annotations
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-16"


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

    # 0. Camaquã — Toucas de Amor / drive-thru solidário — PUBLICAR
    "e738cdccde091ef45bf5cc654df473b4c6f7cdaa": {
        "titulo_sultv": "Projeto Toucas de Amor faz drive-thru em Camaquã para arrecadar lã e aquecer o inverno",
        "chamada_faixa": "Drive-thru solidário arrecada lã em Camaquã",
        "subtitulo": "Ação solidária recolhe novelos de lã para a confecção de toucas e peças de inverno destinadas a famílias em vulnerabilidade na Costa Doce.",
        "lead": "O projeto Toucas de Amor promove em Camaquã um drive-thru solidário para arrecadar novelos de lã que serão transformados em toucas, agasalhos e peças de inverno entregues a famílias em situação de vulnerabilidade social. A ação chega no auge do frio gaúcho, quando cresce a procura por roupas quentes nos serviços de assistência da região.",
        "ganchos_3": [
            "Drive-thru solidário arrecada lã em Camaquã",
            "Novelos viram toucas e agasalhos para famílias",
            "Mobilização no auge do frio na Costa Doce"
        ],
        "angulo_editorial": "Solidariedade comunitária em cidade-núcleo (Camaquã) no pico do inverno, com formato participativo (drive-thru). Pauta positiva, de mobilização social — perfil ideal SulTV.",
        "fontes_complementares_sugeridas": ["Sesc Camaquã", "Secretaria de Assistência Social de Camaquã", "voluntárias do projeto Toucas de Amor"],
        "lead_materia_longa": "O projeto Toucas de Amor promove em Camaquã um drive-thru solidário para arrecadar novelos de lã destinados à confecção de toucas e peças de inverno para famílias em situação de vulnerabilidade.",
        "post_instagram": {
            "caption": "Em Camaquã, novelo de lã vira abraço quente. O projeto Toucas de Amor montou um drive-thru solidário para arrecadar lã que será transformada em toucas e agasalhos para famílias que mais sentem o frio da Costa Doce. Quem tem lã sobrando em casa pode contribuir — cada novelo pode aquecer uma noite inteira.",
            "hashtags": ["#Camaquã", "#ToucasDeAmor", "#Solidariedade", "#Inverno", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Lã que vira abraço em Camaquã.",
            "desenvolvimento_45s": "O projeto Toucas de Amor montou um drive-thru solidário em Camaquã para arrecadar novelos de lã. A lã recolhida é transformada por voluntárias em toucas, cachecóis e agasalhos entregues a famílias em situação de vulnerabilidade. A ação chega no auge do frio, quando os serviços de assistência social registram maior procura por roupas quentes. Quem quiser ajudar pode levar lã em bom estado aos pontos de coleta indicados.",
            "fechamento_8s": "Um novelo, uma noite mais quente.",
            "cta_5s": "Saiba como ajudar no SulTV.",
            "trilha_sugerida": "instrumental acolhedor"
        },
        "tag_thumbnail": "Solidariedade",
        "briefing_visual": {
            "descricao_pt": "Novelos de lã coloridos empilhados em cesto, mãos tricotando touca de inverno, ambiente acolhedor, sem rostos identificáveis",
            "query_en": ["colorful wool yarn balls basket", "hands knitting winter hat wool", "knitting charity donation"],
            "evitar": ["rostos identificáveis", "marcas", "texto legível", "logos"],
            "prompt_ia": "Colorful balls of wool yarn in a wicker basket with hands knitting a winter hat, warm cozy indoor light, no identifiable faces, no brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Ação solidária concreta em cidade-núcleo (Camaquã) no auge do inverno — alto apelo comunitário positivo"
    },

    # 1. Camaquã — Vélez Camaquã avança na Copa LNF — PUBLICAR
    "16b98841146cb52c394cc118609af6783949631f": {
        "titulo_sultv": "Vélez Camaquã vence fora de casa e avança às quartas de final da Copa LNF",
        "chamada_faixa": "Vélez Camaquã avança na Copa LNF",
        "subtitulo": "Equipe de futsal superou o adversário catarinense na prorrogação e garantiu vaga entre os oito melhores da competição nacional.",
        "lead": "O Vélez Camaquã garantiu vaga nas quartas de final da Copa LNF de futsal ao vencer o Lages-SC fora de casa, em partida decidida na prorrogação. O resultado coloca o representante da Costa Doce entre os oito melhores da principal competição nacional da modalidade e celebra o esporte regional do Sul do estado.",
        "ganchos_3": [
            "Vélez Camaquã vence na prorrogação e avança",
            "Time da Costa Doce entre os oito melhores da Copa LNF",
            "Vitória fora de casa em jogo eletrizante"
        ],
        "angulo_editorial": "Esporte regional de cidade-núcleo (Camaquã) com conquista concreta em competição nacional — orgulho local, pauta positiva e mobilizadora da torcida da Costa Doce.",
        "fontes_complementares_sugeridas": ["Vélez Camaquã", "Liga Nacional de Futsal (LNF)", "comissão técnica do clube"],
        "lead_materia_longa": "O Vélez Camaquã garantiu vaga nas quartas de final da Copa LNF de futsal ao vencer o Lages-SC fora de casa, em partida decidida na prorrogação.",
        "post_instagram": {
            "caption": "Camaquã está nas quartas! O Vélez superou o Lages-SC fora de casa, na prorrogação, e avançou na Copa LNF de futsal. A Costa Doce agora torce por um time entre os oito melhores do país. Que venham as quartas de final — bola no chão e coração na quadra!",
            "hashtags": ["#VélezCamaquã", "#Futsal", "#CopaLNF", "#Camaquã", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Camaquã nas quartas de final!",
            "desenvolvimento_45s": "O Vélez Camaquã venceu o Lages-SC fora de casa, em jogo decidido na prorrogação, e garantiu vaga nas quartas de final da Copa LNF de futsal. A conquista coloca a Costa Doce entre os oito melhores da principal competição nacional da modalidade. Para o futsal do interior gaúcho, chegar a essa fase é resultado de trabalho de base, dedicação dos atletas e apoio da torcida.",
            "fechamento_8s": "A Costa Doce nas quartas da LNF.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental energético esportivo"
        },
        "tag_thumbnail": "Esporte",
        "briefing_visual": {
            "descricao_pt": "Quadra de futsal com bola e marcas da quadra em destaque, atmosfera de jogo, sem rostos identificáveis nem escudos de marcas",
            "query_en": ["indoor futsal court ball", "futsal game action indoor", "indoor soccer court"],
            "evitar": ["rostos identificáveis", "escudos de clubes reais", "marcas", "texto"],
            "prompt_ia": "Dynamic wide shot of an indoor futsal court with a ball in motion under bright sports lighting, no identifiable faces, no team logos, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Conquista esportiva concreta de time de cidade-núcleo (Camaquã) em competição nacional — orgulho regional"
    },

    # 2. Tapes — Coleta de eletrônicos remarcada p/ 17/jun — PUBLICAR
    "cbddd137f8e3aa362714a81824d39e177bc7e66b": {
        "titulo_sultv": "Tapes remarca coleta gratuita de lixo eletrônico para esta quarta-feira",
        "chamada_faixa": "Tapes faz coleta de eletrônicos quarta-feira",
        "subtitulo": "Ação do programa MP Sustentare recolhe gratuitamente resíduos eletrônicos no dia 17 de junho, das 9h às 16h, na Praça Rui Barbosa.",
        "lead": "A coleta gratuita de resíduos eletrônicos em Tapes foi remarcada para esta quarta-feira, 17 de junho, das 9h às 16h, na Praça Rui Barbosa. A ação do programa MP Sustentare, conduzida pela Secretaria Municipal de Meio Ambiente, havia sido adiada por causa das instabilidades climáticas e dá destino ambientalmente correto a equipamentos sem uso.",
        "ganchos_3": [
            "Coleta de eletrônicos em Tapes nesta quarta",
            "Descarte gratuito das 9h às 16h na Praça Rui Barbosa",
            "Programa MP Sustentare dá destino correto ao lixo eletrônico"
        ],
        "angulo_editorial": "Serviço público concreto, com data, horário e local definidos, em cidade-núcleo (Tapes). Utilidade direta ao morador e viés ambiental — pauta de serviço clássica SulTV.",
        "fontes_complementares_sugeridas": ["Prefeitura de Tapes", "Secretaria Municipal de Meio Ambiente de Tapes", "programa MP Sustentare"],
        "lead_materia_longa": "A coleta gratuita de resíduos eletrônicos em Tapes foi remarcada para esta quarta-feira, 17 de junho, das 9h às 16h, na Praça Rui Barbosa, em ação do programa MP Sustentare.",
        "post_instagram": {
            "caption": "Aquele celular velho na gaveta tem destino certo em Tapes. A coleta gratuita de lixo eletrônico foi remarcada para esta quarta-feira, 17 de junho, das 9h às 16h, na Praça Rui Barbosa. É só levar os equipamentos sem uso e dar a eles o descarte ambientalmente correto. Anota a data!",
            "hashtags": ["#Tapes", "#LixoEletrônico", "#MeioAmbiente", "#Sustentabilidade", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tapes recolhe seu lixo eletrônico.",
            "desenvolvimento_45s": "A coleta gratuita de resíduos eletrônicos em Tapes foi remarcada para esta quarta-feira, 17 de junho, das 9h às 16h, na Praça Rui Barbosa. A ação do programa MP Sustentare havia sido adiada por causa do tempo instável. Celulares, computadores, cabos e pequenos eletrodomésticos sem uso podem ser entregues no local e recebem destinação ambientalmente correta, evitando que materiais contaminantes acabem no lixo comum.",
            "fechamento_8s": "Descarte certo, ambiente protegido.",
            "cta_5s": "Veja os detalhes no SulTV.",
            "trilha_sugerida": "instrumental leve e informativo"
        },
        "tag_thumbnail": "Meio Ambiente",
        "briefing_visual": {
            "descricao_pt": "Equipamentos eletrônicos antigos (celulares, cabos, placas) reunidos para reciclagem, vista de cima, sem pessoas",
            "query_en": ["electronic waste recycling pile", "old electronics e-waste collection", "discarded gadgets recycling"],
            "evitar": ["rostos identificáveis", "marcas legíveis", "texto", "logos"],
            "prompt_ia": "Top-down view of assorted old electronic devices, cables and circuit boards arranged for recycling collection, neutral background, no people, no readable brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público com data/hora/local concretos em cidade-núcleo (Tapes), utilidade direta e viés ambiental"
    },

    # 6. Cristal — reunião de segurança pública prefeito + BPM — PUBLICAR
    "f6344ccfbeebeb426982842a44881910459162a4": {
        "titulo_sultv": "Cristal e Brigada Militar alinham reforço da segurança pública no município",
        "chamada_faixa": "Cristal reforça a segurança com a Brigada",
        "subtitulo": "Encontro na Prefeitura reuniu o prefeito, o comando do 30º Batalhão e a Câmara para tratar de ações de policiamento no município.",
        "lead": "A Prefeitura de Cristal recebeu o comando do 30º Batalhão de Polícia Militar para uma reunião voltada ao fortalecimento da segurança pública no município. O encontro, realizado na tarde de segunda-feira, reuniu o prefeito Marcelo Krolow, o comandante do batalhão, oficiais da corporação e o presidente da Câmara de Vereadores, e tratou de medidas para ampliar o policiamento e a sensação de segurança na cidade-núcleo da Costa Doce.",
        "ganchos_3": [
            "Cristal e Brigada Militar alinham segurança pública",
            "Reunião na Prefeitura com comando do 30º BPM",
            "Foco em ampliar o policiamento no município"
        ],
        "angulo_editorial": "Segurança pública é tema de alto interesse em cidade-núcleo (Cristal), com fontes institucionais nomeadas (prefeito e comando da Brigada). Pauta concreta e factual, sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "30º Batalhão de Polícia Militar", "Câmara de Vereadores de Cristal"],
        "lead_materia_longa": "A Prefeitura de Cristal recebeu o comando do 30º Batalhão de Polícia Militar para uma reunião voltada ao fortalecimento da segurança pública no município, com a participação do prefeito Marcelo Krolow e do presidente da Câmara de Vereadores.",
        "post_instagram": {
            "caption": "Segurança se constrói com diálogo. Em Cristal, a Prefeitura reuniu o comando do 30º Batalhão de Polícia Militar para alinhar ações de policiamento e fortalecer a segurança pública no município. Participaram o prefeito, oficiais da Brigada e a Câmara de Vereadores. A pauta agora é transformar conversa em mais presença nas ruas.",
            "hashtags": ["#Cristal", "#SegurançaPública", "#BrigadaMilitar", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal mira mais segurança.",
            "desenvolvimento_45s": "A Prefeitura de Cristal reuniu o comando do 30º Batalhão de Polícia Militar para tratar do fortalecimento da segurança pública no município. O encontro contou com o prefeito, oficiais da Brigada Militar e o presidente da Câmara de Vereadores. A pauta envolveu ações de policiamento e estratégias para ampliar a presença das forças de segurança e a sensação de proteção da população nas ruas da cidade.",
            "fechamento_8s": "Diálogo por uma cidade mais segura.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio e institucional"
        },
        "tag_thumbnail": "Segurança",
        "briefing_visual": {
            "descricao_pt": "Viatura da Brigada Militar do RS em rua de cidade pequena do interior gaúcho, luz do dia, sem rostos identificáveis",
            "query_en": ["police patrol car small town brazil", "police vehicle street daytime", "brazilian municipal street patrol"],
            "evitar": ["rostos identificáveis", "placas legíveis", "marcas", "texto"],
            "prompt_ia": "A police patrol car on a quiet small-town street in southern Brazil during daytime, no identifiable faces, no readable plates, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Segurança pública em cidade-núcleo (Cristal), fato concreto e recente com fontes institucionais nomeadas"
    },

    # 11. Cristal — 1ª Rústica Hilmo Saalfeld, 250 atletas — PUBLICAR
    "c45667a6ac425207c9b91dcda2b8a016ba403bd4": {
        "titulo_sultv": "1ª Rústica Hilmo Saalfeld reúne 250 atletas e movimenta Cristal no fim de semana",
        "chamada_faixa": "Rústica reúne 250 atletas em Cristal",
        "subtitulo": "Prova de corrida e caminhada levou competidores de várias cidades da região às ruas de Cristal, mesmo com o frio do fim de semana.",
        "lead": "A 1ª Rústica Hilmo Saalfeld reuniu cerca de 250 atletas nas ruas de Cristal na manhã de domingo, em prova de corrida e caminhada que atraiu competidores e visitantes de diversas cidades da região. Mesmo com o frio, o evento esportivo movimentou a cidade-núcleo da Costa Doce e reforçou o calendário de atividades comunitárias do município.",
        "ganchos_3": [
            "250 atletas na 1ª Rústica Hilmo Saalfeld em Cristal",
            "Prova reuniu corredores de várias cidades da região",
            "Esporte e superação mesmo com o frio"
        ],
        "angulo_editorial": "Evento esportivo comunitário em cidade-núcleo (Cristal) com número expressivo de participantes e alcance regional. Pauta positiva, de mobilização e movimentação econômica local.",
        "fontes_complementares_sugeridas": ["organização da Rústica Hilmo Saalfeld", "Prefeitura de Cristal", "Super Atacado Cristal"],
        "lead_materia_longa": "A 1ª Rústica Hilmo Saalfeld reuniu cerca de 250 atletas nas ruas de Cristal na manhã de domingo, em prova de corrida e caminhada que atraiu competidores de diversas cidades da região.",
        "post_instagram": {
            "caption": "Cristal acordou cedo e correu junto! A 1ª Rústica Hilmo Saalfeld reuniu cerca de 250 atletas, mesmo com o frio, em uma manhã de corrida, caminhada e superação. Vieram competidores de várias cidades da região, movimentando o município e mostrando que esporte também aquece. Bora pra segunda edição?",
            "hashtags": ["#Cristal", "#Corrida", "#RústicaHilmoSaalfeld", "#Esporte", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "250 atletas correndo em Cristal.",
            "desenvolvimento_45s": "A 1ª Rústica Hilmo Saalfeld reuniu cerca de 250 atletas nas ruas de Cristal na manhã de domingo. A prova de corrida e caminhada atraiu competidores e visitantes de diversas cidades da região, mesmo com as baixas temperaturas. Além do espírito esportivo, eventos como esse movimentam o comércio e o turismo local, colocam a cidade no mapa das provas de rua do interior e incentivam a prática de atividade física na comunidade.",
            "fechamento_8s": "Esporte que move Cristal.",
            "cta_5s": "Veja como foi no SulTV.",
            "trilha_sugerida": "instrumental energético"
        },
        "tag_thumbnail": "Esporte",
        "briefing_visual": {
            "descricao_pt": "Grupo de corredores de rua largando em prova de corrida em manhã fria, vista ampla, sem rostos identificáveis em primeiro plano",
            "query_en": ["street running race start crowd", "outdoor road race runners", "fun run marathon start"],
            "evitar": ["rostos identificáveis em close", "números de peito legíveis com nomes", "marcas", "texto"],
            "prompt_ia": "Wide shot of a crowd of street runners starting a road race on a cold morning, motion and energy, no identifiable faces in close-up, no brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento esportivo comunitário em cidade-núcleo (Cristal) com 250 participantes e alcance regional"
    },

    # 7. São Lourenço do Sul — Campanha do Agasalho — PUBLICAR
    "48f6bcb4bf3b07bf4195d88755b6d0949a7d6437": {
        "titulo_sultv": "São Lourenço do Sul aquece o inverno com pontos de coleta da Campanha do Agasalho",
        "chamada_faixa": "São Lourenço aquece o inverno com doações",
        "subtitulo": "Empresas, entidades e instituições do município montam pontos de coleta para receber roupas de inverno, cobertores e calçados.",
        "lead": "As Campanhas do Agasalho ganham força em São Lourenço do Sul com a queda das temperaturas. Empresas, entidades e instituições do município mantêm diferentes pontos de coleta para receber roupas de inverno, cobertores e calçados em bom estado, mobilizando a solidariedade dos lourencianos no auge do frio na Costa Doce.",
        "ganchos_3": [
            "Campanha do Agasalho mobiliza São Lourenço do Sul",
            "Pontos de coleta espalhados pelo município",
            "Doações de roupas, cobertores e calçados no inverno"
        ],
        "angulo_editorial": "Solidariedade e serviço em cidade-núcleo (São Lourenço do Sul), com participação distribuída entre empresas e entidades. Pauta positiva e mobilizadora, alinhada à estação.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Secretaria de Assistência Social", "entidades participantes da campanha"],
        "lead_materia_longa": "As Campanhas do Agasalho ganham força em São Lourenço do Sul com a queda das temperaturas, com empresas, entidades e instituições mantendo pontos de coleta para roupas de inverno, cobertores e calçados.",
        "post_instagram": {
            "caption": "Quando o frio aperta, a solidariedade aquece São Lourenço do Sul. As Campanhas do Agasalho estão ativas em empresas, entidades e instituições do município, com vários pontos de coleta recebendo roupas de inverno, cobertores e calçados em bom estado. Sua doação pode ser o agasalho que falta na noite gelada de alguém.",
            "hashtags": ["#SãoLourençoDoSul", "#CampanhaDoAgasalho", "#Solidariedade", "#Inverno", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "São Lourenço aquece quem precisa.",
            "desenvolvimento_45s": "Com a chegada do frio, as Campanhas do Agasalho ganham força em São Lourenço do Sul. Empresas, entidades e instituições do município montaram diferentes pontos de coleta que recebem roupas de inverno, cobertores e calçados em bom estado. As doações são destinadas a famílias e pessoas em situação de vulnerabilidade, justamente no período mais rigoroso do inverno gaúcho. Pequenos gestos somados fazem a diferença.",
            "fechamento_8s": "Doe e aqueça o inverno de alguém.",
            "cta_5s": "Veja os pontos no SulTV.",
            "trilha_sugerida": "instrumental acolhedor"
        },
        "tag_thumbnail": "Solidariedade",
        "briefing_visual": {
            "descricao_pt": "Roupas de inverno e cobertores dobrados em caixa de doação, ambiente interno acolhedor, sem rostos identificáveis",
            "query_en": ["winter coats donation box", "folded blankets clothing donation", "warm clothing charity collection"],
            "evitar": ["rostos identificáveis", "marcas", "texto legível", "logos"],
            "prompt_ia": "Folded winter coats and blankets arranged in a clothing donation box indoors, warm soft light, no identifiable faces, no brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta solidária concreta em cidade-núcleo (São Lourenço do Sul) no auge do inverno"
    },

    # 16. Barra do Ribeiro / Pelotas — CMPC projeto Natureza R$ 27 bi — PUBLICAR
    "0d5b5546c2181520d61a65fde680dafeb3d853e6": {
        "titulo_sultv": "Projeto da CMPC em Barra do Ribeiro mobiliza apoio e promete R$ 27 bilhões em investimentos",
        "chamada_faixa": "Projeto da CMPC promete R$ 27 bilhões",
        "subtitulo": "Manifestação em Porto Alegre defendeu o avanço do empreendimento florestal-industrial e a regularidade do licenciamento ambiental.",
        "lead": "O projeto Natureza, da CMPC, previsto para Barra do Ribeiro, voltou ao centro do debate econômico gaúcho com a previsão de R$ 27 bilhões em investimentos. Uma manifestação realizada em frente ao Palácio Piratini, em Porto Alegre, defendeu o avanço do empreendimento, enquanto o Governo do Estado reforçou a regularidade do processo de licenciamento ambiental do projeto.",
        "ganchos_3": [
            "Projeto da CMPC prevê R$ 27 bilhões em Barra do Ribeiro",
            "Manifestação em Porto Alegre defende o empreendimento",
            "Governo reforça regularidade do licenciamento ambiental"
        ],
        "angulo_editorial": "Investimento de grande porte com impacto direto na Costa Doce (Barra do Ribeiro, cidade-núcleo) — emprego, cadeia florestal e desenvolvimento regional. Tratamento factual e equilibrado sobre o estágio do licenciamento, sem viés.",
        "fontes_complementares_sugeridas": ["CMPC", "Governo do Estado do RS", "Prefeitura de Barra do Ribeiro", "órgãos ambientais estaduais"],
        "lead_materia_longa": "O projeto Natureza, da CMPC, previsto para Barra do Ribeiro, voltou ao centro do debate econômico gaúcho com a previsão de R$ 27 bilhões em investimentos, em meio a manifestação de apoio em Porto Alegre e à defesa, pelo Governo do Estado, da regularidade do licenciamento ambiental.",
        "post_instagram": {
            "caption": "Barra do Ribeiro pode receber um dos maiores investimentos da história recente do RS. O projeto Natureza, da CMPC, prevê R$ 27 bilhões e voltou ao centro do debate, com manifestação de apoio em Porto Alegre e a garantia do Governo do Estado sobre a regularidade do licenciamento ambiental. Um tema que mexe com emprego, economia e meio ambiente na Costa Doce.",
            "hashtags": ["#BarraDoRibeiro", "#CMPC", "#Investimento", "#Economia", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "R$ 27 bilhões de olho na Costa Doce.",
            "desenvolvimento_45s": "O projeto Natureza, da CMPC, previsto para Barra do Ribeiro, voltou ao centro do debate econômico gaúcho com a previsão de R$ 27 bilhões em investimentos. Uma manifestação em frente ao Palácio Piratini defendeu o avanço do empreendimento florestal-industrial, enquanto o Governo do Estado reforçou a regularidade do processo de licenciamento ambiental. O projeto é acompanhado de perto por mexer com emprego, cadeia florestal e desenvolvimento da região.",
            "fechamento_8s": "Um investimento que divide opiniões.",
            "cta_5s": "Entenda no SulTV.",
            "trilha_sugerida": "instrumental institucional"
        },
        "tag_thumbnail": "Economia",
        "briefing_visual": {
            "descricao_pt": "Plantio de eucalipto em fileiras no interior do Rio Grande do Sul, vista ampla, sem pessoas nem marcas",
            "query_en": ["eucalyptus plantation rows aerial", "managed forest plantation brazil", "pulp wood forest landscape"],
            "evitar": ["rostos identificáveis", "logos de empresas", "texto", "marcas"],
            "prompt_ia": "Aerial wide shot of rows of eucalyptus plantation in southern Brazil under soft daylight, no people, no company logos, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Investimento de grande porte com impacto direto em cidade-núcleo da Costa Doce (Barra do Ribeiro)"
    },

    # 18. Guaíba — Operação Inverno Defesa Civil — PUBLICAR (override p/ materia_longa)
    "3b348ce4a42ffbd249fd98d4c5ed494b381ac4dc": {
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Guaíba ativa Operação Inverno para proteger pessoas em situação de vulnerabilidade no frio",
        "chamada_faixa": "Guaíba ativa a Operação Inverno",
        "subtitulo": "Defesa Civil intensifica monitoramento e ações de acolhimento quando a sensação térmica fica abaixo de 7°C.",
        "lead": "A Defesa Civil de Guaíba ativou a Operação Inverno para reforçar a proteção de pessoas em situação de vulnerabilidade durante os dias mais frios. O protocolo entra em ação quando a sensação térmica fica abaixo de 7°C e prevê monitoramento intensificado, abordagens sociais e acolhimento, garantindo resposta rápida às baixas temperaturas.",
        "ganchos_3": [
            "Guaíba ativa a Operação Inverno",
            "Protocolo entra em ação com sensação térmica abaixo de 7°C",
            "Monitoramento e acolhimento de pessoas vulneráveis"
        ],
        "angulo_editorial": "Serviço público de proteção social no auge do frio, com critério técnico claro (7°C). Utilidade direta e apelo humano — pauta de serviço SulTV.",
        "fontes_complementares_sugeridas": ["Defesa Civil de Guaíba", "Secretaria de Assistência Social de Guaíba", "Prefeitura de Guaíba"],
        "lead_materia_longa": "A Defesa Civil de Guaíba ativou a Operação Inverno para reforçar a proteção de pessoas em situação de vulnerabilidade durante os dias mais frios, com o protocolo entrando em ação quando a sensação térmica fica abaixo de 7°C.",
        "post_instagram": {
            "caption": "O frio chegou forte e Guaíba se mobilizou. A Defesa Civil ativou a Operação Inverno para proteger quem está em situação de vulnerabilidade. Quando a sensação térmica cai abaixo de 7°C, o protocolo entra em ação com monitoramento, abordagens sociais e acolhimento. Frio severo pede atenção redobrada com quem mais precisa.",
            "hashtags": ["#Guaíba", "#OperaçãoInverno", "#DefesaCivil", "#Frio", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Guaíba liga o alerta do frio.",
            "desenvolvimento_45s": "A Defesa Civil de Guaíba ativou a Operação Inverno para proteger pessoas em situação de vulnerabilidade durante os dias mais frios. O protocolo é acionado quando a sensação térmica fica abaixo de 7°C e prevê monitoramento intensificado, abordagens sociais, avaliação das necessidades e acolhimento. A iniciativa busca dar resposta rápida ao frio severo, que oferece risco especialmente a quem está em situação de rua.",
            "fechamento_8s": "Frio forte pede cuidado redobrado.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental sóbrio e solidário"
        },
        "tag_thumbnail": "Defesa Civil",
        "briefing_visual": {
            "descricao_pt": "Cobertores e itens de acolhimento prontos para distribuição em noite fria de cidade gaúcha, sem rostos identificáveis",
            "query_en": ["blankets winter shelter night", "cold weather relief blankets", "homeless winter aid supplies"],
            "evitar": ["rostos identificáveis", "marcas", "texto legível", "logos"],
            "prompt_ia": "Stacked warm blankets and relief supplies ready for distribution on a cold winter night in a southern Brazilian town, no identifiable faces, no brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público de proteção social no auge do frio, com critério técnico concreto"
    },

    # 26. Canguçu — RS Qualificação Recomeçar — PUBLICAR
    "09d5760b87be1b342adb054e10e520bcc3f8e415": {
        "titulo_sultv": "Programa RS Qualificação Recomeçar inicia turmas de cursos gratuitos em Canguçu",
        "chamada_faixa": "Cursos gratuitos começam em Canguçu",
        "subtitulo": "Aula inaugural marcou o início da capacitação profissional voltada à inserção no mercado de trabalho no município.",
        "lead": "O programa RS Qualificação Recomeçar teve sua aula inaugural em Canguçu, marcando o início de cursos gratuitos de capacitação profissional no município. A iniciativa busca ampliar as oportunidades de inserção no mercado de trabalho e qualificar a mão de obra local, atendendo moradores que buscam recolocação ou primeiro emprego na região.",
        "ganchos_3": [
            "Cursos gratuitos do RS Recomeçar começam em Canguçu",
            "Aula inaugural marca início da capacitação",
            "Foco em inserção no mercado de trabalho"
        ],
        "angulo_editorial": "Qualificação profissional e geração de oportunidades em cidade da região Sul (Canguçu). Pauta de serviço e desenvolvimento, com impacto social direto.",
        "fontes_complementares_sugeridas": ["Prefeitura de Canguçu", "programa RS Qualificação Recomeçar", "Secretaria estadual de Trabalho"],
        "lead_materia_longa": "O programa RS Qualificação Recomeçar teve sua aula inaugural em Canguçu, marcando o início de cursos gratuitos de capacitação profissional voltados à inserção no mercado de trabalho.",
        "post_instagram": {
            "caption": "Recomeçar também é se qualificar. Em Canguçu, o programa RS Qualificação Recomeçar começou com aula inaugural e abre turmas de cursos gratuitos de capacitação profissional. A meta é ampliar as oportunidades de quem busca o primeiro emprego ou uma recolocação. Conhecimento que abre portas na região.",
            "hashtags": ["#Canguçu", "#Qualificação", "#RSRecomeçar", "#Trabalho", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Curso gratuito que abre portas.",
            "desenvolvimento_45s": "O programa RS Qualificação Recomeçar teve sua aula inaugural em Canguçu, dando início a cursos gratuitos de capacitação profissional no município. A iniciativa busca ampliar as oportunidades de inserção no mercado de trabalho, qualificando moradores que procuram recolocação ou o primeiro emprego. Em municípios do interior, a qualificação local evita deslocamentos e aproxima a formação das necessidades das empresas da região.",
            "fechamento_8s": "Qualificação perto de casa.",
            "cta_5s": "Saiba como participar no SulTV.",
            "trilha_sugerida": "instrumental otimista"
        },
        "tag_thumbnail": "Educação",
        "briefing_visual": {
            "descricao_pt": "Sala de aula de curso profissionalizante com pessoas de costas assistindo aula, ambiente simples, sem rostos identificáveis",
            "query_en": ["vocational training classroom students", "adult education class back view", "professional course classroom"],
            "evitar": ["rostos identificáveis", "marcas", "texto legível", "logos"],
            "prompt_ia": "A vocational training classroom with adult students seen from behind attending a class, simple bright room, no identifiable faces, no brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Qualificação profissional gratuita em cidade da região Sul (Canguçu), fato concreto e impacto social"
    },

    # 27. Encruzilhada do Sul — Nota Fiscal Premiada — PUBLICAR
    "93ead45af45f7460451b53107befb4234889579b": {
        "titulo_sultv": "Nota Fiscal Premiada volta a Encruzilhada do Sul com moto e prêmios em dinheiro",
        "chamada_faixa": "Nota Fiscal Premiada sorteia moto e PIX",
        "subtitulo": "Campanha incentiva o pedido de nota fiscal e a valorização do comércio local, com prêmios que incluem uma moto zero e PIX em dinheiro.",
        "lead": "A campanha Nota Fiscal Premiada está de volta em Encruzilhada do Sul, incentivando os consumidores a pedir nota fiscal e valorizar o comércio local. Ao trocar as notas por números da sorte, o participante concorre a prêmios que incluem uma moto zero quilômetro e PIX em dinheiro, fortalecendo a economia do município.",
        "ganchos_3": [
            "Nota Fiscal Premiada volta a Encruzilhada do Sul",
            "Prêmios incluem moto zero e PIX em dinheiro",
            "Campanha valoriza o comércio local"
        ],
        "angulo_editorial": "Economia e cidadania fiscal em cidade da região (Encruzilhada do Sul), com mecânica concreta de prêmios e incentivo ao comércio local. Pauta de serviço positiva.",
        "fontes_complementares_sugeridas": ["Prefeitura de Encruzilhada do Sul", "Secretaria de Finanças do município", "associação comercial local"],
        "lead_materia_longa": "A campanha Nota Fiscal Premiada está de volta em Encruzilhada do Sul, incentivando os consumidores a pedir nota fiscal e concorrer a prêmios que incluem uma moto zero quilômetro e PIX em dinheiro.",
        "post_instagram": {
            "caption": "Pedir nota fiscal em Encruzilhada do Sul agora pode valer uma moto zero. A campanha Nota Fiscal Premiada voltou: você troca suas notas por números da sorte e concorre a prêmios em dinheiro via PIX e a uma moto 0km. Além de concorrer, você valoriza o comércio local e fortalece a economia da cidade. Guarde suas notas!",
            "hashtags": ["#EncruzilhadaDoSul", "#NotaFiscalPremiada", "#ComércioLocal", "#Economia", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Sua nota fiscal pode virar prêmio.",
            "desenvolvimento_45s": "A campanha Nota Fiscal Premiada está de volta em Encruzilhada do Sul. Ao pedir nota fiscal e trocá-la por números da sorte, o consumidor concorre a prêmios que incluem uma moto zero quilômetro e PIX em dinheiro. Mais do que a chance de ganhar, a campanha estimula a cidadania fiscal e a valorização do comércio local, ajudando a movimentar a economia e a aumentar a arrecadação que retorna em serviços para o município.",
            "fechamento_8s": "Peça nota e concorra.",
            "cta_5s": "Veja as regras no SulTV.",
            "trilha_sugerida": "instrumental animado"
        },
        "tag_thumbnail": "Economia",
        "briefing_visual": {
            "descricao_pt": "Cupons fiscais e notas de compra em cima de balcão de comércio, com moto desfocada ao fundo, sem rostos nem marcas",
            "query_en": ["paper receipts retail counter", "shopping receipts stack", "small shop counter receipts"],
            "evitar": ["rostos identificáveis", "marcas legíveis", "texto legível em destaque", "logos"],
            "prompt_ia": "Close-up of paper purchase receipts on a small retail shop counter with a motorcycle softly blurred in the background, no identifiable faces, no readable brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Campanha de economia e cidadania fiscal em cidade da região (Encruzilhada do Sul), mecânica concreta"
    },

    # ---------- REBAIXAR ----------
    "d6732430183e4e9db23bc78b61ac65796d1ef238": _skip(
        "REBAIXAR", "Boletim meteorológico de serviço; cidade já contemplada e tema do frio coberto por outras pautas do dia"),
    "0c78bd0cc00e7d0302fc635b3fdbfbd510252753": _skip(
        "REBAIXAR", "Pauta procedural de concurso com classificações de maio — desatualizada"),
    "26af69553f9eace59585246f1178879d0a9caa90": _skip(
        "REBAIXAR", "Conteúdo de série promocional gastronômica; cidade (Guaíba) já contemplada"),
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "REBAIXAR", "Pauta procedural legislativa estadual, sem âncora local forte na Costa Doce"),
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR", "Pauta técnica de destinação de recursos, baixo apelo regional direto"),
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": _skip(
        "REBAIXAR", "Pauta estadual/nacional de crédito rural sem âncora em cidade do Sul-RS"),
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": _skip(
        "REBAIXAR", "Apreensão genérica no RS sem âncora específica no núcleo Sul/Costa Doce"),
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": _skip(
        "REBAIXAR", "Fiscalização genérica no RS sem âncora específica no núcleo Sul/Costa Doce"),
    "e6fff2725635f8da6e880c351f39276a44142f44": _skip(
        "REBAIXAR", "Evento em Esteio (Região Metropolitana), fora do núcleo Sul/Costa Doce"),
    "fce3119cfcb33ce7ea0f4b2f61a2bcadbc3f4fa5": _skip(
        "REBAIXAR", "Post de conscientização institucional; cidade (Canguçu) já contemplada"),
    "4150eaa6c6753d222a0d600d584bf002af8ce204": _skip(
        "REBAIXAR", "Duplicata da Nota Fiscal Premiada (Encruzilhada do Sul) já aprovada"),
    "350fa1ef49d2d04812deb7be9018576613611ef1": _skip(
        "REBAIXAR", "Mostra cultural em Santa Maria (Frederico Westphalen), fora do núcleo Sul"),
    "60ac623e84a23b9292d2f8aad738ebf8fe5758b7": _skip(
        "REBAIXAR", "Lançamento de plataforma em Santa Maria, fora do núcleo Sul; baixo apelo direto"),
    "6588128a57e7ccb1a7613032c4adb75f6ca1a3e7": _skip(
        "REBAIXAR", "Post institucional leve (convite), sem fato concreto noticiável"),
    "ab5409ae86fa444ce503622f930b80d86920eb6c": _skip(
        "REBAIXAR", "Aviso de serviço pontual (mutirão de castração); vira nota interna"),
    "ba58a0f5b4fe990048d7481629694cc38a7f1d42": _skip(
        "REBAIXAR", "Pauta do Corede Vale do Rio Pardo, fora do núcleo Sul/Costa Doce"),
    "1caef4ac7fcfd18e6a8fa86d1257b4668c686f11": _skip(
        "REBAIXAR", "Vestibular em Santa Cruz do Sul, fora do núcleo Sul/Costa Doce"),
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "REBAIXAR", "Aviso de audiência pública sem conteúdo desenvolvido"),

    # ---------- BLOQUEAR (explícitos) ----------
    "991dbaa9fff99a1bd6a044a98be22f9815900ff0": _skip(
        "BLOQUEAR", "Guardrail: tragédia com vítima identificada (homicídio) + região distante (Serra)"),
    "2d870a9873d6a9e2393594ca9695f2fb86cd7083": _skip(
        "BLOQUEAR", "Esporte nacional (Copa do Mundo) sem âncora regional Sul-RS"),
    "60d4de7cf2643dde3ae3c9aa55263622c2a7f7f9": _skip(
        "BLOQUEAR", "Título é cabeçalho de boletim/jornal informativo, não matéria única"),
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "BLOQUEAR", "Conteúdo desatualizado (abril/2026) e corpo vazio"),
    "7328151d0f689699ca147e00ec7ffb87008ee51e": _skip(
        "BLOQUEAR", "Conteúdo desatualizado (janeiro/2026) e corpo vazio"),
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR", "Edital procedural de penalidade, sem corpo noticiável"),
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR", "Edital procedural de abertura de prazo, sem corpo noticiável"),
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR", "Aviso procedural (emissão de notas fiscais), sem corpo noticiável"),
    "2ca9c6c05b652779fe1185d698a6d67e649d2e53": _skip(
        "BLOQUEAR", "Título é cabeçalho de seção de secretaria, não matéria"),
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": _skip(
        "BLOQUEAR", "Título é cabeçalho de seção de secretaria, não matéria"),
}


MATERIAS = {
    # 0 — Camaquã — Toucas de Amor
    "e738cdccde091ef45bf5cc654df473b4c6f7cdaa": """### Título ###
Projeto Toucas de Amor faz drive-thru em Camaquã para arrecadar lã e aquecer o inverno

### Artigo ###
O projeto Toucas de Amor promove em Camaquã um drive-thru solidário para arrecadar novelos de lã que serão transformados em toucas, cachecóis e agasalhos destinados a famílias em situação de vulnerabilidade social na região da Costa Doce. A ação chega em um momento decisivo do calendário: o frio mais rigoroso do ano costuma se concentrar entre junho e agosto, quando cresce a procura por roupas quentes nos serviços de assistência social do município. O formato de drive-thru facilita a participação: quem deseja colaborar pode passar pelo ponto de coleta e entregar a doação sem sair do carro, em uma dinâmica prática que aproxima a comunidade da causa. A lã recolhida é repassada a voluntárias que tricotam, ponto a ponto, peças capazes de proteger do frio quem mais precisa. Mais do que arrecadar material, a iniciativa mobiliza a solidariedade local e transforma um gesto simples em conforto real. Cada novelo doado vira uma touca, um par de luvas ou um cachecol que pode significar noites mais protegidas para crianças, idosos e famílias inteiras. Campanhas como essa também reforçam o papel da rede de proteção social, que acompanha as famílias ao longo do ano e busca caminhos para que possam superar a vulnerabilidade. Para colaborar, a orientação é procurar o ponto de coleta indicado e conferir os horários de recebimento. Quem tem lã guardada em casa, sem uso, tem agora um destino certo para ela: aquecer o inverno de quem vive os dias mais frios em situação de risco. Pequenos gestos, quando somados, mudam a temperatura de uma comunidade inteira.

### Legenda sugerida ###
Projeto Toucas de Amor monta drive-thru em Camaquã para arrecadar lã e confeccionar agasalhos no inverno.

### Palavras-chave ###
Camaquã, Toucas de Amor, doação, lã, inverno, solidariedade, Costa Doce, assistência social
""",

    # 1 — Camaquã — Vélez Camaquã
    "16b98841146cb52c394cc118609af6783949631f": """### Título ###
Vélez Camaquã vence fora de casa e avança às quartas de final da Copa LNF

### Artigo ###
O Vélez Camaquã garantiu vaga nas quartas de final da Copa LNF de futsal ao vencer o Lages-SC fora de casa, em partida decidida apenas na prorrogação. O resultado coloca o representante da Costa Doce entre os oito melhores times da principal competição nacional da modalidade e renova o entusiasmo da torcida no Sul do estado. O confronto foi disputado do início ao fim, com as duas equipes buscando o resultado e a definição saindo somente no tempo extra, o que valoriza ainda mais a conquista de uma vitória longe de casa, diante da torcida adversária. Para o futsal do interior gaúcho, alcançar essa fase é fruto de um trabalho que vai muito além da quadra: envolve formação de base, dedicação diária dos atletas, comissão técnica preparada e o apoio de patrocinadores e da comunidade. Cada avanço em uma competição nacional projeta o nome da cidade, incentiva crianças e jovens a praticarem o esporte e movimenta a economia local em torno dos jogos. O futsal é uma das modalidades mais populares do Rio Grande do Sul, com forte tradição em municípios do interior, e ver uma equipe da Costa Doce entre as melhores do país reforça esse vínculo entre o esporte e a identidade regional. Agora, a expectativa se volta às quartas de final, etapa em que a equipe encontrará adversários ainda mais qualificados. O desafio cresce, mas a campanha construída até aqui mostra que o Vélez Camaquã tem condições de sonhar alto. A torcida promete acompanhar de perto cada passo dessa caminhada.

### Legenda sugerida ###
Vélez Camaquã supera o Lages-SC na prorrogação e garante vaga nas quartas de final da Copa LNF de futsal.

### Palavras-chave ###
Vélez Camaquã, futsal, Copa LNF, Camaquã, esporte, Costa Doce, quartas de final, interior gaúcho
""",

    # 2 — Tapes — Coleta de eletrônicos
    "cbddd137f8e3aa362714a81824d39e177bc7e66b": """### Título ###
Tapes remarca coleta gratuita de lixo eletrônico para esta quarta-feira

### Artigo ###
A coleta gratuita de resíduos eletrônicos em Tapes foi remarcada para esta quarta-feira, 17 de junho, das 9h às 16h, na Praça Rui Barbosa. A ação faz parte do programa MP Sustentare, conduzido pela Secretaria Municipal de Meio Ambiente, e havia sido adiada em razão das instabilidades climáticas registradas na região. Durante o período, moradores poderão levar ao local equipamentos eletrônicos sem uso para descarte ambientalmente correto. Celulares, computadores, monitores, cabos, carregadores e pequenos eletrodomésticos estão entre os itens que costumam ser recebidos nesse tipo de mutirão. O objetivo é evitar que esse material, que contém componentes potencialmente contaminantes, acabe no lixo comum ou em terrenos baldios, onde pode causar danos ao solo, à água e à saúde pública. O lixo eletrônico é um dos resíduos que mais cresce no mundo, impulsionado pela rápida troca de aparelhos. Quando descartado de forma adequada, boa parte dos componentes pode ser reciclada e reaproveitada, reduzindo a extração de novos recursos naturais e o impacto ambiental. Ações como essa também cumprem um papel educativo, ao mostrar à população que existe um caminho seguro e gratuito para se desfazer de equipamentos antigos. Para os moradores de Tapes, o recado é simples: vale aproveitar a data para revisar gavetas e armários, separar aquilo que não funciona mais e levar ao ponto de coleta. Além de organizar a casa, o gesto contribui diretamente para a preservação do meio ambiente na Costa Doce. A orientação da administração municipal é comparecer dentro do horário previsto e, em caso de dúvidas sobre quais itens são aceitos, buscar informação nos canais oficiais da prefeitura.

### Legenda sugerida ###
Coleta gratuita de lixo eletrônico em Tapes acontece nesta quarta (17), das 9h às 16h, na Praça Rui Barbosa.

### Palavras-chave ###
Tapes, lixo eletrônico, coleta, MP Sustentare, meio ambiente, reciclagem, Costa Doce, descarte
""",

    # 6 — Cristal — segurança pública
    "f6344ccfbeebeb426982842a44881910459162a4": """### Título ###
Cristal e Brigada Militar alinham reforço da segurança pública no município

### Artigo ###
A Prefeitura de Cristal recebeu o comando do 30º Batalhão de Polícia Militar para uma reunião voltada ao fortalecimento da segurança pública no município. O encontro, realizado na tarde de segunda-feira, reuniu o prefeito Marcelo Krolow, o comandante do batalhão, oficiais da corporação e o presidente da Câmara de Vereadores, em uma articulação entre o poder público municipal e as forças de segurança. O objetivo do encontro foi discutir estratégias de policiamento e medidas para ampliar a presença ostensiva e a sensação de segurança da população. Reuniões desse tipo costumam tratar de pontos como a distribuição do efetivo, o atendimento a demandas específicas de bairros e localidades do interior, ações preventivas e a integração entre prefeitura, Câmara e Brigada Militar. Em municípios menores, a proximidade entre gestores e comando da segurança é um fator importante: permite identificar com mais rapidez as áreas que precisam de atenção e construir respostas conjuntas. A segurança pública é uma das principais preocupações da população em qualquer cidade, e o diálogo institucional é o primeiro passo para transformar demandas em ações concretas nas ruas. A presença do Legislativo no encontro reforça o caráter compartilhado da pauta, que tende a envolver também o debate sobre recursos e apoio estrutural ao trabalho policial. Para os moradores de Cristal, o resultado esperado desse tipo de articulação é prático: mais policiamento, respostas mais ágeis e um ambiente de maior tranquilidade no dia a dia. A continuidade das tratativas e o desdobramento das medidas discutidas devem ser acompanhados ao longo das próximas semanas, conforme as ações forem implementadas no município.

### Legenda sugerida ###
Prefeitura de Cristal e comando do 30º Batalhão da Brigada Militar alinham ações para reforçar a segurança pública.

### Palavras-chave ###
Cristal, segurança pública, Brigada Militar, 30º Batalhão, policiamento, Costa Doce, prefeitura, Câmara
""",

    # 11 — Cristal — Rústica Hilmo Saalfeld
    "c45667a6ac425207c9b91dcda2b8a016ba403bd4": """### Título ###
1ª Rústica Hilmo Saalfeld reúne 250 atletas e movimenta Cristal no fim de semana

### Artigo ###
A 1ª Rústica Hilmo Saalfeld reuniu cerca de 250 atletas nas ruas de Cristal na manhã de domingo, em uma prova de corrida e caminhada que atraiu competidores e visitantes de diversas cidades da região. Mesmo com o frio característico do inverno gaúcho, o evento movimentou a cidade e marcou a estreia de uma competição que nasce com a proposta de se firmar no calendário esportivo local. Com concentração e largada em ponto central do município, a prova reuniu corredores experientes, praticantes iniciantes e caminhantes, em um clima de confraternização e superação. Esse perfil variado é uma das marcas das corridas de rua, que conseguem unir o esporte de alto desempenho ao incentivo à atividade física para todas as idades. Eventos como a Rústica têm impacto que vai além das pistas. A chegada de atletas de outras cidades movimenta o comércio, os serviços e a hospedagem, gerando renda para o município no fim de semana. Ao mesmo tempo, projeta o nome de Cristal no circuito regional de provas de rua e fortalece a identidade da comunidade em torno do esporte. A realização de uma primeira edição bem-sucedida costuma abrir caminho para que o evento se repita e cresça nos anos seguintes, com mais participantes e estrutura ampliada. Para a população local, a prova também funciona como estímulo à adoção de hábitos mais saudáveis e ao uso dos espaços públicos para a prática esportiva. O saldo positivo da estreia anima organizadores e atletas, que já projetam uma segunda edição. Enquanto isso, fica o registro de uma manhã em que Cristal acordou cedo, enfrentou o frio e correu junto.

### Legenda sugerida ###
Primeira edição da Rústica Hilmo Saalfeld reúne cerca de 250 atletas e movimenta Cristal mesmo com o frio.

### Palavras-chave ###
Cristal, Rústica Hilmo Saalfeld, corrida de rua, esporte, atletas, Costa Doce, caminhada, evento
""",

    # 7 — São Lourenço do Sul — Campanha do Agasalho
    "48f6bcb4bf3b07bf4195d88755b6d0949a7d6437": """### Título ###
São Lourenço do Sul aquece o inverno com pontos de coleta da Campanha do Agasalho

### Artigo ###
As Campanhas do Agasalho ganham força em São Lourenço do Sul à medida que as temperaturas caem e o inverno se aprofunda na Costa Doce. Empresas, entidades e instituições do município mantêm diferentes pontos de coleta para receber roupas de inverno, cobertores e calçados em bom estado, mobilizando a solidariedade dos lourencianos justamente no período mais frio do ano. A descentralização das doações é um ponto forte dessa edição: em vez de um único local, vários espaços espalhados pela cidade funcionam como pontos de recebimento, o que facilita a participação da comunidade. Cada morador pode contribuir no ponto mais próximo de sua casa ou de seu trabalho, com peças que não usa mais, mas que ainda têm vida útil e podem proteger alguém do frio. Os itens arrecadados são destinados a famílias e pessoas em situação de vulnerabilidade social, para quem o inverno representa um desafio adicional. Cobertores, casacos, calçados fechados e roupas infantis estão entre os itens de maior necessidade nesta época. A mobilização também reforça o trabalho contínuo da rede de proteção social, que acompanha as famílias ao longo do ano. A campanha do agasalho é uma tradição em muitos municípios gaúchos e tem um valor que vai além do material doado: fortalece o senso de comunidade e mostra como a solidariedade pode se organizar de forma simples e eficaz. Em São Lourenço do Sul, o convite está feito a moradores, empresas e instituições que queiram somar esforços. Quem puder colaborar pode procurar um dos pontos de coleta espalhados pelo município. Em noites de frio intenso, um agasalho doado pode significar muito mais do que conforto: pode significar proteção.

### Legenda sugerida ###
Campanhas do Agasalho mobilizam São Lourenço do Sul com pontos de coleta de roupas, cobertores e calçados.

### Palavras-chave ###
São Lourenço do Sul, Campanha do Agasalho, doação, inverno, solidariedade, Costa Doce, assistência social
""",

    # 16 — Barra do Ribeiro — CMPC
    "0d5b5546c2181520d61a65fde680dafeb3d853e6": """### Título ###
Projeto da CMPC em Barra do Ribeiro mobiliza apoio e promete R$ 27 bilhões em investimentos

### Artigo ###
O projeto Natureza, da CMPC, previsto para Barra do Ribeiro, voltou ao centro do debate econômico gaúcho com a previsão de R$ 27 bilhões em investimentos. Uma manifestação realizada em frente ao Palácio Piratini, em Porto Alegre, defendeu o avanço do empreendimento florestal-industrial, enquanto o Governo do Estado reforçou a regularidade do processo de licenciamento ambiental do projeto. Empreendimentos dessa magnitude estão entre os maiores já anunciados para o Rio Grande do Sul e despertam atenção por seu potencial de impacto na economia regional. A construção e a operação de uma planta industrial desse porte costumam gerar milhares de empregos diretos e indiretos, movimentar a cadeia florestal, demandar serviços e fornecedores locais e ampliar a arrecadação dos municípios envolvidos. Para uma cidade como Barra do Ribeiro, na região da Costa Doce, a perspectiva de receber um investimento dessa escala representa uma possível transformação no perfil econômico e na geração de oportunidades. Ao mesmo tempo, projetos de grande porte mobilizam debates sobre licenciamento, sustentabilidade e impactos ambientais, etapas que integram o processo de aprovação. A manifestação de apoio e o posicionamento do Governo do Estado sobre a regularidade do licenciamento fazem parte desse percurso, em que diferentes setores expressam suas posições. O acompanhamento técnico dos órgãos ambientais é o que define as condições para que um empreendimento avance, conciliando desenvolvimento econômico e proteção ambiental. O tema deve seguir em evidência nas próximas semanas, à medida que as etapas do projeto avançam. Para a população da região, o interesse é direto: empregos, renda e desenvolvimento de um lado, e a garantia de que o crescimento ocorra com responsabilidade ambiental de outro. O equilíbrio entre essas dimensões será determinante para o futuro do projeto e da região.

### Legenda sugerida ###
Projeto Natureza, da CMPC, prevê R$ 27 bilhões em Barra do Ribeiro e mobiliza debate sobre economia e licenciamento.

### Palavras-chave ###
Barra do Ribeiro, CMPC, projeto Natureza, investimento, economia, licenciamento ambiental, Costa Doce, emprego
""",

    # 18 — Guaíba — Operação Inverno
    "3b348ce4a42ffbd249fd98d4c5ed494b381ac4dc": """### Título ###
Guaíba ativa Operação Inverno para proteger pessoas em situação de vulnerabilidade no frio

### Artigo ###
A Defesa Civil de Guaíba ativou a Operação Inverno para reforçar a proteção de pessoas em situação de vulnerabilidade durante os dias mais frios. O protocolo entra em ação quando a sensação térmica fica abaixo de 7°C e prevê monitoramento intensificado, abordagens sociais, avaliação das necessidades e acolhimento, garantindo uma resposta rápida diante das baixas temperaturas. Com a chegada das massas de ar frio típicas do auge do inverno gaúcho, o risco para quem está exposto ao tempo aumenta de forma significativa. Pessoas em situação de rua, idosos e indivíduos sem acesso a abrigo adequado estão entre os mais afetados, e o frio severo pode representar risco à saúde e até à vida. Por isso, protocolos como a Operação Inverno funcionam como uma rede de segurança, acionada justamente nos momentos mais críticos. As abordagens sociais são uma das principais ferramentas dessa operação. Equipes percorrem a cidade para identificar pessoas em situação de risco, oferecer acolhimento, encaminhar para locais aquecidos e disponibilizar itens como cobertores e agasalhos. O critério técnico da sensação térmica abaixo de 7°C permite que a ativação seja objetiva e ágil, sem depender apenas da percepção do frio. A iniciativa também depende da colaboração da comunidade. Moradores que identificarem pessoas em situação de vulnerabilidade expostas ao frio podem acionar os canais da Defesa Civil e da assistência social do município, ajudando a direcionar o atendimento. A Operação Inverno reforça o papel do poder público na proteção dos mais vulneráveis e mostra que o enfrentamento ao frio extremo exige planejamento, estrutura e solidariedade. Em noites de temperaturas próximas de zero, a diferença entre o risco e a proteção pode estar em um acolhimento a tempo.

### Legenda sugerida ###
Defesa Civil de Guaíba ativa a Operação Inverno, acionada quando a sensação térmica fica abaixo de 7°C.

### Palavras-chave ###
Guaíba, Operação Inverno, Defesa Civil, frio, vulnerabilidade, acolhimento, inverno, assistência social
""",

    # 26 — Canguçu — RS Qualificação Recomeçar
    "09d5760b87be1b342adb054e10e520bcc3f8e415": """### Título ###
Programa RS Qualificação Recomeçar inicia turmas de cursos gratuitos em Canguçu

### Artigo ###
O programa RS Qualificação Recomeçar teve sua aula inaugural em Canguçu, marcando o início de uma série de cursos gratuitos de capacitação profissional no município. A iniciativa busca ampliar as oportunidades de inserção no mercado de trabalho, qualificando moradores que procuram recolocação profissional ou o primeiro emprego. A aula inaugural é o ponto de partida de uma formação voltada a aproximar a qualificação das necessidades reais do mercado. Programas como esse costumam oferecer cursos em áreas com demanda por mão de obra, permitindo que os participantes desenvolvam habilidades específicas e ampliem suas chances de conseguir uma vaga. Para municípios do interior, a oferta de qualificação local tem um valor especial. Evita que moradores precisem se deslocar a centros maiores para estudar, reduz custos e aproxima a formação das oportunidades existentes na própria região. Além disso, fortalece a economia local, ao preparar trabalhadores para atender empresas e empreendimentos do município e do entorno. A qualificação profissional é reconhecida como um dos caminhos mais eficazes para a geração de renda e a redução das desigualdades. Ao investir na capacitação da população, o poder público contribui para que mais pessoas tenham acesso a melhores condições de trabalho e de vida. Em um cenário de transformações no mundo do trabalho, manter-se atualizado e adquirir novas competências se tornou ainda mais importante. Para os moradores de Canguçu interessados, o recado é acompanhar os canais oficiais da prefeitura e do programa para conhecer os cursos disponíveis, os requisitos e as formas de inscrição. A oportunidade de se qualificar gratuitamente, perto de casa, é um convite para quem busca recomeçar e construir novas perspectivas profissionais.

### Legenda sugerida ###
RS Qualificação Recomeçar começa em Canguçu com aula inaugural e cursos gratuitos de capacitação profissional.

### Palavras-chave ###
Canguçu, RS Qualificação Recomeçar, qualificação profissional, cursos gratuitos, trabalho, emprego, capacitação
""",

    # 27 — Encruzilhada do Sul — Nota Fiscal Premiada
    "93ead45af45f7460451b53107befb4234889579b": """### Título ###
Nota Fiscal Premiada volta a Encruzilhada do Sul com moto e prêmios em dinheiro

### Artigo ###
A campanha Nota Fiscal Premiada está de volta em Encruzilhada do Sul, incentivando os consumidores a pedir nota fiscal nas compras e a valorizar o comércio local. Ao trocar as notas por números da sorte, o participante concorre a prêmios que incluem uma moto zero quilômetro e PIX em dinheiro, em uma mecânica que une a chance de ganhar à promoção da cidadania fiscal. O funcionamento da campanha é simples: a cada compra com nota fiscal, o consumidor acumula cupons ou números que valem como chances nos sorteios. Quanto mais notas, maiores as possibilidades de ser contemplado. Além da moto zero, a premiação prevê valores em dinheiro transferidos via PIX, ampliando o alcance e o interesse da população. Mais do que uma promoção, campanhas de nota fiscal premiada têm um objetivo concreto: estimular que as transações comerciais sejam registradas, fortalecendo a arrecadação do município. Esses recursos retornam à comunidade na forma de serviços públicos, investimentos e melhorias. Ao pedir a nota, o consumidor contribui para um ciclo que beneficia toda a cidade. O comércio local também é diretamente favorecido. A valorização das compras dentro do município ajuda a manter empregos, fortalecer empreendedores e movimentar a economia de Encruzilhada do Sul. Em tempos de concorrência com grandes centros e com as compras pela internet, incentivar o consumo no comércio da própria cidade é uma estratégia importante para o desenvolvimento local. Para participar, a orientação aos moradores é guardar as notas fiscais das compras e ficar atento às regras e aos prazos da campanha, divulgados pelos canais oficiais. Uma atitude simples, no dia a dia, pode render bons prêmios e, ao mesmo tempo, ajudar a construir uma cidade melhor.

### Legenda sugerida ###
Campanha Nota Fiscal Premiada retorna a Encruzilhada do Sul com moto zero e prêmios em dinheiro via PIX.

### Palavras-chave ###
Encruzilhada do Sul, Nota Fiscal Premiada, comércio local, economia, cidadania fiscal, prêmios, arrecadação
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
            angul = _skip("BLOQUEAR", "Sem angulação configurada — descartado pelo guardrail")
            angul["titulo_sultv"] = item.get("titulo", "")[:100]
        else:
            angul = PAUTA_ANGULADA[h]

        if angul["decisao_final"] == "PUBLICAR" and pub_count >= 10:
            angul = {**angul, "decisao_final": "REBAIXAR", "decisao_motivo": "Quota diária de 10 PUBLICAR esgotada"}
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

    materias_dir.mkdir(exist_ok=True)
    nwrite = 0
    for p in pauta:
        if p["decisao_final"] == "PUBLICAR" and p.get("formato_sugerido") == "materia_longa":
            corpo = MATERIAS.get(p["id_hash"])
            if corpo:
                (materias_dir / f"{p['id_hash']}.md").write_text(corpo, encoding="utf-8")
                nwrite += 1
            else:
                print(f"[angular] AVISO: {p['id_hash']} é PUBLICAR/materia_longa mas SEM texto em MATERIAS")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
