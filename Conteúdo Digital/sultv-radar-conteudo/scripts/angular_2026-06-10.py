#!/usr/bin/env python3
"""
angular_2026-06-10.py — angulação editorial + redação no fluxo cowork-faz-tudo.

Pauta de 2026-06-10 — angulação Claude na sessão cowork.
Lê state/aprovadas_2026-06-10.json, gera state/pauta_2026-06-10.json com
decisao_final (PUBLICAR/REBAIXAR/BLOQUEAR) e escreve as matérias longas.

REGRA 12 (INEGOCIÁVEL): nenhum texto menciona veículo de comunicação.
Atribuição apenas a fontes primárias institucionais.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-10"


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
    # 0 — Cresol Camaquã: educação financeira + bem-estar emocional — PUBLICAR materia_longa
    "0dc297418c5e4a9ebe4fd0c6b8ba21643551ff7b": {
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Cresol Camaquã lança projeto que une educação financeira e bem-estar no trabalho",
        "chamada_faixa": "Camaquã une finanças e bem-estar no trabalho",
        "subtitulo": "Iniciativa leva conversas dinâmicas às empresas para humanizar o cuidado com o dinheiro e enfrentar os efeitos do endividamento.",
        "lead": "A Cresol de Camaquã lançou um projeto que une educação financeira e bem-estar emocional no ambiente de trabalho. A proposta leva conversas dinâmicas às empresas da região para humanizar o cuidado com o dinheiro e enfrentar os impactos emocionais do endividamento entre os trabalhadores.",
        "ganchos_3": [
            "Projeto une educação financeira e bem-estar no trabalho em Camaquã",
            "Conversas dinâmicas levam o tema dinheiro para dentro das empresas",
            "Iniciativa enfrenta os efeitos emocionais do endividamento"
        ],
        "angulo_editorial": "Educação financeira aplicada com recorte de bem-estar no trabalho, em cidade-núcleo (Camaquã/Costa Doce); pauta positiva e de serviço, sem teor médico-prescritivo, ancorada em iniciativa institucional de cooperativa de crédito.",
        "fontes_complementares_sugeridas": ["Cresol Camaquã", "Sebrae RS", "associações empresariais de Camaquã"],
        "lead_materia_longa": "A Cresol de Camaquã lançou um projeto que une educação financeira e bem-estar emocional no ambiente de trabalho, levando conversas dinâmicas às empresas da região.",
        "post_instagram": {
            "caption": "Falar de dinheiro também é cuidar das pessoas. A Cresol de Camaquã lançou um projeto que une educação financeira e bem-estar no trabalho, com conversas dinâmicas dentro das empresas para enfrentar os efeitos do endividamento. Organizar as contas alivia o bolso e a cabeça.",
            "hashtags": ["#Camaquã", "#EducaçãoFinanceira", "#BemEstar", "#CostaDoce", "#Trabalho", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Dinheiro e saúde andam juntos.",
            "desenvolvimento_45s": "A Cresol de Camaquã lançou um projeto que une educação financeira e bem-estar no ambiente de trabalho. A ideia é levar conversas dinâmicas para dentro das empresas, ajudando os trabalhadores a organizar o orçamento, planejar gastos e enfrentar os efeitos emocionais do endividamento. Quando as contas saem do vermelho, sobra tranquilidade para a vida toda.",
            "fechamento_8s": "Cuidar do bolso é cuidar de quem trabalha.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental leve e otimista"
        },
        "tag_thumbnail": "Educação financeira em Camaquã",
        "briefing_visual": {
            "descricao_pt": "Roda de conversa de trabalhadores em ambiente de empresa no interior do RS, clima acolhedor, sem rostos identificáveis em primeiro plano",
            "query_en": ["workplace group discussion meeting", "financial education workshop people", "team conversation office brazil"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "Warm group conversation among workers in a small-town company in southern Brazil, people seated in a circle, soft daylight, no readable faces in foreground, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Iniciativa concreta e positiva em cidade-núcleo (Camaquã), com tema de serviço (educação financeira) sem conteúdo médico-prescritivo"
    },

    # 1 — Campanha do Agasalho Camaquã — PUBLICAR nota_curta
    "133131206e84391ce72c4411031597e997522067": {
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "Camaquã lança Campanha do Agasalho para o inverno de 2026",
        "chamada_faixa": "Camaquã lança Campanha do Agasalho 2026",
        "subtitulo": "Mobilização arrecada roupas e cobertores para famílias do município enfrentarem o frio.",
        "lead": "Camaquã lançou a Campanha do Agasalho 2026 para arrecadar roupas, calçados e cobertores destinados a famílias em situação de vulnerabilidade durante o inverno. Os pontos de coleta e a lista de itens necessários já estão divulgados no município.",
        "ganchos_3": [
            "Campanha do Agasalho 2026 mobiliza Camaquã contra o frio",
            "Arrecadação de roupas, calçados e cobertores",
            "Pontos de coleta abertos no município"
        ],
        "angulo_editorial": "Serviço e solidariedade no inverno, cidade-núcleo (Camaquã); chamada para participação da comunidade.",
        "fontes_complementares_sugeridas": ["Prefeitura de Camaquã", "Secretaria de Assistência Social de Camaquã"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "O frio chegou e a solidariedade também. Camaquã lançou a Campanha do Agasalho 2026, que arrecada roupas, calçados e cobertores para famílias do município. Aquele casaco parado no armário pode aquecer alguém neste inverno. Procure os pontos de coleta e participe.",
            "hashtags": ["#Camaquã", "#CampanhaDoAgasalho", "#Solidariedade", "#Inverno2026", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O frio chegou, a solidariedade também.",
            "desenvolvimento_45s": "Camaquã lançou a Campanha do Agasalho 2026 para arrecadar roupas, calçados e cobertores para famílias que enfrentam o inverno em situação de vulnerabilidade. Aquela peça que está parada no armário pode aquecer alguém. A comunidade pode deixar as doações nos pontos de coleta espalhados pelo município.",
            "fechamento_8s": "Doe e aqueça uma vida neste inverno.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental acolhedor"
        },
        "tag_thumbnail": "Campanha do Agasalho",
        "briefing_visual": {
            "descricao_pt": "Caixas de doação com roupas e cobertores dobrados em ponto de coleta, mãos colocando um casaco, sem rostos",
            "query_en": ["winter clothes donation box", "warm clothing donation drive", "blankets coats charity collection"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Donation boxes filled with folded winter clothes and blankets at a collection point, hands placing a coat, no faces, warm indoor light, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço solidário sazonal em cidade-núcleo (Camaquã), com utilidade pública clara"
    },

    # 3 — Declaração Anual de Rebanho Tapes — PUBLICAR materia_longa (agro)
    "d69906d280f27e21bcfe4af39db247662985bf35": {
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Produtores de Tapes têm até 30 de junho para a Declaração Anual de Rebanho",
        "chamada_faixa": "Declaração de Rebanho em Tapes vai até 30 de junho",
        "subtitulo": "Documento é obrigatório para todos os produtores com animais de produção e pode ser feito on-line ou presencialmente.",
        "lead": "Os produtores rurais de Tapes têm até 30 de junho para entregar a Declaração Anual de Rebanho 2026. O documento é obrigatório para todos os criadores que possuem animais de produção e pode ser preenchido pela internet ou presencialmente na Inspetoria de Defesa Agropecuária do município.",
        "ganchos_3": [
            "Prazo da Declaração Anual de Rebanho 2026 termina em 30 de junho",
            "Documento é obrigatório para quem tem animais de produção",
            "Declaração pode ser feita on-line ou presencialmente em Tapes"
        ],
        "angulo_editorial": "Serviço agropecuário de prazo, cidade-núcleo (Tapes); informação obrigatória para o produtor, atribuída à Secretaria Municipal de Agricultura.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Agricultura de Tapes", "Inspetoria de Defesa Agropecuária de Tapes", "SEAPI/RS"],
        "lead_materia_longa": "Os produtores rurais de Tapes têm até 30 de junho para entregar a Declaração Anual de Rebanho 2026, obrigatória para todos os criadores com animais de produção.",
        "post_instagram": {
            "caption": "Produtor de Tapes, não deixe para a última hora! A Declaração Anual de Rebanho 2026 vai até 30 de junho e é obrigatória para todo mundo que tem animais de produção. Dá para fazer pela internet, no Produtor Online, ou presencialmente na Inspetoria de Defesa Agropecuária. Marque na agenda.",
            "hashtags": ["#Tapes", "#Agro", "#DeclaraçãoDeRebanho", "#DefesaAgropecuária", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Produtor de Tapes, fica o aviso.",
            "desenvolvimento_45s": "Quem tem animais de produção em Tapes precisa entregar a Declaração Anual de Rebanho 2026 até o dia 30 de junho. O documento é obrigatório e pode ser feito pela internet, no sistema Produtor Online, ou presencialmente na Inspetoria de Defesa Agropecuária do município. A declaração é fundamental para a defesa sanitária do rebanho e para o planejamento das ações de saúde animal na região.",
            "fechamento_8s": "Prazo termina em 30 de junho.",
            "cta_5s": "Mais informações no SulTV.",
            "trilha_sugerida": "instrumental objetivo"
        },
        "tag_thumbnail": "Declaração de Rebanho",
        "briefing_visual": {
            "descricao_pt": "Gado bovino em campo aberto no pampa gaúcho durante o dia, sem pessoas, cerca ao fundo",
            "query_en": ["cattle herd pasture brazil", "beef cattle field daytime", "cows grazing fence pampas"],
            "evitar": ["pessoas", "marcas de gado legíveis", "texto", "logos"],
            "prompt_ia": "Herd of beef cattle grazing on open green pasture in southern Brazil during the day, wire fence in the background, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço agropecuário obrigatório com prazo definido em cidade-núcleo (Tapes); alto interesse da audiência rural"
    },

    # 7 — Milho 100% Cristal — PUBLICAR nota_curta
    "3bcd71781bcfc407288395c051708c5803ee00d4": {
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "Agricultores familiares de Cristal já podem retirar sementes de milho gratuitas",
        "chamada_faixa": "Cristal libera sementes de milho gratuitas",
        "subtitulo": "Programa Milho 100% atende agricultores familiares na Secretaria de Desenvolvimento Rural a partir desta terça-feira.",
        "lead": "Os agricultores familiares de Cristal interessados em receber sementes de milho gratuitas pelo programa Milho 100%, do Governo do Estado, já podem comparecer à Secretaria de Desenvolvimento Rural do município, na Rua Marau, nº 39, a partir desta terça-feira (9).",
        "ganchos_3": [
            "Programa Milho 100% distribui sementes gratuitas em Cristal",
            "Atendimento na Secretaria de Desenvolvimento Rural, na Rua Marau, 39",
            "Iniciativa fortalece a recuperação produtiva da agricultura familiar"
        ],
        "angulo_editorial": "Serviço agro de distribuição de insumos para agricultura familiar, cidade segunda-camada (Cristal); informação prática de onde e quando retirar.",
        "fontes_complementares_sugeridas": ["Secretaria de Desenvolvimento Rural de Cristal", "SEAPI/RS"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Agricultor familiar de Cristal, a semente de milho gratuita chegou! Pelo programa Milho 100%, do Governo do Estado, basta comparecer à Secretaria de Desenvolvimento Rural, na Rua Marau, 39, a partir desta terça (9), com os documentos. O programa ajuda a recuperar e fortalecer a lavoura. Aproveite.",
            "hashtags": ["#Cristal", "#Agro", "#Milho100", "#AgriculturaFamiliar", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Semente de milho de graça em Cristal.",
            "desenvolvimento_45s": "Os agricultores familiares de Cristal já podem retirar sementes de milho gratuitas pelo programa Milho 100%, do Governo do Estado. O atendimento começa nesta terça-feira na Secretaria de Desenvolvimento Rural, na Rua Marau, número 39. É preciso levar os documentos pessoais. O programa é voltado à recuperação produtiva da agricultura familiar e ao fortalecimento das lavouras.",
            "fechamento_8s": "Corra que a procura é grande.",
            "cta_5s": "Detalhes no SulTV.",
            "trilha_sugerida": "instrumental animado"
        },
        "tag_thumbnail": "Sementes de milho gratuitas",
        "briefing_visual": {
            "descricao_pt": "Mãos segurando sementes de milho douradas, sacaria de sementes ao fundo, ambiente rural, sem rostos",
            "query_en": ["corn seeds hands closeup", "maize seed bags farm", "yellow corn kernels planting"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Close-up of hands holding golden corn seeds with seed sacks in the background, rural setting, daylight, no faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço agro concreto e datado para agricultura familiar; utilidade direta ao público rural"
    },

    # 8 — Coleta de sangue São Lourenço do Sul — PUBLICAR nota_curta
    "25f6b8e8fb936f33b84ef1e16bfdf415c285d622": {
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "Coleta de sangue volta a São Lourenço do Sul no dia 16 de junho",
        "chamada_faixa": "Coleta de sangue volta a São Lourenço dia 16",
        "subtitulo": "Ação na Santa Casa, em parceria com o Hemopel, abre 50 vagas e deve passar a ser mensal.",
        "lead": "A coleta de sangue volta a São Lourenço do Sul no dia 16 de junho, na Santa Casa de Misericórdia, em parceria com o Hemopel. A ação abre 50 vagas para doadores e a previsão é de que passe a ocorrer mensalmente, ampliando as oportunidades de doação no município.",
        "ganchos_3": [
            "Coleta de sangue retorna a São Lourenço do Sul em 16 de junho",
            "Santa Casa e Hemopel abrem 50 vagas para doadores",
            "Previsão é de coletas mensais no município"
        ],
        "angulo_editorial": "Serviço de saúde pública e mobilização, cidade-núcleo (São Lourenço do Sul); convocação de doadores, sem teor médico-prescritivo.",
        "fontes_complementares_sugeridas": ["Santa Casa de São Lourenço do Sul", "Hemopel", "Secretaria Municipal de Saúde de São Lourenço do Sul"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Doar sangue leva alguns minutos e pode salvar vidas. No dia 16 de junho, a coleta volta a São Lourenço do Sul, na Santa Casa, em parceria com o Hemopel, com 50 vagas. A ideia é que passe a ser mensal. Talvez você nunca conheça quem vai receber, mas o seu gesto faz toda a diferença.",
            "hashtags": ["#SãoLourençoDoSul", "#DoaçãoDeSangue", "#Hemopel", "#Saúde", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Doar sangue salva vidas.",
            "desenvolvimento_45s": "A coleta de sangue volta a São Lourenço do Sul no dia 16 de junho, na Santa Casa de Misericórdia, em parceria com o Hemopel. São 50 vagas para doadores, e a previsão é de que a ação passe a acontecer todos os meses, fortalecendo os estoques que são tão importantes para quem enfrenta cirurgias e tratamentos. Bastam alguns minutos para ajudar quem precisa.",
            "fechamento_8s": "Dia 16 de junho, na Santa Casa.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental emotivo sóbrio"
        },
        "tag_thumbnail": "Doação de sangue",
        "briefing_visual": {
            "descricao_pt": "Bolsa de coleta de sangue e materiais de hemocentro sobre mesa, ambiente clínico claro, sem pessoas identificáveis",
            "query_en": ["blood donation bag clinic", "blood collection equipment", "blood bank donation supplies"],
            "evitar": ["rostos de pacientes", "marcas", "texto", "logos"],
            "prompt_ia": "Blood collection bag and donation supplies on a table in a bright clinical setting, no identifiable people, soft daylight, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Mobilização de saúde pública com data e local definidos em cidade-núcleo (São Lourenço do Sul)"
    },

    # 13 — Aldir Blanc Barra do Ribeiro — PUBLICAR materia_longa
    "ed5de350ac85eb327fb2dd3a082da35d5be793ac": {
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Barra do Ribeiro habilita 33 propostas culturais em marco da Lei Aldir Blanc",
        "chamada_faixa": "Barra do Ribeiro habilita 33 projetos de cultura",
        "subtitulo": "Política Nacional Aldir Blanc registra recorde de inscrições habilitadas no Ciclo 2 do município.",
        "lead": "Barra do Ribeiro alcançou um marco histórico na área cultural com 33 propostas habilitadas no Ciclo 2 da Política Nacional Aldir Blanc. O resultado soma 11 habilitados no Edital 001/2026 e 22 no Edital 002/2026, demonstrando a força da produção cultural do município da Costa Doce.",
        "ganchos_3": [
            "Barra do Ribeiro habilita 33 propostas culturais pela Lei Aldir Blanc",
            "São 11 habilitados no Edital 001 e 22 no Edital 002 de 2026",
            "Marco histórico de inscrições no Ciclo 2 da política cultural"
        ],
        "angulo_editorial": "Fomento à cultura local com números concretos e recorde, cidade-núcleo (Barra do Ribeiro); pauta positiva de desenvolvimento cultural, atribuída à Prefeitura.",
        "fontes_complementares_sugeridas": ["Prefeitura de Barra do Ribeiro", "Secretaria de Cultura de Barra do Ribeiro", "Ministério da Cultura"],
        "lead_materia_longa": "Barra do Ribeiro alcançou um marco histórico na área cultural com 33 propostas habilitadas no Ciclo 2 da Política Nacional Aldir Blanc.",
        "post_instagram": {
            "caption": "A cultura de Barra do Ribeiro está em festa! O município habilitou 33 propostas culturais no Ciclo 2 da Lei Aldir Blanc — 11 no Edital 001/2026 e 22 no Edital 002/2026, um recorde. É a criatividade e o compromisso dos agentes culturais movimentando a cidade. A lista completa sai nos canais oficiais da Prefeitura.",
            "hashtags": ["#BarraDoRibeiro", "#Cultura", "#LeiAldirBlanc", "#CostaDoce", "#FomentoCultural", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A cultura de Barra do Ribeiro em festa.",
            "desenvolvimento_45s": "Barra do Ribeiro bateu recorde de inscrições culturais habilitadas no Ciclo 2 da Política Nacional Aldir Blanc. Foram 33 propostas aprovadas, sendo 11 no Edital 001 e 22 no Edital 002 deste ano. O número mostra a força dos artistas e produtores culturais do município, que vão poder tirar seus projetos do papel com o apoio da política de fomento. A lista completa dos habilitados é divulgada nos canais oficiais da Prefeitura.",
            "fechamento_8s": "Recorde histórico para a cultura local.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental cultural alegre"
        },
        "tag_thumbnail": "Cultura em Barra do Ribeiro",
        "briefing_visual": {
            "descricao_pt": "Apresentação cultural em palco de cidade pequena do interior do RS, plateia ao fundo, luzes quentes, sem rostos em close",
            "query_en": ["small town cultural stage performance", "community arts event audience", "local culture festival brazil"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "Cultural performance on a community stage in a small town in southern Brazil, audience in the background, warm stage lights, no faces in close-up, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato concreto com números oficiais e recorde cultural em cidade-núcleo (Barra do Ribeiro)"
    },

    # 18 — Creche Guaíba — PUBLICAR nota_curta
    "fe9aef729ee3e5e99f1a83607eaf91ba08acf3af": {
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "Guaíba abre 2º período de inscrições para creche até 15 de junho",
        "chamada_faixa": "Guaíba abre inscrições para creche até dia 15",
        "subtitulo": "Vagas são para a etapa de 0 a 3 anos da Rede Municipal de Ensino no ano letivo de 2026.",
        "lead": "Guaíba abriu o 2º período de inscrições para vagas na etapa creche, de 0 a 3 anos, da Rede Municipal de Ensino para o ano letivo de 2026. As inscrições vão de 8 a 15 de junho e podem ser feitas pelo site da Prefeitura, nas escolas municipais ou na Secretaria Municipal de Educação.",
        "ganchos_3": [
            "Guaíba abre 2º período de inscrições para creche",
            "Inscrições de 8 a 15 de junho para crianças de 0 a 3 anos",
            "Cadastro pode ser feito on-line, nas escolas ou na Secretaria de Educação"
        ],
        "angulo_editorial": "Serviço educacional com prazo, cidade-núcleo (Guaíba); informação prática para famílias.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Educação de Guaíba", "Prefeitura de Guaíba"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Atenção, famílias de Guaíba! Está aberto o 2º período de inscrições para a creche (0 a 3 anos) da Rede Municipal de Ensino, para 2026. O prazo vai de 8 a 15 de junho e dá para se inscrever pelo site da Prefeitura, nas escolas municipais ou na Secretaria de Educação. Não deixe para a última hora.",
            "hashtags": ["#Guaíba", "#Educação", "#Creche", "#Matrículas2026", "#RioGrandeDoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Famílias de Guaíba, atenção.",
            "desenvolvimento_45s": "Guaíba abriu o segundo período de inscrições para vagas na creche, etapa de zero a três anos, da Rede Municipal de Ensino para o ano letivo de 2026. As inscrições vão de 8 a 15 de junho e podem ser feitas pelo site da Prefeitura, nas escolas municipais ou na Secretaria Municipal de Educação. A etapa é voltada às famílias que não se inscreveram antes ou que precisam atualizar dados.",
            "fechamento_8s": "Prazo termina dia 15 de junho.",
            "cta_5s": "Mais informações no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Inscrições para creche",
        "briefing_visual": {
            "descricao_pt": "Sala de educação infantil colorida e vazia com brinquedos e mesinhas, ambiente acolhedor, sem crianças identificáveis",
            "query_en": ["empty daycare classroom colorful", "preschool room toys tables", "kindergarten classroom interior"],
            "evitar": ["crianças identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Bright, colorful empty early-childhood classroom with small tables and toys, welcoming atmosphere, no children, daylight, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço educacional com prazo curto em cidade-núcleo (Guaíba); utilidade direta às famílias"
    },

    # 19 — HOB robótica FIERGS Pelotas — PUBLICAR materia_longa
    "d837c631025a0927c2a737aeb12deaa42536357c": {
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Projeto leva robótica a professores e alunos de escolas municipais de Pelotas",
        "chamada_faixa": "Robótica chega às escolas municipais de Pelotas",
        "subtitulo": "Iniciativa Hands on Bot, do Sistema FIERGS, prevê formação de docentes e criação de clubes de robótica para estudantes.",
        "lead": "Pelotas recebe o projeto Hands on Bot (HOB), do Sistema FIERGS, que leva a robótica para professores e alunos das escolas municipais. A iniciativa prevê formação inovadora para docentes e a criação de clubes de robótica para estudantes do 6º ao 9º ano do Ensino Fundamental.",
        "ganchos_3": [
            "Projeto Hands on Bot leva robótica às escolas municipais de Pelotas",
            "Formação de professores e clubes de robótica para alunos",
            "Iniciativa do Sistema FIERGS mira o Ensino Fundamental"
        ],
        "angulo_editorial": "Educação e tecnologia em Pelotas (Costa Doce ampliada); pauta positiva de inovação no ensino público, atribuída ao Sistema FIERGS.",
        "fontes_complementares_sugeridas": ["Sistema FIERGS", "SESI/SENAI-RS", "Secretaria Municipal de Educação de Pelotas"],
        "lead_materia_longa": "Pelotas recebe o projeto Hands on Bot (HOB), do Sistema FIERGS, que leva a robótica para professores e alunos das escolas municipais.",
        "post_instagram": {
            "caption": "Robótica na escola pública de Pelotas! O projeto Hands on Bot, do Sistema FIERGS, vai formar professores e criar clubes de robótica para alunos do 6º ao 9º ano da rede municipal. É a tecnologia abrindo portas para o futuro dos estudantes da Costa Doce. Preparar a molecada hoje é colher inovação amanhã.",
            "hashtags": ["#Pelotas", "#Robótica", "#Educação", "#Tecnologia", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Robótica na escola pública de Pelotas.",
            "desenvolvimento_45s": "Pelotas recebe o projeto Hands on Bot, do Sistema FIERGS, que leva a robótica para dentro das escolas municipais. A proposta forma os professores com uma metodologia inovadora e cria clubes de robótica para os alunos do 6º ao 9º ano do Ensino Fundamental. Mais do que montar robôs, a ideia é desenvolver raciocínio lógico, trabalho em equipe e o gosto pela ciência e pela tecnologia desde cedo.",
            "fechamento_8s": "Tecnologia abrindo portas para o futuro.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental moderno energético"
        },
        "tag_thumbnail": "Robótica nas escolas",
        "briefing_visual": {
            "descricao_pt": "Mesa com kit de robótica educacional, peças e pequeno robô montado, ambiente de sala de aula, sem rostos",
            "query_en": ["educational robotics kit classroom", "students robot building parts", "STEM robotics learning"],
            "evitar": ["crianças identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "Table with an educational robotics kit, components and a small assembled robot in a classroom setting, hands working in the background, no identifiable faces, daylight, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Inovação no ensino público em Pelotas; pauta de educação e tecnologia alinhada ao foco editorial"
    },

    # 22 — Danças Gaúchas Dom Feliciano — PUBLICAR nota_curta
    "8a32910f923087ad173a41aa10a66817ed34be8c": {
        "formato_sugerido": "nota_curta",
        "titulo_sultv": "Projeto de danças gaúchas fortalece a cultura nas escolas de Dom Feliciano",
        "chamada_faixa": "Danças gaúchas nas escolas de Dom Feliciano",
        "subtitulo": "Atividade no contraturno escolar aproxima crianças das tradições do Rio Grande do Sul.",
        "lead": "As escolas de Ensino Fundamental da Rede Municipal de Dom Feliciano desenvolvem, no contraturno escolar, um Projeto de Danças Gaúchas que aproxima as crianças das tradições do Rio Grande do Sul. As aulas valorizam a cultura local e contribuem para a educação integral dos estudantes.",
        "ganchos_3": [
            "Projeto de danças gaúchas movimenta escolas de Dom Feliciano",
            "Atividade ocorre no contraturno escolar",
            "Crianças conhecem e valorizam as tradições do RS"
        ],
        "angulo_editorial": "Cultura e educação em cidade-núcleo (Dom Feliciano); pauta leve e identitária, valorização das tradições gaúchas.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Educação de Dom Feliciano", "Prefeitura de Dom Feliciano"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Em Dom Feliciano, a tradição entra na escola! Crianças da rede municipal participam de um projeto de danças gaúchas no contraturno, aprendendo a valorizar a cultura do Rio Grande do Sul enquanto desenvolvem coordenação e trabalho em grupo. Cultura que se ensina cedo, fica para a vida toda.",
            "hashtags": ["#DomFeliciano", "#Cultura", "#DançasGaúchas", "#Tradição", "#RioGrandeDoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A tradição entra na escola.",
            "desenvolvimento_45s": "As escolas da Rede Municipal de Dom Feliciano desenvolvem, no contraturno escolar, um projeto de danças gaúchas que leva as crianças a conhecer e valorizar as tradições do Rio Grande do Sul. Além de despertar o gosto pela cultura, a atividade contribui para a coordenação motora, a disciplina e o trabalho em equipe dos estudantes. É a identidade gaúcha sendo cultivada desde cedo.",
            "fechamento_8s": "Cultura que fica para a vida toda.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "vaneira ou xote instrumental"
        },
        "tag_thumbnail": "Danças gaúchas na escola",
        "briefing_visual": {
            "descricao_pt": "Crianças dançando dança tradicional gaúcha em pátio de escola, trajes típicos coloridos, sem rostos identificáveis em close",
            "query_en": ["traditional folk dance children", "gaucho dance costume brazil", "school cultural dance performance"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "Children performing a traditional gaucho folk dance in a school courtyard, colorful regional costumes, movement and joy, no identifiable faces in close-up, daylight, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura e tradição gaúcha em cidade-núcleo (Dom Feliciano); pauta leve e identitária on-brand"
    },

    # 24 — Renegociação de dívidas rurais Senado — PUBLICAR materia_longa
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "formato_sugerido": "materia_longa",
        "titulo_sultv": "Produtores do RS acompanham com apreensão a renegociação de dívidas rurais",
        "chamada_faixa": "RS teme travamento da renegociação de dívidas rurais",
        "subtitulo": "Setor receia perder acesso ao crédito para a próxima safra caso a proposta não avance no Congresso.",
        "lead": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas no Congresso e temem as consequências caso a proposta não seja aprovada. O principal receio do setor é ficar sem acesso ao crédito rural para financiar a próxima safra, um risco que atinge regiões produtoras de arroz e soja como a Costa Doce.",
        "ganchos_3": [
            "Produtores gaúchos temem travamento da renegociação de dívidas rurais",
            "Sem aprovação, risco é faltar crédito para a próxima safra",
            "Endividamento se agravou com estiagens e enchentes no estado"
        ],
        "angulo_editorial": "Economia do agro com impacto direto na audiência rural do RS; pauta de política agrícola sem viés partidário, ancorada nas entidades do setor e no calendário da safra.",
        "fontes_complementares_sugeridas": ["Farsul", "Federação dos Trabalhadores na Agricultura (Fetag-RS)", "Banco do Brasil", "bancada gaúcha no Congresso"],
        "lead_materia_longa": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas no Congresso e temem ficar sem acesso ao crédito para a próxima safra.",
        "post_instagram": {
            "caption": "O campo gaúcho está de olho em Brasília. Produtores do RS temem que a renegociação de dívidas rurais trave no Congresso — e, sem ela, falte crédito para financiar a próxima safra. Depois de estiagens e enchentes, o setor diz que precisa da medida para seguir plantando. O calendário agrícola não espera.",
            "hashtags": ["#Agro", "#RioGrandeDoSul", "#CréditoRural", "#Safra", "#DívidasRurais", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O campo gaúcho de olho em Brasília.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a renegociação de dívidas no Congresso. O maior medo do setor é ficar sem crédito para financiar a próxima safra, justamente depois de anos marcados por estiagens severas e pelas enchentes históricas que atingiram o estado. Sem conseguir pagar as safras frustradas, muitos produtores perderam capacidade de tomar novos financiamentos. As entidades do agro cobram celeridade, porque o calendário do plantio não espera.",
            "fechamento_8s": "Decisão é decisiva para a safra 2026/2027.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Dívidas rurais no RS",
        "briefing_visual": {
            "descricao_pt": "Lavoura de soja ou arroz no Sul do RS sob céu nublado, vista ampla, sem pessoas, clima de incerteza",
            "query_en": ["soybean field cloudy sky brazil", "rice field southern brazil wide", "farmland horizon overcast"],
            "evitar": ["pessoas identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Wide view of a soybean or rice field in southern Brazil under an overcast sky, no people, sense of uncertainty, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Economia do agro com alto impacto na audiência rural do RS; tema de política agrícola, não partidário"
    },

    # ===== REBAIXAR =====
    "77e4b4ab8c1229a770b8659ada1313ac6be02fc3": _skip("REBAIXAR", "Conteúdo de conscientização genérica sobre o Dia da Imunização, sem fato local concreto; vira nota interna"),
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip("REBAIXAR", "Notícia datada de abril/2026 (curso de qualificação) — defasada para a pauta do dia"),
    "7328151d0f689699ca147e00ec7ffb87008ee51e": _skip("REBAIXAR", "Notícia datada de janeiro/2026 (plataforma de pesca) — defasada para a pauta do dia"),
    "51061f4920f28aa2b69b4c48d49beb12ccc713a9": _skip("REBAIXAR", "Duplica o item de sementes de milho de Cristal já selecionado (item com mais detalhes operacionais)"),
    "29519749dd5200f8b069ec89882481ccf62fb734": _skip("REBAIXAR", "Tema de vacinação genérica em São Lourenço já contemplado pela coleta de sangue (item mais concreto da cidade)"),
    "94999f70347d3369dab08cf5d146cf3fcb1ed987": _skip("REBAIXAR", "Texto-fonte agregado/confuso (vários cabeçalhos misturados) sobre ferrovias; sem ângulo limpo para redação segura"),
    "1da03ab302ef5141f6aa907ff1f2b048029f1b4b": _skip("REBAIXAR", "Programa Baita Empreendedor em Guaíba — bom, mas excede a quota da cidade (creche tem prazo mais urgente)"),
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip("REBAIXAR", "Debate sobre privatizações/plebiscito tem viés político-partidário sensível (guardrail) — não publicar"),
    "49348b06a39337d964518e54a7715142418ea220": _skip("REBAIXAR", "Audiência sobre Funcriança datada de 29/maio e em Porto Alegre (fora do núcleo) — defasada"),
    "76f9e23500770062ad601dc315f86d2926860844": _skip("REBAIXAR", "Pauta climática de enquadramento nacional (MG/BA), sem âncora concreta no Sul-RS"),
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": _skip("REBAIXAR", "Apreensão de produtos (fiscalização) sem âncora em cidade-núcleo; baixo interesse regional específico"),
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": _skip("REBAIXAR", "Apreensão de alimentos (fiscalização) sem âncora em cidade-núcleo; baixo interesse regional específico"),

    # ===== BLOQUEAR =====
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip("BLOQUEAR", "Edital de penalidade — conteúdo procedural/administrativo, sem valor editorial (guardrail edital)"),
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip("BLOQUEAR", "Edital de abertura de prazo — conteúdo procedural/administrativo (guardrail edital)"),
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip("BLOQUEAR", "Aviso de audiência pública sem corpo de texto — cabeçalho procedural"),
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip("BLOQUEAR", "Aviso técnico sobre emissão de notas fiscais — procedural e sem corpo de matéria"),
}


def main():
    apr_path = ROOT / "state" / f"aprovadas_{HOJE}.json"
    pauta_path = ROOT / "state" / f"pauta_{HOJE}.json"
    materias_dir = ROOT / "state" / f"materias_{HOJE}"

    data = json.loads(apr_path.read_text(encoding="utf-8"))
    apr_list = data.get("aprovadas") or data.get("curadas") or (data if isinstance(data, list) else [])

    pauta = []
    pub_count = 0
    for item in apr_list:
        h = item["id_hash"]
        if h not in PAUTA_ANGULADA:
            angul = _skip("BLOQUEAR", "Item fora do top selecionado pela curadoria do dia (quota/relevância)")
            angul["titulo_sultv"] = item.get("titulo", "")[:100]
        else:
            angul = PAUTA_ANGULADA[h]

        if angul["decisao_final"] == "PUBLICAR" and pub_count >= 10:
            angul = {**angul, "decisao_final": "REBAIXAR", "decisao_motivo": "Quota diária de 10 publicações esgotada"}
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
    print("[angular] decisões:", Counter(p["decisao_final"] for p in pauta))
    print("[angular] PUBLICAR:", pub_count)

    materias_dir.mkdir(exist_ok=True)
    nwrite = 0
    for p in pauta:
        if p["decisao_final"] == "PUBLICAR" and p.get("formato_sugerido") == "materia_longa":
            corpo = MATERIAS.get(p["id_hash"])
            if corpo:
                (materias_dir / f"{p['id_hash']}.md").write_text(corpo, encoding="utf-8")
                nwrite += 1
                print(f"[angular] matéria -> {p['id_hash']}.md ({len(corpo)} chars)")
            else:
                print(f"[angular] AVISO: {p['id_hash']} é PUBLICAR/materia_longa sem texto em MATERIAS")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


# Matérias longas — redação SulTV (3ª pessoa institucional, sem menção a veículos — regra 12)
MATERIAS = {
    "0dc297418c5e4a9ebe4fd0c6b8ba21643551ff7b": """### Título ###
