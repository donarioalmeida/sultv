#!/usr/bin/env python3
"""angular_hoje.py — angulação editorial Claude (sessão cowork) para 2026-06-29.
Lê state/aprovadas_<date>.json, grava state/pauta_<date>.json + matérias.
Respeita REGRA 12 (anti-menção a veículos) e quota 10/dia.
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
        "titulo_sultv": "", "subtitulo": "", "lead": "", "chamada_faixa": "",
        "ganchos_3": [], "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "", "decisao_final": decisao, "decisao_motivo": motivo,
    }


PAUTA_ANGULADA = {
    # ===== PUBLICAR (7 matérias longas) =====

    # #20 Produtores RS — renegociação de dívidas no Senado (agro RS)
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "titulo_sultv": "Produtores do RS temem que renegociação de dívidas rurais trave no Senado",
        "chamada_faixa": "Campo gaúcho teme travar crédito da safra",
        "subtitulo": "Setor receia ficar sem acesso ao crédito rural para a próxima safra caso a proposta não avance no Congresso.",
        "lead": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a votação da renegociação de dívidas no Senado e temem ficar sem acesso ao crédito rural para financiar a próxima safra — risco que atinge em cheio regiões produtoras como a Costa Doce, onde arroz e soja sustentam a economia de dezenas de municípios.",
        "ganchos_3": [
            "Renegociação de dívidas rurais aguarda votação no Senado",
            "Sem o acordo, produtores podem perder acesso ao crédito da safra",
            "Costa Doce, produtora de arroz e soja, está entre as regiões mais expostas"
        ],
        "angulo_editorial": "Economia do agro com impacto direto na audiência rural do RS; pauta concreta sobre crédito e safra, sem viés partidário. Atribuição a entidades do setor, sem menção a veículos.",
        "fontes_complementares_sugeridas": ["Farsul", "bancada gaúcha no Senado", "cooperativas de crédito rural"],
        "lead_materia_longa": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a votação da renegociação de dívidas no Senado e temem ficar sem acesso ao crédito rural para a próxima safra.",
        "post_instagram": {
            "caption": "O campo gaúcho está em alerta: a renegociação de dívidas rurais aguarda votação no Senado e, sem o acordo, muitos produtores podem ficar sem crédito para financiar a próxima safra. O risco pesa sobre regiões como a Costa Doce, onde arroz e soja movem a economia. O calendário agrícola não espera.",
            "hashtags": ["#Agro", "#RioGrandeDoSul", "#CréditoRural", "#Safra", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tensão no campo gaúcho.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul temem que a renegociação de dívidas trave no Senado. O principal receio do setor é ficar sem acesso ao crédito rural para financiar a próxima safra, depois de anos de estiagens e enchentes que comprometeram a capacidade de pagamento no campo. Em regiões produtoras como a Costa Doce, onde arroz e soja sustentam a economia, a definição do Congresso será decisiva para o planejamento da safra 2026/2027.",
            "fechamento_8s": "Decisão do Senado pode definir a próxima safra.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Crédito rural em risco",
        "briefing_visual": {
            "descricao_pt": "Lavoura de soja madura ao entardecer no Sul do Brasil, vista ampla, sem pessoas",
            "query_en": ["soybean field harvest sunset brazil", "soy crop golden hour", "agriculture field southern brazil"],
            "evitar": ["pessoas", "marcas", "texto", "logos"],
            "prompt_ia": "Wide shot of a mature soybean field at sunset in southern Brazil, golden light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Economia do agro de alto interesse para a audiência rural do RS; fato concreto (votação no Senado), âncora regional forte (Costa Doce)"
    },

    # #2 Nova ponte rural em Sertão Santana (agro/infra)
    "46d77822ff53c597dbceae9cf69a0b7ac5285bba": {
        "titulo_sultv": "Nova ponte em área rural de Sertão Santana melhora acesso e fortalece a agricultura",
        "chamada_faixa": "Ponte nova fortalece o agro em Sertão Santana",
        "subtitulo": "Obra conduzida pela Secretaria Municipal de Agricultura amplia o escoamento da produção e o deslocamento das famílias do interior.",
        "lead": "A Prefeitura de Sertão Santana, por meio da Secretaria Municipal de Agricultura, está construindo uma nova ponte em área rural do município para melhorar o acesso das comunidades do interior e fortalecer o setor agrícola da região.",
        "ganchos_3": [
            "Prefeitura constrói nova ponte em área rural de Sertão Santana",
            "Obra melhora o escoamento da produção agrícola",
            "Acesso facilita o deslocamento das famílias do interior"
        ],
        "angulo_editorial": "Infraestrutura rural com impacto direto no produtor; pauta concreta e positiva de cidade da Costa Doce ampliada. Atribuição à prefeitura.",
        "fontes_complementares_sugeridas": ["Prefeitura de Sertão Santana", "Secretaria Municipal de Agricultura"],
        "lead_materia_longa": "A Prefeitura de Sertão Santana, por meio da Secretaria Municipal de Agricultura, está construindo uma nova ponte em área rural do município para melhorar o acesso e fortalecer o setor agrícola.",
        "post_instagram": {
            "caption": "Sertão Santana ganha uma nova ponte em área rural. A obra da Secretaria Municipal de Agricultura melhora o acesso das comunidades do interior e fortalece o escoamento da produção — infraestrutura que faz a diferença no dia a dia de quem vive e trabalha no campo.",
            "hashtags": ["#SertãoSantana", "#Agro", "#InfraestruturaRural", "#CostaDoce", "#Agricultura", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Mais acesso no campo.",
            "desenvolvimento_45s": "A Prefeitura de Sertão Santana está construindo uma nova ponte em área rural do município, por meio da Secretaria Municipal de Agricultura. A obra vai melhorar o acesso das comunidades do interior, facilitar o deslocamento das famílias e fortalecer o escoamento da produção agrícola — um ganho concreto para quem depende das estradas rurais para trabalhar e vender o que produz.",
            "fechamento_8s": "Infraestrutura que fortalece o agro.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental otimista"
        },
        "tag_thumbnail": "Ponte rural nova",
        "briefing_visual": {
            "descricao_pt": "Ponte rural de concreto sobre arroio em estrada de terra no interior do Sul do Brasil, vegetação ao redor, sem pessoas",
            "query_en": ["rural concrete bridge dirt road", "countryside bridge stream brazil", "farm road bridge"],
            "evitar": ["pessoas", "marcas", "texto", "logos"],
            "prompt_ia": "A rural concrete bridge over a small stream on a dirt road in the southern Brazilian countryside, green vegetation around, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Infraestrutura rural concreta em cidade da cobertura; interesse direto do produtor, fonte institucional clara"
    },

    # #14 Cristal — melhorias em estradas do interior (núcleo)
    "01ef011ecdae21c60e1584906736e0e1b68bd082": {
        "titulo_sultv": "Cristal intensifica melhorias nas estradas do interior com cascalhamento e patrolamento",
        "chamada_faixa": "Cristal recupera estradas do interior",
        "subtitulo": "Serviços de cascalhamento e patrolamento atendem diferentes localidades e dão apoio às propriedades rurais do município.",
        "lead": "A Prefeitura de Cristal intensificou os trabalhos de manutenção nas estradas do interior, com serviços de cascalhamento e patrolamento em diferentes localidades e apoio às propriedades rurais — uma ação que melhora as condições de tráfego e o escoamento da produção no município da Costa Doce.",
        "ganchos_3": [
            "Prefeitura de Cristal recupera estradas do interior",
            "Serviços incluem cascalhamento e patrolamento",
            "Apoio às propriedades rurais em diversas localidades"
        ],
        "angulo_editorial": "Serviço público de utilidade direta ao produtor em cidade-núcleo; pauta concreta e positiva. Atribuição à prefeitura.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria de Obras de Cristal"],
        "lead_materia_longa": "A Prefeitura de Cristal intensificou os trabalhos de manutenção nas estradas do interior, com serviços de cascalhamento e patrolamento e apoio às propriedades rurais.",
        "post_instagram": {
            "caption": "Estradas do interior de Cristal recebem reforço: a prefeitura intensificou o cascalhamento e o patrolamento em diferentes localidades, com apoio às propriedades rurais. Estrada boa é produção que chega ao mercado e família que se desloca com segurança.",
            "hashtags": ["#Cristal", "#EstradasRurais", "#Agro", "#CostaDoce", "#Infraestrutura", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Estradas em recuperação.",
            "desenvolvimento_45s": "A Prefeitura de Cristal intensificou as melhorias nas estradas do interior do município. Os serviços incluem cascalhamento e patrolamento em diferentes localidades, além de apoio às propriedades rurais. Para o produtor da região, a manutenção das estradas representa mais segurança no deslocamento e facilidade no escoamento da produção até os pontos de venda.",
            "fechamento_8s": "Manutenção que apoia o campo.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental positivo"
        },
        "tag_thumbnail": "Estradas do interior",
        "briefing_visual": {
            "descricao_pt": "Motoniveladora trabalhando em estrada de terra rural no Sul do Brasil, campo ao redor, sem rostos identificáveis",
            "query_en": ["motor grader dirt road maintenance", "rural road grading gravel", "road machinery countryside"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A motor grader maintaining a rural dirt road in southern Brazil, open fields around, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público concreto em cidade-núcleo (Cristal) com impacto direto no produtor rural"
    },

    # #15 Cristal — programa Prepara RS (núcleo / clima)
    "9ce36499a218324114c169a9d64f04aae0558ec9": {
        "titulo_sultv": "Cristal integra o programa Prepara RS de prevenção a eventos climáticos extremos",
        "chamada_faixa": "Cristal entra no Prepara RS contra extremos",
        "subtitulo": "Lançamento apresentou ações e recursos para que os municípios se preparem para enchentes, estiagens e outros eventos extremos.",
        "lead": "O município de Cristal participou do lançamento do programa Prepara RS, iniciativa voltada à prevenção e à resposta a eventos climáticos extremos. O encontro apresentou ações e recursos para fortalecer a capacidade dos municípios da Costa Doce diante de enchentes, estiagens e temporais.",
        "ganchos_3": [
            "Cristal integra o programa estadual Prepara RS",
            "Foco em prevenção a enchentes, estiagens e temporais",
            "Programa oferece ações e recursos aos municípios"
        ],
        "angulo_editorial": "Resiliência climática regional, tema sensível para o RS após as enchentes recentes; pauta concreta de política pública preventiva. Atribuição ao programa estadual e à prefeitura.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Defesa Civil do RS", "programa Prepara RS"],
        "lead_materia_longa": "O município de Cristal participou do lançamento do programa Prepara RS, voltado à prevenção e à resposta a eventos climáticos extremos.",
        "post_instagram": {
            "caption": "Cristal entra no Prepara RS, programa estadual de prevenção a eventos climáticos extremos. O lançamento apresentou ações e recursos para que os municípios estejam mais preparados contra enchentes, estiagens e temporais. Depois do que o RS viveu, prevenção é prioridade.",
            "hashtags": ["#Cristal", "#PreparaRS", "#Clima", "#DefesaCivil", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Prevenção em primeiro lugar.",
            "desenvolvimento_45s": "O município de Cristal participou do lançamento do programa Prepara RS, voltado à prevenção e à resposta a eventos climáticos extremos. O encontro apresentou ações e recursos para que os municípios se preparem melhor para enchentes, estiagens e temporais. Para a Costa Doce, que sentiu de perto os efeitos dos últimos eventos climáticos, fortalecer a prevenção é uma agenda urgente.",
            "fechamento_8s": "Municípios mais preparados.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Prepara RS em Cristal",
        "briefing_visual": {
            "descricao_pt": "Rio cheio às margens de área rural no Sul do Brasil sob céu nublado, sem pessoas, clima de alerta",
            "query_en": ["river flood rural area cloudy", "swollen river floodplain brazil", "rural flooding prevention"],
            "evitar": ["pessoas", "marcas", "texto", "logos"],
            "prompt_ia": "A swollen river near rural land in southern Brazil under a cloudy sky, no people, sense of weather alert, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Política pública preventiva de resiliência climática em cidade-núcleo; tema de alta relevância pós-enchentes no RS"
    },

    # #13 São Lourenço do Sul — decreto horário Copa do Mundo (núcleo / serviço)
    "6efbfa9389c4b51a10c5e9449458fa3c97f3b5aa": {
        "titulo_sultv": "São Lourenço do Sul define horário especial de expediente durante a Copa do Mundo",
        "chamada_faixa": "São Lourenço muda expediente na Copa",
        "subtitulo": "Decreto municipal estabelece atendimento em horário excepcional nas repartições públicas nos dias de jogos.",
        "lead": "O Município de São Lourenço do Sul publicou decreto que estabelece horário excepcional de expediente nas repartições públicas municipais durante a Copa do Mundo FIFA 2026. A medida organiza o atendimento ao público nos dias de jogos e orienta servidores e moradores sobre o funcionamento dos serviços.",
        "ganchos_3": [
            "Decreto define horário especial nas repartições de São Lourenço do Sul",
            "Mudança vale para os dias de jogos da Copa do Mundo",
            "Medida organiza o atendimento ao público"
        ],
        "angulo_editorial": "Serviço de utilidade pública em cidade-núcleo; informação prática para o morador. Atribuição ao município (decreto).",
        "fontes_complementares_sugeridas": ["Prefeitura de São Lourenço do Sul"],
        "lead_materia_longa": "O Município de São Lourenço do Sul publicou decreto que estabelece horário excepcional de expediente nas repartições públicas municipais durante a Copa do Mundo FIFA 2026.",
        "post_instagram": {
            "caption": "Atenção, São Lourenço do Sul: a prefeitura publicou decreto com horário especial de expediente nas repartições públicas nos dias de jogos da Copa do Mundo. Antes de ir até um órgão municipal, confira o funcionamento para não perder a viagem.",
            "hashtags": ["#SãoLourençoDoSul", "#CopaDoMundo", "#ServiçoPúblico", "#CostaDoce", "#Utilidade", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Muda o expediente na Copa.",
            "desenvolvimento_45s": "O Município de São Lourenço do Sul publicou um decreto que define horário excepcional de expediente nas repartições públicas municipais durante a Copa do Mundo. A medida organiza o atendimento ao público nos dias de jogos. A orientação para o morador é conferir o funcionamento dos serviços antes de se deslocar até um órgão da prefeitura nessas datas.",
            "fechamento_8s": "Confira antes de ir.",
            "cta_5s": "Detalhes no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Expediente na Copa",
        "briefing_visual": {
            "descricao_pt": "Fachada de prédio público municipal no Sul do Brasil em dia claro, sem pessoas identificáveis",
            "query_en": ["city hall building facade brazil", "municipal government building", "public office building exterior"],
            "evitar": ["rostos identificáveis", "marcas", "texto legível", "logos"],
            "prompt_ia": "Facade of a municipal public building in southern Brazil on a clear day, no identifiable people, no readable text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de utilidade pública concreto (decreto) em cidade-núcleo; informação prática para o morador"
    },

    # #17 Pelotas — programa de Defesa Civil reconhecido nacionalmente
    "91178d18b7ebe1592878c085f2485d62b8a11da5": {
        "titulo_sultv": "Programa de Pelotas é reconhecido nacionalmente por reduzir riscos de desastres",
        "chamada_faixa": "Pelotas premiada por reduzir riscos",
        "subtitulo": "Iniciativa 'Pelotas sem risco, cidade resiliente', da Defesa Civil, foi destaque na Campanha Nacional Cidades sem Riscos.",
        "lead": "O programa 'Pelotas sem risco, cidade resiliente', conduzido pela Secretaria de Proteção e Defesa Civil de Pelotas, foi reconhecido neste sábado (27) durante a 9ª Campanha Nacional Cidades sem Riscos. O destaque valoriza ações de prevenção a desastres em um município que sentiu de perto os efeitos dos eventos climáticos recentes na Costa Doce.",
        "ganchos_3": [
            "Programa de Defesa Civil de Pelotas recebe reconhecimento nacional",
            "'Pelotas sem risco' é destaque na Campanha Cidades sem Riscos",
            "Ações de prevenção a desastres ganham visibilidade no país"
        ],
        "angulo_editorial": "Política pública de resiliência reconhecida nacionalmente, com âncora forte em Pelotas (Costa Doce ampliada); pauta positiva e relevante após as enchentes. Atribuição à Defesa Civil e à campanha nacional.",
        "fontes_complementares_sugeridas": ["Secretaria de Proteção e Defesa Civil de Pelotas", "Campanha Nacional Cidades sem Riscos"],
        "lead_materia_longa": "O programa 'Pelotas sem risco, cidade resiliente', da Secretaria de Proteção e Defesa Civil de Pelotas, foi reconhecido neste sábado (27) durante a 9ª Campanha Nacional Cidades sem Riscos.",
        "post_instagram": {
            "caption": "Reconhecimento nacional para Pelotas: o programa 'Pelotas sem risco, cidade resiliente', da Defesa Civil, foi destaque na 9ª Campanha Nacional Cidades sem Riscos. Prevenção a desastres é uma agenda séria — e a Costa Doce sabe disso melhor do que ninguém.",
            "hashtags": ["#Pelotas", "#DefesaCivil", "#Resiliência", "#Prevenção", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Pelotas no mapa nacional.",
            "desenvolvimento_45s": "O programa 'Pelotas sem risco, cidade resiliente', da Secretaria de Proteção e Defesa Civil, foi reconhecido na 9ª Campanha Nacional Cidades sem Riscos. O destaque valoriza as ações de prevenção a desastres desenvolvidas no município. Para a Costa Doce, que enfrentou de perto os efeitos dos eventos climáticos recentes, ver uma política de prevenção dar certo e ganhar reconhecimento é um sinal importante.",
            "fechamento_8s": "Prevenção que dá resultado.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental inspirador"
        },
        "tag_thumbnail": "Pelotas resiliente",
        "briefing_visual": {
            "descricao_pt": "Equipe de defesa civil com coletes em atividade de prevenção em área urbana no Sul do Brasil, sem rostos identificáveis em primeiro plano",
            "query_en": ["civil defense team vests city", "disaster prevention drill urban", "emergency response volunteers"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "Civil defense team in vests during a prevention activity in an urban area of southern Brazil, no identifiable faces in the foreground, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Política pública positiva com reconhecimento nacional, âncora forte em Pelotas; tema relevante de resiliência climática"
    },

    # #21 MP-RS — operação apreende produtos vencidos (segurança/consumo, RS)
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": {
        "titulo_sultv": "Operação do MP-RS apreende cinco toneladas de produtos vencidos em mercados gaúchos",
        "chamada_faixa": "MP-RS apreende 5 toneladas de vencidos",
        "subtitulo": "Fiscalização recolheu alimentos e bebidas impróprios em três estabelecimentos; um deles foi interditado e o responsável, preso.",
        "lead": "Uma operação de fiscalização do Ministério Público do Rio Grande do Sul apreendeu cerca de cinco toneladas de produtos vencidos e impróprios para consumo em três mercados gaúchos. Em um dos estabelecimentos, foram encontradas bebidas com prazo de validade vencido há nove anos, o que resultou em interdição total e na prisão do responsável.",
        "ganchos_3": [
            "MP-RS apreende cinco toneladas de produtos impróprios",
            "Bebidas vencidas há nove anos foram encontradas em um mercado",
            "Estabelecimento é interditado e responsável é preso"
        ],
        "angulo_editorial": "Defesa do consumidor e segurança alimentar em escopo estadual; ação concreta de fiscalização com fonte primária (MP-RS), sem identificação de pessoas além da informação oficial.",
        "fontes_complementares_sugeridas": ["Ministério Público do Rio Grande do Sul", "Vigilância Sanitária"],
        "lead_materia_longa": "Uma operação de fiscalização do Ministério Público do Rio Grande do Sul apreendeu cerca de cinco toneladas de produtos vencidos e impróprios para consumo em três mercados gaúchos.",
        "post_instagram": {
            "caption": "Cinco toneladas de produtos impróprios foram apreendidas pelo Ministério Público do RS em três mercados gaúchos. Em um deles, havia bebidas vencidas há nove anos — o estabelecimento foi interditado e o responsável, preso. Fique de olho: confira sempre a validade do que você compra.",
            "hashtags": ["#RioGrandeDoSul", "#DefesaDoConsumidor", "#MPRS", "#SegurançaAlimentar", "#Fiscalização", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cinco toneladas apreendidas.",
            "desenvolvimento_45s": "Uma operação de fiscalização do Ministério Público do Rio Grande do Sul apreendeu cerca de cinco toneladas de produtos vencidos e impróprios para consumo em três mercados gaúchos. Em um dos estabelecimentos, foram encontradas bebidas com validade vencida há nove anos. O local foi interditado e o responsável, preso. A orientação ao consumidor é simples: conferir sempre a data de validade e a procedência dos produtos antes de comprar.",
            "fechamento_8s": "Confira sempre a validade.",
            "cta_5s": "Detalhes no SulTV.",
            "trilha_sugerida": "instrumental tenso leve"
        },
        "tag_thumbnail": "Produtos vencidos apreendidos",
        "briefing_visual": {
            "descricao_pt": "Prateleiras de supermercado com produtos diversos, foco em embalagens, sem rostos de pessoas, luz de loja",
            "query_en": ["supermarket shelves products", "grocery store inspection shelf", "food products expiry date shelf"],
            "evitar": ["rostos de pessoas", "marcas legíveis", "texto", "logos"],
            "prompt_ia": "Supermarket shelves with assorted packaged products, focus on packaging, no people's faces, store lighting, no readable brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Defesa do consumidor com fato concreto e fonte primária (MP-RS); interesse amplo da audiência do RS"
    },

    # ===== REBAIXAR =====
    "ae275d114c829372c73d45a840c8d8c814a2e085": _skip(
        "REBAIXAR", "Perfil de personalidade com tema de saúde mental e figura/origem pouco verificáveis no insumo; risco de imprecisão e sensibilidade — vira nota interna"),
    "889cc3fdaaf2be558a8b64061fe7ade5341cc62b": _skip(
        "REBAIXAR", "Evento de conscientização já realizado (25/06) e de menor impacto noticioso; mantido como nota interna"),
    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": _skip(
        "REBAIXAR", "Nota técnica administrativa (poda/arborização) com título malformado pelo scraper; conteúdo procedural, sem matéria longa"),
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR", "Conteúdo procedural sobre destinação de recursos ao Funcriança; baixo apelo editorial, vira nota interna"),
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": _skip(
        "REBAIXAR", "Mesma temática de fiscalização/apreensão do item já selecionado (MP-RS); evita conteúdo duplicado-ish"),
    "c85ac3696d7da10929f8082aeb17de1ac01c2a0e": _skip(
        "REBAIXAR", "Pauta soft de educação ambiental fora das cidades-núcleo (Santa Maria); mantida como post potencial em nota interna"),
    "9f62b86b08e5c4a4aebd6000472ab5493fde551f": _skip(
        "REBAIXAR", "Pauta cultural soft fora das cidades-núcleo (Santa Maria); baixo apelo para a faixa do dia"),
    "61a29c9d85ffe07be2a0fad91d78c3eec17e4e62": _skip(
        "REBAIXAR", "Entrega de emendas por parlamentar nomeada — risco de viés político-partidário; vira nota interna"),
    "49d8f26a006c375064fb109752718bf3c4da0002": _skip(
        "REBAIXAR", "Ocorrência policial genérica fora das cidades-núcleo (Venâncio Aires); baixo impacto regional"),
    "d80aa939ff0d7bc5378f7a61cec90aff131525dd": _skip(
        "REBAIXAR", "Evento beneficente em instituição de oncologia (tema sensível de saúde) e fora do núcleo; mantido como nota interna"),
    "d626c194043c0c20a47d498151a08dc77688c793": _skip(
        "REBAIXAR", "Serviço de trânsito da BR-470 na Serra Gaúcha, distante do núcleo de cobertura Sul-RS; baixo interesse para a faixa"),

    # ===== BLOQUEAR =====
    "efeb2976a45a839ec9ac55c6321746031db2580d": _skip(
        "BLOQUEAR", "Onda de calor na Europa — pauta internacional sem âncora regional Sul-RS"),
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "BLOQUEAR", "Conteúdo desatualizado (inscrições de abril/2026); fora de janela editorial"),
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR", "Edital de penalidade — documento procedural, não é matéria"),
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR", "Edital de abertura de prazo — documento procedural, não é matéria"),
    "4a19f3b447abaaef75271b2e2dbf1a33ae46591b": _skip(
        "BLOQUEAR", "Título é cabeçalho/menu raspado pelo scraper; conteúdo procedural sem corpo aproveitável"),
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR", "Aviso de audiência pública — documento procedural"),
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR", "Comunicado administrativo sobre emissão de notas fiscais — procedural/serviço técnico"),
    "a6d042be95d54d6ef82415d825a77afc9d6fa43d": _skip(
        "BLOQUEAR", "Título é cabeçalho de seção (Conferência Municipal de Saúde) raspado como matéria"),
    "93d8797025ffe98d7c47bb3b29fd426a9dec54b2": _skip(
        "BLOQUEAR", "Título é cabeçalho de seção raspado pelo scraper; conteúdo malformado"),
    "0c78bd0cc00e7d0302fc635b3fdbfbd510252753": _skip(
        "BLOQUEAR", "Concurso público com data de classificação em maio — procedural e desatualizado"),
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "BLOQUEAR", "Debate sobre privatizações, concessões e plebiscito — terreno político-partidário sensível (guardrail)"),
    "6155a2f0ea3a2fcb746b6f464e72ec91a753436b": _skip(
        "BLOQUEAR", "Terremotos na Venezuela — pauta internacional sem âncora regional Sul-RS"),
}


MATERIAS = {
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS temem que renegociação de dívidas rurais trave no Senado

### Artigo ###
Produtores rurais do Rio Grande do Sul vivem dias de apreensão à espera da votação da renegociação de dívidas no Senado. O principal receio do setor é ficar sem acesso ao crédito rural para financiar a próxima safra — um risco que atinge em cheio regiões produtoras como a Costa Doce, onde o arroz e a soja sustentam a economia de dezenas de municípios. O endividamento do campo gaúcho se agravou nos últimos anos com a sucessão de eventos climáticos extremos: estiagens severas que quebraram safras consecutivas e, na sequência, as enchentes históricas que atingiram o estado. Sem conseguir honrar os compromissos das safras frustradas, muitos produtores acumularam parcelas e perderam a capacidade de tomar novos financiamentos, entrando em um ciclo que compromete o custeio do próximo plantio. A renegociação em discussão é vista pelas entidades do setor como condição para restabelecer a capacidade de pagamento e manter o produtor na atividade. Enquanto a votação não acontece, cresce a tensão no campo, porque o calendário agrícola não espera: as decisões sobre compra de insumos e financiamento da safra de verão precisam ser tomadas nos próximos meses. Lideranças do agronegócio gaúcho têm intensificado a interlocução com a bancada do estado em Brasília para dar celeridade à tramitação. O tema deve seguir no centro do debate econômico do agro nas próximas semanas, e o desfecho no Senado será decisivo para o planejamento da safra 2026/2027 no Rio Grande do Sul.

### Legenda sugerida ###
Campo gaúcho teme ficar sem crédito para a próxima safra caso a renegociação de dívidas não avance no Senado.

### Palavras-chave ###
renegociação de dívidas, crédito rural, Senado, Rio Grande do Sul, agro, safra, arroz, soja, Costa Doce
""",

    "46d77822ff53c597dbceae9cf69a0b7ac5285bba": """### Título ###
Nova ponte em área rural de Sertão Santana melhora acesso e fortalece a agricultura

### Artigo ###
A Prefeitura de Sertão Santana, por meio da Secretaria Municipal de Agricultura, está construindo uma nova ponte em uma área rural do município. A obra integra um conjunto de ações voltadas a melhorar a infraestrutura do interior e fortalecer o setor agrícola, que é a base da economia local. A nova estrutura vai facilitar o deslocamento das famílias que vivem e trabalham no campo, além de qualificar o escoamento da produção até os pontos de comercialização. Em municípios de perfil rural como Sertão Santana, na Costa Doce ampliada, as pontes e estradas do interior cumprem um papel decisivo: são por elas que passam o leite, os grãos, os insumos e o transporte escolar das comunidades mais afastadas. Quando uma travessia fica precária ou interditada, o prejuízo é imediato para quem produz e para quem precisa chegar à cidade. Com a nova ponte, a administração municipal busca dar mais segurança ao tráfego e reduzir o tempo de viagem entre as localidades rurais e a sede do município. A obra também representa um incentivo à permanência das famílias no campo, ao melhorar as condições de quem vive da agricultura. O investimento em infraestrutura rural costuma ter efeito multiplicador na economia local, ao baratear o transporte da produção e ampliar o acesso a serviços. A expectativa é de que a entrega da ponte beneficie diretamente as comunidades atendidas pela travessia e contribua para o desenvolvimento agrícola da região.

### Legenda sugerida ###
Obra da Secretaria Municipal de Agricultura melhora o acesso ao interior e o escoamento da produção em Sertão Santana.

### Palavras-chave ###
Sertão Santana, ponte rural, infraestrutura, agricultura, Costa Doce, estradas do interior, agro, escoamento da produção
""",

    "01ef011ecdae21c60e1584906736e0e1b68bd082": """### Título ###
Cristal intensifica melhorias nas estradas do interior com cascalhamento e patrolamento

### Artigo ###
A Prefeitura de Cristal intensificou os trabalhos de manutenção nas estradas do interior do município, com serviços de cascalhamento e patrolamento em diferentes localidades e apoio às propriedades rurais. As ações buscam melhorar as condições de tráfego nas vias não pavimentadas, que são essenciais para o dia a dia das comunidades do campo. Para o produtor rural de Cristal, na Costa Doce, a qualidade das estradas do interior tem efeito direto sobre a atividade econômica. É por essas vias que escoam a produção agrícola, circulam os insumos, passa o transporte escolar e se deslocam as famílias que precisam chegar à área urbana para acessar serviços de saúde, educação e comércio. Estradas em más condições encarecem o frete, aumentam o desgaste dos veículos e podem isolar localidades em períodos de chuva intensa. O cascalhamento reforça a superfície das vias e melhora a drenagem, reduzindo a formação de atoleiros, enquanto o patrolamento regulariza o leito da estrada e elimina buracos e ondulações. Combinados, os dois serviços ampliam a durabilidade das vias e a segurança de quem trafega por elas. O apoio às propriedades rurais complementa esse trabalho, com intervenções pontuais que facilitam o acesso a áreas produtivas. A manutenção das estradas do interior é uma demanda permanente em municípios de perfil agrícola, e a continuidade desses serviços ao longo do ano é o que garante condições estáveis de trânsito no campo, independentemente das variações do clima.

### Legenda sugerida ###
Cascalhamento e patrolamento reforçam as estradas do interior de Cristal e apoiam as propriedades rurais.

### Palavras-chave ###
Cristal, estradas do interior, cascalhamento, patrolamento, infraestrutura rural, Costa Doce, agro, propriedades rurais
""",

    "9ce36499a218324114c169a9d64f04aae0558ec9": """### Título ###
Cristal integra o programa Prepara RS de prevenção a eventos climáticos extremos

### Artigo ###
O município de Cristal participou do lançamento do programa Prepara RS, iniciativa voltada à prevenção e à resposta a eventos climáticos extremos. O encontro apresentou um conjunto de ações e recursos destinados a fortalecer a capacidade dos municípios de se anteciparem e reagirem a enchentes, estiagens, temporais e outros eventos que têm se tornado mais frequentes no Rio Grande do Sul. A adesão ao programa ganha peso especial na Costa Doce, região que sentiu de perto os efeitos dos eventos climáticos dos últimos anos. As enchentes que atingiram o estado expuseram a importância de estruturas de prevenção, de planos de contingência e de uma articulação eficiente entre as esferas municipal, estadual e federal nos momentos de crise. A proposta do Prepara RS é justamente reduzir a vulnerabilidade dos municípios antes que os desastres ocorram, com foco em planejamento, capacitação de equipes e disponibilização de recursos. Para a gestão municipal, integrar o programa significa ter acesso a ferramentas que ajudam a mapear áreas de risco, a organizar respostas mais rápidas e a proteger a população e a economia local. No campo, a prevenção a eventos extremos também é determinante: estiagens e enchentes afetam diretamente as safras, a infraestrutura rural e a renda das famílias produtoras. Ao se somar ao Prepara RS, Cristal reforça a agenda de resiliência climática que se tornou prioridade em todo o estado, transformando a experiência dos últimos anos em planejamento concreto para o futuro.

### Legenda sugerida ###
Cristal adere ao Prepara RS, programa estadual que reforça a prevenção a enchentes, estiagens e temporais.

### Palavras-chave ###
Cristal, Prepara RS, prevenção, eventos climáticos extremos, Defesa Civil, resiliência, Costa Doce, Rio Grande do Sul
""",

    "6efbfa9389c4b51a10c5e9449458fa3c97f3b5aa": """### Título ###
São Lourenço do Sul define horário especial de expediente durante a Copa do Mundo

### Artigo ###
O Município de São Lourenço do Sul publicou um decreto que estabelece horário excepcional de expediente nas repartições públicas municipais durante a Copa do Mundo FIFA 2026. A medida organiza o atendimento ao público nos dias de jogos e orienta tanto os servidores quanto a população sobre o funcionamento dos serviços nesse período. Ajustes de expediente durante grandes eventos esportivos são uma prática comum na administração pública, e têm como objetivo conciliar o interesse coletivo de acompanhar os jogos com a continuidade dos serviços essenciais à população. Na prática, isso significa que, nos dias de partidas, alguns setores podem funcionar em horários diferentes do habitual. Para o morador de São Lourenço do Sul, a principal recomendação é verificar o funcionamento dos órgãos municipais antes de se deslocar até uma repartição nos dias de jogos, evitando viagens desnecessárias e filas. Serviços de caráter essencial costumam ser preservados nesse tipo de decreto, mas a confirmação dos horários específicos de cada setor é o que garante que o cidadão seja atendido. A publicação do decreto antecipa a organização do calendário e dá previsibilidade ao atendimento, em um município da Costa Doce que, como tantos outros, vive o clima de Copa do Mundo. A orientação institucional reforça que a medida é temporária e vale apenas para o período do torneio, retornando o expediente ao funcionamento normal após o encerramento dos jogos.

### Legenda sugerida ###
Decreto estabelece horário excepcional nas repartições de São Lourenço do Sul nos dias de jogos da Copa do Mundo.

### Palavras-chave ###
São Lourenço do Sul, Copa do Mundo, expediente, repartições públicas, decreto, serviço público, Costa Doce
""",

    "91178d18b7ebe1592878c085f2485d62b8a11da5": """### Título ###
Programa de Pelotas é reconhecido nacionalmente por reduzir riscos de desastres

### Artigo ###
O programa "Pelotas sem risco, cidade resiliente", conduzido pela Secretaria de Proteção e Defesa Civil de Pelotas, foi reconhecido neste sábado (27) durante a 9ª Campanha Nacional Cidades sem Riscos. O destaque valoriza as ações de prevenção a desastres desenvolvidas no município e coloca Pelotas como referência em uma agenda que se tornou central no Rio Grande do Sul. O reconhecimento tem peso simbólico e prático para a Costa Doce ampliada, região que sentiu de perto os efeitos dos eventos climáticos extremos dos últimos anos. As enchentes que atingiram o estado evidenciaram a importância de políticas de prevenção estruturadas, capazes de mapear áreas de risco, preparar a população e organizar respostas rápidas em situações de emergência. Programas voltados à resiliência urbana atuam justamente nessa frente: antecipam-se aos desastres em vez de apenas reagir a eles. Isso envolve obras de contenção, sistemas de alerta, planos de evacuação, capacitação de equipes e trabalho de conscientização junto às comunidades mais expostas. Quando bem executadas, essas ações reduzem perdas materiais e, sobretudo, salvam vidas. O reconhecimento nacional de uma iniciativa local serve de incentivo para que outros municípios da região avancem em suas próprias estratégias de prevenção. Em um cenário de mudanças climáticas, em que eventos extremos tendem a se tornar mais frequentes e intensos, investir em resiliência deixou de ser opção e passou a ser necessidade. O caso de Pelotas mostra que o planejamento preventivo, somado ao engajamento da comunidade, é capaz de produzir resultados concretos e de ganhar visibilidade para além das fronteiras do estado.

### Legenda sugerida ###
Iniciativa da Defesa Civil de Pelotas é destaque na 9ª Campanha Nacional Cidades sem Riscos.

### Palavras-chave ###
Pelotas, Defesa Civil, cidade resiliente, prevenção de desastres, Cidades sem Riscos, resiliência, Costa Doce
""",

    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": """### Título ###
