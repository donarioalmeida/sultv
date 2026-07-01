#!/usr/bin/env python3
"""
angular_2026-06-15.py — angulação editorial + redação (cowork-faz-tudo).
Pauta de 2026-06-15. Lê state/aprovadas_2026-06-15.json, gera
state/pauta_2026-06-15.json + state/materias_2026-06-15/<id_hash>.md.

Regra 12 (INEGOCIÁVEL): nenhum texto menciona veículos/portais/rádios/jornais.
Material coletado é insumo, reformatado 100% no tom Redação SulTV.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-15"


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

    # 0. Camaquã — Campanha do Agasalho 2026 — PUBLICAR materia_longa
    "882edeb88f0be982907d48640a98bb6fe38fa6b1": {
        "titulo_sultv": "Camaquã lança Campanha do Agasalho 2026 e abre pontos de doação para o inverno",
        "chamada_faixa": "Camaquã lança Campanha do Agasalho 2026",
        "subtitulo": "Ação coordenada pela Assistência Social arrecada roupas e cobertores e busca promover autonomia das famílias atendidas no inverno.",
        "lead": "A Prefeitura de Camaquã lançou a Campanha do Agasalho 2026, mobilização que arrecada roupas, calçados e cobertores para apoiar famílias em situação de vulnerabilidade durante o inverno na Costa Doce. As ações foram apresentadas pelo secretário Fabiano Ribeiro, que destacou medidas voltadas também à autonomia das famílias atendidas.",
        "ganchos_3": [
            "Campanha do Agasalho 2026 mobiliza Camaquã para o inverno",
            "Doações de roupas, calçados e cobertores em pontos de coleta",
            "Foco também na autonomia das famílias em vulnerabilidade"
        ],
        "angulo_editorial": "Solidariedade e serviço em cidade-núcleo (Camaquã) no auge do frio — pauta comunitária positiva, com fonte institucional nomeada (secretário), perfil ideal SulTV.",
        "fontes_complementares_sugeridas": ["Prefeitura de Camaquã", "Secretaria de Assistência Social de Camaquã", "CRAS Camaquã"],
        "lead_materia_longa": "A Prefeitura de Camaquã lançou a Campanha do Agasalho 2026, que arrecada roupas, calçados e cobertores para apoiar famílias em situação de vulnerabilidade durante o inverno.",
        "post_instagram": {
            "caption": "Camaquã lançou a Campanha do Agasalho 2026. A mobilização arrecada roupas, calçados e cobertores para ajudar famílias a enfrentar o inverno da Costa Doce. Quem puder doar aquece quem mais precisa — um agasalho que sobra no seu armário pode fazer a diferença na vida de uma família.",
            "hashtags": ["#Camaquã", "#CampanhaDoAgasalho", "#Solidariedade", "#Inverno", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Camaquã aquece o inverno.",
            "desenvolvimento_45s": "A Prefeitura de Camaquã lançou a Campanha do Agasalho 2026. A ação arrecada roupas, calçados e cobertores para apoiar famílias em situação de vulnerabilidade durante os meses mais frios. Além da doação imediata, a campanha aposta em medidas para promover a autonomia das famílias atendidas. Quem quiser colaborar pode levar peças em bom estado aos pontos de coleta indicados pela Secretaria de Assistência Social.",
            "fechamento_8s": "Doe e aqueça quem precisa.",
            "cta_5s": "Saiba como no SulTV.",
            "trilha_sugerida": "instrumental acolhedor"
        },
        "tag_thumbnail": "Campanha do Agasalho",
        "briefing_visual": {
            "descricao_pt": "Cobertores e roupas de inverno dobrados em caixas de doação, ambiente interno, sem rostos identificáveis",
            "query_en": ["winter clothes donation box", "folded blankets charity donation", "warm clothing collection"],
            "evitar": ["rostos identificáveis", "marcas", "texto legível", "logos"],
            "prompt_ia": "Folded winter blankets and warm clothing arranged in donation boxes indoors, soft natural light, no identifiable faces, no brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta solidária concreta em cidade-núcleo (Camaquã) no auge do inverno, com fonte institucional nomeada — alto interesse comunitário"
    },

    # 1. Camaquã — Vereador aciona Anatel por falhas da TIM — PUBLICAR materia_longa
    "5b7dd5a19fab42dfa2fa1abff1b84af7bb5b3381": {
        "titulo_sultv": "Vereador aciona Anatel por falhas de telefonia e internet em Camaquã e região",
        "chamada_faixa": "Anatel é acionada por falhas de telefonia em Camaquã",
        "subtitulo": "Solicitação encaminhada à agência reguladora busca esclarecimentos e medidas para reduzir as falhas na telefonia móvel e na internet.",
        "lead": "O vereador Vladimir Tili acionou a Agência Nacional de Telecomunicações (Anatel) para cobrar providências diante das falhas recorrentes de telefonia móvel e internet em Camaquã e região. A solicitação pede esclarecimentos sobre a qualidade do serviço prestado e medidas para reduzir as instabilidades que afetam moradores e empresas da Costa Doce.",
        "ganchos_3": [
            "Anatel é acionada por falhas de telefonia em Camaquã",
            "Solicitação cobra qualidade do sinal móvel e da internet",
            "Instabilidades afetam moradores e empresas da região"
        ],
        "angulo_editorial": "Serviço e direito do consumidor em cidade-núcleo (Camaquã) — conectividade é tema concreto e de utilidade direta; fonte institucional nomeada (vereador), sem viés partidário/eleitoral.",
        "fontes_complementares_sugeridas": ["Anatel", "Câmara de Vereadores de Camaquã", "Procon regional"],
        "lead_materia_longa": "O vereador Vladimir Tili acionou a Agência Nacional de Telecomunicações (Anatel) para cobrar providências diante das falhas recorrentes de telefonia móvel e internet em Camaquã e região.",
        "post_instagram": {
            "caption": "Sinal que cai, internet que trava: as falhas de telefonia em Camaquã e região foram levadas à Anatel. A solicitação cobra esclarecimentos sobre a qualidade do serviço e medidas para resolver as instabilidades que atrapalham moradores e empresas da Costa Doce. Conectividade é serviço essencial.",
            "hashtags": ["#Camaquã", "#Anatel", "#Telefonia", "#Internet", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Sinal ruim vira caso na Anatel.",
            "desenvolvimento_45s": "As falhas recorrentes de telefonia móvel e internet em Camaquã e região foram levadas à Anatel. A solicitação cobra esclarecimentos sobre a qualidade do serviço e medidas para reduzir as instabilidades. Para moradores, comércio e produtores rurais, a conectividade deixou de ser conforto e virou ferramenta de trabalho: vendas, pagamentos, telemedicina e até a gestão da lavoura dependem de um sinal que funcione.",
            "fechamento_8s": "Cobrança por sinal de qualidade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental neutro"
        },
        "tag_thumbnail": "Falhas de telefonia",
        "briefing_visual": {
            "descricao_pt": "Torre de telefonia celular ao fundo de paisagem rural do Sul do Brasil, céu claro, sem pessoas",
            "query_en": ["cell tower rural landscape", "telecommunications antenna countryside", "mobile signal tower field"],
            "evitar": ["pessoas", "logos de operadoras", "texto", "marcas legíveis"],
            "prompt_ia": "A cellular telecommunications tower in a rural southern Brazilian landscape under a clear sky, no people, no brand logos, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta de serviço/consumidor concreta em cidade-núcleo (Camaquã) — conectividade afeta moradores e produtores; fonte nomeada, sem viés eleitoral"
    },

    # 2. Tapes — 'JORNAL INFORMATIVO DA PREFA – EDIÇÃO 02' — BLOQUEAR (header/agregado)
    "60d4de7cf2643dde3ae3c9aa55263622c2a7f7f9": _skip(
        "BLOQUEAR",
        "Título é cabeçalho de boletim institucional agregado ('JORNAL INFORMATIVO DA PREFA – EDIÇÃO 02') — não é fato único ancorável; regra de bloqueio de cabeçalhos/seções"
    ),

    # 3. Sertão Santana — Bocha Quadrangular Final — REBAIXAR
    "bc70ff44760df32faf91f7781e947aa605f25149": _skip(
        "REBAIXAR",
        "Resultado de campeonato amador de bocha de baixo interesse para a audiência ampla — vira nota de agenda esportiva"
    ),

    # 4. Arambaré — cursos de qualificação (16/abril) — REBAIXAR (pauta antiga)
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "REBAIXAR",
        "Notícia datada de 16/04/2026 raspada da página da prefeitura — inscrições provavelmente encerradas; publicar como atual seria impreciso"
    ),

    # 5. Arambaré — reconstrução plataforma de pesca (19/janeiro) — REBAIXAR (pauta antiga)
    "7328151d0f689699ca147e00ec7ffb87008ee51e": _skip(
        "REBAIXAR",
        "Notícia datada de 19/01/2026 raspada da página da prefeitura — anúncio antigo, sem fato novo verificável nesta data"
    ),

    # 6. Chuvisca — edital de penalidade — BLOQUEAR
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR",
        "Edital procedural de publicação de penalidade — sem valor editorial; regra de bloqueio de editais"
    ),

    # 7. Chuvisca — edital perímetro urbano — BLOQUEAR
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR",
        "Edital procedural (abertura de prazo para requerimentos) — regra de bloqueio de editais; tema pode virar pauta própria quando houver fato"
    ),

    # 8. São Lourenço do Sul — reunião Sesc/Senac/Sindilojas — REBAIXAR
    "4a19f3b447abaaef75271b2e2dbf1a33ae46591b": _skip(
        "REBAIXAR",
        "Reunião administrativa de 'alinhamento de possíveis ações' sem fato concreto fechado — vira nota interna; prioridade do dia em SLS ficou com a Operação Terra Forte"
    ),

    # 9. Barra do Ribeiro — Velejaço solidário — REBAIXAR (título quebrado)
    "2ca9c6c05b652779fe1185d698a6d67e649d2e53": _skip(
        "REBAIXAR",
        "Título raspado quebrado ('Secretaria... 6 Velejaço solidário') e sem corpo de texto — conteúdo fino; pode render agenda quando houver data/detalhes"
    ),

    # 10. Barra do Ribeiro — contracheques servidores — BLOQUEAR
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": _skip(
        "BLOQUEAR",
        "Título é cabeçalho de secretaria concatenado com aviso interno a servidores — comunicado administrativo, não é matéria"
    ),

    # 11. Sentinela do Sul — aviso de audiência pública — REBAIXAR
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "REBAIXAR",
        "Título genérico '📢 AVISO DE AUDIÊNCIA PÚBLICA' sem corpo de texto/data/tema — sem fato ancorável; acompanhar para virar pauta quando houver pauta da audiência"
    ),

    # 12. Sentinela do Sul — emissão de notas fiscais — BLOQUEAR
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR",
        "Comunicado procedural sobre emissor nacional de NFS-e — aviso administrativo, não é matéria"
    ),

    # 13. Cristal — Rua Camaquã preparação para calçamento — REBAIXAR (consistente c/ 04/06)
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": _skip(
        "REBAIXAR",
        "Obra em estágio preparatório, fonte sem corpo de texto — conteúdo fino (já rebaixado em 04/06 pela mesma razão); publicar quando o calçamento iniciar/concluir"
    ),

    # 14. São Lourenço do Sul — Operação Terra Forte (50 famílias) — PUBLICAR materia_longa
    "efd8d70803038c24031276ce8b3cad9118f9fd60": {
        "titulo_sultv": "São Lourenço do Sul entrega cartões da primeira fase do Operação Terra Forte a 50 famílias",
        "chamada_faixa": "Operação Terra Forte beneficia 50 famílias",
        "subtitulo": "Entrega reuniu município, Emater/RS e Banrisul na primeira etapa do programa de apoio à agricultura familiar.",
        "lead": "Cinquenta famílias de São Lourenço do Sul receberam, na última sexta-feira (12), os cartões da primeira fase do Programa Operação Terra Forte. A entrega reuniu a administração municipal, a Emater/RS-Ascar e o Banrisul, em ação voltada a fortalecer a agricultura familiar na região da Costa Doce.",
        "ganchos_3": [
            "50 famílias contempladas na primeira fase do programa",
            "Município, Emater/RS e Banrisul juntos na entrega",
            "Apoio direto à agricultura familiar de São Lourenço do Sul"
        ],
        "angulo_editorial": "Agro e desenvolvimento social em cidade-núcleo (São Lourenço do Sul) — fato concreto, quantitativo (50 famílias), recente (12/6) e institucional (Emater, Banrisul); perfil ideal SulTV.",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul", "Emater/RS-Ascar", "Banrisul"],
        "lead_materia_longa": "Cinquenta famílias de São Lourenço do Sul receberam, na última sexta-feira (12), os cartões da primeira fase do Programa Operação Terra Forte, em entrega que reuniu o município, a Emater/RS-Ascar e o Banrisul.",
        "post_instagram": {
            "caption": "Cinquenta famílias de São Lourenço do Sul receberam os cartões da primeira fase do Programa Operação Terra Forte. A entrega reuniu o município, a Emater/RS e o Banrisul para fortalecer a agricultura familiar da Costa Doce. Apoio que chega na porteira de quem produz o alimento da nossa mesa.",
            "hashtags": ["#SãoLourençoDoSul", "#AgriculturaFamiliar", "#Emater", "#Agro", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Reforço para a agricultura familiar.",
            "desenvolvimento_45s": "Cinquenta famílias de São Lourenço do Sul receberam os cartões da primeira fase do Programa Operação Terra Forte. A entrega reuniu a administração municipal, a Emater do Rio Grande do Sul e o Banrisul, num esforço para fortalecer a agricultura familiar. Programas como esse facilitam o acesso a recursos para investir na produção, melhorar a renda no campo e manter as famílias na atividade, peça-chave para a economia dos municípios da Costa Doce.",
            "fechamento_8s": "Primeira fase já é realidade.",
            "cta_5s": "Confira no SulTV.",
            "trilha_sugerida": "instrumental campeiro leve"
        },
        "tag_thumbnail": "Operação Terra Forte",
        "briefing_visual": {
            "descricao_pt": "Pequena propriedade de agricultura familiar no Sul do Brasil com horta e plantação, dia claro, sem rostos identificáveis",
            "query_en": ["family farm small holding brazil", "smallholder vegetable farm", "rural family agriculture field"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A small family farm in southern Brazil with vegetable beds and crops under clear daylight, no identifiable faces, no brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato concreto, quantitativo e recente de apoio à agricultura familiar em cidade-núcleo (SLS), com instituições parceiras — perfil ideal da audiência SulTV"
    },

    # 15. Cristal — Av. Passo do Mendonça limpeza — REBAIXAR (já publicada em 31/05)
    "804da2cbe08274dd604274d8db6acc48cc218fed": _skip(
        "REBAIXAR",
        "Mesma pauta já publicada pelo Radar em 31/05 — dedup do histórico bloquearia; sem fato novo"
    ),

    # 16. Guaíba — Ginásio Vila Iolanda 91% — PUBLICAR nota_curta
    "9d5c35e9be86ae890a20d830c6145e4be5e610fc": {
        "titulo_sultv": "Ginásio da Vila Iolanda, em Guaíba, chega a 91% de obras e entra na reta final",
        "chamada_faixa": "Ginásio da Vila Iolanda em Guaíba a 91%",
        "subtitulo": "Obra em fase de acabamento amplia a estrutura esportiva do município com recursos públicos.",
        "lead": "A construção do Ginásio da Vila Iolanda, em Guaíba, chegou a 91% de execução e avança para a etapa final de acabamentos. O espaço amplia a estrutura esportiva do município e foi viabilizado com recursos públicos.",
        "ganchos_3": [
            "Obra do Ginásio da Vila Iolanda a 91% de conclusão",
            "Espaço entra na etapa final de acabamentos",
            "Novo equipamento esportivo para Guaíba"
        ],
        "angulo_editorial": "Investimento público e esporte comunitário na região metropolitana próxima à Costa Doce — fato concreto e quantitativo (91%), pauta positiva de serviço.",
        "fontes_complementares_sugeridas": ["Prefeitura de Guaíba", "Secretaria de Obras de Guaíba"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "O Ginásio da Vila Iolanda, em Guaíba, já está com 91% das obras concluídas e entra na reta final de acabamentos. Mais um espaço para o esporte e a comunidade, viabilizado com recursos públicos. A bola está quase pronta para rolar.",
            "hashtags": ["#Guaíba", "#Esporte", "#ObraPública", "#Comunidade", "#RS", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Novo ginásio em Guaíba.",
            "desenvolvimento_45s": "A construção do Ginásio da Vila Iolanda, em Guaíba, chegou a 91% e entra na etapa final de acabamentos. O novo espaço amplia a estrutura esportiva do município e foi viabilizado com recursos públicos. Equipamentos como esse atendem escolas, projetos sociais e o esporte amador do bairro, criando oportunidades para crianças e jovens.",
            "fechamento_8s": "Reta final de obras.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental enérgico leve"
        },
        "tag_thumbnail": "Ginásio Vila Iolanda",
        "briefing_visual": {
            "descricao_pt": "Construção de ginásio esportivo coberto em fase final de obras, estrutura metálica e quadra, sem pessoas",
            "query_en": ["sports gym construction interior", "covered court building site", "indoor arena construction"],
            "evitar": ["pessoas", "marcas", "texto", "logos"],
            "prompt_ia": "Interior of a covered sports gymnasium under final-stage construction, metal roof structure and concrete court, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Investimento público concreto e quantitativo (91%) em equipamento esportivo de Guaíba — pauta positiva de serviço"
    },

    # 17. Pelotas — edital de leilão Santander — BLOQUEAR
    "819d32a271bcac9bb069558c347f1a99683e55f0": _skip(
        "BLOQUEAR",
        "Edital de leilão de alienação fiduciária com nomes de partes privadas — procedural, regra de bloqueio de editais; risco de exposição de pessoa física"
    ),

    # 18. Pelotas — Dia de Combate ao Trabalho Infantil — REBAIXAR (cautela menores)
    "234a6969e7c00de1991dd10bc680dbcd6a755946": _skip(
        "REBAIXAR",
        "Pauta de conscientização relevante, mas envolve menores (guardrail) — por cautela vira nota interna em vez de matéria amplificada"
    ),

    # 19. Guaíba — 'Sabores de Guaíba' churrascaria — REBAIXAR
    "26af69553f9eace59585246f1178879d0a9caa90": _skip(
        "REBAIXAR",
        "Conteúdo de feature gastronômico com teor promocional de estabelecimento privado — não é hard news; vira nota"
    ),

    # 20. Pelotas/ALERS — concessões/privatizações/PPPs — REBAIXAR (política sensível)
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "REBAIXAR",
        "Manifestação de parlamentares sobre privatizações/plebiscito tangencia política partidária e polarização — vira nota interna por cautela"
    ),

    # 21. Pelotas/ALERS — Funcriança 'Valores que Ficam' — REBAIXAR
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR",
        "Pauta fiscal/administrativa (destinação ao Funcriança), de baixo apelo e tangenciando menores — vira nota interna"
    ),

    # 22. RS — 'INFORMAÇÕES AGROPECUÁRIAS' (header Emater) — BLOQUEAR
    "e914edb4101909198de490e19b4ee3ebeb063e57": _skip(
        "BLOQUEAR",
        "Título é cabeçalho de seção do informativo conjuntural ('INFORMAÇÕES AGROPECUÁRIAS') — raspagem de menu, não é matéria; bloqueio conhecido"
    ),

    # 23. RS — Onda de frio polar na semana — PUBLICAR materia_longa
    "892cde7b48dd63105d731d9788fe695189b3109d": {
        "titulo_sultv": "Massa de ar polar traz semana de frio intenso e madrugadas geladas no Sul",
        "chamada_faixa": "Semana de frio intenso no Sul do RS",
        "subtitulo": "Temperaturas devem ficar entre as mais baixas desde meados de maio, com risco de geada em diversas regiões.",
        "lead": "O Sul do Brasil entra em uma semana de frio intenso, com a chegada de uma massa de ar polar que deve derrubar as temperaturas a patamares não registrados desde meados de maio. As madrugadas mais geladas trazem risco de geada em diversas regiões do Rio Grande do Sul, exigindo atenção redobrada no campo e nas cidades.",
        "ganchos_3": [
            "Massa de ar polar derruba temperaturas no Sul",
            "Frio mais intenso desde meados de maio",
            "Risco de geada exige atenção no campo e nas cidades"
        ],
        "angulo_editorial": "Clima é serviço de altíssimo interesse no início do inverno — pauta de utilidade imediata para produtores e moradores; tom informativo, sem sensacionalismo, sem citação de veículo.",
        "fontes_complementares_sugeridas": ["Inmet", "Defesa Civil RS", "Emater/RS-Ascar"],
        "lead_materia_longa": "O Sul do Brasil entra em uma semana de frio intenso, com a chegada de uma massa de ar polar que deve derrubar as temperaturas a patamares não registrados desde meados de maio.",
        "post_instagram": {
            "caption": "Prepare o agasalho: uma massa de ar polar derruba as temperaturas no Sul nesta semana, com madrugadas entre as mais frias desde maio e risco de geada em várias regiões. No campo, atenção com animais, lavouras sensíveis e a água das tubulações. Nas cidades, cuidado redobrado com idosos e crianças.",
            "hashtags": ["#Frio", "#Inverno", "#Clima", "#Geada", "#RioGrandeDoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O frio chegou pra valer.",
            "desenvolvimento_45s": "Uma massa de ar polar avança sobre o Sul do Brasil e traz uma semana de frio intenso, com temperaturas não registradas desde meados de maio. As madrugadas mais geladas aumentam o risco de geada em diversas regiões do Rio Grande do Sul. No campo, é hora de redobrar a atenção com animais, lavouras sensíveis e o abastecimento de água. Nas cidades, o cuidado vale especialmente para idosos, crianças e pessoas em situação de rua.",
            "fechamento_8s": "Frio forte a semana toda.",
            "cta_5s": "Acompanhe o clima no SulTV.",
            "trilha_sugerida": "instrumental contemplativo"
        },
        "tag_thumbnail": "Onda de frio no Sul",
        "briefing_visual": {
            "descricao_pt": "Campo rural do Sul do Brasil coberto de geada ao amanhecer, capim branco e neblina baixa, sem pessoas",
            "query_en": ["frost covered field sunrise", "frosty pasture morning fog", "white frost grass winter"],
            "evitar": ["pessoas", "marcas", "texto", "logos"],
            "prompt_ia": "A rural field in southern Brazil covered with frost at sunrise, white frosted grass and low mist, cold blue light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima é pauta de altíssimo interesse no início do inverno — fato concreto e serviço de utilidade imediata para o campo e as cidades do RS"
    },

    # 24. RS — comportamento do tempo no Centro do Brasil — REBAIXAR (sem âncora Sul)
    "3b5074e66b1d09eda1f8dc861b2bcf3f9a9fd4a4": _skip(
        "REBAIXAR",
        "Pauta climática focada em Centro-Oeste/Sudeste, sem âncora no Sul — fora do recorte regional; vira nota interna"
    ),

    # 25. RS — jogador da seleção / Copa — REBAIXAR (nacional, sem âncora)
    "fd021710b9df63e6d77ba27406ea0519e1019446": _skip(
        "REBAIXAR",
        "Curiosidade esportiva nacional (Copa do Mundo) sem âncora regional Sul-RS — fora do recorte"
    ),

    # 26. Santa Maria — HUSM recebe profissionais angolanos — PUBLICAR post
    "64ff5a9766ff3a88e12044797b2fa33e2de1e24f": {
        "titulo_sultv": "Hospital Universitário de Santa Maria recebe 30 profissionais angolanos para formação",
        "chamada_faixa": "HUSM recebe 30 profissionais de Angola",
        "subtitulo": "Intercâmbio integra programa de cooperação Brasil-Angola em formação de recursos humanos em saúde.",
        "lead": "O Hospital Universitário de Santa Maria (HUSM) recebeu 30 profissionais angolanos para atividades de formação e estágios supervisionados. A iniciativa integra o Programa de Formação de Recursos Humanos em Saúde Brasil-Angola, que aproxima os dois países na qualificação de equipes.",
        "ganchos_3": [
            "30 profissionais angolanos em formação no HUSM",
            "Cooperação Brasil-Angola em saúde",
            "Santa Maria como polo de qualificação"
        ],
        "angulo_editorial": "Educação e saúde em cidade de peso na audiência (Santa Maria) — pauta institucional positiva de cooperação internacional; sem teor médico-prescritivo.",
        "fontes_complementares_sugeridas": ["HUSM", "UFSM", "Ebserh"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "O Hospital Universitário de Santa Maria recebeu 30 profissionais angolanos para atividades de formação e estágios supervisionados, dentro do Programa de Formação de Recursos Humanos em Saúde Brasil-Angola. Conhecimento que cruza o oceano e fortalece a saúde pública dos dois lados.",
            "hashtags": ["#SantaMaria", "#Saúde", "#HUSM", "#BrasilAngola", "#RS", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Santa Maria forma talentos de Angola.",
            "desenvolvimento_45s": "O Hospital Universitário de Santa Maria recebeu 30 profissionais angolanos para atividades de formação e estágios supervisionados. A iniciativa faz parte do Programa de Formação de Recursos Humanos em Saúde entre Brasil e Angola, e coloca Santa Maria como polo de qualificação em saúde. O intercâmbio fortalece equipes, troca experiências e amplia a capacidade dos sistemas públicos dos dois países.",
            "fechamento_8s": "Cooperação que transforma.",
            "cta_5s": "Veja no SulTV.",
            "trilha_sugerida": "instrumental institucional leve"
        },
        "tag_thumbnail": "HUSM Brasil-Angola",
        "briefing_visual": {
            "descricao_pt": "Corredor moderno de hospital universitário com profissionais de jaleco ao fundo desfocados, sem rostos identificáveis",
            "query_en": ["hospital corridor healthcare staff", "medical training hospital", "university hospital interior"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A modern university hospital corridor with blurred staff in white coats in the background, faces not identifiable, clean light, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta institucional positiva de cooperação internacional em cidade de peso na audiência (Santa Maria) — sem teor médico-prescritivo"
    },

    # 27. Rio Grande — entrega de óculos a estudantes — REBAIXAR
    "ed500fa1650f558d19912507960d8107c15b73b6": _skip(
        "REBAIXAR",
        "Programa social positivo, mas envolve estudantes (menores) e está fora do núcleo de cobertura prioritário — vira nota interna por cautela e quota"
    ),

    # 28. Cachoeira do Sul — BM apoia captação de órgãos — PUBLICAR post
    "64461abe7ef0b9a05ba5c6df355d6f7695a751b6": {
        "titulo_sultv": "Brigada Militar dá apoio à chegada de equipe médica para captação de órgãos em Cachoeira do Sul",
        "chamada_faixa": "BM apoia captação de órgãos em Cachoeira",
        "subtitulo": "Operação garantiu deslocamento rápido de equipe médica de Porto Alegre ao município.",
        "lead": "A Brigada Militar prestou apoio à chegada de uma equipe médica para a captação de órgãos em Cachoeira do Sul, no último sábado (13). A ação garantiu o deslocamento rápido e seguro dos profissionais vindos de Porto Alegre, etapa decisiva em processos de doação que dependem de agilidade.",
        "ganchos_3": [
            "Brigada Militar viabiliza logística de captação de órgãos",
            "Equipe médica chega de Porto Alegre a Cachoeira do Sul",
            "Agilidade que salva vidas na doação de órgãos"
        ],
        "angulo_editorial": "Serviço público e solidariedade — atuação institucional da Brigada Militar em ação que viabiliza doação de órgãos; pauta positiva, sensível e respeitosa, sem identificação de doador/receptor.",
        "fontes_complementares_sugeridas": ["Brigada Militar", "Central de Transplantes RS", "Santa Casa de Porto Alegre"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Em Cachoeira do Sul, a Brigada Militar prestou apoio à chegada de uma equipe médica para a captação de órgãos, garantindo um deslocamento rápido e seguro. Por trás de cada transplante existe uma corrida contra o tempo — e gestos como esse fazem a diferença entre uma vida que continua e uma que se perde. Seja doador: converse com a sua família.",
            "hashtags": ["#CachoeiraDoSul", "#DoaçãoDeÓrgãos", "#BrigadaMilitar", "#Solidariedade", "#RS", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Corrida contra o tempo que salva vidas.",
            "desenvolvimento_45s": "A Brigada Militar prestou apoio à chegada de uma equipe médica para a captação de órgãos em Cachoeira do Sul. A operação garantiu o deslocamento rápido e seguro dos profissionais vindos de Porto Alegre. Em processos de doação, cada minuto conta, e a logística integrada entre forças de segurança e equipes de saúde é o que viabiliza transplantes que dão nova chance a quem espera. Ser doador é um gesto que continua em outra vida.",
            "fechamento_8s": "Doar é um ato de amor.",
            "cta_5s": "Converse com sua família. Veja no SulTV.",
            "trilha_sugerida": "instrumental emotivo sóbrio"
        },
        "tag_thumbnail": "Apoio à doação de órgãos",
        "briefing_visual": {
            "descricao_pt": "Viatura policial com giroflex aceso em via, em apoio a deslocamento, ao entardecer, sem rostos identificáveis",
            "query_en": ["police escort vehicle lights", "emergency medical transport road", "patrol car emergency lights"],
            "evitar": ["rostos identificáveis", "marcas", "placas legíveis", "texto", "logos"],
            "prompt_ia": "A police patrol vehicle with active emergency lights escorting on a road at dusk, motion and urgency, no identifiable faces, no readable plates, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Ação institucional positiva da Brigada Militar viabilizando doação de órgãos — pauta de serviço e solidariedade, tratada com respeito e sem identificar doador/receptor"
    },

    # 29. Dom Feliciano — Expo Dom Feliciano (chamada a expositores) — REBAIXAR
    "6340d3559d8de7d9a39fd0359a8c6671cd6c985e": _skip(
        "REBAIXAR",
        "Chamada comercial a expositores ('essa é a sua chance') — teor publicitário; vira nota de agenda quando houver programação do evento"
    ),

    # 30. Mato Leitão — mutirão ressonância — REBAIXAR
    "b8e97115fbaf0b6d0ebd8b4d185d498c58a5172b": _skip(
        "REBAIXAR",
        "Serviço de saúde fora do núcleo de cobertura (região de Venâncio Aires), score baixo — vira nota interna"
    ),

    # 31. Venâncio Aires — projeto literário — REBAIXAR
    "1f0cd2e79bc7ad9dd67092fa09f19b5fafc05e4f": _skip(
        "REBAIXAR",
        "Pauta cultural de baixo apelo e fora do núcleo de cobertura — vira nota interna"
    ),

    # 32. Bento Gonçalves — Brasil x Marrocos — REBAIXAR (nacional)
    "2d870a9873d6a9e2393594ca9695f2fb86cd7083": _skip(
        "REBAIXAR",
        "Resultado de jogo da seleção (Copa do Mundo) — pauta nacional sem âncora regional; fora do recorte SulTV"
    ),

    # 33. Bento Gonçalves — homicídio com vítima nomeada — BLOQUEAR (guardrail)
    "991dbaa9fff99a1bd6a044a98be22f9815900ff0": _skip(
        "BLOQUEAR",
        "Guardrail: tragédia com vítima identificada (homicídio, nome próprio da vítima) — bloqueio automático"
    ),
}


MATERIAS = {
    "882edeb88f0be982907d48640a98bb6fe38fa6b1": """### Título ###
