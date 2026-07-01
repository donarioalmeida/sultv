"""
Angulação editorial — 2026-06-14
Gerado autonomamente pelo Cowork (scheduled task sultv-radar-pauta-diaria)
"""
import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).parent.parent
STATE = REPO / "state"
MATERIAS_DIR = STATE / "materias_2026-06-14"
MATERIAS_DIR.mkdir(exist_ok=True)
DATE = "2026-06-14"

# ──────────────────────────────────────────────
# PAUTA ANGULADA — 10 PUBLICAR / 17 REBAIXAR / 15 BLOQUEAR
# ──────────────────────────────────────────────
PAUTA_ANGULADA = [
    {
        "id_hash": "882edeb88f0be982907d48640a98bb6fe38fa6b1",
        "titulo": "Camaquã lança Campanha do Agasalho 2026; saiba como colaborar",
        "cidade": "Camaquã",
        "fonte_nome": "Rádio Acústica FM — Costa Doce",
        "url_fonte": "https://acusticafm.com.br/camaqua-lanca-campanha-agasalho-2026-colaborar/",
        "score_editorial": 10,
        "score_combinado": 22.0,
        "tag_principal": "comunidade",
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Camaquã lança Campanha do Agasalho 2026 com foco em autonomia das famílias",
        "subtitulo": "Secretaria apresenta ações para enfrentar o inverno e apoiar famílias vulneráveis no município",
        "lead": "Camaquã iniciou nesta semana a Campanha do Agasalho 2026, com ações voltadas ao enfrentamento do inverno e à promoção da autonomia das famílias atendidas pela rede de assistência social do município.",
        "chamada_faixa": "AGASALHO 2026 EM CAMAQUÃ",
        "ganchos_3": [
            "Como colaborar com a arrecadação de agasalhos em Camaquã",
            "Ações da Secretaria para autonomia de famílias vulneráveis no inverno",
            "Campanha chega à Costa Doce para aquecer quem mais precisa"
        ],
        "angulo_editorial": "Inverno chegando no Sul do RS, Camaquã mobiliza solidariedade. Ênfase na inovação da abordagem — autonomia das famílias, não só doação de roupas.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Assistência Social de Camaquã", "Defesa Civil Municipal"],
        "lead_materia_longa": "Com o inverno se estabelecendo no Sul do Rio Grande do Sul, a Prefeitura de Camaquã lançou a Campanha do Agasalho 2026. A iniciativa vai além da arrecadação de roupas e cobertores: o Secretário Fabiano Ribeiro apresentou ações que buscam promover a autonomia das famílias atendidas pela rede de assistência social do município.",
        "post_instagram": {
            "caption": "Camaquã está com a Campanha do Agasalho 2026 em andamento! Solidariedade que aquece o inverno na Costa Doce. Saiba como colaborar. #Camaquã #AgasalhoCamaquã #CostadoçeRS #SolidariedadeRS",
            "hashtags": ["Camaquã", "AgasalhoCamaquã", "CostadoceRS", "SolidariedadeRS", "InvernoRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Camaquã tem campanha do agasalho 2026!",
            "desenvolvimento_45s": "A prefeitura de Camaquã lançou esta semana a Campanha do Agasalho 2026. O secretário Fabiano Ribeiro apresentou ações que vão além da doação de roupas — o objetivo é também promover a autonomia das famílias atendidas no inverno gaúcho. A Costa Doce se mobiliza para aquecer quem mais precisa.",
            "fechamento_8s": "Solidariedade em ação no Sul do RS. Confira como contribuir.",
            "cta_5s": "Segue a SulTV para mais notícias da Costa Doce.",
            "trilha_sugerida": "suave, emotivo"
        },
        "tag_thumbnail": "AGASALHO 2026",
        "briefing_visual": {
            "descricao_pt": "Agasalhos e cobertores coloridos empilhados em ponto de coleta, ambiente interno, sem texto, sem pessoas identificáveis",
            "query_en": ["winter clothes donation pile brazil", "warm clothing charity collection"],
            "evitar": ["texto sobreposto", "logos de marcas", "faces identificáveis"],
            "prompt_ia": "Colorful pile of winter coats, sweaters and blankets in a donation collection point, warm lighting, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Campanha de inverno em cidade-núcleo com abordagem inovadora (autonomia familiar). Fato concreto, fonte institucional."
    },
    {
        "id_hash": "5b7dd5a19fab42dfa2fa1abff1b84af7bb5b3381",
        "titulo": "Vereador Vladimir Tili aciona Anatel por falhas da TIM em Camaquã e região",
        "cidade": "Camaquã",
        "fonte_nome": "Rádio Acústica FM — Costa Doce",
        "url_fonte": "https://acusticafm.com.br/vereador-vladimir-aciona-tim-camaqua-e-regiao/",
        "score_editorial": 10,
        "score_combinado": 21.0,
        "tag_principal": "politica_local",
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Vereador aciona Anatel contra falhas de internet e telefonia da TIM em Camaquã e região",
        "subtitulo": "Solicitação encaminhada ao órgão regulador pede esclarecimentos e medidas para reduzir interrupções na rede",
        "lead": "O vereador Vladimir Tili encaminhou solicitação à Anatel exigindo esclarecimentos e providências sobre as recorrentes falhas de telefonia móvel e internet da TIM em Camaquã e nos municípios da região.",
        "chamada_faixa": "CÂMARA ACIONA ANATEL CONTRA A TIM",
        "ganchos_3": [
            "Moradores de Camaquã relatam falhas constantes de sinal da TIM",
            "Anatel deve investigar e exigir providências da operadora",
            "Problema afeta não apenas Camaquã mas cidades vizinhas da Costa Doce"
        ],
        "angulo_editorial": "Ação fiscalizatória do legislativo local em defesa dos consumidores — narrativa de vereador trabalhando pelos cidadãos. Relevante para toda a região que depende de conectividade.",
        "fontes_complementares_sugeridas": ["Câmara Municipal de Camaquã", "Anatel — Canal de Atendimento"],
        "lead_materia_longa": "O vereador Vladimir Tili protocolou solicitação junto à Agência Nacional de Telecomunicações, a Anatel, cobrando providências contra as falhas recorrentes no serviço de telefonia móvel e internet da TIM em Camaquã e nas cidades da região. A ação legislativa busca esclarecimentos sobre as causas das interrupções e medidas concretas para reduzir os problemas de conectividade que afetam moradores e produtores rurais.",
        "post_instagram": {
            "caption": "Câmara de Camaquã aciona a Anatel pelas falhas da TIM na região. O vereador Vladimir Tili entrou em ação pelos consumidores da Costa Doce. #Camaquã #Anatel #TIM #CostadoceRS",
            "hashtags": ["Camaquã", "Anatel", "TIM", "CostadoceRS", "TelecomRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "TIM com problemas em Camaquã? Vereador foi à Anatel!",
            "desenvolvimento_45s": "O vereador Vladimir Tili acionou a Anatel contra as falhas de telefonia e internet da TIM em Camaquã e região. A solicitação pede esclarecimentos e medidas concretas para reduzir as interrupções que prejudicam moradores e produtores rurais da Costa Doce.",
            "fechamento_8s": "Câmara cobra da Anatel respostas para o consumidor da Costa Doce.",
            "cta_5s": "Segue a SulTV para acompanhar a resposta da Anatel.",
            "trilha_sugerida": "corporativo, direto"
        },
        "tag_thumbnail": "TIM NA ANATEL",
        "briefing_visual": {
            "descricao_pt": "Torre de telecomunicações em área rural, céu com nuvens ao fundo, sem texto, paisagem gaúcha",
            "query_en": ["cell tower rural brazil", "telecommunications antenna countryside"],
            "evitar": ["logos de operadoras", "texto", "faces identificáveis"],
            "prompt_ia": "Cell phone tower in rural southern Brazil landscape, overcast sky, grassy fields, no text, no logos, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Ação concreta do legislativo municipal em cidade-núcleo sobre problema que afeta toda a região. Alta relevância para consumidores."
    },
    {
        "id_hash": "545abfde72ea5629e9fe58fcd3b8ab6a3f9952dc",
        "titulo": "⚠️ Devido às condições climáticas adversas, a ação de coleta gratuita de eletrônicos que aconteceria nesta sexta-feira (12/06) foi cancelada",
        "cidade": "Tapes",
        "fonte_nome": "Instagram @prefeituradetapes",
        "url_fonte": "https://www.instagram.com/p/DZfj27RuP5l/",
        "score_editorial": 10,
        "score_combinado": 18.0,
        "tag_principal": "serviço",
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "Coleta de eletrônicos em Tapes é adiada por condições climáticas",
        "subtitulo": "Prefeitura promete nova data para descarte correto de resíduos eletrônicos na comunidade",
        "lead": "A ação de coleta gratuita de resíduos eletrônicos prevista para esta sexta-feira (13/06) em Tapes foi cancelada por condições climáticas adversas. A prefeitura informará em breve a nova data.",
        "chamada_faixa": "COLETA DE ELETRÔNICOS ADIADA",
        "ganchos_3": ["Chuvas intensas no Sul forçam cancelamento", "Nova data em breve — Tapes promete comunicar moradores"],
        "angulo_editorial": "Serviço de utilidade pública adiado — nota de serviço para a comunidade de Tapes.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Atenção Tapes! A coleta de eletrônicos desta sexta foi adiada por conta das chuvas. Fique ligado para a nova data. #Tapes #DescarteCerto #ResiduosEletronicos",
            "hashtags": ["Tapes", "DescarteCerto", "ResiduosEletronicos"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Coleta de eletrônicos em Tapes foi adiada!",
            "desenvolvimento_45s": "Por conta do tempo ruim no Sul do RS, a ação de coleta gratuita de resíduos eletrônicos prevista para esta sexta em Tapes foi cancelada. A prefeitura deve divulgar em breve a nova data para o descarte correto.",
            "fechamento_8s": "Fique atento às redes da prefeitura de Tapes.",
            "cta_5s": "SulTV traz todas as novidades da Costa Doce.",
            "trilha_sugerida": "informativo"
        },
        "tag_thumbnail": "COLETA ADIADA TAPES",
        "briefing_visual": {
            "descricao_pt": "Caixas com aparelhos eletrônicos usados aguardando descarte, sem pessoas identificáveis, sem texto",
            "query_en": ["electronic waste collection boxes", "e-waste recycling"],
            "evitar": ["logos", "texto", "faces identificáveis"],
            "prompt_ia": "Cardboard boxes filled with old electronic devices ready for recycling, clean background, no text, no faces, editorial style"
        },
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Notícia de cancelamento de evento passado (12/06 foi ontem). Sem valor de pauta para hoje (14/06). Nova data ainda não divulgada — nada concreto para publicar."
    },
    {
        "id_hash": "a3533cde66a8c4980dc360e776b8a90f9bd35335",
        "titulo": "PREFEITO RECEBE REPRESENTANTE DA COLÔNIA DOS PESCADORES Z-43 PARA TRATAR DE MEDIDAS PREVENTIVAS",
        "cidade": "Tapes",
        "fonte_nome": "Instagram @prefeituradetapes",
        "url_fonte": "https://www.instagram.com/p/DZfJAomPaIl/",
        "score_editorial": 10,
        "score_combinado": 21.5,
        "tag_principal": "clima",
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Tapes: prefeitura e pescadores da Z-43 se reúnem para planejar ações preventivas diante da cheia",
        "subtitulo": "Prefeito Luiz Carlos Garcez recebe colônia de pescadores para discutir riscos de elevação das águas no período de chuvas",
        "lead": "A prefeitura de Tapes recebeu a representante da Colônia dos Pescadores Z-43, Kelly Rigon, para debater medidas preventivas diante do aumento das chuvas e da possível elevação do nível das águas que pode impactar a comunidade pesqueira do município.",
        "chamada_faixa": "TAPES SE PREPARA PARA A CHEIA",
        "ganchos_3": [
            "Colônia Z-43 articula com prefeitura para proteger pescadores na época de chuvas",
            "Nível das águas preocupa produtores e famílias da zona pesqueira de Tapes",
            "Costa Doce em alerta: chuvas intensas pedem planejamento preventivo"
        ],
        "angulo_editorial": "Narrativa de preparação preventiva — prefeitura agindo proativamente antes da cheia, valorizando a parceria com comunidade pesqueira. Âncora forte: Z-43, identidade da Costa Doce.",
        "fontes_complementares_sugeridas": ["Prefeitura Municipal de Tapes", "Colônia dos Pescadores Z-43", "Defesa Civil de Tapes"],
        "lead_materia_longa": "O prefeito de Tapes, Luiz Carlos Coutinho Garcez, recebeu nesta semana Kelly Rigon, representante da Colônia dos Pescadores Z-43, para uma reunião sobre ações preventivas diante do período de chuvas intensas e da possível elevação do nível das águas que ameaçam a comunidade pesqueira. A Costa Doce registrou aumento de precipitações nos últimos dias, e a articulação entre a prefeitura e as entidades locais busca minimizar os impactos sobre as famílias que vivem da pesca.",
        "post_instagram": {
            "caption": "Tapes se prepara! Prefeitura e Colônia Z-43 juntas para proteger pescadores diante da chuva e elevação das águas. #Tapes #PescadoresRS #CostaDoce #PrevenCAO",
            "hashtags": ["Tapes", "PescadoresRS", "CostaDoce", "DefesaCivil", "ChuvaRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tapes se prepara para o período de chuvas!",
            "desenvolvimento_45s": "O prefeito de Tapes recebeu a representante da Colônia dos Pescadores Z-43 para planejar ações preventivas. Com as chuvas intensas e o risco de elevação das águas, prefeitura e pescadores articulam juntos para proteger a comunidade pesqueira da Costa Doce.",
            "fechamento_8s": "Prevenção em ação no litoral sul gaúcho.",
            "cta_5s": "Acompanhe a SulTV para mais do litoral do Sul.",
            "trilha_sugerida": "climático, tenso mas esperançoso"
        },
        "tag_thumbnail": "CHEIA EM TAPES",
        "briefing_visual": {
            "descricao_pt": "Barcos de pesca no estuário da Lagoa dos Patos com céu nublado e água escura, sem texto, sem pessoas identificáveis",
            "query_en": ["fishing boats lake southern brazil", "lagoa dos patos fishermen boats"],
            "evitar": ["texto", "faces identificáveis", "propaganda política"],
            "prompt_ia": "Small fishing boats moored on a wide brown lake under overcast skies in southern Brazil, calm water, no people visible, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Reunião preventiva concreta entre prefeitura e colônia Z-43 (identidade forte Costa Doce). Alta relevância diante do contexto de chuvas. Cidade-núcleo."
    },
    {
        "id_hash": "2346e7997cb81be47d84ad1d21d435d66b68344f",
        "titulo": "⚽️ COMUNICADO OFICIAL",
        "cidade": "Arambaré",
        "fonte_nome": "Instagram @prefeituradearambare",
        "url_fonte": "https://www.instagram.com/p/DZfWd2gxX85/",
        "score_editorial": 10,
        "score_combinado": 16.0,
        "tag_principal": "esporte",
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "17ª Copa Santa Rita tem rodada deste domingo cancelada em Arambaré",
        "subtitulo": "",
        "lead": "",
        "chamada_faixa": "COPA CANCELADA EM ARAMBARÉ",
        "ganchos_3": [],
        "angulo_editorial": "Cancelamento de partida — sem fato novo, só aviso. Não agrega valor editorial.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {"abertura_2s": "", "desenvolvimento_45s": "", "fechamento_8s": "", "cta_5s": "", "trilha_sugerida": ""},
        "tag_thumbnail": "",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Apenas aviso de cancelamento de partida de futebol local sem nova data divulgada. Sem valor editorial."
    },
    {
        "id_hash": "394b624e90eb180abfce5ed085d50699b0cba0cf",
        "titulo": "💉 VACINA DA GRIPE LIBERADA PARA TODA A POPULAÇÃO!",
        "cidade": "Arambaré",
        "fonte_nome": "Instagram @prefeituradearambare",
        "url_fonte": "https://www.instagram.com/p/DZfV3B4R0NF/",
        "score_editorial": 10,
        "score_combinado": 20.0,
        "tag_principal": "saude_publica",
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Arambaré libera vacina da gripe para toda a população a partir desta segunda-feira",
        "subtitulo": "Secretaria de Saúde amplia vacinação para moradores a partir dos 6 meses; atendimento das 8h às 16h",
        "lead": "A partir desta segunda-feira, 15 de junho, a vacina contra a gripe está liberada para toda a população de Arambaré com idade acima de 6 meses, conforme anúncio da Secretaria Municipal de Saúde.",
        "chamada_faixa": "VACINA DA GRIPE PARA TODOS EM ARAMBARÉ",
        "ganchos_3": [
            "Vacinação disponível das 8h às 11h30 e das 13h às 16h",
            "Grupos prioritários continuam sendo vacinados normalmente",
            "Inverno gaúcho: momento ideal para imunização contra influenza"
        ],
        "angulo_editorial": "Serviço público de saúde com impacto direto na comunidade de cidade-núcleo. Muito oportuno com inverno começando. Sem menção a diagnóstico ou tratamento — é acesso a serviço público gratuito.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Saúde de Arambaré"],
        "lead_materia_longa": "A Secretaria Municipal de Saúde de Arambaré informa que, a partir desta segunda-feira, dia 15 de junho, a vacina contra a gripe está liberada para toda a população do município com idade a partir de 6 meses. A vacinação acontece nos horários das 8h às 11h30 e das 13h às 16h, com os grupos prioritários continuando a ser atendidos normalmente.",
        "post_instagram": {
            "caption": "Moradores de Arambaré, atenção! A vacina da gripe está liberada para toda a população a partir desta segunda (15/06). Das 8h às 16h no posto de saúde. #Arambaré #VacinaDaGripe #SaudePublica #CostaDoce",
            "hashtags": ["Arambaré", "VacinaDaGripe", "SaudePublica", "CostaDoce", "InvernoRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Vacina da gripe liberada para todos em Arambaré!",
            "desenvolvimento_45s": "A partir desta segunda-feira, 15 de junho, toda a população de Arambaré com mais de 6 meses pode tomar a vacina contra a gripe. O atendimento é das 8h às 11h30 e das 13h às 16h. Os grupos prioritários continuam sendo vacinados normalmente. Com o inverno chegando, a imunização é essencial.",
            "fechamento_8s": "Procure o posto de saúde de Arambaré e se proteja.",
            "cta_5s": "Segue a SulTV para as novidades da Costa Doce.",
            "trilha_sugerida": "positivo, informativo"
        },
        "tag_thumbnail": "VACINA DA GRIPE ARAMBARÉ",
        "briefing_visual": {
            "descricao_pt": "Seringa com vacina sobre fundo claro com detalhes azuis, sem texto, estilo clean editorial médico",
            "query_en": ["influenza vaccine syringe", "flu shot medical clean background"],
            "evitar": ["texto", "logos", "faces identificáveis", "sangue"],
            "prompt_ia": "Close-up of flu vaccine syringe on clean white and blue surface, soft natural lighting, no text, no faces, editorial medical photography style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de saúde pública gratuito iniciando amanhã em cidade-núcleo. Alta utilidade para a audiência. Não configura conselho médico — é acesso a serviço público."
    },
    {
        "id_hash": "ed8d120b785029e0cb62e3da9a91f9a966a30562",
        "titulo": "🌽 Na manhã desta sexta-feira (12), foi realizado o sorteio dos beneficiários do Programa Milho 100% em Cristal",
        "cidade": "Cristal",
        "fonte_nome": "Instagram @prefeituradecristal",
        "url_fonte": "https://www.instagram.com/p/DZfY14lFtww/",
        "score_editorial": 9,
        "score_combinado": 19.5,
        "tag_principal": "agro",
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Alta procura leva Cristal a realizar sorteio público dos beneficiários do Programa Milho 100%",
        "subtitulo": "Inscrições superaram a oferta de sacas disponíveis; transparência e igualdade guiaram a seleção dos contemplados",
        "lead": "O município de Cristal realizou na manhã desta sexta-feira (12/06) o sorteio dos beneficiários do Programa Milho 100%, medida adotada após o número de inscrições superar a quantidade de sacas disponíveis. A seleção foi feita de forma pública para garantir transparência e igualdade de oportunidades entre os participantes.",
        "chamada_faixa": "SORTEIO DO MILHO EM CRISTAL",
        "ganchos_3": [
            "Grande adesão ao programa revela necessidade de insumos no interior gaúcho",
            "Transparência como garantia: sorteio público em Cristal",
            "Programa Milho 100% fortalece produtores familiares da região"
        ],
        "angulo_editorial": "Sorteio como notícia de transparência pública e demanda reprimida por insumos agrícolas. Oportunidade de discutir a necessidade de ampliar programas de distribuição.",
        "fontes_complementares_sugeridas": ["Prefeitura Municipal de Cristal", "Secretaria de Agricultura de Cristal"],
        "lead_materia_longa": "Cristal realizou na manhã desta sexta-feira, 12 de junho, o sorteio público dos beneficiários do Programa Milho 100%. A medida foi necessária porque o número de inscrições superou a quantidade de sacas de milho disponíveis para distribuição no município. Para garantir transparência e igualdade entre todos os inscritos, a prefeitura optou pelo sorteio aberto à comunidade, com presença de representantes das famílias agricultoras.",
        "post_instagram": {
            "caption": "Cristal realizou sorteio dos beneficiários do Programa Milho 100%! A grande adesão dos produtores mostrou que a demanda por sementes supera a oferta. Tudo com transparência e igualdade. #Cristal #ProgramaMilho #AgroRS #CostaDoce",
            "hashtags": ["Cristal", "ProgramaMilho", "AgroRS", "CostaDoce", "AgriculturaFamiliar"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal sorteia beneficiários do milho por alta demanda!",
            "desenvolvimento_45s": "Em Cristal, o Programa Milho 100% gerou tanta procura que as sacas disponíveis não eram suficientes para todos os inscritos. A solução foi um sorteio público, realizado nesta sexta-feira com transparência e igualdade para as famílias agricultoras da região.",
            "fechamento_8s": "Programa que faz diferença para o produtor rural do Sul do RS.",
            "cta_5s": "Segue a SulTV para o agro do Sul.",
            "trilha_sugerida": "positivo, rural"
        },
        "tag_thumbnail": "MILHO 100% EM CRISTAL",
        "briefing_visual": {
            "descricao_pt": "Espigas de milho amarelas colhidas empilhadas, fundo verde campo gaúcho, sem pessoas identificáveis, sem texto",
            "query_en": ["corn harvest southern brazil", "maize cobs yellow pile rural"],
            "evitar": ["texto", "logos", "faces identificáveis"],
            "prompt_ia": "Pile of yellow corn cobs harvested in a rural setting in southern Brazil, bright natural light, green background, no people, no text, editorial agricultural photography style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Programa agropecuário com sorteio público em cidade-núcleo. Fato concreto, demanda reprimida por insumos revela contexto econômico dos produtores."
    },
    {
        "id_hash": "45bd9a3823beeb280988d13e0f8211adcbd1907c",
        "titulo": "📑 O prefeito Marcelo Krolow recebeu na tarde desta quinta-feira representantes das Secretarias...",
        "cidade": "Cristal",
        "fonte_nome": "Instagram @prefeituradecristal",
        "url_fonte": "https://www.instagram.com/p/DZfUJEBlnjL/",
        "score_editorial": 9,
        "score_combinado": 17.0,
        "tag_principal": "politica_local",
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "Cristal alinha ações intersetoriais de saúde, educação e assistência social",
        "subtitulo": "",
        "lead": "",
        "chamada_faixa": "",
        "ganchos_3": [],
        "angulo_editorial": "Reunião institucional interna sem desdobramento público claro. Conteúdo de assessoria de imprensa.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {"abertura_2s": "", "desenvolvimento_45s": "", "fechamento_8s": "", "cta_5s": "", "trilha_sugerida": ""},
        "tag_thumbnail": "",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Reunião de alinhamento interno entre secretarias sem desdobramento concreto para o cidadão. Baixo valor editorial — conteúdo de assessoria."
    },
    {
        "id_hash": "e20c1c924e3c8c691279f7b5e6788daf274bbf9f",
        "titulo": "A Prefeitura Municipal de São Lourenço do Sul, por meio da Defesa Civil e das equipes de monitoramento, informa que o município segue acompanhando as condições hidrometeorológicas...",
        "cidade": "São Lourenço do Sul",
        "fonte_nome": "Instagram @prefsls",
        "url_fonte": "https://www.instagram.com/p/DZf5sx9Eppe/",
        "score_editorial": 9,
        "score_combinado": 20.5,
        "tag_principal": "clima",
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "São Lourenço do Sul registra 84 mm de chuva e aciona monitoramento de arroios",
        "subtitulo": "Defesa Civil acompanha elevação do nível do arroio Passo do Candombe após chuvas intensas nas últimas 12 horas",
        "lead": "São Lourenço do Sul registrou 84 milímetros de chuva nas últimas 12 horas na localidade do Passo do Pinto, além de elevação do nível do arroio Passo do Candombe. A Defesa Civil e as equipes de monitoramento do município seguem em alerta acompanhando as condições hidrometeorológicas nas regiões do interior.",
        "chamada_faixa": "84MM EM SÃO LOURENÇO DO SUL",
        "ganchos_3": [
            "Passo do Pinto registra 84 mm em apenas 12 horas",
            "Arroio Passo do Candombe em elevação preocupa moradores do interior",
            "Defesa Civil de SLS em estado de alerta e monitoramento contínuo"
        ],
        "angulo_editorial": "Dado meteorológico concreto (84mm/12h) com consequência direta (arroio em elevação) e ação oficial (monitoramento ativo). Narrativa de alerta preventivo para a audiência rural.",
        "fontes_complementares_sugeridas": ["Defesa Civil de São Lourenço do Sul", "Prefeitura de São Lourenço do Sul"],
        "lead_materia_longa": "A Prefeitura de São Lourenço do Sul, por meio da Defesa Civil e das equipes de monitoramento, informou que o município registrou 84 milímetros de chuva nas últimas 12 horas na localidade do Passo do Pinto. Além disso, é monitorada a elevação do nível do arroio no Passo do Candombe. As equipes seguem em alerta nas regiões do interior, acompanhando as condições hidrometeorológicas para orientar moradores e produtores rurais sobre eventuais riscos.",
        "post_instagram": {
            "caption": "⚠️ Atenção moradores de São Lourenço do Sul! 84mm de chuva em 12 horas no Passo do Pinto. Arroio Candombe em elevação. Defesa Civil em alerta. #SãoLourencodosul #ChuvaRS #DefesaCivil #CostaDoce",
            "hashtags": ["SaoLourencoDoSul", "ChuvaRS", "DefesaCivil", "CostaDoce", "AlertaRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "São Lourenço do Sul em alerta com 84mm de chuva!",
            "desenvolvimento_45s": "Nas últimas 12 horas, o Passo do Pinto em São Lourenço do Sul registrou 84 milímetros de chuva. O arroio Passo do Candombe está em elevação e a Defesa Civil municipal acompanha de perto as condições do interior. Moradores devem ficar atentos.",
            "fechamento_8s": "Fique em segurança. Siga as orientações da Defesa Civil.",
            "cta_5s": "SulTV acompanha as chuvas no Sul do RS.",
            "trilha_sugerida": "tenso, urgente"
        },
        "tag_thumbnail": "ALERTA DE CHUVA SÃO LOURENÇO",
        "briefing_visual": {
            "descricao_pt": "Arroio transbordando com água barrenta em área rural do Sul do RS, céu escuro, sem pessoas, sem texto",
            "query_en": ["flooded creek heavy rain south brazil", "overflowing stream rural rio grande do sul"],
            "evitar": ["texto", "logos", "faces identificáveis"],
            "prompt_ia": "Overflowing brown stream in rural southern Brazil countryside after heavy rain, cloudy dark sky, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Dado meteorológico concreto (84mm/12h) com impacto em cidade-núcleo. Defesa Civil em alerta — informação de segurança pública relevante."
    },
    {
        "id_hash": "313694dcd9657c5bbc15d619b4c64f5230036b36",
        "titulo": "A saúde que queremos construir passa pela participação de todos.",
        "cidade": "São Lourenço do Sul",
        "fonte_nome": "Instagram @prefsls",
        "url_fonte": "https://www.instagram.com/p/DZfjZo0l8ra/",
        "score_editorial": 9,
        "score_combinado": 15.0,
        "tag_principal": "saude",
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "São Lourenço do Sul sedia etapa municipal da Conferência Nacional de Saúde em 26 de junho",
        "subtitulo": "",
        "lead": "",
        "chamada_faixa": "",
        "ganchos_3": [],
        "angulo_editorial": "Convite para conferência futura — baixo valor notícia, sem fato consumado.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {"abertura_2s": "", "desenvolvimento_45s": "", "fechamento_8s": "", "cta_5s": "", "trilha_sugerida": ""},
        "tag_thumbnail": "",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Convite para evento futuro (26/06) sem fato consumado. Conteúdo promocional institucional."
    },
    {
        "id_hash": "e01838afcd9335ee307b79a73b8b0bf111bfe4ba",
        "titulo": "EDITAL DE PUBLICAÇÃO DE PENALIDADE Nº 001/202630/03/2026",
        "cidade": "Chuvisca",
        "fonte_nome": "Prefeitura de Chuvisca",
        "url_fonte": "https://www.chuvisca.rs.gov.br/site/Noticias/administracao/909056-edital-de-publicaccedilatildeo-de-penalidade-nordm-0012026",
        "score_editorial": 9,
        "score_combinado": 14.0,
        "tag_principal": "outro",
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "",
        "subtitulo": "",
        "lead": "",
        "chamada_faixa": "",
        "ganchos_3": [],
        "angulo_editorial": "Edital de penalidade administrativa — conteúdo procedural/legal sem valor editorial.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {"abertura_2s": "", "desenvolvimento_45s": "", "fechamento_8s": "", "cta_5s": "", "trilha_sugerida": ""},
        "tag_thumbnail": "",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Edital procedural administrativo sem valor jornalístico. Data do edital (30/03/2026) indica conteúdo antigo."
    },
    {
        "id_hash": "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c",
        "titulo": "EDITAL Nº 002/2026 - ABERTURA DE PRAZO PARA REQUERIMENTOS SOBRE O PROJETO DE AMPLIAÇÃO DO PERÍMETRO URBANO",
        "cidade": "Chuvisca",
        "fonte_nome": "Prefeitura de Chuvisca",
        "url_fonte": "https://www.chuvisca.rs.gov.br/site/Noticias/administracao/908521",
        "score_editorial": 9,
        "score_combinado": 14.0,
        "tag_principal": "outro",
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "",
        "subtitulo": "",
        "lead": "",
        "chamada_faixa": "",
        "ganchos_3": [],
        "angulo_editorial": "Edital de abertura de prazo urbanístico — procedural.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {"caption": "", "hashtags": []},
        "roteiro_short_60s": {"abertura_2s": "", "desenvolvimento_45s": "", "fechamento_8s": "", "cta_5s": "", "trilha_sugerida": ""},
        "tag_thumbnail": "",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Edital de prazo urbanístico — procedural, sem valor jornalístico para a audiência geral."
    },
    {
        "id_hash": "9871f55e350347ffc87529113c20f43960ab4750",
        "titulo": "Educação que transforma vidas!",
        "cidade": "Barra do Ribeiro",
        "fonte_nome": "Instagram @prefeituradebarradoribeiro",
        "url_fonte": "https://www.instagram.com/p/DZfxnJgFN71/",
        "score_editorial": 9,
        "score_combinado": 14.5,
        "tag_principal": "educacao",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Conteúdo promocional de governo com título genérico. Sem fato novo.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Título genérico/vazio. Conteúdo promocional sem fato concreto."
    },
    {
        "id_hash": "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220",
        "titulo": "📢 AVISO DE AUDIÊNCIA PÚBLICA",
        "cidade": "Sentinela do Sul",
        "fonte_nome": "Prefeitura de Sentinela do Sul",
        "url_fonte": "https://www.sentineladosul.rs.gov.br/noticias/aviso-de-audiencia-publica-1",
        "score_editorial": 8,
        "score_combinado": 13.5,
        "tag_principal": "politica_local",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Aviso procedimental de audiência pública, sem conteúdo.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Aviso de audiência pública sem data, pauta ou conteúdo no resumo. Procedural."
    },
    {
        "id_hash": "c77c704f766cfa913b42a8d2b37cfc4c03320244",
        "titulo": "05/05/2026EMISSÃO DE NOTAS FISCAIS PELO EMISSOR NACIONAL",
        "cidade": "Sentinela do Sul",
        "fonte_nome": "Prefeitura de Sentinela do Sul",
        "url_fonte": "https://www.sentineladosul.rs.gov.br/noticias/emissao-de-notas-fiscais-pelo-emissor-nacional",
        "score_editorial": 8,
        "score_combinado": 12.0,
        "tag_principal": "outro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Conteúdo tributário/fiscal de maio — desatualizado e sem valor jornalístico.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Conteúdo tributário procedural de 05/05/2026 — completamente fora de pauta."
    },
    {
        "id_hash": "2ca9c6c05b652779fe1185d698a6d67e649d2e53",
        "titulo": "Secretaria Municipal do Turismo, Desporto e Lazer6 Velejaço solidário",
        "cidade": "Barra do Ribeiro",
        "fonte_nome": "Prefeitura de Barra do Ribeiro",
        "url_fonte": "https://www.barradoribeiro.rs.gov.br/noticiasView/632_6-Velejaco-solidario.html",
        "score_editorial": 8,
        "score_combinado": 12.5,
        "tag_principal": "esporte",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Evento esportivo náutico em cidade secundária — sem conteúdo no resumo.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Sem conteúdo no resumo. Evento náutico em cidade fora do núcleo primário."
    },
    {
        "id_hash": "9d5c35e9be86ae890a20d830c6145e4be5e610fc",
        "titulo": "🏟️ Mais um importante investimento para o esporte de Guaíba está perto de se tornar realidade!",
        "cidade": "Guaíba",
        "fonte_nome": "Instagram @prefeituradeguaiba",
        "url_fonte": "https://www.instagram.com/reel/DZh9ESKhWIp/",
        "score_editorial": 8,
        "score_combinado": 14.0,
        "tag_principal": "esporte",
        "titulo_sultv": "Ginásio da Vila Iolanda em Guaíba chega a 91% de obra concluída",
        "chamada_faixa": "",
        "angulo_editorial": "Obra pública com percentual concreto em cidade próxima ao eixo sul. Boa pauta mas fora do núcleo primário.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Avanço de obra público em cidade fora do núcleo primário SulTV. Conteúdo positivo mas dilui a identidade geográfica da Costa Doce."
    },
    {
        "id_hash": "819d32a271bcac9bb069558c347f1a99683e55f0",
        "titulo": "Edital de Leilão de Alienação Fiduciária Banco Santander (Brasil) S/A X Romulo Rodeghiero Rodrigues",
        "cidade": "Pelotas",
        "fonte_nome": "Diário da Manhã (Pelotas)",
        "url_fonte": "https://diariodamanhapelotas.com.br/site/edital-de-leilao-de-alienacao-fiduciaria-banco-santander-brasil-s-a-x-romulo-rodeghiero-rodrigues-3/",
        "score_editorial": 8,
        "score_combinado": 12.0,
        "tag_principal": "outro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Edital judicial de leilão fiduciário — procedural legal.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Edital judicial de leilão bancário. Conteúdo procedural/legal sem valor jornalístico."
    },
    {
        "id_hash": "234a6969e7c00de1991dd10bc680dbcd6a755946",
        "titulo": "Trabalho infantil: 'Quando uma criança é forçada a trabalhar, seu futuro é comprometido', alerta desembargadora Rejane Pedra",
        "cidade": "Pelotas",
        "fonte_nome": "Diário da Manhã (Pelotas)",
        "url_fonte": "https://diariodamanhapelotas.com.br/site/trabalho-infantil-quando-uma-crianca-e-forcada-a-trabalhar/",
        "score_editorial": 8,
        "score_combinado": 13.0,
        "tag_principal": "outro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Guardrail: conteúdo envolvendo menores (trabalho infantil). Aplicar restrição.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Guardrail ativo: conteúdo envolvendo menores (Dia Mundial de Combate ao Trabalho Infantil)."
    },
    {
        "id_hash": "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e",
        "titulo": "Ao final da audiência em Pelotas, parlamentares manifestam-se sobre concessões, privatizações e PPPs",
        "cidade": "Pelotas",
        "fonte_nome": "Assembleia Legislativa RS (ALERS)",
        "url_fonte": "http://www2.al.rs.gov.br/noticias/ExibeNoticia/tabid/5374/IdMateria/316307/language/pt-BR/Default.aspx",
        "score_editorial": 8,
        "score_combinado": 18.0,
        "tag_principal": "politica_regional",
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "Deputados debatem em Pelotas privatizações e parcerias público-privadas no setor de energia do RS",
        "subtitulo": "Audiência pública discutiu plebiscito sobre estatais energéticas e concessões de serviços públicos na região",
        "lead": "Deputados estaduais manifestaram posições sobre privatizações, parcerias público-privadas e concessões de serviços públicos ao final de audiência realizada em Pelotas. O plebiscito para deliberar sobre estatais do setor energético foi um dos principais pontos do debate.",
        "chamada_faixa": "PRIVATIZAÇÕES EM DEBATE EM PELOTAS",
        "ganchos_3": [
            "Plebiscito sobre estatais de energia do RS em discussão",
            "Concessões e PPPs: o que muda para os gaúchos?",
            "Assembleia Legislativa ouve a população de Pelotas e região"
        ],
        "angulo_editorial": "Audiência pública com alto impacto regional — discussão sobre privatizações de energia interessa diretamente produtores rurais e consumidores do Sul do RS. Fonte primária confiável (ALERS).",
        "fontes_complementares_sugeridas": ["Assembleia Legislativa do RS", "Deputados participantes"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Debate em Pelotas sobre PPPs, privatizações e concessões. Deputados discutiram os caminhos para o setor de energia no RS. #Pelotas #AsambleiaRS #PPP #EnergiaRS #CostaDoce",
            "hashtags": ["Pelotas", "AssembleiaRS", "PPP", "EnergiaRS", "PoliticaRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Debate sobre privatizações chegou a Pelotas!",
            "desenvolvimento_45s": "Deputados estaduais debateram em Pelotas as privatizações, parcerias público-privadas e concessões de serviços públicos. O plebiscito sobre estatais do setor de energia foi o principal ponto da discussão. A audiência reuniu parlamentares e representantes da comunidade no Sul do RS.",
            "fechamento_8s": "O futuro dos serviços públicos gaúchos passa pelo Sul.",
            "cta_5s": "SulTV, a voz do Sul do RS.",
            "trilha_sugerida": "institucional, sério"
        },
        "tag_thumbnail": "PRIVATIZAÇÕES DEBATE PELOTAS",
        "briefing_visual": {
            "descricao_pt": "Auditório com plateia e painelistas ao fundo, ambiente de audiência pública, sem texto, iluminação formal",
            "query_en": ["public hearing auditorium brazil", "government meeting audience hall"],
            "evitar": ["texto", "logos partidários", "faces identificáveis em close"],
            "prompt_ia": "Wide shot of government public hearing auditorium in Brazil, formal lighting, audience in seats, speakers at front table, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Audiência pública da ALERS sobre privatizações realizada em Pelotas — relevante para consumidores e produtores do Sul do RS. Fonte institucional primária."
    },
    {
        "id_hash": "49348b06a39337d964518e54a7715142418ea220",
        "titulo": "Técnicos detalham legislação e passos a serem seguidos na destinação de recursos ao Funcriança",
        "cidade": "Porto Alegre",
        "fonte_nome": "Assembleia Legislativa RS (ALERS)",
        "url_fonte": "http://www2.al.rs.gov.br/noticias/ExibeNoticia/tabid/5374/IdMateria/316303/language/pt-BR/Default.aspx",
        "score_editorial": 8,
        "score_combinado": 12.0,
        "tag_principal": "outro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Conteúdo técnico-legal sobre Funcriança — sem impacto direto para a audiência geral da SulTV.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Conteúdo técnico-fiscal sobre destinação de IR ao Funcriança. Sem âncora regional direta para a audiência SulTV."
    },
    {
        "id_hash": "e914edb4101909198de490e19b4ee3ebeb063e57",
        "titulo": "INFORMAÇÕES AGROPECUÁRIAS",
        "cidade": "RS",
        "fonte_nome": "Emater RS — Notícias",
        "url_fonte": "https://www.emater.tche.br/site/info-agro/informativo_conjuntural.php",
        "score_editorial": 9,
        "score_combinado": 13.0,
        "tag_principal": "agro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Cabeçalho de seção do site Emater — não é matéria.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Cabeçalho de seção do portal Emater RS, não é matéria jornalística."
    },
    {
        "id_hash": "ddcd388ff38cf8bb1e89d08320447b73c9be844a",
        "titulo": "'A gente não dorme mais': produtores do RS temem que renegociação de dívidas não seja aprovada pelo Senado",
        "cidade": "RS",
        "fonte_nome": "Canal Rural — seção RS",
        "url_fonte": "https://www.canalrural.com.br/nacional/rio-grande-do-sul/a-gente-nao-dorme-mais-produtores-do-rs-temem-que-renegociacao-de-dividas-nao-seja-aprovada-pelo-senado/",
        "score_editorial": 7,
        "score_combinado": 16.5,
        "tag_principal": "agro",
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Produtores gaúchos cobram aprovação da renegociação de dívidas no Senado antes do início da próxima safra",
        "subtitulo": "Risco de bloqueio no Senado preocupa agricultores que dependem de crédito rural para plantio",
        "lead": "Produtores rurais do Rio Grande do Sul vivem com ansiedade crescente diante do risco de a renegociação de dívidas agrícolas não ser aprovada pelo Senado Federal. O setor alerta que a falta de definição pode comprometer o acesso ao crédito rural necessário para a próxima safra.",
        "chamada_faixa": "RENEGOCIAÇÃO DE DÍVIDAS NO SENADO",
        "ganchos_3": [
            "Sem aprovação no Senado, produtores gaúchos podem perder crédito para a próxima safra",
            "Bancada ruralista e agricultores pressionam por votação urgente",
            "Rio Grande do Sul, um dos estados mais endividados do agro brasileiro, aguarda desfecho"
        ],
        "angulo_editorial": "Pauta de alto impacto financeiro para o agro gaúcho — risco real e imediato (crédito da próxima safra). A frase 'a gente não dorme mais' humaniza e ancora na ansiedade real do produtor. Reformatar 100% sem mencionar fonte veículo.",
        "fontes_complementares_sugeridas": ["Federação da Agricultura do RS (Farsul)", "Sindicatos rurais do Sul do RS"],
        "lead_materia_longa": "Produtores rurais gaúchos aguardam com apreensão a votação no Senado Federal sobre a renegociação das dívidas agrícolas. O receio crescente no setor é que, sem a aprovação da medida, os agricultores percam o acesso ao crédito rural necessário para iniciar o plantio da próxima safra. No Rio Grande do Sul, um dos estados com maior volume de endividamento no campo, a tensão é palpável entre as famílias que dependem do financiamento para custear a produção de grãos.",
        "post_instagram": {
            "caption": "Produtores gaúchos na corda bamba! O Senado ainda não votou a renegociação das dívidas agrícolas e o prazo para a próxima safra se aproxima. #AgroRS #DividasAgricolas #Senado #ProdutoresRS #Agronegocio",
            "hashtags": ["AgroRS", "DividasAgricolas", "Senado", "ProdutoresRS", "Agronegocio"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Produtores gaúchos ansiosos com renegociação de dívidas!",
            "desenvolvimento_45s": "No Rio Grande do Sul, agricultores aguardam com preocupação a votação no Senado sobre a renegociação das dívidas agrícolas. Se não for aprovada, o setor pode perder acesso ao crédito rural para a próxima safra. A tensão é real em todo o campo gaúcho.",
            "fechamento_8s": "O futuro da safra gaúcha pode ser decidido no Senado.",
            "cta_5s": "SulTV, o agro do Sul do RS.",
            "trilha_sugerida": "tenso, rural, acústico"
        },
        "tag_thumbnail": "DÍVIDAS NO SENADO",
        "briefing_visual": {
            "descricao_pt": "Produtor rural em lavoura de soja ao amanhecer, olhar preocupado para o horizonte, sem texto, sem identificação de face clara",
            "query_en": ["farmer worried soybean field brazil", "rural producer southern brazil sunrise field"],
            "evitar": ["texto", "logos", "faces em close identificáveis"],
            "prompt_ia": "Farmer standing at the edge of a soybean field at dawn in southern Brazil, looking at the horizon with concern, golden morning light, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta financeira de alto impacto para produtores gaúchos — risco real ao crédito da próxima safra. Âncora RS clara. Conteúdo reformatado sem mencionar veículo de origem."
    },
    {
        "id_hash": "8c10d704aa76774d2be1bdb6d93ca335fbf9061b",
        "titulo": "Vinhos vencidos há 9 anos são apreendidos: 'um dos piores estabelecimentos que já vimos'",
        "cidade": "RS",
        "fonte_nome": "Canal Rural — seção RS",
        "url_fonte": "https://www.canalrural.com.br/seguranca/vinhos-vencidos-ha-9-anos-sao-apreendidos-um-dos-piores-estabelecimentos-que-ja-vimos/",
        "score_editorial": 7,
        "score_combinado": 15.0,
        "tag_principal": "seguranca_alimentar",
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "MP gaúcho apreende cinco toneladas de produtos vencidos em três mercados, incluindo vinhos com 9 anos de validade expirada",
        "subtitulo": "Um estabelecimento foi interditado totalmente e o proprietário preso; força-tarefa agiu em mercados do Rio Grande do Sul",
        "lead": "Uma força-tarefa do Ministério Público do Rio Grande do Sul apreendeu cinco toneladas de produtos impróprios para consumo em três mercados gaúchos. A ação revelou vinhos com prazo de validade expirado há 9 anos e resultou na interdição total de um dos estabelecimentos e na prisão do proprietário.",
        "chamada_faixa": "VINHOS VENCIDOS APREENDIDOS NO RS",
        "ganchos_3": [
            "Vinhos com 9 anos de prazo vencido encontrados em prateleiras",
            "Estabelecimento interditado e dono preso no Rio Grande do Sul",
            "Cinco toneladas de produtos impróprios recolhidos pela força-tarefa"
        ],
        "angulo_editorial": "Operação com resultado concreto e dramaticidade natural (9 anos vencido!). Fonte primária: MP-RS. Reformatar sem mencionar veículo.",
        "fontes_complementares_sugeridas": ["Ministério Público do Rio Grande do Sul"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "🚨 Fiscalização gaúcha apreende 5 toneladas de produtos vencidos! Entre eles, vinhos com 9 anos de validade expirada. Um proprietário foi preso e um mercado interditado. #SegurancaAlimentar #FiscalizacaoRS #MPRS",
            "hashtags": ["SegurancaAlimentar", "FiscalizacaoRS", "MPRS", "ConsumidorRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Vinhos com 9 anos vencidos apreendidos no RS!",
            "desenvolvimento_45s": "Uma força-tarefa do Ministério Público gaúcho recolheu cinco toneladas de produtos vencidos em três mercados do Rio Grande do Sul. A situação mais grave foi encontrar vinhos com prazo expirado há 9 anos nas prateleiras. Um estabelecimento foi completamente interditado e o proprietário preso.",
            "fechamento_8s": "Fiscalização em ação para proteger o consumidor gaúcho.",
            "cta_5s": "Acompanhe a SulTV, o Sul em destaque.",
            "trilha_sugerida": "urgente, impactante"
        },
        "tag_thumbnail": "5 TONELADAS VENCIDAS RS",
        "briefing_visual": {
            "descricao_pt": "Garrafas de vinho em prateleiras de mercado, fundo de loja de alimentos, sem texto, sem pessoas identificáveis",
            "query_en": ["wine bottles supermarket shelf", "wine store display bottles"],
            "evitar": ["texto com datas", "logos", "faces identificáveis"],
            "prompt_ia": "Rows of wine bottles on supermarket shelves, warm lighting, no people, no text visible, editorial photography style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Operação do MP-RS com resultado concreto e impactante. Segurança alimentar — interesse direto do consumidor gaúcho. Fonte primária institucional."
    },
    {
        "id_hash": "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf",
        "titulo": "Fiscais apreendem 630 kg de alimentos impróprios para consumo",
        "cidade": "RS",
        "fonte_nome": "Canal Rural — seção RS",
        "url_fonte": "https://www.canalrural.com.br/seguranca/fiscais-apreendem-630-kg-de-alimentos-improprios-para-consumo/",
        "score_editorial": 7,
        "score_combinado": 14.5,
        "tag_principal": "seguranca_alimentar",
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "Força-tarefa gaúcha apreende 630 kg de alimentos impróprios em cinco estabelecimentos",
        "subtitulo": "Carnes, ovos, amendoim, iogurtes, pães e álcool foram recolhidos em operação do Ministério Público do RS",
        "lead": "Uma força-tarefa do Ministério Público do Rio Grande do Sul apreendeu 630 quilogramas de alimentos impróprios para consumo em cinco estabelecimentos comerciais. Entre os produtos recolhidos estão carnes, ovos, amendoim, iogurtes, pães e álcool.",
        "chamada_faixa": "630 KG APREENDIDOS NO RS",
        "ganchos_3": [
            "Variedade de alimentos impróprios encontrados em cinco estabelecimentos",
            "Fiscalização do MP-RS em ação pela segurança alimentar dos gaúchos",
            "Resultado de força-tarefa reforça importância da fiscalização do comércio"
        ],
        "angulo_editorial": "Complementa o item de vinhos vencidos — mesma operação ou operação correlata. Fonte primária MP-RS. Publicar como nota separada pelo volume concreto (630 kg).",
        "fontes_complementares_sugeridas": ["Ministério Público do Rio Grande do Sul"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "630 kg de alimentos impróprios retirados de circulação no RS! Carne, ovos, iogurte e mais — tudo apreendido pela fiscalização gaúcha em cinco estabelecimentos. #SegurancaAlimentar #MPRS #FiscalizacaoRS",
            "hashtags": ["SegurancaAlimentar", "MPRS", "FiscalizacaoRS", "ConsumidorRS"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "630 kg de alimentos impróprios apreendidos no RS!",
            "desenvolvimento_45s": "O Ministério Público gaúcho recolheu 630 quilos de alimentos fora das condições de consumo em cinco estabelecimentos comerciais do Rio Grande do Sul. Carnes, ovos, amendoim, iogurtes, pães e álcool estavam impróprios para consumo e foram retirados de circulação.",
            "fechamento_8s": "Fiscalização protege o consumidor gaúcho.",
            "cta_5s": "Segue a SulTV para as notícias que importam.",
            "trilha_sugerida": "impactante, informativo"
        },
        "tag_thumbnail": "630 KG IMPRÓPRIOS RS",
        "briefing_visual": {
            "descricao_pt": "Alimentos em embalagens plásticas dispostos para fiscalização, sem texto, ambiente de inspeção sanitária",
            "query_en": ["food inspection confiscated products brazil", "supermarket food safety inspection"],
            "evitar": ["texto", "logos", "faces identificáveis"],
            "prompt_ia": "Food products laid out on table for inspection, various packaged meats and dairy, no text, no faces, editorial documentation photography style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Operação concreta do MP-RS. Complementa item de vinhos vencidos. Segurança alimentar — alta relevância para consumidores gaúchos."
    },
    # Items 26-42: REBAIXAR / BLOQUEAR resumidos
    {
        "id_hash": "bde33368856dbdeb6aa6cd6c59085d2ea2c4960c",
        "titulo": "Prefeitura de Sertão Santana assina Termo de Fomento com CTG Tio Raymundo",
        "cidade": "Sertão Santana",
        "fonte_nome": "Instagram @pref.sertaosantana",
        "url_fonte": "https://www.instagram.com/p/DZfzziPEek_/",
        "score_editorial": 7,
        "score_combinado": 11.0,
        "tag_principal": "cultura",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "R$ 9.750 para CTG local — convênio de baixo valor, fora do núcleo primário.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Termo de fomento de baixo valor (R$ 9.750) para CTG fora do núcleo primário. Conteúdo de assessoria local."
    },
    {
        "id_hash": "796c2834066f6048e6312d9168dab9139a7b4a6c",
        "titulo": "PEDIDOS DE SEMENTE DE BATATA",
        "cidade": "Canguçu",
        "fonte_nome": "Instagram @prefeituradecangucu",
        "url_fonte": "https://www.instagram.com/p/DZfWyOEkT5q/",
        "score_editorial": 7,
        "score_combinado": 11.5,
        "tag_principal": "agro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Aviso de pedidos de semente — procedural agrícola local.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Aviso de pedidos de semente procedural. Boa pauta potencial mas sem conteúdo jornalístico desenvolvido."
    },
    {
        "id_hash": "7fb69e39c3c3e7d78ee851f987e64b1565c4df91",
        "titulo": "INSCRIÇÕES ABERTAS PARA O PROGRAMA BANRISUL DE PATROCÍNIOS 2027",
        "cidade": "Encruzilhada do Sul",
        "fonte_nome": "Instagram @prefeituraencruzilhadadosul",
        "url_fonte": "https://www.instagram.com/p/DZfvPmvCSTX/",
        "score_editorial": 7,
        "score_combinado": 11.0,
        "tag_principal": "outro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Programa de patrocínios institucional — divulgação, não é pauta jornalística.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Divulgação institucional de programa de patrocínios bancários. Não é pauta jornalística."
    },
    {
        "id_hash": "b5cea601247c282e95a62bbe6bc9805e678ee4ff",
        "titulo": "O que é o 12 de Junho",
        "cidade": "Dom Feliciano",
        "fonte_nome": "Instagram @prefeituradomfeliciano",
        "url_fonte": "https://www.instagram.com/p/DZfJxZCxYgg/",
        "score_editorial": 6,
        "score_combinado": 10.0,
        "tag_principal": "outro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Guardrail: conteúdo sobre trabalho infantil/menores.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Guardrail: conteúdo envolvendo menores (Dia Mundial contra Trabalho Infantil)."
    },
    {
        "id_hash": "e0295fa6a6c460786bd6d6b0f63b132a0c2eaaa6",
        "titulo": "2º JANTAR AROMAS E SABORES ENCRUZILHADENSES",
        "cidade": "Encruzilhada do Sul",
        "fonte_nome": "Instagram @prefeituraencruzilhadadosul",
        "url_fonte": "https://www.instagram.com/p/DZfXbctgg-F/",
        "score_editorial": 6,
        "score_combinado": 10.5,
        "tag_principal": "agro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Evento gastronômico futuro (11/07). Divulgação antecipada sem fato consumado.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Evento futuro (11/07). Sem fato consumado. Divulgação de agenda antecipada."
    },
    {
        "id_hash": "64ff5a9766ff3a88e12044797b2fa33e2de1e24f",
        "titulo": "Husm recebe 30 profissionais angolanos para atividades de formação",
        "cidade": "Santa Maria",
        "fonte_nome": "UFSM — Politécnico",
        "url_fonte": "https://www.ufsm.br/2026/06/11/husm-recebe-30-profissionais-angolanos",
        "score_editorial": 6,
        "score_combinado": 9.5,
        "tag_principal": "saude",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Intercâmbio acadêmico em Santa Maria — fora da zona geográfica primária SulTV.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Intercâmbio acadêmico em Santa Maria, fora da zona Sul-RS primária."
    },
    {
        "id_hash": "2e443f6524fe184d493450189732a2d33ce423f0",
        "titulo": "Cuidado, respeito e inclusão em pauta no serviço público",
        "cidade": "Eldorado do Sul",
        "fonte_nome": "Instagram @prefeldoradodosul",
        "url_fonte": "https://www.instagram.com/p/DZfXtr6nJsS/",
        "score_editorial": 6,
        "score_combinado": 9.5,
        "tag_principal": "politica_local",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Palestra interna de servidores — conteúdo institucional sem impacto externo.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Palestra interna de servidores municipais. Conteúdo de assessoria sem impacto externo."
    },
    {
        "id_hash": "5576572fa9ff5f43f9357771f36fa33675b30074",
        "titulo": "Grande procura marcou o Feirão de Emprego realizado em Eldorado do Sul",
        "cidade": "Eldorado do Sul",
        "fonte_nome": "Instagram @prefeldoradosul",
        "url_fonte": "https://www.instagram.com/p/DZfXc6xnNlo/",
        "score_editorial": 6,
        "score_combinado": 9.8,
        "tag_principal": "economia",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Feirão de emprego positivo mas fora do núcleo Sul-RS. Sem dados concretos de vagas no resumo.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Feirão de emprego em Eldorado do Sul — fora do núcleo primário. Sem dados concretos de vagas."
    },
    {
        "id_hash": "ed500fa1650f558d19912507960d8107c15b73b6",
        "titulo": "Mais saúde, mais inclusão e mais oportunidades para aprender!",
        "cidade": "Rio Grande",
        "fonte_nome": "Instagram @prefeituradoriogrande",
        "url_fonte": "https://www.instagram.com/reel/DZiLuKmOwOU/",
        "score_editorial": 6,
        "score_combinado": 9.5,
        "tag_principal": "politica_local",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Entrega de óculos para estudantes em Rio Grande — bom programa mas fora do núcleo primário.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Programa social positivo em Rio Grande, mas fora do núcleo primário SulTV."
    },
    {
        "id_hash": "a119b3ab032b6823f5ae72deb74b301b0c6f2ce6",
        "titulo": "VIVA ANTIGA REITORIA!",
        "cidade": "Santa Maria",
        "fonte_nome": "Instagram @prefeituradesantamaria",
        "url_fonte": "https://www.instagram.com/p/DZfyyu9lGgR/",
        "score_editorial": 6,
        "score_combinado": 9.0,
        "tag_principal": "evento",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Evento cultural da UFSM em Santa Maria — fora da zona primária.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Evento cultural universitário em Santa Maria, fora do núcleo geográfico SulTV."
    },
    {
        "id_hash": "f76a9f4d8f924103e2f97c3ba0809495beee21e9",
        "titulo": "Atenção, expositores! Inscrições Dom Feliciano",
        "cidade": "Dom Feliciano",
        "fonte_nome": "Instagram @prefeituradomfeliciano",
        "url_fonte": "https://www.instagram.com/reel/DZgHFEQRkMa/",
        "score_editorial": 4,
        "score_combinado": 7.0,
        "tag_principal": "evento",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Aviso de inscrições para feirão local — conteúdo de agenda.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Aviso de inscrições para expositores de feirão local — agenda, sem fato jornalístico."
    },
    {
        "id_hash": "d83adf57e4affc249a1f845dd7e445639170d29a",
        "titulo": "Resultados Quadrangular Final Bocha Sertão Santana",
        "cidade": "Sertão Santana",
        "fonte_nome": "Instagram @pref.sertaosantana",
        "url_fonte": "https://www.instagram.com/p/DZfw59FESG1/",
        "score_editorial": 4,
        "score_combinado": 7.0,
        "tag_principal": "esporte",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Resultados de bocha local — nicho muito específico, fora do núcleo.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Resultado de campeonato de bocha municipal — nicho muito específico, fora do núcleo primário."
    },
    {
        "id_hash": "34081616e488e5b65acf1cb61b59eb1b26f99e95",
        "titulo": "12 de Junho - Dia Mundial de Combate ao Trabalho Infantil - Canguçu",
        "cidade": "Canguçu",
        "fonte_nome": "Instagram @prefeituradecangucu",
        "url_fonte": "https://www.instagram.com/p/DZfOyDkCVnJ/",
        "score_editorial": 4,
        "score_combinado": 7.5,
        "tag_principal": "outro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Guardrail: conteúdo envolvendo menores.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Guardrail: conteúdo sobre trabalho infantil/menores."
    },
    {
        "id_hash": "f12c914bbfe7d14874787fb0b75ef225c0789505",
        "titulo": "Motorista perde controle de veículo e colide contra poste em Venâncio Aires",
        "cidade": "Venâncio Aires",
        "fonte_nome": "Folha do Mate",
        "url_fonte": "https://folhadomate.com/noticias/transito/motorista-perde-controle-de-veiculo-e-colide-contra-poste-em-venancio/",
        "score_editorial": 5,
        "score_combinado": 8.0,
        "tag_principal": "transito",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Acidente menor em cidade fora do núcleo, sem vítima grave identificada. Baixa relevância regional.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Acidente de trânsito menor em cidade fora do núcleo primário SulTV."
    },
    {
        "id_hash": "60dbd239974f644ecad5bbc5ad569de010734829",
        "titulo": "Promagro: incentivo para jovens agricultores com vontade de investir",
        "cidade": "Venâncio Aires",
        "fonte_nome": "Folha do Mate",
        "url_fonte": "https://folhadomate.com/noticias/rural/promagro-incentivo-para-jovens-agricultores-com-vontade-de-investir/",
        "score_editorial": 5,
        "score_combinado": 8.5,
        "tag_principal": "agro",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Programa agrícola para jovens em cidade fora do núcleo. Boa pauta em outro contexto.",
        "briefing_visual": {},
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Promagro em Venâncio Aires — fora do núcleo primário Sul-RS. Sem âncora Costa Doce."
    },
    {
        "id_hash": "2d870a9873d6a9e2393594ca9695f2fb86cd7083",
        "titulo": "Brasil empata com Marrocos na estreia da Copa do Mundo",
        "cidade": "Bento Gonçalves",
        "fonte_nome": "Diário do Aço",
        "url_fonte": "https://serranossa.com.br/brasil-empata-com-marrocos-na-estreia-da-copa-do-mundo/",
        "score_editorial": 5,
        "score_combinado": 8.0,
        "tag_principal": "esporte",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Esporte nacional sem âncora regional Sul-RS. SulTV não tem formato esportivo nacional.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Copa do Mundo — conteúdo nacional sem âncora Sul-RS. Fora do escopo editorial SulTV."
    },
    {
        "id_hash": "991dbaa9fff99a1bd6a044a98be22f9815900ff0",
        "titulo": "Polícia Civil prende mulher investigada por homicídio ocorrido em Bento Gonçalves",
        "cidade": "Bento Gonçalves",
        "fonte_nome": "Diário do Aço",
        "url_fonte": "https://serranossa.com.br/policia-civil-prende-mulher-investigada-por-homicidio-em-bento-goncalves/",
        "score_editorial": 5,
        "score_combinado": 8.5,
        "tag_principal": "policia",
        "titulo_sultv": "",
        "chamada_faixa": "",
        "angulo_editorial": "Homicídio com vítima identificada em Bento Gonçalves — guardrail (vítima identificada + crime grave). Fora do núcleo primário.",
        "briefing_visual": {},
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Guardrail: tragédia com vítima identificada (Mário Augusto de Lima Gomes). Fora do núcleo Sul-RS."
    },
]

# ──────────────────────────────────────────────
# MATÉRIAS LONGAS
# ──────────────────────────────────────────────
MATERIAS = {
    "882edeb88f0be982907d48640a98bb6fe38fa6b1": """### Título ###
Camaquã lança Campanha do Agasalho 2026 com foco em autonomia das famílias

### Artigo ###
Com a chegada do inverno no Sul do Rio Grande do Sul, Camaquã deu início à Campanha do Agasalho 2026. A iniciativa vai além da tradicional arrecadação de roupas e cobertores: o Secretário Fabiano Ribeiro apresentou uma série de ações estruturadas para enfrentar o frio e promover a autonomia das famílias atendidas pela rede de assistência social do município.

A campanha mobiliza moradores, comércios e entidades locais para reunir agasalhos e materiais de aquecimento que serão distribuídos para famílias em situação de vulnerabilidade. O diferencial desta edição está na articulação entre a arrecadação de itens e o fortalecimento de vínculos comunitários que garantam apoio além da temporada de frio.

Na Costa Doce, onde as temperaturas caem com intensidade durante os meses de inverno, ações como essa têm impacto direto na qualidade de vida de moradores em situação de risco social. Informações sobre os pontos de coleta e o cronograma de distribuição devem ser divulgados pela Prefeitura de Camaquã em breve.

### Legenda sugerida ###
Campanha do Agasalho 2026 chega a Camaquã com ações voltadas à solidariedade e à autonomia das famílias vulneráveis no inverno gaúcho.

### Palavras-chave ###
campanha do agasalho Camaquã, inverno 2026, Costa Doce, assistência social Camaquã, agasalho RS
""",

    "5b7dd5a19fab42dfa2fa1abff1b84af7bb5b3381": """### Título ###
Vereador aciona Anatel contra falhas de internet e telefonia da TIM em Camaquã e região

### Artigo ###
O vereador Vladimir Tili protocolou solicitação junto à Agência Nacional de Telecomunicações — Anatel — cobrando providências contra as falhas recorrentes nos serviços de telefonia móvel e internet da operadora TIM em Camaquã e nos municípios vizinhos. A ação legislativa busca esclarecimentos sobre as causas das interrupções e medidas concretas para reduzir os problemas de conectividade que afetam moradores e produtores rurais da região.

Segundo a solicitação encaminhada pela Câmara Municipal, os problemas persistentes no sinal de voz e dados da operadora têm gerado prejuízos à rotina dos usuários, especialmente em áreas rurais da Costa Doce onde a conectividade é fundamental para a comunicação e o funcionamento das atividades do campo.

A Anatel é o órgão responsável pela regulação e fiscalização dos serviços de telecomunicações no Brasil e tem o poder de exigir melhorias das operadoras quando os serviços não atendem aos padrões estabelecidos. O vereador aguarda resposta formal do regulador sobre as providências que serão adotadas.

### Legenda sugerida ###
Câmara de Camaquã pressiona Anatel para melhorar sinal da TIM na região da Costa Doce e municípios vizinhos.

### Palavras-chave ###
Anatel Camaquã, TIM falhas internet, telefonia móvel Costa Doce, vereador Vladimir Tili, conectividade RS
""",

    "a3533cde66a8c4980dc360e776b8a90f9bd35335": """### Título ###
Tapes: prefeitura e pescadores da Colônia Z-43 planejam ações preventivas diante da cheia

### Artigo ###
O prefeito de Tapes, Luiz Carlos Coutinho Garcez, recebeu em seu gabinete Kelly Rigon, representante da Colônia dos Pescadores Z-43, para uma reunião de planejamento sobre as ações preventivas diante do período de chuvas intensas e do risco de elevação do nível das águas que pode impactar as famílias que vivem da pesca na região.

O encontro reuniu ainda outras autoridades municipais para discutir os fluxos de trabalho e os protocolos de monitoramento que serão adotados para proteger a comunidade pesqueira. A Colônia Z-43 é uma das entidades mais representativas do setor pesqueiro da Costa Doce, atuando diretamente com as famílias que dependem da Lagoa dos Patos e dos arroios da região.

Com o histórico de cheias que afetou o litoral sul gaúcho nos últimos anos, a articulação preventiva entre o poder público e as entidades da pesca é considerada fundamental para minimizar danos materiais e garantir a segurança dos pescadores e suas famílias durante os períodos de maior precipitação.

### Legenda sugerida ###
Tapes reforça prevenção: prefeitura e pescadores da Z-43 articulam medidas para proteger a comunidade pesqueira diante das chuvas.

### Palavras-chave ###
Tapes cheia, Colônia Z-43, pescadores Costa Doce, prevenção enchente RS, Lagoa dos Patos
""",

    "394b624e90eb180abfce5ed085d50699b0cba0cf": """### Título ###
Arambaré libera vacina da gripe para toda a população a partir desta segunda-feira

### Artigo ###
A Secretaria Municipal de Saúde de Arambaré anunciou que, a partir desta segunda-feira, 15 de junho, a vacina contra a gripe estará disponível para toda a população do município com idade a partir de 6 meses de vida. A ampliação do público-alvo ocorre no início do inverno gaúcho, período de maior circulação do vírus influenza.

O atendimento para vacinação acontece nos horários das 8h às 11h30 e das 13h às 16h. A Prefeitura informou que os grupos prioritários — como idosos, gestantes, crianças e profissionais de saúde — continuam sendo vacinados normalmente, com a expansão agora abrangendo todos os moradores que ainda não se imunizaram.

A vacinação contra a gripe é gratuita e oferecida pelo Sistema Único de Saúde. Com temperaturas caindo em toda a Costa Doce, a Secretaria de Saúde recomenda que os moradores aproveitem a ampliação do calendário vacinal para se protegerem antes do período mais rigoroso do inverno.

### Legenda sugerida ###
Arambaré amplia vacinação contra gripe para toda a população a partir de segunda-feira, 15 de junho, no horário comercial.

### Palavras-chave ###
vacina gripe Arambaré, vacinação influenza RS, Secretaria de Saúde Arambaré, Costa Doce saúde, inverno 2026
""",

    "ed8d120b785029e0cb62e3da9a91f9a966a30562": """### Título ###
Alta procura leva Cristal a realizar sorteio público dos beneficiários do Programa Milho 100%

### Artigo ###
O município de Cristal realizou na manhã desta sexta-feira, 12 de junho, o sorteio público dos beneficiários do Programa Milho 100%. A medida foi necessária porque o número de inscrições de agricultores superou a quantidade de sacas de milho disponíveis para distribuição pelo município nesta edição do programa.

Para garantir transparência e igualdade de oportunidades entre todos os inscritos, a Prefeitura de Cristal optou pela realização de um sorteio aberto, com a participação de representantes das famílias agricultoras e da comunidade local. A iniciativa é parte do esforço municipal para apoiar a produção familiar e reduzir os custos com insumos no campo.

O Programa Milho 100% é voltado para agricultores familiares e pequenos produtores, oferecendo sementes a preços acessíveis ou de forma gratuita como incentivo ao plantio na região. A grande adesão ao programa em Cristal reflete a necessidade de mais apoio às famílias rurais que buscam alternativas para custear a produção diante dos preços ainda elevados dos insumos agrícolas.

### Legenda sugerida ###
Cristal realiza sorteio público do Programa Milho 100% após grande procura superar a oferta de sacas disponíveis.

### Palavras-chave ###
Programa Milho 100% Cristal, sorteio beneficiários Cristal RS, agricultura familiar Costa Doce, insumos agrícolas RS, sementes milho RS
""",

    "e20c1c924e3c8c691279f7b5e6788daf274bbf9f": """### Título ###
São Lourenço do Sul registra 84 mm de chuva e aciona monitoramento de arroios

### Artigo ###
A Prefeitura de São Lourenço do Sul, por meio da Defesa Civil e das equipes de monitoramento, informou que o município registrou 84 milímetros de chuva nas últimas 12 horas na localidade do Passo do Pinto. O volume expressivo de precipitação causou a elevação do nível do arroio no Passo do Candombe, que está sendo acompanhado de perto pelas equipes municipais.

As equipes seguem em estado de alerta nas regiões do interior, monitorando as condições hidrometeorológicas em pontos críticos do município para orientar moradores e produtores rurais sobre eventuais riscos. A Defesa Civil orienta a população das áreas mais baixas e próximas aos cursos d'água a redobrar os cuidados e acompanhar os boletins oficiais.

O período de junho registra historicamente maior volume de chuvas no Sul do Rio Grande do Sul, com risco elevado de enxurradas e transbordamentos de arroios em áreas rurais. São Lourenço do Sul, por sua localização na Costa Doce e pelas características do relevo da região, é um dos municípios que exige monitoramento mais frequente nesta época do ano.

### Legenda sugerida ###
São Lourenço do Sul registra 84 mm em 12 horas no Passo do Pinto; Defesa Civil monitora arroio Passo do Candombe.

### Palavras-chave ###
São Lourenço do Sul chuva, Defesa Civil SLS, arroio Passo do Candombe, 84mm chuva RS, enchente Costa Doce
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores gaúchos cobram aprovação da renegociação de dívidas no Senado antes do início da próxima safra

### Artigo ###
Produtores rurais do Rio Grande do Sul vivem com apreensão crescente diante do risco de a renegociação das dívidas agrícolas não ser aprovada pelo Senado Federal. O temor no setor é que, sem a aprovação da medida, os agricultores percam o acesso ao crédito rural necessário para financiar o plantio da próxima safra, comprometendo a produção de grãos no estado.

No Rio Grande do Sul, um dos estados com maior volume de endividamento no campo brasileiro, a tensão se reflete diretamente nas propriedades rurais. Famílias que dependem do financiamento agrícola aguardam uma definição urgente do Legislativo para planejar os próximos meses de atividade no campo.

O setor alerta que a indefinição sobre a renegociação das dívidas afeta não apenas o planejamento financeiro das propriedades, mas também a capacidade de adquirir insumos, sementes e defensivos a tempo para o início do período de plantio. A pressão cresce sobre os parlamentares para que o tema seja votado com urgência, garantindo que os produtores gaúchos possam se organizar para a nova temporada agrícola com segurança.

### Legenda sugerida ###
Produtores gaúchos aguardam votação no Senado sobre renegociação de dívidas agrícolas para planejar a próxima safra.

### Palavras-chave ###
renegociação dívidas agrícolas RS, Senado crédito rural, produtores gaúchos dívidas, safra RS 2026, agronegócio RS
"""
}


def main():
    # Monta o pauta_<date>.json
    from datetime import datetime, timezone
    pauta_json = {
        "data": DATE,
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "total": len(PAUTA_ANGULADA),
        "pauta": PAUTA_ANGULADA
    }

    pauta_path = STATE / f"pauta_{DATE}.json"
    with open(pauta_path, "w", encoding="utf-8") as f:
        json.dump(pauta_json, f, ensure_ascii=False, indent=2)
    print(f"[angular] Escrito: {pauta_path}")

    # Escreve matérias longas
    for id_hash, conteudo in MATERIAS.items():
        md_path = MATERIAS_DIR / f"{id_hash}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(conteudo.strip() + "\n")
        print(f"[angular] Matéria: {md_path.name}")

    # Sumário
    publicar = [i for i in PAUTA_ANGULADA if i.get("decisao_final") == "PUBLICAR"]
    rebaixar = [i for i in PAUTA_ANGULADA if i.get("decisao_final") == "REBAIXAR"]
    bloquear = [i for i in PAUTA_ANGULADA if i.get("decisao_final") == "BLOQUEAR"]
    alerta   = [i for i in PAUTA_ANGULADA if i.get("decisao_final") == "ALERTA_HUMANO"]

    print(f"\n[angular] === SUMÁRIO ===")
    print(f"[angular] PUBLICAR:  {len(publicar)} (quota: 10)")
    print(f"[angular] REBAIXAR:  {len(rebaixar)}")
    print(f"[angular] BLOQUEAR:  {len(bloquear)}")
    print(f"[angular] ALERTA:    {len(alerta)}")
    print(f"[angular] Matérias longas: {len(MATERIAS)}")
    print(f"[angular] Total na pauta: {len(PAUTA_ANGULADA)}")

    for i, item in enumerate(publicar, 1):
        print(f"  {i:02d}. [{item.get('tag_principal','')}] {item.get('titulo_sultv','')[:80]}")


if __name__ == "__main__":
    main()
