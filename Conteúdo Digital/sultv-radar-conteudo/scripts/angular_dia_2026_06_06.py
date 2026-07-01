#!/usr/bin/env python3
"""angular_dia_2026_06_06.py — angulação editorial do dia 2026-06-06 (cowork-faz-tudo).

Decisões tomadas por Claude na sessão Cowork. Gera:
  state/pauta_2026-06-06.json
  state/materias_2026-06-06/<id_hash>.md  (8 matérias PUBLICAR)

Resumo: 30 aprovadas -> 8 PUBLICAR / 12 REBAIXAR / 10 BLOQUEAR (quota 10 ok).
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-06"

APROVADAS = ROOT / "state" / f"aprovadas_{HOJE}.json"
PAUTA_OUT = ROOT / "state" / f"pauta_{HOJE}.json"
MAT_DIR = ROOT / "state" / f"materias_{HOJE}"

# ----------------------------------------------------------------------------
# Decisões + angulação por id_hash
# ----------------------------------------------------------------------------
ANG = {

# 1) PUBLICAR — Fogo destrói máquina agrícola em Tapes (Acústica FM)
"88eded03182b3531e963c3cce234d5ea77efeac6": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Fato concreto e recente em cidade-núcleo (Tapes); fonte regional confiável; sem vítima identificada.",
 "titulo_sultv": "Incêndio destrói máquina agrícola em fazenda de Tapes e mobiliza bombeiros",
 "chamada_faixa": "Fogo destrói máquina agrícola em Tapes",
 "subtitulo": "Bombeiros agiram para evitar que as chamas se alastrassem à plantação que cerca o local, na zona rural do município.",
 "lead": "Uma máquina agrícola foi destruída pelo fogo neste sábado (6) em uma fazenda na zona rural de Tapes, na Costa Doce. A ação rápida dos bombeiros impediu que as chamas atingissem a plantação ao redor, evitando um prejuízo de proporções maiores.",
 "ganchos_3": [
  "Máquina agrícola consumida pelo fogo em fazenda de Tapes",
  "Bombeiros impediram que chamas chegassem à lavoura",
  "Alerta de prevenção para produtores da Costa Doce"
 ],
 "angulo_editorial": "Segurança rural em cidade-núcleo: fato concreto (incêndio em máquina) com serviço embutido — prevenção de incêndios em maquinário agrícola, tema sensível ao produtor da Costa Doce.",
 "fontes_complementares_sugeridas": ["Corpo de Bombeiros de Tapes/Camaquã", "Sindicato Rural da região", "Emater/RS-Ascar"],
 "lead_materia_longa": "Uma máquina agrícola foi destruída pelo fogo neste sábado (6) em uma fazenda na zona rural de Tapes, na região da Costa Doce. Bombeiros evitaram que as chamas se alastrassem à plantação que cerca o local.",
 "post_instagram": {
  "caption": "Susto na zona rural de Tapes: uma máquina agrícola foi destruída pelo fogo neste sábado, mas a ação rápida dos bombeiros evitou que as chamas chegassem à lavoura. O episódio reforça a importância da manutenção preventiva e da limpeza do maquinário nesta época do ano.",
  "hashtags": ["#Tapes", "#CostaDoce", "#SegurançaRural", "#Agro", "#RioGrandeDoSul", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "Fogo destrói máquina agrícola em Tapes.",
  "desenvolvimento_45s": "Uma máquina agrícola foi totalmente destruída pelo fogo neste sábado em uma fazenda na zona rural de Tapes. Os bombeiros agiram rápido e impediram que as chamas se alastrassem para a plantação que cerca o local. Não há registro de feridos. Incêndios em maquinário costumam estar ligados a acúmulo de palha junto ao motor, superaquecimento e falhas elétricas — e a manutenção preventiva é a principal arma do produtor.",
  "fechamento_8s": "As causas do incêndio ainda não foram divulgadas.",
  "cta_5s": "Acompanhe as notícias da Costa Doce no site da SulTV.",
  "trilha_sugerida": "tensa-leve"
 },
 "tag_thumbnail": "TAPES",
 "briefing_visual": {
  "descricao_pt": "Colheitadeira em lavoura na zona rural de Tapes, no Sul do RS, ao entardecer, fumaça leve ao fundo, sem pessoas",
  "query_en": ["combine harvester field dusk", "farm machinery field smoke", "agricultural machine rural"],
  "evitar": ["chamas em close sensacionalista", "pessoas com rosto visível", "marcas de fabricantes", "texto", "logos"],
  "prompt_ia": "Wide shot of an agricultural combine harvester in a rural field in southern Brazil at dusk, faint smoke rising in the distance, dramatic but restrained mood, no people, no visible brands, no text, editorial photojournalism style"
 }
},

# 2) PUBLICAR — Fiergs robótica rede pública (CLIC R)
"71d8e4c166749fecf87911b126851418544f1bfb": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Fato concreto (lançamento de programa) com alcance estadual e interesse direto dos municípios da Costa Doce; educação + tecnologia.",
 "titulo_sultv": "Fiergs lança formação em robótica para alunos e professores da rede pública do RS",
 "chamada_faixa": "Fiergs leva robótica às escolas do RS",
 "subtitulo": "Projeto do Sistema Fiergs quer levar tecnologia e cultura maker às escolas municipais gaúchas, capacitando também os professores.",
 "lead": "Escolas municipais de todo o Rio Grande do Sul poderão receber formação em robótica para alunos e professores por meio de um projeto lançado pelo Sistema Fiergs, apresentado na quinta-feira (4) em entrevista ao Gaúcha Atualidade, da Rádio Gaúcha.",
 "ganchos_3": [
  "Sistema Fiergs lança formação em robótica para a rede pública",
  "Capacitação alcança professores e estudantes de escolas municipais",
  "Oportunidade concreta para municípios da Costa Doce aderirem"
 ],
 "angulo_editorial": "Educação e inovação com porta de entrada municipal: o programa é estadual, mas a adesão é das prefeituras — ângulo de oportunidade para as secretarias de educação da Costa Doce.",
 "fontes_complementares_sugeridas": ["Sistema Fiergs", "Secretarias municipais de Educação da Costa Doce", "SESI-RS"],
 "lead_materia_longa": "Escolas municipais de todo o Rio Grande do Sul poderão receber formação em robótica para alunos e professores por meio de um projeto lançado pelo Sistema Fiergs.",
 "post_instagram": {
  "caption": "Robótica na escola pública: o Sistema Fiergs lançou um projeto para levar formação em robótica a alunos e professores de escolas municipais do RS. A meta declarada é impactar a educação gaúcha — e a adesão passa pelas prefeituras. Boa janela para os municípios da Costa Doce.",
  "hashtags": ["#Educação", "#Robótica", "#Fiergs", "#RioGrandeDoSul", "#Inovação", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "Robótica nas escolas públicas do RS.",
  "desenvolvimento_45s": "O Sistema Fiergs lançou um projeto para levar formação em robótica a alunos e professores de escolas municipais do Rio Grande do Sul. A proposta capacita o professor e engaja o estudante, aproximando a rede pública da cultura maker e das carreiras técnicas. A adesão passa pelas prefeituras — uma oportunidade para os municípios da Costa Doce colocarem suas escolas no mapa da tecnologia.",
  "fechamento_8s": "Secretarias de educação devem acompanhar os canais da Fiergs.",
  "cta_5s": "Mais educação e inovação no site da SulTV.",
  "trilha_sugerida": "inspiradora"
 },
 "tag_thumbnail": "EDUCAÇÃO",
 "briefing_visual": {
  "descricao_pt": "Mãos de estudantes montando um pequeno robô educacional sobre classe escolar, peças coloridas, sem rostos visíveis",
  "query_en": ["students hands robotics kit", "educational robot classroom", "robot building parts desk"],
  "evitar": ["rostos de crianças", "uniformes identificáveis", "logos", "texto"],
  "prompt_ia": "Close-up of students' hands assembling a small educational robot on a classroom desk, colorful electronic parts and wires, warm natural light, no faces, no logos, no text, editorial photojournalism style"
 }
},

# 3) PUBLICAR — Incêndio restaurante RSC-287 Santa Cruz do Sul (Clic Camaquã)
"84b8978fae2b1f692a53df06e2b5d4cbd4d78799": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Fato concreto e recente, sem vítima identificada; repercussão regional via fonte de Camaquã.",
 "titulo_sultv": "Incêndio destrói restaurante e floricultura às margens da RSC-287 em Santa Cruz do Sul",
 "chamada_faixa": "Incêndio destrói restaurante na RSC-287",
 "subtitulo": "Chamas começaram na noite de sexta-feira e mobilizaram bombeiros por mais de cinco horas de combate.",
 "lead": "Mais de cinco horas de combate às chamas marcaram a noite de sexta-feira (5) em Santa Cruz do Sul, onde um incêndio destruiu completamente um restaurante tradicional e uma floricultura às margens da RSC-287.",
 "ganchos_3": [
  "Restaurante tradicional e floricultura completamente destruídos",
  "Mais de cinco horas de combate às chamas",
  "Causas do incêndio serão investigadas"
 ],
 "angulo_editorial": "Segurança e prevenção: fato relevante para quem trafega pela RSC-287 e alerta sobre prevenção de incêndios em estabelecimentos comerciais à beira de rodovia.",
 "fontes_complementares_sugeridas": ["Corpo de Bombeiros de Santa Cruz do Sul", "CRBM", "Defesa Civil"],
 "lead_materia_longa": "Mais de cinco horas de combate às chamas marcaram a noite de sexta-feira (5) em Santa Cruz do Sul, onde um incêndio destruiu completamente um restaurante tradicional e uma floricultura às margens da RSC-287.",
 "post_instagram": {
  "caption": "Um incêndio destruiu completamente um restaurante tradicional e uma floricultura às margens da RSC-287, em Santa Cruz do Sul. As chamas começaram na noite de sexta-feira e os bombeiros trabalharam por mais de cinco horas no combate. As causas serão investigadas.",
  "hashtags": ["#SantaCruzDoSul", "#RSC287", "#Bombeiros", "#RioGrandeDoSul", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "Incêndio de grandes proporções na RSC-287.",
  "desenvolvimento_45s": "Um restaurante tradicional e uma floricultura às margens da RSC-287, em Santa Cruz do Sul, foram completamente destruídos pelo fogo na noite de sexta-feira. Os bombeiros trabalharam por mais de cinco horas no combate às chamas. Não há informações sobre feridos, e as causas do incêndio serão investigadas pelas autoridades.",
  "fechamento_8s": "O caso segue em apuração.",
  "cta_5s": "Acompanhe no site da SulTV.",
  "trilha_sugerida": "tensa-leve"
 },
 "tag_thumbnail": "INCÊNDIO",
 "briefing_visual": {
  "descricao_pt": "Bombeiros combatendo incêndio em edificação comercial à noite, vistos a distância, fumaça e luzes de emergência",
  "query_en": ["firefighters night building fire", "fire truck smoke night", "firefighters hose flames distance"],
  "evitar": ["rostos identificáveis", "vítimas", "marcas/fachadas reais", "texto"],
  "prompt_ia": "Firefighters spraying water on a burning single-story commercial building at night, seen from a distance, heavy smoke and emergency lights, no identifiable faces, no text, editorial photojournalism style"
 }
},

# 4) PUBLICAR — Cristal: Rua Camaquã preparação calçamento (Prefeitura)
"5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Obra concreta de infraestrutura em cidade da segunda camada (Cristal); fonte oficial.",
 "titulo_sultv": "Rua Camaquã recebe preparação para obras de calçamento em Cristal",
 "chamada_faixa": "Rua Camaquã terá calçamento em Cristal",
 "subtitulo": "Serviços preliminares antecedem a pavimentação da via e integram pacote de melhorias urbanas no município.",
 "lead": "A Rua Camaquã, em Cristal, na região da Costa Doce, começou a receber os serviços de preparação para as obras de calçamento, segundo a Prefeitura. A etapa antecede a pavimentação e integra a agenda de melhorias viárias do município.",
 "ganchos_3": [
  "Rua Camaquã entra em fase de preparação para calçamento",
  "Obra integra pacote de melhorias viárias em Cristal",
  "Calçamento reduz poeira e melhora escoamento da chuva"
 ],
 "angulo_editorial": "Infraestrutura municipal na Costa Doce: pauta positiva e de serviço, com impacto direto na rotina dos moradores de Cristal.",
 "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria de Obras de Cristal"],
 "lead_materia_longa": "A Rua Camaquã, em Cristal, na região da Costa Doce, começou a receber os serviços de preparação para as obras de calçamento, segundo a Prefeitura.",
 "post_instagram": {
  "caption": "Obras em Cristal: a Rua Camaquã começou a receber os serviços de preparação para o calçamento. A pavimentação de vias urbanas reduz poeira e barro, melhora o escoamento da chuva e valoriza a região. Moradores devem ficar atentos a alterações no trânsito durante a execução.",
  "hashtags": ["#Cristal", "#CostaDoce", "#Obras", "#Infraestrutura", "#RioGrandeDoSul", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "Calçamento a caminho em Cristal.",
  "desenvolvimento_45s": "A Rua Camaquã, em Cristal, começou a receber os serviços de preparação para as obras de calçamento. A etapa antecede a pavimentação e integra o pacote de melhorias viárias do município, que recentemente também finalizou os trabalhos na Avenida Passo do Mendonça. O calçamento reduz poeira e barro e melhora o escoamento da água da chuva.",
  "fechamento_8s": "A Prefeitura orienta atenção às mudanças no trânsito.",
  "cta_5s": "Notícias da Costa Doce no site da SulTV.",
  "trilha_sugerida": "neutra-positiva"
 },
 "tag_thumbnail": "CRISTAL",
 "briefing_visual": {
  "descricao_pt": "Rua de cidade do interior em obras de calçamento, paralelepípedos empilhados e areia, luz difusa, sem pessoas",
  "query_en": ["cobblestone street construction", "paving stones road work", "street paving small town"],
  "evitar": ["pessoas com rosto visível", "placas com nomes", "marcas", "texto"],
  "prompt_ia": "Small-town street being prepared for cobblestone paving in southern Brazil, stacked paving stones and sand piles along the road, overcast soft light, no people, no text, editorial photojournalism style"
 }
},

# 5) PUBLICAR — São Lourenço do Sul: Selo Prata Amigo da Vacina (SLR)
"ff08241618128d19c4b248113b1c116cebb5459a": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Reconhecimento institucional de saúde pública (não é saúde médica individual); cidade da segunda camada; fonte local.",
 "titulo_sultv": "São Lourenço do Sul conquista Selo Prata Amigo da Vacina por cobertura vacinal",
 "chamada_faixa": "São Lourenço conquista selo da vacinação",
 "subtitulo": "Certificação estadual reconhece o cumprimento das metas de cobertura vacinal e o engajamento da população nas campanhas.",
 "lead": "São Lourenço do Sul foi certificado em nível estadual com o selo Amigo da Vacina — Categoria Prata, pelo cumprimento das metas de cobertura vacinal, incluindo a vacina Pentavalente. O anúncio foi destacado pelo secretário municipal da Saúde, Diego Elias.",
 "ganchos_3": [
  "Município certificado com Selo Prata Amigo da Vacina",
  "Metas de cobertura vacinal cumpridas, incluindo a Pentavalente",
  "Secretaria busca ampliar adesão às campanhas"
 ],
 "angulo_editorial": "Pauta positiva de saúde pública institucional: reconhecimento estadual + convite à comunidade para manter carteiras de vacinação em dia.",
 "fontes_complementares_sugeridas": ["Secretaria Municipal da Saúde de São Lourenço do Sul", "Secretaria Estadual da Saúde do RS"],
 "lead_materia_longa": "São Lourenço do Sul foi certificado em nível estadual com o selo Amigo da Vacina — Categoria Prata, pelo cumprimento das metas de cobertura vacinal das campanhas municipais.",
 "post_instagram": {
  "caption": "Reconhecimento para São Lourenço do Sul: o município conquistou o Selo Prata Amigo da Vacina, certificação estadual pelo cumprimento das metas de cobertura vacinal. Agora, o objetivo é ampliar ainda mais a adesão às campanhas. Carteira de vacinação em dia é proteção para toda a comunidade.",
  "hashtags": ["#SãoLourençoDoSul", "#Vacinação", "#SaúdePública", "#CostaDoce", "#RioGrandeDoSul", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "São Lourenço do Sul ganha selo estadual de vacinação.",
  "desenvolvimento_45s": "O município conquistou o selo Amigo da Vacina — Categoria Prata, certificação estadual concedida pelo cumprimento das metas de cobertura vacinal, incluindo a vacina Pentavalente. O reconhecimento reflete o engajamento da população nas campanhas, e a Secretaria Municipal da Saúde agora trabalha para ampliar a adesão.",
  "fechamento_8s": "A orientação é manter a carteira de vacinação em dia.",
  "cta_5s": "Mais saúde e comunidade no site da SulTV.",
  "trilha_sugerida": "positiva"
 },
 "tag_thumbnail": "SAÚDE",
 "briefing_visual": {
  "descricao_pt": "Frascos de vacina e seringa sobre bancada de unidade de saúde, luz clínica suave, sem pessoas e sem rótulos",
  "query_en": ["vaccine vials syringe clinic", "vaccination vials close up", "health clinic counter vaccine"],
  "evitar": ["crianças", "rostos", "rótulos/marcas de vacina", "agulha aplicada em pessoa", "texto"],
  "prompt_ia": "Close-up of unlabeled vaccine vials and a syringe on a clean health clinic counter, soft clinical lighting, shallow depth of field, no people, no brand labels, no text, editorial photojournalism style"
 }
},

# 6) PUBLICAR — Pelotas: morango / associação Emater (Diário da Manhã)
"5243be736e2649528d6bc837fd8bbde97e1353d1": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Fato concreto de agro/agricultura familiar na Costa Doce ampliada (Pelotas); fonte confiável.",
 "titulo_sultv": "Produtores de morango de Pelotas discutem criação de associação com apoio da Emater",
 "chamada_faixa": "Morango de Pelotas rumo à associação",
 "subtitulo": "Cerca de 30 produtores da Feira Municipal participaram de reunião promovida pela Emater/RS-Ascar para debater a organização coletiva.",
 "lead": "Cerca de 30 produtores de morango participantes da Feira Municipal de Pelotas se reuniram para discutir a criação de uma associação da categoria, em encontro promovido pela Emater/RS-Ascar, com foco em comercialização, políticas públicas e representatividade.",
 "ganchos_3": [
  "Cerca de 30 produtores de morango reunidos em Pelotas",
  "Associação deve fortalecer comercialização e representatividade",
  "Encontro promovido pela Emater/RS-Ascar"
 ],
 "angulo_editorial": "Agricultura familiar e associativismo na Zona Sul: organização coletiva como caminho para mercado e políticas públicas — pauta de fomento típica SulTV.",
 "fontes_complementares_sugeridas": ["Emater/RS-Ascar Pelotas", "Secretaria de Desenvolvimento Rural de Pelotas", "produtores da Feira Municipal"],
 "lead_materia_longa": "Cerca de 30 produtores de morango participantes da Feira Municipal de Pelotas se reuniram para discutir a criação de uma associação da categoria, em encontro promovido pela Emater/RS-Ascar.",
 "post_instagram": {
  "caption": "O morango de Pelotas quer se organizar: cerca de 30 produtores da Feira Municipal se reuniram com a Emater/RS-Ascar para discutir a criação de uma associação. Juntos, eles ganham força na comercialização, no acesso a políticas públicas e na representatividade da categoria.",
  "hashtags": ["#Pelotas", "#Morango", "#AgriculturaFamiliar", "#Emater", "#ZonaSul", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "Produtores de morango de Pelotas querem associação.",
  "desenvolvimento_45s": "Cerca de 30 produtores de morango que participam da Feira Municipal de Pelotas se reuniram em encontro promovido pela Emater/RS-Ascar para discutir a criação de uma associação da categoria. A organização coletiva fortalece a comercialização, facilita o acesso a políticas públicas e dá mais voz ao produtor. Os próximos passos passam pela formalização da entidade.",
  "fechamento_8s": "O movimento sinaliza amadurecimento da cadeia de frutas na Zona Sul.",
  "cta_5s": "Mais agro no site da SulTV.",
  "trilha_sugerida": "positiva"
 },
 "tag_thumbnail": "AGRO",
 "briefing_visual": {
  "descricao_pt": "Morangos frescos em caixas de madeira em banca de feira de produtores, close vibrante, sem pessoas",
  "query_en": ["strawberries farmers market boxes", "fresh strawberry harvest", "strawberry crates market"],
  "evitar": ["pessoas com rosto visível", "marcas", "texto", "embalagens identificáveis"],
  "prompt_ia": "Fresh ripe strawberries in wooden crates at a farmers market stall in southern Brazil, vibrant red fruit, soft morning light, no people, no text, editorial photojournalism style"
 }
},

# 7) PUBLICAR — MetSul: neve há um ano / El Niño 2026
"01e4af8f22701aee0014a55e168747935cd1d8cd": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Análise climática regional de alto interesse da audiência (inverno/El Niño); fonte de referência (MetSul).",
 "titulo_sultv": "Um ano após neve no Sul do Brasil, El Niño reduz chance de nevadas em 2026",
 "chamada_faixa": "El Niño reduz chance de neve em 2026",
 "subtitulo": "Fenômeno de aquecimento do Pacífico tende a deixar o inverno gaúcho mais úmido e com menos janelas de frio intenso, aponta a MetSul.",
 "lead": "Há um ano, em 29 de maio de 2025, nevava com acumulação no Rio Grande do Sul e em Santa Catarina — algo raro para maio. Em 2026, porém, a presença do El Niño pode impedir a repetição do fenômeno, segundo análise da MetSul Meteorologia.",
 "ganchos_3": [
  "Um ano da neve rara de maio de 2025 no RS e em SC",
  "El Niño tende a deixar o inverno mais úmido e quente",
  "Sinal climático importa para o planejamento da safra"
 ],
 "angulo_editorial": "Clima como pauta de planejamento rural: a leitura do El Niño interessa do morador urbano ao produtor da Costa Doce que define manejo de inverno e a próxima safra de verão.",
 "fontes_complementares_sugeridas": ["MetSul Meteorologia", "Inmet", "Emater/RS-Ascar"],
 "lead_materia_longa": "Há um ano, em 29 de maio de 2025, nevava com acumulação no Rio Grande do Sul e em Santa Catarina. Em 2026, a presença do El Niño pode impedir a repetição do fenômeno, segundo a MetSul Meteorologia.",
 "post_instagram": {
  "caption": "Lembra da neve de maio de 2025? Um ano depois, o cenário é outro: com El Niño atuando, o inverno de 2026 tende a ser mais úmido e com menos janelas de frio intenso no Sul do Brasil, segundo a MetSul. Para o campo, o sinal climático pesa no manejo de inverno e no planejamento da próxima safra.",
  "hashtags": ["#Clima", "#ElNiño", "#Inverno2026", "#RioGrandeDoSul", "#Agro", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "Vai nevar em 2026? O El Niño responde.",
  "desenvolvimento_45s": "Há um ano, em maio de 2025, nevava com acumulação no Rio Grande do Sul e em Santa Catarina. Em 2026, porém, o El Niño — fenômeno de aquecimento das águas do Pacífico — tende a deixar o inverno do Sul mais úmido e com temperaturas médias mais altas, reduzindo as janelas de frio intenso necessárias para a neve. Para o produtor, mais chuva no inverno muda o manejo de solo e o planejamento da safra.",
  "fechamento_8s": "A recomendação é acompanhar os boletins oficiais.",
  "cta_5s": "Previsões e clima no site da SulTV.",
  "trilha_sugerida": "contemplativa"
 },
 "tag_thumbnail": "CLIMA",
 "briefing_visual": {
  "descricao_pt": "Paisagem rural do Sul do Brasil com geada e neve leve sobre campo, araucárias ao fundo, luz fria de manhã",
  "query_en": ["frost field winter landscape", "light snow rural field", "winter morning farm frost"],
  "evitar": ["pessoas", "construções identificáveis", "texto", "logos"],
  "prompt_ia": "Rural landscape in southern Brazil with light snow and frost covering a grassy field, araucaria trees in the background, cold blue early morning light, no people, no text, editorial photojournalism style"
 }
},

# 8) PUBLICAR — Canal Rural: renegociação de dívidas no Senado
"ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Tema econômico central para o produtor do RS (crédito rural/safra); fonte parceira em contexto positivo; política pública, não partidária.",
 "titulo_sultv": "Produtores do RS temem que renegociação de dívidas não seja aprovada pelo Senado",
 "chamada_faixa": "Dívidas do campo: RS pressiona o Senado",
 "subtitulo": "Setor teme ficar sem acesso ao crédito rural para a próxima safra caso a proposta não avance, mostra reportagem do Canal Rural.",
 "lead": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas do setor no Senado. O receio, segundo reportagem do Canal Rural, é ficar sem acesso ao crédito rural para a próxima safra caso a proposta não seja aprovada.",
 "ganchos_3": [
  "Renegociação de dívidas do campo em análise no Senado",
  "Receio de safra sem acesso ao crédito rural",
  "Endividamento agravado por estiagens e enchentes de 2024"
 ],
 "angulo_editorial": "Economia rural com âncora regional: na Costa Doce, arroz e soja dependem de custeio — a tramitação no Senado define a capacidade de plantio da próxima safra.",
 "fontes_complementares_sugeridas": ["Canal Rural", "Farsul", "Federarroz", "bancada gaúcha no Senado"],
 "lead_materia_longa": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas do setor no Senado, com receio de ficar sem acesso ao crédito rural para a próxima safra.",
 "post_instagram": {
  "caption": "\"A gente não dorme mais\": a frase de um produtor gaúcho resume a apreensão do campo com a renegociação de dívidas em análise no Senado. Sem a aprovação, o receio é ficar sem acesso ao crédito rural para a próxima safra — um risco direto para quem planta arroz e soja no Sul do RS.",
  "hashtags": ["#Agro", "#CréditoRural", "#RioGrandeDoSul", "#Safra", "#Senado", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "O campo gaúcho não dorme tranquilo.",
  "desenvolvimento_45s": "Produtores do Rio Grande do Sul temem que a renegociação de dívidas do setor não seja aprovada pelo Senado. O endividamento se agravou após estiagens seguidas e as enchentes de 2024, e sem a renegociação o receio é não conseguir contratar o custeio da próxima safra. Na Costa Doce, onde arroz e soja puxam a economia, o acesso ao crédito define a capacidade de plantio.",
  "fechamento_8s": "Entidades do setor defendem aprovação célere.",
  "cta_5s": "Acompanhe a economia do agro no site da SulTV.",
  "trilha_sugerida": "tensa-leve"
 },
 "tag_thumbnail": "AGRO",
 "briefing_visual": {
  "descricao_pt": "Lavoura de soja com trator ao longe sob céu nublado no Rio Grande do Sul, clima sóbrio, sem pessoas",
  "query_en": ["soybean field tractor cloudy", "farm field overcast sky", "soy crop field brazil"],
  "evitar": ["pessoas com rosto visível", "marcas de máquinas", "texto", "logos"],
  "prompt_ia": "Soybean field with a tractor in the far distance under an overcast sky in Rio Grande do Sul, Brazil, sober moody light, wide editorial framing, no people, no visible brands, no text, editorial photojournalism style"
 }
},

# ---------------- REBAIXAR (12) ----------------
"5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Pauta datada de 16/04/2026 (quase dois meses); risco de inscrições encerradas. Vira nota interna para checagem de prazo.",
 "titulo_sultv": "Arambaré tem cursos gratuitos de qualificação profissional pelo RS Qualificação",
 "angulo_editorial": "Serviço relevante para cidade-núcleo, mas requer confirmação de vigência das inscrições antes de publicar."
},
"7328151d0f689699ca147e00ec7ffb87008ee51e": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Anúncio de 19/01/2026; sem confirmação de status atual da obra. Checar andamento antes de repercutir.",
 "titulo_sultv": "Arambaré anuncia reconstrução da Plataforma de Pesca Quito Lima",
 "angulo_editorial": "Pauta de potencial alto (turismo/pesca em cidade-núcleo) — sugerir follow-up sobre andamento da obra."
},
"6d583901d0b2623e718e91c071da59f2069c1522": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Lei municipal de 2025 sem fato novo datado; conteúdo de aviso permanente da prefeitura.",
 "titulo_sultv": "Barra do Ribeiro proíbe fogos com estampido por lei municipal",
 "angulo_editorial": "Serviço atemporal de bem-estar animal — pode virar post frio em data oportuna (festas de fim de ano)."
},
"4ceb630b463e5a73d241cc134657509620995c00": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Duplicata do item ff082416 (mesma pauta do selo Amigo da Vacina, versão sem resumo).",
 "titulo_sultv": "São Lourenço do Sul conquista Selo Prata Amigo da Vacina (duplicado)",
 "angulo_editorial": "Conteúdo coberto pela matéria principal do dia."
},
"804da2cbe08274dd604274d8db6acc48cc218fed": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Segunda pauta de Cristal no dia, de menor peso (limpeza de canteiro). A vaga de Cristal foi para o calçamento da Rua Camaquã; esta entra como contexto na matéria publicada.",
 "titulo_sultv": "Avenida Passo do Mendonça recebe limpeza e reorganização em Cristal",
 "angulo_editorial": "Usada como contexto na matéria do calçamento da Rua Camaquã."
},
"a6885d87261ed899066eaed1e127d684baa35ba1": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Pauta estadual de Justiça do Trabalho sem âncora Costa Doce; interesse difuso.",
 "titulo_sultv": "Justiça do Trabalho gaúcha movimenta R$ 156,8 milhões em acordos",
 "angulo_editorial": "Número expressivo, mas sem recorte regional que justifique matéria própria."
},
"da4142fbb0edad6b837e4d203d5fe4dd944d642b": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Fact-check de 28/05 já com mais de uma semana; MetSul já representada na pauta do dia com análise mais atual.",
 "titulo_sultv": "MetSul desmente boato de 'ciclones gêmeos' no litoral do Brasil",
 "angulo_editorial": "Checagem útil, mas envelhecida; quota MetSul do dia ocupada pela pauta do El Niño."
},
"8c10d704aa76774d2be1bdb6d93ca335fbf9061b": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Fato de 14/05 (três semanas); fora da janela de atualidade do Radar.",
 "titulo_sultv": "Vinhos vencidos há 9 anos são apreendidos em mercados gaúchos",
 "angulo_editorial": "Pauta de fiscalização relevante, porém datada."
},
"92a6390bbe4cd5b16486593f31d3720a4666bcaa": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Artigo de análise institucional (deep tech), sem fato concreto datado; tag 'policia' atribuída pelo classificador está incorreta.",
 "titulo_sultv": "Tecnopuc debate formação de deep techs no ecossistema gaúcho",
 "angulo_editorial": "Bom insumo para pauta fria de inovação; não é notícia factual."
},
"005c3f84f53ec63f1a7f123b52192249e4dcd062": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Evento de abertura já realizado em 26/05; cobertura perderia atualidade.",
 "titulo_sultv": "Programa Hangar abre edição Energia e Saúde no Tecnopuc",
 "angulo_editorial": "Acompanhar resultados do programa para eventual pauta futura."
},
"014b0c7e7ebe83a7e9d2818d435714326ff6390e": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Pauta institucional de Santa Maria sem âncora Costa Doce; interesse moderado.",
 "titulo_sultv": "Projeto liderado pela UFSM integra hospitais universitários gaúchos",
 "angulo_editorial": "Relevância estadual difusa; sem gancho regional direto."
},
"16206258f59fab2b8f9623840b8b17dccdd97f4f": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Coluna de opinião de veículo de Venâncio Aires; Radar não republica conteúdo opinativo de terceiros.",
 "titulo_sultv": "Coluna defende prevenção como legado das enchentes de 2024",
 "angulo_editorial": "Tema prevenção é caro à audiência — vale pauta própria da redação, não réplica de coluna."
},

# ---------------- BLOQUEAR (10) ----------------
"e8243e7e1901a6c9be6fc53a4655813d09f9cca9": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Pauta vencida: prazo de inscrição do Enem 2026 encerrou às 23h59 de sexta (5); publicar sábado induziria a erro."
},
"e01838afcd9335ee307b79a73b8b0bf111bfe4ba": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Edital procedural (publicação de penalidade) — sem valor noticioso; guardrail de edital."
},
"7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Edital procedural de 30/03 (abertura de prazo para requerimentos); vencido e burocrático."
},
"09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Título genérico de aviso ('AVISO DE AUDIÊNCIA PÚBLICA') sem conteúdo nem data — cabeçalho procedural."
},
"c77c704f766cfa913b42a8d2b37cfc4c03320244": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Aviso administrativo procedural (emissor nacional de NF) de 05/05; sem valor noticioso."
},
"74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Comunicado interno a servidores (revisão de contracheques); não é notícia para o público."
},
"52a34cdaeffd6c322e99946d7c0ec9b186f6071c": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Aviso interno de manutenção do Moodle/UFSM, já vencido (retorno previsto para 03/06)."
},
"462f0b5dc029d973aa47d866332ce37a9a0d5794": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Coluna de opinião sobre esporte amador da região da Serra — fora da área de cobertura e opinativo."
},
"afe430799de79547d2d9b7086008075f10225dbc": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Conteúdo promocional/comercial (sorteio de empresa na ExpoBento), região distante."
},
"0476dd3a86bfea166e89841310b3c479865f2ca6": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Conteúdo promocional de inauguração de loja (Havan/Garibaldi), região distante da cobertura."
},
}

# ----------------------------------------------------------------------------
# Matérias longas (.md) — formato literal PROMPT_REDACAO_SULTV
# ----------------------------------------------------------------------------
MATERIAS = {

"88eded03182b3531e963c3cce234d5ea77efeac6": """### Título ###
Incêndio destrói máquina agrícola em fazenda de Tapes e mobiliza bombeiros

