#!/usr/bin/env python3
"""Angulação editorial do dia 2026-05-17, gerada por Claude na sessão Cowork."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-05-17"
APROVADAS = ROOT / "state" / f"aprovadas_{HOJE}.json"
PAUTA_OUT = ROOT / "state" / f"pauta_{HOJE}.json"
MAT_DIR = ROOT / "state" / f"materias_{HOJE}"
MAT_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------ ANGULAÇÃO
# Decisões editoriais por id_hash dos itens aprovados de hoje.
PAUTA_ANGULADA = {
    # --- 1. Arambaré abre cursos gratuitos (cidade-núcleo) ---
    "e370728cabf9868c99ea7f3a5323d444ac76d0dd": {
        "titulo_sultv": "Arambaré abre inscrições para cursos gratuitos de qualificação profissional",
        "subtitulo": "Programa municipal oferta capacitação para moradores da Costa Doce com vagas limitadas.",
        "lead": "A Prefeitura de Arambaré abriu inscrições para cursos gratuitos de qualificação profissional, voltados a moradores da cidade. As vagas são limitadas e atendem diferentes áreas técnicas, com foco em ampliar oportunidades de trabalho e renda na Costa Doce.",
        "ganchos_3": [
            "Vagas gratuitas com inscrição aberta na Prefeitura",
            "Qualificação ajustada ao mercado regional da Costa Doce",
            "Política pública de geração de renda em cidade litorânea"
        ],
        "angulo_editorial": "Serviço público concreto em cidade-núcleo da SulTV (Arambaré). Pauta de utilidade direta para a audiência, alinhada à estratégia de cobertura regional.",
        "fontes_complementares_sugeridas": ["Sine Municipal", "FGTAS", "Sebrae RS"],
        "lead_materia_longa": "A Prefeitura de Arambaré, na Costa Doce gaúcha, abriu inscrições para um conjunto de cursos gratuitos de qualificação profissional voltados aos moradores da cidade. O programa integra a estratégia municipal de geração de renda e ampliação de oportunidades em uma região marcada pela combinação entre economia rural, turismo de praia e pesca artesanal. As vagas são limitadas e contemplam diferentes áreas técnicas, com aulas previstas para iniciar nas próximas semanas. A iniciativa reforça o esforço da gestão municipal em conectar a mão de obra local a setores com demanda crescente no comércio, nos serviços e na cadeia produtiva regional.",
        "post_instagram": {
            "caption": "Arambaré abriu inscrições para cursos gratuitos de qualificação profissional. Vagas limitadas para moradores da Costa Doce.",
            "hashtags": ["#Arambaré", "#CostaDoce", "#SulTV", "#Qualificação", "#TrabalhoRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Arambaré abre cursos gratuitos.",
            "desenvolvimento_45s": "A Prefeitura de Arambaré está com inscrições abertas para cursos gratuitos de qualificação profissional. As vagas são limitadas e contemplam diferentes áreas técnicas, alinhadas às oportunidades de trabalho na Costa Doce. O programa faz parte da política municipal de geração de renda e busca ampliar a empregabilidade dos moradores em setores como comércio, serviços e cadeia produtiva regional.",
            "fechamento_8s": "Vagas limitadas — interessados devem procurar a Prefeitura.",
            "cta_5s": "Cobertura completa no SulTV.",
            "trilha_sugerida": "instrumental otimista"
        },
        "tag_thumbnail": "Vagas gratuitas em Arambaré",
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cidade-núcleo (Arambaré) com fato de serviço público — prioridade editorial"
    },

    # --- 2. Motorock em Lajeado (rebaixar - fora da região) ---
    "8ecf23f919ba6c89fb1bc3b96d576456aa7ef168": {
        "titulo_sultv": "",
        "subtitulo": "",
        "lead": "",
        "ganchos_3": [],
        "angulo_editorial": "Evento em Lajeado — fora da hierarquia geográfica da SulTV (atribuído erroneamente a Pelotas pela fonte). Sem âncora regional Sul-RS.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Pauta de Lajeado (Vale do Taquari) sem âncora Sul-RS — fora do perímetro editorial"
    },

    # --- 3. Cristal workshop Artesão (cidade-núcleo secundária) ---
    "7f82eab384d643864de1fa6898d10d5f0535abc7": {
        "titulo_sultv": "Cristal recebe workshop “Artesão em Foco” nos dias 18 e 19 de maio",
        "subtitulo": "Programação traz oficinas e capacitações voltadas ao artesanato e produtos identitários da Costa Doce.",
        "lead": "Cristal, no Sul do Rio Grande do Sul, sedia nos dias 18 e 19 de maio o workshop “Artesão em Foco”, com oficinas práticas, orientações técnicas e capacitação para artesãos locais. A iniciativa busca fortalecer a produção identitária da região e qualificar profissionais do setor.",
        "ganchos_3": [
            "Workshop com programação prática em dois dias",
            "Foco em produtos identitários da Costa Doce",
            "Capacitação técnica para artesãos do interior"
        ],
        "angulo_editorial": "Evento em Cristal (segunda camada da hierarquia SulTV). Combina capacitação, identidade regional e fomento à microeconomia local.",
        "fontes_complementares_sugeridas": ["Sebrae RS", "Secretaria de Cultura RS"],
        "lead_materia_longa": "Cristal, no Sul do Rio Grande do Sul, recebe nos dias 18 e 19 de maio o workshop “Artesão em Foco”, voltado para a qualificação de artesãos e o desenvolvimento de produtos identitários da região. A programação integra oficinas práticas, orientações técnicas e capacitações pensadas para fortalecer a microeconomia local e dar visibilidade ao trabalho de produtores manuais da Costa Doce. A iniciativa parte da Prefeitura de Cristal em parceria com instituições de apoio ao artesanato e busca conectar a produção local com mercados de turismo e cultura, segmentos em expansão na região. As atividades são abertas a artesãos de toda a região, com vagas distribuídas conforme inscrição prévia.",
        "post_instagram": {
            "caption": "Cristal recebe nos dias 18 e 19 de maio o workshop “Artesão em Foco”, com oficinas e capacitações para fortalecer o artesanato local.",
            "hashtags": ["#Cristal", "#Artesanato", "#CostaDoce", "#SulTV", "#EconomiaCriativa"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal aposta no artesanato.",
            "desenvolvimento_45s": "Nos dias 18 e 19 de maio, Cristal recebe o workshop “Artesão em Foco”, com oficinas práticas, orientações e capacitações para artesãos locais. O evento foca no desenvolvimento de produtos identitários da Costa Doce e busca fortalecer a microeconomia regional. A iniciativa amplia o protagonismo do artesanato como vetor de renda e identidade cultural para o Sul do Rio Grande do Sul.",
            "fechamento_8s": "Programação aberta a artesãos de toda a região.",
            "cta_5s": "Cobertura completa no SulTV.",
            "trilha_sugerida": "violão regional"
        },
        "tag_thumbnail": "Artesanato em foco em Cristal",
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento concreto em cidade da segunda camada (Cristal) — pauta de comunidade legítima"
    },

    # --- 4. Pelotas Campanha do Agasalho (título precisa ser reescrito) ---
    "5b53c846036bb2fb31255b4e16c4bd893985f60e": {
        "titulo_sultv": "Pelotas lança Campanha do Agasalho 2026 com primeiras doações já entregues",
        "subtitulo": "Iniciativa da Assistência Social mobiliza a cidade para arrecadar roupas no inverno gaúcho.",
        "lead": "A Prefeitura de Pelotas lançou nesta semana a Campanha do Agasalho 2026, com as primeiras doações já entregues à Secretaria de Assistência Social. A ação busca mobilizar empresas e cidadãos para arrecadar roupas e cobertores que serão distribuídos a famílias em vulnerabilidade durante o inverno gaúcho.",
        "ganchos_3": [
            "Primeiras doações da edição 2026 já foram entregues",
            "Mobilização em rede com empresas e moradores",
            "Distribuição prioritária para famílias em vulnerabilidade"
        ],
        "angulo_editorial": "Utilidade pública clássica em Pelotas (Costa Doce ampliada). Pauta de mobilização social, oportuna no início do inverno gaúcho.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Assistência Social", "Conselho Municipal dos Direitos da Pessoa Idosa"],
        "lead_materia_longa": "A Prefeitura de Pelotas lançou esta semana a Campanha do Agasalho 2026, com as primeiras doações já entregues à Secretaria Municipal de Assistência Social. A iniciativa busca arrecadar roupas, cobertores e calçados em bom estado para distribuição a famílias em situação de vulnerabilidade durante o inverno gaúcho, período em que a demanda por proteção térmica cresce significativamente na região. A campanha conta com pontos de coleta espalhados por escolas, secretarias municipais e estabelecimentos parceiros, e mobiliza empresas, escolas e moradores em torno de uma rede de solidariedade. O modelo de campanha repete-se há mais de uma década no município e mantém-se como uma das principais ações de articulação entre poder público e sociedade civil no enfrentamento aos efeitos do frio sobre as populações mais expostas.",
        "post_instagram": {
            "caption": "Pelotas começou a Campanha do Agasalho 2026 — primeiras doações já entregues. Quem puder ajudar pode procurar os pontos de coleta da cidade.",
            "hashtags": ["#Pelotas", "#CampanhaDoAgasalho", "#CostaDoce", "#SulTV", "#Solidariedade"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Pelotas lança Agasalho 2026.",
            "desenvolvimento_45s": "A Prefeitura de Pelotas lançou esta semana a Campanha do Agasalho 2026, com as primeiras doações já entregues à Secretaria de Assistência Social. A iniciativa busca arrecadar roupas e cobertores para distribuição a famílias em vulnerabilidade durante o inverno gaúcho. Empresas, escolas e moradores podem contribuir nos pontos de coleta espalhados pela cidade.",
            "fechamento_8s": "Mobilização anual cresce no início do frio.",
            "cta_5s": "Detalhes e pontos de coleta no SulTV.",
            "trilha_sugerida": "instrumental ascendente"
        },
        "tag_thumbnail": "Pelotas recebe agasalhos",
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta de utilidade pública em Pelotas (Costa Doce ampliada). Título original era cabeçalho da seção; reescrito com base no conteúdo real."
    },

    # --- 5. Copa Prefeito 2026 Cristal ---
    "e04af26ff80167353fa5704d59d6095acaa86096": {
        "titulo_sultv": "Cristal abre Copa Prefeito 2026 com cerimônia no Estádio da Baixada",
        "subtitulo": "Torneio amador reúne equipes locais e marca início da temporada do futebol municipal.",
        "lead": "A Copa Prefeito 2026 de Cristal foi oficialmente aberta no Estádio da Baixada, no campo municipal, com cerimônia e os primeiros jogos da fase inicial. A competição mobiliza equipes da cidade e reforça o calendário do futebol amador na região da Costa Doce.",
        "ganchos_3": [
            "Cerimônia oficial marca abertura no Estádio da Baixada",
            "Primeiros jogos já entregaram clima de torneio",
            "Esporte amador como vetor de comunidade em Cristal"
        ],
        "angulo_editorial": "Esporte amador em cidade-núcleo SulTV (Cristal). Pauta de comunidade e identidade local, com cobertura factual da abertura.",
        "fontes_complementares_sugeridas": ["Liga Pelotense", "Federação Gaúcha de Futebol"],
        "lead_materia_longa": "A Copa Prefeito 2026 de Cristal teve abertura oficial no Estádio da Baixada, no campo municipal, com cerimônia e os primeiros jogos da fase inicial do torneio. A competição é tradicional no calendário esportivo da cidade e mobiliza equipes amadoras da região, reunindo comunidade, dirigentes e torcedores em torno do futebol local. A edição deste ano segue formato semelhante às anteriores, com fase classificatória e mata-mata, e tem nas arquibancadas um termômetro da força do esporte amador na Costa Doce, segmento que vem ganhando estrutura e visibilidade no Sul do Rio Grande do Sul. Os jogos seguem nas próximas semanas no campo municipal, com agenda definida pela organização da competição.",
        "post_instagram": {
            "caption": "Começou em Cristal a Copa Prefeito 2026: cerimônia oficial e primeiros jogos no Estádio da Baixada marcaram a abertura.",
            "hashtags": ["#Cristal", "#CopaPrefeito", "#FutebolAmador", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Bola rolando em Cristal.",
            "desenvolvimento_45s": "A Copa Prefeito 2026 foi oficialmente aberta no Estádio da Baixada, em Cristal. Com cerimônia de abertura e primeiros jogos, o torneio mobiliza equipes amadoras da cidade e reforça a tradição do futebol local na Costa Doce. A competição segue nas próximas semanas com fase classificatória e mata-mata.",
            "fechamento_8s": "Comunidade no campo, esporte como ponto de encontro.",
            "cta_5s": "Resultados rodada a rodada no SulTV.",
            "trilha_sugerida": "vinheta esportiva regional"
        },
        "tag_thumbnail": "Copa Prefeito começou",
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Esporte amador em cidade-núcleo SulTV (Cristal) — vetor de comunidade"
    },

    # --- 6. Fotos do Flickr Farsul — BLOQUEAR ---
    "54da86550dbad394c36708a7a9c2f7ad94d48e38": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "Item é cabeçalho da seção de fotos do site da Farsul — não é matéria.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {}, "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Guardrail: título é cabeçalho de seção (‘Fotos do Flickr’), não conteúdo editorial"
    },

    # --- 7. Senar Goiás — REBAIXAR (sem âncora Sul-RS) ---
    "da51f513eedac97c3509a07562301081e4f2e203": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "Cobertura sobre cursos do Senar em Goiás. Sem âncora regional Sul-RS. Cabe encaminhar para acompanhamento do Senar-RS em pauta futura.",
        "fontes_complementares_sugeridas": ["Senar-RS"],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {}, "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Pauta nacional (Goiás) sem âncora Sul-RS — fora do perímetro editorial"
    },

    # --- 8. INFORMAÇÕES AGROPECUÁRIAS Emater — BLOQUEAR ---
    "e914edb4101909198de490e19b4ee3ebeb063e57": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "Item é cabeçalho da seção do site da Emater RS — não é matéria.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {}, "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Guardrail: título é cabeçalho de seção (‘INFORMAÇÕES AGROPECUÁRIAS’) — sem conteúdo editorial unitário"
    },

    # --- 9. Avisos e Alertas Defesa Civil — BLOQUEAR ---
    "72da33ff967bd936651054a9f0405448f2ba54dd": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "Item é índice da seção de prevenção do site da Defesa Civil RS — não é matéria individual.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {}, "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Guardrail: título genérico de seção (‘Avisos e Alertas / Dicas de prevenção’)"
    },

    # --- 10. Copersucar biometano — REBAIXAR (sem âncora) ---
    "d1d93bf71ca273d885626f17d7f7f2fb2cf3f0f4": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "Inovação relevante (frota a biometano), mas pauta nacional sem âncora Sul-RS. Pode entrar em pauta futura conectando com cooperativas e setor canavieiro do RS.",
        "fontes_complementares_sugeridas": ["FETAG-RS", "Cooperativas de cana RS"],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {}, "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Pauta nacional Forbes sem âncora Sul-RS — guardar para futura cobertura conectada à região"
    },

    # --- 11. Prenda 24ª RT Venâncio Aires ---
    "198d34443ce0b2b43ce512566321c485eec36f93": {
        "titulo_sultv": "Prenda do GF Essência da Tradição representa a 24ª RT na Ciranda Estadual",
        "subtitulo": "Laura Janisch Machado, de 16 anos, vai disputar a Ciranda Estadual de Prendas representando a região.",
        "lead": "Laura Janisch Machado, prenda Juvenil do GF Essência da Tradição, representará a 24ª Região Tradicionalista na Ciranda Estadual de Prendas. A jovem de 16 anos, moradora de Venâncio Aires, foi escolhida em concurso regional e disputará a próxima etapa da seleção estadual do MTG-RS.",
        "ganchos_3": [
            "Prenda Juvenil de 16 anos representa a 24ª RT",
            "Cultura gaúcha em destaque na Ciranda Estadual",
            "Tradicionalismo do Vale do Rio Pardo no centro do palco"
        ],
        "angulo_editorial": "Cultura gauchesca em alta nas redes — pauta leve, de identidade regional, com bom apelo visual para Instagram/Facebook.",
        "fontes_complementares_sugeridas": ["MTG-RS", "24ª RT"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Laura Janisch Machado, prenda Juvenil do GF Essência da Tradição, representa a 24ª Região Tradicionalista na Ciranda Estadual. Aos 16 anos, a jovem de Venâncio Aires leva a tradição do Vale do Rio Pardo ao palco estadual.",
            "hashtags": ["#Tradicionalismo", "#MTGRS", "#VenâncioAires", "#PrendaGaúcha", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tradição gaúcha em destaque.",
            "desenvolvimento_45s": "Laura Janisch Machado, prenda Juvenil do GF Essência da Tradição, vai representar a 24ª Região Tradicionalista na Ciranda Estadual de Prendas. A jovem de 16 anos é moradora de Venâncio Aires e leva ao palco estadual a identidade cultural do Vale do Rio Pardo.",
            "fechamento_8s": "Representação regional na maior seleção de prendas do RS.",
            "cta_5s": "Cobertura no SulTV.",
            "trilha_sugerida": "milonga"
        },
        "tag_thumbnail": "Prenda Juvenil na Ciranda Estadual",
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta cultural identitária do RS — alto apelo para post social, sem matéria longa"
    },

    # --- 12. Vacinação contra gripe Passo do Sobrado/Vale Verde ---
    "71223ffdfdd9ee63e44248cd411e7a8ba969ae51": {
        "titulo_sultv": "Vacinação contra gripe avança em Passo do Sobrado e Vale Verde",
        "subtitulo": "Municípios aplicaram mais de 80% das doses recebidas do Ministério da Saúde.",
        "lead": "Passo do Sobrado e Vale Verde, na região central do Rio Grande do Sul, lideram o avanço da campanha de vacinação contra a gripe no Vale do Rio Pardo. Ambos os municípios já aplicaram mais de 80% das doses recebidas do Ministério da Saúde, com cobertura voltada aos públicos prioritários.",
        "ganchos_3": [
            "Mais de 80% das doses já aplicadas nos dois municípios",
            "Cobertura prioriza públicos definidos pelo Ministério da Saúde",
            "Vale do Rio Pardo na liderança regional da campanha"
        ],
        "angulo_editorial": "Serviço público de saúde com dado concreto — campanha de vacinação (não diagnóstico individual). Foco no avanço comparativo da cobertura.",
        "fontes_complementares_sugeridas": ["Secretaria Estadual de Saúde RS", "Conass"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Passo do Sobrado e Vale Verde avançam na vacinação contra a gripe — mais de 80% das doses recebidas do Ministério da Saúde já foram aplicadas. Cobertura segue voltada aos públicos prioritários.",
            "hashtags": ["#Vacinação", "#SaúdePública", "#PassoDoSobrado", "#ValeVerde", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Vacinação avança no Vale do Rio Pardo.",
            "desenvolvimento_45s": "Passo do Sobrado e Vale Verde já aplicaram mais de 80% das doses da vacina contra a gripe recebidas do Ministério da Saúde. A cobertura está voltada aos públicos prioritários definidos pelo governo federal e coloca os dois municípios entre os mais adiantados da região.",
            "fechamento_8s": "Cobertura segue ativa nas unidades de saúde.",
            "cta_5s": "Mais informações no SulTV.",
            "trilha_sugerida": "instrumental claro"
        },
        "tag_thumbnail": "Vacinação avança no RS",
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Saúde pública (campanha de vacinação) com dado quantitativo — não é orientação médica individual"
    },

    # --- 13. Wine South America Bento Gonçalves ---
    "bc7b4592afbe4be54f5137a9e16b76cb4ddeeb92": {
        "titulo_sultv": "Wine South America 2026 movimenta R$ 120 milhões em negócios em Bento Gonçalves",
        "subtitulo": "Feira reuniu mais de 7 mil visitantes e compradores de 20 países na Serra Gaúcha.",
        "lead": "A Wine South America 2026 movimentou R$ 120 milhões em negócios em Bento Gonçalves, na Serra Gaúcha. A sexta edição da feira reuniu mais de 7 mil visitantes e compradores de mais de 20 países, consolidando o Brasil entre os mercados mais estratégicos para o setor vitivinícola internacional.",
        "ganchos_3": [
            "R$ 120 milhões em negócios na sexta edição",
            "Mais de 7 mil visitantes e compradores de 20 países",
            "Serra Gaúcha reforça liderança no setor vitivinícola"
        ],
        "angulo_editorial": "Negócio expressivo do agro gaúcho (vitivinicultura) — dado quantitativo forte. Cobertura factual com leitura econômica regional.",
        "fontes_complementares_sugeridas": ["Ibravin", "Aprovale"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Wine South America 2026 movimentou R$ 120 milhões em Bento Gonçalves — mais de 7 mil visitantes e compradores de 20 países passaram pela Serra Gaúcha na sexta edição da feira.",
            "hashtags": ["#WineSouthAmerica", "#BentoGonçalves", "#SerraGaúcha", "#Vitivinicultura", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Vinho gaúcho fatura alto.",
            "desenvolvimento_45s": "A Wine South America 2026 fechou em Bento Gonçalves com R$ 120 milhões em negócios. A sexta edição da feira reuniu mais de 7 mil visitantes e compradores de mais de 20 países, consolidando o Brasil entre os mercados mais estratégicos para o setor vitivinícola internacional.",
            "fechamento_8s": "Serra Gaúcha reforça protagonismo no vinho.",
            "cta_5s": "Cobertura completa no SulTV.",
            "trilha_sugerida": "instrumental sofisticado"
        },
        "tag_thumbnail": "Wine SA fatura R$ 120 milhões",
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Negócio expressivo do agro gaúcho (vitivinicultura) com dado quantitativo — alto interesse"
    },

    # --- 14. Aeroclube Bento Gonçalves edital — BLOQUEAR ---
    "4f84b92329ebd586d2c5352aad064536b6f84614": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "Edital de convocação de assembleia de aeroclube — conteúdo procedural, sem valor editorial para a audiência SulTV.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {}, "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Guardrail: edital procedural (convocação de assembleia) — não é matéria"
    },
}

# Matérias longas no formato literal do PROMPT_REDACAO_SULTV.
MATERIAS = {
    # 1. Arambaré cursos
    "e370728cabf9868c99ea7f3a5323d444ac76d0dd": """### Título ###
