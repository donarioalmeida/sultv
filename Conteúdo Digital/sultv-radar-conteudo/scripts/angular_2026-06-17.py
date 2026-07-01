#!/usr/bin/env python3
"""
angular_2026-06-17.py — angulação editorial + redação (cowork-faz-tudo).
Pauta de 2026-06-17. Regra 12 INEGOCIÁVEL aplicada: nenhum veículo de
comunicação é citado em títulos, leads, captions ou matérias. Atribuição
apenas a fontes primárias institucionais.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = datetime.now(timezone.utc).strftime("%Y-%m-%d")


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

    # 0. Camaquã — Festa de São João ampliada — PUBLICAR materia_longa
    "b19d54aa307276a3d94f4535e449d9aa14bf943a": {
        "titulo_sultv": "Festa de São João de Camaquã amplia programação com shows na Prainha no sábado",
        "chamada_faixa": "São João de Camaquã tem programação ampliada",
        "subtitulo": "Evento ocorre neste sábado (20) no Complexo Poliesportivo Ruy de Castro Netto, com atrações culturais a partir das 14h30.",
        "lead": "A Festa de São João de Camaquã terá programação ampliada neste sábado (20), no Complexo Poliesportivo Ruy de Castro Netto, na Prainha. A celebração reúne invernadas, grupos de folclore e shows musicais ao longo da tarde e da noite, com cerimônia oficial, bênção e acendimento da fogueira a partir das 20h.",
        "ganchos_3": [
            "Festa de São João de Camaquã acontece neste sábado (20) na Prainha",
            "Programação cultural começa às 14h30 com invernadas e folclore",
            "Cerimônia oficial e acendimento da fogueira às 20h"
        ],
        "angulo_editorial": "Cultura e tradição em cidade-núcleo da cobertura — agenda de serviço com data, local e horários, perfil familiar; pauta positiva de calendário regional junino.",
        "fontes_complementares_sugeridas": ["Prefeitura de Camaquã", "Secretaria Municipal de Cultura de Camaquã"],
        "lead_materia_longa": "A Festa de São João de Camaquã terá programação ampliada neste sábado (20), no Complexo Poliesportivo Ruy de Castro Netto, na Prainha, com atrações culturais a partir das 14h30.",
        "post_instagram": {
            "caption": "A Festa de São João de Camaquã vem com tudo neste sábado (20), na Prainha! A programação foi ampliada e começa às 14h30 com invernadas e grupos de folclore, seguindo com shows ao longo da tarde. Às 20h tem cerimônia oficial, bênção e o acendimento da fogueira. Um dia de cultura, tradição e diversão para toda a família.",
            "hashtags": ["#Camaquã", "#SãoJoão", "#FestasJuninas", "#Cultura", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "São João chega em Camaquã.",
            "desenvolvimento_45s": "A Festa de São João de Camaquã terá programação ampliada neste sábado, dia 20, no Complexo Poliesportivo Ruy de Castro Netto, na Prainha. A celebração começa às 14h30, com invernadas e grupos de folclore, e segue com shows musicais ao longo da tarde. À noite, às 20h, acontece a cerimônia oficial, a bênção do pároco e o tradicional acendimento da fogueira. É um evento gratuito, pensado para reunir famílias em torno da cultura e das tradições juninas da região.",
            "fechamento_8s": "Tradição junina na Prainha.",
            "cta_5s": "Programe-se com o SulTV.",
            "trilha_sugerida": "instrumental festivo regional"
        },
        "tag_thumbnail": "São João de Camaquã",
        "briefing_visual": {
            "descricao_pt": "Fogueira de festa junina acesa à noite com bandeirinhas coloridas ao fundo, ambiente de arraial no Sul do Brasil, sem rostos identificáveis",
            "query_en": ["bonfire festa junina night", "june festival decorations brazil", "country festival flags bonfire"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A bonfire burning at night during a Brazilian June festival, colorful paper flags strung overhead, festive rural setting in southern Brazil, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agenda cultural concreta (data, local, horários) em cidade-núcleo; pauta junina familiar de serviço"
    },

    # 1. Camaquã — jantar beneficente em prol de Sandra — REBAIXAR
    "7b19c5762b0ea7ea5f46b7b25a84fff142f01213": _skip(
        "REBAIXAR",
        "Conteúdo escasso na fonte e identificação de pessoa privada em contexto de campanha pessoal (provável saúde) — risco de regra de saúde/identificação; vira nota interna"
    ),

    # 2. Tapes — R$ 6,9 mi e 34 moradias — PUBLICAR materia_longa
    "85e1e49c224d76ffee83f0d7ac8e9cbdaeeedfa6": {
        "titulo_sultv": "Tapes garante R$ 6,9 milhões e viabiliza 34 moradias para famílias em áreas de risco",
        "chamada_faixa": "Tapes garante R$ 6,9 mi para 34 moradias",
        "subtitulo": "Recursos do Fundo Nacional de Habitação de Interesse Social asseguram casas para famílias em situação de vulnerabilidade.",
        "lead": "O município de Tapes garantiu a manutenção de R$ 6,9 milhões do Fundo Nacional de Habitação de Interesse Social (FNHIS), recursos que vão viabilizar 34 moradias para famílias em situação de vulnerabilidade e em áreas de risco. O resultado veio após articulação técnica da defesa civil municipal junto à Caixa Econômica Federal e ao Ministério das Cidades.",
        "ganchos_3": [
            "Tapes assegura R$ 6,9 milhões do FNHIS para habitação",
            "Recurso viabiliza 34 moradias para famílias vulneráveis",
            "Mudança de regra permitiu aquisição de imóveis em vez de construção em área inviável"
        ],
        "angulo_editorial": "Habitação e proteção a famílias em área de risco em cidade-núcleo da Costa Doce — fato concreto com valor oficial e número de moradias, articulação institucional positiva; tema sensível pós-enchentes.",
        "fontes_complementares_sugeridas": ["Prefeitura de Tapes", "Defesa Civil de Tapes", "Ministério das Cidades", "Caixa Econômica Federal"],
        "lead_materia_longa": "O município de Tapes garantiu a manutenção de R$ 6,9 milhões do Fundo Nacional de Habitação de Interesse Social (FNHIS), recursos que vão viabilizar 34 moradias para famílias em situação de vulnerabilidade e em áreas de risco.",
        "post_instagram": {
            "caption": "Tapes garantiu R$ 6,9 milhões do Fundo Nacional de Habitação de Interesse Social para assegurar 34 moradias a famílias em situação de vulnerabilidade e em áreas de risco. O resultado veio de um trabalho técnico da defesa civil municipal com a Caixa e o Ministério das Cidades. Moradia digna é proteção para quem mais precisa.",
            "hashtags": ["#Tapes", "#Habitação", "#Moradia", "#FNHIS", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Moradia para 34 famílias em Tapes.",
            "desenvolvimento_45s": "Tapes garantiu a manutenção de 6,9 milhões de reais do Fundo Nacional de Habitação de Interesse Social, recursos que vão viabilizar 34 moradias para famílias em situação de vulnerabilidade e em áreas de risco. O projeto inicial previa 46 casas em um loteamento, mas estudos técnicos apontaram que a área exigiria altos investimentos em infraestrutura. Com uma nova portaria, o município passou a poder adquirir imóveis, assegurando o recurso e o atendimento às famílias. Foi um trabalho de articulação da defesa civil municipal com a Caixa e o Ministério das Cidades.",
            "fechamento_8s": "Recurso garantido para quem mais precisa.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental esperançoso"
        },
        "tag_thumbnail": "Moradias em Tapes",
        "briefing_visual": {
            "descricao_pt": "Conjunto de casas populares recém-construídas em cidade pequena do Sul do Brasil em dia claro, sem pessoas",
            "query_en": ["social housing houses brazil", "new affordable homes street", "small town residential houses"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A row of newly built simple social housing homes in a small southern Brazilian town on a clear day, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato concreto com valor oficial (R$ 6,9 mi) e número de moradias em cidade-núcleo; tema habitacional sensível e de alto interesse"
    },

    # 3. Tapes — Encontro estadual de escotismo (ECHEMAR) — PUBLICAR materia_longa
    "0d7e9665c5b4929e603f7055539c2c047848018f": {
        "titulo_sultv": "Tapes sedia encontro estadual do escotismo e celebra reabertura de grupo escoteiro",
        "chamada_faixa": "Tapes sedia encontro estadual do escotismo",
        "subtitulo": "Camping Municipal recebeu mais de 40 chefes e dirigentes escoteiros do RS e marcou a reabertura do Grupo Escoteiro do Mar Araxanes.",
        "lead": "Tapes foi sede, no último sábado (13), do ECHEMAR 2026 – Encontro de Chefes da Modalidade do Mar, que reuniu mais de 40 chefes e dirigentes escoteiros de diferentes regiões do Rio Grande do Sul. O encontro, realizado no Camping Municipal Antônio Alfonsin Simchen, também celebrou a reabertura do Grupo Escoteiro do Mar Araxanes.",
        "ganchos_3": [
            "Tapes sediou encontro estadual da modalidade do mar do escotismo",
            "Mais de 40 chefes e dirigentes de todo o RS participaram",
            "Evento marcou a reabertura do Grupo Escoteiro do Mar Araxanes"
        ],
        "angulo_editorial": "Comunidade e formação de jovens em cidade-núcleo às margens da Lagoa dos Patos — pauta positiva de engajamento social, com âncora na vocação náutica de Tapes; valoriza atividade que forma crianças e adolescentes.",
        "fontes_complementares_sugeridas": ["Prefeitura de Tapes", "União dos Escoteiros do Brasil – Região RS", "Grupo Escoteiro do Mar Araxanes"],
        "lead_materia_longa": "Tapes foi sede, no último sábado (13), do ECHEMAR 2026 – Encontro de Chefes da Modalidade do Mar, que reuniu mais de 40 chefes e dirigentes escoteiros de diferentes regiões do Rio Grande do Sul, no Camping Municipal Antônio Alfonsin Simchen.",
        "post_instagram": {
            "caption": "Tapes recebeu mais de 40 chefes e dirigentes escoteiros de todo o Rio Grande do Sul no ECHEMAR 2026, encontro da Modalidade do Mar realizado no Camping Municipal. O evento celebrou a reabertura do Grupo Escoteiro do Mar Araxanes — uma vitória para a formação de crianças e jovens em uma cidade que vive às margens da Lagoa dos Patos.",
            "hashtags": ["#Tapes", "#Escotismo", "#Comunidade", "#Juventude", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Escotismo em Tapes.",
            "desenvolvimento_45s": "Tapes foi sede do ECHEMAR 2026, o Encontro de Chefes da Modalidade do Mar, que reuniu mais de 40 chefes e dirigentes escoteiros de diferentes regiões do Rio Grande do Sul no Camping Municipal. Durante o evento, foram debatidos planejamentos e ações para fortalecer a Modalidade do Mar e celebrada a reabertura do Grupo Escoteiro do Mar Araxanes. Para uma cidade ribeirinha como Tapes, o escotismo náutico une formação de jovens, valores e o vínculo com a Lagoa dos Patos.",
            "fechamento_8s": "Formação e tradição às margens da lagoa.",
            "cta_5s": "Confira no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Escotismo em Tapes",
        "briefing_visual": {
            "descricao_pt": "Acampamento com barracas à beira de lago ao amanhecer no Sul do Brasil, bandeiras e mastro, sem rostos identificáveis",
            "query_en": ["scout camp tents lakeside", "camping tents lake morning", "outdoor camp flags"],
            "evitar": ["rostos identificáveis", "menores", "marcas", "texto", "logos"],
            "prompt_ia": "A camping site with tents beside a calm lake at sunrise in southern Brazil, a flagpole and flags, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento estadual sediado em cidade-núcleo, comunidade e formação de jovens; pauta positiva com âncora na vocação náutica local"
    },

    # 4. Arambaré — Saúde na Estrada no Assentamento Caturritas — PUBLICAR materia_longa
    "612ffb08a1ba713e460e43a35aebc9d85358c4c8": {
        "titulo_sultv": "Unidade móvel leva atendimento médico ao Assentamento Caturritas em Arambaré dia 25",
        "chamada_faixa": "Saúde na Estrada chega ao Caturritas em Arambaré",
        "subtitulo": "Programa Saúde na Estrada atende moradores da comunidade rural no dia 25 de junho; orientação é levar o Cartão do SUS.",
        "lead": "A Unidade Móvel de Saúde da Prefeitura de Arambaré estará no Assentamento Caturritas no dia 25 de junho, levando atendimento médico aos moradores da comunidade rural. A ação faz parte do programa Saúde na Estrada, que busca aproximar o atendimento das localidades mais distantes do município da Costa Doce.",
        "ganchos_3": [
            "Atendimento médico no Assentamento Caturritas em 25 de junho",
            "Programa Saúde na Estrada leva unidade móvel à zona rural",
            "Moradores devem levar o Cartão do SUS"
        ],
        "angulo_editorial": "Saúde de serviço e acesso na zona rural de cidade-núcleo — informação de utilidade imediata (data, local, orientação), sem teor médico-prescritivo; valoriza interiorização do atendimento.",
        "fontes_complementares_sugeridas": ["Prefeitura de Arambaré", "Secretaria Municipal de Saúde de Arambaré"],
        "lead_materia_longa": "A Unidade Móvel de Saúde da Prefeitura de Arambaré estará no Assentamento Caturritas no dia 25 de junho, levando atendimento médico aos moradores da comunidade rural, dentro do programa Saúde na Estrada.",
        "post_instagram": {
            "caption": "Saúde mais perto de quem vive no campo: a Unidade Móvel de Saúde de Arambaré atende no Assentamento Caturritas no dia 25 de junho, com consultas médicas para os moradores da comunidade. Não esqueça de levar o Cartão do SUS. O programa Saúde na Estrada leva atendimento até as localidades mais distantes do município.",
            "hashtags": ["#Arambaré", "#Saúde", "#SUS", "#SaúdeNaEstrada", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Saúde chega ao campo em Arambaré.",
            "desenvolvimento_45s": "A Unidade Móvel de Saúde de Arambaré vai atender no Assentamento Caturritas no dia 25 de junho, oferecendo consultas médicas aos moradores da comunidade rural. A ação faz parte do programa Saúde na Estrada, que leva atendimento às localidades mais distantes do município. Quem for ser atendido deve levar o Cartão do SUS. É uma forma de garantir que o cuidado com a saúde chegue também a quem vive longe do centro.",
            "fechamento_8s": "Atendimento no dia 25 de junho.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental acolhedor"
        },
        "tag_thumbnail": "Saúde na Estrada Arambaré",
        "briefing_visual": {
            "descricao_pt": "Van ou unidade móvel de saúde estacionada em estrada de terra de zona rural no Sul do Brasil, sem rostos identificáveis",
            "query_en": ["mobile health unit van rural", "medical van countryside road", "rural health outreach vehicle"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A mobile health unit van parked on a dirt road in a rural community in southern Brazil, daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de saúde com data e local em comunidade rural de cidade-núcleo; utilidade imediata sem teor médico-prescritivo"
    },

    # 5. Arambaré — cursos de qualificação (16/abril) — REBAIXAR (antiga)
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "REBAIXAR",
        "Notícia datada de 16/04/2026 raspada da página da prefeitura — inscrições provavelmente encerradas; publicar como atual seria impreciso"
    ),

    # 6. Cristal — reunião de planejamento de limpeza/manutenção — REBAIXAR
    "6d4334f756e8e21932963970c56e3ad757bf1c64": _skip(
        "REBAIXAR",
        "Reunião administrativa de rotina sobre planejamento de serviços de limpeza — fato fino, sem entregável concreto à população; vira nota interna"
    ),

    # 7. Cristal — reunião com 30º BPM, pedido de aumento de efetivo — PUBLICAR materia_longa
    "f6344ccfbeebeb426982842a44881910459162a4": {
        "titulo_sultv": "Cristal pede aumento do efetivo da Brigada Militar em reunião com o 30º BPM",
        "chamada_faixa": "Cristal pede mais efetivo da Brigada Militar",
        "subtitulo": "Administração municipal recebeu o comando do 30º Batalhão para tratar do fortalecimento da segurança pública na cidade.",
        "lead": "A Administração Municipal de Cristal recebeu o comando do 30º Batalhão de Polícia Militar para uma reunião voltada ao fortalecimento da segurança pública no município. Entre as principais demandas apresentadas, o município solicitou o aumento do efetivo da Brigada Militar para ampliar a presença policial na cidade da Costa Doce.",
        "ganchos_3": [
            "Cristal solicita ampliação do efetivo da Brigada Militar",
            "Reunião reuniu administração municipal e comando do 30º BPM",
            "Objetivo é reforçar a segurança pública no município"
        ],
        "angulo_editorial": "Segurança pública em cidade-núcleo — demanda concreta da administração por mais policiamento, pauta institucional de interesse direto da população; sem viés partidário.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "30º Batalhão de Polícia Militar", "Brigada Militar"],
        "lead_materia_longa": "A Administração Municipal de Cristal recebeu o comando do 30º Batalhão de Polícia Militar para uma reunião voltada ao fortalecimento da segurança pública no município, na qual solicitou o aumento do efetivo da Brigada Militar.",
        "post_instagram": {
            "caption": "Cristal quer mais segurança nas ruas: em reunião com o comando do 30º Batalhão de Polícia Militar, a administração municipal pediu o aumento do efetivo da Brigada Militar para ampliar o policiamento na cidade. A segurança pública é uma das principais demandas da população, e o diálogo entre município e Brigada é o caminho para fortalecer o efetivo.",
            "hashtags": ["#Cristal", "#Segurança", "#BrigadaMilitar", "#SegurançaPública", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Mais segurança em Cristal.",
            "desenvolvimento_45s": "A administração municipal de Cristal recebeu o comando do 30º Batalhão de Polícia Militar para discutir o fortalecimento da segurança pública na cidade. Entre as principais demandas, o município pediu o aumento do efetivo da Brigada Militar, buscando ampliar a presença policial nas ruas. A segurança é uma das maiores preocupações da população, e o reforço do policiamento depende da articulação entre o poder municipal e as forças de segurança do estado.",
            "fechamento_8s": "Município cobra reforço no policiamento.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Segurança em Cristal",
        "briefing_visual": {
            "descricao_pt": "Viatura da Brigada Militar estacionada em rua de cidade pequena do interior do RS em dia claro, sem rostos identificáveis",
            "query_en": ["police car street brazil", "military police vehicle town", "patrol car small town"],
            "evitar": ["rostos identificáveis", "placas legíveis", "texto", "logos"],
            "prompt_ia": "A military police patrol car parked on a quiet street of a small town in southern Brazil during the day, no identifiable people, no readable plates, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Demanda concreta de segurança pública (aumento de efetivo) em cidade-núcleo, interesse direto da população; tom institucional sem viés partidário"
    },

    # 8. São Lourenço do Sul — atualização de vacinação dia 17 — PUBLICAR materia_longa
    "30a1e2c79d28bac9d592e51269a0709cf8f404a6": {
        "titulo_sultv": "São Lourenço do Sul faz atualização da carteira de vacinação nesta quarta no Centro",
        "chamada_faixa": "São Lourenço atualiza carteira de vacinação dia 17",
        "subtitulo": "Equipe de vacinação atende em frente à Farmácia Municipal nesta quarta (17), nos turnos da manhã e da tarde.",
        "lead": "São Lourenço do Sul realiza nesta quarta-feira (17) uma ação de atualização das carteiras de vacinação da comunidade. A equipe de vacinação atende em frente à Farmácia Municipal, na Rua Coronel Alfredo Born, nº 288, no Centro, das 9h às 11h e das 13h às 16h.",
        "ganchos_3": [
            "Atualização de vacinas nesta quarta-feira (17) no Centro",
            "Atendimento das 9h às 11h e das 13h às 16h",
            "Comunidade deve levar a carteira de vacinação"
        ],
        "angulo_editorial": "Saúde de serviço com data, local e horário precisos em cidade-núcleo — utilidade imediata para o leitor, sem teor médico-prescritivo; incentivo à prevenção coletiva.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Secretaria Municipal de Saúde de São Lourenço do Sul"],
        "lead_materia_longa": "São Lourenço do Sul realiza nesta quarta-feira (17) uma ação de atualização das carteiras de vacinação da comunidade, em frente à Farmácia Municipal, no Centro, das 9h às 11h e das 13h às 16h.",
        "post_instagram": {
            "caption": "Tem vacina para colocar em dia? Nesta quarta-feira (17), a equipe de vacinação de São Lourenço do Sul atende em frente à Farmácia Municipal, no Centro, das 9h às 11h e das 13h às 16h. Leve a tua carteira de vacinação e confira se está tudo em dia. Cuidar da saúde é um gesto simples que protege você, sua família e toda a comunidade.",
            "hashtags": ["#SãoLourençoDoSul", "#Vacinação", "#Saúde", "#Prevenção", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Vacina em dia em São Lourenço.",
            "desenvolvimento_45s": "São Lourenço do Sul realiza nesta quarta-feira, dia 17, uma ação de atualização das carteiras de vacinação. A equipe atende em frente à Farmácia Municipal, no Centro, das 9h às 11h e das 13h às 16h. A orientação é levar a carteira de vacinação para conferir se está tudo em dia. Manter as vacinas atualizadas é uma das formas mais simples de proteger a saúde individual e de toda a comunidade.",
            "fechamento_8s": "Atendimento nesta quarta, no Centro.",
            "cta_5s": "Confira no SulTV.",
            "trilha_sugerida": "instrumental leve e positivo"
        },
        "tag_thumbnail": "Vacinação em São Lourenço",
        "briefing_visual": {
            "descricao_pt": "Caderneta de vacinação e frascos de vacina sobre mesa de posto de saúde, foco nos objetos, sem rostos",
            "query_en": ["vaccination card vaccine vials", "immunization record table", "vaccine bottles clinic"],
            "evitar": ["rostos identificáveis", "marcas de fabricantes", "texto legível", "logos"],
            "prompt_ia": "A vaccination record booklet and vaccine vials on a clinic table, soft natural light, close-up on the objects, no people, no readable brand text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de saúde com data (hoje), local e horário em cidade-núcleo; utilidade imediata, sem teor médico-prescritivo"
    },

    # 9. São Lourenço do Sul — balanço de manutenção urbana — REBAIXAR
    "c9a35d0e78e79a53b784d184da63a4870f32ba03": _skip(
        "REBAIXAR",
        "Balanço genérico de ações de manutenção (01 a 13/06) sem fato único ancorável — vira nota interna; pode render pauta quando houver entrega específica"
    ),

    # 10. Chuvisca — edital de penalidade — BLOQUEAR
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR",
        "Edital procedural de publicação de penalidade — sem corpo de texto nem valor editorial; regra de bloqueio de editais"
    ),

    # 11. Chuvisca — edital perímetro urbano — BLOQUEAR
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR",
        "Edital procedural (abertura de prazo para requerimentos) — regra de bloqueio de editais"
    ),

    # 12. Sentinela do Sul — aviso de audiência pública — BLOQUEAR
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR",
        "Título genérico '📢 AVISO DE AUDIÊNCIA PÚBLICA' sem corpo de texto — sem fato ancorável"
    ),

    # 13. Sentinela do Sul — emissão de notas fiscais — BLOQUEAR
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR",
        "Comunicado procedural sobre emissor nacional de NFS-e — aviso administrativo, não é matéria"
    ),

    # 14. Barra do Ribeiro — cabeçalho de secretaria de Turismo — BLOQUEAR
    "2ca9c6c05b652779fe1185d698a6d67e649d2e53": _skip(
        "BLOQUEAR",
        "Título é cabeçalho de secretaria concatenado a fragmento de menu — raspagem de seção, não é matéria"
    ),

    # 15. Barra do Ribeiro — cabeçalho admin/contracheques — BLOQUEAR
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": _skip(
        "BLOQUEAR",
        "Título é cabeçalho de secretaria concatenado com aviso interno a servidores — comunicado administrativo, não é matéria"
    ),

    # 16. Pelotas/Barra do Ribeiro — CMPC R$ 27 bi Projeto Natureza — PUBLICAR materia_longa
    "0d5b5546c2181520d61a65fde680dafeb3d853e6": {
        "titulo_sultv": "Governo do Estado reforça regularidade do licenciamento do projeto de R$ 27 bilhões da CMPC em Barra do Ribeiro",
        "chamada_faixa": "Estado reforça licenciamento do projeto de R$ 27 bi",
        "subtitulo": "Investimento da CMPC em Barra do Ribeiro é apontado como um dos maiores da história do RS e mira nova fábrica de celulose.",
        "lead": "O Governo do Rio Grande do Sul reforçou a regularidade do processo de licenciamento ambiental do Projeto Natureza, investimento de R$ 27 bilhões da CMPC previsto para Barra do Ribeiro, na região da Costa Doce. O empreendimento, voltado à produção de celulose, é apontado como um dos maiores aportes privados da história do estado.",
        "ganchos_3": [
            "Projeto Natureza prevê R$ 27 bilhões em Barra do Ribeiro",
            "Governo do Estado reforça regularidade do licenciamento ambiental",
            "Empreendimento de celulose é um dos maiores aportes privados do RS"
        ],
        "angulo_editorial": "Economia e desenvolvimento regional — aporte bilionário em cidade da Costa Doce, com impacto direto em empregos e cadeia produtiva; foco no investimento e na regularidade do licenciamento, atribuído apenas ao Governo do Estado e à empresa, sem viés partidário-eleitoral.",
        "fontes_complementares_sugeridas": ["Governo do Estado do RS", "CMPC", "Fepam", "Prefeitura de Barra do Ribeiro"],
        "lead_materia_longa": "O Governo do Rio Grande do Sul reforçou a regularidade do processo de licenciamento ambiental do Projeto Natureza, investimento de R$ 27 bilhões da CMPC previsto para Barra do Ribeiro, na região da Costa Doce.",
        "post_instagram": {
            "caption": "Um dos maiores investimentos privados da história do Rio Grande do Sul pode sair em Barra do Ribeiro: o Projeto Natureza, da CMPC, prevê R$ 27 bilhões na produção de celulose. O Governo do Estado reforçou a regularidade do processo de licenciamento ambiental do empreendimento. Um aporte desse porte movimenta empregos e a economia de toda a Costa Doce.",
            "hashtags": ["#BarraDoRibeiro", "#Investimento", "#Economia", "#Celulose", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "R$ 27 bilhões na Costa Doce.",
            "desenvolvimento_45s": "O Governo do Rio Grande do Sul reforçou a regularidade do processo de licenciamento ambiental do Projeto Natureza, investimento de 27 bilhões de reais da CMPC previsto para Barra do Ribeiro. O empreendimento, voltado à produção de celulose, é apontado como um dos maiores aportes privados da história do estado. Um projeto desse porte tem potencial de gerar milhares de empregos e movimentar a cadeia produtiva de toda a região da Costa Doce, da construção à operação da futura fábrica.",
            "fechamento_8s": "Investimento histórico em discussão.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental institucional"
        },
        "tag_thumbnail": "Investimento em Barra do Ribeiro",
        "briefing_visual": {
            "descricao_pt": "Plantação de eucalipto em fileiras no Sul do Brasil com vista ampla ao amanhecer, sem pessoas",
            "query_en": ["eucalyptus plantation rows brazil", "pulp wood forestry aerial", "eucalyptus forest sunrise"],
            "evitar": ["pessoas", "marcas", "texto", "logos"],
            "prompt_ia": "Wide view of orderly rows of eucalyptus plantation in southern Brazil at sunrise, soft golden light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Aporte econômico bilionário (R$ 27 bi) em cidade da Costa Doce, alto impacto regional em empregos; angulado no investimento e no licenciamento, atribuído a fontes institucionais, sem viés eleitoral"
    },

    # 17. Pelotas — concurso magistério (maio, procedural) — BLOQUEAR
    "0c78bd0cc00e7d0302fc635b3fdbfbd510252753": _skip(
        "BLOQUEAR",
        "Aviso procedural de concurso com prazo de maio — defasado e sem valor editorial atual"
    ),

    # 18. Guaíba — Operação Inverno da Defesa Civil — PUBLICAR (nota_curta)
    "3b348ce4a42ffbd249fd98d4c5ed494b381ac4dc": {
        "titulo_sultv": "Defesa Civil de Guaíba ativa Operação Inverno para proteger pessoas em vulnerabilidade",
        "chamada_faixa": "Guaíba ativa Operação Inverno",
        "subtitulo": "Ação é acionada quando a sensação térmica fica abaixo de 7°C; demandas podem ser comunicadas pelo telefone 199.",
        "lead": "A Defesa Civil de Guaíba intensificou o monitoramento e as ações de acolhimento a pessoas em situação de vulnerabilidade com a chegada do frio, por meio da Operação Inverno. A ação é ativada quando a sensação térmica fica abaixo de 7°C e prevê abordagens sociais, distribuição de cobertores e encaminhamento para abrigo provisório.",
        "ganchos_3": [
            "Operação Inverno é ativada com sensação térmica abaixo de 7°C",
            "Defesa Civil distribui cobertores e oferece abrigo provisório",
            "Demandas podem ser comunicadas pelo telefone 199, 24 horas"
        ],
        "angulo_editorial": "Serviço e proteção social no início do inverno — utilidade imediata com canal de contato (199); pauta de cidadania e solidariedade, fonte primária Defesa Civil.",
        "fontes_complementares_sugeridas": ["Defesa Civil de Guaíba", "Prefeitura de Guaíba", "Assistência Social de Guaíba"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Com a chegada do frio, a Defesa Civil de Guaíba ativou a Operação Inverno para proteger pessoas em situação de vulnerabilidade. Quando a sensação térmica fica abaixo de 7°C, equipes realizam abordagens sociais, distribuem cobertores e encaminham para abrigo provisório. Viu alguém em situação de rua passando frio? Comunique pelo telefone 199, disponível 24 horas. Cuidar das pessoas é responsabilidade de todos.",
            "hashtags": ["#Guaíba", "#OperaçãoInverno", "#DefesaCivil", "#Solidariedade", "#RS", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Operação Inverno em Guaíba.",
            "desenvolvimento_45s": "A Defesa Civil de Guaíba ativou a Operação Inverno para proteger pessoas em situação de vulnerabilidade durante os dias mais frios. A ação é acionada quando a sensação térmica fica abaixo de 7°C e prevê abordagens sociais, avaliação das condições de saúde, distribuição de cobertores e encaminhamento para abrigo provisório. Quem identificar alguém em situação de rua passando frio pode comunicar pelo telefone 199, disponível 24 horas por dia.",
            "fechamento_8s": "Frio pede solidariedade.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental acolhedor"
        },
        "tag_thumbnail": "Operação Inverno Guaíba",
        "briefing_visual": {
            "descricao_pt": "Cobertores dobrados empilhados prontos para distribuição em noite fria, ambiente urbano, sem rostos",
            "query_en": ["folded blankets donation stack", "winter blankets charity", "cold night city street"],
            "evitar": ["rostos identificáveis", "pessoas em situação de rua identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A neat stack of folded blankets ready for distribution on a cold night in an urban setting, warm light, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de proteção social com canal de contato (199) no início do inverno; fonte primária Defesa Civil, pauta de cidadania"
    },

    # 19. ALERS — audiência Pelotas concessões/privatizações — REBAIXAR
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "REBAIXAR",
        "Conteúdo agregado de manifestações parlamentares sobre privatizações — tangencia política partidária e carece de âncora concreta; vira nota interna"
    ),

    # 20. ALERS — Funcriança/Valores que Ficam — REBAIXAR
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR",
        "Pauta procedural de campanha de destinação de IR sem fato novo ancorável na cobertura; vira nota interna"
    ),

    # 21. RS — renegociação de dívidas rurais no Senado — PUBLICAR materia_longa
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "titulo_sultv": "Produtores do RS temem ficar sem crédito para a safra caso renegociação de dívidas não avance",
        "chamada_faixa": "Renegociação de dívidas preocupa o campo gaúcho",
        "subtitulo": "Setor teme perder acesso ao crédito rural para o próximo plantio caso a proposta de renegociação não seja aprovada.",
        "lead": "Produtores rurais do Rio Grande do Sul vivem a expectativa pela aprovação da renegociação de dívidas e temem as consequências caso a proposta não avance. O principal receio do setor é ficar sem acesso ao crédito rural para o financiamento da próxima safra, em regiões produtoras como a Costa Doce, onde o arroz e a soja sustentam a economia de dezenas de municípios.",
        "ganchos_3": [
            "Renegociação de dívidas rurais aguarda votação no Congresso",
            "Receio do campo é ficar sem crédito para a próxima safra",
            "Estiagens e enchentes agravaram o endividamento no RS"
        ],
        "angulo_editorial": "Agro e economia — endividamento rural é a pauta econômica mais sensível do campo gaúcho após estiagens e enchentes; foco no impacto para o produtor da Costa Doce (arroz e soja). Sem viés partidário: tramitação de interesse econômico, sem menção a veículos.",
        "fontes_complementares_sugeridas": ["Farsul", "Federarroz", "Congresso Nacional", "entidades de representação do setor"],
        "lead_materia_longa": "Produtores rurais do Rio Grande do Sul vivem a expectativa pela aprovação da renegociação de dívidas e temem ficar sem acesso ao crédito rural para a próxima safra caso a proposta não avance.",
        "post_instagram": {
            "caption": "A renegociação das dívidas rurais segue pendente e o campo gaúcho está em alerta: sem a aprovação, o receio é ficar sem crédito para plantar a próxima safra. Depois de sucessivas estiagens e das enchentes, o endividamento virou a maior preocupação do produtor do RS, em regiões como a Costa Doce, onde arroz e soja movimentam a economia.",
            "hashtags": ["#Agro", "#CréditoRural", "#RioGrandeDoSul", "#Safra", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Campo gaúcho em alerta.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul aguardam com apreensão a aprovação da renegociação de dívidas. O receio é que, sem a proposta, o setor fique sem acesso ao crédito rural para financiar a próxima safra. Depois de sucessivas quebras por estiagem e das enchentes, o endividamento se acumulou e a renegociação virou condição para muitos produtores seguirem plantando arroz e soja na região da Costa Doce. O calendário agrícola não espera, e as decisões sobre a próxima safra precisam ser tomadas nos próximos meses.",
            "fechamento_8s": "Setor cobra definição.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Dívidas rurais e crédito",
        "briefing_visual": {
            "descricao_pt": "Lavoura de soja madura no Rio Grande do Sul com céu carregado ao fundo, vista ampla, sem pessoas",
            "query_en": ["soybean field cloudy sky brazil", "mature soybean crop wide shot", "farm field storm clouds"],
            "evitar": ["pessoas", "marcas de máquinas", "texto", "logos"],
            "prompt_ia": "Wide shot of a mature soybean field in southern Brazil under heavy gray clouds, dramatic but realistic light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta econômica mais sensível do agro gaúcho com âncora regional clara (crédito para a safra de arroz e soja); redigida sem menção a veículos (regra 12)"
    },

    # 22. RS — vinhos vencidos apreendidos (fiscalização) — REBAIXAR
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": _skip(
        "REBAIXAR",
        "Fiscalização estadual relevante, mas com identificação negativa de estabelecimentos e sem âncora no núcleo Costa Doce; vira nota interna"
    ),

    # 23. RS — apreensão de 630 kg de alimentos (mesma força-tarefa) — REBAIXAR
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": _skip(
        "REBAIXAR",
        "Duplicata da mesma força-tarefa de fiscalização do item anterior — sem âncora no núcleo; vira nota interna"
    ),

    # 24. RS — Multifeira de Esteio (maio, metropolitana) — REBAIXAR
    "e6fff2725635f8da6e880c351f39276a44142f44": _skip(
        "REBAIXAR",
        "Evento na região metropolitana (Esteio) e com data já passada (maio) — fora do núcleo Costa Doce; vira nota interna"
    ),

    # 25. Sertão Santana — Termos de Fomento a entidades — REBAIXAR
    "ebf159c5f7b5bea63d6c3d9d891f7e9f650a352b": _skip(
        "REBAIXAR",
        "Entrega de termos de fomento a entidades — pauta administrativa de baixo gancho; vira nota interna"
    ),

    # 26. Amaral Ferrador — visita SINDITABACO ao gabinete — REBAIXAR
    "63a6ac2ca1d31f81d6777c345692d7019b5f80f9": _skip(
        "REBAIXAR",
        "Visita institucional de articulação sem entregável concreto; vira nota interna"
    ),

    # 27. Amaral Ferrador — audiência com diretor do DAER — REBAIXAR
    "d495dcc8e3b569216b364db3fb2ef094cb5cddbd": _skip(
        "REBAIXAR",
        "Audiência sobre estradas sem definição/entregável anunciado; acompanhar e publicar quando houver obra ou compromisso concreto"
    ),

    # 28. Encruzilhada do Sul — esclarecimento sobre energia — REBAIXAR
    "dac571bf9bc552b21bf2f135a68956473f78f9de": _skip(
        "REBAIXAR",
        "Esclarecimento administrativo sobre comunicado de desligamento de energia — aviso de utilidade pontual; vira nota interna"
    ),

    # 29. Encruzilhada do Sul — Nota Fiscal Premiada — REBAIXAR
    "93ead45af45f7460451b53107befb4234889579b": _skip(
        "REBAIXAR",
        "Campanha promocional municipal de baixo gancho editorial; vira nota interna"
    ),

    # 30. Sertão Santana — agenda em Porto Alegre (CAFF) — REBAIXAR
    "2e2bdcdbb04de728c4d45a48821e689471d8490a": _skip(
        "REBAIXAR",
        "Agenda administrativa sem entregável concreto; formato menor, vira nota interna"
    ),

    # 31. Canguçu — conscientização violência pessoa idosa — REBAIXAR
    "fce3119cfcb33ce7ea0f4b2f61a2bcadbc3f4fa5": _skip(
        "REBAIXAR",
        "Pauta de data alusiva sem fato/ação concreta ancorável; vira nota interna"
    ),

    # 32. Santa Maria — UFSM vagas complementares — REBAIXAR
    "bb8a2cf41511dff678bcb1a1db0dc4712561decc": _skip(
        "REBAIXAR",
        "Serviço da UFSM relevante, mas fora do núcleo Costa Doce; vira nota interna"
    ),

    # 33. Santa Maria — UFSM Mostra Cinema e DH — REBAIXAR
    "350fa1ef49d2d04812deb7be9018576613611ef1": _skip(
        "REBAIXAR",
        "Evento cultural distante do núcleo de cobertura; vira nota interna"
    ),

    # 34. Rio Grande — caminhão caçamba agricultura familiar — REBAIXAR
    "600873529f4ddf3f0d4311f0f87ae85744f2326c": _skip(
        "REBAIXAR",
        "Entrega de equipamento positiva mas de gancho menor e fora do núcleo; vira nota interna"
    ),

    # 35. Dom Feliciano — oficina de costura no CRAS — REBAIXAR
    "0b7ee95d1ff2a2bf9796a4a0274d482a7917de18": _skip(
        "REBAIXAR",
        "Atividade pontual de assistência social, gancho menor; vira nota interna"
    ),

    # 36. Dom Feliciano — convite Arraiá da Lorenz — REBAIXAR
    "6588128a57e7ccb1a7613032c4adb75f6ca1a3e7": _skip(
        "REBAIXAR",
        "Divulgação de evento privado/comunitário; vira nota interna/agenda"
    ),

    # 37. Bagé — texto opinativo sobre IA no Direito — REBAIXAR
    "0c808e564b7055a38c3dbf400337a0d63db5ee62": _skip(
        "REBAIXAR",
        "Post opinativo/institucional sem fato local concreto; vira nota interna"
    ),

    # 38. Canguçu — Prefeito na Vila no Bairro Fonseca — REBAIXAR
    "7f337e2b5f2332393d8699de617c37f8150a6138": _skip(
        "REBAIXAR",
        "Agenda de itinerância do governo municipal, gancho menor e fora do núcleo; vira nota interna"
    ),

    # 39. Venâncio Aires — entidades cobram fumageiras — REBAIXAR
    "81a7382b22b3b8855eb01977b6fb99336abf30d7": _skip(
        "REBAIXAR",
        "Pauta de cadeia do tabaco relevante mas fora do núcleo Costa Doce; vira nota interna"
    ),

    # 40. Venâncio Aires — roda de conversa pessoa idosa — REBAIXAR
    "74bf9c2f058c3fd756123777df14d6cf63d9c903": _skip(
        "REBAIXAR",
        "Atividade de data alusiva fora do núcleo; vira nota interna"
    ),

    # 41. Bento Gonçalves — exposição cultural Vale dos Vinhedos — REBAIXAR
    "62ff80870c2148aae022d7cb5d05837b77ed5867": _skip(
        "REBAIXAR",
        "Evento cultural na Serra, fora do núcleo Costa Doce; vira nota interna/agenda"
    ),

    # 42. Bento Gonçalves — vacinação gripe — REBAIXAR
    "16391dcdb93208983d47d03efa085d01964669a6": _skip(
        "REBAIXAR",
        "Serviço de saúde positivo, mas fora do núcleo de cobertura; vira nota interna"
    ),
}


MATERIAS = {
    "b19d54aa307276a3d94f4535e449d9aa14bf943a": """### Título ###
