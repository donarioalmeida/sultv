#!/usr/bin/env python3
"""
angular_dia_2026_06_03.py — angulação editorial + redação (cowork-faz-tudo).

Gera state/pauta_2026-06-03.json + state/materias_2026-06-03/<id_hash>.md
a partir de state/aprovadas_2026-06-03.json.

Decisões do dia (Claude na sessão):
  PUBLICAR  (9): 2,5,11,12,13,14,20,22 (materia_longa) + 26 (post)
  REBAIXAR (13): 0,3,4,15,16,18,19,21,23,25,27,28,29
  BLOQUEAR  (8): 1,6,7,8,9,10,17,24
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-03"


def rebaixar(motivo):
    return {
        "titulo_sultv": "", "chamada_faixa": "", "subtitulo": "", "lead": "",
        "ganchos_3": [], "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "", "decisao_final": "REBAIXAR", "decisao_motivo": motivo,
    }


def bloquear(motivo):
    d = rebaixar(motivo)
    d["decisao_final"] = "BLOQUEAR"
    return d


PAUTA_ANGULADA = {
    # ---------- BLOQUEAR ----------
    "39040e1f1cb77f03aacbf3ca232d766172a316ea": bloquear(
        "Promoção de programa (podcast Clic Cast) de veículo concorrente — não é fato jornalístico próprio."),
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": bloquear(
        "Edital de penalidade procedural (Nº 001/2026) — conteúdo administrativo sem interesse editorial."),
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": bloquear(
        "Edital procedural de abertura de prazo para requerimentos — administrativo, sem fato ancorável."),
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": bloquear(
        "Aviso de audiência pública sem assunto definido no título — cabeçalho procedural genérico."),
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": bloquear(
        "Aviso administrativo sobre emissão de notas fiscais — serviço procedural, não é notícia."),
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": bloquear(
        "Cabeçalho de seção 'Secretaria da Administração' + aviso de contracheques — não é fato único."),
    "c9d7816f567a0929b8e43b9848b721dbcd3d6ed5": bloquear(
        "Edital de leilão e intimação judicial com nome próprio — procedural + guardrail de exposição pessoal."),
    "52a34cdaeffd6c322e99946d7c0ec9b186f6071c": bloquear(
        "Aviso técnico de indisponibilidade de sistema (Moodle UFSM) — serviço de TI, não é notícia."),

    # ---------- REBAIXAR ----------
    "0521400d7f8aa15253ee5cea32ba0725d2b07412": rebaixar(
        "Promoção comercial de varejista (sorteio de TVs) — publicidade, não fato jornalístico."),
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": rebaixar(
        "Cidade-núcleo, mas matéria de prefeitura datada de abril/2026 — inscrições provavelmente encerradas (conteúdo vencido)."),
    "7328151d0f689699ca147e00ec7ffb87008ee51e": rebaixar(
        "Cidade-núcleo, mas anúncio datado de janeiro/2026 — informação defasada para a pauta diária."),
    "4b00032a83f85b029fab249533ae2623085a7c83": rebaixar(
        "Processo de licitação/contratação procedural e confuso, sem ancoragem clara de fato — vira nota interna."),
    "804da2cbe08274dd604274d8db6acc48cc218fed": rebaixar(
        "Segundo item de serviço viário de Cristal no mesmo dia (similar ao calçamento da Rua Camaquã, score menor) — evita redundância."),
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": rebaixar(
        "Cobertura legislativa institucional (concessões/PPPs) com viés político-partidário potencial e baixa âncora factual regional."),
    "49348b06a39337d964518e54a7715142418ea220": rebaixar(
        "Detalhamento técnico de legislação (Funcriança) — baixa âncora regional e tema sensível a menores."),
    "da4142fbb0edad6b837e4d203d5fe4dd944d642b": rebaixar(
        "Fact-check de boato de escopo nacional ('ciclones gêmeos no Brasil') — sem âncora Sul-RS específica."),
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": rebaixar(
        "Apreensão de vinhos vencidos — fato de 14/05 (20 dias), defasado para pauta diária e de tom sensacionalista."),
    "f5683bac6713586e9f3dbe7b7c32643cd52bf560": rebaixar(
        "Cultura em Santa Maria (rádio universitária) — fora do núcleo Costa Doce, baixa prioridade; mantém só como nota."),
    "e91146e4fc1e208b0a15335c6a9c833f921e9936": rebaixar(
        "Obra cultural em Venâncio Aires — fora do núcleo, fato futuro (entrega em julho), baixa âncora."),
    "a354329526fb680045e13475a554761fb1b32029": rebaixar(
        "Apreensão de drone com drogas em Caxias do Sul — Serra Gaúcha, região distante do núcleo Costa Doce; tema policial."),
    "44b5ced0f6df4f3ca299f82937b050fd6c5ace6f": rebaixar(
        "Exposição cultural em Bento Gonçalves — Serra Gaúcha, fora do núcleo, baixa prioridade."),

    # ---------- PUBLICAR ----------
    # 2 — Banda Municipal de Barão do Triunfo recebe novos uniformes
    "539b54a2d1a0b4698d2496905ad6ae78fc29ad7d": {
        "titulo_sultv": "Banda Municipal de Barão do Triunfo recebe novos uniformes e retoma tradição cultural",
        "chamada_faixa": "Banda de Barão do Triunfo ganha novos uniformes",
        "subtitulo": "Entrega oficial dos uniformes marca a retomada da banda e reforça a vida cultural do município da Costa Doce.",
        "lead": "A Banda Municipal de Barão do Triunfo recebeu oficialmente novos uniformes em cerimônia da Administração Municipal, em um gesto que marca a retomada de uma das tradições culturais mais antigas da cidade. O reforço valoriza os músicos locais e devolve à comunidade um símbolo de identidade que acompanha datas cívicas e festivas do município da Costa Doce.",
        "ganchos_3": [
            "Uniformes novos entregues em cerimônia oficial",
            "Banda Municipal retoma atividades e tradição",
            "Cultura local reforçada em Barão do Triunfo"
        ],
        "angulo_editorial": "Cultura e comunidade em município da Costa Doce — fato concreto (entrega de uniformes) com forte valor identitário e simbólico para a audiência regional. Pauta positiva de valorização cultural.",
        "fontes_complementares_sugeridas": ["Prefeitura de Barão do Triunfo", "Secretaria de Cultura municipal", "regente da Banda Municipal"],
        "lead_materia_longa": "A Banda Municipal de Barão do Triunfo recebeu oficialmente novos uniformes em cerimônia da Administração Municipal, marcando a retomada de uma das tradições culturais mais antigas do município da Costa Doce.",
        "post_instagram": {
            "caption": "A música está de volta às ruas de Barão do Triunfo. A Banda Municipal recebeu novos uniformes em cerimônia oficial, marcando a retomada de uma tradição que acompanha as datas mais importantes da cidade. Um reforço para a cultura e para quem faz a banda acontecer.",
            "hashtags": ["#BarãoDoTriunfo", "#BandaMunicipal", "#Cultura", "#CostaDoce", "#SulTV", "#TradiçãoGaúcha"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Banda de Barão do Triunfo renovada.",
            "desenvolvimento_45s": "A Banda Municipal de Barão do Triunfo recebeu novos uniformes em cerimônia oficial da Administração Municipal. Mais do que roupa nova, a entrega marca a retomada de uma das tradições culturais mais antigas do município da Costa Doce. A banda acompanha desfiles cívicos, festas e datas importantes, levando música às ruas e fortalecendo o sentimento de pertencimento da comunidade. O investimento valoriza os músicos locais e estimula novas gerações a manterem viva essa tradição.",
            "fechamento_8s": "Tradição cultural de volta às ruas.",
            "cta_5s": "Mais no SulTV.",
            "trilha_sugerida": "banda marcial instrumental leve"
        },
        "tag_thumbnail": "Banda Municipal",
        "briefing_visual": {
            "descricao_pt": "Banda municipal de sopros e percussão em desfile de rua em cidade pequena do interior do RS, instrumentos brilhando ao sol, sem rostos identificáveis em close",
            "query_en": ["municipal marching band street", "brass band parade small town", "community band instruments outdoor"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "A municipal brass and percussion band marching on a small-town street in southern Brazil, instruments gleaming in daylight, festive community atmosphere, no identifiable faces in close-up, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato concreto de cultura na Costa Doce, fonte regional confiável, item novo (02/06) e de forte vínculo identitário."
    },

    # 5 — Camaquã: medidas contra doenças respiratórias no inverno
    "18beb09aabef8a73a0972181dea3b3b739b72536": {
        "titulo_sultv": "Camaquã reforça ações de saúde para enfrentar doenças respiratórias no inverno",
        "chamada_faixa": "Camaquã reforça saúde contra doenças do inverno",
        "subtitulo": "Com a chegada do frio na Costa Doce, a prefeitura amplia ações de prevenção e atendimento à população.",
        "lead": "Com a aproximação do inverno e a queda das temperaturas na Costa Doce, a Prefeitura de Camaquã colocou em prática um conjunto de ações para enfrentar o aumento sazonal das doenças respiratórias. As medidas reforçam a rede de atendimento e a prevenção em um período do ano historicamente associado à alta de casos de gripes e resfriados na região.",
        "ganchos_3": [
            "Prefeitura amplia ações para o inverno",
            "Prevenção de doenças respiratórias na Costa Doce",
            "Rede de saúde reforçada com a chegada do frio"
        ],
        "angulo_editorial": "Serviço público e utilidade à população em cidade-núcleo (Camaquã) — ação concreta de governo, sazonalmente oportuna (início do inverno). Pauta de serviço, sem qualquer recomendação médica individual.",
        "fontes_complementares_sugeridas": ["Prefeitura de Camaquã", "Secretaria Municipal de Saúde de Camaquã"],
        "lead_materia_longa": "Com a aproximação do inverno e a queda das temperaturas na Costa Doce, a Prefeitura de Camaquã colocou em prática um conjunto de ações voltadas a enfrentar o aumento sazonal das doenças respiratórias.",
        "post_instagram": {
            "caption": "O frio chegou na Costa Doce e, com ele, a temporada das doenças respiratórias. A Prefeitura de Camaquã reforçou ações de prevenção e atendimento para proteger a população neste inverno. Fique atento aos serviços de saúde do seu município.",
            "hashtags": ["#Camaquã", "#Saúde", "#Inverno", "#CostaDoce", "#SulTV", "#Prevenção"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Camaquã se prepara para o inverno.",
            "desenvolvimento_45s": "Com a chegada do frio na Costa Doce, a Prefeitura de Camaquã reforçou as ações de saúde para enfrentar o aumento das doenças respiratórias. O inverno é o período do ano em que mais crescem os casos de gripes e resfriados, e a prefeitura ampliou a prevenção e o atendimento à população. A orientação é que os moradores acompanhem os canais oficiais do município para saber onde buscar atendimento e como se proteger nesta época.",
            "fechamento_8s": "Saúde reforçada para o inverno.",
            "cta_5s": "Detalhes no SulTV.",
            "trilha_sugerida": "instrumental neutro"
        },
        "tag_thumbnail": "Saúde no inverno",
        "briefing_visual": {
            "descricao_pt": "Manhã de inverno fria com neblina sobre uma cidade do Sul do RS, pessoas agasalhadas ao longe, sem rostos identificáveis, clima úmido e frio",
            "query_en": ["cold foggy winter morning town brazil", "frost winter small town street", "misty cold morning south brazil"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "ambiente hospitalar dramático"],
            "prompt_ia": "A cold foggy winter morning over a small southern Brazilian town, bundled-up people in the distance, soft grey light, calm everyday atmosphere, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Ação concreta de governo em cidade-núcleo, oportuna no início do inverno; serviço público sem aconselhamento médico individual (fora do guardrail de saúde)."
    },

    # 11 — Barra do Ribeiro: lei proíbe fogos com estampido
    "6d583901d0b2623e718e91c071da59f2069c1522": {
        "titulo_sultv": "Barra do Ribeiro proíbe fogos com estampido por lei municipal",
        "chamada_faixa": "Barra do Ribeiro proíbe fogos com estampido",
        "subtitulo": "Lei Municipal nº 2850/2025 veta artefatos barulhentos e protege animais e pessoas sensíveis ao ruído.",
        "lead": "Barra do Ribeiro passou a proibir o uso de fogos de artifício com estampido em todo o município por meio da Lei Municipal nº 2850/2025. A medida acompanha uma tendência crescente de cidades gaúchas que vetam artefatos barulhentos para proteger animais, pessoas com sensibilidade ao ruído e a fauna local, mantendo apenas os fogos de efeito visual.",
        "ganchos_3": [
            "Lei municipal veta fogos com estampido",
            "Proteção a animais e pessoas sensíveis ao ruído",
            "Apenas fogos de efeito visual seguem permitidos"
        ],
        "angulo_editorial": "Legislação de utilidade pública em município da Costa Doce — fato concreto (lei em vigor) com forte apelo junto à audiência rural e urbana sensível à causa animal. Pauta de serviço e cidadania.",
        "fontes_complementares_sugeridas": ["Prefeitura de Barra do Ribeiro", "Câmara de Vereadores de Barra do Ribeiro", "ONGs de proteção animal"],
        "lead_materia_longa": "Barra do Ribeiro passou a proibir o uso de fogos de artifício com estampido em todo o município por meio da Lei Municipal nº 2850/2025, acompanhando a tendência de cidades gaúchas que vetam artefatos barulhentos para proteger animais e pessoas sensíveis ao ruído.",
        "post_instagram": {
            "caption": "Barra do Ribeiro disse não aos fogos barulhentos. A Lei Municipal nº 2850/2025 proíbe os fogos com estampido no município, protegendo animais e pessoas sensíveis ao ruído. Os fogos de efeito visual, sem barulho, seguem liberados. Uma medida pela convivência e pelo bem-estar animal.",
            "hashtags": ["#BarraDoRibeiro", "#BemEstarAnimal", "#FogosSemBarulho", "#CostaDoce", "#SulTV", "#Cidadania"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Barra do Ribeiro proíbe fogos barulhentos.",
            "desenvolvimento_45s": "Barra do Ribeiro aprovou uma lei que proíbe o uso de fogos de artifício com estampido em todo o município. A Lei Municipal nº 2850/2025 acompanha o movimento de várias cidades gaúchas que vetam artefatos barulhentos para proteger animais, pessoas com sensibilidade ao ruído e a fauna local. Os fogos de efeito apenas visual, sem barulho, continuam permitidos. A medida une segurança, bem-estar animal e respeito à convivência.",
            "fechamento_8s": "Fogos visuais seguem permitidos.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental suave"
        },
        "tag_thumbnail": "Fogos sem barulho",
        "briefing_visual": {
            "descricao_pt": "Cão tranquilo deitado em ambiente doméstico calmo ao entardecer, ou fogos de efeito apenas visual coloridos no céu sem multidão, sem texto",
            "query_en": ["silent fireworks colorful sky", "calm dog at home evening", "fireworks display night no crowd"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "animais assustados/sofrendo"],
            "prompt_ia": "Colorful visual-only fireworks lighting up a night sky over a small town, no crowd, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Lei municipal concreta de utilidade pública na Costa Doce, com forte apelo de bem-estar animal junto à audiência rural e urbana."
    },

    # 12 — Cristal: Rua Camaquã preparada para calçamento
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": {
        "titulo_sultv": "Cristal prepara a Rua Camaquã para obras de calçamento",
        "chamada_faixa": "Cristal prepara Rua Camaquã para calçamento",
        "subtitulo": "Serviços iniciais abrem caminho para a pavimentação de mais uma via no município da Costa Doce.",
        "lead": "A Prefeitura de Cristal iniciou os serviços de preparação da Rua Camaquã para receber obras de calçamento, dando início a mais uma etapa de qualificação da malha viária urbana do município. A intervenção atende a uma demanda antiga dos moradores e promete melhorar o acesso e a circulação em uma das ruas da cidade da Costa Doce.",
        "ganchos_3": [
            "Rua Camaquã recebe preparação para o calçamento",
            "Mais uma via qualificada em Cristal",
            "Demanda dos moradores começa a ser atendida"
        ],
        "angulo_editorial": "Infraestrutura e serviço público em cidade-núcleo (Cristal) — obra concreta com utilidade direta e cotidiana para a população. Pauta de mobilidade urbana.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria de Obras de Cristal"],
        "lead_materia_longa": "A Prefeitura de Cristal iniciou os serviços de preparação da Rua Camaquã para receber obras de calçamento, dando início a mais uma etapa de qualificação da malha viária urbana do município da Costa Doce.",
        "post_instagram": {
            "caption": "Mais uma rua de Cristal vai ganhar calçamento. A Prefeitura começou os serviços de preparação da Rua Camaquã para receber a pavimentação, atendendo uma demanda antiga dos moradores. Obra que melhora o acesso, a circulação e o dia a dia de quem vive no bairro.",
            "hashtags": ["#Cristal", "#Obras", "#Calçamento", "#CostaDoce", "#SulTV", "#Infraestrutura"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Calçamento novo a caminho em Cristal.",
            "desenvolvimento_45s": "A Prefeitura de Cristal começou a preparar a Rua Camaquã para receber obras de calçamento. É mais uma etapa de qualificação das ruas do município da Costa Doce, atendendo a uma demanda antiga dos moradores. A pavimentação melhora o acesso, organiza a circulação, ajuda na drenagem da chuva e valoriza os imóveis da região. A prefeitura orienta que a comunidade acompanhe os canais oficiais sobre o andamento e eventuais mudanças no trânsito.",
            "fechamento_8s": "Mais uma via qualificada.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental neutro"
        },
        "tag_thumbnail": "Obras na Rua Camaquã",
        "briefing_visual": {
            "descricao_pt": "Rua de terra de cidade pequena do interior do RS sendo preparada para pavimentação, máquina de obra ou base de pedras ao fundo, dia claro, sem pessoas identificáveis",
            "query_en": ["dirt road preparation paving", "street construction small town", "road groundwork machinery"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto legível", "logos"],
            "prompt_ia": "A dirt street in a small southern Brazilian town being prepared for cobblestone paving, groundwork and a small construction machine in the background, clear daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Obra concreta de mobilidade em cidade-núcleo (Cristal); serviço público útil. Dedup online no Wix é a salvaguarda contra repetição."
    },

    # 13 — São Lourenço do Sul: corrida solidária OW
    "8ac0f5e54a1446f013927374779c0bd628febc5a": {
        "titulo_sultv": "Corrida solidária movimenta o esporte e o engajamento social em São Lourenço do Sul",
        "chamada_faixa": "Corrida solidária movimenta São Lourenço do Sul",
        "subtitulo": "Projeto 'OW Aquecendo Além do Corre' une atividade física e ações de solidariedade na Costa Doce.",
        "lead": "O projeto 'OW Aquecendo Além do Corre' tem unido a prática esportiva à solidariedade em São Lourenço do Sul, mobilizando corredores da região em torno de causas sociais. A iniciativa, apresentada na rádio local pela OW Assessoria de Corrida, reforça como o esporte pode se transformar em ferramenta de engajamento comunitário em um dos municípios mais ativos da Costa Doce.",
        "ganchos_3": [
            "Esporte e solidariedade caminham juntos",
            "Corredores da Costa Doce engajados em causas sociais",
            "Assessoria local participa de maratona internacional"
        ],
        "angulo_editorial": "Esporte e comunidade em cidade-núcleo (São Lourenço do Sul) — pauta positiva que une atividade física, saúde e solidariedade, com forte apelo de engajamento social.",
        "fontes_complementares_sugeridas": ["OW Assessoria de Corrida", "SLR Rádio", "secretaria municipal de esportes"],
        "lead_materia_longa": "O projeto 'OW Aquecendo Além do Corre' tem unido a prática esportiva à solidariedade em São Lourenço do Sul, mobilizando corredores da região em torno de causas sociais, conforme apresentado na rádio local pela OW Assessoria de Corrida.",
        "post_instagram": {
            "caption": "Em São Lourenço do Sul, correr também é aquecer corações. O projeto 'OW Aquecendo Além do Corre' une o esporte à solidariedade, mobilizando corredores da Costa Doce em torno de causas sociais. Saúde, comunidade e um propósito a cada quilômetro.",
            "hashtags": ["#SãoLourençoDoSul", "#Corrida", "#Solidariedade", "#CostaDoce", "#SulTV", "#EsporteEComunidade"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Correr por uma causa em São Lourenço.",
            "desenvolvimento_45s": "Em São Lourenço do Sul, o projeto 'OW Aquecendo Além do Corre' une o esporte à solidariedade. A OW Assessoria de Corrida mobiliza corredores da Costa Doce em torno de causas sociais, mostrando que a atividade física pode ir além da saúde e virar engajamento comunitário. A equipe também marcou presença em provas de grande porte, como a Maratona Internacional de Porto Alegre, levando o nome do município para fora da região.",
            "fechamento_8s": "Esporte que aquece corações.",
            "cta_5s": "Mais no SulTV.",
            "trilha_sugerida": "instrumental motivacional leve"
        },
        "tag_thumbnail": "Corrida solidária",
        "briefing_visual": {
            "descricao_pt": "Grupo de corredores amadores em rua ou orla ao amanhecer em cidade do Sul do RS, movimento e energia, sem rostos identificáveis em close",
            "query_en": ["amateur runners group street sunrise", "running club outdoor brazil", "people jogging waterfront morning"],
            "evitar": ["rostos identificáveis em close", "marcas de patrocínio", "texto", "logos"],
            "prompt_ia": "A group of amateur runners on a lakeside street at sunrise in a southern Brazilian town, sense of movement and energy, warm morning light, no identifiable faces in close-up, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta positiva de esporte e solidariedade em cidade-núcleo (São Lourenço do Sul), item novo (02/06) com bom apelo de engajamento."
    },

    # 14 — São Lourenço do Sul: Semana do Meio Ambiente x sacolas plásticas
    "05d36f23daf2761c14c65a27910c36e80e9b16f2": {
        "titulo_sultv": "São Lourenço do Sul promove Semana do Meio Ambiente com ação contra sacolas plásticas",
        "chamada_faixa": "São Lourenço marca Semana do Meio Ambiente",
        "subtitulo": "Programação inclui mobilização no comércio para reduzir o uso de sacolas plásticas na Costa Doce.",
        "lead": "São Lourenço do Sul preparou uma programação especial para a Semana do Meio Ambiente, com destaque para uma ação junto ao comércio voltada a reduzir o uso de sacolas plásticas. A iniciativa, conduzida pela Secretaria de Planejamento e Meio Ambiente e pelo Conselho Municipal de Meio Ambiente, conecta a data ambiental a uma mudança concreta de hábitos no município da Costa Doce.",
        "ganchos_3": [
            "Semana do Meio Ambiente com programação especial",
            "Comércio mobilizado contra sacolas plásticas",
            "Mudança de hábitos em pauta na Costa Doce"
        ],
        "angulo_editorial": "Meio ambiente e cidadania em cidade-núcleo (São Lourenço do Sul) — pauta oportuna (Semana do Meio Ambiente, em torno de 5 de junho) com ação concreta e mudança de comportamento. Tema caro à audiência rural e urbana.",
        "fontes_complementares_sugeridas": ["Secretaria de Planejamento e Meio Ambiente de São Lourenço do Sul", "Conselho Municipal de Meio Ambiente (Camuma)", "CDL/associação comercial local"],
        "lead_materia_longa": "São Lourenço do Sul preparou uma programação especial para a Semana do Meio Ambiente, com destaque para uma ação junto ao comércio voltada a reduzir o uso de sacolas plásticas, conduzida pela Secretaria de Planejamento e Meio Ambiente e pelo Conselho Municipal de Meio Ambiente.",
        "post_instagram": {
            "caption": "São Lourenço do Sul entra na Semana do Meio Ambiente com uma ação prática: mobilizar o comércio contra o uso de sacolas plásticas. Pequenas mudanças de hábito que fazem diferença para a Costa Doce. Vamos juntos? 🌱",
            "hashtags": ["#SãoLourençoDoSul", "#MeioAmbiente", "#MenosPlástico", "#CostaDoce", "#SulTV", "#Sustentabilidade"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Semana do Meio Ambiente em São Lourenço.",
            "desenvolvimento_45s": "São Lourenço do Sul preparou uma programação especial para a Semana do Meio Ambiente. O destaque é uma ação junto ao comércio para reduzir o uso de sacolas plásticas, conduzida pela secretaria de meio ambiente e pelo conselho municipal. A iniciativa transforma a data ambiental em mudança concreta de hábitos, envolvendo lojistas e consumidores. É a Costa Doce dando exemplo de cuidado com o meio ambiente no dia a dia.",
            "fechamento_8s": "Menos plástico, mais consciência.",
            "cta_5s": "Confira no SulTV.",
            "trilha_sugerida": "instrumental leve e otimista"
        },
        "tag_thumbnail": "Semana do Meio Ambiente",
        "briefing_visual": {
            "descricao_pt": "Sacola de tecido reutilizável com frutas e verduras sobre balcão de comércio, ou paisagem natural preservada da Costa Doce, luz natural, sem texto",
            "query_en": ["reusable cloth shopping bag groceries", "no plastic bag eco shopping", "preserved nature lagoon brazil"],
            "evitar": ["pessoas com rosto visível", "marcas de supermercado", "texto", "logos"],
            "prompt_ia": "A reusable cloth shopping bag filled with fresh fruits and vegetables on a market counter, soft natural light, eco-friendly mood, no people, no brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta ambiental oportuna (Semana do Meio Ambiente, ~05/06) em cidade-núcleo, com ação concreta e apelo de cidadania."
    },

    # 20 — MetSul: neve há um ano x El Niño 2026
    "01e4af8f22701aee0014a55e168747935cd1d8cd": {
        "titulo_sultv": "Sul teve neve há um ano; meteorologia avalia chances de nevadas em 2026",
        "chamada_faixa": "Sul teve neve há um ano; e em 2026?",
        "subtitulo": "MetSul lembra a neve de maio de 2025 e analisa o cenário climático para o inverno deste ano no RS.",
        "lead": "Há exatamente um ano, em 29 de maio de 2025, o Rio Grande do Sul e Santa Catarina registravam neve com acumulação, fenômeno incomum para o mês de maio. Um ano depois, a meteorologia avalia as condições do inverno de 2026 e o papel dos padrões climáticos do Pacífico na probabilidade de novas nevadas no Sul do Brasil, tema que mobiliza a atenção de produtores e moradores da região.",
        "ganchos_3": [
            "Há um ano nevava no Sul do Brasil",
            "Meteorologia avalia o inverno de 2026",
            "Padrões do Pacífico influenciam as chances de neve"
        ],
        "angulo_editorial": "Clima e tempo no Sul — tema central para a audiência rural e urbana do RS, especialmente no início do inverno. Fonte especializada (MetSul). Pauta de meteorologia e impacto no campo.",
        "fontes_complementares_sugeridas": ["MetSul Meteorologia", "Inmet", "Emater-RS"],
        "lead_materia_longa": "Há exatamente um ano, em 29 de maio de 2025, o Rio Grande do Sul e Santa Catarina registravam neve com acumulação, um fenômeno incomum para o mês de maio, segundo a MetSul Meteorologia.",
        "post_instagram": {
            "caption": "Você lembra? Há um ano, o Sul do Brasil amanhecia coberto de neve em pleno mês de maio. E em 2026, será que tem nevada de novo? A meteorologia analisa o cenário do inverno deste ano no RS. O frio promete — a neve, a gente acompanha. ❄️",
            "hashtags": ["#RioGrandeDoSul", "#Clima", "#Inverno", "#MetSul", "#SulTV", "#Tempo"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Há um ano nevava no Sul.",
            "desenvolvimento_45s": "Em 29 de maio de 2025, o Rio Grande do Sul e Santa Catarina registravam neve com acumulação, algo raro para maio. Um ano depois, a meteorologia avalia as condições do inverno de 2026 e o quanto os padrões climáticos do Oceano Pacífico podem influenciar a chance de novas nevadas. Para quem vive e produz no Sul, entender o clima é essencial: ele define o ritmo da lavoura, o cuidado com os animais e a rotina das cidades. O SulTV acompanha as próximas previsões.",
            "fechamento_8s": "O inverno gaúcho promete.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental atmosférico frio"
        },
        "tag_thumbnail": "Neve no Sul",
        "briefing_visual": {
            "descricao_pt": "Paisagem rural do Sul do Brasil coberta por geada ou fina camada de neve ao amanhecer, campo e cerca de madeira, luz fria, sem pessoas",
            "query_en": ["frost covered field sunrise south brazil", "snow rural landscape fence", "frozen pasture winter morning"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "montanhas alpinas estrangeiras óbvias"],
            "prompt_ia": "A rural pasture in southern Brazil covered by frost and a thin layer of snow at sunrise, wooden fence, cold blue light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima/tempo é conteúdo central para a audiência do RS no início do inverno; fonte especializada confiável (MetSul)."
    },

    # 22 — Canal Rural: renegociação de dívidas no Senado (RS)
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "titulo_sultv": "Produtores do RS acompanham com apreensão a votação da renegociação de dívidas no Senado",
        "chamada_faixa": "RS teme votação da renegociação de dívidas",
        "subtitulo": "Setor rural gaúcho receia ficar sem acesso ao crédito para a próxima safra caso a medida não avance.",
        "lead": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas no Senado, temendo que a falta de aprovação comprometa o acesso ao crédito para a próxima safra. Depois de sucessivas adversidades climáticas, o tema é tratado como prioritário pelo setor, que vê na medida uma condição para manter a atividade no campo e garantir o plantio.",
        "ganchos_3": [
            "Votação no Senado preocupa o campo gaúcho",
            "Acesso ao crédito da próxima safra em risco",
            "Setor rural pressiona por aprovação da medida"
        ],
        "angulo_editorial": "Agronegócio e crédito rural — pauta de altíssima relevância para a audiência produtora do RS, com impacto direto na próxima safra. Conteúdo de parceiro (Canal Rural) curado para a Costa Doce. Tema econômico, sem viés partidário.",
        "fontes_complementares_sugeridas": ["Canal Rural", "Farsul", "Senado Federal", "sindicatos rurais do RS"],
        "lead_materia_longa": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas no Senado, temendo que a ausência de aprovação comprometa o acesso ao crédito para a próxima safra.",
        "post_instagram": {
            "caption": "'A gente não dorme mais.' O campo gaúcho vive dias de tensão com a votação da renegociação de dívidas no Senado. Depois de tantas adversidades climáticas, produtores do RS temem ficar sem crédito para plantar a próxima safra. Uma pauta que define o futuro de muitas famílias rurais.",
            "hashtags": ["#Agro", "#RioGrandeDoSul", "#CréditoRural", "#Safra", "#SulTV", "#Agronegócio"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tensão no campo gaúcho.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul acompanham com apreensão a votação da renegociação de dívidas no Senado. O receio é claro: sem a aprovação da medida, muitos podem ficar sem acesso ao crédito rural para a próxima safra. Depois de seguidas adversidades climáticas, o tema virou prioridade para o setor, que vê na renegociação uma condição para continuar produzindo. É uma pauta que vai muito além da política: ela define o futuro de milhares de famílias do campo no RS.",
            "fechamento_8s": "Crédito da safra em jogo.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental tenso e sóbrio"
        },
        "tag_thumbnail": "Crédito rural no RS",
        "briefing_visual": {
            "descricao_pt": "Produtor rural observando lavoura de soja ou arroz ao entardecer no RS, de costas, clima de incerteza, campo amplo, sem rosto identificável",
            "query_en": ["farmer looking at soybean field sunset", "rice field farmer silhouette brazil", "rural producer crop field dusk"],
            "evitar": ["rosto identificável", "marcas", "texto", "logos de partidos"],
            "prompt_ia": "A rural producer seen from behind looking over a vast soybean field at dusk in southern Brazil, mood of uncertainty, warm low light, no identifiable face, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta de agronegócio e crédito rural de altíssima relevância para o produtor do RS; conteúdo de parceiro (Canal Rural) curado, sem viés partidário."
    },

    # 26 — Folha do Mate: Chama Crioula em Rio Pardo (POST)
    "ad20280ab1849469fb74cf0a02b123da5dbd806a": {
        "titulo_sultv": "Rio Pardo sediará a 77ª Geração e Distribuição da Chama Crioula em 2026",
        "chamada_faixa": "Rio Pardo recebe a Chama Crioula 2026",
        "subtitulo": "Ato tradicionalista que acende a centelha da Semana Farroupilha será em agosto, no Parque de Exposições.",
        "lead": "Rio Pardo foi escolhida para sediar a 77ª Geração e Distribuição da Chama Crioula em 2026, um dos atos mais simbólicos do tradicionalismo gaúcho. A cerimônia, marcada para 14 de agosto no Parque de Exposições do Sindicato Rural, acende a centelha que será levada por cavalarianos a municípios de todo o Rio Grande do Sul, dando início às celebrações da cultura campeira.",
        "ganchos_3": [
            "Rio Pardo sedia a 77ª Chama Crioula",
            "Centelha será levada por cavalarianos a todo o RS",
            "Cerimônia marca o calendário tradicionalista de agosto"
        ],
        "angulo_editorial": "Tradicionalismo gaúcho — tema de forte identidade para a audiência do RS, antecipando o calendário da Semana Farroupilha. Formato post para redes sociais.",
        "fontes_complementares_sugeridas": ["Folha do Mate", "MTG-RS", "Sindicato Rural de Rio Pardo"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "A centelha da tradição já tem casa em 2026: Rio Pardo vai sediar a 77ª Geração e Distribuição da Chama Crioula. No dia 14 de agosto, no Parque de Exposições do Sindicato Rural, acende-se o fogo que cavalarianos levarão a municípios de todo o RS. A cultura campeira segue viva e a galope. 🔥🐎",
            "hashtags": ["#ChamaCrioula", "#Tradicionalismo", "#RioPardo", "#RioGrandeDoSul", "#SulTV", "#CulturaGaúcha"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A Chama Crioula tem casa em 2026.",
            "desenvolvimento_45s": "Rio Pardo vai sediar a 77ª Geração e Distribuição da Chama Crioula. No dia 14 de agosto, no Parque de Exposições do Sindicato Rural, acende-se a centelha que dá início às celebrações do tradicionalismo gaúcho. A partir dali, cavalarianos percorrem centenas de quilômetros para levar o fogo simbólico a municípios de todo o Rio Grande do Sul, mantendo viva a cultura campeira e o espírito da Semana Farroupilha.",
            "fechamento_8s": "Tradição que segue a galope.",
            "cta_5s": "Mais no SulTV.",
            "trilha_sugerida": "vanerão instrumental"
        },
        "tag_thumbnail": "Chama Crioula",
        "briefing_visual": {
            "descricao_pt": "Cavalarianos tradicionalistas gaúchos cavalgando com pilcha em campo aberto do RS, bandeira ou chama simbólica, luz dourada, sem rostos identificáveis em close",
            "query_en": ["gaucho horsemen riding field brazil", "traditional riders flag pampa", "horseback riders golden hour south brazil"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "Traditional gaucho horsemen in typical attire riding across an open field in southern Brazil carrying a symbolic flame, golden hour light, no identifiable faces in close-up, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Tradicionalismo gaúcho de forte identidade regional, antecipando o calendário farroupilha; publicado como post nas redes."
    },
}


MATERIAS = {
    "539b54a2d1a0b4698d2496905ad6ae78fc29ad7d": """### Título ###