Cresol Camaquã lança projeto que une educação financeira e bem-estar no trabalho

### Artigo ###
A Cresol de Camaquã lançou um projeto que une educação financeira e bem-estar emocional dentro do ambiente de trabalho. A proposta leva conversas dinâmicas às empresas da região com o objetivo de humanizar o cuidado com o dinheiro e enfrentar os impactos emocionais que o endividamento provoca na vida dos trabalhadores. A iniciativa parte de uma constatação cada vez mais reconhecida: as dívidas não pesam apenas no orçamento, mas também na saúde, no sono e na produtividade de quem precisa lidar com contas em atraso. Ao trazer o tema para dentro das empresas, o projeto busca quebrar o tabu que ainda cerca as finanças pessoais e mostrar que falar de dinheiro de forma aberta é o primeiro passo para reorganizar a vida. Nas conversas, são abordados temas como o planejamento do orçamento doméstico, o controle de gastos, a diferença entre dívidas saudáveis e armadilhas do crédito, e formas de sair do vermelho com tranquilidade. A escolha do ambiente de trabalho como espaço para essa conversa tem lógica: é ali que muitas pessoas passam boa parte do dia e onde os efeitos do estresse financeiro se manifestam com clareza. Para o município de Camaquã, na Costa Doce, iniciativas como essa fortalecem uma cultura de consumo consciente e de organização das contas, que se reflete no comércio local, na inadimplência e na qualidade de vida das famílias. A educação financeira deixa de ser um assunto distante, restrito a especialistas, e passa a fazer parte do cotidiano dos trabalhadores da região, numa abordagem que valoriza tanto o equilíbrio das finanças quanto o cuidado com as pessoas.

