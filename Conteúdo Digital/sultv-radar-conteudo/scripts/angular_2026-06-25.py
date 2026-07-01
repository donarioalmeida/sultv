#!/usr/bin/env python3
"""
angular_2026-06-25.py — angulação editorial + redação (cowork-faz-tudo).
Decisões editoriais Claude na sessão para a pauta de 2026-06-25.
Regra 12 INEGOCIÁVEL: nenhum texto menciona veículos/portais/rádios/jornais.
Atribuição apenas a fontes primárias institucionais.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-25"


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

    # IDX 0 — Junho Vermelho / doação de sangue (Camaquã) — PUBLICAR
    "ae480230bb1ab97528290995310f77d546ac5818": {
        "titulo_sultv": "Junho Vermelho: inverno derruba estoques de sangue e doação se torna urgente na Costa Doce",
        "chamada_faixa": "Inverno reduz estoque de sangue; doe agora",
        "subtitulo": "Com a queda de temperatura, os hemocentros registram menos doadores; campanha reforça a importância de doar sangue regularmente.",
        "lead": "Os dias frios trazem um alerta que se repete todo ano. Com a chegada do inverno, período em que os estoques dos hemocentros costumam registrar queda, a campanha Junho Vermelho chama a atenção dos moradores de Camaquã e de toda a Costa Doce para a importância da doação regular de sangue, gesto simples que pode salvar vidas.",
        "ganchos_3": [
            "Inverno reduz a procura e derruba os estoques dos hemocentros",
            "Campanha Junho Vermelho reforça a doação regular de sangue",
            "Uma única doação pode ajudar a salvar até quatro vidas"
        ],
        "angulo_editorial": "Serviço de utilidade pública de alto alcance e apelo comunitário. Campanha de saúde pública (não é diagnóstico médico). Ângulo regional: estoques que atendem a Costa Doce. Sem viés partidário, sem dramalhão.",
        "fontes_complementares_sugeridas": ["Hemocentro do Estado do RS (Hemorgs)", "Secretarias Municipais de Saúde da Costa Doce"],
        "lead_materia_longa": "Os dias frios trazem um alerta que se repete todo ano. Com a chegada do inverno, período em que os estoques dos hemocentros costumam registrar queda, a campanha Junho Vermelho chama a atenção para a importância da doação regular de sangue.",
        "post_instagram": {
            "caption": "Chegou o frio, e com ele um alerta importante: no inverno os estoques de sangue costumam cair. É justamente quando as pessoas saem menos de casa que os hemocentros mais precisam de doadores. Por isso existe o Junho Vermelho, campanha que lembra a importância de doar sangue de forma regular. Doar é rápido, seguro e não faz falta para quem doa, mas pode significar tudo para quem espera por uma cirurgia, um tratamento ou uma emergência. Em Camaquã e em toda a Costa Doce, o recado é o mesmo: se você está saudável, reserve um tempo para doar. Uma única bolsa pode ajudar a salvar várias vidas. Espalhe essa ideia e chame um amigo para doar junto.",
            "hashtags": ["#JunhoVermelho", "#DoeSangue", "#Camaquã", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "No frio, falta sangue nos hospitais.",
            "desenvolvimento_45s": "Com a chegada do inverno, os estoques dos hemocentros costumam cair, porque as pessoas saem menos de casa e doam menos. É nesse período que a campanha Junho Vermelho reforça a importância da doação regular de sangue. Doar é rápido, seguro e não prejudica quem doa, mas pode salvar a vida de quem espera por uma cirurgia, um tratamento ou uma emergência. Em Camaquã e na Costa Doce, quem está saudável pode procurar um ponto de coleta e fazer a diferença.",
            "fechamento_8s": "Uma doação, várias vidas salvas.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "emotivo positivo"
        },
        "tag_thumbnail": "Junho Vermelho, doação de sangue",
        "briefing_visual": {
            "descricao_pt": "Bolsa de sangue para doação em hemocentro, ambiente hospitalar limpo, foco no equipamento, sem rostos identificáveis",
            "query_en": ["blood donation bag", "blood donation center", "red cross blood donor"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Close-up of a blood donation bag and tubing in a clean medical donation center, warm light, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de utilidade pública e saúde comunitária em cidade-núcleo (Camaquã), alto apelo e fato sazonal concreto. Sem guardrail."
    },

    # IDX 1 — Menino ajuda no 'bafo' (Camaquã) — REBAIXAR
    "e77017cb9d9253429616ce63237ae2f37fd7f63b": _skip(
        "REBAIXAR", "Conteúdo soft/anedótico sem fato concreto verificável nem fonte institucional. Boa peça leve, mas a quota do dia prioriza serviço e fatos civis."),

    # IDX 2 — Defesa Civil de Tapes no CIPDC 2026 — PUBLICAR
    "69e55e539fb3c957f367c14db975687ca36e8e76": {
        "titulo_sultv": "Defesa Civil de Tapes participa de congresso internacional e debate preparação para o El Niño",
        "chamada_faixa": "Tapes debate prevenção e El Niño em congresso",
        "subtitulo": "Representantes do município acompanham o CIPDC 2026, em Porto Alegre, com foco na preparação para eventos climáticos extremos.",
        "lead": "A prevenção a desastres entrou na pauta de Tapes. A Defesa Civil do município participa do Congresso Internacional de Proteção e Defesa Civil, o CIPDC 2026, realizado de 23 a 25 de junho em Porto Alegre, onde gestores discutem a preparação para o fenômeno El Niño 2026/2027 e a resposta a eventos climáticos extremos que afetam a Costa Doce.",
        "ganchos_3": [
            "Defesa Civil de Tapes acompanha congresso internacional do setor",
            "Preparação para o El Niño 2026/2027 está entre os temas centrais",
            "Troca de experiências fortalece a prevenção a desastres na região"
        ],
        "angulo_editorial": "Fato institucional concreto em cidade-núcleo (Tapes), com fonte primária (Defesa Civil Municipal). Tema relevante para a Costa Doce, marcada por cheias recentes. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Coordenadoria Municipal de Defesa Civil de Tapes", "Defesa Civil do Estado do RS"],
        "lead_materia_longa": "A prevenção a desastres entrou na pauta de Tapes. A Defesa Civil do município participa do Congresso Internacional de Proteção e Defesa Civil, o CIPDC 2026, realizado de 23 a 25 de junho em Porto Alegre.",
        "post_instagram": {
            "caption": "Prevenir é sempre melhor do que remediar, e Tapes está de olho nisso. A Defesa Civil do município participou do Congresso Internacional de Proteção e Defesa Civil, o CIPDC 2026, em Porto Alegre, ao lado de gestores e especialistas de várias regiões. Entre os temas em destaque está a preparação para o fenômeno El Niño 2026/2027, que pode trazer chuvas e eventos climáticos extremos. Para uma cidade da Costa Doce, que conhece de perto os efeitos das cheias, investir em conhecimento e em planejamento é proteger vidas e patrimônio. Quando a Defesa Civil se prepara, toda a comunidade fica mais segura.",
            "hashtags": ["#Tapes", "#DefesaCivil", "#ElNiño", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tapes se prepara para o clima extremo.",
            "desenvolvimento_45s": "A Defesa Civil de Tapes participou do Congresso Internacional de Proteção e Defesa Civil, o CIPDC 2026, em Porto Alegre, ao lado de gestores e especialistas de várias regiões. Um dos temas centrais foi a preparação para o fenômeno El Niño 2026/2027, que pode trazer chuvas intensas e eventos climáticos extremos. Para uma cidade da Costa Doce, que já sentiu os efeitos das cheias, planejamento e prevenção significam proteger vidas e patrimônio.",
            "fechamento_8s": "Prevenção é proteção para todos.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo sóbrio"
        },
        "tag_thumbnail": "Defesa Civil, prevenção El Niño",
        "briefing_visual": {
            "descricao_pt": "Auditório de congresso com plateia assistindo a palestra sobre proteção e defesa civil, ambiente institucional, sem rostos identificáveis em primeiro plano",
            "query_en": ["conference auditorium audience", "emergency management seminar", "civil defense meeting"],
            "evitar": ["pessoas com rosto visível em close", "marcas", "texto", "logos"],
            "prompt_ia": "Wide shot of a professional conference auditorium with an audience attending a presentation, neutral institutional setting, no identifiable faces in foreground, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato institucional concreto em cidade-núcleo (Tapes), fonte primária Defesa Civil, tema climático de alta relevância para a Costa Doce."
    },

    # IDX 3 — Declaração Anual de Rebanho prazo 30/06 (Tapes) — PUBLICAR
    "1731235a445ae103fcc24a28232938f2407b1f1a": {
        "titulo_sultv": "Declaração Anual de Rebanho: produtores de Tapes têm até 30 de junho para regularizar",
        "chamada_faixa": "Rebanho: prazo da declaração encerra em 30/06",
        "subtitulo": "Atualização é obrigatória para quem tem animais de produção e pode ser feita online ou na Inspetoria de Defesa Agropecuária.",
        "lead": "O relógio corre para o produtor rural da Costa Doce. Os produtores de Tapes têm até o dia 30 de junho para realizar a Declaração Anual de Rebanho 2026, atualização obrigatória para todos que possuem animais de produção e que é fundamental para o controle sanitário e o planejamento do setor agropecuário no município.",
        "ganchos_3": [
            "Prazo para a Declaração Anual de Rebanho encerra em 30 de junho",
            "Atualização é obrigatória para quem possui animais de produção",
            "Declaração pode ser feita online ou de forma presencial"
        ],
        "angulo_editorial": "Serviço agropecuário de utilidade pública com prazo (alta urgência), em cidade-núcleo (Tapes). Fonte primária: Secretaria Municipal de Agricultura e Inspetoria de Defesa Agropecuária. Atinge diretamente a base rural da audiência.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Agricultura e Desenvolvimento Rural de Tapes", "Inspetoria de Defesa Agropecuária de Tapes"],
        "lead_materia_longa": "O relógio corre para o produtor rural da Costa Doce. Os produtores de Tapes têm até o dia 30 de junho para realizar a Declaração Anual de Rebanho 2026, atualização obrigatória para todos que possuem animais de produção.",
        "post_instagram": {
            "caption": "Atenção, produtor: o prazo está acabando. Quem possui animais de produção em Tapes tem até o dia 30 de junho para fazer a Declaração Anual de Rebanho 2026. A atualização é obrigatória e fundamental para o controle sanitário, o planejamento e o desenvolvimento do setor agropecuário. A boa notícia é que dá para resolver de forma simples: a declaração pode ser feita online, pelo sistema do Produtor Online, ou presencialmente na Inspetoria de Defesa Agropecuária do município. Deixar para a última hora é arriscar perder o prazo e enfrentar problemas com a regularização. Organize os dados do seu rebanho e garanta a sua declaração em dia.",
            "hashtags": ["#Tapes", "#Agro", "#DeclaraçãoDeRebanho", "#DefesaAgropecuária", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Produtor, atenção ao prazo!",
            "desenvolvimento_45s": "Quem tem animais de produção em Tapes precisa fazer a Declaração Anual de Rebanho 2026 até o dia 30 de junho. A atualização é obrigatória e essencial para o controle sanitário e o planejamento do setor agropecuário. A declaração pode ser feita online, pelo sistema do Produtor Online, ou presencialmente na Inspetoria de Defesa Agropecuária do município. Deixar para a última hora é arriscar perder o prazo, então o ideal é organizar os dados do rebanho e regularizar logo.",
            "fechamento_8s": "Rebanho declarado, produtor tranquilo.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo agro"
        },
        "tag_thumbnail": "Declaração de Rebanho, prazo",
        "briefing_visual": {
            "descricao_pt": "Gado bovino em pasto verde no interior do Rio Grande do Sul, manhã de inverno, sem pessoas",
            "query_en": ["cattle herd pasture brazil", "cows green field farm", "livestock farm southern brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Beef cattle grazing in a green pasture in rural southern Brazil on a cool winter morning, soft light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço agropecuário com prazo (utilidade pública alta) em cidade-núcleo (Tapes). Fonte primária institucional. Segundo item de Tapes dentro da quota 2/cidade."
    },

    # IDX 4 — Arambaré formação étnico-racial — REBAIXAR
    "58c775b6ca179de847743f1399adcfa54436e516": _skip(
        "REBAIXAR", "Segundo item de Arambaré; priorizada a Festa Junina (mais timely e de maior apelo comunitário). Conteúdo institucional válido, mas vira nota interna."),

    # IDX 5 — Festa Junina de Arambaré — PUBLICAR
    "5ec657641f88db018d679fc6eb7bd0bf38269a1e": {
        "titulo_sultv": "Festa Junina de Arambaré reúne a comunidade nesta sexta com música, quadrilha e show",
        "chamada_faixa": "Arambaré celebra o São João nesta sexta-feira",
        "subtitulo": "Programação no Loteamento Popular começa às 16h, com apresentações de estudantes, do CRAS e show de encerramento.",
        "lead": "A tradição junina toma conta de Arambaré nesta sexta-feira. A Festa Junina do município acontece no dia 27 de junho, a partir das 16h, no Loteamento Popular, com uma programação que reúne coral, apresentações de estudantes, quadrilha e show de banda para celebrar o São João com toda a comunidade da Costa Doce.",
        "ganchos_3": [
            "Festa Junina de Arambaré acontece nesta sexta, dia 27",
            "Programação começa às 16h no Loteamento Popular",
            "Coral, quadrilha e show animam a celebração da comunidade"
        ],
        "angulo_editorial": "Evento comunitário concreto, com data, hora e local, em cidade-núcleo (Arambaré) e em período sazonal (São João). Alto apelo de público e valorização da cultura local. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Prefeitura de Arambaré", "Secretaria Municipal de Educação de Arambaré"],
        "lead_materia_longa": "A tradição junina toma conta de Arambaré nesta sexta-feira. A Festa Junina do município acontece no dia 27 de junho, a partir das 16h, no Loteamento Popular.",
        "post_instagram": {
            "caption": "Chegou a hora de vestir o xadrez e celebrar! A Festa Junina de Arambaré acontece nesta sexta-feira, dia 27 de junho, a partir das 16h, no Loteamento Popular. A programação foi preparada para reunir toda a família numa tarde de alegria, cultura e tradição: abertura com o Coral Municipal, apresentações dos estudantes da rede, quadrilha e o casamento na roça com o pessoal do CRAS, e à noite o show da banda para encerrar a festa em grande estilo. É a oportunidade perfeita para prestigiar os estudantes, valorizar as tradições juninas e curtir um momento especial com a comunidade. Leve a família, chame os amigos e venha celebrar o São João em Arambaré.",
            "hashtags": ["#Arambaré", "#FestaJunina", "#SãoJoão", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Vem aí a Festa Junina de Arambaré!",
            "desenvolvimento_45s": "A Festa Junina de Arambaré acontece nesta sexta-feira, dia 27 de junho, a partir das 16h, no Loteamento Popular. A programação reúne toda a família, com abertura do Coral Municipal, apresentações dos estudantes da rede, quadrilha e casamento na roça com o pessoal do CRAS, e à noite o show de banda para encerrar a festa. É a chance de prestigiar os estudantes, celebrar as tradições juninas e curtir um momento especial com a comunidade.",
            "fechamento_8s": "Traga a família e venha celebrar.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "festiva junina"
        },
        "tag_thumbnail": "Festa Junina, Arambaré",
        "briefing_visual": {
            "descricao_pt": "Festa junina brasileira com bandeirinhas coloridas, fogueira e decoração típica de São João, ambiente noturno festivo, sem rostos identificáveis",
            "query_en": ["festa junina decoration", "brazilian june festival lights", "colorful bunting flags night"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Brazilian festa junina scene with colorful triangular bunting flags, warm lights and rustic decorations at dusk, festive atmosphere, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento comunitário concreto (data/hora/local) em cidade-núcleo (Arambaré), sazonal e de alto apelo. Fonte primária Prefeitura."
    },

    # IDX 6 — UBS Porte II Chuvisca — PUBLICAR
    "31fb7c80312523d384bb96a83eefaaca270eaf81": {
        "titulo_sultv": "Chuvisca avança na construção de nova UBS com investimento de R$ 2,45 milhões",
        "chamada_faixa": "Chuvisca ergue nova UBS de R$ 2,45 milhões",
        "subtitulo": "Obra da Unidade Básica de Saúde Porte II amplia e qualifica o atendimento à população do município.",
        "lead": "A saúde de Chuvisca ganha um reforço de peso. A construção da nova Unidade Básica de Saúde Porte II segue avançando no município, viabilizada por um investimento de R$ 2.452.054,00 e voltada à ampliação e à qualificação dos serviços de saúde oferecidos à população da Costa Doce.",
        "ganchos_3": [
            "Nova UBS Porte II avança em Chuvisca",
            "Investimento chega a R$ 2,45 milhões",
            "Obra amplia e qualifica o atendimento à população"
        ],
        "angulo_editorial": "Investimento público concreto e quantificado em cidade-núcleo (Chuvisca). Saúde como infraestrutura (não é orientação médica). Fonte primária: Prefeitura. Fato positivo de desenvolvimento regional.",
        "fontes_complementares_sugeridas": ["Prefeitura de Chuvisca", "Secretaria Municipal de Saúde de Chuvisca"],
        "lead_materia_longa": "A saúde de Chuvisca ganha um reforço de peso. A construção da nova Unidade Básica de Saúde Porte II segue avançando no município, viabilizada por um investimento de R$ 2.452.054,00.",
        "post_instagram": {
            "caption": "Boa notícia para a saúde de Chuvisca: a construção da nova Unidade Básica de Saúde Porte II segue avançando no município. A obra é fruto de um longo processo, que envolveu planejamento, estudos técnicos, aquisição do terreno, licenciamento e todas as autorizações necessárias até chegar ao canteiro. Com um investimento de mais de R$ 2,4 milhões, a nova unidade vai ampliar e qualificar o atendimento oferecido à população, aproximando os serviços de saúde de quem mais precisa. Investir em estrutura é investir no cuidado com as pessoas, e cada etapa concluída representa um passo importante para uma saúde pública melhor no interior.",
            "hashtags": ["#Chuvisca", "#Saúde", "#UBS", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Chuvisca investe na saúde.",
            "desenvolvimento_45s": "A construção da nova Unidade Básica de Saúde Porte II segue avançando em Chuvisca. A obra é resultado de um longo processo, que passou por planejamento, estudos técnicos, aquisição do terreno e licenciamento, até chegar ao canteiro. Com um investimento de mais de R$ 2,4 milhões, a nova unidade vai ampliar e qualificar o atendimento oferecido à população, aproximando os serviços de saúde de quem mais precisa no interior.",
            "fechamento_8s": "Mais estrutura, mais cuidado.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo positivo"
        },
        "tag_thumbnail": "UBS, investimento em saúde",
        "briefing_visual": {
            "descricao_pt": "Canteiro de obras de um prédio público de saúde em construção no interior, estrutura em alvenaria, capacete e andaimes, sem rostos identificáveis",
            "query_en": ["health clinic construction site", "public building under construction", "new clinic building brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A small public health clinic under construction in a rural Brazilian town, brick walls and scaffolding, daytime, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Investimento público concreto e quantificado em cidade-núcleo (Chuvisca), infraestrutura de saúde. Fonte primária Prefeitura."
    },

    # IDX 7 — ABF futebol SLS — REBAIXAR
    "8e1bf94a02dbd7418574a2daafce640e6d703f8b": _skip(
        "REBAIXAR", "Anúncio de jogo de futebol amador; baixo valor civil e SLS já tem cota. Vira nota leve."),

    # IDX 8 — Previsão meteorológica SLS — REBAIXAR
    "1288dbc8afa87503de267ac34e2c9ec1fe71ae47": _skip(
        "REBAIXAR", "Boletim meteorológico rotineiro; o frio estadual já é coberto pela matéria das ~70 cidades. Segundo item de SLS."),

    # IDX 9 — Edital de penalidade (Chuvisca) — BLOQUEAR
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR", "Edital procedural/administrativo sem texto e sem valor jornalístico (guardrail de edital)."),

    # IDX 10 — Núcleo de Atendimento TEA (Barra do Ribeiro) — PUBLICAR
    "15920be0f1a1a4cd24939465621c58afc813ef2d": {
        "titulo_sultv": "Barra do Ribeiro inaugura Núcleo de Atendimento Especializado para crianças com TEA",
        "chamada_faixa": "Barra do Ribeiro abre núcleo de atendimento ao TEA",
        "subtitulo": "Espaço oferece fonoaudiologia, terapia ocupacional e atendimento educacional especializado a alunos da rede municipal.",
        "lead": "A inclusão ganhou um endereço em Barra do Ribeiro. Na última terça-feira, 23 de junho, o município inaugurou o Núcleo de Atendimento Especializado voltado a crianças com Transtorno do Espectro Autista, um espaço que reúne serviços de fonoaudiologia, terapia ocupacional e atendimento educacional especializado para alunos da rede municipal de ensino.",
        "ganchos_3": [
            "Barra do Ribeiro inaugura Núcleo de Atendimento Especializado para o TEA",
            "Espaço oferece fonoaudiologia, terapia ocupacional e AEE",
            "Atendimento começa pelos alunos da rede municipal de ensino"
        ],
        "angulo_editorial": "Fato concreto e datado (inauguração 23/06), de forte apelo social (inclusão e infância) em cidade da Costa Doce ampliada (Barra do Ribeiro). Fonte primária: Prefeitura e secretarias. Não é conteúdo médico individualizado, e sim política pública de serviço.",
        "fontes_complementares_sugeridas": ["Prefeitura de Barra do Ribeiro", "Secretaria Municipal de Educação e Cultura", "Secretaria Municipal de Saúde"],
        "lead_materia_longa": "A inclusão ganhou um endereço em Barra do Ribeiro. Na última terça-feira, 23 de junho, o município inaugurou o Núcleo de Atendimento Especializado voltado a crianças com Transtorno do Espectro Autista.",
        "post_instagram": {
            "caption": "Um avanço importante para a inclusão e para o cuidado com as crianças de Barra do Ribeiro. O município inaugurou o Núcleo de Atendimento Especializado voltado a crianças com Transtorno do Espectro Autista, o TEA. O espaço foi pensado para oferecer atendimento qualificado, com serviços de fonoaudiologia, terapia ocupacional e atendimento educacional especializado. Neste primeiro momento, o trabalho começa pelos alunos da rede municipal de ensino, garantindo apoio no desenvolvimento e na aprendizagem. Iniciativas como essa mostram que acolher é também estruturar serviços, e que cada criança merece um lugar preparado para receber o cuidado de que precisa.",
            "hashtags": ["#BarraDoRibeiro", "#Inclusão", "#TEA", "#Educação", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Barra do Ribeiro avança na inclusão.",
            "desenvolvimento_45s": "O município inaugurou o Núcleo de Atendimento Especializado voltado a crianças com Transtorno do Espectro Autista, o TEA. O espaço oferece serviços de fonoaudiologia, terapia ocupacional e atendimento educacional especializado. Neste primeiro momento, o trabalho começa pelos alunos da rede municipal de ensino, garantindo apoio no desenvolvimento e na aprendizagem. Estruturar um serviço como esse é dar às crianças e às famílias um lugar preparado para acolher e cuidar.",
            "fechamento_8s": "Acolher também é estruturar.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "emotivo positivo"
        },
        "tag_thumbnail": "inclusão, atendimento TEA",
        "briefing_visual": {
            "descricao_pt": "Sala de atendimento infantil colorida e acolhedora com brinquedos pedagógicos e materiais terapêuticos, sem crianças com rosto visível",
            "query_en": ["pediatric therapy room", "child occupational therapy toys", "colorful learning room kids"],
            "evitar": ["crianças com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A warm, colorful pediatric therapy and learning room with educational toys and soft materials, empty of people, bright daylight, no identifiable children, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Inauguração concreta e datada de serviço público de inclusão, forte apelo social, Costa Doce ampliada (Barra do Ribeiro). Fonte primária institucional."
    },

    # IDX 11 — Conselho do Idoso BdR (07/05 antigo) — REBAIXAR
    "d000afa68502f9fbd9ab7ac727b76dccee2d1cd7": _skip(
        "REBAIXAR", "Reunião de 07/05 (conteúdo defasado) e segundo item de Barra do Ribeiro. Priorizado o Núcleo TEA."),

    # IDX 12 — Aviso de audiência pública (Sentinela do Sul) — BLOQUEAR
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR", "Aviso/edital procedural sem corpo de texto (guardrail de edital)."),

    # IDX 13 — Emissão de notas fiscais (Sentinela do Sul) — BLOQUEAR
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR", "Comunicado administrativo/procedural sem corpo de texto (guardrail de edital)."),

    # IDX 14 — Melhorias em estradas (Cristal) — PUBLICAR
    "01ef011ecdae21c60e1584906736e0e1b68bd082": {
        "titulo_sultv": "Cristal melhora estradas do interior com cascalhamento e patrolamento e apoia o produtor rural",
        "chamada_faixa": "Cristal recupera estradas e apoia o interior",
        "subtitulo": "Serviços incluem cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades do município.",
        "lead": "As estradas que ligam o campo à cidade estão recebendo atenção em Cristal. A Prefeitura executa melhorias nas vias do interior do município, com serviços de cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades, garantindo o escoamento da produção e o acesso das famílias na Costa Doce.",
        "ganchos_3": [
            "Cristal recupera estradas do interior em várias localidades",
            "Serviços incluem cascalhamento, patrolamento e apoio às propriedades",
            "Melhorias facilitam o escoamento da produção e o acesso rural"
        ],
        "angulo_editorial": "Infraestrutura rural concreta em cidade-núcleo (Cristal), de impacto direto sobre o produtor e o escoamento da safra. Fonte primária: Prefeitura. Tema central para a audiência rural.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria Municipal de Obras de Cristal"],
        "lead_materia_longa": "As estradas que ligam o campo à cidade estão recebendo atenção em Cristal. A Prefeitura executa melhorias nas vias do interior do município, com serviços de cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades.",
        "post_instagram": {
            "caption": "Estrada boa é o que mantém o interior conectado, e Cristal está trabalhando nisso. A Prefeitura realiza melhorias nas estradas do interior do município, com serviços de cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades. Para quem vive e produz no campo, a diferença é enorme: estradas em boas condições facilitam o escoamento da safra, melhoram o acesso ao transporte escolar e à saúde, e reduzem o desgaste de máquinas e veículos. No tempo chuvoso, então, uma via bem cuidada é a garantia de que ninguém fica isolado. Cuidar das estradas rurais é cuidar de quem produz e movimenta a economia da região.",
            "hashtags": ["#Cristal", "#EstradasRurais", "#Agro", "#Infraestrutura", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal cuida das estradas do interior.",
            "desenvolvimento_45s": "A Prefeitura de Cristal realiza melhorias nas estradas do interior do município, com cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades. Para quem vive e produz no campo, a diferença é grande: estradas em boas condições facilitam o escoamento da safra, melhoram o acesso ao transporte e à saúde e reduzem o desgaste de máquinas e veículos. No tempo chuvoso, uma via bem cuidada é a garantia de que ninguém fica isolado no interior.",
            "fechamento_8s": "Estrada boa, interior conectado.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo agro"
        },
        "tag_thumbnail": "estradas rurais, Cristal",
        "briefing_visual": {
            "descricao_pt": "Estrada de chão cascalhada no interior do Rio Grande do Sul com patrol/máquina ao fundo, paisagem rural, sem rostos identificáveis",
            "query_en": ["gravel rural road grader", "dirt road countryside brazil", "road maintenance machine farm"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A freshly graded gravel road winding through rural farmland in southern Brazil with a road grader machine in the distance, daytime, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Infraestrutura rural concreta em cidade-núcleo (Cristal), impacto direto no produtor e no escoamento. Fonte primária Prefeitura."
    },

    # IDX 15 — PREPARA RS (Cristal) — REBAIXAR
    "9ce36499a218324114c169a9d64f04aae0558ec9": _skip(
        "REBAIXAR", "Segundo item de Cristal; participação em lançamento de programa estadual, menos concreto localmente que as estradas. Vira nota."),

    # IDX 16 — Defesa Civil Guaíba congresso — REBAIXAR
    "364b872691e450e6b35f25c845d8a6d9a0894029": _skip(
        "REBAIXAR", "Mesma pauta do CIPDC já contemplada por Tapes (núcleo). Guaíba é segunda camada; evita duplicidade temática."),

    # IDX 18 — Pescadores assinam primeiros contratos do Incra (Pelotas) — PUBLICAR
    "b969263c34ba39f0fe24cd73c37f46b35ac7db50": {
        "titulo_sultv": "Inédito: pescadores de Pelotas e Rio Grande assinam os primeiros contratos de crédito do Incra no país",
        "chamada_faixa": "Pesca gaúcha assina crédito inédito do Incra",
        "subtitulo": "Cinco comunidades pesqueiras artesanais foram as primeiras do Brasil a assinar o Crédito Instalação, em ato na Colônia Z3.",
        "lead": "O Sul do Rio Grande do Sul entrou para a história da pesca artesanal brasileira. Famílias de cinco comunidades pesqueiras de Pelotas e Rio Grande foram as primeiras de todo o país a assinar contratos do Crédito Instalação do Incra, em ato realizado na Colônia Z3, marco que reforça o apoio à pesca artesanal na Costa Doce.",
        "ganchos_3": [
            "Pescadores gaúchos são os primeiros do país a assinar o Crédito Instalação",
            "Cinco comunidades artesanais de Pelotas e Rio Grande foram contempladas",
            "Assinatura ocorreu em ato na Colônia Z3"
        ],
        "angulo_editorial": "Fato concreto, datado e inédito no Brasil, com forte âncora regional (Pelotas/Rio Grande) e apelo ao setor primário artesanal. Fonte primária: Incra e comunidades pesqueiras. Pauta de desenvolvimento e renda no campo/água da Costa Doce.",
        "fontes_complementares_sugeridas": ["Incra — Instituto Nacional de Colonização e Reforma Agrária", "Colônia de Pescadores Z3", "Comunidades pesqueiras artesanais de Pelotas e Rio Grande"],
        "lead_materia_longa": "O Sul do Rio Grande do Sul entrou para a história da pesca artesanal brasileira. Famílias de cinco comunidades pesqueiras de Pelotas e Rio Grande foram as primeiras de todo o país a assinar contratos do Crédito Instalação do Incra.",
        "post_instagram": {
            "caption": "Um marco histórico saiu do Sul do Rio Grande do Sul. Famílias de cinco comunidades pesqueiras artesanais de Pelotas e Rio Grande foram as primeiras de todo o Brasil a assinar contratos do Crédito Instalação do Incra. A assinatura aconteceu em ato na Colônia Z3 e representa muito mais do que papéis: é o reconhecimento da pesca artesanal como atividade que merece apoio, estrutura e futuro. O crédito ajuda as famílias a se estabelecerem, melhorar as condições de trabalho e fortalecer uma tradição que move a economia e a cultura da Costa Doce. Quando a pesca artesanal é valorizada, ganham as famílias, ganha a região e ganha o Rio Grande.",
            "hashtags": ["#Pelotas", "#RioGrande", "#PescaArtesanal", "#Incra", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Marco histórico na pesca gaúcha.",
            "desenvolvimento_45s": "Famílias de cinco comunidades pesqueiras artesanais de Pelotas e Rio Grande foram as primeiras de todo o Brasil a assinar contratos do Crédito Instalação do Incra. A assinatura aconteceu em ato na Colônia Z3 e representa o reconhecimento da pesca artesanal como atividade que merece apoio e estrutura. O crédito ajuda as famílias a se estabelecerem, melhorar as condições de trabalho e fortalecer uma tradição que move a economia e a cultura da Costa Doce.",
            "fechamento_8s": "Pesca valorizada, região mais forte.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo inspirador"
        },
        "tag_thumbnail": "pesca artesanal, crédito Incra",
        "briefing_visual": {
            "descricao_pt": "Barcos de pesca artesanal coloridos parados na margem da Lagoa dos Patos ao amanhecer, redes de pesca, sem rostos identificáveis",
            "query_en": ["artisanal fishing boats lagoon", "small fishing boats brazil", "fishing nets harbor sunrise"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Colorful small artisanal fishing boats moored along a calm lagoon shore at sunrise in southern Brazil, fishing nets visible, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato inédito no país com forte âncora regional (Pelotas/Rio Grande) e apelo ao setor primário artesanal. Fonte primária Incra/Colônia Z3."
    },

    # IDX 19 — Impostômetro R$ 2 trilhões — REBAIXAR
    "f45888fc6c8ce27a161247bdf2ba6a37b669b6ca": _skip(
        "REBAIXAR", "Marco nacional de arrecadação sem âncora concreta no Sul-RS (regra do -3). Vira nota econômica interna."),

    # IDX 20 — Parlamentares concessões/PPPs (PoA) — REBAIXAR
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "REBAIXAR", "Pauta político-legislativa estadual sensível (privatizações/PPPs); risco de viés partidário (guardrail). Não publicar como matéria."),

    # IDX 24 — Produtores RS temem renegociação de dívidas — PUBLICAR
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "titulo_sultv": "Produtores do RS acompanham com apreensão a renegociação das dívidas rurais antes da safra",
        "chamada_faixa": "Campo gaúcho teme falta de crédito para a safra",
        "subtitulo": "Setor receia ficar sem acesso ao crédito rural para a próxima safra enquanto a renegociação tramita.",
        "lead": "A próxima safra começa a ser planejada sob tensão no campo gaúcho. Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação das dívidas rurais, temerosos de ficar sem acesso ao crédito necessário para o plantio, um impasse que mexe diretamente com a economia do interior e da Costa Doce.",
        "ganchos_3": [
            "Produtores do RS temem ficar sem crédito para a próxima safra",
            "Renegociação das dívidas rurais ainda tramita",
            "Impasse afeta a economia do interior gaúcho"
        ],
        "angulo_editorial": "Pauta agro estadual de alta relevância para a base rural da audiência. Fato setorial concreto (impasse no crédito). Sem viés partidário: foca a preocupação do produtor e o impacto econômico, não a disputa política.",
        "fontes_complementares_sugeridas": ["Federação da Agricultura do RS (Farsul)", "Sindicatos rurais", "Cooperativas agrícolas gaúchas"],
        "lead_materia_longa": "A próxima safra começa a ser planejada sob tensão no campo gaúcho. Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação das dívidas rurais.",
        "post_instagram": {
            "caption": "No campo gaúcho, a próxima safra já começa a ser planejada com preocupação. Produtores rurais do Rio Grande do Sul acompanham de perto a renegociação das dívidas rurais, temendo ficar sem acesso ao crédito necessário para plantar. Depois de anos marcados por adversidades climáticas, que reduziram a produção e apertaram a renda, muitos dependem dessa renegociação para reorganizar as contas e seguir produzindo. O crédito rural é o combustível da lavoura: é com ele que se compra semente, insumo e combustível. Sem ele, o ciclo da produção fica ameaçado, com reflexos no comércio, nos fornecedores e no emprego das cidades do interior. O campo espera respostas que tragam previsibilidade.",
            "hashtags": ["#Agro", "#RioGrandeDoSul", "#CréditoRural", "#Safra", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O campo gaúcho está apreensivo.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul acompanham com preocupação a renegociação das dívidas rurais, temendo ficar sem acesso ao crédito para a próxima safra. Depois de anos de adversidades climáticas, que reduziram a produção e apertaram a renda, muitos dependem dessa renegociação para reorganizar as contas. O crédito rural é o combustível da lavoura: sem ele, o ciclo da produção fica ameaçado, com reflexos no comércio, nos fornecedores e no emprego das cidades do interior.",
            "fechamento_8s": "O campo espera previsibilidade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo sóbrio"
        },
        "tag_thumbnail": "crédito rural, dívidas no campo",
        "briefing_visual": {
            "descricao_pt": "Lavoura de soja colhida no Rio Grande do Sul com trator/colheitadeira ao fundo no fim de tarde, sem rostos identificáveis",
            "query_en": ["soybean field harvest brazil", "tractor farm field sunset", "agriculture crop south brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A wide soybean field in southern Brazil at late afternoon with a harvester in the distance, warm golden light, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta agro estadual central para a audiência rural; fato setorial concreto sobre crédito e safra, sem viés partidário."
    },

    # IDX 25 — Vinhos vencidos apreendidos (RS) — REBAIXAR
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": _skip(
        "REBAIXAR", "Operação estadual de fiscalização (duplicada com o item de 630 kg). Mantida como nota; evita duas matérias do mesmo fato."),

    # IDX 26 — Fiscais apreendem 630 kg de alimentos (RS) — REBAIXAR
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": _skip(
        "REBAIXAR", "Mesmo fato da apreensão pela fiscalização estadual; sem âncora em cidade-núcleo. Vira nota de consumo."),

    # IDX 27 — Frio abaixo de zero em quase 70 cidades (RS) — PUBLICAR
    "775f9b501ba50ff6ad224de967b2336e8dfb9479": {
        "titulo_sultv": "Quase 70 cidades gaúchas registram frio abaixo de zero e marcam as menores temperaturas do ano",
        "chamada_faixa": "Frio congelante cobre quase 70 cidades do RS",
        "subtitulo": "Manhã desta quarta teve geada e temperaturas negativas em todo o Estado; mínima de 2026 segue em -6,4 °C.",
        "lead": "O inverno mostrou a que veio no Rio Grande do Sul. Um grande número de cidades gaúchas registrou nesta quarta-feira (24) as menores temperaturas do ano até agora, em um amanhecer de frio congelante e geada, com impacto direto sobre as lavouras e a rotina dos moradores da Costa Doce.",
        "ganchos_3": [
            "Quase 70 cidades gaúchas registram temperaturas abaixo de zero",
            "Manhã desta quarta teve as menores marcas do ano",
            "Mínima de 2026 segue em -6,4 °C, registrada em Pinheiro Machado"
        ],
        "angulo_editorial": "Fato climático estadual concreto e datado, de alto interesse para a audiência rural e urbana. Impacto direto sobre lavouras (geada) e rotina. Conteúdo próprio, sem citar veículo de meteorologia.",
        "fontes_complementares_sugeridas": ["Institutos de meteorologia", "Emater/RS", "Defesa Civil do RS"],
        "lead_materia_longa": "O inverno mostrou a que veio no Rio Grande do Sul. Um grande número de cidades gaúchas registrou nesta quarta-feira (24) as menores temperaturas do ano até agora, em um amanhecer de frio congelante e geada.",
        "post_instagram": {
            "caption": "O Rio Grande do Sul acordou congelando. Nesta quarta-feira (24), quase 70 cidades gaúchas registraram temperaturas abaixo de zero, marcando as menores temperaturas do ano até agora, num amanhecer de frio intenso e geada. A mínima de 2026 no Estado segue sendo de -6,4 °C, registrada em Pinheiro Machado, no dia 16 de junho. Além do desconforto, o frio extremo acende o alerta no campo: a geada pode afetar lavouras e pastagens, e exige cuidado redobrado com os animais. Para os moradores, o recado é se agasalhar bem, proteger os mais vulneráveis e ficar atento às orientações da Defesa Civil. O inverno chegou com força na Costa Doce.",
            "hashtags": ["#RioGrandeDoSul", "#Frio", "#Geada", "#Inverno", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O RS acordou congelando.",
            "desenvolvimento_45s": "Nesta quarta-feira, quase 70 cidades gaúchas registraram temperaturas abaixo de zero, marcando as menores temperaturas do ano até agora, num amanhecer de frio intenso e geada. A mínima de 2026 no Estado segue sendo de menos 6,4 graus, em Pinheiro Machado. Além do desconforto, o frio extremo acende o alerta no campo: a geada pode afetar lavouras e pastagens e exige cuidado com os animais. Para os moradores, vale se agasalhar bem e proteger os mais vulneráveis.",
            "fechamento_8s": "O inverno chegou com força.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativo clima"
        },
        "tag_thumbnail": "frio, geada no RS",
        "briefing_visual": {
            "descricao_pt": "Campo coberto de geada branca ao amanhecer no interior do Rio Grande do Sul, sol baixo no horizonte, sem pessoas",
            "query_en": ["frost covered field sunrise", "white frost grass morning", "frozen pasture winter"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A rural field covered in white frost at sunrise in southern Brazil, low golden sun on the horizon, cold winter morning, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato climático estadual concreto e datado, alto interesse rural+urbano e impacto direto sobre lavouras (geada). Conteúdo próprio, sem citar veículo."
    },
}


MATERIAS = {

    "ae480230bb1ab97528290995310f77d546ac5818": """### Título ###