Arambaré abre inscrições para cursos gratuitos de qualificação profissional

### Artigo ###
A Prefeitura de Arambaré, na Costa Doce gaúcha, abriu inscrições para um conjunto de cursos gratuitos de qualificação profissional voltados aos moradores da cidade. O programa integra a estratégia municipal de geração de renda e ampliação de oportunidades em uma região marcada pela combinação entre economia rural, turismo de praia e pesca artesanal. As vagas são limitadas e contemplam diferentes áreas técnicas, com início das aulas previsto para as próximas semanas em espaço disponibilizado pela Prefeitura. A iniciativa reforça o esforço da gestão municipal em conectar a mão de obra local a setores com demanda crescente no comércio, nos serviços e na cadeia produtiva regional. As capacitações são estruturadas em diferentes módulos e contam com cargas horárias compatíveis com a rotina de trabalho dos participantes, fator que tende a ampliar a adesão. Para o município, o programa representa uma porta de entrada para qualificação profissional sem barreiras de custo, contribuindo diretamente para a permanência dos jovens na cidade e para a profissionalização de trabalhadores que atuam de forma autônoma na orla, no comércio e nos serviços locais. A Prefeitura informa que as inscrições devem ser feitas presencialmente na sede da Prefeitura, com documentação básica, e que a divulgação das listas de selecionados sairá após o período de inscrição. A expectativa é de que o programa seja replicado em ciclos ao longo do ano, conforme demanda da população e disponibilidade de parceiros institucionais.