Banda Municipal de Barão do Triunfo recebe novos uniformes e retoma tradição cultural

### Artigo ###
A Banda Municipal de Barão do Triunfo recebeu oficialmente novos uniformes em cerimônia promovida pela Administração Municipal, marcando a retomada de uma das tradições culturais mais antigas da cidade da Costa Doce. Mais do que uma renovação de vestimentas, a entrega representa o reconhecimento ao trabalho dos músicos locais e o compromisso do município com a preservação de uma manifestação que acompanha a comunidade há gerações. A banda é presença constante em desfiles cívicos, festas religiosas, datas comemorativas e eventos oficiais, levando música às ruas e reforçando o sentimento de pertencimento entre os moradores. Em cidades de pequeno porte do Rio Grande do Sul, agremiações como essa cumprem um papel que vai além do entretenimento: elas formam jovens, ocupam o tempo livre com atividade cultural saudável e mantêm viva uma linguagem artística que atravessa o tempo. A uniformização adequada também tem valor prático e simbólico, padronizando a apresentação do grupo e elevando a autoestima de quem se dedica aos ensaios e às apresentações, muitas vezes de forma voluntária. A retomada das atividades da Banda Municipal abre espaço para a renovação do repertório, a chegada de novos integrantes e o estímulo ao aprendizado musical entre crianças e adolescentes. Para a comunidade, ouvir a banda tocar é reencontrar uma memória afetiva coletiva, associada a momentos importantes da vida da cidade. A iniciativa fortalece o calendário cultural de Barão do Triunfo e serve de incentivo para que outros municípios da Costa Doce valorizem suas próprias tradições. A expectativa é de que, com o reforço, a banda amplie sua presença em eventos regionais, levando o nome do município a apresentações em outras cidades e mantendo acesa a chama de uma tradição que pertence a todos.