Festa de São João de Camaquã amplia programação com shows na Prainha no sábado

### Artigo ###
A Festa de São João de Camaquã terá programação ampliada neste sábado (20), no Complexo Poliesportivo Ruy de Castro Netto, na Prainha. A celebração, uma das mais tradicionais do calendário junino do município, foi reforçada para oferecer um dia inteiro de cultura, tradição e diversão para toda a família. A abertura está marcada para as 14h30, com a apresentação de invernadas e de grupos de folclore da região, valorizando a cultura gaúcha e o trabalho de formação de jovens dançarinos. Ao longo da tarde, o público acompanha uma sequência de atrações musicais que misturam tradição e entretenimento, em um ambiente preparado para receber moradores de Camaquã e de cidades vizinhas. O ponto alto da noite acontece às 20h, com a cerimônia oficial, a bênção do pároco e o tradicional acendimento da fogueira, símbolo maior das festas de São João. As festas juninas têm forte significado cultural e religioso no interior do Rio Grande do Sul, reunindo comunidades em torno de comidas típicas, música e das tradições passadas de geração em geração. Para os municípios, esses eventos também movimentam a economia local, com a participação de expositores, food trucks e do comércio, além de fortalecerem o turismo regional na época mais fria do ano. A entrada é uma oportunidade de lazer acessível em família, e a recomendação é que o público se programe com antecedência, levando agasalho para curtir a noite junto à fogueira. A programação completa e eventuais atualizações de horário podem ser conferidas nos canais oficiais da Prefeitura de Camaquã.