### Legenda sugerida ###
Arambaré abre inscrições para cursos gratuitos de qualificação profissional.

### Palavras-chave ###
Arambaré, cursos gratuitos, qualificação profissional, Costa Doce, prefeitura, geração de renda, capacitação
""",

    # 3. Cristal workshop
    "7f82eab384d643864de1fa6898d10d5f0535abc7": """### Título ###
Cristal recebe workshop “Artesão em Foco” nos dias 18 e 19 de maio

### Artigo ###
Cristal, no Sul do Rio Grande do Sul, recebe nos dias 18 e 19 de maio o workshop “Artesão em Foco”, voltado para a qualificação de artesãos e o desenvolvimento de produtos identitários da região. A programação integra oficinas práticas, orientações técnicas e capacitações pensadas para fortalecer a microeconomia local e dar visibilidade ao trabalho de produtores manuais da Costa Doce. A iniciativa parte da Prefeitura de Cristal em parceria com instituições de apoio ao artesanato e busca conectar a produção local com mercados de turismo e cultura, segmentos em expansão na região. As atividades são abertas a artesãos de toda a região e oferecem uma combinação de teoria e prática que vai desde escolha de matéria-prima e técnicas de acabamento até orientações sobre precificação, identidade visual de marca e canais de comercialização. O workshop reforça uma tendência observada em diversos municípios da Costa Doce, que vêm tratando o artesanato como ativo de desenvolvimento econômico, identidade cultural e atração turística. Os organizadores informam que a programação completa será divulgada nos canais oficiais da Prefeitura, com vagas distribuídas conforme inscrição prévia. Para Cristal, o evento representa uma oportunidade de integrar artesãos novos e experientes, fortalecer redes de produção e qualificar o que chega ao consumidor final, em um momento em que a procura por peças com identidade regional cresce no estado.

