#!/usr/bin/env python3
"""
angular_dia_2026_05_20.py — angulação editorial + redação (cowork-faz-tudo).

Lê state/aprovadas_2026-05-20.json, gera state/pauta_2026-05-20.json com
angulação + decisao_final, e escreve state/materias_2026-05-20/<id_hash>.md
para cada item PUBLICAR + materia_longa.

Decisões do dia (14 aprovados):
  PUBLICAR (3): Arambaré cursos, Cristal/Movimento Sul Resiliente, Pelotas/Castramóvel
  REBAIXAR (5): Languiru PF (sensível+fonte agregada), Copa Prefeito Cristal,
                Embrapa Belém (nacional), Copersucar biometano (nacional),
                SUS Venâncio (saúde/nacional)
  BLOQUEAR (6): Emater header, Defesa Civil header, Farsul Flickr,
                Miss Petite Teen (menor), BM tráfico Caxias (menores+distante),
                Caxias discurso de ódio (menores+distante+sensível)
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-05-20"


PAUTA_ANGULADA = {
    # 1. Arambaré cursos gratuitos — PUBLICAR (núcleo)
    "e370728cabf9868c99ea7f3a5323d444ac76d0dd": {
        "titulo_sultv": "Arambaré abre inscrições para cursos gratuitos de qualificação profissional",
        "subtitulo": "Programa municipal oferece capacitação técnica para moradores da Costa Doce, com vagas limitadas.",
        "lead": "A Prefeitura de Arambaré abriu inscrições para cursos gratuitos de qualificação profissional voltados a moradores da cidade. As vagas são limitadas e contemplam diferentes áreas técnicas, com objetivo de ampliar oportunidades de renda na Costa Doce.",
        "ganchos_3": [
            "Vagas gratuitas com inscrição aberta",
            "Capacitação técnica alinhada ao mercado local",
            "Prefeitura amplia política de geração de renda",
        ],
        "angulo_editorial": "Programa público de qualificação em cidade-núcleo da SulTV (Arambaré), com impacto direto na população — pauta de serviço alinhada ao interesse central da audiência.",
        "fontes_complementares_sugeridas": ["FGTAS", "Sine Municipal", "Sebrae RS"],
        "lead_materia_longa": "A Prefeitura de Arambaré, na Costa Doce gaúcha, abriu inscrições para um conjunto de cursos gratuitos de qualificação profissional voltado aos moradores da cidade.",
        "post_instagram": {
            "caption": "Arambaré abriu inscrições para cursos gratuitos de qualificação profissional. Vagas limitadas — quem é da Costa Doce já pode garantir o lugar.",
            "hashtags": ["#Arambaré", "#CostaDoce", "#SulTV", "#Qualificação", "#TrabalhoRS"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Arambaré abre cursos gratuitos.",
            "desenvolvimento_45s": "A Prefeitura de Arambaré está com inscrições abertas para cursos gratuitos de qualificação profissional. As vagas são limitadas e distribuídas em diferentes áreas técnicas, alinhadas às oportunidades de trabalho na Costa Doce. O programa faz parte da política municipal de geração de renda e busca ampliar a empregabilidade dos moradores em setores como comércio, serviços e cadeia produtiva regional.",
            "fechamento_8s": "Inscrições limitadas — moradores devem procurar a Prefeitura.",
            "cta_5s": "Acompanhe a íntegra no SulTV.",
            "trilha_sugerida": "instrumental otimista",
        },
        "tag_thumbnail": "Vagas gratuitas em Arambaré",
        "briefing_visual": {
            "descricao_pt": "Sala de aula de curso profissionalizante com adultos em formação técnica, ambiente de capacitação em cidade pequena do Sul do RS, sem rostos em close",
            "query_en": ["vocational training classroom brazil", "adult professional course workshop", "skills training class"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "Wide shot of an adult vocational training classroom in a small southern Brazilian town, people learning practical technical skills, warm natural daylight, no readable text, no logos, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cidade-núcleo (Arambaré) com fato de serviço público — conteúdo prioritário",
    },

    # 2. Languiru / Polícia Federal — REBAIXAR (sensível + fonte agregada)
    "25db344f0621bedb066565f715492b18d6a53b82": {
        "titulo_sultv": "Investigação sobre a Languiru avança com auditoria entregue ao Ministério Público",
        "subtitulo": "Apuração da Polícia Federal tem desdobramentos; tema exige confirmação em fontes primárias antes de publicação.",
        "lead": "A Polícia Federal avança em investigação envolvendo a cooperativa Languiru, após auditoria ser entregue ao Ministério Público. O caso é sensível e a fonte coletada agrega múltiplas manchetes — requer checagem direta com PF/MP antes de matéria longa.",
        "ganchos_3": [
            "Auditoria entregue ao Ministério Público",
            "Investigação em andamento",
            "Tema econômico de grande cooperativa gaúcha",
        ],
        "angulo_editorial": "Pauta econômica relevante (grande cooperativa do RS), mas com sourcing agregado/confuso e natureza de investigação criminal em curso. Conservar como nota interna e confirmar em fontes oficiais (PF/MP) antes de qualquer publicação. Presunção de inocência.",
        "fontes_complementares_sugeridas": ["Polícia Federal", "Ministério Público", "Assessoria Languiru"],
        "lead_materia_longa": "",
        "post_instagram": {},
        "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Investigação criminal em curso com sourcing agregado/confuso — exige confirmação em fontes primárias antes de publicar; flag para revisão humana",
    },

    # 3. Cristal — Movimento Sul Resiliente — PUBLICAR (núcleo, clima)
    "8f012b6b663e922efd2e3e46ca8ef2dbfd09589a": {
        "titulo_sultv": "Cristal sedia reunião do Movimento Sul Resiliente e recebe estudo de prevenção de desastres",
        "subtitulo": "Encontro na Câmara Municipal debateu adaptação climática e entregou mapeamento de áreas de risco.",
        "lead": "A Câmara Municipal de Cristal recebeu encontro do Movimento Sul Resiliente, que debateu ações de adaptação climática e entregou ao município um estudo de mapeamento voltado à prevenção de desastres. A iniciativa reforça a agenda de resiliência no Sul do Rio Grande do Sul.",
        "ganchos_3": [
            "Estudo de mapeamento de risco entregue ao município",
            "Adaptação climática na pauta da Câmara",
            "Costa Doce avança em prevenção de desastres",
        ],
        "angulo_editorial": "Pauta de resiliência climática em cidade-núcleo (Cristal), com forte ressonância pós-enchentes de 2024 no RS. Combina ciência aplicada, gestão pública e segurança comunitária — interesse central da audiência regional.",
        "fontes_complementares_sugeridas": ["Defesa Civil RS", "Movimento Sul Resiliente", "Sema RS"],
        "lead_materia_longa": "A Câmara Municipal de Cristal, no Sul do Rio Grande do Sul, recebeu reunião do Movimento Sul Resiliente.",
        "post_instagram": {
            "caption": "Cristal recebeu o Movimento Sul Resiliente: encontro debateu adaptação climática e entregou ao município um estudo de mapeamento para prevenção de desastres.",
            "hashtags": ["#Cristal", "#CostaDoce", "#SulTV", "#Resiliência", "#Clima", "#PrevençãoDeDesastres"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal aposta em resiliência.",
            "desenvolvimento_45s": "A Câmara Municipal de Cristal recebeu encontro do Movimento Sul Resiliente, que debateu ações de adaptação climática e entregou ao município um estudo de mapeamento para prevenção de desastres. A iniciativa fortalece a capacidade da cidade de antecipar riscos e proteger a população, em uma agenda que ganhou urgência no Rio Grande do Sul após os eventos climáticos extremos dos últimos anos.",
            "fechamento_8s": "Mapeamento orienta ações de prevenção na Costa Doce.",
            "cta_5s": "Cobertura completa no SulTV.",
            "trilha_sugerida": "instrumental sóbrio e esperançoso",
        },
        "tag_thumbnail": "Cristal mapeia o risco",
        "briefing_visual": {
            "descricao_pt": "Reunião em câmara municipal do interior gaúcho com pessoas debatendo em mesa e mapas de prevenção de desastres, Cristal/RS, sem rostos identificáveis",
            "query_en": ["city council meeting brazil", "climate adaptation planning meeting", "flood risk map table"],
            "evitar": ["rostos identificáveis", "logos partidários", "bandeiras de partido", "texto"],
            "prompt_ia": "Wide editorial shot of a municipal council chamber meeting in a small southern Brazilian town discussing climate resilience and flood prevention, risk maps on the table, daylight through windows, no readable text, no logos, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cidade-núcleo (Cristal) + agenda de resiliência climática de alto interesse regional",
    },

    # 4. Pelotas — Castramóvel — PUBLICAR (serviço, Costa Doce ampliada)
    "32fa7b18a1d1dc1f7406f06e90b3c9aaf9b32701": {
        "titulo_sultv": "Castramóvel de Pelotas atende Passo do Salso e Vila Governaço com 200 vagas",
        "subtitulo": "Cadastro para castração gratuita de cães e gatos vai de 25 a 29 de maio nos dois bairros.",
        "lead": "A Prefeitura de Pelotas levará o Castramóvel aos bairros Passo do Salso e Vila Governaço, com 200 vagas para castração gratuita de cães e gatos. O cadastro dos interessados será realizado entre os dias 25 e 29 de maio.",
        "ganchos_3": [
            "200 vagas para castração gratuita",
            "Cadastro de 25 a 29 de maio",
            "Atendimento itinerante chega a dois bairros",
        ],
        "angulo_editorial": "Pauta de serviço público em Pelotas (Costa Doce ampliada), com dados concretos (200 vagas, datas e bairros) — utilidade direta para a audiência urbana, com viés de saúde animal e controle populacional.",
        "fontes_complementares_sugeridas": ["Secretaria de Qualidade Ambiental de Pelotas", "CRMV-RS"],
        "lead_materia_longa": "A Prefeitura de Pelotas levará o Castramóvel aos bairros Passo do Salso e Vila Governaço, com 200 vagas de castração gratuita.",
        "post_instagram": {
            "caption": "Castramóvel chega ao Passo do Salso e à Vila Governaço, em Pelotas, com 200 vagas de castração gratuita. Cadastro de 25 a 29 de maio.",
            "hashtags": ["#Pelotas", "#CostaDoce", "#SulTV", "#Castramóvel", "#SaúdeAnimal", "#ProteçãoAnimal"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Castração gratuita em Pelotas.",
            "desenvolvimento_45s": "A Prefeitura de Pelotas vai levar o Castramóvel aos bairros Passo do Salso e Vila Governaço, com 200 vagas para castração gratuita de cães e gatos. O cadastro dos interessados será feito entre os dias 25 e 29 de maio. O programa contribui para o controle populacional de animais e para a saúde pública, reduzindo o abandono e os riscos sanitários associados.",
            "fechamento_8s": "Vagas limitadas — cadastro entre 25 e 29 de maio.",
            "cta_5s": "Detalhes e endereços no SulTV.",
            "trilha_sugerida": "leve e amigável",
        },
        "tag_thumbnail": "Castramóvel em Pelotas",
        "briefing_visual": {
            "descricao_pt": "Unidade móvel veterinária (van branca de saúde animal) atendendo em bairro residencial de Pelotas, sem pessoas identificáveis",
            "query_en": ["mobile veterinary clinic van", "animal castration mobile unit", "pet spay neuter mobile clinic"],
            "evitar": ["rostos identificáveis", "marcas comerciais", "texto", "logos"],
            "prompt_ia": "Wide shot of a white mobile veterinary clinic van parked in a residential neighborhood of a southern Brazilian city, animal health service unit, daytime, no readable text, no logos, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público em Pelotas (Costa Doce ampliada) com dados concretos — alta utilidade para a audiência",
    },

    # 5. Copa Prefeito 2026 (Cristal) — REBAIXAR (esporte amador secundário; quota/qualidade)
    "e04af26ff80167353fa5704d59d6095acaa86096": {
        "titulo_sultv": "Cristal abre Copa Prefeito 2026 com cerimônia no Estádio da Baixada",
        "subtitulo": "Competição de futebol amador reúne equipes locais na temporada.",
        "lead": "A Copa Prefeito 2026 de Cristal foi aberta no Estádio da Baixada, com cerimônia e os primeiros jogos da fase inicial, mobilizando equipes amadoras da cidade.",
        "ganchos_3": [
            "Abertura oficial no Estádio da Baixada",
            "Equipes amadoras na temporada",
            "Esporte como vetor de comunidade em Cristal",
        ],
        "angulo_editorial": "Esporte amador em cidade-núcleo (Cristal) — pauta de comunidade legítima, porém secundária frente à pauta de resiliência climática da mesma cidade já priorizada hoje. Vira nota/post.",
        "fontes_complementares_sugeridas": ["Liga Pelotense"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Começou em Cristal a Copa Prefeito 2026: cerimônia oficial e primeiros jogos no Estádio da Baixada marcaram a abertura.",
            "hashtags": ["#Cristal", "#CopaPrefeito", "#FutebolAmador", "#CostaDoce", "#SulTV"],
        },
        "roteiro_short_60s": {},
        "tag_thumbnail": "Copa Prefeito começou",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Esporte amador secundário; Cristal já tem pauta prioritária (resiliência) no dia — usar como post/nota",
    },

    # 6. Embrapa Belém — REBAIXAR (nacional/distante)
    "f3ef6e32be17f92059396cc9c0d1198d2c81a63a": {
        "titulo_sultv": "Embrapa abre floresta urbana em Belém para expedição científica",
        "subtitulo": "Ação integra a Semana Nacional da Biodiversidade com ciência cidadã.",
        "lead": "A Embrapa abre uma floresta urbana em Belém (PA) para expedição científica de registro de fauna, flora e fungos, dentro da Semana Nacional da Biodiversidade.",
        "ganchos_3": ["Ciência cidadã em ação", "Semana Nacional da Biodiversidade", "Embrapa e biodiversidade urbana"],
        "angulo_editorial": "Pauta nacional/Norte sem ancoragem Sul-RS. Mantém como nota interna de referência em ciência/agro.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {},
        "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Pauta nacional (Belém/PA) sem leitura regional Sul-RS",
    },

    # 7. Emater INFORMAÇÕES AGROPECUÁRIAS — BLOQUEAR (cabeçalho de seção)
    "e914edb4101909198de490e19b4ee3ebeb063e57": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Título é cabeçalho de seção do site Emater ('INFORMAÇÕES AGROPECUÁRIAS') — coletor pegou menu, não matéria",
    },

    # 8. Defesa Civil Avisos e Alertas — BLOQUEAR (cabeçalho de seção)
    "72da33ff967bd936651054a9f0405448f2ba54dd": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Cabeçalho de seção da Defesa Civil ('Avisos e Alertas / Dicas de prevenção') com conteúdo procedural antigo — não é matéria",
    },

    # 9. Farsul Fotos do Flickr — BLOQUEAR (galeria)
    "54da86550dbad394c36708a7a9c2f7ad94d48e38": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Agregador de fotos do Flickr (Farsul) — não é matéria",
    },

    # 10. Copersucar biometano — REBAIXAR (nacional)
    "d1d93bf71ca273d885626f17d7f7f2fb2cf3f0f4": {
        "titulo_sultv": "Copersucar planeja frota de logística 100% movida a biometano",
        "subtitulo": "Iniciativa prevê redução de 90% nas emissões e ganho de competitividade.",
        "lead": "A Copersucar anunciou plano para operar 100% de sua frota logística com biometano, em iniciativa que pode reduzir 90% das emissões de gases poluentes e ampliar competitividade frente aos preços do petróleo.",
        "ganchos_3": ["90% menos emissões", "Frota 100% biometano", "Descarbonização do sucroalcooleiro"],
        "angulo_editorial": "Caso nacional do setor sucroalcooleiro — sem ângulo Sul-RS direto. Referência futura em conteúdo de inovação e descarbonização do agro.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {},
        "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Pauta nacional sem ancoragem Sul-RS — nota interna para referência (carbono/inovação)",
    },

    # 11. Miss Brasil Petite Teen — BLOQUEAR (menor)
    "d604261fbe0b0508c9333d8cd6860fee59da6567": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Guardrail: conteúdo envolvendo menor (concurso com adolescente de 17 anos)",
    },

    # 12. SUS Venâncio — REBAIXAR (saúde/nacional, fraco regional)
    "6a388e87ad73367632fdb32b5f83443de2646036": {
        "titulo_sultv": "Venâncio Aires busca ampliar recursos do SUS em audiência no Ministério da Saúde",
        "subtitulo": "Pauta principal foi o aumento do teto de Média e Alta Complexidade (MAC).",
        "lead": "Comitiva de Venâncio Aires foi recebida no Ministério da Saúde para tratar de alternativas de ampliação de recursos do SUS, com foco no aumento do teto de Média e Alta Complexidade.",
        "ganchos_3": ["Teto MAC em discussão", "Comitiva no Ministério da Saúde", "Financiamento do SUS no interior"],
        "angulo_editorial": "Pauta de financiamento de saúde com viés nacional e cidade fora do núcleo SulTV (Venâncio Aires). Ângulo regional fraco — nota interna.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {},
        "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Financiamento do SUS com viés nacional e cidade fora do núcleo — ancoragem regional fraca",
    },

    # 13. BM tráfico Caxias — BLOQUEAR (crime distante + menores)
    "9f3c46c3d2f5a5bb07cb6f10d7dab9705a464dbf": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Crime/polícia em região distante (Serra/Caxias) e apreensão de menores — fora do território e guardrail de menores",
    },

    # 14. Caxias discurso de ódio — BLOQUEAR (crime distante + menores + ideológico)
    "e11f90fce4a2862c9a49a1f6390320d767003a66": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Crime/justiça em região distante (Caxias), envolvendo menores e tema ideológico sensível (discurso de ódio) — fora do território e múltiplos guardrails",
    },
}


MATERIAS = {
    # Arambaré cursos
    "e370728cabf9868c99ea7f3a5323d444ac76d0dd": """### Título ###