### Artigo ###
Uma máquina agrícola foi destruída pelo fogo neste sábado (6) em uma fazenda na zona rural de Tapes, na região da Costa Doce. Segundo informações da Rádio Acústica FM, a ação rápida dos bombeiros evitou que as chamas se alastrassem para a plantação que cerca o local, o que poderia transformar a perda pontual do equipamento em um prejuízo de proporções muito maiores. Não há registro de feridos, e as causas do incêndio ainda não foram divulgadas pelas autoridades. Incêndios em maquinário agrícola são um risco conhecido no campo: o acúmulo de palha e resíduos junto ao motor, o superaquecimento de componentes, falhas elétricas e a falta de manutenção preventiva figuram entre os principais fatores apontados por especialistas em segurança rural. Em períodos de tempo seco, uma única faísca pode ser suficiente para iniciar um foco de difícil controle em meio à lavoura. O episódio deste sábado serve de alerta para os produtores da Costa Doce, em especial nesta época do ano, quando máquinas passam por uso intenso e revisões costumam ser adiadas. A recomendação técnica é manter limpeza periódica do equipamento, revisar o sistema elétrico, carregar extintores adequados a bordo e interromper a operação ao primeiro sinal de superaquecimento. A reportagem acompanha o caso e aguarda informações oficiais do Corpo de Bombeiros sobre a origem do fogo e a extensão dos danos. Com informações da Rádio Acústica FM.

