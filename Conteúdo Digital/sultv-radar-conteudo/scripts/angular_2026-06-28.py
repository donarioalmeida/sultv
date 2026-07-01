#!/usr/bin/env python3
"""
angular_2026-06-28.py — angulação editorial + redação (cowork-faz-tudo).
Decisões editoriais Claude na sessão para a pauta de 2026-06-28.
Regra 12 INEGOCIÁVEL: nenhum texto menciona veículos/portais/rádios/jornais.
Atribuição apenas a fontes primárias institucionais.
Quota: máximo 10 PUBLICAR (regra 14).
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-28"


def _skip(decisao: str, motivo: str, titulo: str = "") -> dict:
    return {
        "titulo_sultv": titulo, "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": decisao,
        "decisao_motivo": motivo,
    }


PAUTA_ANGULADA = {

    # IDX 2 — Tapes: visita técnica queijos artesanais — PUBLICAR
    "b813b3c1125e55fcd642f740f8bb7d8042bf22c7": {
        "titulo_sultv": "Tapes recebe visita técnica que fortalece a produção de queijos artesanais",
        "chamada_faixa": "Tapes fortalece queijo artesanal",
        "subtitulo": "Secretaria da Agricultura acompanha queijaria local para qualificar a produção e ampliar a inspeção municipal.",
        "lead": "A produção de queijos artesanais de Tapes ganha um reforço técnico. A Secretaria da Agricultura do município realizou uma visita à Queijaria Flor do Araçá para acompanhar de perto o processo produtivo e orientar sobre boas práticas, num movimento que valoriza um dos elos mais tradicionais da economia rural da Costa Doce.",
        "ganchos_3": [
            "Visita técnica acompanha a produção de queijos em Tapes",
            "Inspeção municipal orienta boas práticas na queijaria",
            "Agroindústria artesanal ganha apoio da Secretaria da Agricultura"
        ],
        "angulo_editorial": "Agroindústria familiar em cidade-núcleo (Tapes), com fonte primária institucional (Secretaria da Agricultura e SIM). Valoriza cadeia produtiva regional, tema central da audiência rural. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Secretaria da Agricultura de Tapes", "Serviço de Inspeção Municipal (SIM)"],
        "lead_materia_longa": "A produção de queijos artesanais de Tapes ganha um reforço técnico. A Secretaria da Agricultura do município realizou uma visita à Queijaria Flor do Araçá para acompanhar de perto o processo produtivo e orientar sobre boas práticas.",
        "post_instagram": {
            "caption": "O queijo artesanal é um dos sabores que ajudam a contar a história do interior gaúcho, e em Tapes ele acaba de ganhar um reforço. A Secretaria da Agricultura do município visitou a Queijaria Flor do Araçá para acompanhar de perto a produção e orientar sobre boas práticas, ao lado do Serviço de Inspeção Municipal. Esse tipo de visita técnica faz diferença na vida de quem produz: aproxima o poder público da agroindústria familiar, qualifica o processo, dá segurança ao consumidor e abre portas para que o produto chegue a mais mercados com o selo da inspeção em dia. Por trás de cada peça de queijo há trabalho de família, conhecimento que passa de geração em geração e a vontade de fazer cada vez melhor. Valorizar essa produção é valorizar a economia da Costa Doce e a identidade do nosso interior. Tapes mostra que cuidar do pequeno produtor é cuidar do futuro do agro regional.",
            "hashtags": ["#Tapes", "#QueijoArtesanal", "#Agro", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tapes valoriza o queijo artesanal.",
            "desenvolvimento_45s": "A Secretaria da Agricultura de Tapes visitou a Queijaria Flor do Araçá para acompanhar de perto a produção e orientar sobre boas práticas, junto do Serviço de Inspeção Municipal. A visita técnica aproxima o poder público da agroindústria familiar, qualifica o processo e dá mais segurança ao consumidor, abrindo caminho para que o produto chegue a mais mercados com a inspeção em dia.",
            "fechamento_8s": "Cuidar do pequeno produtor é cuidar do agro regional.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "regional acolhedora"
        },
        "tag_thumbnail": "queijo artesanal, Tapes",
        "briefing_visual": {
            "descricao_pt": "Peças de queijo artesanal em maturação sobre prateleiras de madeira em uma pequena queijaria do interior, sem pessoas",
            "query_en": ["artisanal cheese aging shelves", "cheese dairy farm brazil", "handmade cheese wheels"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Wheels of artisanal cheese aging on wooden shelves in a small countryside dairy in southern Brazil, warm natural light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agroindústria familiar em cidade-núcleo (Tapes), fonte primária institucional, tema de forte interesse rural. Sem guardrail."
    },

    # IDX 7 — Cristal: PREPARA-RS R$ 200 mil — PUBLICAR
    "df4bb74213a932848bc016c469a266a2e1247455": {
        "titulo_sultv": "Cristal recebe R$ 200 mil do PREPARA-RS para obra de prevenção a desastres climáticos",
        "chamada_faixa": "Cristal: R$ 200 mil contra desastres",
        "subtitulo": "Recurso estadual será aplicado em obra de canalização na Sanga Leste para reduzir riscos de enchentes.",
        "lead": "Cristal vai investir em prevenção. O município foi contemplado com R$ 200 mil do programa estadual PREPARA-RS, recurso que será aplicado em uma obra de canalização na Sanga Leste, voltada a reduzir os riscos de desastres climáticos e a proteger moradores de áreas vulneráveis a alagamentos.",
        "ganchos_3": [
            "Cristal recebe R$ 200 mil para prevenção de desastres",
            "Obra de canalização na Sanga Leste reduz risco de enchentes",
            "Recurso estadual reforça a proteção das áreas vulneráveis"
        ],
        "angulo_editorial": "Fato concreto e quantitativo (R$ 200 mil) em cidade-núcleo (Cristal), fonte primária institucional. Tema de prevenção a desastres é altamente relevante no RS pós-eventos climáticos. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Programa estadual PREPARA-RS"],
        "lead_materia_longa": "Cristal vai investir em prevenção. O município foi contemplado com R$ 200 mil do programa estadual PREPARA-RS, recurso que será aplicado em uma obra de canalização na Sanga Leste.",
        "post_instagram": {
            "caption": "Depois de tudo que o Rio Grande do Sul enfrentou com os eventos climáticos dos últimos anos, prevenir deixou de ser opção e virou prioridade. Cristal acaba de dar um passo nessa direção: o município foi contemplado com R$ 200 mil do programa estadual PREPARA-RS, recurso que será aplicado em uma obra de canalização na Sanga Leste. Na prática, a intervenção melhora o escoamento da água e reduz o risco de alagamentos, protegendo moradores que vivem em áreas mais vulneráveis. Obras de drenagem e canalização não costumam aparecer nas manchetes, mas são exatamente o tipo de investimento que faz diferença quando a chuva aperta. Cada metro de canal bem feito é mais segurança para as famílias e menos prejuízo para a cidade. Cristal mostra que aprender com o passado é construir um futuro mais preparado para a Costa Doce.",
            "hashtags": ["#Cristal", "#PreparaRS", "#PrevençãoDeDesastres", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal investe em prevenção a desastres.",
            "desenvolvimento_45s": "O município foi contemplado com R$ 200 mil do programa estadual PREPARA-RS. O recurso será aplicado em uma obra de canalização na Sanga Leste, que melhora o escoamento da água e reduz o risco de alagamentos, protegendo moradores de áreas mais vulneráveis. Depois dos eventos climáticos dos últimos anos no Rio Grande do Sul, esse tipo de investimento em drenagem se tornou prioridade para as cidades da região.",
            "fechamento_8s": "Aprender com o passado é construir um futuro mais preparado.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "séria e esperançosa"
        },
        "tag_thumbnail": "prevenção de desastres, Cristal",
        "briefing_visual": {
            "descricao_pt": "Obra de canalização e drenagem urbana com maquinário em canal de concreto, dia, sem pessoas identificáveis",
            "query_en": ["urban drainage canal construction", "concrete water channel works", "flood prevention infrastructure"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Urban drainage canal construction works with concrete channeling in a small Brazilian town, excavator working, daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato concreto e quantitativo em cidade-núcleo (Cristal), fonte primária institucional, tema de prevenção a desastres. Sem guardrail."
    },

    # IDX 9 — Chuvisca: atendimentos de fonoaudiologia — PUBLICAR
    "01bf2ce86421848340a2a13f7cc548a169884964": {
        "titulo_sultv": "Chuvisca organiza atendimentos de fonoaudiologia na rede municipal de saúde",
        "chamada_faixa": "Chuvisca organiza atendimento de fono",
        "subtitulo": "Serviço será realizado na unidade de Saúde Mental, com agenda definida para atender a comunidade.",
        "lead": "A saúde de Chuvisca ganha mais um serviço organizado. A Secretaria Municipal de Saúde definiu a agenda de atendimentos em fonoaudiologia na unidade de Saúde Mental do município, estruturando o acesso da comunidade a um cuidado que faz diferença no desenvolvimento e na qualidade de vida dos pacientes.",
        "ganchos_3": [
            "Chuvisca define agenda de atendimento em fonoaudiologia",
            "Serviço será realizado na unidade de Saúde Mental",
            "Secretaria de Saúde organiza o acesso da comunidade"
        ],
        "angulo_editorial": "Serviço de utilidade pública em cidade-núcleo (Chuvisca), fonte primária institucional (Secretaria Municipal de Saúde). Informação organizacional de acesso, sem orientação clínica. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Prefeitura de Chuvisca", "Secretaria Municipal de Saúde de Chuvisca"],
        "lead_materia_longa": "A saúde de Chuvisca ganha mais um serviço organizado. A Secretaria Municipal de Saúde definiu a agenda de atendimentos em fonoaudiologia na unidade de Saúde Mental do município.",
        "post_instagram": {
            "caption": "Em cidades do interior, organizar bem cada serviço de saúde é o que garante que o cuidado chegue a quem precisa. Em Chuvisca, a Secretaria Municipal de Saúde definiu a agenda de atendimentos em fonoaudiologia, que serão realizados na unidade de Saúde Mental do município. A fonoaudiologia tem um papel importante e nem sempre lembrado: ajuda no desenvolvimento da fala e da linguagem das crianças, apoia a comunicação e a alimentação em diferentes fases da vida e contribui para a qualidade de vida em todas as idades. Ter esse serviço organizado e com dias definidos facilita o planejamento das famílias e evita deslocamentos desnecessários. É o tipo de iniciativa que mostra como a atenção básica, quando bem estruturada, melhora de verdade o dia a dia da comunidade. Quem precisa do atendimento deve procurar a Secretaria de Saúde para se informar sobre os horários. Chuvisca segue cuidando da sua gente.",
            "hashtags": ["#Chuvisca", "#Saúde", "#Fonoaudiologia", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Chuvisca organiza o atendimento de fonoaudiologia.",
            "desenvolvimento_45s": "A Secretaria Municipal de Saúde de Chuvisca definiu a agenda de atendimentos em fonoaudiologia, que serão realizados na unidade de Saúde Mental do município. A fonoaudiologia ajuda no desenvolvimento da fala e da linguagem, apoia a comunicação e a alimentação e contribui para a qualidade de vida em todas as idades. Ter o serviço com dias definidos facilita o planejamento das famílias.",
            "fechamento_8s": "Atenção básica bem organizada melhora o dia a dia da comunidade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "calma e acolhedora"
        },
        "tag_thumbnail": "saúde, Chuvisca",
        "briefing_visual": {
            "descricao_pt": "Fachada ou recepção de uma unidade básica de saúde do interior, ambiente limpo e organizado, sem pessoas identificáveis",
            "query_en": ["small health clinic building", "public health center interior", "rural health unit brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos", "crianças identificáveis"],
            "prompt_ia": "Exterior of a small public health unit in a Brazilian countryside town, clean and welcoming, daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de utilidade pública em cidade-núcleo (Chuvisca), fonte primária institucional, sem orientação clínica. Sem guardrail."
    },

    # IDX 11 — São Lourenço do Sul: Defesa Civil previsão — PUBLICAR
    "96ec78213adb3fee09ae0373ec6eef0ede62f443": {
        "titulo_sultv": "Defesa Civil de São Lourenço do Sul divulga previsão do tempo para o fim de semana",
        "chamada_faixa": "São Lourenço: tempo no fim de semana",
        "subtitulo": "Boletim aponta sexta e sábado estáveis, com mudança no quadro a partir da noite de sábado.",
        "lead": "São Lourenço do Sul começa o fim de semana com tempo firme. O boletim divulgado pela Defesa Civil Municipal indica sexta-feira ensolarada e sábado com sol entre nuvens e temperaturas amenas, com uma virada prevista a partir da noite de sábado, quando a aproximação de um sistema muda o cenário.",
        "ganchos_3": [
            "Sexta e sábado seguem estáveis em São Lourenço do Sul",
            "Defesa Civil orienta sobre a virada do tempo no domingo",
            "Boletim meteorológico ajuda a planejar o fim de semana"
        ],
        "angulo_editorial": "Serviço meteorológico oportuno em cidade-núcleo (São Lourenço do Sul), fonte primária institucional (Defesa Civil Municipal / CPMet-UFPel). Utilidade pública direta. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Defesa Civil Municipal de São Lourenço do Sul", "CPMet/UFPel"],
        "lead_materia_longa": "São Lourenço do Sul começa o fim de semana com tempo firme. O boletim divulgado pela Defesa Civil Municipal indica sexta-feira ensolarada e sábado com sol entre nuvens e temperaturas amenas.",
        "post_instagram": {
            "caption": "Quem é da Costa Doce sabe: planejar o fim de semana passa por olhar para o céu. Em São Lourenço do Sul, a Defesa Civil Municipal divulgou o boletim com a previsão para os próximos dias, e a notícia é boa para quem quer aproveitar. A sexta-feira segue com tempo estável e ensolarado, e o sábado mantém o cenário, com sol entre nuvens e temperaturas amenas, típicas do inverno gaúcho. A mudança aparece mais para o fim do período: entre a noite de sábado e a manhã de domingo, a aproximação de um sistema altera o quadro e pede atenção. Acompanhar os boletins da Defesa Civil é um hábito que vale a pena, tanto para quem tem planos ao ar livre quanto para o produtor rural, que organiza as atividades do campo conforme o tempo. Aproveite os dias firmes, programe-se para a virada e mantenha o olho na previsão. A Costa Doce agradece quem se planeja.",
            "hashtags": ["#SãoLourençodoSul", "#Previsão", "#DefesaCivil", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "O tempo no fim de semana em São Lourenço do Sul.",
            "desenvolvimento_45s": "A Defesa Civil Municipal divulgou o boletim com a previsão para os próximos dias. A sexta-feira segue estável e ensolarada, e o sábado mantém o cenário, com sol entre nuvens e temperaturas amenas. A virada aparece mais para o fim do período: entre a noite de sábado e a manhã de domingo, a aproximação de um sistema altera o quadro e pede atenção.",
            "fechamento_8s": "Aproveite os dias firmes e fique de olho na virada.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "leve e ensolarada"
        },
        "tag_thumbnail": "previsão do tempo, São Lourenço do Sul",
        "briefing_visual": {
            "descricao_pt": "Vista da orla da Lagoa dos Patos em São Lourenço do Sul com céu de sol entre nuvens, sem pessoas",
            "query_en": ["lagoon shore sunny sky", "calm lake horizon clouds", "waterfront blue sky brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Calm shore of a large lagoon at São Lourenço do Sul in southern Brazil under a sky with sun between clouds, serene winter light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço meteorológico oportuno em cidade-núcleo, fonte primária institucional (Defesa Civil). Sem guardrail."
    },

    # IDX 13 — Barra do Ribeiro: oficina de audiovisual — PUBLICAR
    "ea8a271d9bc72061b2fe7f531e34bca69b145a69": {
        "titulo_sultv": "Escolas de Barra do Ribeiro recebem oficina de audiovisual pela Política Nacional Aldir Blanc",
        "chamada_faixa": "Barra do Ribeiro: oficina nas escolas",
        "subtitulo": "Projeto levou técnicas de produção audiovisual a estudantes da rede municipal e estadual.",
        "lead": "A cultura entrou na sala de aula em Barra do Ribeiro. As escolas municipais e o Colégio Estadual Carlos Pinto receberam a Oficina de Audiovisual da Padula Produções, projeto contemplado pela Política Nacional Aldir Blanc, que apresentou aos estudantes técnicas de produção e despertou novos olhares sobre a comunicação e a arte.",
        "ganchos_3": [
            "Oficina de audiovisual chega às escolas de Barra do Ribeiro",
            "Estudantes aprendem técnicas de produção na prática",
            "Projeto da Política Nacional Aldir Blanc estimula a cultura local"
        ],
        "angulo_editorial": "Cultura e educação em cidade da região, com fonte primária institucional (rede municipal e estadual). Fomenta protagonismo juvenil e formação cultural. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Escolas municipais de Barra do Ribeiro", "Colégio Estadual Carlos Pinto"],
        "lead_materia_longa": "A cultura entrou na sala de aula em Barra do Ribeiro. As escolas municipais e o Colégio Estadual Carlos Pinto receberam a Oficina de Audiovisual da Padula Produções, projeto contemplado pela Política Nacional Aldir Blanc.",
        "post_instagram": {
            "caption": "Aprender a contar histórias com imagem e som pode abrir um mundo novo para um estudante, e foi exatamente isso que aconteceu em Barra do Ribeiro. As escolas municipais e o Colégio Estadual Carlos Pinto receberam a Oficina de Audiovisual da Padula Produções, projeto contemplado pela Política Nacional Aldir Blanc. Na prática, os estudantes conheceram técnicas de produção audiovisual, experimentaram o processo de criação e descobriram que comunicação e arte também podem ser caminho de futuro. Iniciativas como essa fazem diferença porque levam cultura para dentro da escola e mostram, na prática, profissões e possibilidades que muitas vezes pareciam distantes. Quando um jovem do interior segura uma câmera e entende como uma história ganha forma na tela, algo muda. Investir em cultura e educação é plantar oportunidade. Barra do Ribeiro mostra como projetos culturais podem transformar a sala de aula em espaço de descoberta.",
            "hashtags": ["#BarraDoRibeiro", "#Cultura", "#Educação", "#AldirBlanc", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cultura na sala de aula em Barra do Ribeiro.",
            "desenvolvimento_45s": "As escolas municipais e o Colégio Estadual Carlos Pinto receberam a Oficina de Audiovisual da Padula Produções, projeto contemplado pela Política Nacional Aldir Blanc. Os estudantes conheceram técnicas de produção audiovisual, experimentaram o processo de criação e descobriram que comunicação e arte podem ser caminho de futuro. Iniciativas assim levam cultura para dentro da escola e abrem novas possibilidades.",
            "fechamento_8s": "Investir em cultura e educação é plantar oportunidade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "inspiradora e jovem"
        },
        "tag_thumbnail": "cultura, educação, Barra do Ribeiro",
        "briefing_visual": {
            "descricao_pt": "Estudantes de costas manuseando câmera e equipamento de vídeo em sala de aula, foco nos equipamentos, sem rostos identificáveis",
            "query_en": ["students film workshop camera", "video production class", "kids learning filmmaking"],
            "evitar": ["rostos de menores identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A school audiovisual workshop with a video camera on a tripod and students seen from behind, focus on the equipment, bright classroom, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura e educação na região, fonte primária institucional, protagonismo juvenil. Sem guardrail (foco institucional, sem exposição de menores)."
    },

    # IDX 16 — Guaíba: Sarandeio Farroupilha do Centenário — PUBLICAR
    "ce85cd87201e74ffe56eda208f34ac6cca2c198c": {
        "titulo_sultv": "Guaíba abre o Sarandeio Farroupilha do Centenário com festa descentralizada",
        "chamada_faixa": "Guaíba abre o Sarandeio Farroupilha",
        "subtitulo": "Tradição gaúcha chega a diferentes regiões da cidade, com tiro de laço e bailes ao longo da programação.",
        "lead": "A tradição gaúcha tomou conta de Guaíba. Começou o Sarandeio Farroupilha do Centenário, que neste ano acontece de forma descentralizada e leva a cultura campeira a diferentes regiões da cidade, com tiro de laço durante o dia e bailes à noite reunindo a comunidade em torno do chimarrão e do fandango.",
        "ganchos_3": [
            "Sarandeio Farroupilha do Centenário começa em Guaíba",
            "Festa descentralizada leva a tradição a vários bairros",
            "Tiro de laço e bailes reúnem a comunidade campeira"
        ],
        "angulo_editorial": "Cultura e tradição gaúcha em cidade da região metropolitana sul, fonte primária institucional (Prefeitura). Tema de identidade regional forte para a audiência. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Prefeitura de Guaíba", "DTG Estância Farroupilha"],
        "lead_materia_longa": "A tradição gaúcha tomou conta de Guaíba. Começou o Sarandeio Farroupilha do Centenário, que neste ano acontece de forma descentralizada e leva a cultura campeira a diferentes regiões da cidade.",
        "post_instagram": {
            "caption": "Tem cheiro de chimarrão no ar e a tradição gaúcha de volta às rodas: começou em Guaíba o Sarandeio Farroupilha do Centenário. A novidade deste ano é o formato descentralizado, que leva a festa para diferentes regiões da cidade, aproximando a cultura campeira de mais moradores. A programação reúne tiro de laço durante o dia e bailes à noite, com a comunidade celebrando junto aquilo que é a alma do Rio Grande: o cavalo, a bota, a prenda, o fandango e o orgulho de ser gaúcho. Eventos como esse mantêm viva uma herança que passa de geração em geração e fortalecem o sentimento de pertencimento. Levar a tradição para os bairros é abrir espaço para que mais gente participe, dance, torça e se reconheça nessa cultura. Vista a pilcha, prepare a cuia e venha sarandear. Guaíba mostra que tradição boa é tradição que se compartilha.",
            "hashtags": ["#Guaíba", "#TradiçãoGaúcha", "#Farroupilha", "#RioGrandedoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Começou o Sarandeio Farroupilha em Guaíba.",
            "desenvolvimento_45s": "O Sarandeio Farroupilha do Centenário chegou com novidade: neste ano a festa é descentralizada e leva a cultura campeira a diferentes regiões da cidade. A programação reúne tiro de laço durante o dia e bailes à noite, com a comunidade celebrando a tradição gaúcha. Levar a festa para os bairros aproxima mais moradores e fortalece o sentimento de pertencimento.",
            "fechamento_8s": "Tradição boa é tradição que se compartilha.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "vaneira gaúcha"
        },
        "tag_thumbnail": "tradição gaúcha, Guaíba",
        "briefing_visual": {
            "descricao_pt": "Cavaleiro com pilcha tradicional gaúcha em piquete de tiro de laço, bandeira do RS, sem rosto identificável",
            "query_en": ["gaucho horse rider traditional", "rodeo lasso south brazil", "gaucho tradition horse"],
            "evitar": ["rosto identificável", "marcas", "texto", "logos"],
            "prompt_ia": "A gaucho in traditional pilcha attire on horseback at a rural festival ground in Rio Grande do Sul, Brazilian gaucho culture, golden afternoon light, rider seen from a distance, no identifiable face, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura e tradição gaúcha na região, fonte primária institucional, identidade regional forte. Sem guardrail."
    },

    # IDX 23 — RS: renegociação de dívidas rurais — PUBLICAR (agro)
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "titulo_sultv": "Produtores do RS acompanham com apreensão a renegociação de dívidas rurais",
        "chamada_faixa": "Produtores temem por dívidas rurais",
        "subtitulo": "Setor teme ficar sem acesso ao crédito rural para a próxima safra caso a renegociação não avance.",
        "lead": "A apreensão toma conta do campo gaúcho. Produtores rurais do Rio Grande do Sul acompanham de perto a tramitação da renegociação de dívidas e temem ficar sem acesso ao crédito rural para a próxima safra, num momento em que a recuperação financeira de muitas propriedades depende de prazos e condições mais adequados à realidade do setor.",
        "ganchos_3": [
            "Produtores do RS temem ficar sem crédito para a próxima safra",
            "Renegociação de dívidas rurais é acompanhada com apreensão",
            "Recuperação das propriedades depende de prazos mais adequados"
        ],
        "angulo_editorial": "Tema central da audiência rural do RS, com âncora regional clara. Tratar como pauta econômica do agro, sem viés partidário — foco no impacto sobre o produtor e o crédito da safra. Sem guardrail (não nomear partidos nem fazer disputa partidária).",
        "fontes_complementares_sugeridas": ["Entidades de representação do produtor rural", "Federação da Agricultura do RS"],
        "lead_materia_longa": "A apreensão toma conta do campo gaúcho. Produtores rurais do Rio Grande do Sul acompanham de perto a tramitação da renegociação de dívidas e temem ficar sem acesso ao crédito rural para a próxima safra.",
        "post_instagram": {
            "caption": "No campo, a conta não para de rodar, e muitos produtores gaúchos estão perdendo o sono. A renegociação de dívidas rurais está em discussão, e o setor acompanha cada passo com apreensão. O receio é concreto: sem uma solução adequada, parte dos produtores pode ficar sem acesso ao crédito rural na hora de financiar a próxima safra. Depois de anos marcados por estiagens, excesso de chuva e oscilações de preço, muitas propriedades do Rio Grande do Sul precisam de fôlego para se reorganizar. Prazos mais longos e condições compatíveis com a realidade do campo não são um favor: são o que mantém a roda da produção girando, garante emprego no interior e comida na mesa do país. O agro gaúcho é resiliente, mas resiliência também precisa de condições para se sustentar. O setor segue atento, na torcida por uma definição que dê segurança a quem produz. O campo precisa de previsibilidade para seguir plantando.",
            "hashtags": ["#Agro", "#CréditoRural", "#RioGrandedoSul", "#Safra", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Produtores gaúchos temem ficar sem crédito.",
            "desenvolvimento_45s": "A renegociação de dívidas rurais está em discussão e o setor acompanha cada passo com apreensão. O receio é concreto: sem uma solução adequada, parte dos produtores pode ficar sem acesso ao crédito rural para financiar a próxima safra. Depois de anos de estiagem, excesso de chuva e oscilação de preços, muitas propriedades do Rio Grande do Sul precisam de prazos mais longos para se reorganizar.",
            "fechamento_8s": "O campo precisa de previsibilidade para seguir plantando.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "reflexiva e firme"
        },
        "tag_thumbnail": "crédito rural, dívidas, agro RS",
        "briefing_visual": {
            "descricao_pt": "Lavoura de soja ou trigo no Rio Grande do Sul ao entardecer, com trator ao fundo, sem pessoas identificáveis",
            "query_en": ["soybean field sunset brazil", "farm tractor crop field", "wheat field southern brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "A wide soybean field in Rio Grande do Sul at sunset with a tractor in the distance, contemplative rural mood, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Tema central da audiência rural do RS com âncora regional. Enquadrado como pauta econômica do agro, sem viés partidário. Sem guardrail."
    },

    # IDX 25 — RS: apreensão de 630 kg de alimentos — PUBLICAR
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": {
        "titulo_sultv": "Força-tarefa apreende 630 kg de alimentos impróprios para consumo no RS",
        "chamada_faixa": "RS: 630 kg de alimentos apreendidos",
        "subtitulo": "Ação fiscalizou cinco estabelecimentos e recolheu carnes, ovos, laticínios e outros produtos fora das condições de consumo.",
        "lead": "A fiscalização tirou de circulação 630 quilos de alimentos impróprios para consumo no Rio Grande do Sul. Uma força-tarefa percorreu cinco estabelecimentos e recolheu carnes, ovos, amendoim, iogurtes, pães e bebidas que estavam fora das condições adequadas, em uma ação que reforça a proteção da saúde do consumidor.",
        "ganchos_3": [
            "Força-tarefa apreende 630 kg de alimentos impróprios no RS",
            "Cinco estabelecimentos foram fiscalizados na ação",
            "Operação reforça a proteção da saúde do consumidor"
        ],
        "angulo_editorial": "Fato concreto e quantitativo (630 kg), segurança alimentar com interesse estadual amplo, fonte primária institucional (Ministério Público do RS). Sem guardrail (sem vítima identificada, sem partidarização).",
        "fontes_complementares_sugeridas": ["Ministério Público do Rio Grande do Sul", "Órgãos de vigilância sanitária"],
        "lead_materia_longa": "A fiscalização tirou de circulação 630 quilos de alimentos impróprios para consumo no Rio Grande do Sul. Uma força-tarefa percorreu cinco estabelecimentos e recolheu carnes, ovos, amendoim, iogurtes, pães e bebidas que estavam fora das condições adequadas.",
        "post_instagram": {
            "caption": "O que chega à mesa precisa ter procedência e condições de consumo, e foi para garantir isso que uma força-tarefa entrou em ação no Rio Grande do Sul. A operação fiscalizou cinco estabelecimentos e apreendeu 630 quilos de alimentos impróprios para consumo, entre carnes, ovos, amendoim, iogurtes, pães e bebidas que estavam fora das condições adequadas. Esse tipo de fiscalização é essencial e nem sempre ganha destaque, mas protege diretamente a saúde de quem compra. Produto mal armazenado, vencido ou sem origem clara pode causar desde uma intoxicação alimentar até problemas mais sérios. A recomendação para o consumidor é sempre conferir a validade, observar as condições de armazenamento e desconfiar de preços e ofertas que fogem do razoável. Comprar com atenção é também cuidar da própria família. O trabalho de quem fiscaliza ajuda a manter o comércio sério funcionando e o consumidor protegido.",
            "hashtags": ["#RioGrandedoSul", "#SegurançaAlimentar", "#Fiscalização", "#Consumidor", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "630 quilos de alimentos apreendidos no RS.",
            "desenvolvimento_45s": "Uma força-tarefa fiscalizou cinco estabelecimentos no Rio Grande do Sul e apreendeu 630 quilos de alimentos impróprios para consumo, entre carnes, ovos, amendoim, iogurtes, pães e bebidas fora das condições adequadas. Esse tipo de fiscalização protege diretamente a saúde de quem compra. A recomendação ao consumidor é conferir a validade, observar o armazenamento e desconfiar de ofertas fora do razoável.",
            "fechamento_8s": "Comprar com atenção é cuidar da própria família.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "informativa e firme"
        },
        "tag_thumbnail": "segurança alimentar, fiscalização RS",
        "briefing_visual": {
            "descricao_pt": "Inspeção sanitária em estabelecimento comercial, prateleiras de alimentos sendo verificadas, sem rostos identificáveis",
            "query_en": ["food safety inspection shop", "health inspector market shelves", "food control warehouse"],
            "evitar": ["rostos identificáveis", "marcas comerciais legíveis", "texto", "logos"],
            "prompt_ia": "A food safety inspection scene in a commercial storage room with shelves of food products being checked, neutral institutional setting, no identifiable people, no readable brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato concreto e quantitativo de segurança alimentar, interesse estadual amplo, fonte primária institucional (MP-RS). Sem guardrail."
    },

    # IDX 28 — Amaral Ferrador: Unidade Odontológica Móvel — PUBLICAR
    "e93271ddd33993182fc7c76c4f992bb9ed645c87": {
        "titulo_sultv": "Amaral Ferrador conquista Unidade Odontológica Móvel para ampliar o atendimento",
        "chamada_faixa": "Amaral Ferrador ganha odonto móvel",
        "subtitulo": "Equipamento vai levar atendimento odontológico a diferentes localidades do município, incluindo o interior.",
        "lead": "A saúde bucal de Amaral Ferrador ganha um reforço de peso. O município conquistou uma Unidade Odontológica Móvel, equipamento que permitirá levar atendimento a diferentes localidades, ampliando o acesso da população — especialmente de quem vive no interior e tem mais dificuldade de chegar até a sede.",
        "ganchos_3": [
            "Amaral Ferrador conquista Unidade Odontológica Móvel",
            "Atendimento odontológico vai chegar ao interior do município",
            "Equipamento amplia o acesso da população à saúde bucal"
        ],
        "angulo_editorial": "Conquista de serviço de saúde em cidade-núcleo (Amaral Ferrador), fonte primária institucional (Prefeitura/Secretaria de Saúde). Ampliação concreta de acesso, sem orientação clínica. Sem guardrail.",
        "fontes_complementares_sugeridas": ["Prefeitura de Amaral Ferrador", "Secretaria Municipal de Saúde de Amaral Ferrador"],
        "lead_materia_longa": "A saúde bucal de Amaral Ferrador ganha um reforço de peso. O município conquistou uma Unidade Odontológica Móvel, equipamento que permitirá levar atendimento a diferentes localidades, ampliando o acesso da população.",
        "post_instagram": {
            "caption": "Levar o dentista até quem mais precisa: é isso que Amaral Ferrador acaba de conquistar. O município recebeu uma Unidade Odontológica Móvel, um consultório sobre rodas que permite levar o atendimento odontológico a diferentes localidades, incluindo o interior, onde chegar até a sede nem sempre é fácil. Para muita gente do meio rural, deslocamento, distância e horário de trabalho acabam adiando um cuidado básico que faz toda a diferença na saúde e na autoestima. Com a unidade móvel, o atendimento vai ao encontro da comunidade, aproximando o serviço de saúde de quem está mais longe. Conquistas como essa mostram que pensar a saúde no interior é também pensar em logística e em chegar perto das pessoas. Saúde bucal é saúde, e cada sorriso bem cuidado é qualidade de vida. Amaral Ferrador dá um passo importante para que ninguém fique para trás no atendimento.",
            "hashtags": ["#AmaralFerrador", "#Saúde", "#SaúdeBucal", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Amaral Ferrador conquista odontologia móvel.",
            "desenvolvimento_45s": "O município recebeu uma Unidade Odontológica Móvel, um consultório sobre rodas que vai levar o atendimento odontológico a diferentes localidades, incluindo o interior, onde chegar até a sede nem sempre é fácil. Com a unidade, o serviço de saúde vai ao encontro da comunidade, aproximando o atendimento de quem está mais longe e ampliando o acesso da população à saúde bucal.",
            "fechamento_8s": "Saúde bucal é saúde, e cada sorriso cuidado é qualidade de vida.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "positiva e acolhedora"
        },
        "tag_thumbnail": "saúde bucal, Amaral Ferrador",
        "briefing_visual": {
            "descricao_pt": "Veículo tipo van/ônibus adaptado como consultório odontológico móvel estacionado, sem pessoas identificáveis",
            "query_en": ["mobile dental clinic van", "health mobile unit bus", "medical van countryside"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A mobile dental clinic van parked in a small Brazilian countryside town ready to serve the community, daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Conquista concreta de serviço de saúde em cidade-núcleo, fonte primária institucional, ampliação de acesso. Sem guardrail."
    },

    # IDX 32 — Rio Grande/Pelotas: COPSul Carta Compromisso — PUBLICAR
    "f29cc027834a8ce15c786267925c81e25f66cf29": {
        "titulo_sultv": "COPSul encerra segunda edição em Pelotas com aprovação da Carta Compromisso",
        "chamada_faixa": "COPSul aprova Carta Compromisso",
        "subtitulo": "Conferência Sul sobre Mudanças Climáticas reuniu encaminhamentos para fortalecer a articulação regional.",
        "lead": "A região sul fechou dois dias de debate sobre o clima com um documento na mão. A segunda edição da Conferência Sul sobre Mudanças Climáticas, a COPSul, foi encerrada em Pelotas com a aprovação da Carta Compromisso, que reúne os principais encaminhamentos construídos durante o evento e reforça a articulação regional diante dos desafios climáticos.",
        "ganchos_3": [
            "COPSul encerra segunda edição com a Carta Compromisso",
            "Documento reúne encaminhamentos para o enfrentamento climático",
            "Conferência fortalece a articulação regional no Sul do RS"
        ],
        "angulo_editorial": "Pauta climática regional com âncora na Costa Doce (Pelotas), tema estratégico para o agro e para as cidades do Sul do RS após os eventos extremos. Fonte primária (organização da conferência). Sem guardrail.",
        "fontes_complementares_sugeridas": ["Organização da Conferência Sul sobre Mudanças Climáticas (COPSul)"],
        "lead_materia_longa": "A região sul fechou dois dias de debate sobre o clima com um documento na mão. A segunda edição da Conferência Sul sobre Mudanças Climáticas, a COPSul, foi encerrada em Pelotas com a aprovação da Carta Compromisso.",
        "post_instagram": {
            "caption": "O Sul do Rio Grande do Sul sabe na pele o que significam as mudanças climáticas, e transformar essa experiência em ação foi o objetivo da COPSul. A segunda edição da Conferência Sul sobre Mudanças Climáticas terminou em Pelotas com a aprovação da Carta Compromisso, documento que reúne os principais encaminhamentos construídos ao longo de dois dias de debates e reforça a articulação regional. O tema não é abstrato: enchentes, estiagens e eventos extremos já afetam diretamente a produção rural, as cidades e a vida das famílias da Costa Doce. Pensar adaptação, prevenção e desenvolvimento sustentável deixou de ser pauta de futuro para virar urgência do presente. Quando municípios, entidades e comunidade se sentam à mesma mesa e saem com compromissos definidos, a região ganha força para buscar soluções juntos. O clima é o desafio do nosso tempo, e enfrentá-lo exige articulação. A COPSul mostra que o Sul está atento e disposto a agir.",
            "hashtags": ["#COPSul", "#MudançasClimáticas", "#CostaDoce", "#RioGrandedoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "COPSul termina com Carta Compromisso em Pelotas.",
            "desenvolvimento_45s": "A segunda edição da Conferência Sul sobre Mudanças Climáticas terminou em Pelotas com a aprovação da Carta Compromisso, documento que reúne os principais encaminhamentos construídos em dois dias de debates e reforça a articulação regional. O tema não é abstrato: enchentes, estiagens e eventos extremos já afetam a produção rural e a vida das famílias da Costa Doce. Adaptação e prevenção viraram urgência do presente.",
            "fechamento_8s": "O clima é o desafio do nosso tempo, e enfrentá-lo exige articulação.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "séria e mobilizadora"
        },
        "tag_thumbnail": "mudanças climáticas, COPSul, Pelotas",
        "briefing_visual": {
            "descricao_pt": "Auditório de conferência com plateia ao fundo e mesa de debates, ambiente institucional, sem rostos identificáveis em primeiro plano",
            "query_en": ["conference auditorium audience", "climate summit panel stage", "seminar hall debate"],
            "evitar": ["rostos identificáveis em close", "marcas", "texto", "logos"],
            "prompt_ia": "A regional climate conference auditorium with a panel table on stage and a seated audience seen from behind, institutional setting, no identifiable faces in foreground, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Pauta climática regional com âncora na Costa Doce (Pelotas), estratégica para o agro e as cidades do Sul. Fonte primária. Sem guardrail."
    },

    # ===== BLOQUEAR (guardrails) =====
    "d004accdf1717341825e09c92ef1b79dd90ce7f3": {
        **_skip("BLOQUEAR", "Guardrail: conteúdo envolvendo menor (criança) + crime/tragédia, sem âncora regional. Pauta nacional/internacional.",
                "ChatGPT ajudou a impedir plano de assassinato de criança"),
    },
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": {
        **_skip("BLOQUEAR", "Guardrail: política partidária (parlamentares, concessões, privatizações, PPPs). Disputa partidária fora do escopo.",
                "Parlamentares manifestam-se sobre concessões, privatizações e PPPs"),
    },
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": {
        **_skip("BLOQUEAR", "Título procedural/cabeçalho de seção com data antiga (05/05) — emissão de notas fiscais. Sem valor editorial.",
                "Emissão de notas fiscais pelo emissor nacional"),
    },

    # ===== REBAIXAR =====
    "4d192cf91d7ef9f986f9ea34fffa72075222e89c": {
        **_skip("REBAIXAR", "Saúde médica (campanha de vacinação) de abrangência estadual sem âncora regional forte; tema sensível. Vira nota interna.",
                "Alerta sobre baixa adesão à vacinação contra a influenza"),
    },
    "d00f19d46bdc3f61b698d15c65d0e8bee1d3ba11": {
        **_skip("REBAIXAR", "Segundo item de Tapes (quota de publicação preenchida pela visita técnica). Vaga de emprego vira nota de serviço interna.",
                "Sine de Tapes oferece vaga para vigia"),
    },
    "2c66372aa8f08ae544272cdd0b4d0552a60951ed": {
        **_skip("REBAIXAR", "Segundo item de Cristal (quota preenchida pelo PREPARA-RS). Limpeza de canteiro é rotina de baixo impacto.",
                "Limpeza do canteiro central da Avenida Passo do Mendonça"),
    },
    "809b4791c1acb10061fa9bb3125e79ccc53a1f15": {
        **_skip("REBAIXAR", "Aviso procedural de alteração de horário de expediente. Baixo valor editorial isolado.",
                "Alteração no horário de expediente"),
    },
    "f72de9fd06876db6baf7bd29e80d8c0f6587e0a4": {
        **_skip("REBAIXAR", "Título genérico/autoelogio sem fato concreto destacável.",
                "Semana com conquistas que fazem a diferença"),
    },
    "1bb71adab26b571eebbf1fc5d7bf52fcc21a8f39": {
        **_skip("REBAIXAR", "Cobertura genérica de evento sem fato concreto ou data útil destacável.",
                "Tarde marcada por alegria, integração e tradição"),
    },
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": {
        **_skip("REBAIXAR", "Aviso de audiência pública — procedural. Vira nota de agenda.",
                "Aviso de audiência pública"),
    },
    "bd92711b7702c7c7df50a735bc52c15c8fa5e140": {
        **_skip("REBAIXAR", "Pauta nacional (Censo Escolar) sem âncora regional Sul-RS.",
                "Censo Escolar: Brasil reduz índices de reprovação"),
    },
    "0c78bd0cc00e7d0302fc635b3fdbfbd510252753": {
        **_skip("REBAIXAR", "Concurso com data antiga (13 de maio) — procedural e desatualizado.",
                "Classificações finais de concurso para magistério"),
    },
    "49348b06a39337d964518e54a7715142418ea220": {
        **_skip("REBAIXAR", "Conteúdo procedural sobre destinação de recursos; envolve fundo da criança (sensível). Vira nota interna.",
                "Legislação e passos para destinação de recursos ao Funcriança"),
    },
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": {
        **_skip("REBAIXAR", "Pauta sensacionalista e sobreposta à apreensão de alimentos (item já publicado). Evita duplicidade temática.",
                "Vinhos vencidos há 9 anos são apreendidos"),
    },
    "e40cfca61a2890d7a59df6e6447f68903f8c80eb": {
        **_skip("REBAIXAR", "Tema climático estadual sobreposto à previsão de São Lourenço (já publicada). Vira nota de serviço.",
                "Esclarecimento sobre ciclone no fim de semana"),
    },
    "f76ea299bef7679e45c48adf607c6ce32dd1c2c0": {
        **_skip("REBAIXAR", "Ocorrência policial em município distante (São Gabriel) fora do núcleo; risco de identificação. Vira nota interna.",
                "Polícia Civil cumpre mandado de prisão em São Gabriel"),
    },
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
            angul = _skip("REBAIXAR", "Fora do top de prioridade do dia (score baixo / sem âncora forte / formato post).")
            angul["titulo_sultv"] = (item.get("titulo", "") or "")[:100]
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
    print(f"[angular] decisões:", dict(Counter(p["decisao_final"] for p in pauta)))
    print(f"[angular] PUBLICAR: {pub_count}")

    materias_dir.mkdir(exist_ok=True)
    nwrite = 0
    for p in pauta:
        if p["decisao_final"] == "PUBLICAR" and p.get("formato_sugerido") == "materia_longa":
            corpo = MATERIAS.get(p["id_hash"])
            if corpo:
                f = materias_dir / f"{p['id_hash']}.md"
                f.write_text(corpo, encoding="utf-8")
                nwrite += 1
                print(f"[angular] matéria -> {f.name} ({len(corpo)} chars)")
            else:
                print(f"[angular] AVISO: {p['id_hash']} PUBLICAR/materia_longa SEM texto em MATERIAS")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


MATERIAS = {

    "b813b3c1125e55fcd642f740f8bb7d8042bf22c7": """### Título ###