Operação do MP-RS apreende cinco toneladas de produtos vencidos em mercados gaúchos

### Artigo ###
Uma operação de fiscalização do Ministério Público do Rio Grande do Sul apreendeu cerca de cinco toneladas de produtos vencidos e impróprios para consumo em três mercados gaúchos. Entre os itens recolhidos havia alimentos e bebidas com prazo de validade expirado, alguns deles guardados em condições inadequadas. Em um dos estabelecimentos fiscalizados, foram localizadas bebidas com validade vencida há nove anos, o que levou à interdição total do local e à prisão do responsável. A ação integra o trabalho permanente de proteção ao consumidor e de garantia da segurança alimentar, áreas em que a fiscalização cumpre papel essencial. A comercialização de produtos vencidos ou armazenados de forma irregular representa risco direto à saúde da população, já que alimentos impróprios podem causar intoxicações e outras complicações. A retirada desses itens de circulação evita que cheguem à mesa do consumidor. Casos como esse reforçam a importância de o consumidor adotar cuidados básicos no momento da compra: conferir sempre a data de validade, observar as condições de armazenamento e a integridade das embalagens, e desconfiar de preços muito abaixo do mercado. Diante de qualquer irregularidade, o cidadão pode acionar os órgãos de defesa do consumidor e a vigilância sanitária. As apreensões e a interdição mostram que a fiscalização está atenta e que estabelecimentos que descumprem as normas estão sujeitos a sanções que vão da retirada dos produtos à interdição e à responsabilização criminal. A expectativa é de que as investigações tenham continuidade para apurar a origem dos produtos e eventuais outras irregularidades.