Junho Vermelho: inverno derruba estoques de sangue e doação se torna urgente na Costa Doce

### Artigo ###
Os dias frios trazem um alerta que se repete todo ano. Com a chegada do inverno, período em que os estoques dos hemocentros costumam registrar queda, a campanha Junho Vermelho chama a atenção dos moradores de Camaquã e de toda a Costa Doce para a importância da doação regular de sangue, um gesto simples que pode salvar vidas. A redução não acontece por acaso. No frio, as pessoas saem menos de casa, adiam compromissos e acabam deixando a doação para depois. Ao mesmo tempo, a demanda dos hospitais não diminui: cirurgias, tratamentos de saúde e atendimentos de emergência seguem dependendo de bolsas disponíveis. É justamente nesse descompasso que mora o risco. Quando os estoques baixam, qualquer imprevisto pode se transformar em uma corrida contra o tempo para encontrar o tipo sanguíneo necessário. Doar sangue é um ato seguro, rápido e que não prejudica a saúde de quem doa. Em poucos minutos, o doador contribui com uma quantidade que o organismo repõe naturalmente, e uma única bolsa pode beneficiar mais de uma pessoa. Os requisitos são simples: estar bem de saúde, dentro da faixa de peso e idade exigidas, alimentado e com documento de identificação. Pequenos cuidados antes e depois da doação garantem que tudo ocorra tranquilamente. A campanha Junho Vermelho existe para manter essa consciência viva durante todo o ano, e não apenas nos momentos de falta. Doadores regulares são a base de um sistema de saúde que funciona, porque garantem previsibilidade aos hemocentros e segurança a quem precisa de uma transfusão. No interior, onde as distâncias podem dificultar o acesso rápido, manter os estoques abastecidos é ainda mais importante. O recado para a população da Costa Doce é direto: se você está saudável, reserve um tempo para doar e leve um amigo junto. Espalhar a informação também ajuda, porque cada novo doador fortalece toda a rede. No inverno ou em qualquer estação, a solidariedade de quem doa é o que mantém vidas em movimento.

