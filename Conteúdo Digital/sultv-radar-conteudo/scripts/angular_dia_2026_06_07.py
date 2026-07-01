#!/usr/bin/env python3
"""angular_dia_2026_06_07.py — angulação editorial do dia 2026-06-07 (cowork-faz-tudo).

Decisões tomadas por Claude na sessão Cowork. Gera:
  state/pauta_2026-06-07.json
  state/materias_2026-06-07/<id_hash>.md  (4 matérias PUBLICAR)

Resumo: 30 aprovadas -> 4 PUBLICAR / 5 REBAIXAR / 21 BLOQUEAR (quota 10 ok).
Nota do dia: domingo com muitos duplicados do histórico (8 itens já publicados
em dias anteriores) e alto volume de editais/avisos procedurais de prefeituras.
Regra 12 aplicada integralmente: nenhuma menção a veículos nos textos.
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-07"

APROVADAS = ROOT / "state" / f"aprovadas_{HOJE}.json"
PAUTA_OUT = ROOT / "state" / f"pauta_{HOJE}.json"
MAT_DIR = ROOT / "state" / f"materias_{HOJE}"

ANG = {

# ============================ PUBLICAR (4) ============================

# 1) PUBLICAR — Murilo Cardoso, campeão mundial de jiu-jitsu (Camaquã)
"1fb11c1f31a01fb5ce1038c92ebe74fa30835b80": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Fato concreto e positivo em cidade-núcleo (Camaquã): título mundial inédito de atleta local; pauta de comunidade com forte apelo regional.",
 "titulo_sultv": "Atleta de Camaquã conquista título mundial de jiu-jitsu na faixa azul",
 "chamada_faixa": "CAMPEÃO MUNDIAL DE JIU-JITSU É DE CAMAQUÃ",
 "subtitulo": "Murilo Cardoso celebrou a conquista inédita e destacou o apoio que sempre recebeu da comunidade camaquense.",
 "lead": "Camaquã, na Costa Doce, comemora um título mundial: o atleta Murilo Cardoso conquistou o Mundial de Jiu-Jitsu na faixa azul, resultado inédito na carreira do camaquense, que atribuiu a vitória também ao apoio recebido da comunidade local.",
 "ganchos_3": [
  "Título mundial inédito para atleta camaquense na faixa azul",
  "Murilo Cardoso destacou o apoio da comunidade de Camaquã",
  "Esporte da Costa Doce ganhando projeção internacional"
 ],
 "angulo_editorial": "Orgulho regional: conquista esportiva internacional de atleta de cidade-núcleo, com ângulo de comunidade — o papel do apoio local na formação de atletas do interior.",
 "fontes_complementares_sugeridas": ["Secretaria de Esportes de Camaquã", "Federação Gaúcha de Jiu-Jitsu", "Academia do atleta em Camaquã"],
 "lead_materia_longa": "O atleta camaquense Murilo Cardoso conquistou o título do Mundial de Jiu-Jitsu na faixa azul, resultado inédito que projeta o esporte da Costa Doce no cenário internacional.",
 "post_instagram": {
  "caption": "De Camaquã para o mundo! O atleta Murilo Cardoso conquistou o título do Mundial de Jiu-Jitsu na faixa azul — resultado inédito na carreira do camaquense, que fez questão de dividir a conquista com a comunidade que sempre o apoiou. Orgulho da Costa Doce no tatame internacional.",
  "hashtags": ["#Camaquã", "#CostaDoce", "#JiuJitsu", "#Esporte", "#RioGrandeDoSul", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "Camaquã tem um campeão mundial de jiu-jitsu.",
  "desenvolvimento_45s": "O atleta camaquense Murilo Cardoso conquistou o título do Mundial de Jiu-Jitsu na faixa azul, um resultado inédito na sua trajetória. Ao celebrar a conquista, o atleta fez questão de lembrar o apoio que sempre recebeu da comunidade de Camaquã — das torcidas nos campeonatos regionais ao incentivo para competir fora. A vitória coloca o esporte da Costa Doce no mapa internacional e serve de inspiração para jovens atletas de toda a região.",
  "fechamento_8s": "A conquista é mais um capítulo do esporte camaquense em alta.",
  "cta_5s": "Acompanhe as histórias da Costa Doce no site da SulTV.",
  "trilha_sugerida": "inspiradora"
 },
 "tag_thumbnail": "CAMAQUÃ",
 "briefing_visual": {
  "descricao_pt": "Atleta de jiu-jitsu de kimono azul em tatame durante competição, em momento de vitória, sem rosto identificável em close",
  "query_en": ["brazilian jiu jitsu competition mat", "jiu jitsu athlete gi victory", "martial arts tournament mat"],
  "evitar": ["rosto em close identificável", "marcas de equipes", "texto", "logos", "bandeiras de academias"],
  "prompt_ia": "Wide shot of a brazilian jiu-jitsu athlete in a blue gi celebrating victory on a competition mat, arena lighting, dynamic but respectful composition, no identifiable faces, no brands, no text, editorial photojournalism style"
 }
},

# 2) PUBLICAR — Justiça do Trabalho gaúcha: R$ 156,8 mi em acordos
"a6885d87261ed899066eaed1e127d684baa35ba1": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Fato concreto com dado quantitativo forte e abrangência estadual; fonte primária institucional (Justiça do Trabalho); interesse direto de trabalhadores e empregadores da região.",
 "titulo_sultv": "Justiça do Trabalho gaúcha fecha R$ 156,8 milhões em acordos na Semana da Conciliação",
 "chamada_faixa": "ACORDOS TRABALHISTAS SOMAM R$ 156,8 MILHÕES NO RS",
 "subtitulo": "Valor foi homologado durante a 10ª Semana Nacional da Conciliação Trabalhista, realizada entre 25 e 29 de maio.",
 "lead": "A Justiça do Trabalho do Rio Grande do Sul homologou R$ 156,8 milhões em acordos durante a 10ª Semana Nacional da Conciliação Trabalhista, realizada entre os dias 25 e 29 de maio, encerrando processos de forma mais rápida para trabalhadores e empresas gaúchas.",
 "ganchos_3": [
  "R$ 156,8 milhões em acordos homologados em apenas cinco dias",
  "Conciliação encerra processos com mais rapidez para as duas partes",
  "Trabalhadores e empresas da Zona Sul também podem buscar acordos"
 ],
 "angulo_editorial": "Economia e serviço: o dado estadual vira utilidade regional — a conciliação como caminho mais rápido e barato para resolver disputas trabalhistas, válido para empregados e empregadores da Costa Doce e Zona Sul.",
 "fontes_complementares_sugeridas": ["TRT da 4ª Região", "OAB Subseção Camaquã", "Sindicatos de trabalhadores e patronais da região"],
 "lead_materia_longa": "A Justiça do Trabalho gaúcha homologou R$ 156,8 milhões em acordos durante a 10ª Semana Nacional da Conciliação Trabalhista, realizada entre 25 e 29 de maio.",
 "post_instagram": {
  "caption": "R$ 156,8 milhões em acordos em cinco dias: esse foi o resultado da 10ª Semana Nacional da Conciliação Trabalhista na Justiça do Trabalho gaúcha. A conciliação encerra processos com mais rapidez e menos custo — alternativa que vale tanto para o trabalhador quanto para a empresa, inclusive aqui na região.",
  "hashtags": ["#JustiçaDoTrabalho", "#Conciliação", "#RioGrandeDoSul", "#Economia", "#Trabalho", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "R$ 156,8 milhões em acordos trabalhistas no RS.",
  "desenvolvimento_45s": "A Justiça do Trabalho gaúcha homologou R$ 156,8 milhões em acordos durante a 10ª Semana Nacional da Conciliação Trabalhista, entre 25 e 29 de maio. Na conciliação, trabalhador e empresa chegam a um entendimento homologado pelo juiz, encerrando o processo sem a espera de anos por uma sentença. O mecanismo reduz custos para os dois lados e está disponível o ano inteiro nas varas do trabalho, inclusive nas unidades que atendem a Zona Sul e a Costa Doce.",
  "fechamento_8s": "A conciliação pode ser pedida em qualquer fase do processo.",
  "cta_5s": "Mais economia e serviço no site da SulTV.",
  "trilha_sugerida": "informativa"
 },
 "tag_thumbnail": "ECONOMIA",
 "briefing_visual": {
  "descricao_pt": "Aperto de mãos sobre mesa com documentos e martelo de juiz ao fundo, ambiente de sala de audiência, sem rostos visíveis",
  "query_en": ["handshake agreement documents desk", "labor court gavel documents", "mediation handshake office"],
  "evitar": ["rostos identificáveis", "logos de tribunais", "texto legível em documentos", "marcas"],
  "prompt_ia": "Close-up of a handshake over a desk with legal documents and a judge gavel softly blurred in the background, courtroom setting, warm neutral light, no faces, no text, editorial photojournalism style"
 }
},

# 3) PUBLICAR — É falso que "ciclones gêmeos" vão atingir o Brasil
"da4142fbb0edad6b837e4d203d5fe4dd944d642b": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Serviço público de checagem: boato meteorológico circulando em redes sociais com potencial de alarme na região; desmentir é função editorial relevante.",
 "titulo_sultv": "É falso que ciclones gêmeos vão atingir o Brasil, apontam meteorologistas",
 "chamada_faixa": "CICLONES GÊMEOS NO BRASIL? É FALSO",
 "subtitulo": "Publicações em redes sociais alertam para suposto fenômeno com riscos ao Sul do país; previsões oficiais não indicam nada parecido.",
 "lead": "Circula nas redes sociais um alerta falso sobre a formação de supostos ciclones gêmeos no litoral do Brasil, com riscos para a população do Sul e do Sudeste. Meteorologistas verificaram a informação e confirmam: não há qualquer previsão desse tipo de fenômeno para os próximos dias.",
 "ganchos_3": [
  "Boato sobre ciclones gêmeos se espalha nas redes sociais",
  "Meteorologistas confirmam que não há previsão do fenômeno",
  "Orientação é seguir apenas canais oficiais de meteorologia e Defesa Civil"
 ],
 "angulo_editorial": "Checagem como serviço: o RS é sensível a alertas climáticos desde 2024, e boatos meteorológicos geram pânico real na população — desmentir com clareza e reforçar os canais oficiais é papel da redação regional.",
 "fontes_complementares_sugeridas": ["Inmet", "Defesa Civil do RS", "Sala de Situação SEMA-RS"],
 "lead_materia_longa": "Circula nas redes sociais um alerta falso sobre a formação de supostos ciclones gêmeos no litoral brasileiro, com riscos para o Sul do país. Não há previsão desse fenômeno.",
 "post_instagram": {
  "caption": "Atenção: é FALSO o alerta sobre ciclones gêmeos que estaria circulando para o Sul do Brasil. Meteorologistas verificaram as publicações e não há nenhuma previsão desse tipo de fenômeno. Antes de compartilhar alertas de clima, confira sempre os canais oficiais — Inmet e Defesa Civil. Informação errada também causa estrago.",
  "hashtags": ["#FakeNews", "#Clima", "#DefesaCivil", "#RioGrandeDoSul", "#Checagem", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "Ciclones gêmeos no Brasil? Isso é falso.",
  "desenvolvimento_45s": "Está circulando nas redes sociais um alerta sobre a formação de supostos ciclones gêmeos no litoral do Brasil, com riscos para o Sul e o Sudeste. Meteorologistas verificaram a informação: não existe nenhuma previsão desse fenômeno. Desde as enchentes de 2024, alertas falsos de clima encontram terreno fértil no RS e geram pânico desnecessário. A orientação é simples: só confie em previsões dos canais oficiais, como o Inmet e a Defesa Civil do seu município.",
  "fechamento_8s": "Antes de compartilhar, verifique a fonte do alerta.",
  "cta_5s": "Informação verificada no site da SulTV.",
  "trilha_sugerida": "informativa-séria"
 },
 "tag_thumbnail": "É FALSO",
 "briefing_visual": {
  "descricao_pt": "Imagem de satélite de nuvens sobre o oceano Atlântico Sul, vista do espaço, formação de tempestade, sem texto",
  "query_en": ["satellite storm clouds ocean", "cyclone satellite view atlantic", "weather satellite clouds sea"],
  "evitar": ["montagens sensacionalistas", "texto sobreposto", "logos", "mapas com marcas de portais"],
  "prompt_ia": "Satellite view of swirling storm clouds over the South Atlantic ocean, realistic meteorological imagery, blue and white tones, no land labels, no text, editorial photojournalism style"
 }
},

# 4) PUBLICAR — Vinhos vencidos há 9 anos apreendidos (MP-RS)
"8c10d704aa76774d2be1bdb6d93ca335fbf9061b": {
 "decisao_final": "PUBLICAR",
 "decisao_motivo": "Fato concreto de segurança alimentar com fonte primária institucional (Ministério Público do RS); serviço direto ao consumidor gaúcho; sem vítima identificada.",
 "titulo_sultv": "Vinhos vencidos há 9 anos: operação apreende 5 toneladas de produtos estragados no RS",
 "chamada_faixa": "5 TONELADAS DE PRODUTOS VENCIDOS APREENDIDOS NO RS",
 "subtitulo": "Fiscalização do Ministério Público encontrou alimentos e bebidas impróprios em três mercados gaúchos; um estabelecimento foi interditado e o proprietário, preso.",
 "lead": "Cinco toneladas de produtos estragados, incluindo vinhos vencidos há nove anos, foram apreendidas em uma operação de fiscalização do Ministério Público do Rio Grande do Sul em três mercados do estado. Um dos estabelecimentos teve interdição total e o proprietário foi preso.",
 "ganchos_3": [
  "Vinhos vencidos há 9 anos estavam à venda em mercados gaúchos",
  "Cinco toneladas de produtos impróprios foram confiscadas",
  "Consumidor deve conferir validade e denunciar irregularidades"
 ],
 "angulo_editorial": "Segurança alimentar como serviço: além do fato (operação do MP), a pauta orienta o consumidor da região a conferir validade, condições de armazenamento e canais de denúncia.",
 "fontes_complementares_sugeridas": ["Ministério Público do RS", "Procon municipal", "Vigilância Sanitária dos municípios da região"],
 "lead_materia_longa": "Cinco toneladas de produtos estragados, incluindo vinhos vencidos há nove anos, foram apreendidas em operação do Ministério Público do Rio Grande do Sul em três mercados gaúchos.",
 "post_instagram": {
  "caption": "Vinho vencido há NOVE anos na prateleira: uma operação do Ministério Público do RS apreendeu cinco toneladas de produtos estragados em três mercados gaúchos. Um dos estabelecimentos foi totalmente interditado e o dono acabou preso. Fica o alerta: confira sempre a validade — e denuncie irregularidades à Vigilância Sanitária ou ao Procon.",
  "hashtags": ["#SegurançaAlimentar", "#MPRS", "#Consumidor", "#RioGrandeDoSul", "#Fiscalização", "#SulTV"]
 },
 "roteiro_short_60s": {
  "abertura_2s": "Vinhos vencidos há nove anos à venda no RS.",
  "desenvolvimento_45s": "Uma operação de fiscalização do Ministério Público do Rio Grande do Sul apreendeu cinco toneladas de produtos estragados em três mercados do estado — entre eles, vinhos vencidos há nove anos. Um dos estabelecimentos teve interdição total e o proprietário foi preso. Produtos vencidos e mal armazenados representam risco real à saúde. O consumidor deve conferir a validade na gôndola e denunciar irregularidades à Vigilância Sanitária do município ou ao Procon.",
  "fechamento_8s": "A fiscalização segue em outros estabelecimentos do estado.",
  "cta_5s": "Mais notícias do RS no site da SulTV.",
  "trilha_sugerida": "tensa-leve"
 },
 "tag_thumbnail": "FISCALIZAÇÃO",
 "briefing_visual": {
  "descricao_pt": "Garrafas de vinho empoeiradas em prateleira de mercado, foco nas garrafas antigas, sem marcas legíveis nem pessoas",
  "query_en": ["dusty wine bottles shelf", "old wine bottles store shelf", "expired products supermarket shelf"],
  "evitar": ["marcas e rótulos legíveis", "pessoas", "logos de redes de mercado", "texto"],
  "prompt_ia": "Close-up of dusty old wine bottles on a dimly lit supermarket shelf, labels blurred and unreadable, moody lighting suggesting neglect, no people, no readable brands, no text, editorial photojournalism style"
 }
},

# ============================ REBAIXAR (5) ============================

"74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Aviso administrativo interno (revisão de contracheques de servidores de Barra do Ribeiro), sem corpo de texto; público restrito — vira nota interna."
},
"d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Manifestações de parlamentares sobre privatizações/PPPs tangenciam disputa partidária (guardrail de cautela); sem fato novo concreto além do debate."
},
"49348b06a39337d964518e54a7715142418ea220": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Pauta de evento já realizado (audiência de 29/05, mais de uma semana atrás); tema perene mas sem gancho de atualidade hoje."
},
"014b0c7e7ebe83a7e9d2818d435714326ff6390e": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "Pauta institucional universitária (UFSM/Rede HU+) distante do núcleo geográfico; relevância indireta para a audiência da Costa Doce."
},
"66d5a1e7554d8aeb42f8b71516c7a70ec6e076ab": {
 "decisao_final": "REBAIXAR",
 "decisao_motivo": "História humana positiva, mas fora da área de cobertura núcleo (Venâncio Aires) e envolvendo pessoa em situação sensível — exigiria apuração própria antes de publicar."
},

# ============================ BLOQUEAR (21) ============================

"a3c43bdca9d47601b35735bf588edb24bac0170a": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Conteúdo publicitário/institucional de cooperativa (URL de seção 'publicidade'); não é pauta jornalística."
},
"71d8e4c166749fecf87911b126851418544f1bfb": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Duplicata: matéria Fiergs/robótica publicada em 2026-06-06 (match id_hash + título no histórico)."
},
"e8243e7e1901a6c9be6fc53a4655813d09f9cca9": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Pauta vencida (prazo do Enem encerrou sexta 05/06; hoje é domingo 07/06) e fato já coberto em publicação anterior sobre as inscrições."
},
"5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Duplicata em substância: cursos de qualificação de Arambaré já publicados (histórico); título raspado com data de 16/04 indica conteúdo antigo."
},
"7328151d0f689699ca147e00ec7ffb87008ee51e": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Conteúdo antigo raspado do site da prefeitura (datado de 19/01/2026); sem gancho de atualidade."
},
"e01838afcd9335ee307b79a73b8b0bf111bfe4ba": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Edital procedural (publicação de penalidade), datado de 30/03; sem interesse jornalístico."
},
"7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Edital procedural sem corpo de texto nem data confirmada; tema (perímetro urbano) pode render pauta futura com apuração própria."
},
"09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Título genérico de aviso ('AVISO DE AUDIÊNCIA PÚBLICA') sem corpo de texto — sem o quê/quando/onde, não há matéria."
},
"c77c704f766cfa913b42a8d2b37cfc4c03320244": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Aviso procedural sobre emissor de notas fiscais, datado de 05/05; sem interesse jornalístico atual."
},
"6d583901d0b2623e718e91c071da59f2069c1522": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Duplicata: lei de fogos sem estampido de Barra do Ribeiro já publicada (match id_hash + título no histórico)."
},
"5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Duplicata: calçamento da Rua Camaquã (Cristal) publicado em 2026-06-06 (match id_hash + URL + título)."
},
"4ceb630b463e5a73d241cc134657509620995c00": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Duplicata: selo Amigo da Vacina de São Lourenço do Sul já publicado (match título no histórico)."
},
"ff08241618128d19c4b248113b1c116cebb5459a": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Duplicata: mesmo item do selo Amigo da Vacina, repetido na própria coleta (match id_hash + título)."
},
"804da2cbe08274dd604274d8db6acc48cc218fed": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Duplicata: limpeza da Avenida Passo do Mendonça (Cristal) publicada em 2026-06-06 (match id_hash + URL + título)."
},
"5243be736e2649528d6bc837fd8bbde97e1353d1": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Duplicata: associação dos produtores de morango de Pelotas publicada em 2026-06-06 (match id_hash + título)."
},
"01e4af8f22701aee0014a55e168747935cd1d8cd": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Duplicata: matéria do El Niño/neve publicada em 2026-06-06 (match id_hash + título)."
},
"ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Duplicata: renegociação de dívidas no Senado publicada em 2026-06-06 (match id_hash + título)."
},
"52a34cdaeffd6c322e99946d7c0ec9b186f6071c": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Aviso interno de TI da UFSM (Moodle indisponível); irrelevante para a audiência."
},
"1b65b50064ef2eda1d5c750a134327ce1c8a465f": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Esporte de região distante do núcleo (Venâncio Aires) e categoria sub-15 (envolve menores) — fora da régua editorial."
},
"afe430799de79547d2d9b7086008075f10225dbc": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Promoção comercial (sorteio de scooter por empresa na ExpoBento); conteúdo publicitário."
},
"0476dd3a86bfea166e89841310b3c479865f2ca6": {
 "decisao_final": "BLOQUEAR",
 "decisao_motivo": "Conteúdo publicitário de loja (Havan Garibaldi); não é pauta jornalística."
},
}

# ============================ MATÉRIAS LONGAS (4) ============================

MATERIAS = {

"1fb11c1f31a01fb5ce1038c92ebe74fa30835b80": """### Título ###
Atleta de Camaquã conquista título mundial de jiu-jitsu na faixa azul