### Legenda sugerida ###
Projeto em Camaquã leva conversas sobre dinheiro e bem-estar para dentro das empresas da região.

### Palavras-chave ###
Camaquã, educação financeira, bem-estar no trabalho, endividamento, Cresol, consumo consciente, Costa Doce, finanças pessoais
""",

    "d69906d280f27e21bcfe4af39db247662985bf35": """### Título ###
Produtores de Tapes têm até 30 de junho para a Declaração Anual de Rebanho

### Artigo ###
Os produtores rurais de Tapes têm até o dia 30 de junho para entregar a Declaração Anual de Rebanho 2026. A informação é da Secretaria Municipal de Agricultura e Desenvolvimento Rural, que reforça o caráter obrigatório do documento para todos os criadores que possuem animais de produção. A declaração pode ser feita pela internet, por meio do sistema Produtor Online, ou presencialmente na Inspetoria de Defesa Agropecuária de Tapes, localizada na Rua Hermínio José Soares, número 666. Mais do que uma formalidade, a Declaração Anual de Rebanho é uma ferramenta central da defesa sanitária animal. É por meio dela que o poder público mantém atualizado o mapa do rebanho do município e do estado, informação essencial para o planejamento de campanhas de vacinação, para o controle de doenças e para a rastreabilidade dos animais. Manter os dados em dia também é condição para que o produtor tenha acesso a uma série de serviços, como a emissão de guias de trânsito animal, indispensáveis para a comercialização e o transporte do rebanho. A recomendação das autoridades é não deixar a declaração para a última hora, evitando filas e eventuais transtornos no fechamento do prazo. Em uma região como a Costa Doce, onde a pecuária convive com as lavouras de arroz e soja e tem papel importante na economia rural, o cumprimento do prazo é um cuidado que protege tanto o produtor individual quanto a sanidade do rebanho de todo o município. Quem tiver dúvidas pode procurar diretamente a Inspetoria de Defesa Agropecuária ou a Secretaria Municipal de Agricultura de Tapes para orientação sobre o preenchimento.

