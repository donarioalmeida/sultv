#!/usr/bin/env python3
"""angular_real_2026_05_30.py — angulacao editorial REAL do dia (keyed por id_hash das aprovadas)."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-05-30"

PAUTA_ANGULADA = {
 # 1. Arambaré — Concurso Peão e Prenda 2026 — PUBLICAR materia_longa (cidade-núcleo)
 "0e61e5e422d3b3aa28a3ae89a9e5a7e38c619260": {
   "titulo_sultv": "Arambaré abre Concurso de Escolha do Peão e Prenda 2026 com edital e material de estudo",
   "chamada_faixa": "Arambaré abre concurso de Peão e Prenda 2026",
   "subtitulo": "Município da Costa Doce disponibiliza edital e conteúdo de apoio aos candidatos do tradicional concurso da cultura gaúcha.",
   "lead": "Arambaré publicou o edital do Concurso de Escolha do Peão e Prenda 2026 e disponibilizou o material de estudo aos candidatos, dando início a um dos processos mais tradicionais da cultura gaúcha no município da Costa Doce.",
   "ganchos_3": ["Edital e material de estudo já disponíveis", "Concurso valoriza a cultura tradicionalista", "Renovação de Peão e Prenda de Arambaré"],
   "angulo_editorial": "Cultura tradicionalista em cidade-núcleo (Arambaré), fato concreto com edital publicado e forte vínculo identitário com a audiência da Costa Doce.",
   "fontes_complementares_sugeridas": ["Prefeitura de Arambaré", "CTG local", "MTG-RS"],
   "lead_materia_longa": "Arambaré publicou o edital do Concurso de Escolha do Peão e Prenda 2026 e disponibilizou o material de estudo aos candidatos, em iniciativa que valoriza a cultura tradicionalista do município da Costa Doce.",
   "post_instagram": {"caption": "Arambaré abriu o Concurso de Escolha do Peão e Prenda 2026. O edital e o material de estudo já estão disponíveis para quem quer representar o município nos eventos da cultura gaúcha ao longo do ano.", "hashtags": ["#Arambaré", "#PeãoEPrenda", "#CulturaGaúcha", "#Tradicionalismo", "#CostaDoce", "#SulTV"]},
   "roteiro_short_60s": {"abertura_2s": "Peão e Prenda em Arambaré.", "desenvolvimento_45s": "Arambaré publicou o edital do Concurso de Escolha do Peão e Prenda 2026 e já disponibilizou o material de estudo aos candidatos. O concurso é uma das tradições mais fortes da cultura gaúcha e define quem vai representar o município nos eventos ao longo do ano. Interessados devem acompanhar os canais oficiais da prefeitura para conferir prazos e critérios.", "fechamento_8s": "Edital e material já disponíveis.", "cta_5s": "Detalhes na SulTV.", "trilha_sugerida": "vanerão instrumental leve"},
   "tag_thumbnail": "Peão e Prenda 2026",
   "briefing_visual": {"descricao_pt": "Casal de prenda e peão em traje típico gaúcho em evento tradicionalista ao ar livre na Costa Doce, sem rostos identificáveis, luz natural", "query_en": ["gaucho traditional costume brazil", "south brazil folk dancers", "traditional rural festival attire"], "evitar": ["rostos identificáveis", "marcas", "texto", "logos"], "prompt_ia": "Traditional gaucho couple in typical southern Brazilian folk attire at an outdoor cultural festival, natural daylight, no identifiable faces, no text, editorial photojournalism style"},
   "decisao_final": "PUBLICAR",
   "decisao_motivo": "Cultura em cidade-núcleo (Arambaré) com edital publicado — fato concreto e forte vínculo identitário.",
 },
 # 2. Cristal — Av. Passo do Mendonça limpeza/reorganização — PUBLICAR materia_longa (2ª camada)
 "804da2cbe08274dd604274d8db6acc48cc218fed": {
   "titulo_sultv": "Cristal conclui limpeza e reorganização do canteiro central da Avenida Passo do Mendonça",
   "chamada_faixa": "Cristal finaliza melhorias na Av. Passo do Mendonça",
   "subtitulo": "Ações no canteiro central encerram o pacote de melhorias após a pavimentação da via.",
   "lead": "A Prefeitura de Cristal concluiu serviços de limpeza e reorganização do canteiro central da Avenida Passo do Mendonça, finalizando o pacote de melhorias iniciado com a pavimentação da via.",
   "ganchos_3": ["Canteiro central revitalizado", "Conclusão das melhorias pós-pavimentação", "Qualificação do espaço urbano"],
   "angulo_editorial": "Serviço público urbano em cidade-núcleo de segunda camada (Cristal), conclusão concreta de obra com utilidade direta à população.",
   "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria de Obras de Cristal"],
   "lead_materia_longa": "A Prefeitura de Cristal concluiu serviços de limpeza e reorganização do canteiro central da Avenida Passo do Mendonça, finalizando o pacote de melhorias iniciado com a pavimentação da via.",
   "post_instagram": {"caption": "Cristal concluiu a limpeza e a reorganização do canteiro central da Avenida Passo do Mendonça, fechando o pacote de melhorias que começou com a pavimentação da via. 🌿", "hashtags": ["#Cristal", "#CostaDoce", "#Infraestrutura", "#Obras", "#SulTV"]},
   "roteiro_short_60s": {"abertura_2s": "Avenida renovada em Cristal.", "desenvolvimento_45s": "A Prefeitura de Cristal concluiu a limpeza e a reorganização do canteiro central da Avenida Passo do Mendonça. As ações encerram o pacote de melhorias iniciado com a pavimentação da via, qualificando um dos espaços urbanos do município.", "fechamento_8s": "Espaço urbano mais qualificado.", "cta_5s": "Notícias da sua cidade na SulTV.", "trilha_sugerida": "instrumental neutro"},
   "tag_thumbnail": "Av. Passo do Mendonça",
   "briefing_visual": {"descricao_pt": "Canteiro central arborizado e limpo de avenida em cidade pequena do Sul do RS, dia claro, sem pessoas nem placas legíveis", "query_en": ["landscaped avenue median", "clean city boulevard greenery", "urban street median trees"], "evitar": ["pessoas com rosto visível", "marcas", "texto legível", "logos"], "prompt_ia": "A clean, landscaped central median of an urban avenue in a small southern Brazilian town, daylight, no people, no readable signs, editorial photojournalism style"},
   "decisao_final": "PUBLICAR",
   "decisao_motivo": "Serviço público concreto em cidade-núcleo de 2ª camada (Cristal).",
 },
 # 3. Pelotas — Centro Esportivo do Obelisco inaugurado — PUBLICAR materia_longa (reframe do título-seção)
 "2a55be1c531f9cd7fb3626aa7a4f895f854b1691": {
   "titulo_sultv": "Pelotas inaugura Centro Esportivo do Obelisco e convoca comunidade para a conservação",
   "chamada_faixa": "Pelotas inaugura Centro Esportivo do Obelisco",
   "subtitulo": "Espaço foi entregue na manhã de sexta-feira (29) com participação da comunidade e de autoridades municipais.",
   "lead": "Pelotas inaugurou na manhã de sexta-feira (29) o Centro Esportivo do Obelisco, em ato que reuniu a comunidade e autoridades municipais e marcou um apelo pela conservação coletiva do novo espaço.",
   "ganchos_3": ["Novo Centro Esportivo entregue", "Comunidade convocada para a conservação", "Esporte e lazer para o bairro"],
   "angulo_editorial": "Equipamento público de esporte e lazer em Pelotas (Costa Doce ampliada), fato concreto de comunidade — foco no espaço e no uso coletivo, sem viés partidário.",
   "fontes_complementares_sugeridas": ["Prefeitura de Pelotas", "Secretaria de Esporte, Lazer e Juventude de Pelotas"],
   "lead_materia_longa": "Pelotas inaugurou na manhã de sexta-feira (29) o Centro Esportivo do Obelisco, em ato que reuniu a comunidade e autoridades municipais e marcou um apelo pela conservação coletiva do novo espaço.",
   "post_instagram": {"caption": "Pelotas inaugurou o Centro Esportivo do Obelisco. O espaço foi entregue à comunidade na sexta-feira (29), com um chamado para que todos ajudem a conservar a nova estrutura de esporte e lazer. 🏀", "hashtags": ["#Pelotas", "#Esporte", "#Comunidade", "#CostaDoce", "#SulTV"]},
   "roteiro_short_60s": {"abertura_2s": "Espaço novo de esporte em Pelotas.", "desenvolvimento_45s": "Pelotas inaugurou na sexta-feira o Centro Esportivo do Obelisco. O espaço foi entregue à comunidade em ato com autoridades municipais, e a mensagem foi clara: cuidar do equipamento é tarefa de todos. Mais esporte e lazer para o bairro.", "fechamento_8s": "Cuidar é de todos.", "cta_5s": "Acompanhe na SulTV.", "trilha_sugerida": "indie urbano leve"},
   "tag_thumbnail": "Centro Esportivo",
   "briefing_visual": {"descricao_pt": "Quadra poliesportiva pública nova em bairro de cidade do Sul do RS, dia claro, sem rostos identificáveis", "query_en": ["public sports court neighborhood", "outdoor basketball court community", "new sports facility city"], "evitar": ["rostos identificáveis", "marcas", "texto", "logos"], "prompt_ia": "A newly built public multi-sport court in a neighborhood of a southern Brazilian city, clear daylight, no identifiable faces, no logos, no text, editorial photojournalism style"},
   "decisao_final": "PUBLICAR",
   "decisao_motivo": "Equipamento público de esporte/lazer em Pelotas — fato concreto de comunidade; título reescrito para focar no espaço (não no agente político).",
 },
 # 4. Cristal — ponto facultativo Corpus Christi — PUBLICAR materia_longa (serviço/utilidade)
 "f627cc1c2a9732aca6846189a5bfb42f1535d1d3": {
   "titulo_sultv": "Cristal terá ponto facultativo nos dias 4 e 5 de junho por causa de Corpus Christi",
   "chamada_faixa": "Cristal tem ponto facultativo no Corpus Christi",
   "subtitulo": "Decreto suspende o atendimento nas repartições municipais na quinta-feira do feriado e na sexta seguinte.",
   "lead": "A Prefeitura de Cristal decretou ponto facultativo nos dias 4 e 5 de junho, quando as repartições municipais terão o atendimento suspenso em razão do feriado de Corpus Christi.",
   "ganchos_3": ["Ponto facultativo nos dias 4 e 5 de junho", "Atendimento suspenso nas repartições", "Feriado de Corpus Christi"],
   "angulo_editorial": "Serviço de utilidade pública em cidade-núcleo de 2ª camada (Cristal) — informação prática sobre expediente municipal no feriado.",
   "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Diário Oficial do Município"],
   "lead_materia_longa": "A Prefeitura de Cristal decretou ponto facultativo nos dias 4 e 5 de junho, quando as repartições municipais terão o atendimento suspenso em razão do feriado de Corpus Christi.",
   "post_instagram": {"caption": "Atenção, Cristal: as repartições municipais terão ponto facultativo nos dias 4 e 5 de junho, por causa do feriado de Corpus Christi. Programe-se. 📅", "hashtags": ["#Cristal", "#CorpusChristi", "#Serviço", "#CostaDoce", "#SulTV"]},
   "roteiro_short_60s": {"abertura_2s": "Programe-se, Cristal.", "desenvolvimento_45s": "A Prefeitura de Cristal decretou ponto facultativo nos dias 4 e 5 de junho. As repartições municipais terão o atendimento suspenso por causa do feriado de Corpus Christi. Vale conferir os serviços essenciais que seguem funcionando.", "fechamento_8s": "Atendimento suspenso nos dias 4 e 5.", "cta_5s": "Mais informações na SulTV.", "trilha_sugerida": "instrumental neutro"},
   "tag_thumbnail": "Ponto facultativo",
   "briefing_visual": {"descricao_pt": "Fachada de prédio público municipal no Sul do RS em dia claro, sem pessoas nem texto legível", "query_en": ["city hall building facade brazil", "municipal government building", "public office exterior"], "evitar": ["pessoas com rosto visível", "marcas", "texto legível", "logos"], "prompt_ia": "Facade of a small Brazilian municipal government building under clear daylight, no people, no readable text, editorial photojournalism style"},
   "decisao_final": "PUBLICAR",
   "decisao_motivo": "Serviço de utilidade pública em cidade-núcleo de 2ª camada (Cristal).",
 },
 # 11. Venâncio Aires — Emef placas solares Afubra — PUBLICAR post (sem citar menores)
 "4c2578d0c44508e8553a0e90f0ac698a608a109f": {
   "titulo_sultv": "Escola de Venâncio Aires recebe placas solares da Afubra após projeto de eficiência energética",
   "chamada_faixa": "Escola de Venâncio ganha energia solar",
   "subtitulo": "Instituição foi contemplada com R$ 25 mil para a instalação a partir de projeto sobre redução do consumo de energia.",
   "lead": "Uma escola municipal de Venâncio Aires recebeu a instalação de placas solares da Afubra, fruto de um projeto de eficiência energética que rendeu R$ 25 mil em investimento.",
   "ganchos_3": ["R$ 25 mil em energia solar", "Projeto de eficiência energética", "Parceria com a Afubra"],
   "angulo_editorial": "Inovação e sustentabilidade na educação (RS) — energia solar em escola pública via parceria com a Afubra. Foco institucional, sem identificar menores.",
   "fontes_complementares_sugeridas": ["Folha do Mate", "Afubra", "Secretaria de Educação de Venâncio Aires"],
   "lead_materia_longa": "",
   "post_instagram": {"caption": "Energia limpa na escola: uma instituição de Venâncio Aires recebeu placas solares da Afubra, fruto de um projeto de eficiência energética contemplado com R$ 25 mil. Inovação e sustentabilidade na educação pública. ☀️", "hashtags": ["#VenâncioAires", "#EnergiaSolar", "#Educação", "#Sustentabilidade", "#Inovação", "#SulTV"]},
   "roteiro_short_60s": {"abertura_2s": "Energia solar na escola.", "desenvolvimento_45s": "Uma escola municipal de Venâncio Aires recebeu placas solares da Afubra. A instalação nasceu de um projeto de eficiência energética desenvolvido na escola, contemplado com R$ 25 mil. Sustentabilidade e economia caminhando juntas na educação pública.", "fechamento_8s": "Inovação que ensina e economiza.", "cta_5s": "Acompanhe na SulTV.", "trilha_sugerida": "corporativa otimista"},
   "tag_thumbnail": "Energia solar",
   "briefing_visual": {"descricao_pt": "Painéis solares fotovoltaicos instalados no telhado de uma escola, céu azul, sem pessoas", "query_en": ["solar panels school roof", "photovoltaic panels building", "rooftop solar installation"], "evitar": ["crianças", "rostos identificáveis", "marcas", "texto", "logos"], "prompt_ia": "Photovoltaic solar panels installed on the roof of a school building under a blue sky, no people, no children, no logos, no text, editorial photojournalism style"},
   "decisao_final": "PUBLICAR",
   "decisao_motivo": "Inovação/sustentabilidade na educação (RS) com fato concreto (R$25 mil, energia solar). Conteúdo redigido SEM identificar os alunos menores citados na fonte.",
 },
 # ── REBAIXAR ──
 "2a8f37e0042de551b76e10c07719cb8e5d6f66d4": {"decisao_final": "REBAIXAR", "decisao_motivo": "Etapa procedural de licitação (Estrada da Costa) com resumo vazio — sem fato ancorável; 2º item de Pelotas."},
 "9f0efb9d65fad461e201729f2fea8aebc5c0ac47": {"decisao_final": "REBAIXAR", "decisao_motivo": "Reunião interna de comissão com viés de 'participação política' e resumo raso ('Ver mais >')."},
 "9fe4f7079b8f79b3731f3c1c677312cf5d10cf40": {"decisao_final": "REBAIXAR", "decisao_motivo": "Conteúdo raso ('Ver mais >'); reunião institucional FETAG/Seduc sem fato concreto."},
 "c3cfb9bd1061887bb8136633d4d2a1f83be8a261": {"decisao_final": "REBAIXAR", "decisao_motivo": "Atrito político-local entre prefeitura e Corsan; 2º item de Venâncio Aires."},
 "17fe8d5332852444662b6cf73198cb1d13d1b668": {"decisao_final": "REBAIXAR", "decisao_motivo": "Sinistro (incêndio) em região distante do núcleo (Serra), sem âncora Sul-RS; tom policial."},
 # ── BLOQUEAR ──
 "54da86550dbad394c36708a7a9c2f7ad94d48e38": {"decisao_final": "BLOQUEAR", "decisao_motivo": "Agregador 'Fotos do Flickr' (Farsul) — cabeçalho de seção, não é matéria."},
 "e914edb4101909198de490e19b4ee3ebeb063e57": {"decisao_final": "BLOQUEAR", "decisao_motivo": "Título 'INFORMAÇÕES AGROPECUÁRIAS' é índice de seção (Emater), URL de informativo conjuntural — não é matéria única."},
 "427ec442c2076f9cb003b8f1f25c15418f35e4cd": {"decisao_final": "BLOQUEAR", "decisao_motivo": "Cabeçalho de seção ('Avisos e Alertas') + alertas de granizo datados de 25/05 (5 dias, expirados)."},
 "32da03d420a0dce647a87aad69e2ac4a67657d1f": {"decisao_final": "BLOQUEAR", "decisao_motivo": "Guardrail: crime envolvendo crianças (menores) + região distante do núcleo + tom policial."},
}

MATERIAS = {
 "0e61e5e422d3b3aa28a3ae89a9e5a7e38c619260": """### Título ###
