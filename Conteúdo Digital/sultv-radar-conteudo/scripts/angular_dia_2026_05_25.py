#!/usr/bin/env python3
"""
angular_dia_2026_05_25.py — angulação editorial + redação (cowork-faz-tudo).

Lê state/aprovadas_2026-05-25.json, gera state/pauta_2026-05-25.json com
angulação + decisao_final, e escreve state/materias_2026-05-25/<id_hash>.md
para cada item PUBLICAR com formato materia_longa OU nota_curta.

Decisões do dia (14 aprovados):
  PUBLICAR (7): Arambaré cursos (longa), Cristal Av. Passo do Mendonça (longa),
                Pelotas Castramóvel (longa), Cristal ponto facultativo (nota),
                FETAG dumping leite (post), Venâncio Dia do Desafio (post),
                Venâncio Corsan ruas (post)
  REBAIXAR (3): FETAG mobilização fumicultores (raso), Bento/TJRS (Serra),
                Bento/IR 2026 (nacional)
  BLOQUEAR (4): Pelotas header "Desenvolvimento/Inovação" (#carouselNews),
                Emater "INFORMAÇÕES AGROPECUÁRIAS" header, Farsul Flickr,
                Defesa Civil "Avisos e Alertas" header
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-05-25"


PAUTA_ANGULADA = {
    # 1. Arambaré cursos gratuitos — PUBLICAR (núcleo, materia_longa)
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

    # 2. Cristal — Avenida Passo do Mendonça — PUBLICAR (núcleo, materia_longa)
    "804da2cbe08274dd604274d8db6acc48cc218fed": {
        "titulo_sultv": "Avenida Passo do Mendonça recebe limpeza e reorganização após pavimentação em Cristal",
        "subtitulo": "Serviços no canteiro central encerram pacote de melhorias na via, em cidade-núcleo da Costa Doce.",
        "lead": "A Prefeitura de Cristal concluiu serviços de limpeza e reorganização na Avenida Passo do Mendonça, com intervenções no canteiro central que finalizam o pacote de melhorias iniciado com a pavimentação da via. A obra reforça a agenda de infraestrutura urbana na cidade.",
        "ganchos_3": [
            "Canteiro central recebe reorganização",
            "Etapa final após a pavimentação da avenida",
            "Infraestrutura urbana avança em Cristal",
        ],
        "angulo_editorial": "Pauta de infraestrutura urbana em cidade-núcleo (Cristal), com fato concreto de conclusão de obra — utilidade direta e valorização do espaço público para a audiência da Costa Doce.",
        "fontes_complementares_sugeridas": ["Secretaria de Obras de Cristal", "Câmara de Cristal"],
        "lead_materia_longa": "A Avenida Passo do Mendonça, em Cristal, no Sul do Rio Grande do Sul, recebeu serviços de limpeza e reorganização que encerram o pacote de melhorias da via.",
        "post_instagram": {
            "caption": "A Avenida Passo do Mendonça, em Cristal, recebeu limpeza e reorganização do canteiro central — etapa final das melhorias após a pavimentação.",
            "hashtags": ["#Cristal", "#CostaDoce", "#SulTV", "#Infraestrutura", "#ObrasRS"],
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal finaliza melhorias na avenida.",
            "desenvolvimento_45s": "A Prefeitura de Cristal concluiu os serviços de limpeza e reorganização na Avenida Passo do Mendonça. As ações no canteiro central finalizam o pacote de melhorias iniciado com a pavimentação da via, que se tornou um dos principais corredores da cidade. A intervenção busca melhorar a mobilidade, a segurança e a aparência do espaço público, em uma agenda de infraestrutura urbana acompanhada de perto pela comunidade.",
            "fechamento_8s": "Obra encerra etapa de melhorias na via.",
            "cta_5s": "Cobertura completa no SulTV.",
            "trilha_sugerida": "instrumental neutro",
        },
        "tag_thumbnail": "Cristal conclui obra",
        "briefing_visual": {
            "descricao_pt": "Avenida pavimentada recém-reformada com canteiro central organizado em cidade pequena do Sul do RS, vista de rua ao nível do solo, sem pessoas identificáveis",
            "query_en": ["newly paved avenue median strip", "small town main street brazil", "urban road landscaping"],
            "evitar": ["rostos identificáveis", "placas de carro legíveis", "logos", "texto"],
            "prompt_ia": "Wide street-level shot of a newly paved avenue with a tidy landscaped central median in a small southern Brazilian town, clear daylight, no readable text, no logos, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cidade-núcleo (Cristal) com obra concluída — fato concreto de infraestrutura",
    },

    # 3. Pelotas — header "Desenvolvimento, Empreendedorismo e Inovação" — BLOQUEAR
    "da39a3ee5e6b4b0d3255bfef95601890afd80709": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Título é cabeçalho de seção do portal de Pelotas e URL inválida (#carouselNews) — coletor pegou menu, não matéria",
    },

    # 4. Pelotas — Castramóvel — PUBLICAR (Costa Doce ampliada, materia_longa)
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

    # 5. Cristal — ponto facultativo Corpus Christi — PUBLICAR (nota_curta)
    "f627cc1c2a9732aca6846189a5bfb42f1535d1d3": {
        "titulo_sultv": "Cristal terá ponto facultativo nos dias 4 e 5 de junho por causa de Corpus Christi",
        "subtitulo": "Repartições municipais ficam sem atendimento na quinta e na sexta; serviços essenciais seguem mantidos.",
        "lead": "A Prefeitura de Cristal definiu por decreto ponto facultativo nos dias 4 e 5 de junho, em razão do feriado de Corpus Christi. Nas datas, o atendimento nas repartições municipais fica suspenso, retornando à normalidade na semana seguinte.",
        "ganchos_3": [
            "Ponto facultativo na quinta e na sexta",
            "Repartições sem atendimento ao público",
            "Serviços essenciais seguem funcionando",
        ],
        "angulo_editorial": "Nota de serviço em cidade-núcleo (Cristal): informa o cidadão sobre funcionamento do poder público no feriado de Corpus Christi — utilidade prática direta.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Atenção, Cristal: a Prefeitura decretou ponto facultativo nos dias 4 e 5 de junho, por causa de Corpus Christi. Programe-se — serviços essenciais seguem mantidos.",
            "hashtags": ["#Cristal", "#CostaDoce", "#SulTV", "#CorpusChristi", "#Serviço"],
        },
        "roteiro_short_60s": {},
        "tag_thumbnail": "Cristal: feriado prolongado",
        "formato_sugerido": "nota_curta",
        "briefing_visual": {
            "descricao_pt": "Fachada de prédio público municipal fechado no interior do RS, calendário de feriado, sem pessoas identificáveis",
            "query_en": ["closed city hall building", "public holiday calendar", "municipal government building facade"],
            "evitar": ["rostos identificáveis", "logos partidários", "texto legível"],
            "prompt_ia": "Wide shot of a small municipal government building facade in southern Brazil on a quiet holiday morning, closed doors, soft daylight, no readable text, no logos, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Nota de serviço em cidade-núcleo (Cristal) — utilidade prática sobre funcionamento no feriado",
    },

    # 6. Emater — INFORMAÇÕES AGROPECUÁRIAS — BLOQUEAR (cabeçalho de seção)
    "e914edb4101909198de490e19b4ee3ebeb063e57": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Título é cabeçalho de seção do site Emater ('INFORMAÇÕES AGROPECUÁRIAS') — coletor pegou menu, não matéria",
    },

    # 7. Farsul — Fotos do Flickr — BLOQUEAR (galeria + parceiro)
    "54da86550dbad394c36708a7a9c2f7ad94d48e38": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Agregador de fotos do Flickr (Farsul) — não é matéria; Farsul é parceiro estratégico",
    },

    # 8. Defesa Civil — Avisos e Alertas — BLOQUEAR (cabeçalho de seção)
    "72da33ff967bd936651054a9f0405448f2ba54dd": {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Cabeçalho de seção da Defesa Civil ('Avisos e Alertas / Dicas de prevenção') com conteúdo procedural antigo (09/05) — não é matéria",
    },

    # 9. FETAG — mobilização fumicultores — REBAIXAR (raso)
    "f9f92856df490e0e556bb546df4a224e030bb4c6": {
        "titulo_sultv": "FETAG-RS organiza mobilização em defesa dos fumicultores",
        "subtitulo": "Entidade prepara ato setorial; tema exige confirmação de data, local e pauta em fonte primária.",
        "lead": "A FETAG-RS anunciou organização de mobilização em defesa dos fumicultores gaúchos. O conteúdo coletado é apenas a chamada da entidade, sem detalhamento — requer apuração de data, local e reivindicações antes de publicação.",
        "ganchos_3": [
            "Mobilização setorial em organização",
            "Fumicultura é cadeia relevante no RS",
            "Pauta econômica do agro familiar",
        ],
        "angulo_editorial": "Tema econômico legítimo da agricultura familiar gaúcha (fumicultura), mas a fonte traz apenas a manchete ('Ver mais'). Conservar como nota interna e confirmar com a FETAG antes de qualquer publicação.",
        "fontes_complementares_sugeridas": ["FETAG-RS", "Afubra"],
        "lead_materia_longa": "",
        "post_instagram": {},
        "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Conteúdo raso (só manchete 'Ver mais') — exige apuração de detalhes em fonte primária antes de publicar",
    },

    # 10. FETAG — dumping leite em pó — PUBLICAR (post_instagram)
    "121db834b930dd25ee20d7080d1a9a842104aafb": {
        "titulo_sultv": "FETAG-RS aponta dumping em importações de leite em pó",
        "subtitulo": "Entidade reforça denúncia sobre concorrência desleal que pressiona produtores gaúchos.",
        "lead": "A FETAG-RS voltou a apontar a prática de dumping nas importações de leite em pó, denúncia que a entidade afirma sustentar há anos. O tema atinge diretamente a competitividade dos produtores de leite do Rio Grande do Sul.",
        "ganchos_3": [
            "Denúncia de concorrência desleal",
            "Pressão sobre o preço pago ao produtor",
            "Cadeia do leite gaúcha em alerta",
        ],
        "angulo_editorial": "Pauta econômica do agro com impacto direto no produtor gaúcho de leite — tema recorrente e relevante para a base rural da audiência. Como a fonte é uma chamada curta, publicar como post de redes, sem matéria longa, até confirmação detalhada.",
        "fontes_complementares_sugeridas": ["FETAG-RS", "Sindilat-RS", "Emater RS"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "A FETAG-RS reforça a denúncia de dumping nas importações de leite em pó — prática de concorrência desleal que pressiona o preço pago ao produtor gaúcho. Um tema que mexe direto com o bolso de quem está na lida do leite no RS.",
            "hashtags": ["#Leite", "#AgroRS", "#SulTV", "#FETAG", "#Pecuária", "#RioGrandeDoSul"],
        },
        "roteiro_short_60s": {},
        "tag_thumbnail": "Leite em pó sob pressão",
        "briefing_visual": {
            "descricao_pt": "Vacas leiteiras em pasto no Sul do RS ou sala de ordenha de pequena propriedade rural, sem pessoas identificáveis",
            "query_en": ["dairy cows pasture brazil", "milk production farm", "dairy cattle field"],
            "evitar": ["rostos identificáveis", "marcas de laticínio", "texto", "logos"],
            "prompt_ia": "Wide shot of dairy cows grazing in a green pasture on a small farm in southern Brazil, soft morning light, no readable text, no logos, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta econômica do agro de alto interesse para o produtor de leite gaúcho — publicar como post de redes",
    },

    # 11. Venâncio Aires — Dia do Desafio / agasalhos — PUBLICAR (post_instagram)
    "6772d862dd126bedeadebdbae083ac687b5101ae": {
        "titulo_sultv": "Dia do Desafio terá ponto de arrecadação de agasalhos em Venâncio Aires",
        "subtitulo": "Coleta acontece na quarta-feira (27), das 8h às 17h, na Travessa São Sebastião Mártir.",
        "lead": "Venâncio Aires terá um ponto de arrecadação de agasalhos na próxima quarta-feira (27), durante o Dia do Desafio. A coleta funcionará das 8h às 17h, na Travessa São Sebastião Mártir, e reforça a campanha do agasalho em pleno inverno gaúcho.",
        "ganchos_3": [
            "Coleta de agasalhos na quarta (27)",
            "Das 8h às 17h, na Travessa São Sebastião Mártir",
            "Dia do Desafio mobiliza a comunidade",
        ],
        "angulo_editorial": "Pauta de comunidade e solidariedade com dados concretos (data, horário e local), ligada à campanha do agasalho no inverno — interesse direto da audiência local.",
        "fontes_complementares_sugeridas": ["Prefeitura de Venâncio Aires", "Sesc RS"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "No Dia do Desafio, Venâncio Aires terá ponto de arrecadação de agasalhos nesta quarta (27), das 8h às 17h, na Travessa São Sebastião Mártir. Frio gaúcho passa — o gesto de solidariedade fica.",
            "hashtags": ["#VenâncioAires", "#CampanhaDoAgasalho", "#SulTV", "#DiaDoDesafio", "#Solidariedade", "#RS"],
        },
        "roteiro_short_60s": {},
        "tag_thumbnail": "Agasalhos em Venâncio",
        "briefing_visual": {
            "descricao_pt": "Caixas e peças de roupas de inverno dobradas em ponto de arrecadação comunitário, agasalhos empilhados, sem pessoas identificáveis",
            "query_en": ["winter clothing donation drive", "donated coats boxes", "warm clothes charity collection"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Wide shot of folded winter coats and blankets stacked at a community donation point indoors, warm light, no readable text, no logos, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta de comunidade/solidariedade com dados concretos (data, hora, local) — interesse local direto",
    },

    # 12. Venâncio Aires — Corsan / intervenções nas ruas — PUBLICAR (post_instagram)
    "d8cbc17399e781607b17f876081441859947bba4": {
        "titulo_sultv": "Corsan faz intervenções e paradas programadas de água em Venâncio Aires nesta semana",
        "subtitulo": "Obras interrompem o trânsito em alguns pontos e afetam o abastecimento no bairro Coronel Brito.",
        "lead": "A Corsan realiza nesta semana intervenções em ruas de Venâncio Aires, com obras que interrompem o trânsito em alguns pontos. Estão previstas, ainda, paradas programadas de abastecimento de água no bairro Coronel Brito.",
        "ganchos_3": [
            "Obras interrompem o trânsito em pontos da cidade",
            "Paradas programadas de água no Coronel Brito",
            "Moradores devem se programar para a semana",
        ],
        "angulo_editorial": "Nota de serviço urbano (trânsito + abastecimento) com utilidade prática imediata para o morador de Venâncio Aires — alerta de impacto no dia a dia.",
        "fontes_complementares_sugeridas": ["Corsan", "Prefeitura de Venâncio Aires"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Atenção, Venâncio Aires: a Corsan faz intervenções em ruas da cidade esta semana, com trânsito interrompido em alguns pontos e paradas programadas de água no bairro Coronel Brito. Se programe e guarde uma reserva de água.",
            "hashtags": ["#VenâncioAires", "#Corsan", "#SulTV", "#Serviço", "#Abastecimento", "#RS"],
        },
        "roteiro_short_60s": {},
        "tag_thumbnail": "Obras e água em Venâncio",
        "briefing_visual": {
            "descricao_pt": "Equipe de obras de saneamento trabalhando em via urbana com sinalização de trânsito, escavação de rua, sem rostos identificáveis",
            "query_en": ["road works water pipe street", "utility roadwork sign", "street excavation infrastructure"],
            "evitar": ["rostos identificáveis", "placas de carro legíveis", "marcas", "texto"],
            "prompt_ia": "Wide shot of a sanitation roadwork site on an urban street with traffic cones and an excavation, daytime, no readable text, no logos, editorial photojournalism style",
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço urbano (trânsito + abastecimento) com utilidade prática imediata para o morador",
    },

    # 13. Bento Gonçalves — estudantes visitam TJRS — REBAIXAR (Serra, fora do núcleo)
    "b3d685f0873e10e0037b1541667f2f178fb9efe7": {
        "titulo_sultv": "Estudantes de Direito de Bento Gonçalves visitam o TJRS",
        "subtitulo": "Visita pelo programa Portas Abertas reuniu cerca de 80 acadêmicos em Porto Alegre.",
        "lead": "Cerca de 80 estudantes de Direito de Bento Gonçalves e de Santiago visitaram o Tribunal de Justiça do RS pelo programa Portas Abertas. A atividade tem caráter educativo e institucional.",
        "ganchos_3": ["Programa Portas Abertas do TJRS", "80 estudantes de Direito", "Educação e instituições"],
        "angulo_editorial": "Pauta educativa/institucional positiva, mas em cidade da Serra (Bento Gonçalves), fora do núcleo SulTV (Sul do RS / Costa Doce). Ancoragem regional fraca — nota interna.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {},
        "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Cidade da Serra (Bento Gonçalves) fora do núcleo Sul-RS — ancoragem regional fraca",
    },

    # 14. Bento Gonçalves — Imposto de Renda 2026 — REBAIXAR (nacional)
    "cac628941b10d7f9477431c340b44c47f6c81f08": {
        "titulo_sultv": "Última semana para declarar o Imposto de Renda 2026",
        "subtitulo": "Receita Federal ainda aguarda cerca de 13 milhões de declarações até o fim do prazo.",
        "lead": "A Receita Federal ainda espera cerca de 13 milhões de declarações do Imposto de Renda 2026 na última semana do prazo. O tema tem alcance nacional, sem recorte regional específico do Sul do RS.",
        "ganchos_3": ["Prazo final do IR 2026", "13 milhões de declarações pendentes", "Serviço de utilidade nacional"],
        "angulo_editorial": "Serviço de utilidade pública, porém de natureza nacional e sem ângulo Sul-RS — republicado por veículo da Serra. Mantém como nota interna; eventual uso como card de serviço genérico.",
        "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "",
        "post_instagram": {},
        "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Pauta nacional (Receita Federal) sem ancoragem Sul-RS",
    },
}


MATERIAS = {
    # Arambaré cursos (materia_longa)
    "e370728cabf9868c99ea7f3a5323d444ac76d0dd": """### Título ###