### Legenda sugerida ###
Inverno derruba os estoques dos hemocentros; campanha Junho Vermelho reforça a importância da doação regular de sangue.

### Palavras-chave ###
Junho Vermelho, doação de sangue, Camaquã, hemocentro, inverno, Costa Doce, saúde
""",

    "69e55e539fb3c957f367c14db975687ca36e8e76": """### Título ###
Defesa Civil de Tapes participa de congresso internacional e debate preparação para o El Niño

### Artigo ###
A prevenção a desastres entrou na pauta de Tapes. A Defesa Civil do município participou do Congresso Internacional de Proteção e Defesa Civil, o CIPDC 2026, realizado de 23 a 25 de junho em Porto Alegre, onde gestores discutiram a preparação para o fenômeno El Niño 2026/2027 e a resposta a eventos climáticos extremos que afetam a Costa Doce. Representando o município, participaram do evento o assessor e o coordenador da Defesa Civil de Tapes, que acompanharam debates, palestras e a troca de experiências com gestores públicos, especialistas e instituições de diversas regiões. Encontros como esse têm um valor que vai além do conteúdo das palestras. Eles permitem que municípios pequenos conheçam soluções já testadas em outras localidades, atualizem protocolos e construam redes de apoio que fazem diferença na hora de uma emergência. Quando a próxima crise chega, ter contatos, planos e procedimentos definidos pode significar respostas mais rápidas e menos prejuízos. A preparação para o El Niño ganha destaque porque o fenômeno costuma alterar o regime de chuvas, aumentando o risco de temporais, enchentes e alagamentos. Para a Costa Doce, região que conhece de perto os efeitos das cheias, antecipar-se a esses cenários é fundamental. Mapear áreas vulneráveis, orientar a população e organizar planos de contingência são medidas que reduzem danos e protegem vidas. A atuação da Defesa Civil é, muitas vezes, silenciosa, mas essencial. É ela que monitora as condições climáticas, emite alertas, coordena evacuações quando necessário e articula o socorro às famílias atingidas. Quanto mais preparada e capacitada estiver a equipe, maior a capacidade de resposta do município diante de um evento extremo. A participação de Tapes no congresso reforça uma postura de planejamento. Em vez de apenas reagir aos desastres, o município busca conhecimento para preveni-los e enfrentá-los com mais estrutura. Investir em capacitação é investir na segurança de toda a comunidade, mostrando que prevenção e informação caminham juntas na proteção das pessoas e do patrimônio.