### Legenda sugerida ###
Banda Municipal de Barão do Triunfo recebe novos uniformes e retoma tradição cultural do município.

### Palavras-chave ###
Barão do Triunfo, Banda Municipal, cultura, uniformes, tradição, Costa Doce, música, Rio Grande do Sul
""",

    "18beb09aabef8a73a0972181dea3b3b739b72536": """### Título ###
Camaquã reforça ações de saúde para enfrentar doenças respiratórias no inverno

### Artigo ###
Com a aproximação do inverno e a queda das temperaturas na Costa Doce, a Prefeitura de Camaquã colocou em prática um conjunto de ações voltadas a enfrentar o aumento sazonal das doenças respiratórias na cidade. O inverno é, historicamente, o período do ano em que crescem os casos de gripes, resfriados e outras enfermidades ligadas ao frio e à baixa umidade, sobretudo entre crianças e idosos, considerados os grupos mais sensíveis. Diante desse cenário, a administração municipal antecipou medidas para reforçar a rede de atendimento e ampliar a prevenção, buscando reduzir o impacto da temporada sobre a população e sobre os serviços de saúde. Iniciativas como essas costumam envolver a organização do fluxo de atendimento nas unidades, a orientação à comunidade sobre cuidados básicos e a atenção redobrada aos públicos mais vulneráveis. A prevenção tem papel central nesse esforço: ambientes ventilados, higiene das mãos, atenção à hidratação e a busca por atendimento ao primeiro sinal de agravamento ajudam a evitar complicações. O planejamento antecipado permite que o município se prepare antes do pico da demanda, evitando sobrecarga e garantindo um atendimento mais ágil quando a procura aumenta. Para a comunidade da Costa Doce, ações coordenadas de saúde pública representam mais segurança em uma época do ano sempre desafiadora. A recomendação é que os moradores acompanhem os canais oficiais da Prefeitura de Camaquã para se informar sobre horários de funcionamento das unidades, campanhas em andamento e os pontos de atendimento disponíveis durante o inverno. O reforço das ações reflete a importância de tratar a sazonalidade das doenças respiratórias com planejamento, e não apenas como uma resposta emergencial, contribuindo para o bem-estar da população ao longo de toda a estação mais fria do ano.