### Legenda sugerida ###
Bombeiros impediram que chamas em máquina agrícola se alastrassem à lavoura em Tapes

### Palavras-chave ###
incêndio em Tapes, máquina agrícola, bombeiros, Costa Doce, segurança rural, Tapes
""",

"71d8e4c166749fecf87911b126851418544f1bfb": """### Título ###
Fiergs lança formação em robótica para alunos e professores da rede pública do RS

### Artigo ###
Escolas municipais de todo o Rio Grande do Sul poderão receber formação em robótica para alunos e professores por meio de um projeto lançado pelo Sistema Fiergs. A iniciativa foi apresentada na quinta-feira (4), em entrevista ao programa Gaúcha Atualidade, da Rádio Gaúcha, com uma mensagem direta: é preciso impactar a educação gaúcha. A proposta atua em duas frentes ao mesmo tempo — capacita o professor, que multiplica o conhecimento em sala de aula, e engaja o estudante, que passa a ter contato prático com tecnologia, programação e cultura maker desde o ensino fundamental. A robótica educacional vem ganhando espaço nas redes públicas do país por desenvolver raciocínio lógico, trabalho em equipe e capacidade de resolução de problemas, competências valorizadas tanto pela indústria quanto pelas carreiras técnicas. Para os municípios da Costa Doce, como Camaquã, Tapes, Cristal e São Lourenço do Sul, programas desse tipo representam uma oportunidade concreta de aproximar os jovens do universo da tecnologia sem depender de grandes investimentos próprios, já que a estrutura de formação parte do Sistema Fiergs. A adesão passa pelas administrações municipais, e as secretarias de educação interessadas devem acompanhar os canais oficiais da federação para informações sobre cronograma e critérios de participação. Com informações do Portal ClicR e da Rádio Gaúcha.