### Artigo ###
Camaquã, na região da Costa Doce, ganhou um campeão mundial. O atleta camaquense Murilo Cardoso conquistou o título do Mundial de Jiu-Jitsu na faixa azul, resultado inédito na sua trajetória esportiva. Ao celebrar a conquista, o atleta fez questão de dividir o mérito com a cidade, destacando o apoio que sempre recebeu da comunidade camaquense ao longo da carreira — do incentivo nos campeonatos regionais à torcida nas competições de maior porte. A faixa azul é uma das primeiras graduações do jiu-jitsu e concentra um número expressivo de competidores em torneios internacionais, o que torna o título ainda mais disputado: para chegar ao topo, o atleta precisa superar adversários de delegações de todo o mundo. A conquista de Murilo Cardoso projeta o esporte da Costa Doce no cenário internacional e reforça um movimento que vem crescendo no interior gaúcho, onde academias de artes marciais têm formado atletas competitivos e ampliado o acesso de crianças e jovens ao esporte. Para a comunidade esportiva de Camaquã, o título funciona como vitrine e inspiração — mostra que é possível sair de uma cidade do interior do Rio Grande do Sul e subir ao lugar mais alto do pódio mundial. A expectativa agora é que o resultado abra portas para novas competições e atraia mais apoio para o desenvolvimento do jiu-jitsu na região.