Camaquã lança Campanha do Agasalho 2026 e abre pontos de doação para o inverno

### Artigo ###
A Prefeitura de Camaquã lançou a Campanha do Agasalho 2026, mobilização que arrecada roupas, calçados e cobertores para apoiar famílias em situação de vulnerabilidade durante o inverno na região da Costa Doce. As ações foram apresentadas pelo secretário Fabiano Ribeiro, que destacou medidas voltadas não apenas ao atendimento imediato, mas também à promoção da autonomia das famílias atendidas. A campanha chega em um momento decisivo do calendário: o frio mais rigoroso do ano costuma se concentrar entre junho e agosto, quando a procura por agasalhos e roupas de cama cresce nos serviços de assistência social. A iniciativa convida moradores, empresas e entidades a doarem peças em bom estado, que serão triadas e distribuídas às famílias cadastradas nos serviços socioassistenciais do município. Cobertores, casacos, calçados fechados e roupas infantis estão entre os itens de maior necessidade nesta época. Além da arrecadação, a campanha reforça o trabalho contínuo da rede de proteção social, que acompanha famílias ao longo do ano e busca caminhos para que possam superar a situação de vulnerabilidade, com acesso a serviços, qualificação e geração de renda. Para colaborar, a orientação é procurar os pontos de coleta indicados pela Secretaria de Assistência Social e conferir os locais e horários de recebimento. Pequenos gestos, quando somados, transformam o inverno de quem mais precisa: um agasalho que sobra em um armário pode significar noites mais protegidas para uma família inteira em Camaquã.