### Legenda sugerida ###
Projeto do Sistema Fiergs leva robótica a alunos e professores de escolas municipais do RS

### Palavras-chave ###
Fiergs, robótica, educação, escolas públicas, Rio Grande do Sul, tecnologia, cultura maker
""",

"84b8978fae2b1f692a53df06e2b5d4cbd4d78799": """### Título ###
Incêndio destrói restaurante e floricultura às margens da RSC-287 em Santa Cruz do Sul

### Artigo ###
Mais de cinco horas de combate às chamas marcaram a noite de sexta-feira (5) em Santa Cruz do Sul, onde um incêndio destruiu completamente um restaurante tradicional e uma floricultura localizados às margens da RSC-287. Segundo informações do Clic Camaquã, o fogo começou durante a noite e consumiu toda a estrutura dos estabelecimentos, exigindo longa mobilização das equipes do Corpo de Bombeiros até o controle total das chamas. Não há informações sobre feridos. As causas do incêndio serão investigadas pelas autoridades competentes. A RSC-287 é uma das principais ligações do Vale do Rio Pardo com a região central do estado, e estabelecimentos à beira da rodovia costumam ser pontos de referência para viajantes, caminhoneiros e moradores — o que amplia o impacto da perda para a comunidade local. Casos como este também acendem o alerta para a prevenção de incêndios em estabelecimentos comerciais, especialmente os que operam cozinhas industriais: a revisão periódica das instalações elétricas, o cuidado com botijões e centrais de GLP e a manutenção de extintores em dia estão entre as medidas básicas recomendadas pelos bombeiros. A reconstrução dos negócios atingidos dependerá da apuração das causas e da cobertura de seguros. A reportagem segue acompanhando a investigação. Com informações do Clic Camaquã.