### Legenda sugerida ###
Defesa Civil de Tapes participa do CIPDC 2026, em Porto Alegre, com foco na preparação para o El Niño 2026/2027.

### Palavras-chave ###
Tapes, Defesa Civil, CIPDC 2026, El Niño, prevenção, Costa Doce, eventos climáticos
""",

    "1731235a445ae103fcc24a28232938f2407b1f1a": """### Título ###
Declaração Anual de Rebanho: produtores de Tapes têm até 30 de junho para regularizar

### Artigo ###
O relógio corre para o produtor rural da Costa Doce. Os produtores de Tapes têm até o dia 30 de junho para realizar a Declaração Anual de Rebanho 2026, uma atualização obrigatória para todos que possuem animais de produção e que é fundamental para o controle sanitário e o planejamento do setor agropecuário no município. A orientação é reforçada pela Secretaria Municipal de Agricultura e Desenvolvimento Rural. A declaração de rebanho é muito mais do que uma formalidade. É por meio dela que os órgãos de defesa agropecuária mantêm atualizado o mapa da pecuária regional, sabendo quantos animais existem, onde estão e quais cuidados sanitários precisam ser adotados. Essas informações são a base para campanhas de vacinação, para o controle de doenças e para o planejamento de políticas voltadas ao produtor. Manter os dados em dia também protege o próprio criador. Um rebanho declarado e regularizado facilita o acesso a crédito, a participação em programas de incentivo e a comercialização dos animais, além de evitar penalidades por irregularidade. Em um setor que depende de confiança sanitária para vender sua produção, estar em conformidade é uma vantagem concreta. A boa notícia é que o processo é simples e acessível. A declaração pode ser feita de forma online, pelo sistema do Produtor Online, sem que o criador precise sair de casa, ou presencialmente, na Inspetoria de Defesa Agropecuária de Tapes, onde a equipe orienta quem tiver dúvidas. Quem ainda não atualizou os dados deve se organizar para não deixar para a última hora. O risco de deixar o prazo passar é real. Sem a declaração, o produtor pode enfrentar dificuldades para movimentar animais, acessar serviços e comprovar a regularidade da atividade. Por isso, a recomendação é reunir as informações do rebanho com antecedência e concluir a declaração dentro do período. Ao cumprir essa obrigação, o produtor de Tapes contribui para a sanidade do rebanho regional e fortalece toda a cadeia agropecuária da Costa Doce, garantindo um setor mais organizado, seguro e preparado para crescer.