Tapes recebe visita técnica que fortalece a produção de queijos artesanais

### Artigo ###
A produção de queijos artesanais de Tapes ganhou um reforço técnico importante. A Secretaria da Agricultura do município realizou uma visita à Queijaria Flor do Araçá para acompanhar de perto o processo produtivo e orientar sobre boas práticas, num movimento que valoriza um dos elos mais tradicionais da economia rural da Costa Doce. A ação contou com a participação do Serviço de Inspeção Municipal (SIM) e do acompanhamento técnico voltado à qualificação da agroindústria familiar. Visitas como essa têm um papel que vai muito além da fiscalização. Elas aproximam o poder público de quem está na ponta da produção, ajudam a corrigir detalhes do processo, reforçam o cumprimento das normas sanitárias e dão ao produtor a segurança de que está no caminho certo. Para o consumidor, o resultado é a garantia de um alimento produzido com qualidade e dentro das condições adequadas. Para o produtor, é a chance de ampliar mercado: um produto com a inspeção em dia pode circular com mais tranquilidade e chegar a novos pontos de venda. O queijo artesanal carrega história. Por trás de cada peça há o trabalho de famílias inteiras, conhecimento passado de geração em geração e a vontade de fazer cada vez melhor um produto que é parte da identidade do interior gaúcho. Em municípios como Tapes, a agroindústria familiar movimenta a economia local, gera renda no campo e ajuda a fixar as famílias na zona rural. Apoiar essa cadeia é apostar no desenvolvimento da região a partir de quem produz. A iniciativa da Secretaria da Agricultura reforça esse compromisso e mostra que valorizar o pequeno produtor é também valorizar o futuro do agro regional. Quando inspeção, orientação técnica e tradição caminham juntas, todo mundo ganha: o produtor, o consumidor e a Costa Doce.