### Legenda sugerida ###
Camaquã reforça ações de saúde e prevenção para enfrentar as doenças respiratórias do inverno.

### Palavras-chave ###
Camaquã, saúde, inverno, doenças respiratórias, prevenção, Costa Doce, serviço público, Rio Grande do Sul
""",

    "6d583901d0b2623e718e91c071da59f2069c1522": """### Título ###
Barra do Ribeiro proíbe fogos com estampido por lei municipal

### Artigo ###
Barra do Ribeiro passou a proibir o uso de fogos de artifício com estampido em todo o território do município por meio da Lei Municipal nº 2850/2025. A medida acompanha um movimento crescente entre as cidades gaúchas, que vêm restringindo os artefatos barulhentos para proteger animais, pessoas com sensibilidade ao ruído e a fauna local, enquanto mantêm liberados apenas os fogos de efeito visual, sem explosão sonora. O barulho intenso provocado pelos fogos tradicionais é uma das principais causas de sofrimento para cães, gatos e outros animais, que reagem com medo, fuga e estresse, e também afeta pessoas com transtornos sensoriais, idosos e bebês. Para a fauna silvestre, o impacto se traduz em desorientação e abandono de ninhos. Ao restringir os estampidos, a legislação busca conciliar a tradição das comemorações com o bem-estar coletivo, mostrando que é possível celebrar sem causar transtorno. Os fogos de efeito apenas visual, que produzem cores e luzes no céu sem o estrondo, seguem permitidos e oferecem uma alternativa segura para festas, eventos e datas comemorativas. A aprovação da lei reflete uma mudança de mentalidade que ganha força no Rio Grande do Sul e no país, impulsionada por entidades de proteção animal e por moradores sensíveis à causa. A efetividade da norma, no entanto, depende da divulgação e da conscientização da população, para que a regra seja compreendida e respeitada no dia a dia. Cabe ao poder público orientar comerciantes e organizadores de eventos sobre o que é permitido, evitando autuações e garantindo a adaptação ao novo cenário. Para Barra do Ribeiro, a medida representa um avanço em cidadania e convivência, alinhando o município a uma pauta cada vez mais presente nas comunidades da Costa Doce. Os interessados devem procurar os canais oficiais da prefeitura para esclarecer dúvidas sobre a aplicação da lei.