### Legenda sugerida ###
Cristal recebe workshop “Artesão em Foco” nos dias 18 e 19 de maio.

### Palavras-chave ###
Cristal, artesanato, Costa Doce, capacitação, workshop, produtos identitários, microeconomia
""",

    # 4. Pelotas Campanha do Agasalho
    "5b53c846036bb2fb31255b4e16c4bd893985f60e": """### Título ###
Pelotas lança Campanha do Agasalho 2026 com primeiras doações já entregues

### Artigo ###
A Prefeitura de Pelotas lançou esta semana a Campanha do Agasalho 2026, com as primeiras doações já entregues à Secretaria Municipal de Assistência Social. A iniciativa busca arrecadar roupas, cobertores e calçados em bom estado para distribuição a famílias em situação de vulnerabilidade durante o inverno gaúcho, período em que a demanda por proteção térmica cresce significativamente na região. A campanha conta com pontos de coleta espalhados por escolas, secretarias municipais e estabelecimentos parceiros, e mobiliza empresas, escolas e moradores em torno de uma rede de solidariedade. O modelo se repete há mais de uma década no município e mantém-se como uma das principais ações de articulação entre poder público e sociedade civil no enfrentamento aos efeitos do frio sobre as populações mais expostas. A Secretaria de Assistência Social coordena a triagem e a distribuição das peças, com atenção prioritária a famílias acompanhadas pelos serviços socioassistenciais da rede municipal. Para 2026, a expectativa é ampliar o número de pontos de coleta e a integração com empresas locais, replicando boas práticas dos anos anteriores. O movimento de chegada das primeiras doações indica engajamento já no início da campanha e abre caminho para uma temporada de mobilização mais ampla nas próximas semanas. Quem desejar contribuir pode procurar os pontos de coleta divulgados pela Prefeitura.