### Legenda sugerida ###
Produtores de Tapes têm até 30 de junho para fazer a Declaração Anual de Rebanho 2026, online ou na Inspetoria de Defesa Agropecuária.

### Palavras-chave ###
Tapes, Declaração de Rebanho, agropecuária, defesa agropecuária, produtor rural, prazo, Costa Doce
""",

    "5ec657641f88db018d679fc6eb7bd0bf38269a1e": """### Título ###
Festa Junina de Arambaré reúne a comunidade nesta sexta com música, quadrilha e show

### Artigo ###
A tradição junina toma conta de Arambaré nesta sexta-feira. A Festa Junina do município acontece no dia 27 de junho, a partir das 16h, no Loteamento Popular, com uma programação que reúne coral, apresentações de estudantes, quadrilha e show de banda para celebrar o São João com toda a comunidade da Costa Doce. O evento foi preparado para ser uma tarde de alegria, cultura e diversão para todas as idades. A abertura fica por conta do Coral Municipal de Arambaré, seguido das apresentações dos estudantes da rede, que sobem ao palco para mostrar o resultado do trabalho preparado em sala de aula. Mais tarde, o grupo do CRAS apresenta números típicos, como o tradicional casamento na roça e a quadrilha, momentos que arrancam risadas e aplausos do público. Para fechar a noite, a festa recebe um show de banda, garantindo música e animação para quem quiser prolongar a comemoração. Mais do que entretenimento, festas como essa cumprem um papel importante na vida comunitária. Elas valorizam as tradições juninas, fortalecem o sentimento de pertencimento e aproximam famílias, vizinhos e gerações em torno de uma celebração que faz parte da cultura brasileira. No interior, esses encontros têm um sabor especial, porque reúnem a cidade inteira em um mesmo espaço de convivência. A escolha do Loteamento Popular como cenário facilita o acesso e amplia a participação dos moradores. Com entrada aberta à comunidade, a expectativa é de bom público para prestigiar os estudantes e celebrar as tradições. Comidas típicas, brincadeiras e a decoração característica completam o clima de arraial, transformando a tarde em um momento de confraternização. O convite está feito a toda a população. A Festa Junina de Arambaré é a oportunidade de reunir a família, encontrar os amigos e valorizar o talento dos estudantes do município, num evento que celebra a cultura e o espírito de comunidade que marcam a Costa Doce. Quem comparecer vai encontrar uma noite especial, feita para guardar boas lembranças.

