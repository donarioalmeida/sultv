# -*- coding: utf-8 -*-
"""Angulação editorial Cowork — 2026-06-12. Gerado pelo Claude na sessão."""
import json, os
from datetime import datetime, timezone

HOJE = "2026-06-12"
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APROV = os.path.join(BASE, "state", f"aprovadas_{HOJE}.json")
OUT_PAUTA = os.path.join(BASE, "state", f"pauta_{HOJE}.json")
OUT_DIR = os.path.join(BASE, "state", f"materias_{HOJE}")
os.makedirs(OUT_DIR, exist_ok=True)

d = json.load(open(APROV))
items = d if isinstance(d, list) else d.get("aprovadas", d.get("itens", []))

A = {}

# ---- BLOQUEADOS ----
A[0] = dict(decisao_final="BLOQUEAR", decisao_motivo="Esporte internacional (Copa do Mundo) sem âncora regional — falso positivo de cidade pela conta IG.")
A[1] = dict(decisao_final="BLOQUEAR", decisao_motivo="Pauta internacional (EUA/Texas) sem âncora regional Sul-RS.")
A[10] = dict(decisao_final="BLOQUEAR", decisao_motivo="PAD sigiloso envolvendo servidora de escola de educação infantil — caso sensível com possível envolvimento de menores, sem fato apurado.")
A[13] = dict(decisao_final="BLOQUEAR", decisao_motivo="Comunicado procedural antigo (05/05) sobre emissor de notas fiscais — sem fato novo.")
A[40] = dict(decisao_final="BLOQUEAR", decisao_motivo="Guardrail: tema envolve abuso sexual infantojuvenil — conteúdo envolvendo menores.")
A[41] = dict(decisao_final="BLOQUEAR", decisao_motivo="Guardrail saúde médica: oferta de contraceptivo com indicação de faixa etária e uso.")
A[42] = dict(decisao_final="BLOQUEAR", decisao_motivo="Esporte nacional/internacional (jogos da Copa) sem âncora regional.")

# ---- REBAIXADOS com motivo específico ----
A[3] = dict(decisao_final="REBAIXAR", decisao_motivo="Pauta soft de educação fiscal escolar — boa, mas fora da quota de 10 PUBLICAR do dia.")
A[12] = dict(decisao_final="REBAIXAR", decisao_motivo="Aviso de audiência pública — registro em nota interna.")
A[15] = dict(decisao_final="REBAIXAR", decisao_motivo="Recadastramento de servidores — aviso administrativo interno.")
A[16] = dict(decisao_final="REBAIXAR", decisao_motivo="Campanha institucional da gestão sobre finanças municipais em contexto de questionamento político — evitar porta-voz de gestão.")
A[26] = dict(decisao_final="REBAIXAR", decisao_motivo="Pauta estadual de renegociação de dívidas sem âncora Costa Doce; material de veículo parceiro exige retrabalho integral — acompanhar desdobramento.")

# ---- PUBLICADOS (10) ----