### Legenda sugerida ###
Festa de São João de Camaquã tem programação ampliada neste sábado (20), na Prainha, com shows e acendimento da fogueira às 20h.

### Palavras-chave ###
Camaquã, Festa de São João, festas juninas, Prainha, cultura, tradição gaúcha, Costa Doce, evento
""",

    "85e1e49c224d76ffee83f0d7ac8e9cbdaeeedfa6": """### Título ###
Tapes garante R$ 6,9 milhões e viabiliza 34 moradias para famílias em áreas de risco

### Artigo ###
O município de Tapes garantiu a manutenção de R$ 6,9 milhões do Fundo Nacional de Habitação de Interesse Social (FNHIS), recursos que vão viabilizar 34 moradias para famílias em situação de vulnerabilidade e que vivem em áreas de risco. O resultado veio após um intenso trabalho técnico e de articulação da defesa civil municipal junto à Caixa Econômica Federal e ao Ministério das Cidades. Inicialmente, o programa previa a construção de 46 casas em um loteamento do município. Porém, estudos técnicos apontaram que a área exigiria altos investimentos em infraestrutura, o que tornava o projeto inviável dentro do orçamento disponível. Diante do risco de perder o recurso, a administração buscou uma alternativa junto aos órgãos federais. A solução veio com a publicação de uma nova portaria que passou a permitir a aquisição de imóveis já existentes, em vez de exigir exclusivamente a construção de unidades novas. Com isso, o município conseguiu preservar o valor e redirecioná-lo para garantir o atendimento às famílias. A política de habitação de interesse social tem papel central na proteção de populações vulneráveis, especialmente em regiões que enfrentaram eventos climáticos extremos nos últimos anos. Tirar famílias de áreas de risco significa não apenas oferecer moradia digna, mas também reduzir a exposição a alagamentos, deslizamentos e outras situações de emergência. Para uma cidade da Costa Doce como Tapes, banhada pela Lagoa dos Patos, esse tipo de ação ganha relevância adicional diante da preocupação com a segurança das comunidades ribeirinhas. Os próximos passos envolvem a definição dos imóveis e dos critérios de seleção das famílias beneficiadas, etapas que serão conduzidas pela administração municipal e divulgadas em seus canais oficiais.