Arambaré abre inscrições para cursos gratuitos de qualificação profissional na Costa Doce

### Artigo ###
A Prefeitura de Arambaré, no Sul do Rio Grande do Sul, abriu inscrições para um pacote de cursos gratuitos de qualificação profissional voltado para moradores da cidade. As vagas são limitadas e contemplam diferentes áreas técnicas, com aulas previstas para iniciar nas próximas semanas em espaço cedido pelo poder público municipal. A iniciativa integra a estratégia da gestão para ampliar oportunidades de renda na Costa Doce, região marcada pela combinação entre economia rural, turismo de praia e pesca artesanal. Ao oferecer capacitação sem custo, o município busca conectar a mão de obra local a setores em demanda, como comércio, serviços e cadeia produtiva. A medida também responde à sazonalidade da economia em Arambaré, em que a oferta de trabalho varia ao longo do ano, e tenta reduzir a dependência de períodos específicos como o veraneio. Para se inscrever, os interessados devem procurar a Secretaria responsável pela política de trabalho e renda na Prefeitura. A documentação e os critérios de seleção estão disponíveis nos canais oficiais do município. Cursos gratuitos de qualificação profissional vêm sendo apontados como uma das ferramentas mais efetivas para melhorar a empregabilidade em cidades pequenas, sobretudo quando articulados com instituições parceiras e com as demandas reais do mercado regional. A expectativa da Prefeitura é que o programa se consolide como ciclo permanente, integrando novas turmas ao longo do ano. A iniciativa reforça o protagonismo de Arambaré na pauta de desenvolvimento humano da Costa Doce e mostra a preocupação do poder público com a geração de renda em uma região estratégica para o Sul do estado.