### Legenda sugerida ###
Secretaria da Agricultura de Tapes faz visita técnica à Queijaria Flor do Araçá para qualificar a produção e fortalecer a agroindústria familiar.

### Palavras-chave ###
Tapes, queijo artesanal, agroindústria familiar, Serviço de Inspeção Municipal, agro, Costa Doce, Rio Grande do Sul
""",

    "df4bb74213a932848bc016c469a266a2e1247455": """### Título ###
Cristal recebe R$ 200 mil do PREPARA-RS para obra de prevenção a desastres climáticos

### Artigo ###
Cristal vai investir em prevenção. O município foi contemplado com R$ 200 mil do programa estadual PREPARA-RS, recurso que será aplicado em uma obra de canalização na Sanga Leste, voltada a reduzir os riscos de desastres climáticos e a proteger moradores de áreas vulneráveis a alagamentos. Segundo informações da Prefeitura, a intervenção deve começar em breve. A escolha do tema não é por acaso. Depois dos eventos climáticos extremos que atingiram o Rio Grande do Sul nos últimos anos, com enchentes que deixaram marcas profundas em diversas cidades, prevenir deixou de ser uma escolha e se tornou prioridade. Obras de drenagem e canalização melhoram o escoamento da água nos períodos de chuva intensa e reduzem o risco de transbordamentos, protegendo quem vive nas áreas mais expostas. O programa estadual funciona como um reforço para que os municípios consigam estruturar essas intervenções, que costumam exigir investimento expressivo. Ao destinar o recurso para a Sanga Leste, Cristal mira um ponto sensível do seu território, antecipando-se a problemas que poderiam se repetir a cada temporada de chuvas. Esse tipo de obra raramente aparece em destaque, mas é exatamente o que faz diferença quando o tempo aperta. Cada metro de canal bem executado representa mais segurança para as famílias, menos prejuízo material e mais tranquilidade para a comunidade. A prevenção também tem peso econômico: evitar o estrago é sempre mais barato do que reconstruir depois. Para os moradores de Cristal, a notícia traz alívio e a perspectiva de um município mais preparado para enfrentar os desafios do clima. A iniciativa mostra que aprender com o passado recente é o melhor caminho para construir um futuro mais seguro na Costa Doce, onde a relação com a água e com o tempo faz parte do dia a dia de quem vive na cidade e no campo.