### Legenda sugerida ###
Declaração Anual de Rebanho 2026 é obrigatória em Tapes e pode ser feita até 30 de junho, on-line ou presencialmente.

### Palavras-chave ###
Tapes, Declaração Anual de Rebanho, defesa agropecuária, pecuária, produtor rural, Produtor Online, Costa Doce, sanidade animal
""",

    "ed5de350ac85eb327fb2dd3a082da35d5be793ac": """### Título ###
Barra do Ribeiro habilita 33 propostas culturais em marco da Lei Aldir Blanc

### Artigo ###
Barra do Ribeiro alcançou um marco histórico na área cultural com 33 propostas habilitadas no Ciclo 2 da Política Nacional Aldir Blanc. O resultado, divulgado pela Prefeitura, soma 11 habilitados no Edital 001/2026 e 22 no Edital 002/2026, e é apontado pela administração municipal como o maior número já registrado no município. A Política Nacional Aldir Blanc é o principal mecanismo de fomento à cultura no país, com recursos federais repassados a estados e municípios para apoiar artistas, grupos, coletivos e espaços culturais. A habilitação é a etapa que confirma quais propostas atenderam aos requisitos dos editais e estão aptas a seguir no processo de execução, transformando projetos em ações concretas para a comunidade. O número expressivo de habilitados revela a vitalidade da produção cultural local, que abrange manifestações como música, dança, teatro, artesanato, literatura e tradições populares. Para uma cidade do porte de Barra do Ribeiro, na Costa Doce, esse volume de propostas representa não apenas o reconhecimento dos fazedores de cultura, mas também a circulação de recursos que movimentam a economia criativa e levam atividades a diferentes públicos. O fomento cultural costuma ter efeito multiplicador: cada projeto contemplado gera oficinas, apresentações, contratações e oportunidades de formação, fortalecendo o tecido cultural do município e estimulando novas gerações de artistas. A lista completa dos habilitados é divulgada nos canais oficiais da Prefeitura de Barra do Ribeiro, que orienta os participantes a acompanharem as próximas etapas dos editais. O resultado consolida a cultura como uma política pública de presença crescente na cidade e reforça a importância da participação dos agentes culturais nos processos de fomento.