### Legenda sugerida ###
Fogo consumiu restaurante e floricultura na RSC-287; combate durou mais de cinco horas

### Palavras-chave ###
incêndio, Santa Cruz do Sul, RSC-287, bombeiros, restaurante, Rio Grande do Sul
""",

"5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": """### Título ###
Rua Camaquã recebe preparação para obras de calçamento em Cristal

### Artigo ###
A Rua Camaquã, em Cristal, na região da Costa Doce, começou a receber os serviços de preparação para as obras de calçamento, segundo informações da Prefeitura. A etapa preliminar antecede a pavimentação propriamente dita e envolve os trabalhos de adequação da via para receber as pedras, fase decisiva para a qualidade e a durabilidade do calçamento. A pavimentação de ruas urbanas traz benefícios diretos e imediatos para os moradores: reduz a poeira nos dias secos e o barro nos dias de chuva, melhora o escoamento da água, facilita o deslocamento de veículos e pedestres e valoriza os imóveis do entorno. A obra na Rua Camaquã se soma a outras melhorias viárias em andamento no município — recentemente, a Avenida Passo do Mendonça, que já havia sido pavimentada, recebeu serviços de limpeza e reorganização do canteiro central como parte da finalização daquela intervenção. O conjunto de ações indica uma agenda continuada de qualificação da malha urbana de Cristal, demanda histórica de municípios de pequeno porte da região. Durante a execução dos trabalhos na Rua Camaquã, os moradores devem ficar atentos a eventuais alterações no trânsito e seguir as orientações das equipes no local. A Prefeitura ainda não divulgou prazo de conclusão da obra. Com informações da Prefeitura de Cristal.