### Legenda sugerida ###
Lei Municipal nº 2850/2025 proíbe fogos com estampido em Barra do Ribeiro; fogos visuais seguem permitidos.

### Palavras-chave ###
Barra do Ribeiro, fogos com estampido, Lei 2850/2025, bem-estar animal, proteção animal, Costa Doce, cidadania, Rio Grande do Sul
""",

    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": """### Título ###
Cristal prepara a Rua Camaquã para obras de calçamento

### Artigo ###
A Prefeitura de Cristal iniciou os serviços de preparação da Rua Camaquã para receber obras de calçamento, dando início a mais uma etapa de qualificação da malha viária urbana do município da Costa Doce. A intervenção começa com os trabalhos de terraplanagem e nivelamento do solo, etapas essenciais para garantir a durabilidade e a qualidade do futuro pavimento. A pavimentação de ruas é uma das demandas mais frequentes da população nas cidades de pequeno e médio porte do Rio Grande do Sul, já que vias sem calçamento sofrem com poeira no tempo seco, lama nos períodos de chuva e dificuldades de acesso para moradores, veículos e serviços públicos. Ao preparar a Rua Camaquã, a administração municipal responde a uma reivindicação antiga da comunidade e sinaliza a continuidade de um trabalho de melhoria da infraestrutura urbana. O calçamento traz benefícios concretos e duradouros: melhora o tráfego de veículos, facilita a chegada de ambulâncias, ônibus escolares e caminhões de coleta, organiza o escoamento da água da chuva e valoriza os imóveis da região. Para os moradores, a obra representa mais conforto, segurança e qualidade de vida no dia a dia, além de reduzir os transtornos causados pelas condições precárias da via. Obras desse tipo também têm efeito sobre a economia local, ao melhorar a circulação e o acesso a comércios e serviços. A administração orienta que a população acompanhe os canais oficiais da Prefeitura de Cristal para se informar sobre o cronograma das etapas, eventuais alterações temporárias no trânsito e os próximos trechos contemplados pelo programa de pavimentação. A expectativa é de que, concluída a preparação, a execução do calçamento avance dentro do planejamento previsto, entregando à comunidade mais uma via qualificada e em condições adequadas de uso.