### Legenda sugerida ###
Festa Junina de Arambaré acontece nesta sexta (27), a partir das 16h, no Loteamento Popular, com coral, quadrilha e show.

### Palavras-chave ###
Arambaré, Festa Junina, São João, comunidade, cultura, evento, Costa Doce
""",

    "31fb7c80312523d384bb96a83eefaaca270eaf81": """### Título ###
Chuvisca avança na construção de nova UBS com investimento de R$ 2,45 milhões

### Artigo ###
A saúde de Chuvisca ganha um reforço de peso. A construção da nova Unidade Básica de Saúde Porte II segue avançando no município, viabilizada por um investimento de R$ 2.452.054,00 e voltada à ampliação e à qualificação dos serviços de saúde oferecidos à população da Costa Doce. A obra é resultado de um processo cuidadoso, que envolveu planejamento, estudos técnicos e o cumprimento de todas as etapas necessárias até a viabilização do projeto. Antes de o canteiro de obras ser aberto, foi preciso percorrer um caminho que incluiu a aquisição do terreno, o licenciamento e as autorizações técnicas e ambientais. Esse rigor garante que a unidade nasça em condições adequadas e dentro das normas, evitando problemas futuros e assegurando que o investimento público seja bem aplicado. Concluídas as etapas iniciais, o município foi contemplado com o recurso que permitiu dar início à construção. Uma Unidade Básica de Saúde é a porta de entrada do sistema público de saúde. É nela que a população encontra atendimento médico e de enfermagem, acompanhamento de doenças crônicas, vacinas, pré-natal, curativos e o encaminhamento para serviços mais especializados quando necessário. Quanto melhor a estrutura, mais qualidade e conforto no atendimento, tanto para os pacientes quanto para os profissionais que trabalham no local. Para um município do interior, contar com uma unidade ampliada significa reduzir deslocamentos, aproximar o cuidado das famílias e desafogar a demanda por atendimento. A nova UBS Porte II foi pensada para oferecer mais espaço e melhores condições, acompanhando o crescimento da população e as necessidades de saúde da comunidade. Cada etapa concluída representa um avanço concreto. Obras como essa mostram que o investimento em infraestrutura é, na prática, investimento nas pessoas, porque se traduz em mais acesso e em melhor atendimento no dia a dia. Ao avançar na construção da nova unidade, Chuvisca reafirma o compromisso com uma saúde pública mais estruturada e próxima de quem precisa, fortalecendo a rede de cuidado na Costa Doce.