### Legenda sugerida ###
Pelotas lança Campanha do Agasalho 2026 com primeiras doações já entregues.

### Palavras-chave ###
Pelotas, Campanha do Agasalho, Assistência Social, inverno gaúcho, doação, solidariedade, Costa Doce
""",

    # 5. Copa Prefeito Cristal
    "e04af26ff80167353fa5704d59d6095acaa86096": """### Título ###
Cristal abre Copa Prefeito 2026 com cerimônia no Estádio da Baixada

### Artigo ###
A Copa Prefeito 2026 de Cristal teve abertura oficial no Estádio da Baixada, no campo municipal, com cerimônia e os primeiros jogos da fase inicial do torneio. A competição é tradicional no calendário esportivo da cidade e mobiliza equipes amadoras da região, reunindo comunidade, dirigentes e torcedores em torno do futebol local. A edição deste ano segue formato semelhante às anteriores, com fase classificatória e mata-mata, e tem nas arquibancadas um termômetro da força do esporte amador na Costa Doce, segmento que vem ganhando estrutura e visibilidade no Sul do Rio Grande do Sul. A abertura oficial reuniu jogadores, comissões técnicas, dirigentes e moradores no Estádio da Baixada, com a cerimônia funcionando também como ponto de encontro para a comunidade local. Os primeiros confrontos já entregaram clima de torneio, com jogos disputados e presença significativa de torcedores nas arquibancadas. A Copa Prefeito faz parte do calendário de incentivo ao esporte amador da Prefeitura e cumpre papel relevante na integração de bairros e comunidades rurais do município. A organização anunciou que os jogos seguirão nas próximas semanas no campo municipal, com agenda definida pela coordenação da competição, e que as equipes mais bem colocadas avançarão à fase eliminatória. Para Cristal, a Copa Prefeito tornou-se um dos principais espaços de fomento ao esporte de base e expressão da cultura comunitária no calendário anual.