### Legenda sugerida ###
Camaquã abre a Campanha do Agasalho 2026 com pontos de coleta de roupas, calçados e cobertores para o inverno.

### Palavras-chave ###
Camaquã, Campanha do Agasalho, doação, inverno, assistência social, solidariedade, Costa Doce, vulnerabilidade
""",

    "5b7dd5a19fab42dfa2fa1abff1b84af7bb5b3381": """### Título ###
Vereador aciona Anatel por falhas de telefonia e internet em Camaquã e região

### Artigo ###
O vereador Vladimir Tili acionou a Agência Nacional de Telecomunicações (Anatel) para cobrar providências diante das falhas recorrentes de telefonia móvel e internet em Camaquã e região. A solicitação encaminhada à agência reguladora pede esclarecimentos sobre a qualidade do serviço prestado e medidas para reduzir as instabilidades que afetam moradores, comércio e produtores rurais da Costa Doce. As quedas de sinal e a lentidão da conexão são reclamações frequentes em municípios do interior gaúcho, onde a cobertura nem sempre acompanha a expansão da demanda. Mais do que uma questão de conforto, a conectividade se tornou ferramenta essencial do dia a dia: o comércio depende de internet para vendas e pagamentos eletrônicos; serviços públicos e bancários migraram para plataformas digitais; e o próprio agronegócio usa aplicativos, sensores e sistemas de gestão que exigem sinal estável no campo. Quando a rede falha, paralisam-se desde uma simples transação até o monitoramento de uma lavoura. A Anatel é o órgão responsável por fiscalizar as operadoras e zelar pela qualidade dos serviços de telecomunicações no país, podendo cobrar das empresas planos de melhoria e, em casos de descumprimento, aplicar sanções. Ao formalizar a solicitação, o objetivo é colocar a situação de Camaquã e região no radar da agência e dar transparência às tratativas. A expectativa de moradores e do setor produtivo é que a cobrança resulte em melhorias concretas na infraestrutura e na estabilidade do sinal, garantindo um serviço à altura das necessidades da população.