### Legenda sugerida ###
Via de Cristal passa por serviços preliminares antes da pavimentação com pedras

### Palavras-chave ###
Cristal, calçamento, Rua Camaquã, obras, infraestrutura, Costa Doce
""",

"ff08241618128d19c4b248113b1c116cebb5459a": """### Título ###
São Lourenço do Sul conquista Selo Prata Amigo da Vacina por cobertura vacinal

### Artigo ###
São Lourenço do Sul foi certificado em nível estadual com o selo Amigo da Vacina — Categoria Prata, reconhecimento concedido aos municípios que cumprem as metas de cobertura vacinal, incluindo a vacina Pentavalente. O anúncio foi destacado pelo secretário municipal da Saúde, Diego Elias, em entrevista à SLR Rádio, que atribuiu o resultado ao engajamento da população nas campanhas de vacinação realizadas no município. A certificação coloca São Lourenço do Sul entre as cidades gaúchas que atingiram os índices estaduais de imunização, um indicador central de saúde pública: coberturas vacinais elevadas protegem a comunidade contra doenças evitáveis e reduzem a pressão sobre a rede de atendimento. Conquistado o selo na categoria Prata, o município agora trabalha para ampliar ainda mais a adesão às campanhas, com atenção especial ao público infantil, cujo calendário concentra as principais vacinas de rotina. A orientação da Secretaria Municipal da Saúde é que as famílias mantenham as carteiras de vacinação em dia e procurem as unidades de saúde para atualizar doses em atraso — o serviço é gratuito e disponível em toda a rede municipal. O reconhecimento estadual reforça o papel das equipes de saúde da Costa Doce, que sustentaram as metas mesmo em um cenário nacional de queda nas coberturas vacinais. Com informações do São Lourenço Reporter.