### Legenda sugerida ###
Prefeitura de Arambaré abre vagas em cursos gratuitos de qualificação profissional para moradores da Costa Doce.

### Palavras-chave ###
Arambaré, cursos gratuitos, qualificação profissional, Costa Doce, geração de renda, Prefeitura de Arambaré, Sul do RS
""",

    # Cristal - Avenida Passo do Mendonça (materia_longa)
    "804da2cbe08274dd604274d8db6acc48cc218fed": """### Título ###
Avenida Passo do Mendonça recebe limpeza e reorganização após pavimentação em Cristal

### Artigo ###
A Prefeitura de Cristal, no Sul do Rio Grande do Sul, concluiu serviços de limpeza e reorganização na Avenida Passo do Mendonça, com intervenções no canteiro central que encerram o pacote de melhorias iniciado com a pavimentação da via. As ações marcam a etapa final de uma obra que transformou um dos principais corredores urbanos da cidade, ampliando as condições de tráfego e a aparência do espaço público. A pavimentação de vias é, em municípios da Costa Doce, uma das demandas mais sentidas pela população, tanto pela mobilidade quanto pelo impacto direto no escoamento da produção, no acesso a serviços e na valorização dos imóveis no entorno. A reorganização do canteiro central, agora finalizada, contempla limpeza, ajuste de áreas verdes e melhoria da sinalização, elementos que contribuem para a segurança de motoristas e pedestres. Esse tipo de intervenção costuma ser percebida pela comunidade como sinal de cuidado com o patrimônio público e de continuidade das políticas de infraestrutura. Para a gestão municipal, encerrar o ciclo de melhorias da avenida representa entregar à população uma via plenamente requalificada, capaz de atender ao fluxo crescente de veículos e de integrar bairros ao centro da cidade. A expectativa é que a requalificação sirva de referência para futuras obras em outras vias de Cristal, dentro de uma agenda de infraestrutura urbana que tem ganhado espaço entre as prioridades do município. A conclusão dos serviços também reforça a importância do planejamento por etapas, em que a pavimentação é seguida por ações complementares de manutenção e organização do espaço, garantindo durabilidade ao investimento realizado.