### Legenda sugerida ###
Com 33 propostas habilitadas, Barra do Ribeiro bate recorde de inscrições culturais pela Lei Aldir Blanc.

### Palavras-chave ###
Barra do Ribeiro, Lei Aldir Blanc, cultura, fomento cultural, economia criativa, editais, Costa Doce, política cultural
""",

    "d837c631025a0927c2a737aeb12deaa42536357c": """### Título ###
Projeto leva robótica a professores e alunos de escolas municipais de Pelotas

### Artigo ###
Pelotas é um dos municípios contemplados pelo projeto Hands on Bot (HOB), do Sistema FIERGS, que leva a robótica para professores e alunos das escolas municipais. A iniciativa prevê uma formação inovadora para os docentes e a criação de clubes de robótica voltados a estudantes do 6º ao 9º ano do Ensino Fundamental, aproximando a rede pública de ensino das tecnologias que vêm transformando o mercado de trabalho e a vida cotidiana. A proposta tem dois eixos complementares. O primeiro é capacitar os professores, oferecendo uma metodologia que permite trabalhar conceitos de robótica e programação em sala de aula, mesmo para quem não tem formação técnica na área. O segundo é mobilizar os estudantes por meio de clubes de robótica, espaços em que os alunos colocam a mão na massa para montar dispositivos, resolver desafios e aprender de forma prática. Mais do que ensinar a construir robôs, projetos desse tipo desenvolvem competências cada vez mais valorizadas, como o raciocínio lógico, a criatividade, a capacidade de resolver problemas e o trabalho em equipe. A robótica educacional funciona como uma porta de entrada para as áreas de ciência, tecnologia, engenharia e matemática, despertando vocações que podem se transformar em escolhas profissionais no futuro. Para Pelotas, na Costa Doce ampliada, levar essa formação à rede municipal significa ampliar o acesso de crianças e adolescentes a um aprendizado que, muitas vezes, fica restrito a escolas particulares ou a grandes centros urbanos. A iniciativa reforça a ideia de que a inovação no ensino público é um investimento direto no desenvolvimento da região, preparando uma nova geração para os desafios de um mundo cada vez mais digital.