Arambaré abre inscrições para cursos gratuitos de qualificação profissional na Costa Doce

### Artigo ###
A Prefeitura de Arambaré, no Sul do Rio Grande do Sul, abriu inscrições para um pacote de cursos gratuitos de qualificação profissional voltado para moradores da cidade. As vagas são limitadas e contemplam diferentes áreas técnicas, com aulas previstas para iniciar nas próximas semanas em espaço cedido pelo poder público municipal. A iniciativa integra a estratégia da gestão para ampliar oportunidades de renda na Costa Doce, região marcada pela combinação entre economia rural, turismo de praia e pesca artesanal. Ao oferecer capacitação sem custo, o município busca conectar a mão de obra local a setores em demanda, como comércio, serviços e cadeia produtiva. A medida também responde à sazonalidade da economia em Arambaré, em que a oferta de trabalho varia ao longo do ano, e tenta reduzir a dependência de períodos específicos como o veraneio. Para se inscrever, os interessados devem procurar a Secretaria responsável pela política de trabalho e renda na Prefeitura. A documentação e os critérios de seleção estão disponíveis nos canais oficiais do município. Cursos gratuitos de qualificação profissional vêm sendo apontados como uma das ferramentas mais efetivas para melhorar a empregabilidade em cidades pequenas, sobretudo quando articulados com instituições parceiras e com as demandas reais do mercado regional. A expectativa da Prefeitura é que o programa se consolide como ciclo permanente, integrando novas turmas ao longo do ano. A iniciativa reforça o protagonismo de Arambaré na pauta de desenvolvimento humano da Costa Doce e mostra a preocupação do poder público com a geração de renda em uma região estratégica para o Sul do estado.