### Legenda sugerida ###
Murilo Cardoso celebrou o título inédito e destacou o apoio da comunidade camaquense

### Palavras-chave ###
Camaquã, jiu-jitsu, Murilo Cardoso, título mundial, esporte, Costa Doce
""",

"a6885d87261ed899066eaed1e127d684baa35ba1": """### Título ###
Justiça do Trabalho gaúcha fecha R$ 156,8 milhões em acordos na Semana da Conciliação

### Artigo ###
A Justiça do Trabalho do Rio Grande do Sul homologou R$ 156,8 milhões em acordos durante a 10ª Semana Nacional da Conciliação Trabalhista, realizada entre os dias 25 e 29 de maio. O montante, fechado em apenas cinco dias de mutirão, reflete a adesão crescente de trabalhadores e empresas a um caminho mais rápido para encerrar disputas: na conciliação, as partes constroem um entendimento que é homologado pelo juiz, encerrando o processo sem a espera — que pode levar anos — por uma sentença definitiva e seus recursos. Para o trabalhador, o acordo significa receber valores com mais agilidade; para a empresa, reduzir custos com o litígio e eliminar a imprevisibilidade de uma condenação futura. A Semana Nacional da Conciliação é promovida anualmente pela Justiça do Trabalho em todo o país, mas o instrumento está disponível o ano inteiro: qualquer das partes pode pedir a conciliação em qualquer fase do processo, inclusive nas varas do trabalho que atendem os municípios da Zona Sul e da Costa Doce. O resultado gaúcho desta edição reforça uma tendência consolidada no Judiciário trabalhista, que tem investido em métodos de solução consensual de conflitos como forma de desafogar as pautas de julgamento e dar resposta mais rápida ao cidadão. Trabalhadores e empregadores da região que possuem processos em andamento podem consultar seus advogados sobre a possibilidade de buscar um acordo.