### Legenda sugerida ###
Cristal é contemplada com R$ 200 mil do PREPARA-RS para obra de canalização na Sanga Leste, reforçando a prevenção a desastres climáticos.

### Palavras-chave ###
Cristal, PREPARA-RS, prevenção de desastres, canalização, Sanga Leste, clima, Costa Doce
""",

    "01bf2ce86421848340a2a13f7cc548a169884964": """### Título ###
Chuvisca organiza atendimentos de fonoaudiologia na rede municipal de saúde

### Artigo ###
A saúde de Chuvisca ganhou mais um serviço organizado. A Secretaria Municipal de Saúde definiu a agenda de atendimentos em fonoaudiologia na unidade de Saúde Mental do município, estruturando o acesso da comunidade a um cuidado que faz diferença no desenvolvimento e na qualidade de vida dos pacientes. Os atendimentos passam a ocorrer em dias definidos, o que facilita o planejamento das famílias e organiza a procura pelo serviço. Em municípios pequenos, organizar bem cada especialidade é o que garante que o cuidado chegue de fato a quem precisa. A fonoaudiologia tem um papel importante e nem sempre lembrado. Ela atua no desenvolvimento da fala e da linguagem, especialmente na infância, apoia a comunicação em diferentes fases da vida e ajuda em questões ligadas à audição e até à alimentação. Um acompanhamento adequado pode transformar a trajetória escolar de uma criança, melhorar a convivência social e devolver autonomia a quem enfrenta dificuldades de comunicação. Ter esse serviço disponível na rede municipal, com dias e local definidos, evita que as famílias precisem se deslocar para outras cidades em busca de atendimento, o que muitas vezes representa custo, tempo e dificuldade. É o tipo de iniciativa que mostra como a atenção básica, quando bem estruturada, melhora de verdade o dia a dia da população. A organização do atendimento também ajuda o próprio serviço de saúde a planejar melhor sua rotina, otimizar o trabalho dos profissionais e ampliar o alcance do cuidado. Quem precisa do atendimento em fonoaudiologia deve procurar a Secretaria Municipal de Saúde para se informar sobre os horários e a forma de acesso. A medida reforça o compromisso de Chuvisca com uma saúde mais próxima e acessível, cuidando da sua gente em todas as fases da vida e garantindo que serviços essenciais cheguem a quem mais precisa deles na comunidade.

