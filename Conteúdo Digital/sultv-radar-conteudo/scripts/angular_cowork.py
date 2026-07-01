#!/usr/bin/env python3
"""
angular_cowork.py — angulação editorial + redação no fluxo cowork-faz-tudo.

Pauta de 2026-06-04 — angulação editorial Claude na sessão cowork.
Lê state/aprovadas_<date>.json, gera state/pauta_<date>.json com angulação
completa + decisao_final (PUBLICAR/REBAIXAR/BLOQUEAR/ALERTA_HUMANO),
e escreve state/materias_<date>/<id_hash>.md para cada item PUBLICAR + materia_longa.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

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
    # 1. Pelotas — 14º caso de dengue em 2026 — PUBLICAR materia_longa
    "293d30ecab37491f415233c4ce53462d32f3b51e": {
        "titulo_sultv": "Pelotas confirma 14º caso de dengue em 2026 e reforça alerta contra o mosquito",
        "chamada_faixa": "Pelotas confirma 14º caso de dengue em 2026",
        "subtitulo": "Paciente de 18 anos contraiu a doença no próprio município, segundo a prefeitura; vigilância reforça orientações de prevenção.",
        "lead": "A Prefeitura de Pelotas confirmou nesta quarta-feira (3) o 14º caso de dengue registrado no município em 2026. O paciente é um jovem de 18 anos que contraiu a doença dentro do próprio município, o que reforça o alerta para a eliminação de focos do mosquito transmissor na Costa Doce ampliada.",
        "ganchos_3": [
            "14º caso de dengue confirmado em Pelotas em 2026",
            "Jovem de 18 anos contraiu a doença no próprio município",
            "Vigilância reforça orientações de prevenção contra o Aedes aegypti"
        ],
        "angulo_editorial": "Saúde pública de utilidade imediata em Pelotas (Costa Doce ampliada) — caso autóctone indica circulação local do vírus; pauta de serviço e prevenção, sem identificação do paciente e sem teor médico-prescritivo.",
        "fontes_complementares_sugeridas": ["Prefeitura de Pelotas", "Vigilância em Saúde de Pelotas", "Secretaria Estadual da Saúde"],
        "lead_materia_longa": "A Prefeitura de Pelotas confirmou nesta quarta-feira (3) o 14º caso de dengue registrado no município em 2026, em um jovem de 18 anos que contraiu a doença dentro do próprio município.",
        "post_instagram": {
            "caption": "Pelotas confirmou o 14º caso de dengue de 2026. O paciente, de 18 anos, contraiu a doença no próprio município — sinal de que o mosquito está circulando por aqui. Dez minutos por semana para eliminar água parada fazem a diferença. Cuide do seu pátio e ajude a proteger a cidade.",
            "hashtags": ["#Pelotas", "#Dengue", "#SaúdePública", "#Prevenção", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Dengue avança em Pelotas.",
            "desenvolvimento_45s": "A Prefeitura de Pelotas confirmou o 14º caso de dengue registrado no município em 2026. O paciente é um jovem de 18 anos que contraiu a doença dentro do próprio município, o que indica circulação local do mosquito transmissor. A orientação da vigilância é eliminar qualquer ponto de água parada em casa, no pátio e no trabalho, além de procurar atendimento ao sentir febre alta, dores no corpo e manchas na pele.",
            "fechamento_8s": "Caso autóctone reforça o alerta na cidade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Dengue em Pelotas",
        "briefing_visual": {
            "descricao_pt": "Agente de saúde inspecionando recipientes com água parada em pátio residencial no Sul do Brasil, sem rosto identificável, luz do dia",
            "query_en": ["mosquito breeding site inspection", "standing water container backyard", "dengue prevention health agent"],
            "evitar": ["rosto identificável", "pacientes", "marcas", "texto", "logos"],
            "prompt_ia": "Health worker inspecting containers with standing water in a residential backyard in southern Brazil, face not visible, daylight, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Saúde pública com fato concreto e número oficial em Pelotas — caso autóctone, alto interesse de serviço; sem identificação de paciente nem conteúdo médico-prescritivo"
    },

    # 2. São Lourenço do Sul — furto de 47 cabeças de gado — PUBLICAR materia_longa
    "a50e1c3a11166004b98df86395d6db399200e9d4": {
        "titulo_sultv": "Operação investiga furto de 47 cabeças de gado em São Lourenço do Sul",
        "chamada_faixa": "Furto de 47 cabeças de gado é investigado",
        "subtitulo": "DECRAB de Camaquã cumpriu mandado de busca e apreendeu arma, munições e celulares em nova fase da Operação Três Estâncias.",
        "lead": "A Delegacia Especializada em Crimes Rurais e Abigeato (DECRAB) de Camaquã deflagrou nova fase da Operação Três Estâncias para investigar o furto de 47 cabeças de gado em São Lourenço do Sul. Durante o cumprimento de mandado de busca, foram apreendidos uma arma, munições e celulares.",
        "ganchos_3": [
            "47 cabeças de gado furtadas em São Lourenço do Sul",
            "DECRAB Camaquã cumpre mandado e apreende arma e celulares",
            "Nova fase da Operação Três Estâncias contra o abigeato"
        ],
        "angulo_editorial": "Segurança no campo na Costa Doce — abigeato é uma das maiores preocupações do produtor rural da região; ação concreta da polícia com apreensões, sem vítima identificada. Pauta de crime rural com tom institucional.",
        "fontes_complementares_sugeridas": ["DECRAB Camaquã", "Polícia Civil RS", "Sindicato Rural de São Lourenço do Sul"],
        "lead_materia_longa": "A Delegacia Especializada em Crimes Rurais e Abigeato (DECRAB) de Camaquã deflagrou nova fase da Operação Três Estâncias para investigar o furto de 47 cabeças de gado em São Lourenço do Sul.",
        "post_instagram": {
            "caption": "A DECRAB de Camaquã cumpriu mandado de busca em nova fase da Operação Três Estâncias, que investiga o furto de 47 cabeças de gado em São Lourenço do Sul. Arma, munições e celulares foram apreendidos. O combate ao abigeato segue como prioridade na Costa Doce.",
            "hashtags": ["#SãoLourençoDoSul", "#Abigeato", "#Segurança", "#DECRAB", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Golpe no abigeato na Costa Doce.",
            "desenvolvimento_45s": "A DECRAB de Camaquã deflagrou nova fase da Operação Três Estâncias para investigar o furto de 47 cabeças de gado em São Lourenço do Sul. Durante o cumprimento de mandado de busca, os policiais apreenderam uma arma, munições e celulares. O abigeato é um dos crimes que mais preocupam os produtores rurais da região, e as investigações seguem para identificar todos os envolvidos.",
            "fechamento_8s": "Investigação segue em andamento.",
            "cta_5s": "Detalhes no SulTV.",
            "trilha_sugerida": "instrumental tenso leve"
        },
        "tag_thumbnail": "Furto de gado investigado",
        "briefing_visual": {
            "descricao_pt": "Gado bovino pastando em campo aberto no pampa gaúcho ao entardecer, cerca de arame ao fundo, sem pessoas",
            "query_en": ["cattle grazing pampas field", "beef cattle fence ranch sunset", "cows pasture southern brazil"],
            "evitar": ["pessoas", "marcas de gado legíveis", "texto", "logos"],
            "prompt_ia": "Cattle grazing on open pampas grassland in southern Brazil at golden hour, wire fence in the background, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Crime rural concreto com ação policial e apreensões em cidade-núcleo da cobertura (SLS/Camaquã) — alto interesse da audiência rural, sem vítima identificada"
    },

    # 3. Tapes/RS — Assembleia aprova medida custos veículos — REBAIXAR
    "61821ddf1888b0b04b2aa3bf6cad45234926390d": _skip(
        "REBAIXAR",
        "Fonte não especifica qual cobrança anual será reduzida nem o texto aprovado — redigir matéria sem esses dados traria risco de imprecisão; vira nota interna até confirmação"
    ),

    # 4. Sentinela do Sul — atração de investimentos e empregos — PUBLICAR materia_longa
    "f89077d77398dc238539b7a4ea1a8ceefafe72d3": {
        "titulo_sultv": "Sentinela do Sul intensifica ações para atrair investimentos e ampliar empregos",
        "chamada_faixa": "Sentinela do Sul quer atrair investimentos",
        "subtitulo": "Prefeitura aposta no desenvolvimento econômico para gerar novas oportunidades de trabalho no município da Costa Doce.",
        "lead": "A Prefeitura de Sentinela do Sul vem intensificando as ações voltadas ao desenvolvimento econômico e à geração de novas oportunidades de emprego para a população. O movimento, conduzido pelo prefeito Julio Carvalho, busca atrair investimentos e fortalecer a economia local no município da Costa Doce.",
        "ganchos_3": [
            "Prefeitura intensifica agenda de desenvolvimento econômico",
            "Foco em atrair investimentos privados ao município",
            "Meta é ampliar a geração de empregos na Costa Doce"
        ],
        "angulo_editorial": "Desenvolvimento econômico local em cidade da Costa Doce — pauta administrativa concreta e positiva, sem viés partidário; interessa a trabalhadores e empreendedores da região.",
        "fontes_complementares_sugeridas": ["Prefeitura de Sentinela do Sul", "ACI da região", "Sala do Empreendedor"],
        "lead_materia_longa": "A Prefeitura de Sentinela do Sul vem intensificando as ações voltadas ao desenvolvimento econômico e à geração de novas oportunidades de emprego para a população do município da Costa Doce.",
        "post_instagram": {
            "caption": "Sentinela do Sul está de olho no futuro: a prefeitura intensificou as ações para atrair investimentos e ampliar a geração de empregos no município. Desenvolvimento econômico que movimenta a Costa Doce.",
            "hashtags": ["#SentinelaDoSul", "#Empregos", "#Investimentos", "#DesenvolvimentoEconômico", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Empregos em Sentinela do Sul.",
            "desenvolvimento_45s": "A Prefeitura de Sentinela do Sul intensificou as ações voltadas ao desenvolvimento econômico e à geração de novas oportunidades de trabalho. O objetivo é atrair investimentos privados, apoiar quem quer empreender e fortalecer a economia local. Para municípios de pequeno porte da Costa Doce, cada nova empresa instalada representa renda circulando na cidade e mais oportunidades para que os jovens permaneçam na região.",
            "fechamento_8s": "Desenvolvimento que gera oportunidades.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental otimista"
        },
        "tag_thumbnail": "Investimentos em Sentinela",
        "briefing_visual": {
            "descricao_pt": "Vista de rua comercial movimentada de cidade pequena do interior do Sul do Brasil em dia claro, fachadas de comércio, sem rostos identificáveis",
            "query_en": ["small town main street commerce", "rural town business district brazil", "small business storefront street"],
            "evitar": ["rostos identificáveis", "marcas", "texto legível", "logos"],
            "prompt_ia": "Main commercial street of a small southern Brazilian town on a clear day, storefronts and light movement, no identifiable faces, no readable signs, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta administrativa concreta e positiva em cidade da Costa Doce — desenvolvimento econômico e empregos, sem viés partidário"
    },

    # 5. Arambaré — cursos de qualificação (16/abril) — REBAIXAR (pauta antiga)
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "REBAIXAR",
        "Notícia datada de 16/04/2026 raspada da página da prefeitura — inscrições podem estar encerradas; publicar como atual seria impreciso"
    ),

    # 6. Arambaré — reconstrução plataforma de pesca (19/janeiro) — REBAIXAR (pauta antiga)
    "7328151d0f689699ca147e00ec7ffb87008ee51e": _skip(
        "REBAIXAR",
        "Notícia datada de 19/01/2026 raspada da página da prefeitura — anúncio antigo, sem fato novo verificável nesta data"
    ),

    # 7. Chuvisca — edital de penalidade — BLOQUEAR
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR",
        "Edital procedural de publicação de penalidade — sem valor editorial, regra de bloqueio de editais"
    ),

    # 8. Chuvisca — edital perímetro urbano — BLOQUEAR
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR",
        "Edital procedural (abertura de prazo para requerimentos) — regra de bloqueio de editais; tema do perímetro urbano pode virar pauta própria quando houver fato"
    ),

    # 9. Barra do Ribeiro — contracheques servidores — BLOQUEAR
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": _skip(
        "BLOQUEAR",
        "Título é cabeçalho de secretaria concatenado com aviso interno a servidores — comunicado administrativo, não é matéria"
    ),

    # 10. Barra do Ribeiro — lei fogos com estampido — REBAIXAR
    "6d583901d0b2623e718e91c071da59f2069c1522": _skip(
        "REBAIXAR",
        "Divulgação de lei municipal de 2025 sem fato novo e sem corpo de texto na fonte — vira nota interna; pode render pauta de serviço em data oportuna (festas juninas/fim de ano)"
    ),

    # 11. Sentinela do Sul — aviso de audiência pública — BLOQUEAR
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR",
        "Título genérico '📢 AVISO DE AUDIÊNCIA PÚBLICA' sem corpo de texto — sem fato ancorável"
    ),

    # 12. Sentinela do Sul — emissão de notas fiscais — BLOQUEAR
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR",
        "Comunicado procedural sobre emissor nacional de NFS-e — aviso administrativo, não é matéria"
    ),

    # 13. Cristal — Rua Camaquã preparação para calçamento — REBAIXAR
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": _skip(
        "REBAIXAR",
        "Obra em estágio preparatório, fonte sem corpo de texto — conteúdo fino; acompanhar e publicar quando o calçamento iniciar/concluir"
    ),

    # 14. São Lourenço do Sul — corrida solidária OW — REBAIXAR
    "8ac0f5e54a1446f013927374779c0bd628febc5a": _skip(
        "REBAIXAR",
        "Pauta comunitária positiva, mas com teor promocional de assessoria privada — vira nota; prioridade do dia ficou com pautas de maior interesse público"
    ),

    # 15. São Lourenço do Sul — Semana do Meio Ambiente — PUBLICAR materia_longa
    "05d36f23daf2761c14c65a27910c36e80e9b16f2": {
        "titulo_sultv": "Semana do Meio Ambiente de São Lourenço do Sul tem ação contra sacolas plásticas no comércio",
        "chamada_faixa": "Semana do Meio Ambiente em São Lourenço",
        "subtitulo": "Programação segue até 5 de junho com palestras e mobilização no comércio local para reduzir o uso de plástico.",
        "lead": "São Lourenço do Sul realiza até esta sexta-feira (5) a programação da Semana do Meio Ambiente, que inclui palestras e uma ação no comércio contra o uso de sacolas plásticas. As atividades, iniciadas em 1º de junho, foram detalhadas pela secretária municipal de Planejamento e Meio Ambiente, Cristiane Gehrke, e pela presidente do Conselho Municipal de Meio Ambiente (Camuma), Elisa Marques Roloff.",
        "ganchos_3": [
            "Programação segue até 5 de junho com palestras",
            "Ação no comércio incentiva redução de sacolas plásticas",
            "Secretaria e Camuma mobilizam a comunidade lourenciana"
        ],
        "angulo_editorial": "Meio ambiente e comunidade em São Lourenço do Sul — agenda em andamento (termina amanhã), com ação prática no comércio; pauta de engajamento local e sustentabilidade, em sintonia com o Dia Mundial do Meio Ambiente (5/6).",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Camuma", "CDL/ACI local"],
        "lead_materia_longa": "São Lourenço do Sul realiza até esta sexta-feira (5) a programação da Semana do Meio Ambiente, que inclui palestras e uma ação no comércio contra o uso de sacolas plásticas.",
        "post_instagram": {
            "caption": "A Semana do Meio Ambiente de São Lourenço do Sul segue até sexta (5) com palestras e uma ação especial no comércio para reduzir o uso de sacolas plásticas. Levar a sacola retornável virou gesto de cuidado com a Lagoa dos Patos e com o futuro da cidade.",
            "hashtags": ["#SãoLourençoDoSul", "#MeioAmbiente", "#Sustentabilidade", "#MenosPlástico", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Menos plástico em São Lourenço.",
            "desenvolvimento_45s": "São Lourenço do Sul realiza até sexta-feira, dia 5, a Semana do Meio Ambiente. A programação inclui palestras e uma ação no comércio contra o uso de sacolas plásticas, organizada pela Secretaria de Planejamento e Meio Ambiente com o Conselho Municipal de Meio Ambiente. A ideia é simples: incentivar o consumidor a adotar sacolas retornáveis e reduzir o plástico que polui o solo e as águas da região da Lagoa dos Patos.",
            "fechamento_8s": "Programação vai até 5 de junho.",
            "cta_5s": "Confira no SulTV.",
            "trilha_sugerida": "instrumental leve e positivo"
        },
        "tag_thumbnail": "Semana do Meio Ambiente",
        "briefing_visual": {
            "descricao_pt": "Sacola de pano reutilizável com frutas e verduras em balcão de mercado, ambiente de comércio local, sem rostos identificáveis",
            "query_en": ["reusable cloth bag groceries", "eco friendly shopping bag market", "no plastic bag store counter"],
            "evitar": ["rostos identificáveis", "marcas", "texto legível", "logos"],
            "prompt_ia": "Reusable cloth shopping bag with fresh produce on a local market counter, warm natural light, no identifiable faces, no brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agenda em andamento (encerra 5/6) com ação prática no comércio em São Lourenço do Sul — pauta ambiental, comunitária e atual"
    },

    # 16. Cristal — Av. Passo do Mendonça limpeza — REBAIXAR (já coberta em 31/05)
    "804da2cbe08274dd604274d8db6acc48cc218fed": _skip(
        "REBAIXAR",
        "Matéria já publicada pelo Radar em 31/05 (mesma pauta da fonte) — dedup do histórico bloquearia; sem fato novo"
    ),

}

# 17. Pelotas — produtores de morango discutem associação — PUBLICAR materia_longa
PAUTA_ANGULADA["5243be736e2649528d6bc837fd8bbde97e1353d1"] = {
    "titulo_sultv": "Produtores de morango de Pelotas discutem criação de associação com apoio da Emater",
    "chamada_faixa": "Morango de Pelotas pode ganhar associação",
    "subtitulo": "Cerca de 30 produtores participaram de reunião promovida pela Emater/RS-Ascar para debater organização coletiva do setor.",
    "lead": "Cerca de 30 produtores de morango de Pelotas participaram de reunião promovida pela Emater/RS-Ascar para discutir a criação de uma associação da categoria. A organização coletiva deve trazer ganhos na comercialização, no acesso a políticas públicas e no fortalecimento da representatividade dos produtores da Costa Doce ampliada.",
    "ganchos_3": [
        "Cerca de 30 produtores de morango reunidos em Pelotas",
        "Emater/RS-Ascar articula a criação de associação",
        "Organização coletiva amplia acesso a mercados e políticas públicas"
    ],
    "angulo_editorial": "Agro e economia local em Pelotas — movimento concreto de organização da cadeia do morango, com papel da Emater; pauta positiva de associativismo rural, perfil ideal SulTV.",
    "fontes_complementares_sugeridas": ["Emater/RS-Ascar Pelotas", "Feira Municipal de Pelotas", "Secretaria de Desenvolvimento Rural de Pelotas"],
    "lead_materia_longa": "Cerca de 30 produtores de morango de Pelotas participaram de reunião promovida pela Emater/RS-Ascar para discutir a criação de uma associação da categoria.",
    "post_instagram": {
        "caption": "O morango de Pelotas quer se organizar: cerca de 30 produtores participaram de reunião promovida pela Emater/RS-Ascar para discutir a criação de uma associação. Juntos, eles ganham força na comercialização e no acesso a políticas públicas. Associativismo que fortalece o agro da Costa Doce.",
        "hashtags": ["#Pelotas", "#Morango", "#Agro", "#Emater", "#Associativismo", "#CostaDoce", "#SulTV"]
    },
    "roteiro_short_60s": {
        "abertura_2s": "Morango de Pelotas se organiza.",
        "desenvolvimento_45s": "Cerca de 30 produtores de morango de Pelotas participaram de uma reunião promovida pela Emater para discutir a criação de uma associação da categoria. A organização coletiva facilita a comercialização da fruta, abre portas para políticas públicas como o PAA e a merenda escolar, e dá mais voz ao produtor. O morango já é destaque na Feira Municipal e pode ganhar ainda mais força com o associativismo.",
        "fechamento_8s": "União que fortalece o produtor.",
        "cta_5s": "Mais no SulTV.",
        "trilha_sugerida": "instrumental campeiro leve"
    },
    "tag_thumbnail": "Morango de Pelotas",
    "briefing_visual": {
        "descricao_pt": "Morangos frescos recém-colhidos em caixas de feira de produtor rural, close nas frutas, sem pessoas",
        "query_en": ["fresh strawberries farmers market crates", "strawberry harvest box close up", "strawberry farm produce"],
        "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
        "prompt_ia": "Freshly harvested strawberries in wooden crates at a farmers market stall, vibrant red fruit close-up, natural light, no people, no text, editorial photojournalism style"
    },
    "decisao_final": "PUBLICAR",
    "decisao_motivo": "Movimento concreto de organização da cadeia do morango com Emater em Pelotas — pauta agro positiva, perfil ideal da audiência SulTV"
}

PAUTA_ANGULADA.update({
    # 18. Pelotas/RS — Justiça do Trabalho R$ 156,8 mi — REBAIXAR
    "a6885d87261ed899066eaed1e127d684baa35ba1": _skip(
        "REBAIXAR",
        "Balanço institucional estadual da Justiça do Trabalho sem âncora específica na Costa Doce — vira nota interna"
    ),

    # 19. ALERS — audiência Pelotas privatizações (2019) — BLOQUEAR
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "BLOQUEAR",
        "Matéria de 29/03/2019 raspada do feed da ALERS — sete anos defasada; além disso tema de privatizações tangencia política partidária"
    ),

    # 20. ALERS — Funcriança (2019) — BLOQUEAR
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "BLOQUEAR",
        "Matéria de 29/03/2019 raspada do feed da ALERS — sete anos defasada, sem valor atual"
    ),

    # 21. Guaíba — MP apura fraude registro de ponto — PUBLICAR materia_longa
    "b9fa2d64dd2d772b3c02fa6b483b4ea64ac251b3": {
        "titulo_sultv": "MP investiga suposta fraude no registro de ponto de servidores na Câmara de Guaíba",
        "chamada_faixa": "MP apura fraude de ponto na Câmara de Guaíba",
        "subtitulo": "Operação mira assessores e servidores comissionados que teriam registrado presença e deixado o Legislativo em seguida.",
        "lead": "O Ministério Público do Rio Grande do Sul deflagrou operação para apurar suposta fraude no registro de ponto de servidores da Câmara de Vereadores de Guaíba. A investigação mira assessores e servidores comissionados que teriam registrado presença no Legislativo e deixado o prédio logo em seguida.",
        "ganchos_3": [
            "MP-RS deflagra operação na Câmara de Guaíba",
            "Assessores teriam batido ponto e deixado o Legislativo",
            "Apuração envolve servidores comissionados"
        ],
        "angulo_editorial": "Fiscalização do poder público na região metropolitana próxima à Costa Doce — ação institucional do MP, relato em tom de apuração (uso de 'suposta', 'teriam'), sem nomes e sem viés partidário.",
        "fontes_complementares_sugeridas": ["MP-RS", "Câmara de Vereadores de Guaíba"],
        "lead_materia_longa": "O Ministério Público do Rio Grande do Sul deflagrou operação para apurar suposta fraude no registro de ponto de servidores da Câmara de Vereadores de Guaíba.",
        "post_instagram": {
            "caption": "O Ministério Público gaúcho investiga suposta fraude no registro de ponto na Câmara de Vereadores de Guaíba. Assessores e servidores comissionados teriam registrado presença e deixado o Legislativo em seguida. A apuração está em andamento.",
            "hashtags": ["#Guaíba", "#MPRS", "#Fiscalização", "#ServiçoPúblico", "#RS", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Operação do MP em Guaíba.",
            "desenvolvimento_45s": "O Ministério Público do Rio Grande do Sul deflagrou operação para apurar suposta fraude no registro de ponto de servidores da Câmara de Vereadores de Guaíba. Segundo a investigação, assessores e servidores comissionados teriam registrado presença no Legislativo e deixado o prédio logo em seguida. O caso segue em apuração e os envolvidos têm direito a defesa em todas as etapas.",
            "fechamento_8s": "Investigação em andamento.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "MP investiga Câmara de Guaíba",
        "briefing_visual": {
            "descricao_pt": "Relógio de ponto eletrônico em parede de repartição pública, corredor institucional vazio, sem pessoas",
            "query_en": ["time clock office wall", "electronic attendance terminal", "empty government office corridor"],
            "evitar": ["pessoas", "rostos", "nomes legíveis", "marcas", "texto", "logos"],
            "prompt_ia": "Electronic time clock terminal on the wall of an empty institutional office corridor, neutral lighting, no people, no readable text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Ação institucional concreta do MP-RS em Guaíba — fiscalização do poder público, redação em tom de apuração sem nomes; sem viés partidário"
    },

    # 22. RS — MetSul: neve há um ano e El Niño 2026 — PUBLICAR materia_longa
    "01e4af8f22701aee0014a55e168747935cd1d8cd": {
        "titulo_sultv": "Um ano após neve no Sul, El Niño deve dificultar novas nevadas no inverno de 2026",
        "chamada_faixa": "El Niño deve dificultar neve no Sul em 2026",
        "subtitulo": "Em maio de 2025, RS e SC registraram neve com acumulação; análise da MetSul aponta cenário menos favorável neste ano.",
        "lead": "Há um ano, em 29 de maio de 2025, o Sul do Brasil registrava a primeira neve daquele ano, com acumulação no Rio Grande do Sul e em Santa Catarina — fenômeno incomum para maio. Em 2026, segundo análise da MetSul Meteorologia, a presença do El Niño tende a dificultar a ocorrência de novas nevadas no inverno.",
        "ganchos_3": [
            "Neve com acumulação completou um ano no Sul do Brasil",
            "El Niño muda o cenário do inverno de 2026",
            "Análise da MetSul aponta condições menos favoráveis à neve"
        ],
        "angulo_editorial": "Clima regional — efeméride da neve de 2025 combinada com a pergunta que interessa a todo gaúcho no início do inverno: vai nevar este ano? Âncora técnica na MetSul, tom informativo sem sensacionalismo.",
        "fontes_complementares_sugeridas": ["MetSul Meteorologia", "Inmet", "Defesa Civil RS"],
        "lead_materia_longa": "Há um ano, em 29 de maio de 2025, o Sul do Brasil registrava a primeira neve daquele ano, com acumulação no Rio Grande do Sul e em Santa Catarina. Em 2026, a presença do El Niño tende a dificultar novas nevadas, segundo a MetSul Meteorologia.",
        "post_instagram": {
            "caption": "Faz um ano que a neve pintou o Sul do Brasil de branco, ainda em maio de 2025. E em 2026, será que repete? Segundo a MetSul Meteorologia, o El Niño tende a dificultar novas nevadas neste inverno. Invernos com El Niño costumam ser mais úmidos e com menos frio extremo no RS.",
        "hashtags": ["#Neve", "#ElNiño", "#Inverno", "#RioGrandeDoSul", "#Clima", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Vai nevar no RS em 2026?",
            "desenvolvimento_45s": "Há exatamente um ano, em maio de 2025, o Sul do Brasil registrava neve com acumulação no Rio Grande do Sul e em Santa Catarina, algo raro para aquele mês. Neste ano o cenário é outro: segundo a MetSul Meteorologia, a presença do El Niño tende a dificultar novas nevadas no inverno de 2026. O fenômeno costuma deixar os invernos gaúchos mais úmidos e com menos episódios de frio extremo, reduzindo as chances de neve.",
            "fechamento_8s": "El Niño joga contra a neve este ano.",
            "cta_5s": "Acompanhe o clima no SulTV.",
            "trilha_sugerida": "instrumental contemplativo"
        },
        "tag_thumbnail": "Neve e El Niño 2026",
        "briefing_visual": {
            "descricao_pt": "Paisagem rural do Sul do Brasil coberta por fina camada de neve ao amanhecer, campo e araucárias, sem pessoas",
            "query_en": ["snow southern brazil countryside", "light snow rural field sunrise", "frost covered pasture winter"],
            "evitar": ["pessoas", "marcas", "texto", "logos"],
            "prompt_ia": "Rural landscape in southern Brazil covered by a thin layer of snow at sunrise, fields and araucaria trees, soft light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima é pauta de altíssimo interesse da audiência no início do inverno — efeméride concreta + análise técnica da MetSul, fonte de maior score do radar"
    },

    # 23. RS — MetSul verifica fake dos ciclones gêmeos — REBAIXAR
    "da4142fbb0edad6b837e4d203d5fe4dd944d642b": _skip(
        "REBAIXAR",
        "Fact-check relevante, mas pauta de 28/05 já com uma semana — prioridade do dia ficou com a pauta de neve/El Niño da mesma fonte; quota qualitativa"
    ),

    # 24. RS — Canal Rural: renegociação de dívidas no Senado — PUBLICAR materia_longa
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "titulo_sultv": "Produtores do RS temem que renegociação de dívidas rurais trave no Senado",
        "chamada_faixa": "Renegociação de dívidas preocupa produtores",
        "subtitulo": "Setor teme ficar sem acesso ao crédito rural para a próxima safra caso a proposta não seja aprovada, mostra o Canal Rural.",
        "lead": "Produtores rurais do Rio Grande do Sul vivem a expectativa pela aprovação da renegociação de dívidas no Senado e temem as consequências caso a proposta não avance. O principal receio do setor, segundo reportagem do Canal Rural, é ficar sem acesso ao crédito rural para o financiamento da próxima safra.",
        "ganchos_3": [
            "Renegociação de dívidas rurais aguarda votação no Senado",
            "Receio é ficar sem crédito para a próxima safra",
            "Sucessivas quebras de safra agravaram o endividamento no RS"
        ],
        "angulo_editorial": "Agro e economia — endividamento rural é a pauta econômica mais sensível do campo gaúcho após as estiagens e enchentes recentes; foco no impacto para o produtor da Costa Doce (arroz e soja), citando o Canal Rural como fonte. Sem viés partidário: trata-se de tramitação legislativa de interesse econômico.",
        "fontes_complementares_sugeridas": ["Canal Rural", "Farsul", "Federarroz", "Senado Federal"],
        "lead_materia_longa": "Produtores rurais do Rio Grande do Sul vivem a expectativa pela aprovação da renegociação de dívidas no Senado e temem ficar sem acesso ao crédito rural para a próxima safra caso a proposta não avance.",
        "post_instagram": {
            "caption": "A renegociação das dívidas rurais segue pendente no Senado e o campo gaúcho está em alerta: sem a aprovação, o receio é ficar sem crédito para plantar a próxima safra. Depois de estiagens e enchentes, o endividamento virou a maior preocupação do produtor do RS.",
            "hashtags": ["#Agro", "#CréditoRural", "#RioGrandeDoSul", "#Safra", "#Senado", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Campo gaúcho em alerta.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul aguardam com apreensão a votação da renegociação de dívidas no Senado. O receio, segundo reportagem do Canal Rural, é que sem a aprovação o setor fique sem acesso ao crédito rural para financiar a próxima safra. Depois de sucessivas quebras por estiagem e enchentes, o endividamento se acumulou e a renegociação virou condição para muitos produtores seguirem plantando arroz e soja na região.",
            "fechamento_8s": "Setor cobra definição do Senado.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Dívidas rurais no Senado",
        "briefing_visual": {
            "descricao_pt": "Lavoura de soja madura no Rio Grande do Sul com céu carregado ao fundo, vista ampla, sem pessoas",
            "query_en": ["soybean field cloudy sky brazil", "mature soybean crop wide shot", "farm field storm clouds"],
            "evitar": ["pessoas", "marcas de máquinas", "texto", "logos"],
            "prompt_ia": "Wide shot of a mature soybean field in southern Brazil under heavy gray clouds, dramatic but realistic light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta econômica mais sensível do agro gaúcho com âncora regional clara (crédito para a safra de arroz e soja) — fonte Canal Rural (parceiro) citada de forma positiva"
    },

    # 25. Santa Maria — UFSM projeto Rede HU+ — REBAIXAR
    "014b0c7e7ebe83a7e9d2818d435714326ff6390e": _skip(
        "REBAIXAR",
        "Pauta institucional da UFSM relevante mas distante do núcleo Costa Doce — vira nota interna"
    ),

    # 26. Santa Maria — Moodle UFSM indisponível — BLOQUEAR
    "52a34cdaeffd6c322e99946d7c0ec9b186f6071c": _skip(
        "BLOQUEAR",
        "Aviso interno de manutenção de TI da UFSM — sem valor editorial para a audiência SulTV"
    ),

    # 27. Venâncio Aires — programa eleitoral 'Seu Voto, Sua Voz' — BLOQUEAR (guardrail política)
    "3d3052f08772dc51ce3b3597a5e7ba24954d7a19": _skip(
        "BLOQUEAR",
        "Guardrail: política partidária/eleitoral (programa de cobertura eleitoral com dirigentes de partidos, tema polarização) — bloqueio automático"
    ),

    # 28. Venâncio Aires — triplo homicídio — BLOQUEAR
    "429b1fdc4efe1e00111a9de9815130e3039268c8": _skip(
        "BLOQUEAR",
        "Crime violento grave (triplo homicídio) em região distante do núcleo — incompatível com tom institucional sem dramalhão; risco de identificação de vítimas no desdobramento"
    ),

    # 29. Bento Gonçalves — ExpoBento e Fenavinho — REBAIXAR
    "35272a52895a0ef9dbcfd3bf86d3cfae4eacaae8": _skip(
        "REBAIXAR",
        "Evento relevante no estado, mas Serra Gaúcha está fora do núcleo Costa Doce — vira nota interna/agenda"
    ),

    # 30. Caxias do Sul — drone adaptado para drogas — REBAIXAR
    "a354329526fb680045e13475a554761fb1b32029": _skip(
        "REBAIXAR",
        "Pauta policial curiosa mas em região distante (Caxias do Sul) — fora do núcleo de cobertura"
    ),
})


MATERIAS = {
    "293d30ecab37491f415233c4ce53462d32f3b51e": """### Título ###