### Legenda sugerida ###
Município atinge metas de cobertura vacinal e recebe certificação estadual na categoria Prata

### Palavras-chave ###
São Lourenço do Sul, vacinação, selo Amigo da Vacina, saúde pública, Costa Doce
""",

"5243be736e2649528d6bc837fd8bbde97e1353d1": """### Título ###
Produtores de morango de Pelotas discutem criação de associação com apoio da Emater

### Artigo ###
Cerca de 30 produtores de morango participantes da Feira Municipal de Pelotas se reuniram para discutir a criação de uma associação da categoria, em encontro promovido pela Emater/RS-Ascar. A organização coletiva, apontou a entidade, traz benefícios que vão da comercialização ao acesso a políticas públicas, passando pelo fortalecimento da representatividade dos produtores junto ao poder público e ao mercado. A produção de morango tem importância crescente na Zona Sul do estado, fortemente ligada à agricultura familiar, e a venda direta ao consumidor — como a realizada na Feira Municipal — é um dos principais canais de escoamento da fruta. Com uma associação formalizada, os produtores ganham escala para compras conjuntas de insumos, participação em programas institucionais de aquisição de alimentos e negociação de melhores condições logísticas e comerciais. O movimento também sinaliza um amadurecimento da cadeia de frutas na região de Pelotas e da Costa Doce, onde a diversificação produtiva vem ganhando espaço ao lado das culturas tradicionais de arroz e soja. Os próximos passos do grupo incluem a definição do formato jurídico da entidade e a formalização do quadro de associados, com acompanhamento técnico da Emater/RS-Ascar. Com informações do Diário da Manhã de Pelotas.