### Legenda sugerida ###
Avenida Passo do Mendonça, em Cristal, conclui pacote de melhorias com limpeza e reorganização do canteiro central.

### Palavras-chave ###
Cristal, Avenida Passo do Mendonça, pavimentação, infraestrutura urbana, obras, Costa Doce, Sul do RS, Prefeitura de Cristal
""",

    # Pelotas - Castramóvel (materia_longa)
    "32fa7b18a1d1dc1f7406f06e90b3c9aaf9b32701": """### Título ###
Castramóvel de Pelotas atende Passo do Salso e Vila Governaço com 200 vagas de castração gratuita

### Artigo ###
A Prefeitura de Pelotas vai levar o Castramóvel aos bairros Passo do Salso e Vila Governaço, com 200 vagas para castração gratuita de cães e gatos. O cadastro dos interessados será realizado entre os dias 25 e 29 de maio, e as vagas são limitadas. O serviço integra a política municipal de bem-estar e controle populacional animal, conduzida pela área de qualidade ambiental. A castração gratuita é uma das ferramentas mais eficientes no combate ao abandono e à superpopulação de animais nas cidades. Ao impedir ninhadas indesejadas, o procedimento reduz o número de animais em situação de rua, diminui riscos sanitários para a população e alivia a pressão sobre protetores independentes e organizações de defesa animal, que costumam operar no limite da capacidade. A escolha de bairros específicos para cada etapa do programa busca democratizar o acesso, levando o atendimento a regiões onde a demanda é alta e a oferta de serviços veterinários acessíveis é menor. O modelo itinerante, com a unidade móvel, permite atender comunidades que dificilmente se deslocariam a uma clínica central. Para participar, os tutores precisam realizar o cadastro dentro do prazo, respeitando os critérios definidos pela Prefeitura quanto a peso, idade e condições de saúde dos animais. As orientações sobre jejum, transporte e cuidados pós-operatórios costumam ser repassadas no momento do cadastro. Programas como esse vêm sendo ampliados em diversas cidades gaúchas como resposta estruturada a um problema crônico de saúde pública e proteção animal. Em Pelotas, a continuidade do Castramóvel sinaliza que o controle populacional deixou de ser ação pontual para se tornar política permanente, com cronograma rotativo entre bairros.