Pelotas confirma 14º caso de dengue em 2026 e reforça alerta contra o mosquito

### Artigo ###
A Prefeitura de Pelotas confirmou nesta quarta-feira (3) o 14º caso de dengue registrado no município em 2026. O paciente é um jovem de 18 anos que contraiu a doença dentro do próprio município, o que caracteriza um caso autóctone e indica a circulação local do mosquito transmissor, o Aedes aegypti. A confirmação reforça o estado de atenção na cidade, uma das maiores da Costa Doce ampliada, e renova as orientações da vigilância em saúde para a eliminação de criadouros. Casos autóctones costumam acender o sinal de alerta das equipes de saúde porque mostram que a transmissão está ocorrendo no território, e não apenas em viagens a outras regiões. A principal medida de prevenção segue sendo a eliminação de água parada: pratos de vasos de plantas, calhas entupidas, pneus, garrafas, caixas d'água destampadas e qualquer recipiente que acumule água podem servir de criadouro para o mosquito. A recomendação das equipes de saúde é dedicar alguns minutos por semana à vistoria de pátios, quintais e áreas de serviço. Quem apresentar sintomas como febre alta de início súbito, dores no corpo e nas articulações, dor atrás dos olhos, manchas vermelhas na pele, náuseas ou cansaço intenso deve procurar uma unidade de saúde para avaliação, evitando a automedicação. O acompanhamento dos números da dengue é atualizado pela prefeitura ao longo do ano, e a colaboração da comunidade na eliminação dos focos é apontada como o fator mais importante para impedir o avanço da doença no município e na região.