### Legenda sugerida ###
Falhas de telefonia e internet em Camaquã e região são levadas à Anatel, com pedido de esclarecimentos e melhorias.

### Palavras-chave ###
Camaquã, Anatel, telefonia, internet, conectividade, serviço público, Costa Doce, telecomunicações
""",

    "efd8d70803038c24031276ce8b3cad9118f9fd60": """### Título ###
São Lourenço do Sul entrega cartões da primeira fase do Operação Terra Forte a 50 famílias

### Artigo ###
Cinquenta famílias de São Lourenço do Sul receberam, na última sexta-feira (12), os cartões da primeira fase do Programa Operação Terra Forte. A entrega reuniu a administração municipal, a Emater/RS-Ascar e o Banrisul, em ação voltada a fortalecer a agricultura familiar em uma das cidades-núcleo da Costa Doce, tradicional polo de produção de alimentos no Sul do estado. O programa direciona recursos e apoio técnico a produtores familiares, segmento responsável por boa parte dos alimentos que chegam às feiras e às mesas da região. Para quem trabalha em pequenas áreas, o acesso a crédito e a assistência técnica faz diferença direta na capacidade de investir na produção, melhorar a renda e permanecer na atividade — um desafio constante diante das oscilações de clima e de mercado. A presença da Emater/RS-Ascar reforça o componente de extensão rural da iniciativa, com orientação sobre manejo, diversificação de culturas e planejamento da propriedade. Já a parceria com o Banrisul viabiliza a parte financeira, por meio dos cartões entregues aos beneficiários. A entrega desta primeira fase sinaliza a continuidade do programa, que deve alcançar novos grupos de famílias nas próximas etapas. Em municípios onde a agricultura familiar sustenta a economia local, ações como essa têm efeito que vai além da porteira: mantêm famílias no campo, movimentam o comércio das cidades e ajudam a garantir o abastecimento regional. A administração municipal deve divulgar o cronograma das fases seguintes e as orientações para os produtores interessados nos canais oficiais.