### Legenda sugerida ###
Secretaria Municipal de Saúde de Chuvisca organiza a agenda de atendimentos em fonoaudiologia na unidade de Saúde Mental do município.

### Palavras-chave ###
Chuvisca, fonoaudiologia, saúde, Secretaria Municipal de Saúde, atenção básica, Costa Doce
""",

    "96ec78213adb3fee09ae0373ec6eef0ede62f443": """### Título ###
Defesa Civil de São Lourenço do Sul divulga previsão do tempo para o fim de semana

### Artigo ###
São Lourenço do Sul começa o fim de semana com tempo firme. O boletim divulgado pela Defesa Civil Municipal indica sexta-feira ensolarada e sábado com sol entre nuvens e temperaturas amenas, com uma virada prevista a partir da noite de sábado, quando a aproximação de um sistema muda o cenário sobre a região. As informações têm como base o acompanhamento meteorológico técnico que orienta o trabalho da Defesa Civil. Para quem vive na Costa Doce, planejar o fim de semana passa por olhar para o céu, e a previsão chega como um aliado. Os dias estáveis abrem espaço para atividades ao ar livre, deslocamentos pela zona rural e tarefas que dependem do tempo bom. As temperaturas seguem típicas do inverno gaúcho, com manhãs mais frias e tardes amenas sob o sol. A estabilidade, no entanto, tem prazo para acabar. A indicação é de que, entre a noite de sábado e a manhã de domingo, o quadro se altere com a chegada de um sistema que aumenta a nebulosidade e pede mais atenção. Acompanhar os boletins da Defesa Civil é um hábito que vale a pena cultivar. Mais do que informar se vai fazer sol ou chuva, esse acompanhamento ajuda a comunidade a se antecipar a mudanças bruscas do tempo e contribui para a segurança de todos, especialmente em uma região que conhece de perto o impacto dos eventos climáticos. Para o produtor rural, a previsão é ferramenta de trabalho: a alternância entre dias firmes e a entrada de frentes úmidas influencia diretamente o planejamento das atividades no campo, da lavoura ao manejo dos animais. A recomendação para o fim de semana é clara: aproveitar os dias de tempo bom, programar-se para a virada prevista e manter o olho na previsão. Em São Lourenço do Sul, o serviço de informação da Defesa Civil reforça o cuidado com a comunidade e ajuda cada morador a organizar a sua rotina com mais tranquilidade.