### Legenda sugerida ###
Castramóvel de Pelotas oferece 200 vagas de castração gratuita no Passo do Salso e na Vila Governaço; cadastro de 25 a 29 de maio.

### Palavras-chave ###
Pelotas, Castramóvel, castração gratuita, saúde animal, proteção animal, controle populacional, Costa Doce, Sul do RS
""",

    # Cristal - ponto facultativo Corpus Christi (nota_curta)
    "f627cc1c2a9732aca6846189a5bfb42f1535d1d3": """### Título ###
Cristal terá ponto facultativo nos dias 4 e 5 de junho por causa de Corpus Christi

### Artigo ###
A Prefeitura de Cristal, no Sul do Rio Grande do Sul, estabeleceu por decreto ponto facultativo nos dias 4 e 5 de junho, em razão do feriado de Corpus Christi. Nas duas datas, o atendimento ao público nas repartições municipais ficará suspenso, com retorno à normalidade na semana seguinte. A medida cria, na prática, um período prolongado de pausa no funcionamento administrativo da Prefeitura. Serviços considerados essenciais, como os de saúde de urgência e plantões obrigatórios, costumam ser preservados nesse tipo de decreto, e a recomendação é que o cidadão verifique antecipadamente o funcionamento de cada setor antes de se deslocar. A orientação vale especialmente para quem depende de atendimentos presenciais, emissão de documentos ou protocolos junto ao município. Decretos de ponto facultativo em datas próximas a feriados são comuns na administração pública e têm como objetivo organizar a rotina dos servidores e o atendimento à população. Para a comunidade de Cristal, a informação serve de alerta para programar com antecedência demandas que dependam das repartições municipais nesses dias.