### Legenda sugerida ###
Operação Terra Forte entrega cartões da primeira fase a 50 famílias da agricultura familiar em São Lourenço do Sul.

### Palavras-chave ###
São Lourenço do Sul, Operação Terra Forte, agricultura familiar, Emater, Banrisul, agro, Costa Doce, crédito rural
""",

    "892cde7b48dd63105d731d9788fe695189b3109d": """### Título ###
Massa de ar polar traz semana de frio intenso e madrugadas geladas no Sul

### Artigo ###
O Sul do Brasil entra em uma semana de frio intenso, com a chegada de uma massa de ar polar que deve derrubar as temperaturas a patamares não registrados desde meados de maio. As madrugadas mais geladas trazem risco de geada em diversas regiões do Rio Grande do Sul, exigindo atenção redobrada tanto no campo quanto nas cidades. O avanço do ar frio de origem polar é típico do auge do inverno gaúcho e costuma vir acompanhado de céu aberto e ventos que acentuam a sensação térmica. Nas áreas rurais, a geada é a principal preocupação: pode comprometer lavouras sensíveis, pastagens e hortaliças, além de exigir cuidados com a criação de animais, especialmente os mais jovens, e com o congelamento de bebedouros e tubulações. Produtores costumam reforçar a proteção de mudas, antecipar o manejo do rebanho e acompanhar de perto a previsão para reduzir perdas. Nas cidades, o frio mais severo acende o alerta para grupos vulneráveis. Idosos, crianças e pessoas com doenças respiratórias estão entre os mais afetados pelas baixas temperaturas, e a recomendação é manter ambientes aquecidos e bem ventilados, redobrar a atenção com o uso seguro de aquecedores e braseiros — que oferecem risco de incêndio e de intoxicação — e reforçar a solidariedade com pessoas em situação de rua. Beber líquidos quentes, agasalhar-se em camadas e proteger as extremidades do corpo são medidas simples que ajudam a atravessar a onda de frio. A orientação geral é acompanhar as atualizações da previsão ao longo da semana, já que a intensidade e a duração do frio podem variar conforme o deslocamento da massa de ar sobre a região.

### Legenda sugerida ###
Massa de ar polar derruba temperaturas no Sul nesta semana, com risco de geada no campo e alerta nas cidades.

### Palavras-chave ###
frio, massa de ar polar, geada, inverno, Rio Grande do Sul, clima, temperaturas, Sul do Brasil
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
                print(f"[angular] AVISO: {p['id_hash']} é PUBLICAR/materia_longa mas SEM texto em MATERIAS")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