### Legenda sugerida ###
Prefeitura de Arambaré abre vagas em cursos gratuitos de qualificação profissional para moradores da Costa Doce.

### Palavras-chave ###
Arambaré, cursos gratuitos, qualificação profissional, Costa Doce, geração de renda, Prefeitura de Arambaré, Sul do RS
""",

    # Cristal - Movimento Sul Resiliente
    "8f012b6b663e922efd2e3e46ca8ef2dbfd09589a": """### Título ###
Cristal sedia reunião do Movimento Sul Resiliente e recebe estudo de prevenção de desastres

### Artigo ###
A Câmara Municipal de Cristal, no Sul do Rio Grande do Sul, recebeu encontro do Movimento Sul Resiliente, que debateu ações de adaptação climática e entregou ao município um estudo de mapeamento voltado à prevenção de desastres. A reunião reuniu representantes do poder público, técnicos e lideranças comunitárias em torno de uma agenda que ganhou centralidade no estado após os eventos climáticos extremos dos últimos anos. O estudo entregue tem caráter prático: identifica áreas mais expostas a inundações, deslizamentos e outros eventos, oferecendo base técnica para que a gestão municipal possa planejar obras, sistemas de alerta e protocolos de evacuação. Esse tipo de mapeamento é considerado peça-chave da chamada gestão de riscos, que substitui a lógica de resposta emergencial por uma cultura de prevenção e antecipação. Para uma cidade da Costa Doce, cercada por áreas rurais e cursos d'água, dispor de um diagnóstico atualizado significa ganhar tempo e precisão na hora de proteger vidas e patrimônio. O Movimento Sul Resiliente articula municípios, universidades e entidades em torno da adaptação climática, partindo do reconhecimento de que o Rio Grande do Sul precisa se preparar para um cenário de eventos mais frequentes e intensos. A iniciativa em Cristal soma-se a esforços de outras cidades gaúchas que buscam transformar lições recentes em políticas públicas estruturadas. Ao receber o estudo, o município passa a ter um instrumento concreto para orientar decisões de infraestrutura, uso do solo e investimento em sistemas de monitoramento. A expectativa é que o diagnóstico se desdobre em ações de curto e médio prazo, integrando a Defesa Civil municipal e a comunidade na construção de uma cidade mais preparada para enfrentar emergências.