### Legenda sugerida ###
Prefeitura de Cristal decreta ponto facultativo em 4 e 5 de junho por Corpus Christi; repartições ficam sem atendimento.

### Palavras-chave ###
Cristal, ponto facultativo, Corpus Christi, feriado, Prefeitura de Cristal, serviço, Costa Doce, Sul do RS
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
                "decisao_motivo": "Sem angulação configurada — descartado pelo guardrail",
            }
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
    print(f"[angular] decisões:", Counter(p["decisao_final"] for p in pauta))

    materias_dir.mkdir(exist_ok=True)
    nwrite = 0
    for p in pauta:
        if p["decisao_final"] == "PUBLICAR" and p.get("formato_sugerido") in ("materia_longa", "nota_curta"):
            corpo = MATERIAS.get(p["id_hash"])
            if corpo:
                f = materias_dir / f"{p['id_hash']}.md"
                f.write_text(corpo, encoding="utf-8")
                nwrite += 1
                print(f"[angular] matéria -> {f.name} ({len(corpo)} chars)")
            else:
                print(f"[angular] AVISO: PUBLICAR {p.get('formato_sugerido')} sem corpo: {p['id_hash']}")
    print(f"[angular] {nwrite} matérias escritas em {materias_dir}")


if __name__ == "__main__":
    main()