### Legenda sugerida ###
Tapes assegura R$ 6,9 milhões do FNHIS e viabiliza 34 moradias para famílias em situação de vulnerabilidade e áreas de risco.

### Palavras-chave ###
Tapes, habitação, moradia, FNHIS, áreas de risco, defesa civil, Costa Doce, habitação de interesse social
""",

    "0d7e9665c5b4929e603f7055539c2c047848018f": """### Título ###
Tapes sedia encontro estadual do escotismo e celebra reabertura de grupo escoteiro

### Artigo ###
Tapes foi sede, no último sábado (13), de um importante momento para o Movimento Escoteiro gaúcho. O Camping Municipal Antônio Alfonsin Simchen recebeu o ECHEMAR 2026 – Encontro de Chefes da Modalidade do Mar, que reuniu mais de 40 chefes e dirigentes escoteiros de diferentes regiões do Rio Grande do Sul. Durante o encontro, foram debatidas ações, planejamentos e perspectivas para fortalecer as atividades da Modalidade do Mar no próximo período, promovendo a troca de experiências entre lideranças e reforçando o compromisso com a formação de crianças, adolescentes e jovens por meio dos valores do escotismo. O evento também marcou a reabertura do Grupo Escoteiro do Mar Araxanes, um momento celebrado pela comunidade local. A Modalidade do Mar é uma das vertentes do escotismo voltada às atividades náuticas, que combinam o aprendizado de técnicas de navegação, segurança aquática e respeito ao meio ambiente com a formação de caráter, liderança e cidadania que caracteriza o movimento. Para Tapes, município que vive às margens da Lagoa dos Patos, a presença de um grupo escoteiro do mar tem significado especial: aproxima crianças e jovens da vocação náutica da cidade e oferece uma alternativa educativa e saudável de ocupação do tempo. O escotismo é reconhecido mundialmente como uma das maiores organizações de educação não formal de jovens, com atuação centrada em valores como solidariedade, disciplina, trabalho em equipe e contato com a natureza. A realização de um encontro estadual em Tapes coloca o município em destaque no cenário escoteiro do Rio Grande do Sul e valoriza o trabalho voluntário de chefes e dirigentes que dedicam seu tempo à formação das novas gerações.