### Legenda sugerida ###
Cristal inicia a preparação da Rua Camaquã para obras de calçamento, atendendo demanda dos moradores.

### Palavras-chave ###
Cristal, Rua Camaquã, calçamento, pavimentação, infraestrutura urbana, obras, Costa Doce, mobilidade
""",

    "8ac0f5e54a1446f013927374779c0bd628febc5a": """### Título ###
Corrida solidária movimenta o esporte e o engajamento social em São Lourenço do Sul

### Artigo ###
O projeto 'OW Aquecendo Além do Corre' tem unido a prática esportiva à solidariedade em São Lourenço do Sul, mobilizando corredores da região em torno de causas sociais e mostrando como o esporte pode ir além do desempenho físico. A iniciativa foi apresentada no programa de rádio local pela equipe da OW Assessoria de Corrida, que destacou tanto o trabalho social quanto a participação em provas de grande porte, como a Maratona Internacional de Porto Alegre. A proposta combina dois valores que conversam diretamente com a comunidade da Costa Doce: o cuidado com a saúde, por meio da atividade física regular, e o espírito de cooperação, traduzido em ações que ajudam quem precisa. A corrida, modalidade acessível e democrática, tem crescido em todo o Rio Grande do Sul, atraindo pessoas de diferentes idades e níveis de preparo. Assessorias como a OW cumprem um papel importante nesse movimento, ao orientar a prática de forma segura, prevenir lesões e estimular a constância dos praticantes. Quando esse trabalho se associa a uma causa social, o impacto se multiplica, transformando treinos e provas em oportunidades de mobilização e arrecadação em favor de quem mais necessita. A presença da equipe em maratonas de destaque também projeta o nome de São Lourenço do Sul para além das fronteiras do município, valorizando os atletas locais e inspirando novos praticantes. Para a cidade, iniciativas como essa fortalecem o esporte amador, promovem hábitos saudáveis e estimulam o senso de comunidade, criando uma rede de pessoas unidas por um propósito comum. O exemplo reforça a ideia de que o esporte é uma ferramenta poderosa de transformação social, capaz de aquecer não apenas o corpo, mas também o coração de quem participa e de quem é beneficiado pelas ações.