A[2] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Obra concreta de segurança viária em cidade-núcleo, fonte primária (Prefeitura de Tapes).",
    titulo_sultv="Tapes instala lombadas de borracha para reforçar a segurança no trânsito",
    subtitulo="Primeira estrutura foi implantada em frente à escola Vicentina, na entrada do município",
    lead="A Prefeitura de Tapes iniciou a instalação de lombadas de borracha em pontos estratégicos da cidade para ampliar a segurança de motoristas e pedestres.",
    chamada_faixa="LOMBADAS NOVAS NO TRÂNSITO DE TAPES",
    ganchos_3=["Primeira lombada em frente à escola Vicentina", "Faixa de pedestres revitalizada e nova sinalização", "Ação integra pacote de segurança viária"],
    angulo_editorial="Serviço ao morador: onde estão as novas lombadas, por que foram instaladas e o que muda para quem dirige em Tapes.",
    fontes_complementares_sugeridas=["Secretaria Municipal de Obras de Tapes", "Departamento de Trânsito de Tapes"],
    lead_materia_longa="A primeira lombada de borracha de Tapes foi instalada em frente à escola Vicentina, na entrada do município, dentro de um conjunto de medidas de segurança viária da prefeitura.",
    post_instagram=dict(caption="Tapes começou a instalar lombadas de borracha em pontos estratégicos da cidade. A primeira ficou em frente à escola Vicentina, na entrada do município, junto com faixa de pedestres revitalizada e nova sinalização. A medida busca proteger motoristas e pedestres.", hashtags=["tapes", "transito", "segurancaviaria", "costadoce", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Lombadas novas no trânsito de Tapes", desenvolvimento_45s="A prefeitura iniciou a instalação de lombadas de borracha em pontos estratégicos. A primeira foi implantada em frente à escola Vicentina, na entrada da cidade, com revitalização da faixa de pedestres e placas de sinalização.", fechamento_8s="A ação faz parte de um pacote de segurança viária.", cta_5s="Siga a SulTV para mais notícias da Costa Doce.", trilha_sugerida="neutra informativa"),
    tag_thumbnail="TRÂNSITO",
    briefing_visual=dict(
        descricao_pt="Lombada de borracha preta e amarela instalada em rua de cidade pequena brasileira, perto de faixa de pedestres, sem pessoas",
        query_en=["rubber speed bump street", "speed bump crosswalk road", "traffic calming residential street"],
        evitar=["rostos identificáveis", "placas de veículos legíveis", "logos", "texto"],
        prompt_ia="Black and yellow rubber speed bump on a small-town Brazilian street near a pedestrian crosswalk, daylight, no people, no text, editorial photojournalism style",
    ),
)

A[4] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Evento comunitário com data, hora e local em cidade-núcleo (Arambaré).",
    titulo_sultv="Festa Junina de Arambaré acontece dia 27 de junho no Loteamento Popular",
    subtitulo="Programação inicia às 16h com apresentações do CRAS e das escolas; show da Banda Balada VIP às 19h",
    lead="A Festa Junina de Arambaré será realizada no dia 27 de junho, a partir das 16h, no Loteamento Popular, com programação para toda a família.",
    chamada_faixa="FESTA JUNINA DE ARAMBARÉ DIA 27",
    ganchos_3=["Programação a partir das 16h no Loteamento Popular", "Apresentações do CRAS e das escolas do município", "Show com a Banda Balada VIP às 19h"],
    angulo_editorial="Agenda cultural da Costa Doce: o que vai ter, onde e a que horas — serviço completo para a comunidade programar a família.",
    fontes_complementares_sugeridas=["Prefeitura de Arambaré", "CRAS de Arambaré"],
    lead_materia_longa="A Festa Junina de Arambaré já tem data marcada: 27 de junho, a partir das 16h, no Loteamento Popular, com apresentações das escolas, atividades do CRAS e show da Banda Balada VIP às 19h.",
    post_instagram=dict(caption="Anota na agenda: a Festa Junina de Arambaré será no dia 27 de junho, a partir das 16h, no Loteamento Popular. Tem apresentações do CRAS e das escolas, diversão para a família e show com a Banda Balada VIP às 19h. 🌽🔥", hashtags=["arambare", "festajunina", "costadoce", "cultura", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Festa Junina de Arambaré tem data marcada", desenvolvimento_45s="Dia 27 de junho, a partir das 16h, no Loteamento Popular. A programação tem apresentações do CRAS e das escolas do município, diversão para toda a família e show com a Banda Balada VIP às 19h.", fechamento_8s="Prepare o traje e reúna a família.", cta_5s="SulTV, a TV da nossa região.", trilha_sugerida="festiva junina"),
    tag_thumbnail="FESTA JUNINA",
    briefing_visual=dict(
        descricao_pt="Decoração de festa junina com bandeirinhas coloridas e fogueira ao entardecer em praça de cidade do interior, sem pessoas identificáveis",
        query_en=["festa junina flags decoration", "june festival brazil bonfire", "colorful bunting party outdoor"],
        evitar=["rostos identificáveis", "marcas", "texto"],
        prompt_ia="Colorful festa junina flags and decorations at dusk in a small Brazilian town square, warm bonfire light, no people, no text, editorial photojournalism style",
    ),
)

A[5] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Obra de pavimentação confirmada em cidade-núcleo via convênio estadual (Pavimenta 3).",
    titulo_sultv="Rua Gustavo Emílio, em Arambaré, será pavimentada pelo programa Pavimenta 3",
    subtitulo="Convênio entre Governo do Estado e prefeitura garante blocos intertravados de concreto na via",
    lead="A Rua Gustavo Emílio, em Arambaré, foi contemplada pelo programa Pavimenta 3, convênio entre o Governo do Estado do Rio Grande do Sul e a prefeitura.",
    chamada_faixa="RUA GUSTAVO EMÍLIO SERÁ PAVIMENTADA",
    ganchos_3=["Convênio do programa estadual Pavimenta 3", "Pavimentação em blocos intertravados de concreto", "Mais mobilidade e qualidade de vida no bairro"],
    angulo_editorial="Infraestrutura que chega na ponta: qual rua, qual programa paga e o que muda para o morador de Arambaré.",
    fontes_complementares_sugeridas=["Prefeitura de Arambaré", "Governo do Estado do RS"],
    lead_materia_longa="A Rua Gustavo Emílio, em Arambaré, foi contemplada com pavimentação pelo programa Pavimenta 3, fruto de convênio entre o Governo do Estado do Rio Grande do Sul e a Prefeitura de Arambaré.",
    post_instagram=dict(caption="Boa notícia para Arambaré: a Rua Gustavo Emílio foi contemplada pelo programa Pavimenta 3, convênio entre o Governo do Estado e a prefeitura. A obra será em blocos intertravados de concreto, trazendo mais mobilidade e qualidade de vida para a comunidade.", hashtags=["arambare", "pavimentacao", "infraestrutura", "costadoce", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Pavimentação nova chegando em Arambaré", desenvolvimento_45s="A Rua Gustavo Emílio foi contemplada pelo programa Pavimenta 3, convênio entre o Governo do Estado e a prefeitura. A obra será executada com blocos intertravados de concreto, garantindo mais mobilidade e acessibilidade.", fechamento_8s="Mais uma obra de infraestrutura para a cidade.", cta_5s="Acompanhe a SulTV.", trilha_sugerida="institucional otimista"),
    tag_thumbnail="OBRAS",
    briefing_visual=dict(
        descricao_pt="Pavimentação de rua com blocos intertravados de concreto em cidade pequena, blocos empilhados e via em obra, sem pessoas",
        query_en=["interlocking concrete pavers street", "paving blocks road construction", "brick road small town"],
        evitar=["rostos", "logos de empresas", "texto"],
        prompt_ia="Interlocking concrete paver blocks being laid on a small-town Brazilian street, stacked pavers beside the road, daylight, no people, no text, editorial photojournalism style",
    ),
)

A[6] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Passo concreto (medição) para asfaltamento em área central de cidade-núcleo (Cristal).",
    titulo_sultv="Cristal avança nos estudos para asfaltar rua que contorna a Praça Os Pioneiros",
    subtitulo="Prefeitura realizou a medição da via no Centro; praça vem recebendo série de melhorias",
    lead="A Prefeitura de Cristal realizou a medição da rua que contorna a Praça Os Pioneiros, no Centro, etapa dos estudos para futuras melhorias de infraestrutura, incluindo o possível asfaltamento da via.",
    chamada_faixa="ASFALTO EM ESTUDO NO CENTRO DE CRISTAL",
    ganchos_3=["Medição da via já foi realizada", "Possibilidade de asfaltamento no entorno da praça", "Espaço tradicional vem recebendo revitalização"],
    angulo_editorial="O que está sendo planejado para o coração de Cristal: etapa atual, próximos passos e o histórico de melhorias na praça.",
    fontes_complementares_sugeridas=["Prefeitura de Cristal"],
    lead_materia_longa="A rua que contorna a Praça Os Pioneiros, no Centro de Cristal, passou por medição realizada pela prefeitura — mais um passo nos estudos para melhorias de infraestrutura que incluem a possibilidade de asfaltamento da via.",
    post_instagram=dict(caption="A Prefeitura de Cristal realizou a medição da rua que contorna a Praça Os Pioneiros, no Centro. É mais um passo nos estudos para melhorias de infraestrutura no local, incluindo a possibilidade de asfaltamento. A praça, palco dos grandes eventos da cidade, vem recebendo uma série de revitalizações.", hashtags=["cristal", "infraestrutura", "costadoce", "obras", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Asfalto novo em estudo no Centro de Cristal", desenvolvimento_45s="A prefeitura mediu a rua que contorna a Praça Os Pioneiros, espaço mais tradicional da cidade. A etapa faz parte dos estudos para melhorias que incluem o possível asfaltamento da via, somando-se à revitalização que a praça vem recebendo.", fechamento_8s="A SulTV acompanha os próximos passos.", cta_5s="Siga a SulTV.", trilha_sugerida="institucional leve"),
    tag_thumbnail="OBRAS",
    briefing_visual=dict(
        descricao_pt="Praça arborizada de cidade pequena do interior gaúcho com rua de entorno, vista ampla, sem pessoas identificáveis",
        query_en=["small town square trees brazil", "town plaza street around", "public square aerial small town"],
        evitar=["rostos", "marcas", "texto"],
        prompt_ia="Tree-lined central square of a small town in southern Brazil with the surrounding street visible, soft afternoon light, no people, no text, editorial photojournalism style",
    ),
)

A[7] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Recursos novos para projetos sociais em cidade-núcleo (Cristal), fato concreto com beneficiários definidos.",
    titulo_sultv="Cristal tem projetos contemplados pelo Fundo Social Sicredi",
    subtitulo="Recursos vão para iniciativas de educação, cultura e assistência social no município",
    lead="O município de Cristal teve projetos contemplados pelo Fundo Social Sicredi, com recursos destinados a ações de educação, cultura e assistência social.",
    chamada_faixa="FUNDO SOCIAL CONTEMPLA PROJETOS DE CRISTAL",
    ganchos_3=["Projetos de educação, cultura e assistência social", "Benefício direto a crianças, jovens e famílias", "Programa investe em iniciativas comunitárias"],
    angulo_editorial="Dinheiro novo para o social: quais áreas recebem, quem é beneficiado e como o programa funciona na prática.",
    fontes_complementares_sugeridas=["Prefeitura de Cristal", "Sicredi"],
    lead_materia_longa="Projetos de Cristal foram contemplados pelo Fundo Social Sicredi, programa que apoia ações de interesse coletivo, com recursos destinados às áreas de educação, cultura e assistência social do município.",
    post_instagram=dict(caption="Cristal teve projetos contemplados pelo Fundo Social Sicredi. Os recursos vão para iniciativas de educação, cultura e assistência social, beneficiando diretamente crianças, jovens e famílias do município. 📑", hashtags=["cristal", "fundosocial", "comunidade", "costadoce", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Projetos de Cristal contemplados por fundo social", desenvolvimento_45s="Os recursos do Fundo Social Sicredi vão para ações de educação, cultura e assistência social, beneficiando crianças, jovens e famílias. O programa investe em projetos comunitários voltados ao desenvolvimento local.", fechamento_8s="Mais investimento social chegando à Costa Doce.", cta_5s="Acompanhe a SulTV.", trilha_sugerida="institucional otimista"),
    tag_thumbnail="COMUNIDADE",
    briefing_visual=dict(
        descricao_pt="Crianças de costas ou mãos em atividade educativa com materiais de pintura e cadernos em ambiente comunitário, sem rostos",
        query_en=["children hands painting craft", "community center activity table", "school supplies education hands"],
        evitar=["rostos de crianças", "logos", "texto legível"],
        prompt_ia="Hands of children doing arts and crafts at a community center table in Brazil, colorful materials, no faces, no text, editorial photojournalism style",
    ),
)

A[8] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Programa público de saúde com fato concreto (formação do 1º grupo) em cidade-núcleo (Chuvisca); sem prescrição médica.",
    titulo_sultv="Chuvisca forma primeiro grupo do Programa de Controle do Tabagismo",
    subtitulo="Iniciativa da Secretaria de Saúde conta com equipe multiprofissional de apoio aos participantes",
    lead="A Prefeitura de Chuvisca, por meio da Secretaria Municipal de Saúde, realizou a formação do primeiro grupo do Programa de Controle do Tabagismo no município.",
    chamada_faixa="CHUVISCA LANÇA GRUPO CONTRA O TABAGISMO",
    ganchos_3=["Primeiro grupo do programa formado no município", "Equipe multiprofissional acompanha os participantes", "Promoção de saúde e qualidade de vida"],
    angulo_editorial="Saúde pública que chega perto: como funciona o grupo, quem acompanha e como o morador pode participar.",
    fontes_complementares_sugeridas=["Secretaria Municipal de Saúde de Chuvisca"],
    lead_materia_longa="O primeiro grupo do Programa de Controle do Tabagismo de Chuvisca foi formado nesta semana pela Secretaria Municipal de Saúde, com acompanhamento de equipe multiprofissional.",
    post_instagram=dict(caption="Chuvisca formou o primeiro grupo do Programa de Controle do Tabagismo. A iniciativa da Secretaria de Saúde conta com equipe multiprofissional — farmacêutico, médicos, enfermeiros e agentes comunitários — para apoiar quem quer parar de fumar. Informações na unidade de saúde.", hashtags=["chuvisca", "saude", "costadoce", "qualidadedevida", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Chuvisca contra o tabagismo", desenvolvimento_45s="A Secretaria de Saúde formou o primeiro grupo do Programa de Controle do Tabagismo. Uma equipe multiprofissional, com farmacêutico, médicos, enfermeiros e agentes comunitários, acompanha os participantes que querem parar de fumar.", fechamento_8s="Informações na unidade de saúde do município.", cta_5s="SulTV, a TV da nossa região.", trilha_sugerida="institucional leve"),
    tag_thumbnail="SAÚDE",
    briefing_visual=dict(
        descricao_pt="Roda de conversa em sala de unidade de saúde comunitária, cadeiras em círculo, ambiente acolhedor, sem rostos identificáveis",
        query_en=["support group circle chairs", "community health meeting room", "group therapy circle empty chairs"],
        evitar=["cigarros glorificados", "rostos identificáveis", "logos", "texto"],
        prompt_ia="Chairs arranged in a welcoming circle in a community health center room in Brazil, soft natural light, no people, no text, editorial photojournalism style",
    ),
)

A[9] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Serviço gratuito com prazo de inscrição em cidade-núcleo (Chuvisca) — cultura tradicionalista.",
    titulo_sultv="Chuvisca abre inscrições para curso gratuito de danças gaúchas",
    subtitulo="Aulas começam dia 25 de junho, às quintas-feiras à noite; inscrições vão até 24 de junho",
    lead="Estão abertas as inscrições para o curso gratuito de danças gaúchas de Chuvisca, promovido pela Secretaria de Educação, Cultura, Desporto e Turismo.",
    chamada_faixa="CURSO GRATUITO DE DANÇAS GAÚCHAS",
    ganchos_3=["Inscrições até 24 de junho", "Aulas às quintas-feiras, das 19h às 21h", "Valorização da cultura tradicionalista"],
    angulo_editorial="Serviço cultural com prazo: quem pode participar, quando começam as aulas e onde se inscrever.",
    fontes_complementares_sugeridas=["Secretaria de Educação, Cultura, Desporto e Turismo de Chuvisca"],
    lead_materia_longa="Chuvisca está com inscrições abertas até 24 de junho para o curso gratuito de danças gaúchas, com aulas a partir de 25 de junho, sempre às quintas-feiras, das 19h às 21h.",
    post_instagram=dict(caption="Bombacha e vestido de prenda em dia! 💃🕺 Chuvisca abriu inscrições para o curso gratuito de danças gaúchas. Inscrições até 24 de junho; aulas a partir de 25 de junho, às quintas, das 19h às 21h. Uma iniciativa para fortalecer a cultura tradicionalista.", hashtags=["chuvisca", "dancasgauchas", "tradicao", "costadoce", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Curso gratuito de danças gaúchas em Chuvisca", desenvolvimento_45s="As inscrições vão até 24 de junho e as aulas começam dia 25, sempre às quintas-feiras, das 19h às 21h. A iniciativa da prefeitura busca fortalecer a cultura tradicionalista e integrar a comunidade pela dança.", fechamento_8s="Garanta a vaga antes do prazo.", cta_5s="Siga a SulTV para mais oportunidades da região.", trilha_sugerida="vanera animada"),
    tag_thumbnail="TRADIÇÃO",
    briefing_visual=dict(
        descricao_pt="Dança tradicional gaúcha com trajes típicos em salão, saias rodadas em movimento, sem rostos identificáveis",
        query_en=["traditional gaucho dance brazil", "folk dance skirts motion", "traditional dance couple costume"],
        evitar=["rostos identificáveis em close", "marcas", "texto"],
        prompt_ia="Traditional gaucho folk dance in southern Brazil, swirling skirts and typical costumes in a community hall, motion blur, no identifiable faces, no text, editorial photojournalism style",
    ),
)

A[18] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Pauta de cultura e educação com fatos fortes em Pelotas: 12 escolas, novo NEABI e estátua com emenda de R$ 100 mil.",
    titulo_sultv="Manoel Padeiro inspira oficinas em 12 escolas da rede municipal de Pelotas",
    subtitulo="Líder quilombola da Serra dos Tapes dará nome a novo Núcleo de Estudos Afro-Brasileiros e Indígenas",
    lead="Doze escolas da rede municipal de Pelotas aderiram às oficinas pedagógicas sobre a história do líder quilombola Manoel Padeiro, da Serra dos Tapes.",
    chamada_faixa="MANOEL PADEIRO INSPIRA 12 ESCOLAS",
    ganchos_3=["12 escolas aderiram às oficinas da rede municipal", "Novo NEABI será inaugurado dia 16 de junho", "Emenda de R$ 100 mil viabiliza estátua do líder quilombola"],
    angulo_editorial="Memória e identidade da região: como a história quilombola da Serra dos Tapes entra na sala de aula e ganha espaço na cidade.",
    fontes_complementares_sugeridas=["Secretaria Municipal de Educação de Pelotas", "Assessoria para as Relações Étnico-Raciais (ERER)"],
    lead_materia_longa="Doze escolas da rede municipal de Pelotas trabalham em oficinas a história do líder quilombola Manoel Padeiro, da Serra dos Tapes, que dará nome ao novo Núcleo de Estudos Afro-Brasileiros e Indígenas a ser inaugurado em 16 de junho.",
    post_instagram=dict(caption="A história do líder quilombola Manoel Padeiro, da Serra dos Tapes, virou tema de oficinas em 12 escolas da rede municipal de Pelotas. No dia 16 de junho, a EMEF Piratinino de Almeida inaugura um Núcleo de Estudos Afro-Brasileiros e Indígenas com o nome dele — e uma estátua em sua homenagem já tem R$ 100 mil garantidos.", hashtags=["pelotas", "educacao", "cultura", "historia", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Quem foi Manoel Padeiro?", desenvolvimento_45s="O líder quilombola da Serra dos Tapes virou tema de oficinas em 12 escolas municipais de Pelotas. No dia 16, um novo Núcleo de Estudos Afro-Brasileiros e Indígenas será inaugurado com o nome dele, e uma estátua em sua homenagem terá R$ 100 mil de emenda parlamentar.", fechamento_8s="História da nossa região ganhando o lugar que merece.", cta_5s="Siga a SulTV.", trilha_sugerida="documental respeitosa"),
    tag_thumbnail="HISTÓRIA",
    briefing_visual=dict(
        descricao_pt="Sala de aula brasileira com produções artísticas e cartazes coloridos sobre cultura afro-brasileira na parede, sem rostos",
        query_en=["classroom art wall colorful", "school project posters wall", "afro brazilian culture art"],
        evitar=["rostos de crianças", "logos", "texto legível em close"],
        prompt_ia="Brazilian classroom wall with colorful student artwork celebrating Afro-Brazilian heritage, warm light, no people, no readable text, editorial photojournalism style",
    ),
)

A[19] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Serviço de saúde pública com fato concreto em Pelotas: campanha lançada, benefício a servidores e demanda do Hemopel.",
    titulo_sultv="Pelotas lança campanha para ampliar doação de sangue entre servidores",
    subtitulo="Ação do Junho Vermelho dá direito a duas folgas; Hemopel precisa de 1.200 bolsas por mês",
    lead="A Prefeitura de Pelotas lançou a quinta edição da campanha Sou Servidor, Sou Doador, que busca ampliar a captação de sangue no Hemocentro Regional de Pelotas durante o Junho Vermelho.",
    chamada_faixa="CAMPANHA DE DOAÇÃO DE SANGUE EM PELOTAS",
    ganchos_3=["Hemopel precisa de cerca de 1.200 bolsas por mês", "Servidores doadores ganham duas folgas", "Uma doação pode ajudar até quatro pessoas"],
    angulo_editorial="Serviço que salva vidas: por que o estoque é crítico, quem pode doar e qual o incentivo para os 9 mil servidores do município.",
    fontes_complementares_sugeridas=["Hemocentro Regional de Pelotas (Hemopel)", "Secretaria de Recursos Humanos de Pelotas"],
    lead_materia_longa="Cerca de 1.200 bolsas de sangue por mês: essa é a demanda do Hemocentro Regional de Pelotas, que motivou a prefeitura a lançar a quinta edição da campanha Sou Servidor, Sou Doador, dentro da programação do Junho Vermelho.",
    post_instagram=dict(caption="Pelotas lançou a campanha Sou Servidor, Sou Doador, do Junho Vermelho. O Hemopel precisa de cerca de 1.200 bolsas de sangue por mês para abastecer os hospitais da cidade — e uma única doação pode ajudar até quatro pessoas. Servidores que doarem ganham duas folgas. ❤️", hashtags=["pelotas", "doesangue", "junhovermelho", "saude", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Uma doação ajuda até quatro pessoas", desenvolvimento_45s="Pelotas lançou a campanha Sou Servidor, Sou Doador no Junho Vermelho. O Hemopel precisa de 1.200 bolsas por mês para abastecer os hospitais da cidade. Servidores que doarem têm direito a duas folgas, e a doação leva poucos minutos.", fechamento_8s="Doar sangue é um gesto que salva vidas.", cta_5s="SulTV, junto com a comunidade.", trilha_sugerida="emotiva leve"),
    tag_thumbnail="SAÚDE",
    briefing_visual=dict(
        descricao_pt="Bolsa de sangue e equipamentos de hemocentro em ambiente clínico limpo, tons de vermelho, sem pessoas identificáveis",
        query_en=["blood donation bag clinic", "blood bank equipment", "blood donation arm closeup"],
        evitar=["rostos", "agulhas em close dramático", "logos", "texto"],
        prompt_ia="Blood donation bag in a clean clinical blood bank setting, soft red tones, no people, no text, editorial photojournalism style",
    ),
)

A[22] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Entrega de infraestrutura de água em cidade-núcleo (Dom Feliciano), com data e local.",
    titulo_sultv="Dom Feliciano recebe quatro novos boosters para reforçar o abastecimento de água",
    subtitulo="Equipamentos ampliam a pressão na rede de distribuição e a segurança operacional do sistema",
    lead="Quatro novos boosters foram entregues oficialmente em Dom Feliciano para fortalecer o abastecimento de água no município.",
    chamada_faixa="MAIS PRESSÃO NA ÁGUA DE DOM FELICIANO",
    ganchos_3=["Quatro boosters entregues ao sistema municipal", "Mais pressão na rede de distribuição", "Benefício para toda a população"],
    angulo_editorial="Investimento que o morador sente na torneira: o que os boosters fazem e o que muda no abastecimento.",
    fontes_complementares_sugeridas=["Prefeitura de Dom Feliciano", "Corsan"],
    lead_materia_longa="Quatro novos boosters foram entregues em Dom Feliciano nesta quinta-feira (11), em ato na prefeitura, para ampliar a pressão da água na rede de distribuição e a segurança operacional do sistema de abastecimento.",
    post_instagram=dict(caption="Dom Feliciano recebeu quatro novos boosters para o sistema de abastecimento de água. 💧 Os equipamentos ampliam a pressão na rede de distribuição e aumentam a segurança operacional, beneficiando toda a população do município.", hashtags=["domfeliciano", "agua", "infraestrutura", "costadoce", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Mais pressão na água de Dom Feliciano", desenvolvimento_45s="Quatro novos boosters foram entregues ao sistema de abastecimento do município. Os equipamentos aumentam a pressão da água na rede de distribuição e a segurança operacional, beneficiando toda a população.", fechamento_8s="Investimento direto na qualidade de vida.", cta_5s="Acompanhe a SulTV.", trilha_sugerida="institucional otimista"),
    tag_thumbnail="ÁGUA",
    briefing_visual=dict(
        descricao_pt="Equipamento de bombeamento de água (booster) e tubulações azuis em estação de abastecimento, sem pessoas",
        query_en=["water pump station pipes", "water booster pump industrial", "water treatment plant pipes blue"],
        evitar=["rostos", "logos de empresas", "texto"],
        prompt_ia="Water booster pumps and blue pipes at a small municipal water supply station in Brazil, daylight, no people, no text, editorial photojournalism style",
    ),
)

pauta = []
for i, m in enumerate(items):
    base = dict(m)
    base["url_fonte"] = m.get("url")
    base.update(A.get(i, dict(decisao_final="REBAIXAR", decisao_motivo="Sem angulação prioritária no dia.")))
    pauta.append(base)

out = {"data": HOJE, "gerado_em": datetime.now(timezone.utc).isoformat(), "total": len(pauta), "pauta": pauta}
json.dump(out, open(OUT_PAUTA, "w"), ensure_ascii=False, indent=2)
pubs = [p for p in pauta if p["decisao_final"] == "PUBLICAR"]
print("pauta escrita:", OUT_PAUTA, "| total:", len(pauta), "| PUBLICAR:", len(pubs),
      "| REBAIXAR:", sum(1 for p in pauta if p["decisao_final"] == "REBAIXAR"),
      "| BLOQUEAR:", sum(1 for p in pauta if p["decisao_final"] == "BLOQUEAR"))
for p in pubs:
    print(" PUB:", p["id_hash"], "|", p["formato_sugerido"], "|", p["titulo_sultv"])