Arambaré abre Concurso de Escolha do Peão e Prenda 2026 com edital e material de estudo

### Artigo ###
Arambaré publicou o edital do Concurso de Escolha do Peão e Prenda 2026 e disponibilizou o material de estudo aos candidatos, dando início a um dos processos mais tradicionais da cultura gaúcha no município da Costa Doce. A divulgação antecipada do edital e do conteúdo de apoio busca facilitar a preparação dos interessados, ampliar a participação e dar transparência aos critérios de avaliação. O concurso define quem representará Arambaré ao longo do ano nos eventos do tradicionalismo, levando o nome da cidade a rodeios, festivais e encontros culturais que movimentam o calendário do Rio Grande do Sul. Mais do que uma disputa, a escolha de peões e prendas cumpre um papel de preservação da identidade campeira, transmitindo às novas gerações os valores, a indumentária, a dança, a música e os costumes que caracterizam a cultura sul-rio-grandense. O material de estudo costuma reunir conteúdos sobre a história do Rio Grande do Sul, tradições, etiqueta campeira e conhecimentos gerais sobre o movimento tradicionalista, exigindo dedicação dos candidatos. Para a comunidade, o concurso fortalece o sentimento de pertencimento e estimula o envolvimento de famílias, Centros de Tradições Gaúchas e entidades culturais locais. A iniciativa também tem reflexo na economia e no turismo, já que as representações participam de eventos em diferentes cidades, promovendo Arambaré e a Costa Doce. Os interessados devem acompanhar os canais oficiais da Prefeitura de Arambaré para conferir prazos de inscrição, requisitos de participação, datas das etapas e a forma de acesso ao material de estudo. A expectativa é de boa adesão, mantendo viva uma tradição que conecta passado e presente na vida cultural do município.