### Legenda sugerida ###
Projeto do Sistema FIERGS leva robótica e formação de professores às escolas municipais de Pelotas.

### Palavras-chave ###
Pelotas, robótica, educação, tecnologia, Hands on Bot, Sistema FIERGS, ensino fundamental, inovação, Costa Doce
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS acompanham com apreensão a renegociação de dívidas rurais

### Artigo ###
Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas no Congresso e temem as consequências caso a proposta não seja aprovada. O principal receio do setor é ficar sem acesso ao crédito rural para financiar a próxima safra, um risco que atinge em cheio regiões produtoras como a Costa Doce, onde o arroz e a soja sustentam a economia de dezenas de municípios. O endividamento do campo gaúcho se agravou nos últimos anos com uma sequência de eventos climáticos extremos. Primeiro, vieram as estiagens severas, que quebraram safras consecutivas e reduziram drasticamente a renda das propriedades. Na sequência, as enchentes históricas que atingiram o estado provocaram perdas em lavouras, máquinas, estradas e estruturas, aprofundando a crise no meio rural. Sem conseguir honrar os compromissos das safras frustradas, muitos produtores acumularam parcelas e perderam a capacidade de tomar novos financiamentos, entrando em um ciclo que compromete o custeio do plantio seguinte. A renegociação em discussão é vista pelas entidades do setor como condição para restabelecer a capacidade de pagamento e manter o produtor na atividade. Enquanto a votação não acontece, cresce a apreensão no campo, porque o calendário agrícola não espera: as decisões sobre compra de insumos e financiamento da safra de verão precisam ser tomadas nos próximos meses. As lideranças do agronegócio gaúcho têm intensificado a interlocução com os parlamentares do estado para dar celeridade à tramitação. Para a economia regional, o desfecho do tema é estratégico, já que a continuidade das lavouras movimenta empregos, comércio e serviços em toda a Costa Doce. Os desdobramentos serão decisivos para o planejamento da safra 2026/2027 no Rio Grande do Sul.

### Legenda sugerida ###
Campo gaúcho teme ficar sem crédito para a próxima safra caso a renegociação de dívidas não avance.

### Palavras-chave ###
renegociação de dívidas, crédito rural, Rio Grande do Sul, agro, safra, arroz, soja, endividamento rural, Costa Doce
""",
}


if __name__ == "__main__":
    main()
