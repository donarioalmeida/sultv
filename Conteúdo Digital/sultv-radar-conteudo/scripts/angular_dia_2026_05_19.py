#!/usr/bin/env python3
"""
angular_dia_2026_05_19.py — angulação editorial da pauta do dia 19/05/2026.
Roda no fluxo cowork-faz-tudo: Claude executa toda a angulação na sessão.

Saídas:
  state/pauta_2026-05-19.json
  state/materias_2026-05-19/<id_hash>.md  (matérias longas)
"""
from __future__ import annotations
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-05-19"


PAUTA_ANGULADA = {
    # 1. Arambaré — cursos gratuitos de qualificação profissional (score 9, cidade-núcleo)
    "e370728cabf9868c99ea7f3a5323d444ac76d0dd": {
        "titulo_sultv": "Arambaré abre inscrições para cursos gratuitos de qualificação profissional",
        "subtitulo": "Programa municipal oferece capacitação técnica gratuita para moradores da Costa Doce.",
        "lead": "A Prefeitura de Arambaré abriu inscrições para cursos gratuitos de qualificação profissional voltados aos moradores da cidade. As vagas são limitadas e contemplam diferentes áreas técnicas, dentro da política municipal de geração de renda para a Costa Doce.",
        "ganchos_3": [
            "Inscrições gratuitas com vagas limitadas",
            "Eixo de qualificação ligado ao mercado regional",
            "Política pública de geração de renda em cidade-núcleo da SulTV",
        ],
        "angulo_editorial": "Cidade-núcleo SulTV (Arambaré) com fato concreto de serviço público, alinhado ao interesse central da audiência da Costa Doce — pauta de prioridade máxima.",
        "fontes_complementares_sugeridas": ["FGTAS-Sine RS", "Sebrae RS", "Senac RS"],
        "lead_materia_longa": "A Prefeitura de Arambaré, na Costa Doce gaúcha, abriu inscrições para um pacote de cursos gratuitos de qualificação profissional voltado aos moradores da cidade. As vagas são limitadas e contemplam diferentes áreas técnicas, com aulas previstas para iniciar nas próximas semanas. O programa integra a estratégia da gestão municipal de ampliar oportunidades de renda em uma região marcada pela combinação entre economia rural, turismo de praia e pesca artesanal. A iniciativa busca conectar a mão de obra local a setores com demanda crescente em Arambaré e no entorno.",
        "post_instagram": {
            "caption": "Arambaré abriu inscrições para cursos gratuitos de qualificação profissional. Vagas limitadas — moradores da Costa Doce já podem garantir o lugar.",
            "hashtags": ["#Arambaré", "#CostaDoce", "#SulTV", "#Qualificação", "#TrabalhoRS"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Arambaré abre cursos gratuitos.",
            "desenvolvimento_45s": "A Prefeitura de Arambaré está com inscrições abertas para cursos gratuitos de qualificação profissional. As vagas são limitadas e estão distribuídas em diferentes áreas técnicas, alinhadas a oportunidades de trabalho na Costa Doce. O programa faz parte da política municipal de geração de renda e busca ampliar a empregabilidade dos moradores em setores como comércio, serviços e cadeia produtiva regional.",
            "fechamento_8s": "Vagas limitadas — moradores devem procurar a Prefeitura.",
            "cta_5s": "Acompanhe a íntegra no SulTV.",
            "trilha_sugerida": "instrumental otimista",
        },
        "tag_thumbnail": "Vagas gratuitas em Arambaré",
        "briefing_visual": {
            "descricao_pt": "Sala de aula técnica vazia com bancadas, ferramentas e cadernos sobre as mesas, luz natural pela janela, ambiente acolhedor de centro de formação profissional no interior do RS",
            "query_en": [
                "vocational training classroom empty",
                "professional course workshop brazil",
                "adult education classroom workbench",
            ],
            "evitar": ["pessoas com rosto visível", "marcas", "texto sobreposto", "logos"],
            "prompt_ia": "Wide shot of an empty vocational training classroom in a small Brazilian town, wooden workbenches with tools and notebooks, soft natural daylight from large windows, warm welcoming atmosphere, no people, no text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cidade-núcleo (Arambaré) com fato de serviço público — conteúdo prioritário",
    },

    # 2. Cristal — Movimento Sul Resiliente / adaptação climática (score 8, segunda camada)
    "8f012b6b663e922efd2e3e46ca8ef2dbfd09589a": {
        "titulo_sultv": "Cristal recebe reunião do Movimento Sul Resiliente e ganha mapeamento de prevenção a desastres",
        "subtitulo": "Encontro na Câmara Municipal debateu adaptação climática e entregou estudo técnico ao município.",
        "lead": "Cristal, no Sul do Rio Grande do Sul, recebeu reunião do Movimento Sul Resiliente na Câmara Municipal. O encontro debateu ações de adaptação climática e entregou ao município um estudo de mapeamento para prevenção de desastres, ferramenta que passa a orientar políticas locais de resposta ao clima.",
        "ganchos_3": [
            "Cristal ganha mapeamento técnico de áreas de risco",
            "Movimento Sul Resiliente articula adaptação climática regional",
            "Câmara Municipal abre debate sobre prevenção a desastres",
        ],
        "angulo_editorial": "Cidade da segunda camada Sul-RS recebe ferramenta concreta (mapeamento) de adaptação climática — pauta de inovação + clima + gestão pública, com impacto direto na agenda da Costa Doce após os eventos extremos de 2024/25.",
        "fontes_complementares_sugeridas": ["Defesa Civil RS", "Sema RS", "Famurs"],
        "lead_materia_longa": "Cristal, no Sul do Rio Grande do Sul, sediou reunião do Movimento Sul Resiliente na Câmara Municipal e recebeu um estudo de mapeamento para prevenção de desastres. O documento, fruto de articulação entre municípios da região e especialistas em adaptação climática, identifica áreas vulneráveis e oferece base técnica para ações preventivas. O encontro reuniu vereadores, técnicos da Prefeitura e representantes do movimento, com foco em estruturar respostas locais coordenadas frente à intensificação de eventos climáticos extremos no Estado.",
        "post_instagram": {
            "caption": "Cristal recebeu o Movimento Sul Resiliente e ganhou um mapeamento técnico para prevenir desastres. Adaptação climática vira agenda de governo municipal na Costa Doce.",
            "hashtags": ["#Cristal", "#SulResiliente", "#CostaDoce", "#AdaptaçãoClimática", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal vira referência em adaptação climática.",
            "desenvolvimento_45s": "A Câmara Municipal de Cristal recebeu reunião do Movimento Sul Resiliente. No encontro, o município ganhou um estudo de mapeamento para prevenção de desastres — uma ferramenta técnica que aponta áreas vulneráveis e orienta políticas de adaptação climática. A iniciativa fortalece a articulação regional do Sul do Rio Grande do Sul para responder de forma coordenada a eventos extremos.",
            "fechamento_8s": "Mapeamento agora orienta políticas locais.",
            "cta_5s": "Detalhes no SulTV.",
            "trilha_sugerida": "instrumental técnico-prospectivo",
        },
        "tag_thumbnail": "Cristal mapeia o risco",
        "briefing_visual": {
            "descricao_pt": "Vista aérea de área urbana com várzea de rio ao fundo no Sul do RS, mostrando ocupação próxima a curso d'água, sob luz de fim de tarde",
            "query_en": [
                "aerial view small brazilian town river",
                "floodplain rural town aerial",
                "flood risk mapping aerial city",
            ],
            "evitar": ["pessoas identificáveis", "marcas", "texto sobreposto", "danos explícitos"],
            "prompt_ia": "Aerial wide shot of a small southern Brazilian town adjacent to a river floodplain at golden hour, mixed urban-rural landscape, calm composition suggesting climate resilience planning, no people visible, no text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cidade da segunda camada com fato concreto + pauta de inovação climática — relevância editorial alta",
    },

    # 3. Pelotas — "Transporte e Trânsito" (cabeçalho de seção)
    "da39a3ee5e6b4b0d3255bfef95601890afd80709": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Título 'Transporte e Trânsito' é cabeçalho de seção do site da Prefeitura, com URL #carouselNews — não é matéria.",
    },

    # 4. Pelotas — STT radar móvel (score 8, Costa Doce ampliada) — versão com URL própria
    "b492b5920e42020715e5357b680e77c87f01dd69": {
        "titulo_sultv": "Pelotas amplia fiscalização eletrônica com radar móvel em duas avenidas centrais",
        "subtitulo": "Ildefonso Simões Lopes e JK de Oliveira passam a integrar o monitoramento da STT.",
        "lead": "A Superintendência de Transporte e Trânsito (STT) de Pelotas amplia a fiscalização eletrônica e passa a operar radar móvel nas avenidas Ildefonso Simões Lopes e JK de Oliveira. Os equipamentos integram o monitoramento eletrônico do município e atuam em vias com fluxo intenso.",
        "ganchos_3": [
            "Duas avenidas centrais entram no radar móvel",
            "STT amplia monitoramento eletrônico",
            "Pauta de segurança viária em Pelotas",
        ],
        "angulo_editorial": "Cidade da Costa Doce ampliada (Pelotas) com fato de serviço público e ângulo de tecnologia em fiscalização — pauta de utilidade direta para o público da SulTV.",
        "fontes_complementares_sugeridas": ["STT Pelotas", "Detran RS"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Atenção em Pelotas: STT amplia fiscalização com radar móvel nas avenidas Ildefonso Simões Lopes e JK de Oliveira. Monitoramento eletrônico entra em operação.",
            "hashtags": ["#Pelotas", "#Trânsito", "#STT", "#CostaDoce", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Pelotas amplia o radar móvel.",
            "desenvolvimento_45s": "A STT de Pelotas anunciou a ampliação da fiscalização eletrônica em duas avenidas centrais. Ildefonso Simões Lopes e JK de Oliveira passam a integrar o monitoramento por radar móvel da cidade. A medida amplia o controle de velocidade em vias com fluxo intenso e reforça a estratégia municipal de segurança viária.",
            "fechamento_8s": "Motoristas devem reforçar atenção em rotas centrais.",
            "cta_5s": "Mais informações no SulTV.",
            "trilha_sugerida": "vinheta urbana objetiva",
        },
        "tag_thumbnail": "Pelotas reforça o radar",
        "briefing_visual": {
            "descricao_pt": "Avenida urbana de Pelotas com tráfego em fluxo livre durante o dia, vista lateral, sinalização viária visível, sem nomes próprios ou placas legíveis",
            "query_en": [
                "urban avenue traffic brazil southern",
                "city avenue cars daytime brazil",
                "traffic enforcement camera street view",
            ],
            "evitar": ["pessoas identificáveis", "placas de carro legíveis", "marcas", "texto sobreposto"],
            "prompt_ia": "Side view of a busy urban avenue in a southern Brazilian midsize city during daytime, moderate car traffic, visible traffic signage but no readable plates or branding, neutral overcast light, no people identifiable, no text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato concreto em cidade Costa Doce ampliada (Pelotas) com utilidade direta para a audiência — formato nota curta sobe a post",
    },

    # 5. Cristal — Copa Prefeito 2026 (score 7 + esporte → post_instagram pela regra 7)
    "e04af26ff80167353fa5704d59d6095acaa86096": {
        "titulo_sultv": "Cristal abre Copa Prefeito 2026 com cerimônia no Estádio da Baixada",
        "subtitulo": "Competição reúne equipes amadoras locais e marca o início do calendário esportivo da cidade.",
        "lead": "A Copa Prefeito 2026 de Cristal foi oficialmente aberta no Estádio da Baixada, com cerimônia e os primeiros jogos da fase inicial. A competição mobiliza equipes amadoras locais e reforça o calendário do futebol amador na Costa Doce.",
        "ganchos_3": [
            "Cerimônia oficial marca abertura no Estádio da Baixada",
            "Primeiros jogos já entregaram clima de torneio",
            "Esporte amador como vetor de comunidade em Cristal",
        ],
        "angulo_editorial": "Esporte amador em cidade da segunda camada — pauta de comunidade. Como tag inclui esporte, formato sobe a post_instagram pela régua editorial.",
        "fontes_complementares_sugeridas": ["Liga Cristalense de Futebol"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Bola rolando em Cristal: Copa Prefeito 2026 abriu oficialmente no Estádio da Baixada. Esporte amador como vetor de comunidade na Costa Doce.",
            "hashtags": ["#Cristal", "#CopaPrefeito2026", "#FutebolAmador", "#CostaDoce", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Bola rolando em Cristal.",
            "desenvolvimento_45s": "A Copa Prefeito 2026 foi oficialmente aberta no Estádio da Baixada, em Cristal. Com cerimônia oficial e primeiros jogos, o torneio mobiliza equipes amadoras da cidade e reforça a tradição do futebol local na Costa Doce. A competição segue nas próximas semanas com fase classificatória e mata-mata.",
            "fechamento_8s": "Comunidade no campo, esporte como ponto de encontro.",
            "cta_5s": "Resultados rodada a rodada no SulTV.",
            "trilha_sugerida": "vinheta esportiva regional",
        },
        "tag_thumbnail": "Copa Prefeito começou",
        "briefing_visual": {
            "descricao_pt": "Campo de futebol amador municipal no Sul do RS visto da arquibancada, grama bem cuidada, traves brancas, sem jogadores ou público em primeiro plano",
            "query_en": [
                "amateur soccer field empty brazil",
                "small town football stadium brazil",
                "municipal soccer pitch sunny day",
            ],
            "evitar": ["pessoas identificáveis", "marcas patrocinadoras", "texto sobreposto", "logos de clubes"],
            "prompt_ia": "Wide shot of a small municipal amateur football field in southern Brazil viewed from empty bleachers, well-kept grass, white goalposts, partly cloudy sky, no players visible, no people identifiable, no text, no brand logos, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Esporte amador em cidade da hierarquia editorial — vetor de comunidade, formato post",
    },

    # 6. Canal Rural — recursos para agricultura familiar no RN (REBAIXAR: sem âncora RS)
    "3f96051ef8a32226e327bdbffb7ea436ff289d7d": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Pauta nacional sobre o Rio Grande do Norte — sem ancoragem Sul-RS. Mantida como nota interna para referência.",
    },

    # 7. Emater — "INFORMAÇÕES AGROPECUÁRIAS" (cabeçalho)
    "e914edb4101909198de490e19b4ee3ebeb063e57": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Cabeçalho de seção do site Emater RS — não é matéria. Itens reais (Polo Ervateiro, Mãe Destaque) estão dentro do resumo, mas o título extraído é genérico.",
    },

    # 8. Defesa Civil RS — "Avisos e Alertas" (cabeçalho)
    "72da33ff967bd936651054a9f0405448f2ba54dd": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Cabeçalho de seção da Defesa Civil RS — não é matéria.",
    },

    # 9. Farsul — "Fotos do Flickr" (agregador)
    "54da86550dbad394c36708a7a9c2f7ad94d48e38": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Agregador de fotos do site da Farsul — não é matéria. Parceiro estratégico (Donário lidera Comissão de Inovação): ainda mais cuidado para não publicar ruído.",
    },

    # 10. Canal Rural — Arqueias com potencial para milho em solos salinizados (score 6, post)
    "ab24f0065135aa38940405f3e62079bff804a1ba": {
        "titulo_sultv": "Pesquisa identifica arqueias com potencial para milho em solos salinizados",
        "subtitulo": "Estudo da Embrapa e da Brandeis University aponta caminho para novos bioinsumos.",
        "lead": "Pesquisa conduzida pela Embrapa em parceria com a Brandeis University identificou arqueias com potencial para elevar a tolerância do milho a solos salinizados. O resultado abre frente para novos bioinsumos e tem leitura relevante para regiões do Brasil que enfrentam salinização de solo, incluindo lavouras de arroz no litoral do RS.",
        "ganchos_3": [
            "Arqueias podem ajudar milho a tolerar excesso de sal",
            "Parceria Embrapa + Brandeis abre frente para bioinsumos",
            "Salinização de solo é desafio também no litoral gaúcho",
        ],
        "angulo_editorial": "Pauta nacional de inovação agro com leitura regional clara: salinização de solo é problema relevante em áreas de produção de arroz no litoral Sul do RS, onde a SulTV tem audiência rural.",
        "fontes_complementares_sugeridas": ["Embrapa Clima Temperado", "Irga"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Embrapa + Brandeis University identificaram arqueias capazes de aumentar a tolerância do milho a solos salinizados. Pesquisa abre frente para novos bioinsumos — tema sensível também para o arroz no litoral do RS.",
            "hashtags": ["#Agro", "#Pesquisa", "#Embrapa", "#Bioinsumos", "#Salinização", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Arqueias podem ajudar o milho.",
            "desenvolvimento_45s": "Pesquisa da Embrapa em parceria com a Brandeis University identificou arqueias — microrganismos antigos — com potencial para aumentar a tolerância do milho a solos com excesso de sal. O achado abre caminho para novos bioinsumos e tem leitura direta para áreas brasileiras que enfrentam salinização de solo, incluindo o litoral do Rio Grande do Sul, onde a cultura do arroz lida com o avanço da salinidade.",
            "fechamento_8s": "Bioinsumos entram no radar da safra futura.",
            "cta_5s": "Mais inovação no SulTV.",
            "trilha_sugerida": "instrumental científico-otimista",
        },
        "tag_thumbnail": "Arqueias contra o sal",
        "briefing_visual": {
            "descricao_pt": "Close-up técnico de raiz de milho com solo em laboratório, iluminação suave de bancada científica, sem rótulos visíveis",
            "query_en": [
                "corn root soil laboratory close up",
                "plant science microbiome research",
                "agriculture research microscope plant",
            ],
            "evitar": ["pessoas com rosto visível", "marcas", "texto sobreposto", "logos de instituições"],
            "prompt_ia": "Close-up macro photograph of a young corn plant root with attached soil on a scientific laboratory bench, soft directional light, neutral background, no labels, no people, no text, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Inovação agro com leitura regional Sul-RS (salinização e arroz no litoral) — pauta de tecnologia",
    },

    # 11. Folha do Mate — Áudios operação 'Contra-ataque' (REBAIXAR)
    "39fd3619e633966f06eec0f1a1651b1c305307fb": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Pauta policial específica de Venâncio Aires sem fato novo concreto neste ciclo — nota interna.",
    },

    # 12. Folha do Mate — Caso Asmuva (REBAIXAR)
    "b3867d5b6ee77a6e6c1b8b232f1e897bcefe9d6f": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Pauta policial municipal específica de VA — fora do core editorial SulTV. Nota interna.",
    },

    # 13. Bento Gonçalves — 10 tiros bairro Progresso (REBAIXAR)
    "014f014c59359f96d1a8dce979e78f08d780f38d": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Pauta policial em Bento Gonçalves — fora do core editorial Sul-RS da SulTV. Nota interna.",
    },

    # 14. Polentaço 2026 — 25 mil visitantes (post_instagram, evento positivo)
    "d7b0fedb8b90418f63ca638848d2caefcf26f72c": {
        "titulo_sultv": "Polentaço 2026 reúne 25 mil visitantes em Monte Belo do Sul em edição histórica de 30 anos",
        "subtitulo": "Festa bate recorde de público e celebra três décadas de tradição na Serra Gaúcha.",
        "lead": "O Polentaço 2026 encerrou no domingo (17), em Monte Belo do Sul, edição histórica que marcou os 30 anos da festa. Com recorde de público, o evento reuniu 25 mil visitantes em três dias, com a tradicional cena do tombo da polenta gigante e atrações inéditas.",
        "ganchos_3": [
            "25 mil visitantes em três dias",
            "Edição histórica de 30 anos",
            "Tombo da polenta gigante mantém a tradição",
        ],
        "angulo_editorial": "Evento gastronômico-cultural com peso turístico para a Serra Gaúcha — pauta positiva, identitária, com fato concreto (recorde de público). Formato post.",
        "fontes_complementares_sugeridas": ["Prefeitura de Monte Belo do Sul", "Setur RS"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Polentaço 2026 fechou em Monte Belo do Sul com 25 mil visitantes em três dias. Edição histórica de 30 anos teve recorde de público e o tradicional tombo da polenta gigante.",
            "hashtags": ["#Polentaço", "#MonteBeloDoSul", "#SerraGaúcha", "#TurismoRS", "#SulTV"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Polentaço bate recorde.",
            "desenvolvimento_45s": "O Polentaço 2026 encerrou em Monte Belo do Sul com 25 mil visitantes em três dias. A edição marcou os 30 anos da festa e teve recorde de público, com o tradicional tombo da polenta gigante e atrações inéditas. O evento consolida o calendário gastronômico-cultural da Serra Gaúcha e reforça a economia do turismo regional.",
            "fechamento_8s": "Festa tradicional volta a movimentar a Serra.",
            "cta_5s": "Cobertura completa no SulTV.",
            "trilha_sugerida": "tradicional italiano-gaúcho festivo",
        },
        "tag_thumbnail": "Polentaço 30 anos",
        "briefing_visual": {
            "descricao_pt": "Tabuleiro de polenta gigante amarela sendo despejado em mesa rústica de madeira em festa popular ao ar livre na Serra Gaúcha, sem rostos identificáveis em primeiro plano",
            "query_en": [
                "polenta italian festival italy",
                "traditional cornmeal feast outdoor",
                "yellow polenta wooden table closeup",
            ],
            "evitar": ["pessoas com rosto visível em primeiro plano", "marcas patrocinadoras", "texto sobreposto"],
            "prompt_ia": "Wide overhead shot of a giant yellow polenta being poured onto a long rustic wooden table at an Italian-Brazilian outdoor festival, soft late afternoon light, warm rural atmosphere, no faces identifiable in foreground, no text, no brand logos, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento turístico-cultural com fato concreto (25 mil visitantes, 30 anos) — pauta positiva regional",
    },
}


# Matérias longas no formato PROMPT_REDACAO_SULTV (3ª pessoa institucional)
MATERIAS = {
    "e370728cabf9868c99ea7f3a5323d444ac76d0dd": """### Título ###
Arambaré abre inscrições para cursos gratuitos de qualificação profissional na Costa Doce

### Artigo ###
A Prefeitura de Arambaré, no Sul do Rio Grande do Sul, abriu inscrições para um pacote de cursos gratuitos de qualificação profissional voltado aos moradores da cidade. As vagas são limitadas e contemplam diferentes áreas técnicas, com aulas previstas para iniciar nas próximas semanas em espaço cedido pelo poder público municipal. A iniciativa integra a estratégia da gestão para ampliar oportunidades de renda na Costa Doce, região marcada pela combinação entre economia rural, turismo de praia e pesca artesanal. Ao oferecer capacitação sem custo, o município busca conectar a mão de obra local a setores em demanda, como comércio, serviços e cadeia produtiva regional. A medida também responde à sazonalidade da economia em Arambaré, em que a oferta de trabalho varia ao longo do ano, e tenta reduzir a dependência de períodos específicos, como o veraneio. Para se inscrever, os interessados devem procurar a Secretaria responsável pela política de trabalho e renda na Prefeitura. A documentação exigida e os critérios de seleção estão disponíveis nos canais oficiais do município. Cursos gratuitos de qualificação profissional vêm sendo apontados como uma das ferramentas mais efetivas para melhorar a empregabilidade em cidades pequenas, sobretudo quando articulados com instituições parceiras e com as demandas reais do mercado regional. A expectativa da Prefeitura é que o programa se consolide como ciclo permanente, integrando novas turmas ao longo do ano. A iniciativa reforça o protagonismo de Arambaré na pauta de desenvolvimento humano da Costa Doce e mostra a preocupação do poder público com a geração de renda em uma região estratégica para o Sul do estado.

### Legenda sugerida ###
Prefeitura de Arambaré abre vagas em cursos gratuitos de qualificação profissional para moradores da Costa Doce.

### Palavras-chave ###
Arambaré, cursos gratuitos, qualificação profissional, Costa Doce, geração de renda, Prefeitura de Arambaré, Sul do RS
""",

    "8f012b6b663e922efd2e3e46ca8ef2dbfd09589a": """### Título ###
Cristal recebe Movimento Sul Resiliente e ganha mapeamento técnico de prevenção a desastres

### Artigo ###
Cristal, no Sul do Rio Grande do Sul, sediou reunião do Movimento Sul Resiliente na Câmara Municipal e recebeu um estudo de mapeamento para prevenção de desastres. O encontro reuniu vereadores, técnicos da Prefeitura e representantes do movimento, com foco em estruturar respostas locais coordenadas frente à intensificação de eventos climáticos extremos no Estado. O Movimento Sul Resiliente articula prefeituras, especialistas e organizações da sociedade civil em torno de ações de adaptação climática no Sul do Rio Grande do Sul. A entrega do mapeamento a Cristal representa um passo concreto para que o município incorpore dados técnicos ao planejamento urbano e à política de proteção civil. O documento identifica áreas de maior vulnerabilidade e oferece base para decisões sobre obras, drenagem, ocupação do solo e protocolos de resposta a eventos extremos. A iniciativa ganha relevância em um cenário em que cidades gaúchas, especialmente as do Sul do estado e da Costa Doce, ainda processam os impactos de enchentes e estiagens severas dos últimos anos. A formalização do mapeamento técnico permite que Cristal antecipe riscos, priorize investimentos e dialogue com outros entes federativos a partir de uma base científica comum. A adesão ao Movimento Sul Resiliente também coloca o município em uma rede regional de troca de experiências, fortalecendo o aprendizado conjunto sobre adaptação. A discussão na Câmara Municipal indica que a agenda climática deixou de ser pauta exclusiva de organismos ambientais para se tornar tema central da gestão pública local. Para a comunidade, o ganho é prático: prevenção custa menos do que reconstrução, e cidades preparadas reduzem o impacto humano e econômico de eventos extremos. O próximo passo, segundo participantes do encontro, é transformar o estudo em diretrizes operacionais nas secretarias municipais, com cronograma de ações de curto, médio e longo prazos.

### Legenda sugerida ###
Cristal recebe Movimento Sul Resiliente e incorpora estudo técnico de mapeamento para prevenção a desastres na Costa Doce.

### Palavras-chave ###
Cristal, Movimento Sul Resiliente, adaptação climática, prevenção a desastres, Costa Doce, Câmara Municipal, Sul do RS
""",

    "b492b5920e42020715e5357b680e77c87f01dd69": """### Título ###
Pelotas amplia fiscalização eletrônica com radar móvel em Ildefonso Simões Lopes e JK de Oliveira

### Artigo ###
A Superintendência de Transporte e Trânsito (STT) de Pelotas anunciou a ampliação da fiscalização eletrônica no município com a entrada em operação do radar móvel em duas avenidas centrais. As avenidas Ildefonso Simões Lopes e JK de Oliveira passam a integrar o sistema de monitoramento eletrônico da cidade, segundo informações divulgadas pela administração municipal. O objetivo é reforçar o controle de velocidade em vias com fluxo elevado e histórico relevante de ocorrências de trânsito. O monitoramento por radar móvel funciona em pontos rotativos, com previsão de presença nos eixos sinalizados pela STT. A medida integra o conjunto de ações de segurança viária do município, que combina sinalização, educação no trânsito e fiscalização eletrônica. Pelotas, principal cidade do Sul do Rio Grande do Sul, tem expandido nos últimos anos o uso de tecnologias de fiscalização, alinhando-se a um movimento mais amplo de outras capitais regionais e cidades médias do estado, que vêm investindo em sistemas inteligentes de gestão do trânsito. A ampliação da fiscalização tem impacto direto na rotina dos motoristas — exige redobrada atenção à sinalização e respeito aos limites de velocidade nas avenidas envolvidas — e tende a reduzir, em médio prazo, os indicadores de gravidade de acidentes nos eixos monitorados. Para a STT, a inclusão de novas avenidas faz parte de um diagnóstico técnico de vias prioritárias, baseado em fluxo, histórico de ocorrências e infraestrutura viária. A expectativa do município é consolidar a fiscalização como ferramenta permanente de gestão de mobilidade. A orientação aos motoristas é simples: respeitar a sinalização e os limites estabelecidos. Mais informações sobre os pontos de operação do radar móvel devem ser divulgadas nos canais oficiais da Prefeitura.

### Legenda sugerida ###
STT amplia fiscalização eletrônica em Pelotas com radar móvel em duas avenidas centrais.

### Palavras-chave ###
Pelotas, STT, radar móvel, fiscalização eletrônica, segurança viária, Costa Doce, trânsito, Sul do RS
""",

    "e04af26ff80167353fa5704d59d6095acaa86096": """### Título ###
Copa Prefeito 2026 começa em Cristal com cerimônia oficial no Estádio da Baixada

### Artigo ###
A Copa Prefeito 2026 de Cristal, no Sul do Rio Grande do Sul, foi oficialmente aberta no Estádio da Baixada, com cerimônia que marcou o início da competição e os primeiros jogos da fase inicial. O torneio é tradicional no calendário esportivo da cidade e mobiliza equipes amadoras formadas em bairros, distritos e empresas locais, reunindo comunidade, dirigentes e torcedores em torno do futebol da região. A edição deste ano segue formato semelhante às anteriores, com fase classificatória e mata-mata, e tem nas arquibancadas um termômetro do peso do esporte amador na Costa Doce. Mais do que disputa esportiva, a Copa Prefeito funciona como ponto de encontro comunitário em uma cidade do porte de Cristal. O estádio se torna palco de convivência, e o calendário do torneio organiza fins de semana inteiros em torno dos jogos. Para a comunidade local, a competição é também uma das poucas ocasiões em que tradições gaúchas de churrasco, encontros familiares e identidade de bairro se entrelaçam com o ritual esportivo. A abertura reforçou ainda a relevância do investimento público em infraestrutura esportiva. O Estádio da Baixada vem recebendo melhorias progressivas, fundamentais para o funcionamento de um torneio que mistura competição, identidade e socialização. Nas próximas semanas, as equipes seguem disputando classificação para a fase eliminatória, com resultados que serão acompanhados de perto pela comunidade local. A organização promete divulgar tabela atualizada nos canais oficiais do município. A Copa Prefeito também opera como vitrine de talentos do futebol amador, com atletas que eventualmente migram para competições regionais de maior alcance, reforçando o papel do esporte de base como vetor de desenvolvimento humano em cidades do interior gaúcho.

### Legenda sugerida ###
Cristal abre Copa Prefeito 2026 com cerimônia oficial no Estádio da Baixada e primeiros jogos.

### Palavras-chave ###
Cristal, Copa Prefeito 2026, futebol amador, Estádio da Baixada, esporte regional, Costa Doce, Sul do RS
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
                "decisao_motivo": "Sem angulação configurada — descartado",
            }
        else:
            angul = PAUTA_ANGULADA[h]

        # Quota: max 10 PUBLICAR/dia (regra 14)
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
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