### Legenda sugerida ###
Projeto 'OW Aquecendo Além do Corre' une esporte e solidariedade em São Lourenço do Sul.

### Palavras-chave ###
São Lourenço do Sul, corrida, esporte, solidariedade, OW Assessoria, Costa Doce, engajamento social, saúde
""",

    "05d36f23daf2761c14c65a27910c36e80e9b16f2": """### Título ###
São Lourenço do Sul promove Semana do Meio Ambiente com ação contra sacolas plásticas

### Artigo ###
São Lourenço do Sul preparou uma programação especial para a Semana do Meio Ambiente, com destaque para uma ação junto ao comércio voltada a reduzir o uso de sacolas plásticas no município da Costa Doce. A iniciativa é conduzida pela Secretaria Municipal de Planejamento e Meio Ambiente em parceria com o Conselho Municipal de Meio Ambiente, e foi divulgada em programa de rádio local pelas representantes das duas instâncias. A escolha de transformar a data ambiental em uma mobilização concreta, em vez de apenas comemorativa, reforça a ideia de que a preservação do meio ambiente passa por mudanças cotidianas de hábito. As sacolas plásticas estão entre os itens de maior impacto ambiental: de uso muitas vezes único e de descarte rápido, levam décadas para se decompor e representam uma ameaça constante a rios, lagoas e à fauna, especialmente em uma região marcada pela presença da Laguna dos Patos e por forte vocação rural e pesqueira. Ao envolver o comércio, a ação alcança o ponto exato em que o consumo acontece, estimulando lojistas e consumidores a adotarem alternativas como sacolas retornáveis, de tecido ou de materiais biodegradáveis. Campanhas educativas como essa têm efeito duplo: reduzem a geração de resíduos no curto prazo e ajudam a construir, no longo prazo, uma cultura de consumo mais consciente. A Semana do Meio Ambiente, celebrada em torno do dia 5 de junho, é o momento ideal para colocar esses temas em evidência e engajar a população. Para São Lourenço do Sul, a iniciativa reafirma o compromisso do município com a sustentabilidade e serve de exemplo para outras cidades da Costa Doce. A população é convidada a acompanhar a programação completa pelos canais oficiais da prefeitura e a aderir às práticas propostas, contribuindo para a proteção do meio ambiente da região.