### Legenda sugerida ###
Movimento Sul Resiliente entrega a Cristal estudo de mapeamento para prevenção de desastres e debate adaptação climática.

### Palavras-chave ###
Cristal, Movimento Sul Resiliente, adaptação climática, prevenção de desastres, resiliência, Costa Doce, Sul do RS, Defesa Civil
""",

    # Pelotas - Castramóvel
    "32fa7b18a1d1dc1f7406f06e90b3c9aaf9b32701": """### Título ###
Castramóvel de Pelotas atende Passo do Salso e Vila Governaço com 200 vagas de castração gratuita

### Artigo ###
A Prefeitura de Pelotas vai levar o Castramóvel aos bairros Passo do Salso e Vila Governaço, com 200 vagas para castração gratuita de cães e gatos. O cadastro dos interessados será realizado entre os dias 25 e 29 de maio, e as vagas são limitadas. O serviço integra a política municipal de bem-estar e controle populacional animal, conduzida pela área de qualidade ambiental. A castração gratuita é uma das ferramentas mais eficientes no combate ao abandono e à superpopulação de animais nas cidades. Ao impedir ninhadas indesejadas, o procedimento reduz o número de animais em situação de rua, diminui riscos sanitários para a população e alivia a pressão sobre protetores independentes e organizações de defesa animal, que costumam operar no limite da capacidade. A escolha de bairros específicos para cada etapa do programa busca democratizar o acesso, levando o atendimento a regiões onde a demanda é alta e a oferta de serviços veterinários acessíveis é menor. O modelo itinerante, com a unidade móvel, permite atender comunidades que dificilmente se deslocariam a uma clínica central. Para participar, os tutores precisam realizar o cadastro dentro do prazo, respeitando os critérios definidos pela Prefeitura quanto a peso, idade e condições de saúde dos animais. As orientações sobre jejum, transporte e cuidados pós-operatórios costumam ser repassadas no momento do cadastro. Programas como esse vêm sendo ampliados em diversas cidades gaúchas como resposta estruturada a um problema crônico de saúde pública e proteção animal. Em Pelotas, a continuidade do Castramóvel sinaliza que o controle populacional deixou de ser ação pontual para se tornar política permanente, com cronograma rotativo entre bairros.

### Legenda sugerida ###
Castramóvel de Pelotas oferece 200 vagas de castração gratuita no Passo do Salso e na Vila Governaço; cadastro de 25 a 29 de maio.

### Palavras-chave ###
Pelotas, Castramóvel, castração gratuita, saúde animal, proteção animal, controle populacional, Costa Doce, Sul do RS
""",
}


def main():
    apr_path = ROOT / "state" / f"aprovadas_{HOJE}.json"
    pauta_path = ROOT / "state" / f"pauta_{HOJE}.json"
    materias_dir = ROOT / "state" / f"materias_{HOJE}"

    data = json.loads(apr_path.read_text(encoding="utf-8"))
    apr_list = data.get("aprovadas") or data.get("curadas") or []

    pauta = []
    pub_long = 0
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

        if angul["decisao_final"] == "PUBLICAR" and pub_long >= 10:
            angul = {**angul, "decisao_final": "REBAIXAR", "decisao_motivo": "Quota diária esgotada"}
        if angul["decisao_final"] == "PUBLICAR":
            pub_long += 1

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
            else:
                print(f"[angular] AVISO: PUBLICAR materia_longa sem corpo: {p['id_hash']}")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