### Legenda sugerida ###
Pelotas chega a 14 casos de dengue em 2026; caso mais recente é de jovem que contraiu a doença no município.

### Palavras-chave ###
Pelotas, dengue, caso autóctone, Aedes aegypti, saúde pública, prevenção, vigilância em saúde, Costa Doce
""",

    "a50e1c3a11166004b98df86395d6db399200e9d4": """### Título ###
Operação investiga furto de 47 cabeças de gado em São Lourenço do Sul

### Artigo ###
A Delegacia Especializada em Crimes Rurais e Abigeato (DECRAB) de Camaquã deflagrou nova fase da Operação Três Estâncias para investigar o furto de 47 cabeças de gado em São Lourenço do Sul, na região da Costa Doce. Durante o cumprimento de mandado de busca e apreensão, os policiais apreenderam uma arma de fogo, munições e aparelhos celulares, materiais que devem ajudar a esclarecer a dinâmica do crime e identificar os envolvidos. O abigeato — como é chamado o furto de animais de produção — é um dos crimes que mais preocupam os produtores rurais do Rio Grande do Sul, por atingir diretamente o patrimônio e a renda das famílias do campo. Além do prejuízo imediato com a perda dos animais, o crime gera insegurança nas propriedades e custos adicionais com vigilância, cercas e seguros. A atuação de delegacias especializadas como a DECRAB tem sido apontada pelo setor produtivo como fundamental para o enfrentamento desse tipo de delito, pela capacidade de reunir inteligência policial, conhecimento do meio rural e integração com outras forças de segurança. A Operação Três Estâncias já teve fases anteriores na região e segue em andamento, com diligências para localizar os animais subtraídos e responsabilizar os autores. A polícia orienta que produtores registrem ocorrência imediatamente ao identificar a falta de animais, mantenham a marcação e a documentação do rebanho em dia e comuniquem movimentações suspeitas nas estradas vicinais, informações que costumam ser decisivas para o trabalho de investigação.