### Legenda sugerida ###
Arambaré abre o Concurso de Peão e Prenda 2026; edital e material de estudo já disponíveis aos candidatos.

### Palavras-chave ###
Arambaré, Concurso de Peão e Prenda, cultura gaúcha, tradicionalismo, edital, Costa Doce, CTG, Rio Grande do Sul
""",
 "804da2cbe08274dd604274d8db6acc48cc218fed": """### Título ###
Cristal conclui limpeza e reorganização do canteiro central da Avenida Passo do Mendonça

### Artigo ###
A Prefeitura de Cristal concluiu os serviços de limpeza e reorganização do canteiro central da Avenida Passo do Mendonça, encerrando o pacote de melhorias iniciado com a pavimentação da via, no município da Costa Doce. A intervenção no canteiro central complementa a obra de pavimentação e tem como objetivo qualificar visualmente o espaço urbano, melhorar a drenagem e organizar a circulação na avenida. Ações desse tipo, ainda que de menor porte, fazem parte da rotina de conservação que mantém as vias públicas em boas condições de uso e contribuem para a segurança de motoristas, ciclistas e pedestres. A finalização das melhorias na Avenida Passo do Mendonça reforça a continuidade do trabalho de infraestrutura urbana no município. A pavimentação de vias, somada à manutenção de canteiros, calçadas e sinalização, integra um conjunto de medidas que impactam diretamente o dia a dia da população, reduzindo o desgaste de veículos, facilitando o escoamento da água da chuva e valorizando os imóveis e o comércio do entorno. Para cidades de menor porte como Cristal, a conservação contínua da malha viária é um investimento que evita gastos maiores no futuro e mantém a qualidade dos espaços públicos. A entrega da avenida revitalizada atende a uma demanda da comunidade e sinaliza a preocupação com a organização e a estética urbana. A administração municipal orienta os moradores a acompanharem os canais oficiais da Prefeitura de Cristal para informações sobre os próximos trechos e obras contemplados pelo programa de melhorias.