### Legenda sugerida ###
Valor foi homologado em cinco dias durante a 10ª Semana Nacional da Conciliação Trabalhista

### Palavras-chave ###
Justiça do Trabalho, conciliação, acordos trabalhistas, Rio Grande do Sul, economia, trabalhador
""",

"da4142fbb0edad6b837e4d203d5fe4dd944d642b": """### Título ###
É falso que ciclones gêmeos vão atingir o Brasil, apontam meteorologistas

### Artigo ###
Um alerta falso sobre a formação de supostos ciclones gêmeos no litoral do Brasil circula nas redes sociais, apontando riscos para a população do Sul e do Sudeste do país. Meteorologistas verificaram as publicações e a conclusão é direta: não há qualquer previsão desse tipo de fenômeno para os próximos dias. As imagens e os textos que acompanham o boato não correspondem aos modelos meteorológicos oficiais, que seguem indicando condições dentro da normalidade para o período. O Rio Grande do Sul é especialmente sensível a esse tipo de desinformação. Desde as enchentes de 2024, alertas falsos sobre eventos climáticos extremos encontram terreno fértil entre os gaúchos e provocam pânico desnecessário, sobrecarregando canais de atendimento e, pior, desgastando a credibilidade dos avisos verdadeiros — aqueles que efetivamente salvam vidas quando um evento severo se aproxima. A orientação para a população da Costa Doce e de todo o estado é simples: previsões e alertas devem ser conferidos exclusivamente nos canais oficiais, como o Instituto Nacional de Meteorologia e a Defesa Civil estadual e municipal, que mantêm cadastro gratuito de avisos por mensagem de celular. Antes de compartilhar qualquer alerta recebido em grupos de aplicativos, vale verificar a origem da informação. Em tempos de clima instável, informação errada também causa estrago — e a checagem é a primeira ferramenta de proteção.