### Legenda sugerida ###
DECRAB de Camaquã cumpre mandado e apreende arma em investigação de furto de 47 bovinos em São Lourenço do Sul.

### Palavras-chave ###
São Lourenço do Sul, abigeato, furto de gado, DECRAB, Camaquã, Operação Três Estâncias, segurança rural, Costa Doce
""",

    "f89077d77398dc238539b7a4ea1a8ceefafe72d3": """### Título ###
Sentinela do Sul intensifica ações para atrair investimentos e ampliar empregos

### Artigo ###
A Prefeitura de Sentinela do Sul vem intensificando as ações voltadas ao desenvolvimento econômico e à geração de novas oportunidades de emprego para a população. Conduzido pelo prefeito Julio Carvalho, o movimento busca atrair investimentos privados e fortalecer a economia do município da Costa Doce, criando condições para que empresas se instalem e para que os negócios já existentes possam crescer. Em municípios de pequeno porte, a agenda de desenvolvimento econômico tem peso direto na vida das famílias: cada nova empresa instalada significa postos de trabalho, renda circulando no comércio local e mais arrecadação para investir em serviços públicos. A atração de investimentos também é vista como estratégia para reduzir a saída de jovens em busca de oportunidades nos centros maiores, um desafio comum às cidades do interior gaúcho. Iniciativas dessa natureza costumam envolver a desburocratização da abertura de empresas, a oferta de áreas e incentivos para instalação, o apoio ao empreendedor local e a aproximação com investidores de fora do município. A localização de Sentinela do Sul, na região da Costa Doce, próxima a centros como Camaquã e com acesso à BR-116, é um dos atrativos que o município pode explorar na busca por novos negócios, somada às potencialidades do setor primário local. A administração municipal deve detalhar nos próximos meses os resultados das tratativas em andamento. Interessados em empreender ou investir no município podem buscar informações diretamente nos canais oficiais da Prefeitura de Sentinela do Sul.