### Legenda sugerida ###
Cristal conclui limpeza e reorganização do canteiro central da Avenida Passo do Mendonça.

### Palavras-chave ###
Cristal, Avenida Passo do Mendonça, obras, infraestrutura urbana, pavimentação, Costa Doce, Rio Grande do Sul
""",
 "2a55be1c531f9cd7fb3626aa7a4f895f854b1691": """### Título ###
Pelotas inaugura Centro Esportivo do Obelisco e convoca comunidade para a conservação

### Artigo ###
Pelotas inaugurou na manhã de sexta-feira (29) o Centro Esportivo do Obelisco, em ato que reuniu a comunidade e autoridades municipais e marcou um apelo pela conservação coletiva do novo espaço, na Costa Doce ampliada. A entrega de um equipamento de esporte e lazer amplia as opções de atividade física e convivência para os moradores do entorno, especialmente crianças, jovens e idosos, que passam a contar com uma estrutura adequada perto de casa. Espaços como esse cumprem um papel social relevante: estimulam hábitos saudáveis, ocupam o tempo da juventude com atividades positivas e fortalecem o senso de comunidade. Durante a inauguração, o chamado foi para que a população participe ativamente da conservação do local. A preservação de praças, quadras e centros esportivos depende do cuidado coletivo, e o engajamento dos usuários é decisivo para que a estrutura se mantenha em boas condições ao longo do tempo. A mensagem reforça a ideia de que o patrimônio público pertence a todos e exige corresponsabilidade. A inauguração do Centro Esportivo do Obelisco integra o conjunto de investimentos em infraestrutura comunitária do município. Equipamentos de esporte e lazer, quando bem cuidados, tornam-se pontos de referência nos bairros e contribuem para a qualidade de vida e a coesão social. A comunidade pode acompanhar a programação de uso e as atividades previstas para o novo espaço pelos canais oficiais da Prefeitura de Pelotas.