### Legenda sugerida ###
Camping Municipal de Tapes recebeu mais de 40 chefes escoteiros do RS no ECHEMAR 2026 e celebrou a reabertura do Grupo Escoteiro do Mar Araxanes.

### Palavras-chave ###
Tapes, escotismo, ECHEMAR, Grupo Escoteiro do Mar Araxanes, Modalidade do Mar, juventude, Lagoa dos Patos, Costa Doce
""",

    "612ffb08a1ba713e460e43a35aebc9d85358c4c8": """### Título ###
Unidade móvel leva atendimento médico ao Assentamento Caturritas em Arambaré dia 25

### Artigo ###
A Unidade Móvel de Saúde da Prefeitura de Arambaré estará no Assentamento Caturritas no dia 25 de junho, levando atendimento médico aos moradores da comunidade rural. A ação integra o programa Saúde na Estrada, voltado a aproximar o atendimento das localidades mais distantes do centro do município, na região da Costa Doce. Para o atendimento, a orientação é que os moradores levem o Cartão do SUS, documento que permite o registro e o acompanhamento do histórico de saúde de cada pessoa na rede pública. A interiorização do atendimento é uma estratégia importante para garantir o direito à saúde em comunidades rurais, onde o deslocamento até a sede do município pode representar uma barreira de acesso, especialmente para idosos, gestantes e pessoas com mobilidade reduzida. Levar a equipe médica até o assentamento reduz custos e tempo de viagem para as famílias e amplia a cobertura da atenção básica. Programas como o Saúde na Estrada costumam oferecer consultas médicas, orientações de prevenção e encaminhamentos quando necessário, funcionando como uma porta de entrada do sistema de saúde nas localidades atendidas. Iniciativas desse tipo também ajudam a identificar precocemente situações que exigem acompanhamento, contribuindo para a prevenção de agravos. A Prefeitura de Arambaré informa que segue trabalhando para ampliar o acesso à saúde e levar atendimento cada vez mais perto da população. Moradores do Assentamento Caturritas e de outras comunidades podem buscar informações sobre o calendário das próximas ações nos canais oficiais do município e na Secretaria Municipal de Saúde.