### Legenda sugerida ###
Cristal abre Copa Prefeito 2026 com cerimônia no Estádio da Baixada.

### Palavras-chave ###
Cristal, Copa Prefeito, futebol amador, Estádio da Baixada, esporte municipal, Costa Doce, comunidade
""",
}


def main() -> None:
    aprovadas = json.loads(APROVADAS.read_text(encoding="utf-8"))
    items = aprovadas.get("aprovadas", aprovadas) if isinstance(aprovadas, dict) else aprovadas
    pauta_items = []
    for it in items:
        h = it["id_hash"]
        ang = PAUTA_ANGULADA.get(h)
        if not ang:
            ang = {
                "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
                "angulo_editorial": "Sem angulação atribuída — revisar manualmente.",
                "fontes_complementares_sugeridas": [],
                "lead_materia_longa": "",
                "post_instagram": {"caption": "", "hashtags": []},
                "roteiro_short_60s": {}, "tag_thumbnail": "",
                "decisao_final": "ALERTA_HUMANO",
                "decisao_motivo": "Item não angulado pela curadoria do dia"
            }
        # preserva TODOS os campos do aprovada (necessários pro MateriaPronta)
        merged = {**it, **ang}
        pauta_items.append(merged)

    pauta = {
        "data": HOJE,
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "total": len(pauta_items),
        "pauta": pauta_items,
    }
    PAUTA_OUT.write_text(json.dumps(pauta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[angular] -> {PAUTA_OUT}")

    publicar = [m for m in pauta_items if m["decisao_final"] == "PUBLICAR"]
    longas = [m for m in publicar if m["formato_sugerido"] == "materia_longa"]
    print(f"[angular] decisão PUBLICAR: {len(publicar)}  (matérias longas: {len(longas)})")
    for h, corpo in MATERIAS.items():
        out = MAT_DIR / f"{h}.md"
        out.write_text(corpo, encoding="utf-8")
        print(f"[angular] matéria -> {out}")


if __name__ == "__main__":
    main()