### Legenda sugerida ###
Semana do Meio Ambiente em São Lourenço do Sul mobiliza o comércio contra o uso de sacolas plásticas.

### Palavras-chave ###
São Lourenço do Sul, Semana do Meio Ambiente, sacolas plásticas, sustentabilidade, meio ambiente, Costa Doce, consumo consciente, Rio Grande do Sul
""",

    "01e4af8f22701aee0014a55e168747935cd1d8cd": """### Título ###
Sul teve neve há um ano; meteorologia avalia chances de nevadas em 2026

### Artigo ###
Há exatamente um ano, em 29 de maio de 2025, o Rio Grande do Sul e Santa Catarina registravam neve com acumulação, um fenômeno raro para o mês de maio e que mobilizou a atenção de moradores e produtores de toda a Região Sul. Um ano depois, com a chegada do inverno de 2026, a meteorologia volta a analisar as condições atmosféricas e a probabilidade de novas nevadas no Sul do Brasil, em um tema que desperta tanto curiosidade quanto preocupação no campo. As nevadas no Brasil são eventos pouco frequentes e dependem da combinação de fatores específicos, como a entrada de massas de ar muito frias, a presença de umidade e temperaturas suficientemente baixas em altitude. Os padrões climáticos de larga escala, ligados às condições do Oceano Pacífico, ajudam a moldar o comportamento do inverno e influenciam a maior ou menor probabilidade desses fenômenos. Para a audiência rural do Rio Grande do Sul, acompanhar a previsão do tempo é parte essencial da rotina, já que o clima define o ritmo das lavouras, o manejo dos rebanhos e o planejamento das atividades do campo. O frio intenso exige cuidados redobrados com animais, plantações sensíveis e com a própria população, especialmente os grupos mais vulneráveis. Episódios de geada forte, por exemplo, podem afetar culturas e pastagens, com reflexos diretos na produção. Independentemente de a neve se confirmar ou não, o inverno gaúcho costuma trazer temperaturas baixas que demandam atenção e preparo. A recomendação dos especialistas é acompanhar as atualizações das previsões ao longo da estação, já que o cenário pode mudar conforme a evolução das condições atmosféricas. O SulTV seguirá acompanhando as informações meteorológicas e seus impactos sobre o campo e as cidades da região, mantendo a comunidade informada sobre o que esperar do inverno deste ano.

### Legenda sugerida ###
Há um ano nevava no Sul do Brasil; meteorologia avalia as chances de novas nevadas no inverno de 2026.

### Palavras-chave ###
neve, Sul do Brasil, inverno 2026, Rio Grande do Sul, clima, meteorologia, El Niño, previsão do tempo
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS acompanham com apreensão a votação da renegociação de dívidas no Senado

### Artigo ###
Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas no Senado, temendo que a ausência de aprovação comprometa o acesso ao crédito necessário para a próxima safra. Depois de uma sequência de adversidades climáticas que atingiram o campo gaúcho nos últimos anos, entre estiagens, excesso de chuvas e perdas de produtividade, o tema passou a ser tratado como prioritário pelo setor, que vê na medida uma condição essencial para manter a atividade produtiva. O endividamento rural é uma realidade que afeta um grande número de propriedades no estado, especialmente as familiares e de pequeno e médio porte. Quando o produtor não consegue renegociar suas dívidas em condições viáveis, corre o risco de ficar sem acesso ao crédito que financia a compra de insumos, sementes, máquinas e demais itens necessários para plantar. Sem crédito, não há plantio; sem plantio, a renda futura fica comprometida, criando um ciclo difícil de romper. É por isso que a votação no Senado é acompanhada com tanta tensão por quem vive da terra. A frase 'a gente não dorme mais', dita por produtores, traduz o peso emocional e financeiro que recai sobre as famílias do campo nesse momento de incerteza. Entidades representativas do agronegócio têm reforçado a importância de uma solução que dê fôlego ao produtor e preserve a capacidade de produção do estado, um dos principais celeiros do país. Para a economia gaúcha, fortemente ligada ao agronegócio, a definição sobre a renegociação tem reflexos que vão muito além das porteiras: alcançam o comércio, os serviços e o emprego nas cidades do interior. O setor aguarda uma resposta que ofereça previsibilidade e segurança para o planejamento da próxima safra, em um tema que segue no centro das atenções do campo do Rio Grande do Sul.

### Legenda sugerida ###
Produtores do RS temem ficar sem crédito para a próxima safra caso a renegociação de dívidas não avance no Senado.

### Palavras-chave ###
agronegócio, renegociação de dívidas, crédito rural, Rio Grande do Sul, safra, produtores rurais, Senado, endividamento
""",
}


def main():
    apr_path = ROOT / "state" / f"aprovadas_{HOJE}.json"
    pauta_path = ROOT / "state" / f"pauta_{HOJE}.json"
    materias_dir = ROOT / "state" / f"materias_{HOJE}"

    data = json.loads(apr_path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        apr_list = data
    else:
        apr_list = data.get("aprovadas") or data.get("curadas") or data.get("itens") or []

    pauta = []
    pub_count = 0
    for item in apr_list:
        h = item["id_hash"]
        if h not in PAUTA_ANGULADA:
            angul = bloquear("Sem angulação configurada — descartado pelo guardrail")
        else:
            angul = PAUTA_ANGULADA[h]

        if angul["decisao_final"] == "PUBLICAR" and pub_count >= 10:
            angul = {**angul, "decisao_final": "REBAIXAR", "decisao_motivo": "Quota diária esgotada (regra 14)"}
        if angul["decisao_final"] == "PUBLICAR":
            pub_count += 1

        pauta.append({**item, **angul})

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
        if p["decisao_final"] == "PUBLICAR" and p.get("formato_sugerido") == "materia_longa":
            corpo = MATERIAS.get(p["id_hash"])
            if corpo:
                (materias_dir / f"{p['id_hash']}.md").write_text(corpo, encoding="utf-8")
                nwrite += 1
                print(f"[angular] matéria -> {p['id_hash']}.md ({len(corpo)} chars)")
            else:
                print(f"[angular] AVISO: {p['id_hash']} PUBLICAR/materia_longa sem texto em MATERIAS")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