### Legenda sugerida ###
Sentinela do Sul intensifica agenda de desenvolvimento econômico para atrair empresas e gerar empregos.

### Palavras-chave ###
Sentinela do Sul, investimentos, empregos, desenvolvimento econômico, Costa Doce, empreendedorismo, interior gaúcho
""",

    "05d36f23daf2761c14c65a27910c36e80e9b16f2": """### Título ###
Semana do Meio Ambiente de São Lourenço do Sul tem ação contra sacolas plásticas no comércio

### Artigo ###
São Lourenço do Sul realiza até esta sexta-feira (5) a programação da Semana do Meio Ambiente, que começou em 1º de junho e inclui palestras e uma ação no comércio local contra o uso de sacolas plásticas. As atividades foram detalhadas pela secretária municipal de Planejamento e Meio Ambiente, Cristiane Gehrke, e pela presidente do Conselho Municipal de Meio Ambiente (Camuma), Elisa Marques Roloff. A mobilização no comércio é um dos destaques da programação: a proposta é incentivar consumidores e lojistas a reduzirem o uso de sacolas plásticas descartáveis, estimulando alternativas como sacolas retornáveis de pano e caixas reutilizáveis. O plástico de uso único está entre os resíduos que mais poluem o solo e os recursos hídricos, tema especialmente sensível em um município banhado pela Lagoa dos Patos, cuja orla é patrimônio ambiental e turístico da Costa Doce. As palestras da semana abordam educação ambiental e práticas sustentáveis, aproximando escolas, comunidade e poder público da agenda ecológica. A realização coincide com o Dia Mundial do Meio Ambiente, celebrado em 5 de junho, data que mobiliza ações em todo o país. Para os organizadores, o engajamento do comércio é estratégico porque transforma um gesto cotidiano — a escolha de como levar as compras para casa — em hábito de cuidado coletivo. A programação completa e as orientações sobre as atividades podem ser conferidas nos canais oficiais da Prefeitura de São Lourenço do Sul e do Camuma.