### Legenda sugerida ###
Defesa Civil Municipal de São Lourenço do Sul aponta sexta e sábado estáveis, com virada do tempo prevista a partir da noite de sábado.

### Palavras-chave ###
São Lourenço do Sul, previsão do tempo, Defesa Civil, fim de semana, clima, Costa Doce
""",

    "ea8a271d9bc72061b2fe7f531e34bca69b145a69": """### Título ###
Escolas de Barra do Ribeiro recebem oficina de audiovisual pela Política Nacional Aldir Blanc

### Artigo ###
A cultura entrou na sala de aula em Barra do Ribeiro. As escolas municipais e o Colégio Estadual Carlos Pinto receberam a Oficina de Audiovisual da Padula Produções, projeto contemplado pela Política Nacional Aldir Blanc, que apresentou aos estudantes técnicas de produção e despertou novos olhares sobre a comunicação e a arte. Por meio de atividades práticas, os jovens tiveram a oportunidade de conhecer de perto o processo de criação audiovisual, da ideia inicial à realização. Levar esse tipo de experiência para dentro da escola tem um valor que vai além do conteúdo técnico. Muitos estudantes do interior nunca tiveram contato direto com a produção de vídeo, com os bastidores de uma filmagem ou com as profissões ligadas à comunicação e à cultura. Ao colocar a câmera na mão e mostrar como uma história ganha forma na tela, oficinas como essa abrem portas, despertam vocações e ampliam horizontes. O audiovisual é hoje uma das linguagens mais presentes no cotidiano dos jovens, que consomem vídeos a todo momento. Ensinar a produzir, e não apenas a assistir, transforma o estudante de espectador em criador, estimula o pensamento crítico e desenvolve habilidades que servem para a vida toda, da capacidade de se expressar ao trabalho em equipe. A iniciativa também fortalece a cultura local, valorizando a produção feita na própria região e incentivando que novas histórias sejam contadas a partir do olhar de quem vive ali. Projetos culturais que chegam às escolas cumprem um papel importante de democratizar o acesso à arte, levando para todos os estudantes oportunidades que muitas vezes ficavam restritas aos grandes centros. Para Barra do Ribeiro, receber a oficina é semear talento e oportunidade entre os jovens. Quando educação e cultura caminham juntas, a sala de aula se transforma em espaço de descoberta, e o futuro de toda uma geração ganha novas possibilidades.