### Legenda sugerida ###
Chuvisca avança na construção da nova UBS Porte II, viabilizada por investimento de R$ 2,45 milhões, para ampliar a saúde pública.

### Palavras-chave ###
Chuvisca, UBS, saúde, investimento, infraestrutura, Costa Doce, atendimento
""",

    "15920be0f1a1a4cd24939465621c58afc813ef2d": """### Título ###
Barra do Ribeiro inaugura Núcleo de Atendimento Especializado para crianças com TEA

### Artigo ###
A inclusão ganhou um endereço em Barra do Ribeiro. Na última terça-feira, 23 de junho, o município inaugurou o Núcleo de Atendimento Especializado voltado a crianças com Transtorno do Espectro Autista, um espaço que reúne serviços de fonoaudiologia, terapia ocupacional e atendimento educacional especializado para alunos da rede municipal de ensino. O projeto foi desenvolvido pela Prefeitura, por meio das secretarias municipais de Educação e Cultura e de Saúde, em uma ação que une duas áreas essenciais no cuidado com a infância. A criação do núcleo responde a uma necessidade concreta das famílias. Crianças com TEA se beneficiam de acompanhamento especializado e contínuo, que estimula a comunicação, a autonomia e o desenvolvimento de habilidades importantes para o convívio e a aprendizagem. Reunir esses serviços em um único espaço facilita o acesso, organiza o atendimento e dá mais conforto às famílias, que muitas vezes precisavam buscar apoio em outras cidades. Entre os serviços oferecidos estão a fonoaudiologia, que trabalha a linguagem e a comunicação; a terapia ocupacional, que desenvolve habilidades para as atividades do dia a dia; e o atendimento educacional especializado, que apoia a inclusão escolar e a aprendizagem. Juntos, esses atendimentos formam uma rede de cuidado que olha para a criança de maneira integral, respeitando o ritmo e as necessidades de cada uma. Neste primeiro momento, o trabalho começa pelos alunos da rede municipal de ensino, garantindo que o suporte chegue de forma estruturada a quem já está no ambiente escolar. A integração entre educação e saúde é um dos pontos fortes da iniciativa, porque permite que professores, terapeutas e famílias caminhem na mesma direção, somando esforços em favor do desenvolvimento das crianças. Iniciativas como essa mostram que acolher é também estruturar serviços. Mais do que um discurso, a inclusão se concretiza quando existem espaços preparados, profissionais capacitados e atendimento de qualidade. Ao inaugurar o núcleo, Barra do Ribeiro dá um passo importante para garantir que cada criança tenha as oportunidades e o apoio de que precisa para se desenvolver com dignidade.

### Legenda sugerida ###
Barra do Ribeiro inaugura Núcleo de Atendimento Especializado para crianças com TEA, com fonoaudiologia, terapia ocupacional e AEE.

### Palavras-chave ###
Barra do Ribeiro, TEA, inclusão, atendimento especializado, educação, saúde, crianças
""",

    "01ef011ecdae21c60e1584906736e0e1b68bd082": """### Título ###
Cristal melhora estradas do interior com cascalhamento e patrolamento e apoia o produtor rural

### Artigo ###
As estradas que ligam o campo à cidade estão recebendo atenção em Cristal. A Prefeitura executa melhorias nas vias do interior do município, com serviços de cascalhamento, patrolamento e apoio às propriedades rurais em diferentes localidades, garantindo o escoamento da produção e o acesso das famílias na Costa Doce. O trabalho atende a uma demanda histórica de quem vive longe do centro e depende das estradas para a rotina e para o trabalho. As intervenções incluem o cascalhamento, que cobre o leito da estrada com material que melhora a trafegabilidade, e o patrolamento, que nivela e regulariza a superfície da via. Juntas, essas ações reduzem buracos, atoleiros e poeira, problemas comuns nas estradas de terra, especialmente nos períodos de chuva. O apoio direto às propriedades rurais completa o serviço, ajudando o produtor a manter os acessos em condições de uso. A importância dessas obras é facilmente percebida no dia a dia. É pela estrada rural que a produção chega ao mercado, que o leite é coletado, que o transporte escolar leva as crianças à escola e que as ambulâncias chegam até quem precisa de atendimento. Uma via em más condições atrapalha tudo isso, encarece o frete, danifica veículos e máquinas e, em casos extremos, pode deixar famílias isoladas. Para a economia local, estradas bem cuidadas são um investimento que se paga. Elas facilitam o escoamento da safra, baratizam o transporte e dão mais segurança a quem circula pelo interior. Em uma região de forte vocação agrícola, manter a malha rural em boas condições é condição básica para o desenvolvimento, porque conecta o produtor aos mercados e aos serviços. Ao priorizar as estradas do interior, Cristal demonstra atenção a quem produz e movimenta a economia do município. As melhorias representam mais do que conforto: significam acesso, segurança e oportunidades para as famílias rurais. Cada trecho recuperado é um passo a mais para integrar o campo e a cidade, reforçando que cuidar da infraestrutura rural é cuidar de quem sustenta a vida no interior da Costa Doce.