### Legenda sugerida ###
Unidade Móvel de Saúde de Arambaré atende no Assentamento Caturritas no dia 25 de junho; leve o Cartão do SUS.

### Palavras-chave ###
Arambaré, Saúde na Estrada, unidade móvel de saúde, Assentamento Caturritas, SUS, saúde rural, Costa Doce, atenção básica
""",

    "f6344ccfbeebeb426982842a44881910459162a4": """### Título ###
Cristal pede aumento do efetivo da Brigada Militar em reunião com o 30º BPM

### Artigo ###
A Administração Municipal de Cristal recebeu o comando do 30º Batalhão de Polícia Militar para uma reunião voltada ao fortalecimento da segurança pública no município. Entre as principais demandas apresentadas, a administração solicitou o aumento do efetivo da Brigada Militar na cidade, com o objetivo de ampliar a presença policial e dar mais sensação de segurança à população cristalense. O encontro também contou com a presença de representantes do poder legislativo municipal, reforçando o caráter institucional da pauta. A ampliação do efetivo policial é uma demanda recorrente de municípios de pequeno e médio porte do interior gaúcho, onde a presença ostensiva da Brigada Militar é fundamental para a prevenção de crimes e para a resposta rápida a ocorrências. O policiamento adequado depende da articulação entre o poder público municipal e as forças de segurança do estado, já que o efetivo é definido conforme critérios como população, área territorial e índices de criminalidade. Reuniões como essa servem para apresentar a realidade local ao comando do batalhão e buscar soluções conjuntas, que podem incluir o reforço de patrulhamento, ações integradas e o uso de tecnologia para o monitoramento. A segurança pública figura entre as principais preocupações da população em todo o país, e a aproximação entre prefeitura, câmara de vereadores e Brigada Militar é apontada como um caminho para qualificar o atendimento à comunidade. Os encaminhamentos da reunião devem ser acompanhados nos próximos meses, com a expectativa de que o diálogo resulte em melhorias concretas no policiamento de Cristal.