### Legenda sugerida ###
Estudantes de Barra do Ribeiro participam da Oficina de Audiovisual contemplada pela Política Nacional Aldir Blanc e aprendem técnicas de produção.

### Palavras-chave ###
Barra do Ribeiro, oficina de audiovisual, cultura, educação, Política Nacional Aldir Blanc, juventude
""",

    "ce85cd87201e74ffe56eda208f34ac6cca2c198c": """### Título ###
Guaíba abre o Sarandeio Farroupilha do Centenário com festa descentralizada

### Artigo ###
A tradição gaúcha tomou conta de Guaíba. Começou o Sarandeio Farroupilha do Centenário, que neste ano acontece de forma descentralizada e leva a cultura campeira a diferentes regiões da cidade, com tiro de laço durante o dia e bailes à noite reunindo a comunidade em torno do chimarrão e do fandango. O primeiro dia teve início no Piquete Vem Pra Guaíba Tchê, junto do DTG Estância Farroupilha, com atividades campeiras ao longo do dia e baile à noite animando os participantes. A novidade do formato descentralizado é o grande diferencial desta edição. Ao levar a festa para diferentes pontos da cidade, em vez de concentrá-la em um único local, a organização aproxima a tradição de mais moradores e abre espaço para que um número maior de pessoas participe, dance e se reconheça nessa cultura. É uma forma de espalhar o sentimento farroupilha por toda a comunidade, valorizando os bairros e as entidades tradicionalistas que mantêm viva a chama da nossa história. Eventos como o Sarandeio cumprem um papel que vai além da diversão. Eles preservam uma herança que passa de geração em geração, fortalecem o sentimento de pertencimento e celebram aquilo que é a alma do Rio Grande do Sul: o cavalo, a pilcha, a prenda, o peão, a música e os costumes campeiros que ajudaram a formar a identidade do estado. Em tempos de tantas mudanças, manter essas tradições é também manter raízes. A cultura gaúcha é um dos maiores patrimônios do povo do Sul, e festas como essa garantem que ela continue pulsando entre as novas gerações. Para Guaíba, o Sarandeio Farroupilha do Centenário é motivo de orgulho e de união, um convite para que moradores de todas as idades vistam a pilcha, preparem a cuia e participem. A tradição, quando compartilhada, fica ainda mais forte, e a cidade mostra que sabe celebrar com alegria aquilo que a torna gaúcha de coração.

### Legenda sugerida ###
Guaíba dá início ao Sarandeio Farroupilha do Centenário em formato descentralizado, com tiro de laço e bailes celebrando a tradição gaúcha.