### Legenda sugerida ###
Semana do Meio Ambiente segue até sexta (5) em São Lourenço do Sul com palestras e ação contra sacolas plásticas.

### Palavras-chave ###
São Lourenço do Sul, Semana do Meio Ambiente, sacolas plásticas, sustentabilidade, Camuma, Lagoa dos Patos, Costa Doce, educação ambiental
""",

    "5243be736e2649528d6bc837fd8bbde97e1353d1": """### Título ###
Produtores de morango de Pelotas discutem criação de associação com apoio da Emater

### Artigo ###
Cerca de 30 produtores de morango de Pelotas participaram de reunião promovida pela Emater/RS-Ascar para discutir a criação de uma associação da categoria. O encontro reuniu participantes da Feira Municipal e marcou um passo concreto na organização coletiva de uma cadeia produtiva que vem ganhando importância na economia rural do município e da Costa Doce ampliada. A organização em associação traz benefícios práticos para o produtor: facilita a comercialização em maior escala, abre acesso a políticas públicas — como programas de aquisição de alimentos e alimentação escolar —, viabiliza compras conjuntas de insumos e fortalece a representatividade da categoria junto ao poder público e ao mercado. Para quem produz em pequenas áreas, como é típico da fruticultura familiar, a união é muitas vezes a diferença entre vender bem e vender mal a produção. O morango de Pelotas já conquistou espaço nas feiras e no comércio local, com a venda direta ao consumidor valorizando a produção fresca e de origem conhecida. A criação de uma associação tende a profissionalizar ainda mais o setor, permitindo padronização de qualidade, planejamento de safra e até a construção de uma identidade regional para a fruta. O papel da Emater/RS-Ascar na articulação reforça o trabalho de extensão rural que historicamente apoia a agricultura familiar gaúcha na transição para formas mais organizadas de produção e venda. Os próximos passos do grupo devem ser definidos em novas reuniões, com a formalização da entidade e a definição de diretoria e estatuto.