### Legenda sugerida ###
Administração de Cristal pede aumento do efetivo da Brigada Militar em reunião com o comando do 30º BPM.

### Palavras-chave ###
Cristal, segurança pública, Brigada Militar, 30º BPM, efetivo policial, policiamento, Costa Doce, interior gaúcho
""",

    "30a1e2c79d28bac9d592e51269a0709cf8f404a6": """### Título ###
São Lourenço do Sul faz atualização da carteira de vacinação nesta quarta no Centro

### Artigo ###
São Lourenço do Sul realiza nesta quarta-feira (17) uma ação de atualização das carteiras de vacinação da comunidade. A equipe de vacinação atende em frente à Farmácia Municipal, na Rua Coronel Alfredo Born, nº 288, no Centro Comercial Dona Maria, sala 3, em dois turnos: das 9h às 11h pela manhã e das 13h às 16h à tarde. A orientação é que cada pessoa leve a sua carteira de vacinação para que a equipe possa conferir quais doses estão em dia e quais precisam ser atualizadas. A iniciativa busca facilitar o acesso da população à imunização, aproveitando um ponto de grande circulação no Centro da cidade para aproximar o serviço dos moradores. Manter a carteira de vacinação atualizada é uma das medidas mais simples e eficazes de proteção da saúde, tanto individual quanto coletiva. A vacinação em dia reduz o risco de doenças que já foram controladas no país e que podem voltar a circular quando a cobertura vacinal cai. A recomendação das equipes de saúde vale para todas as faixas etárias, já que o calendário de imunização inclui vacinas para crianças, adolescentes, adultos e idosos. Ações como essa, realizadas fora das unidades de saúde tradicionais, ajudam a alcançar pessoas que muitas vezes deixam de comparecer aos postos por falta de tempo ou por dificuldade de deslocamento. A Prefeitura de São Lourenço do Sul reforça que cuidar da saúde é um gesto que protege não apenas cada indivíduo, mas também a família e toda a comunidade. Informações sobre o calendário de vacinação e as próximas ações podem ser obtidas na Secretaria Municipal de Saúde e nos canais oficiais do município.