### Legenda sugerida ###
Pelotas inaugura o Centro Esportivo do Obelisco e convoca a comunidade a cuidar do novo espaço.

### Palavras-chave ###
Pelotas, Centro Esportivo do Obelisco, esporte, lazer, comunidade, infraestrutura, Costa Doce, Rio Grande do Sul
""",
 "f627cc1c2a9732aca6846189a5bfb42f1535d1d3": """### Título ###
Cristal terá ponto facultativo nos dias 4 e 5 de junho por causa de Corpus Christi

### Artigo ###
A Prefeitura de Cristal decretou ponto facultativo nos dias 4 e 5 de junho, quando as repartições municipais terão o atendimento suspenso em razão do feriado de Corpus Christi, no município da Costa Doce. O dia 4 de junho, uma quinta-feira, é a data em que se celebra Corpus Christi, tradicionalmente marcada por atos religiosos e pela montagem de tapetes nas ruas em diversas cidades. Com o ponto facultativo estendido à sexta-feira, dia 5, o expediente das repartições municipais fica suspenso, criando um período prolongado de pausa no atendimento administrativo. A medida segue a prática comum em prefeituras gaúchas de conceder ponto facultativo na sexta-feira posterior a feriados que caem na quinta, organizando o calendário de trabalho do serviço público. É importante que a população se programe com antecedência para resolver demandas que dependam de atendimento presencial nas repartições municipais antes do período. Serviços considerados essenciais, como saúde de urgência, limpeza urbana e segurança, costumam manter funcionamento normal ou em regime de plantão, ainda que com equipes reduzidas. O retorno às atividades administrativas ocorre no primeiro dia útil seguinte ao período facultativo. A Prefeitura de Cristal orienta os moradores a acompanharem os canais oficiais do município para confirmar quais serviços permanecem em funcionamento durante o feriado de Corpus Christi e o ponto facultativo, evitando deslocamentos desnecessários.