### Legenda sugerida ###
Cerca de 30 produtores de morango de Pelotas discutem criação de associação em reunião da Emater/RS-Ascar.

### Palavras-chave ###
Pelotas, morango, Emater, associação, agricultura familiar, fruticultura, Feira Municipal, Costa Doce, associativismo
""",

    "b9fa2d64dd2d772b3c02fa6b483b4ea64ac251b3": """### Título ###
MP investiga suposta fraude no registro de ponto de servidores na Câmara de Guaíba

### Artigo ###
O Ministério Público do Rio Grande do Sul deflagrou operação para apurar suposta fraude no registro de ponto de servidores da Câmara de Vereadores de Guaíba. A investigação mira assessores e servidores comissionados que teriam registrado presença no Legislativo municipal e deixado o prédio logo em seguida, sem cumprir o expediente. O caso está em fase de apuração e os envolvidos têm assegurado o direito de defesa em todas as etapas do processo. O registro de ponto é o instrumento que comprova o cumprimento da jornada de trabalho no serviço público, e eventuais fraudes nesse controle configuram lesão direta ao erário, já que a remuneração é paga com recursos dos contribuintes. Investigações desse tipo costumam reunir imagens de câmeras, registros eletrônicos de entrada e saída e depoimentos para confrontar a frequência registrada com a presença efetiva dos servidores. Caso as irregularidades sejam confirmadas, os envolvidos podem responder nas esferas administrativa, civil e criminal, incluindo a devolução de valores recebidos indevidamente. A fiscalização sobre o funcionamento dos legislativos municipais tem se intensificado no Rio Grande do Sul, com o Ministério Público atuando a partir de denúncias e de cruzamento de dados. Para a população, o caso reforça a importância dos mecanismos de transparência, como os portais oficiais que publicam a frequência, os salários e a estrutura de pessoal dos órgãos públicos. A Câmara de Vereadores de Guaíba poderá se manifestar sobre a investigação, e o andamento do caso deve ser acompanhado nos canais oficiais do MP-RS.