### Legenda sugerida ###
Fiscalização recolhe cinco toneladas de produtos impróprios em três mercados; um local é interditado e o responsável, preso.

### Palavras-chave ###
Ministério Público, MP-RS, produtos vencidos, segurança alimentar, defesa do consumidor, fiscalização, Rio Grande do Sul
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
            angul = _skip("BLOQUEAR", "Sem angulação configurada — descartado por guardrail editorial")
            angul["titulo_sultv"] = (item.get("titulo") or "")[:100]
        else:
            angul = PAUTA_ANGULADA[h]
        if angul["decisao_final"] == "PUBLICAR" and pub_count >= 10:
            angul = {**angul, "decisao_final": "REBAIXAR", "decisao_motivo": "Quota diária de 10 publicações esgotada"}
        if angul["decisao_final"] == "PUBLICAR":
            pub_count += 1
        # promover formato a materia_longa para PUBLICAR que tenham matéria
        merged = {**item, **angul}
        if merged["decisao_final"] == "PUBLICAR" and h in MATERIAS:
            merged["formato_sugerido"] = "materia_longa"
        pauta.append(merged)

    out = {"data": HOJE, "gerado_em": datetime.now(timezone.utc).isoformat(),
           "total": len(pauta), "pauta": pauta}
    pauta_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[angular] pauta -> {pauta_path}")
    print("[angular] decisões:", Counter(p["decisao_final"] for p in pauta))

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
                print(f"[angular] AVISO: {p['id_hash']} PUBLICAR/materia_longa sem texto")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