### Palavras-chave ###
Guaíba, Sarandeio Farroupilha, tradição gaúcha, cultura, tiro de laço, Rio Grande do Sul
""",

    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS acompanham com apreensão a renegociação de dívidas rurais

### Artigo ###
A apreensão toma conta do campo gaúcho. Produtores rurais do Rio Grande do Sul acompanham de perto a tramitação da renegociação de dívidas e temem ficar sem acesso ao crédito rural para a próxima safra, num momento em que a recuperação financeira de muitas propriedades depende de prazos e condições mais adequados à realidade do setor. O receio é concreto e tem raízes nos últimos anos. O produtor gaúcho enfrentou uma sequência difícil de adversidades climáticas, com estiagens severas, excesso de chuva em momentos decisivos e perdas expressivas de produtividade. A essas dificuldades somaram-se a oscilação dos preços das commodities e o aumento dos custos de produção, que apertaram as contas de quem vive da terra. O resultado é um endividamento que, sem alternativas de renegociação, pode comprometer a capacidade de o produtor financiar o próximo ciclo. O crédito rural é o combustível da produção. É com ele que o agricultor compra sementes, insumos, combustível e tudo o que precisa para colocar a lavoura no chão. Ficar sem acesso a esse recurso, ou tê-lo restringido por causa de dívidas em aberto, significa risco real de redução de área plantada, queda na produção e impacto em toda a cadeia que depende do campo, do comércio das cidades do interior à geração de empregos. Por isso, a discussão sobre prazos mais longos e condições compatíveis com a realidade rural é acompanhada com tanta atenção. Não se trata de um favor ao produtor, mas de garantir que a roda da economia continue girando, sustentando a renda no interior, a atividade nas pequenas cidades e o abastecimento de alimentos para o país. O agro gaúcho já provou inúmeras vezes a sua resiliência, levantando-se após cada adversidade. Mas resiliência também precisa de condições para se sustentar. Enquanto a definição não vem, o setor segue atento e na expectativa de uma solução que traga segurança e previsibilidade. O campo precisa de horizonte claro para seguir plantando, produzindo e fazendo a sua parte na economia do Rio Grande do Sul.

### Legenda sugerida ###
Produtores rurais do RS acompanham com apreensão a renegociação de dívidas, temendo perder acesso ao crédito rural para a próxima safra.

### Palavras-chave ###
agro, crédito rural, dívidas rurais, safra, Rio Grande do Sul, produtor rural
""",

    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": """### Título ###
Força-tarefa apreende 630 kg de alimentos impróprios para consumo no RS

### Artigo ###
A fiscalização tirou de circulação 630 quilos de alimentos impróprios para consumo no Rio Grande do Sul. Uma força-tarefa percorreu cinco estabelecimentos e recolheu carnes, ovos, amendoim, iogurtes, pães e bebidas que estavam fora das condições adequadas, em uma ação que reforça a proteção da saúde do consumidor. A operação foi conduzida com a participação do Ministério Público do Rio Grande do Sul e de órgãos de fiscalização. O volume apreendido chama a atenção e dá a dimensão do problema. Produtos sem procedência clara, armazenados de forma inadequada ou já vencidos representam um risco direto para quem os consome. Alimentos nessas condições podem provocar desde intoxicações alimentares, com sintomas como mal-estar, vômito e diarreia, até quadros mais graves, especialmente em crianças, idosos e pessoas com a imunidade fragilizada. Por isso, o trabalho de fiscalização é tão importante. Ele atua de forma preventiva, retirando do mercado aquilo que não deveria estar à venda antes que chegue à mesa das famílias. Esse tipo de operação também protege o comércio que trabalha de forma correta, coibindo práticas que geram concorrência desleal e colocam a população em risco. Para o consumidor, fica o alerta e a recomendação de adotar alguns cuidados simples no dia a dia. Vale sempre conferir a data de validade dos produtos, observar as condições de armazenamento e refrigeração, verificar a integridade das embalagens e desconfiar de preços e ofertas que fogem do razoável. Carnes e laticínios exigem atenção redobrada com a temperatura de conservação. Comprar em locais confiáveis e prestar atenção aos detalhes é uma forma de proteger a própria família. A apreensão dos 630 quilos de alimentos mostra que a fiscalização cumpre um papel essencial, ainda que nem sempre ganhe destaque. Garantir que o que chega à mesa tenha procedência e qualidade é cuidar da saúde de todos, e o trabalho de quem fiscaliza é um aliado importante do consumidor gaúcho.

### Legenda sugerida ###
Força-tarefa fiscaliza cinco estabelecimentos no RS e apreende 630 quilos de alimentos impróprios para consumo, protegendo a saúde do consumidor.

### Palavras-chave ###
Rio Grande do Sul, segurança alimentar, fiscalização, alimentos impróprios, Ministério Público, consumidor
""",

    "e93271ddd33993182fc7c76c4f992bb9ed645c87": """### Título ###
Amaral Ferrador conquista Unidade Odontológica Móvel para ampliar o atendimento

### Artigo ###
A saúde bucal de Amaral Ferrador ganhou um reforço de peso. O município conquistou uma Unidade Odontológica Móvel, equipamento que permitirá levar atendimento a diferentes localidades, ampliando o acesso da população, especialmente de quem vive no interior e tem mais dificuldade de chegar até a sede. A retirada da nova unidade foi cumprida em agenda oficial do município, com a participação do prefeito e da equipe de saúde. O equipamento funciona como um consultório odontológico sobre rodas, capaz de se deslocar até bairros e comunidades rurais para levar o serviço diretamente a quem precisa. Para muitas famílias do meio rural, o acesso ao dentista esbarra em obstáculos concretos: a distância até a sede do município, a dificuldade de deslocamento, o custo do transporte e a rotina de trabalho acabam adiando um cuidado básico, mas essencial. Com a unidade móvel, essa lógica se inverte. É o atendimento que vai ao encontro da comunidade, e não o contrário. A saúde bucal tem impacto direto na qualidade de vida das pessoas. Problemas dentários não tratados causam dor, dificultam a alimentação, afetam a fala e mexem com a autoestima, além de poderem evoluir para complicações mais sérias de saúde. Ampliar o acesso à odontologia é, portanto, cuidar da saúde de forma integral. Iniciativas como essa mostram que pensar a saúde no interior é também pensar em logística, em mobilidade e em estratégias criativas para chegar perto das pessoas. Levar o serviço até as comunidades reduz desigualdades de acesso e garante que moradores das localidades mais distantes tenham o mesmo direito ao atendimento que quem mora na área central. Para Amaral Ferrador, a chegada da Unidade Odontológica Móvel representa um avanço importante e concreto, com efeito direto no dia a dia da população. É a prova de que investir em saúde de proximidade faz diferença e de que, com planejamento, é possível levar cuidado a cada canto do município, sem deixar ninguém para trás.

### Legenda sugerida ###
Amaral Ferrador conquista Unidade Odontológica Móvel para levar atendimento odontológico a diferentes localidades, incluindo o interior.

### Palavras-chave ###
Amaral Ferrador, saúde bucal, unidade odontológica móvel, saúde, interior, Costa Doce
""",

    "f29cc027834a8ce15c786267925c81e25f66cf29": """### Título ###
COPSul encerra segunda edição em Pelotas com aprovação da Carta Compromisso

### Artigo ###
A região sul fechou dois dias de debate sobre o clima com um documento na mão. A segunda edição da Conferência Sul sobre Mudanças Climáticas, a COPSul, foi encerrada em Pelotas com a aprovação da Carta Compromisso, que reúne os principais encaminhamentos construídos durante o evento e reforça a articulação regional diante dos desafios climáticos. O documento sintetiza os debates realizados ao longo da conferência e aponta caminhos para o enfrentamento das mudanças do clima na região. O tema está longe de ser abstrato para quem vive no Sul do Rio Grande do Sul. A região conhece de perto os efeitos dos eventos climáticos extremos, com enchentes, estiagens e oscilações bruscas de tempo que afetam diretamente a produção rural, a infraestrutura das cidades e a vida das famílias. Para o agro, em especial, o clima é fator decisivo: define safras, influencia a produtividade e pode representar a diferença entre um bom ano e perdas expressivas. Por isso, discutir adaptação, prevenção e desenvolvimento sustentável deixou de ser pauta de futuro e se tornou urgência do presente. A força de um encontro como a COPSul está justamente na articulação. Quando municípios, entidades, universidades e comunidade se sentam à mesma mesa e saem com compromissos definidos, a região ganha capacidade de buscar soluções de forma conjunta e coordenada, em vez de enfrentar os problemas de maneira isolada. A Carta Compromisso funciona como um norte, registrando prioridades e direcionando esforços para os próximos passos. A construção de respostas às mudanças climáticas exige planejamento de longo prazo, integração entre diferentes setores e a participação ativa de toda a sociedade. Eventos que reúnem esses atores ajudam a transformar preocupação em ação concreta. Para a Costa Doce e para o conjunto do Sul gaúcho, o encerramento da COPSul com a aprovação do documento é um sinal positivo de que a região está atenta ao desafio do nosso tempo e disposta a agir. O clima não espera, e a articulação construída na conferência mostra um caminho de mobilização e responsabilidade diante daquilo que afeta a todos.

### Legenda sugerida ###
Segunda edição da Conferência Sul sobre Mudanças Climáticas é encerrada em Pelotas com a aprovação da Carta Compromisso e foco na articulação regional.

### Palavras-chave ###
COPSul, mudanças climáticas, Pelotas, Carta Compromisso, Costa Doce, Rio Grande do Sul, sustentabilidade
""",
}


if __name__ == "__main__":
    main()