### Legenda sugerida ###
Boato circula nas redes sociais; previsões oficiais não indicam fenômeno semelhante

### Palavras-chave ###
ciclones gêmeos, fake news, meteorologia, Defesa Civil, Rio Grande do Sul, checagem
""",

"8c10d704aa76774d2be1bdb6d93ca335fbf9061b": """### Título ###
Vinhos vencidos há 9 anos: operação apreende 5 toneladas de produtos estragados no RS

### Artigo ###
Cinco toneladas de produtos estragados, entre eles vinhos vencidos há nove anos, foram apreendidas em uma operação de fiscalização do Ministério Público do Rio Grande do Sul em três mercados do estado. A situação encontrada em um dos estabelecimentos foi considerada pelos agentes uma das piores já registradas em fiscalizações do tipo: o local teve interdição total e o proprietário acabou preso. As equipes confiscaram alimentos e bebidas impróprios para o consumo, que serão descartados conforme as normas sanitárias. Produtos vencidos ou mal armazenados representam risco concreto à saúde do consumidor, podendo causar intoxicações alimentares e outras complicações — e a responsabilidade pela retirada das gôndolas é do comerciante, que responde civil e criminalmente pela venda de mercadoria estragada. Para o consumidor da Costa Doce e de toda a região, o caso reforça cuidados simples que fazem diferença: conferir a data de validade antes de levar o produto, observar as condições de conservação e refrigeração nas prateleiras e desconfiar de preços muito abaixo do praticado no mercado. Irregularidades podem ser denunciadas à Vigilância Sanitária do município, ao Procon ou diretamente ao Ministério Público, que mantém canais de atendimento ao cidadão. A fiscalização integra um trabalho permanente de proteção ao consumidor gaúcho e deve alcançar outros estabelecimentos do estado nas próximas etapas.

### Legenda sugerida ###
Fiscalização encontrou alimentos e bebidas impróprios em três mercados gaúchos

### Palavras-chave ###
vinhos vencidos, fiscalização, Ministério Público, segurança alimentar, consumidor, Rio Grande do Sul
""",
}


def main():
    data = json.loads(APROVADAS.read_text(encoding="utf-8"))
    aprovadas = data["aprovadas"] if isinstance(data, dict) and "aprovadas" in data else data

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