### Legenda sugerida ###
Repartições de Cristal terão ponto facultativo nos dias 4 e 5 de junho por causa de Corpus Christi.

### Palavras-chave ###
Cristal, Corpus Christi, ponto facultativo, feriado, expediente, Costa Doce, Rio Grande do Sul
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
        ang = PAUTA_ANGULADA.get(h)
        if ang is None:
            ang = {"decisao_final": "BLOQUEAR", "decisao_motivo": "Sem angulação configurada — descartado por segurança"}
        if ang.get("decisao_final") == "PUBLICAR" and pub_count >= 10:
            ang = {**ang, "decisao_final": "REBAIXAR", "decisao_motivo": "Quota diária (10) esgotada"}
        if ang.get("decisao_final") == "PUBLICAR":
            pub_count += 1
        pauta.append({**item, **ang})

    ordem = {"PUBLICAR": 0, "ALERTA_HUMANO": 1, "REBAIXAR": 2, "BLOQUEAR": 3}
    pauta.sort(key=lambda x: (ordem.get(x.get("decisao_final", "REBAIXAR"), 9), -x.get("score_combinado", 0)))

    out = {"data": HOJE, "gerado_em": datetime.now(timezone.utc).isoformat(), "total": len(pauta), "pauta": pauta}
    pauta_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print("[angular] pauta ->", pauta_path.name)
    print("[angular] decisões:", Counter(p["decisao_final"] for p in pauta))

    materias_dir.mkdir(exist_ok=True)
    n = 0
    for p in pauta:
        if p.get("decisao_final") == "PUBLICAR" and p.get("formato_sugerido") == "materia_longa":
            corpo = MATERIAS.get(p["id_hash"])
            if corpo:
                (materias_dir / f"{p['id_hash']}.md").write_text(corpo, encoding="utf-8")
                n += 1
            else:
                print("[angular] AVISO sem matéria para", p["id_hash"])
    print(f"[angular] {n} matérias longas escritas")

if __name__ == "__main__":
    main()