### Legenda sugerida ###
MP-RS apura suposta fraude no ponto de assessores e comissionados na Câmara de Vereadores de Guaíba.

### Palavras-chave ###
Guaíba, Ministério Público, MP-RS, fraude no ponto, Câmara de Vereadores, servidores comissionados, fiscalização, transparência
""",

    "01e4af8f22701aee0014a55e168747935cd1d8cd": """### Título ###
Um ano após neve no Sul, El Niño deve dificultar novas nevadas no inverno de 2026

### Artigo ###
Há um ano, em 29 de maio de 2025, o Sul do Brasil registrava a primeira neve daquele ano, com acumulação no Rio Grande do Sul e em Santa Catarina — um fenômeno incomum para o mês de maio, que antecipou o clima de inverno e rendeu imagens marcantes nas áreas mais altas da região. Em 2026, o cenário é diferente: segundo análise da MetSul Meteorologia, a presença do fenômeno El Niño tende a dificultar a ocorrência de novas nevadas no inverno que se aproxima. O El Niño é caracterizado pelo aquecimento anormal das águas do Oceano Pacífico Equatorial e altera os padrões de circulação atmosférica em todo o planeta. No Sul do Brasil, seus invernos costumam ser mais úmidos, com chuvas acima da média, e com menor frequência de massas de ar polar intensas — justamente a combinação de frio extremo e umidade em níveis adequados que permite a formação de neve. Isso não significa que o frio estará ausente: episódios de temperaturas baixas, geadas e até eventos isolados de neve em pontos altos da Serra não ficam descartados, mas as condições de grande escala jogam contra a repetição do espetáculo branco de 2025. Para o produtor rural da Costa Doce e de todo o estado, o sinal mais relevante do El Niño costuma ser o regime de chuvas, que influencia o planejamento da safra de inverno e a preparação para o plantio de primavera. O acompanhamento das previsões atualizadas ao longo da estação é recomendado para quem depende do clima no campo.

### Legenda sugerida ###
Neve de maio de 2025 completa um ano; com El Niño, MetSul aponta inverno de 2026 menos favorável a nevadas.

### Palavras-chave ###
neve, El Niño, inverno 2026, Rio Grande do Sul, MetSul, clima, meteorologia, frio, Sul do Brasil
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS temem que renegociação de dívidas rurais trave no Senado

### Artigo ###
Produtores rurais do Rio Grande do Sul vivem a expectativa pela votação da renegociação de dívidas no Senado e temem as consequências caso a proposta não seja aprovada. O principal receio do setor, segundo reportagem do Canal Rural, é ficar sem acesso ao crédito rural para o financiamento da próxima safra — um risco que atinge em cheio regiões produtoras como a Costa Doce, onde o arroz e a soja sustentam a economia de dezenas de municípios. O endividamento do campo gaúcho se agravou nos últimos anos com a sequência de eventos climáticos extremos: estiagens severas que quebraram safras consecutivas e, na sequência, as enchentes históricas que atingiram o estado. Sem conseguir honrar os compromissos das safras frustradas, muitos produtores acumularam parcelas e perderam capacidade de tomar novos financiamentos, entrando em um ciclo que compromete o custeio do próximo plantio. A renegociação em discussão no Congresso é vista pelas entidades do setor como condição para restabelecer a capacidade de pagamento e manter o produtor na atividade. Enquanto a votação não acontece, cresce a apreensão no campo, já que o calendário agrícola não espera: as decisões sobre compra de insumos e financiamento da safra de verão precisam ser tomadas nos próximos meses. Lideranças do agronegócio gaúcho têm intensificado a interlocução com a bancada do estado em Brasília para dar celeridade à tramitação. O tema deve seguir no centro do debate econômico do agro nas próximas semanas, e os desdobramentos no Senado serão decisivos para o planejamento da safra 2026/2027 no Rio Grande do Sul.

### Legenda sugerida ###
Campo gaúcho teme ficar sem crédito para a próxima safra caso renegociação de dívidas não avance no Senado.

### Palavras-chave ###
renegociação de dívidas, crédito rural, Senado, Rio Grande do Sul, agro, safra, arroz, soja, endividamento rural
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

        # Quota: máx 10 publicações/dia (regra 14)
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

    from collections import Counter
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
                print(f"[angular] AVISO: {p['id_hash']} é PUBLICAR/materia_longa mas sem texto em MATERIAS")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