### Legenda sugerida ###
São Lourenço do Sul atualiza carteiras de vacinação nesta quarta (17), em frente à Farmácia Municipal, das 9h às 11h e das 13h às 16h.

### Palavras-chave ###
São Lourenço do Sul, vacinação, carteira de vacinação, saúde, prevenção, imunização, Costa Doce, calendário vacinal
""",

    "0d5b5546c2181520d61a65fde680dafeb3d853e6": """### Título ###
Governo do Estado reforça regularidade do licenciamento do projeto de R$ 27 bilhões da CMPC em Barra do Ribeiro

### Artigo ###
O Governo do Rio Grande do Sul reforçou a regularidade do processo de licenciamento ambiental do Projeto Natureza, investimento de R$ 27 bilhões da CMPC previsto para Barra do Ribeiro, na região da Costa Doce. O empreendimento, voltado à produção de celulose, é apontado como um dos maiores aportes privados da história do estado e está entre os projetos de maior impacto econômico em discussão no Rio Grande do Sul. Investimentos dessa magnitude costumam mobilizar uma extensa cadeia produtiva, que vai da construção civil à logística, passando pela demanda por mão de obra qualificada e por serviços nos municípios da região. A expectativa em torno de projetos de celulose envolve a geração de empregos diretos e indiretos, o aquecimento do comércio local e o aumento da arrecadação, fatores que podem transformar a economia de cidades de pequeno e médio porte como Barra do Ribeiro. Ao mesmo tempo, empreendimentos desse porte exigem processos rigorosos de licenciamento ambiental, etapa em que são avaliados os impactos sobre os recursos hídricos, a vegetação, a fauna e as comunidades do entorno, além das medidas de mitigação e compensação. A manifestação do Governo do Estado sobre a regularidade do processo busca dar previsibilidade ao licenciamento, conduzido pelos órgãos ambientais competentes conforme a legislação. Para a região da Costa Doce, a discussão sobre o Projeto Natureza concentra atenção justamente por combinar a perspectiva de desenvolvimento econômico com a necessidade de garantir a sustentabilidade ambiental, equilíbrio que tende a marcar o debate nas próximas etapas. O andamento do licenciamento e os próximos passos do empreendimento devem seguir entre os principais temas econômicos acompanhados no estado.

### Legenda sugerida ###
Governo do Estado reforça a regularidade do licenciamento ambiental do Projeto Natureza, da CMPC, investimento de R$ 27 bilhões em Barra do Ribeiro.

### Palavras-chave ###
Barra do Ribeiro, CMPC, Projeto Natureza, investimento, celulose, licenciamento ambiental, economia, Costa Doce, Rio Grande do Sul
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS temem ficar sem crédito para a safra caso renegociação de dívidas não avance

### Artigo ###
Produtores rurais do Rio Grande do Sul vivem a expectativa pela aprovação da renegociação de dívidas e temem as consequências caso a proposta não seja aprovada. O principal receio do setor é ficar sem acesso ao crédito rural para o financiamento da próxima safra — um risco que atinge em cheio regiões produtoras como a Costa Doce, onde o arroz e a soja sustentam a economia de dezenas de municípios. O endividamento do campo gaúcho se agravou nos últimos anos com a sequência de eventos climáticos extremos. Estiagens severas quebraram safras consecutivas e, na sequência, as enchentes históricas atingiram amplas áreas do estado, destruindo lavouras, máquinas e estruturas. Sem conseguir honrar os compromissos das safras frustradas, muitos produtores acumularam parcelas em atraso e perderam a capacidade de tomar novos financiamentos, entrando em um ciclo que compromete o custeio do próximo plantio. A renegociação em discussão é vista pelas entidades de representação do setor como condição para restabelecer a capacidade de pagamento dos produtores e mantê-los na atividade. Enquanto a votação não se concretiza, cresce a apreensão no campo, já que o calendário agrícola não espera: as decisões sobre a compra de insumos e o financiamento da safra de verão precisam ser tomadas nos próximos meses. Lideranças do agronegócio gaúcho têm intensificado a interlocução com parlamentares para dar celeridade à tramitação. O endividamento rural permanece como uma das pautas econômicas mais sensíveis para o estado, com efeitos diretos sobre a renda no campo, a geração de empregos e a economia dos municípios que dependem da agricultura. Os desdobramentos da renegociação serão decisivos para o planejamento da safra 2026/2027 no Rio Grande do Sul.

### Legenda sugerida ###
Campo gaúcho teme ficar sem crédito para a próxima safra caso a renegociação de dívidas rurais não avance.

### Palavras-chave ###
renegociação de dívidas, crédito rural, Rio Grande do Sul, agro, safra, arroz, soja, endividamento rural, Costa Doce
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
            angul = _skip("BLOQUEAR", "Sem angulação configurada — descartado pelo guardrail")
            angul["titulo_sultv"] = item.get("titulo", "")[:100]
        else:
            angul = PAUTA_ANGULADA[h]

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
    print("[angular] decisões:", Counter(p["decisao_final"] for p in pauta))
    print("[angular] PUBLICAR:", pub_count)

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