### Legenda sugerida ###
Cristal realiza melhorias nas estradas do interior, com cascalhamento, patrolamento e apoio às propriedades rurais.

### Palavras-chave ###
Cristal, estradas rurais, cascalhamento, patrolamento, infraestrutura, agro, Costa Doce
""",

    "b969263c34ba39f0fe24cd73c37f46b35ac7db50": """### Título ###
Inédito: pescadores de Pelotas e Rio Grande assinam os primeiros contratos de crédito do Incra no país

### Artigo ###
O Sul do Rio Grande do Sul entrou para a história da pesca artesanal brasileira. Famílias de cinco comunidades pesqueiras de Pelotas e Rio Grande foram as primeiras de todo o país a assinar contratos do Crédito Instalação do Incra, em ato realizado na Colônia Z3, um marco que reforça o apoio à pesca artesanal na Costa Doce. A assinatura aconteceu no dia 23 de junho e simboliza o reconhecimento de uma atividade tradicional que move a economia e a cultura da região. O Crédito Instalação é uma política voltada ao fortalecimento de famílias do campo e das águas, oferecendo recursos para que possam se estabelecer, estruturar a atividade produtiva e melhorar as condições de trabalho e de vida. Ao alcançar pela primeira vez comunidades pesqueiras artesanais, o programa amplia seu alcance e passa a contemplar um setor que historicamente teve dificuldade de acesso a esse tipo de apoio. Para os pescadores, o significado vai além do recurso financeiro. Trata-se do reconhecimento de que a pesca artesanal é uma atividade econômica legítima, que sustenta famílias, abastece o mercado com pescado de qualidade e preserva saberes passados de geração em geração. Esse tipo de apoio ajuda a dar segurança e perspectiva de futuro a quem vive da lagoa e do mar. A escolha da Colônia Z3 como palco do ato tem forte simbolismo. A comunidade é uma das mais tradicionais do estado quando o assunto é pesca artesanal, e sediar a assinatura dos primeiros contratos do país reforça o protagonismo da região nesse cenário. O pioneirismo gaúcho serve de referência para que a política chegue, no futuro, a outras comunidades pesqueiras pelo Brasil. O impacto esperado é concreto. Com acesso a crédito, as famílias podem investir em equipamentos, melhorar a estrutura de trabalho e ganhar mais autonomia. Isso se traduz em renda, em permanência das comunidades em seus territórios e na valorização de uma atividade essencial. Ao protagonizar esse momento histórico, Pelotas e Rio Grande mostram a força da pesca artesanal e reafirmam a importância de apoiar quem vive da água na Costa Doce.

### Legenda sugerida ###
Comunidades pesqueiras de Pelotas e Rio Grande são as primeiras do país a assinar o Crédito Instalação do Incra, em ato na Colônia Z3.

### Palavras-chave ###
Pelotas, Rio Grande, pesca artesanal, Incra, Crédito Instalação, Colônia Z3, Costa Doce
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS acompanham com apreensão a renegociação das dívidas rurais antes da safra

### Artigo ###
A próxima safra começa a ser planejada sob tensão no campo gaúcho. Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação das dívidas rurais, temerosos de ficar sem acesso ao crédito necessário para o plantio, um impasse que mexe diretamente com a economia do interior e da Costa Doce. Depois de anos marcados por adversidades climáticas, que reduziram a produção e comprometeram a renda no campo, muitos produtores dependem dessa renegociação para reorganizar as contas e seguir produzindo. O crédito rural é o combustível que mantém a atividade agrícola em movimento. É com ele que o produtor compra sementes, insumos, combustível e tudo o que precisa para plantar e colher. Sem acesso a esse financiamento, o ciclo da produção fica ameaçado, com reflexos que vão além da porteira e atingem o comércio, os fornecedores e o emprego nas cidades do interior. Por isso, a definição sobre a renegociação é acompanhada de perto por quem vive da terra. A preocupação do setor é compreensível. Quando o produtor enfrenta dívidas acumuladas e ainda assim precisa investir na nova safra, a falta de uma solução pode significar a redução da área plantada ou até a interrupção da atividade. Isso impacta a oferta de alimentos, a economia regional e a permanência das famílias no campo. O endividamento, em boa parte, é herança de estiagens e enchentes que castigaram as lavouras nas últimas temporadas, fugindo do controle de quem trabalha na terra. O tema une produtores de diferentes regiões do estado. O Rio Grande do Sul tem peso importante na produção nacional, e o que acontece com o crédito rural gaúcho repercute em toda a cadeia do agronegócio, dos insumos ao transporte, da indústria ao consumidor. Uma solução equilibrada é vista como essencial para dar fôlego ao setor e preservar empregos e renda. Enquanto a renegociação tramita, o campo espera por respostas que tragam previsibilidade e permitam ao produtor planejar a próxima safra com mais tranquilidade e segurança. Para o interior gaúcho, garantir o acesso ao crédito é garantir que a roda da economia continue girando.

### Legenda sugerida ###
Produtores do RS temem ficar sem crédito para a próxima safra enquanto a renegociação das dívidas rurais tramita.

### Palavras-chave ###
agro, Rio Grande do Sul, crédito rural, dívidas rurais, safra, produtores, renegociação
""",

    "775f9b501ba50ff6ad224de967b2336e8dfb9479": """### Título ###
Quase 70 cidades gaúchas registram frio abaixo de zero e marcam as menores temperaturas do ano

### Artigo ###
O inverno mostrou a que veio no Rio Grande do Sul. Um grande número de cidades gaúchas registrou nesta quarta-feira (24) as menores temperaturas do ano até agora, em um amanhecer de frio congelante e geada, com impacto direto sobre as lavouras e a rotina dos moradores da Costa Doce. Quase 70 municípios marcaram valores abaixo de zero, num episódio de frio intenso que tomou conta de boa parte do estado. Apesar da intensidade, a marca mais baixa de 2026 segue sendo a registrada em Pinheiro Machado, de 6,4 graus negativos, no dia 16 de junho. Ainda assim, o amanhecer desta quarta-feira chamou a atenção pela amplitude do frio, que se espalhou por diferentes regiões e cobriu campos e telhados de geada branca. Episódios assim são típicos do inverno gaúcho, quando massas de ar frio avançam pelo estado e derrubam as temperaturas. O frio extremo, no entanto, não traz apenas desconforto. No campo, a geada acende o sinal de alerta. Lavouras sensíveis e pastagens podem ser prejudicadas pela formação de gelo sobre as folhas, e os produtores precisam redobrar a atenção com os animais, especialmente os mais jovens e vulneráveis. Garantir abrigo, alimentação reforçada e água que não congele é parte dos cuidados necessários para atravessar os dias mais rigorosos sem perdas. Nas cidades, o frio intenso exige cuidados com a saúde e com as pessoas em situação de vulnerabilidade. Idosos, crianças e quem vive nas ruas estão mais expostos aos riscos das baixas temperaturas, e a solidariedade da comunidade faz diferença nesses períodos. Agasalhar-se bem, manter os ambientes aquecidos com segurança e evitar a exposição prolongada ao frio são recomendações básicas. A orientação é acompanhar as informações das autoridades e dos órgãos de defesa civil, que monitoram as condições do tempo e emitem alertas quando necessário. O inverno apenas começou e novos episódios de frio podem ocorrer. Para a Costa Doce e para todo o Rio Grande do Sul, o recado é de atenção: proteger as pessoas, cuidar dos animais e preservar as lavouras é a melhor forma de enfrentar as madrugadas geladas que marcam a estação.

### Legenda sugerida ###
Quase 70 cidades gaúchas registraram frio abaixo de zero nesta quarta; a mínima de 2026 segue em -6,4 °C, em Pinheiro Machado.

### Palavras-chave ###
Rio Grande do Sul, frio, geada, inverno, temperaturas negativas, lavouras, Costa Doce
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