### Legenda sugerida ###
Cerca de 30 produtores da Feira Municipal debatem associativismo com a Emater/RS-Ascar

### Palavras-chave ###
morango, Pelotas, Emater, associação, agricultura familiar, Zona Sul
""",

"01e4af8f22701aee0014a55e168747935cd1d8cd": """### Título ###
Um ano após neve no Sul do Brasil, El Niño reduz chance de nevadas em 2026

### Artigo ###
Há um ano, em 29 de maio de 2025, o Brasil registrava a primeira neve daquele ano, com acumulação no Rio Grande do Sul e em Santa Catarina — fenômeno pouco comum para o mês de maio. Em 2026, porém, a presença do El Niño pode impedir que as nevadas se repitam, segundo análise da MetSul Meteorologia. O El Niño é o fenômeno de aquecimento anômalo das águas do Oceano Pacífico equatorial e costuma deixar os invernos do Sul do Brasil mais úmidos e com temperaturas médias mais elevadas. Na prática, isso reduz as janelas de frio intenso e seco que são necessárias para a ocorrência de neve, mesmo nas áreas mais altas da Serra gaúcha e catarinense. Para os moradores da Costa Doce e da Zona Sul, o sinal climático vai além da curiosidade sobre a neve: invernos sob El Niño tendem a registrar chuva acima da média, o que influencia diretamente o manejo de solo, as pastagens, as culturas de inverno e o planejamento da próxima safra de verão, incluindo o arroz e a soja que sustentam a economia regional. O excesso de umidade também exige atenção redobrada com drenagem de lavouras e estradas do interior. A recomendação é acompanhar os boletins meteorológicos oficiais ao longo da estação, já que a intensidade do fenômeno define o tamanho dos seus efeitos. Com informações da MetSul Meteorologia.

### Legenda sugerida ###
El Niño deixa inverno mais úmido e quente e reduz chance de neve no Sul em 2026

### Palavras-chave ###
neve, El Niño, inverno 2026, MetSul, clima, Rio Grande do Sul
""",

"ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS temem que renegociação de dívidas não seja aprovada pelo Senado

### Artigo ###
Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas do setor no Senado. Reportagem do Canal Rural mostra que o receio é ficar sem acesso ao crédito rural para a próxima safra caso a proposta não avance — "a gente não dorme mais", resumiu um dos produtores ouvidos. O endividamento do campo gaúcho se agravou nos últimos anos após uma sequência de safras comprometidas por estiagens severas e pelas enchentes de 2024, que somaram perdas de produção, de infraestrutura e de renda. Com o balanço comprometido, parte dos produtores não consegue liquidar os financiamentos anteriores e, sem a renegociação, fica impedida de contratar o custeio do próximo ciclo. Na Costa Doce e na Zona Sul, onde o arroz e a soja puxam a economia, o acesso ao crédito define a capacidade de plantio: sem custeio, a área semeada encolhe, com efeito em cascata sobre comércio, serviços e arrecadação dos municípios da região. Entidades representativas do setor acompanham a tramitação em Brasília e defendem a aprovação célere da proposta, argumentando que a recuperação da capacidade de pagamento do produtor depende justamente de manter a roda da produção girando. A expectativa é que o tema avance nas próximas semanas no Senado. Com informações do Canal Rural.

### Legenda sugerida ###
Setor teme ficar sem crédito rural para a próxima safra se proposta não avançar no Senado

### Palavras-chave ###
renegociação de dívidas, crédito rural, Senado, produtores rurais, Rio Grande do Sul, safra
""",
}


def main():
    data = json.loads(APROVADAS.read_text(encoding="utf-8"))
    aprovadas = data["aprovadas"]

    pauta = []
    for item in aprovadas:
        h = item["id_hash"]
        ang = ANG.get(h)
        if not ang:
            item["decisao_final"] = "REBAIXAR"
            item["decisao_motivo"] = "Sem angulação específica — fora do top do dia."
            pauta.append(item)
            continue
        merged = {**item, **ang}
        pauta.append(merged)

    out = {
        "data": HOJE,
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "total": len(pauta),
        "pauta": pauta,
    }
    PAUTA_OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[angular] pauta escrita: {PAUTA_OUT} ({len(pauta)} itens)")

    MAT_DIR.mkdir(parents=True, exist_ok=True)
    for h, corpo in MATERIAS.items():
        p = MAT_DIR / f"{h}.md"
        p.write_text(corpo, encoding="utf-8")
        print(f"[angular] matéria: {p.name}")

    pub = [m for m in pauta if m.get("decisao_final") == "PUBLICAR"]
    reb = [m for m in pauta if m.get("decisao_final") == "REBAIXAR"]
    blo = [m for m in pauta if m.get("decisao_final") == "BLOQUEAR"]
    print(f"[angular] PUBLICAR={len(pub)} REBAIXAR={len(reb)} BLOQUEAR={len(blo)}")
    assert len(pub) <= 10, "quota de 10 PUBLICAR estourada"


if __name__ == "__main__":
    main()
