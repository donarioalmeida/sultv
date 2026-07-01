#!/usr/bin/env python3
"""
angular_2026-06-23.py — angulação editorial + redação (cowork-faz-tudo).
Decisões editoriais Claude na sessão para a pauta de 2026-06-23.
Regra 12 INEGOCIÁVEL: nenhum texto menciona veículos/portais/rádios/jornais.
Atribuição apenas a fontes primárias institucionais.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-23"


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

    # IDX 7 — Alerta de frio polar / Defesa Civil (São Lourenço do Sul) — PUBLICAR
    "35a13534bfbc272b8293793c681dc6bfeeee5c09": {
        "titulo_sultv": "Massa de ar polar traz frio intenso a São Lourenço do Sul entre 23 e 26 de junho",
        "chamada_faixa": "Frio polar avança sobre a Costa Doce",
        "subtitulo": "Aviso da Defesa Civil aponta período de frio persistente no Sul do Estado; cuidado redobrado com saúde, animais e lavouras.",
        "lead": "O inverno chega com força ao Sul do Estado. Entre os dias 23 e 26 de junho, uma massa de ar polar avança sobre o Rio Grande do Sul e coloca São Lourenço do Sul e outras cidades da Costa Doce em cenário de atenção, com frio intenso e persistente, segundo aviso da Defesa Civil.",
        "ganchos_3": [
            "Massa de ar polar provoca frio intenso entre 23 e 26 de junho",
            "São Lourenço do Sul está em cenário de atenção, assim como a região sul",
            "Cuidados com saúde, animais e lavouras devem ser redobrados"
        ],
        "angulo_editorial": "Serviço meteorológico de utilidade pública em cidade-núcleo. Fato concreto, datado e institucional (Defesa Civil). Alto interesse para audiência rural e urbana no auge do inverno. Sem viés partidário. Atribuição apenas à Coordenadoria Estadual de Proteção e Defesa Civil.",
        "fontes_complementares_sugeridas": ["Coordenadoria Estadual de Proteção e Defesa Civil (RS)", "Defesa Civil Municipal de São Lourenço do Sul"],
        "lead_materia_longa": "O inverno chega com força ao Sul do Estado. Entre os dias 23 e 26 de junho, uma massa de ar polar avança sobre o Rio Grande do Sul e coloca São Lourenço do Sul e outras cidades da Costa Doce em cenário de atenção, com frio intenso e persistente.",
        "post_instagram": {
            "caption": "Prepare o agasalho: o frio chegou para ficar. Entre os dias 23 e 26 de junho, uma massa de ar polar avança sobre o Rio Grande do Sul e coloca São Lourenço do Sul e a região sul em cenário de atenção, com temperaturas baixas e persistentes. É hora de redobrar os cuidados com crianças, idosos e pessoas mais vulneráveis, proteger os animais e ficar atento às lavouras. O frio faz parte do inverno gaúcho, mas a prevenção é o que garante a segurança de todos.",
            "hashtags": ["#SãoLourençoDoSul", "#Inverno", "#CostaDoce", "#DefesaCivil", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Prepare o agasalho: o frio chegou para ficar.",
            "desenvolvimento_45s": "Entre os dias 23 e 26 de junho, uma massa de ar polar avança sobre o Rio Grande do Sul e coloca São Lourenço do Sul e a região sul em cenário de atenção. O período será de frio intenso e persistente. É hora de redobrar os cuidados com crianças, idosos e pessoas mais vulneráveis, abrigar bem os animais e proteger as lavouras sensíveis à geada. O inverno gaúcho cobra atenção, e a informação correta é a melhor forma de prevenção.",
            "fechamento_8s": "A Costa Doce entra em alerta para o frio.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "ambiente calmo e sóbrio"
        },
        "tag_thumbnail": "frio intenso, São Lourenço do Sul",
        "briefing_visual": {
            "descricao_pt": "Amanhecer gelado de inverno na zona rural da Costa Doce com geada branca cobrindo o campo e neblina baixa, sem pessoas",
            "query_en": ["frost field winter morning", "frosty rural landscape fog", "cold winter countryside brazil"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Wide shot of a frosty rural field at dawn in southern Brazil, white frost covering the grass, low mist, cold blue light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço meteorológico institucional em cidade-núcleo, datado e altamente relevante no auge do inverno. Fonte primária Defesa Civil."
    },

    # IDX 10 — Programa Milho 100% (Barra do Ribeiro, agro) — PUBLICAR
    "09895e181ee1457e829cfcdff10c3f5cc16ae214": {
        "titulo_sultv": "Barra do Ribeiro prorroga até 24 de junho inscrições do Programa Milho 100%",
        "chamada_faixa": "Milho 100% tem prazo até 24 de junho",
        "subtitulo": "Programa destina sementes de milho e sorgo à agricultura familiar na safra 2026/2027; é preciso apresentar o CAF.",
        "lead": "Os produtores rurais de Barra do Ribeiro têm até o dia 24 de junho para garantir o benefício. A Prefeitura prorrogou as inscrições para o Programa Milho 100% da safra 2026/2027, que destina sementes de milho e sorgo à agricultura familiar do município, na região da Costa Doce.",
        "ganchos_3": [
            "Inscrições do Programa Milho 100% vão até 24 de junho",
            "Benefício destina sementes de milho e sorgo à agricultura familiar",
            "É obrigatório apresentar o CAF ou a Declaração de Aptidão"
        ],
        "angulo_editorial": "Pauta agro de serviço em município da Costa Doce — coração do público SulTV. Fato concreto, datado e institucional. Apoio à agricultura familiar com prazo iminente. Sem viés partidário. Atribuição à Secretaria da Agricultura e Meio Ambiente.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal da Agricultura e Meio Ambiente de Barra do Ribeiro", "Emater/RS"],
        "lead_materia_longa": "Os produtores rurais de Barra do Ribeiro têm até o dia 24 de junho para garantir o benefício. A Prefeitura prorrogou as inscrições para o Programa Milho 100% da safra 2026/2027, que destina sementes de milho e sorgo à agricultura familiar do município.",
        "post_instagram": {
            "caption": "Atenção, produtor rural de Barra do Ribeiro: o prazo está acabando. As inscrições para o Programa Milho 100% da safra 2026/2027 foram prorrogadas até 24 de junho. O programa destina sementes de milho e sorgo à agricultura familiar do município e é uma oportunidade concreta de reduzir custos e fortalecer a produção no campo. Para participar, é obrigatório apresentar o CAF, o Cadastro Nacional da Agricultura Familiar, ou a Declaração de Aptidão. Não deixe para a última hora.",
            "hashtags": ["#BarraDoRibeiro", "#Agro", "#AgriculturaFamiliar", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Produtor de Barra do Ribeiro, o prazo está acabando.",
            "desenvolvimento_45s": "As inscrições para o Programa Milho 100% da safra 2026/2027 foram prorrogadas até 24 de junho. O programa destina sementes de milho e sorgo à agricultura familiar do município, ajudando a reduzir custos e fortalecer a produção no campo. Para participar, é obrigatório apresentar o CAF, o Cadastro Nacional da Agricultura Familiar, ou a Declaração de Aptidão. Iniciativas assim mostram a importância de apoiar quem produz alimento no interior gaúcho.",
            "fechamento_8s": "Agricultura familiar com semente garantida na Costa Doce.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "country acústico leve"
        },
        "tag_thumbnail": "Programa Milho 100%, Barra do Ribeiro",
        "briefing_visual": {
            "descricao_pt": "Lavoura de milho ao amanhecer no Sul do Rio Grande do Sul, plantas verdes alinhadas, vista ampla, sem pessoas",
            "query_en": ["corn field rows sunrise", "maize crop farm brazil", "green corn plantation"],
            "evitar": ["pessoas com rosto visível", "marcas", "logos", "texto"],
            "prompt_ia": "Wide aerial shot of a green corn field in rows at sunrise in southern Brazil, golden light, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço agro em município da Costa Doce, alinhado ao público SulTV. Fato concreto e datado, prazo iminente. Fonte institucional."
    },

    # IDX 2 — Cursos gratuitos de qualificação (Tapes) — PUBLICAR
    "5279b35c5e2ae09eaa701098ea38a2d9a06c800c": {
        "titulo_sultv": "Tapes abre inscrições para cursos gratuitos de qualificação profissional",
        "chamada_faixa": "Tapes tem cursos gratuitos de qualificação",
        "subtitulo": "Programa RS Qualificação Recomeçar capacita em áreas com demanda de mão de obra e amplia chances de emprego e renda.",
        "lead": "Quem busca uma oportunidade no mercado de trabalho tem uma porta aberta em Tapes. A Prefeitura, por meio da Secretaria Municipal de Assistência Social, está com inscrições abertas para cursos gratuitos de qualificação profissional pelo Programa RS Qualificação Recomeçar, na região da Costa Doce.",
        "ganchos_3": [
            "Tapes abre inscrições para cursos gratuitos de qualificação",
            "Programa RS Qualificação Recomeçar amplia oportunidades de emprego e renda",
            "Capacitação foca em áreas com grande demanda de mão de obra"
        ],
        "angulo_editorial": "Serviço de educação e trabalho em cidade-núcleo. Fato concreto e institucional, com impacto direto na geração de renda. Sem viés partidário. Atribuição à Secretaria Municipal de Assistência Social.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Assistência Social de Tapes", "Programa RS Qualificação Recomeçar"],
        "lead_materia_longa": "Quem busca uma oportunidade no mercado de trabalho tem uma porta aberta em Tapes. A Prefeitura, por meio da Secretaria Municipal de Assistência Social, está com inscrições abertas para cursos gratuitos de qualificação profissional pelo Programa RS Qualificação Recomeçar.",
        "post_instagram": {
            "caption": "Qualificação que abre portas em Tapes. A Prefeitura está com inscrições abertas para cursos gratuitos de qualificação profissional pelo Programa RS Qualificação Recomeçar. A iniciativa capacita em áreas com grande demanda de mão de obra e amplia as chances de emprego e geração de renda. No interior, cursos gratuitos fazem diferença real: permitem que jovens e adultos melhorem o currículo sem que o custo seja um obstáculo. Quem tem interesse deve procurar a Secretaria Municipal de Assistência Social.",
            "hashtags": ["#Tapes", "#Qualificação", "#Emprego", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Qualificação que abre portas em Tapes.",
            "desenvolvimento_45s": "A Prefeitura de Tapes está com inscrições abertas para cursos gratuitos de qualificação profissional pelo Programa RS Qualificação Recomeçar. A iniciativa capacita em áreas com grande demanda de mão de obra e amplia as chances de emprego e geração de renda. No interior, cursos gratuitos fazem diferença real, ao permitir que jovens e adultos desenvolvam novas habilidades sem que o custo seja um obstáculo. Mão de obra preparada fortalece o comércio e os serviços do município.",
            "fechamento_8s": "Tapes investe em qualificação e oportunidade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "corporativo otimista leve"
        },
        "tag_thumbnail": "cursos gratuitos, Tapes",
        "briefing_visual": {
            "descricao_pt": "Sala de aula de curso profissionalizante com bancadas e ferramentas, ambiente de capacitação, sem rostos identificáveis",
            "query_en": ["vocational training classroom", "professional course workshop", "skills training hands tools"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Bright vocational training classroom with workbenches and tools, professional skills course setting, no recognizable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de educação e trabalho em cidade-núcleo. Fato concreto, institucional, alto interesse comunitário."
    },

    # IDX 4 — Concurso Peão e Prenda 2026 (Arambaré) — PUBLICAR
    "c6d53cb66b19db47387d26a05094ab2ffa6c9a0d": {
        "titulo_sultv": "Arambaré prorroga até 26 de junho inscrições para escolha de Peão e Prenda 2026",
        "chamada_faixa": "Arambaré escolhe Peão e Prenda 2026",
        "subtitulo": "Concurso integra a 35ª Semana Farroupilha do município e valoriza as tradições gaúchas na orla da Lagoa dos Patos.",
        "lead": "As tradições gaúchas ganham nova chance de representação em Arambaré. A Prefeitura prorrogou até 26 de junho as inscrições para o Concurso de Escolha do Peão e da Prenda 2026, que integra a 35ª Semana Farroupilha do município, na orla da Lagoa dos Patos.",
        "ganchos_3": [
            "Inscrições para Peão e Prenda 2026 vão até 26 de junho",
            "Concurso integra a 35ª Semana Farroupilha de Arambaré",
            "Tradição valoriza a cultura gaúcha no interior da Costa Doce"
        ],
        "angulo_editorial": "Cultura e tradição em cidade-núcleo (Arambaré). Fato concreto e datado, forte engajamento comunitário. Celebração da identidade gaúcha. Sem viés partidário. Atribuição à Prefeitura de Arambaré.",
        "fontes_complementares_sugeridas": ["Prefeitura de Arambaré", "Comissão da 35ª Semana Farroupilha de Arambaré"],
        "lead_materia_longa": "As tradições gaúchas ganham nova chance de representação em Arambaré. A Prefeitura prorrogou até 26 de junho as inscrições para o Concurso de Escolha do Peão e da Prenda 2026, que integra a 35ª Semana Farroupilha do município.",
        "post_instagram": {
            "caption": "Quem tem orgulho das tradições gaúchas tem mais tempo para participar. As inscrições para o Concurso de Escolha do Peão e da Prenda 2026 de Arambaré foram prorrogadas até 26 de junho. O concurso integra a 35ª Semana Farroupilha do município e é a oportunidade de representar Arambaré em um dos momentos mais importantes da cultura local. Mais do que um título, ser peão ou prenda é levar adiante os valores, os costumes e a história do povo gaúcho.",
            "hashtags": ["#Arambaré", "#SemanaFarroupilha", "#Tradição", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Quem ama as tradições gaúchas tem mais tempo para participar.",
            "desenvolvimento_45s": "As inscrições para o Concurso de Escolha do Peão e da Prenda 2026 de Arambaré foram prorrogadas até 26 de junho. O concurso integra a 35ª Semana Farroupilha do município, na orla da Lagoa dos Patos, e é a oportunidade de representar a cidade em um dos momentos mais importantes da cultura local. Mais do que um título, ser peão ou prenda é levar adiante os valores, os costumes e a história do povo gaúcho, que seguem vivos no interior.",
            "fechamento_8s": "Arambaré celebra a tradição na Semana Farroupilha.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "vaneira / música gaúcha"
        },
        "tag_thumbnail": "Peão e Prenda, Arambaré",
        "briefing_visual": {
            "descricao_pt": "Traje típico gaúcho — pilcha, bombacha, prenda com vestido de prenda — em cenário campeiro do Rio Grande do Sul, sem rostos identificáveis",
            "query_en": ["gaucho traditional outfit brazil", "rio grande do sul tradition pilcha", "south brazil rural tradition"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Traditional gaucho attire details, pilcha and prenda dress, campeiro setting in southern Brazil, warm tones, no recognizable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura tradicional em cidade-núcleo (Arambaré), datada, forte engajamento. Identidade gaúcha."
    },

    # IDX 22 — Amistoso de futsal hoje (Dom Feliciano) — PUBLICAR
    "75cb051a9ff492106aa226496841fe21557279db": {
        "titulo_sultv": "Dom Feliciano e Cristal se enfrentam em amistoso de futsal nesta terça-feira",
        "chamada_faixa": "Dom Feliciano x Cristal no futsal hoje",
        "subtitulo": "Seleções dos dois municípios da Costa Doce jogam às 21h30 no Ginásio Municipal de Dom Feliciano.",
        "lead": "O esporte reúne a comunidade nesta terça-feira em Dom Feliciano. As seleções de Dom Feliciano e de Cristal, dois municípios da Costa Doce, se enfrentam em um amistoso de futsal às 21h30, no Ginásio Municipal, em partida aberta à torcida.",
        "ganchos_3": [
            "Amistoso de futsal entre Dom Feliciano e Cristal nesta terça",
            "Jogo acontece às 21h30 no Ginásio Municipal de Dom Feliciano",
            "Esporte reúne a comunidade e valoriza os atletas do interior"
        ],
        "angulo_editorial": "Evento esportivo comunitário em cidade-núcleo, datado para hoje. Reúne dois municípios da Costa Doce. Alto engajamento local, sem viés partidário. Não se trata de esporte de região distante, mas de mobilização comunitária regional.",
        "fontes_complementares_sugeridas": ["Prefeitura de Dom Feliciano", "Secretaria Municipal de Esportes de Dom Feliciano"],
        "lead_materia_longa": "O esporte reúne a comunidade nesta terça-feira em Dom Feliciano. As seleções de Dom Feliciano e de Cristal, dois municípios da Costa Doce, se enfrentam em um amistoso de futsal às 21h30, no Ginásio Municipal.",
        "post_instagram": {
            "caption": "É dia de futsal e de emoção em quadra! As seleções de Dom Feliciano e de Cristal se enfrentam nesta terça-feira, 23 de junho, às 21h30, no Ginásio Municipal de Dom Feliciano. Um confronto entre dois municípios da Costa Doce que promete grandes jogadas, espírito esportivo e o apoio da torcida. Eventos como esse valorizam os atletas do interior e reúnem a comunidade em torno do esporte. Venha prestigiar e fazer a sua parte na arquibancada.",
            "hashtags": ["#DomFeliciano", "#Cristal", "#Futsal", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "É dia de futsal e de emoção em quadra!",
            "desenvolvimento_45s": "As seleções de Dom Feliciano e de Cristal se enfrentam nesta terça-feira, às 21h30, no Ginásio Municipal de Dom Feliciano. Um confronto entre dois municípios da Costa Doce que promete grandes jogadas e muito espírito esportivo. Eventos como esse valorizam os atletas do interior, incentivam a prática esportiva entre crianças e jovens e reúnem a comunidade em torno de uma noite de lazer e torcida.",
            "fechamento_8s": "A Costa Doce em quadra nesta terça.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "energética esportiva"
        },
        "tag_thumbnail": "futsal, Dom Feliciano",
        "briefing_visual": {
            "descricao_pt": "Quadra de futsal de ginásio com bola em primeiro plano e arquibancada ao fundo, ambiente esportivo, sem rostos identificáveis",
            "query_en": ["futsal court indoor ball", "indoor soccer gym", "sports arena empty court"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Indoor futsal court with a ball in the foreground and bleachers in the background, sports atmosphere, no recognizable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento esportivo comunitário em cidade-núcleo, datado para hoje, alto engajamento. Mobilização regional da Costa Doce."
    },

    # IDX 29 — Pré-lançamento de livro nativista (Canguçu) — PUBLICAR
    "036d741218cd3b2147eb733fb0abbcc447cea41f": {
        "titulo_sultv": "Canguçu recebe pré-lançamento do livro 'Estradas do Tempo – Versos Nativos'",
        "chamada_faixa": "Canguçu lança livro de versos nativos",
        "subtitulo": "Obra valoriza a cultura e a identidade canguçuense e reforça a literatura produzida no interior gaúcho.",
        "lead": "A cultura do interior ganha mais uma página em Canguçu. A cidade recebe o pré-lançamento do livro 'Estradas do Tempo – Versos Nativos', obra que valoriza a identidade e as tradições canguçuenses e reforça a literatura nativista do Rio Grande do Sul.",
        "ganchos_3": [
            "Canguçu recebe pré-lançamento do livro 'Estradas do Tempo'",
            "Obra valoriza a cultura e a identidade canguçuense",
            "Iniciativa fortalece a literatura nativista do interior gaúcho"
        ],
        "angulo_editorial": "Cultura e literatura regional em município do Sul do Estado. Fato concreto e positivo, valoriza a produção cultural do interior. Sem viés partidário.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Cultura de Canguçu"],
        "lead_materia_longa": "A cultura do interior ganha mais uma página em Canguçu. A cidade recebe o pré-lançamento do livro 'Estradas do Tempo – Versos Nativos', obra que valoriza a identidade e as tradições canguçuenses e reforça a literatura nativista do Rio Grande do Sul.",
        "post_instagram": {
            "caption": "A poesia do campo ganha vida em Canguçu. A cidade recebe o pré-lançamento do livro 'Estradas do Tempo – Versos Nativos', uma obra que celebra a identidade, as tradições e a alma do povo canguçuense. Mais do que um livro, é um registro da cultura nativista que atravessa gerações no interior gaúcho. Iniciativas como essa mantêm viva a memória das comunidades e mostram que a literatura também floresce longe dos grandes centros.",
            "hashtags": ["#Canguçu", "#Cultura", "#Literatura", "#Nativismo", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A poesia do campo ganha vida em Canguçu.",
            "desenvolvimento_45s": "A cidade recebe o pré-lançamento do livro 'Estradas do Tempo – Versos Nativos', uma obra que celebra a identidade, as tradições e a alma do povo canguçuense. Mais do que um livro, é um registro da cultura nativista que atravessa gerações no interior gaúcho. Iniciativas como essa mantêm viva a memória das comunidades, incentivam novos autores e mostram que a literatura também floresce longe dos grandes centros.",
            "fechamento_8s": "Canguçu celebra a cultura nativista.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "violão nativista suave"
        },
        "tag_thumbnail": "livro, Canguçu",
        "briefing_visual": {
            "descricao_pt": "Livro aberto sobre mesa de madeira rústica com paisagem campeira ao fundo, clima nativista, sem rostos identificáveis",
            "query_en": ["open book rustic wooden table", "poetry book countryside", "book pages warm light"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto legível"],
            "prompt_ia": "An open book resting on a rustic wooden table with a soft countryside backdrop, warm nativist atmosphere, no recognizable faces, no readable text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Cultura e literatura regional, fato concreto e positivo, valoriza produção do interior. Diversifica a pauta."
    },

    # IDX 31 — 1º Arraiá da Serra do Sudeste (Encruzilhada do Sul) — PUBLICAR (nota_curta)
    "1dc4162665694c78c967f97fb0dcc114d3cf2b4e": {
        "titulo_sultv": "1º Arraiá da Serra do Sudeste lota o centro de Encruzilhada do Sul",
        "chamada_faixa": "Arraiá lota o centro de Encruzilhada",
        "subtitulo": "Festa junina movimenta o município da Serra do Sudeste com público e comércio aquecido.",
        "lead": "A tradição junina tomou conta de Encruzilhada do Sul. O 1º Arraiá da Serra do Sudeste lotou o centro do município, reunindo grande público em uma das celebrações mais animadas do calendário de junho na região.",
        "ganchos_3": [
            "1º Arraiá da Serra do Sudeste lota o centro de Encruzilhada",
            "Festa junina reúne grande público e aquece o comércio",
            "Tradição fortalece a cultura popular da Serra do Sudeste"
        ],
        "angulo_editorial": "Evento cultural junino de grande público na Serra do Sudeste. Fato concreto, engajamento e impacto no comércio. Sem viés partidário. Nota curta.",
        "fontes_complementares_sugeridas": ["Prefeitura de Encruzilhada do Sul"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "A festa tomou conta da Serra do Sudeste! O 1º Arraiá da Serra do Sudeste lotou o centro de Encruzilhada do Sul, com música, comidas típicas e muita animação. Mais do que diversão, a festa junina movimenta o comércio, reúne as famílias e fortalece a cultura popular da região. Uma estreia que já entra para o calendário cultural do interior gaúcho.",
            "hashtags": ["#EncruzilhadaDoSul", "#Arraiá", "#FestaJunina", "#SerraDoSudeste", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A festa tomou conta da Serra do Sudeste!",
            "desenvolvimento_45s": "O 1º Arraiá da Serra do Sudeste lotou o centro de Encruzilhada do Sul, com música, comidas típicas e muita animação. Mais do que diversão, a festa junina movimenta o comércio local, gera oportunidades e reúne as famílias em torno de uma das tradições mais queridas de junho. Uma estreia que já mostra força e entra para o calendário cultural do interior gaúcho.",
            "fechamento_8s": "Encruzilhada vive a festa de São João.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "forró animado"
        },
        "tag_thumbnail": "Arraiá, Encruzilhada do Sul",
        "briefing_visual": {
            "descricao_pt": "Festa junina noturna com bandeirinhas coloridas e barracas iluminadas em praça do interior gaúcho, sem rostos identificáveis",
            "query_en": ["festa junina bunting night", "june festival stalls lights", "brazilian street festival"],
            "evitar": ["rostos identificáveis", "marcas", "logos", "texto"],
            "prompt_ia": "Nighttime Brazilian June festival with colorful bunting flags and illuminated food stalls in a small-town square, festive lights, no recognizable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento cultural junino de grande público na Serra do Sudeste, fato concreto, engajamento. Formato nota curta."
    },

    # ====== REBAIXAR / BLOQUEAR ======

    # IDX 0 — pessoa encontrada na via, reanimação 25 min (tragédia/saúde) — BLOQUEAR
    "d666b1db933167b53fa29714647601d23642ad5e": _skip(
        "BLOQUEAR", "Possível tragédia com vítima e contexto médico/saúde (reanimação). Guardrail tragédia/saúde."),
    # IDX 1 — relato de dependência química com pessoa nomeada — BLOQUEAR
    "c7db66a6fe8c045689ed648c22733f857a0eb04b": _skip(
        "BLOQUEAR", "Relato pessoal de dependência química com indivíduo privado nomeado. Guardrail saúde/sensível."),
    # IDX 3 — FUNBEA Tapes — REBAIXAR (segundo item de Tapes; quota por cidade/diversidade)
    "b64a24d1d6a321e379c0312612e100e440e93710": _skip(
        "REBAIXAR", "Segundo item de Tapes no dia; priorizado item de cursos. Conteúdo institucional procedural."),
    # IDX 5 — Nota técnica poda Arambaré — REBAIXAR (segundo item de Arambaré)
    "4d53d3c82a893d291ff6de3b083b9bf127ac8347": _skip(
        "REBAIXAR", "Segundo item de Arambaré; priorizado o Concurso de Peão e Prenda. Nota técnica procedural."),
    # IDX 6 — vacinação inverno São Lourenço — REBAIXAR (segundo item da cidade)
    "c77a362745e1d703331af70e6d247db07e7de071": _skip(
        "REBAIXAR", "Segundo item de São Lourenço; priorizado o alerta de frio. Serviço de saúde genérico."),
    # IDX 8 — Edital penalidade Chuvisca — BLOQUEAR (edital procedural / corpo vazio)
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR", "Edital procedural sem conteúdo jornalístico (corpo vazio)."),
    # IDX 9 — Edital perímetro urbano Chuvisca — BLOQUEAR (edital procedural / corpo vazio)
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR", "Edital procedural sem conteúdo jornalístico (corpo vazio)."),
    # IDX 11 — Alistamento militar Barra do Ribeiro — REBAIXAR (genérico, 2º item da cidade)
    "a8eccb2e8abe61c0228309df154714203c920fca": _skip(
        "REBAIXAR", "Serviço nacional genérico e segundo item de Barra do Ribeiro; priorizado o Programa Milho."),
    # IDX 12 — Aviso audiência pública Sentinela — BLOQUEAR (procedural, corpo vazio)
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR", "Aviso procedural sem conteúdo (corpo vazio)."),
    # IDX 13 — Emissão notas fiscais Sentinela — BLOQUEAR (procedural, defasado)
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR", "Comunicado fiscal procedural e defasado (05/05). Sem valor editorial atual."),
    # IDX 14 — Rua Camaquã calçamento Cristal — REBAIXAR (corpo vazio; coberto por outro item)
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": _skip(
        "REBAIXAR", "Corpo vazio; tema de infraestrutura de Cristal coberto em nível menor."),
    # IDX 15 — Inadimplência Vale do Taquari — REBAIXAR (região distante / agregado)
    "239aec7cc7606777878095e03df1110f97d079b7": _skip(
        "REBAIXAR", "Dado agregado do Vale do Taquari, região distante da cobertura Sul-RS. Sem âncora regional."),
    # IDX 16 — Av. Passo do Mendonça Cristal — REBAIXAR (serviço urbano menor, 2º de Cristal)
    "804da2cbe08274dd604274d8db6acc48cc218fed": _skip(
        "REBAIXAR", "Serviço urbano de baixo valor noticioso; segundo item de Cristal."),
    # IDX 17 — limpeza banheiros Guaíba — REBAIXAR
    "e49941209a05422fa376e9fa6cf2f7e512967b60": _skip(
        "REBAIXAR", "Serviço de manutenção de baixo valor noticioso."),
    # IDX 18 — desentupimento valos Guaíba — REBAIXAR
    "0727df7740bf49094df0e16c463860636177c279": _skip(
        "REBAIXAR", "Serviço de manutenção rotineiro; baixo valor noticioso."),
    # IDX 19 — Edital leilão extrajudicial Pelotas — BLOQUEAR (edital procedural)
    "4f9805dc40fa231052926c912de748ec5ec2011b": _skip(
        "BLOQUEAR", "Edital de leilão procedural sem conteúdo editorial."),
    # IDX 20 — PPPs / privatizações / plebiscito ALERS — BLOQUEAR (política partidária)
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "BLOQUEAR", "Tema político-partidário (privatizações, plebiscito, manifestações de parlamentares). Guardrail política."),
    # IDX 21 — Funcriança / destinação de recursos ALERS — REBAIXAR (fora do núcleo, procedural/defasado)
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR", "Pauta de Porto Alegre fora do núcleo, procedural e com data defasada."),
    # IDX 23 — entrega materiais MDC Dom Feliciano — REBAIXAR (2º item da cidade)
    "ef21472a803575b509d4d17f9e7a0a20fc9c9474": _skip(
        "REBAIXAR", "Segundo item de Dom Feliciano; priorizado o amistoso de futsal."),
    # IDX 24 — protocolo raios Copa do Mundo — REBAIXAR (internacional, sem âncora regional)
    "31982e4065225320a0905b990cfbc8686d5008fd": _skip(
        "REBAIXAR", "Pauta internacional (Copa do Mundo) sem âncora regional Sul-RS."),
    # IDX 25 — amanhecer inverno -4°C RS — REBAIXAR (redundante com alerta de frio)
    "055873b031808b741b618cba95d17d541d948a3e": _skip(
        "REBAIXAR", "Redundante com o alerta de frio polar já priorizado para publicação."),
    # IDX 26 — ciclone tropical Copa do Mundo — BLOQUEAR (internacional, sem âncora)
    "a6683f9edcfc9c862dd9febe7d25aba45d237a5d": _skip(
        "BLOQUEAR", "Pauta internacional (Copa do Mundo) sem âncora regional."),
    # IDX 27 — quarta-feira frio e geada RS — REBAIXAR (redundante clima)
    "b0889a9f85770aca01833915dbfe96c99e135c06": _skip(
        "REBAIXAR", "Redundante com o alerta de frio polar já priorizado."),
    # IDX 28 — conquista Amaral Ferrador — REBAIXAR (conteúdo raso)
    "8a50524b05412a99383e77829984d51dbc94eee0": _skip(
        "REBAIXAR", "Conteúdo raso, sem fato concreto descrito."),
    # IDX 30 — exposição Mario Quintana Canguçu — REBAIXAR (2º item da cidade)
    "7fc90a8deff317cf8159ee3210d10b72db027b44": _skip(
        "REBAIXAR", "Segundo item de Canguçu; priorizado o pré-lançamento do livro."),
    # IDX 32 — Feira do Livro UFSM Santa Maria — REBAIXAR (fora do núcleo, cadastro procedural)
    "f0fde321c4466a55dcefddc0c960c6e231a4e791": _skip(
        "REBAIXAR", "Cadastro procedural fora do núcleo de cobertura."),
    # IDX 33 — formação juventude Rio Grande — REBAIXAR
    "b07719172890f3fef5d2df8a8fd4aec714e127b5": _skip(
        "REBAIXAR", "Conteúdo institucional de baixo valor noticioso; formato post."),
    # IDX 34 — alfabetização Rio Grande — REBAIXAR
    "d68776fd739bd1467f612957ec9133b34e19ff72": _skip(
        "REBAIXAR", "Registro de evento já realizado; baixo valor noticioso atual."),
    # IDX 35 — Pátio Rural Santa Maria — REBAIXAR (fora do núcleo)
    "ed54daf8bae3cd1a2b942df2b94ccf3c584783fe": _skip(
        "REBAIXAR", "Evento fora do núcleo de cobertura; formato post."),
    # IDX 36 — alistamento militar Encantado — REBAIXAR
    "185c029cbe5698ab3120100f441807d513e6f627": _skip(
        "REBAIXAR", "Serviço nacional genérico fora do núcleo."),
    # IDX 37 — prisão furtos Pinheiro Machado/Bagé — REBAIXAR (policial fora do núcleo)
    "afc11adae9702f1b4588045be18a4a77a4c471d9": _skip(
        "REBAIXAR", "Ocorrência policial fora do núcleo de cobertura."),
    # IDX 38 — atenção comunidade interior Encruzilhada (saúde) — REBAIXAR (raso)
    "51fd7f4caab4fe45242fac569896d3f8a9291cb7": _skip(
        "REBAIXAR", "Aviso de saúde raso, sem fato concreto."),
    # IDX 39 — adolescente apreendido com drogas Venâncio Aires — BLOQUEAR (menor)
    "74e7b8fbb074d57e8e34a2071e2a464520847134": _skip(
        "BLOQUEAR", "Conteúdo envolvendo menor de idade. Guardrail menores."),
    # IDX 40 — prefeito ouvido CPI Corsan Venâncio Aires — BLOQUEAR (política partidária)
    "20b392071086a05706afc8ada901180c48761ded": _skip(
        "BLOQUEAR", "Tema político-partidário (CPI). Guardrail política."),
    # IDX 41 — edital processo seletivo Monte Belo do Sul — BLOQUEAR (edital procedural)
    "7d269a6762432fb1a0ee45388a62c5192bc8e700": _skip(
        "BLOQUEAR", "Edital procedural sem conteúdo editorial; fora do núcleo."),
    # IDX 42 — casos suspeitos meningite Bento Gonçalves — BLOQUEAR (saúde sensível, fora do núcleo)
    "9031ea4b54b20445726dab4110363ff8fcac7fbc": _skip(
        "BLOQUEAR", "Suspeita de surto de doença (meningite) — saúde sensível; fora do núcleo de cobertura."),
}


MATERIAS = {

    "35a13534bfbc272b8293793c681dc6bfeeee5c09": """### Título ###
Massa de ar polar traz frio intenso a São Lourenço do Sul entre 23 e 26 de junho

### Artigo ###
O inverno chega com força ao Sul do Estado. Entre os dias 23 e 26 de junho, uma massa de ar polar avança sobre o Rio Grande do Sul e coloca São Lourenço do Sul e outras cidades da região sul em cenário de atenção, com frio intenso e persistente, segundo aviso meteorológico da Coordenadoria Estadual de Proteção e Defesa Civil. O período deve registrar temperaturas baixas ao longo de vários dias, exigindo cuidado redobrado de toda a comunidade. Quando o frio se instala por dias seguidos, os riscos vão além do desconforto. As baixas temperaturas favorecem a circulação de vírus respiratórios e podem agravar quadros de saúde, principalmente em crianças, idosos e pessoas mais vulneráveis. Por isso, manter-se aquecido, evitar mudanças bruscas de temperatura e proteger as vias respiratórias são atitudes simples que fazem diferença nesta época do ano. No campo, a atenção também precisa ser dobrada. O frio intenso e a possibilidade de geada exigem cuidado com os animais, que devem ter abrigo adequado, e com as lavouras sensíveis às baixas temperaturas. Produtores rurais da Costa Doce conhecem bem o desafio do inverno gaúcho, e a informação antecipada ajuda no planejamento das próximas atividades. A orientação da Defesa Civil é acompanhar a evolução do tempo e adotar medidas de prevenção em casa, no trabalho e na estrada, já que o frio costuma vir acompanhado de neblina e umidade. Pequenos cuidados evitam acidentes e problemas de saúde. O inverno faz parte da rotina do Sul do Rio Grande do Sul, mas cada estação cobra preparo. Em São Lourenço do Sul e nas cidades vizinhas, a recomendação é clara: agasalhar-se bem, cuidar de quem é mais frágil e ficar atento aos avisos oficiais durante todo o período de frio.

### Legenda sugerida ###
Defesa Civil alerta para massa de ar polar e frio intenso em São Lourenço do Sul entre 23 e 26 de junho.

### Palavras-chave ###
frio intenso, São Lourenço do Sul, massa de ar polar, Defesa Civil, inverno, Costa Doce, geada
""",

    "09895e181ee1457e829cfcdff10c3f5cc16ae214": """### Título ###
Barra do Ribeiro prorroga até 24 de junho inscrições do Programa Milho 100%

### Artigo ###
Os produtores rurais de Barra do Ribeiro têm até o dia 24 de junho para garantir o benefício. A Prefeitura, por meio da Secretaria Municipal da Agricultura e Meio Ambiente, prorrogou as inscrições para o Programa Milho 100% da safra 2026/2027, que destina sementes de milho e sorgo à agricultura familiar do município, na região da Costa Doce. A medida amplia o prazo para que mais famílias do campo possam participar. Programas como esse têm um peso concreto na vida de quem produz. O fornecimento de sementes reduz um dos principais custos do plantio, dá previsibilidade ao produtor e estimula a continuidade da atividade no campo, especialmente entre os agricultores familiares, que respondem por boa parte da produção de alimentos no interior gaúcho. Milho e sorgo, além do consumo, são fundamentais para a alimentação animal, o que reforça toda a cadeia produtiva local. Para participar, é obrigatório apresentar o CAF, o Cadastro Nacional da Agricultura Familiar, ou a Declaração de Aptidão. A exigência garante que o benefício chegue a quem realmente atua na agricultura familiar, dentro das regras do programa. Quem ainda não se inscreveu deve procurar a Secretaria Municipal da Agricultura e Meio Ambiente dentro do prazo. O apoio à agricultura familiar é também investimento no desenvolvimento do município. Quando o produtor tem condições de plantar, a renda circula no comércio local, a produção de alimentos se mantém e a permanência das famílias no campo é fortalecida. Iniciativas que distribuem sementes e insumos ajudam a enfrentar custos crescentes e a manter a atividade viva. Ao prorrogar as inscrições do Programa Milho 100%, Barra do Ribeiro reforça o compromisso com quem produz e com a vocação agrícola da Costa Doce, lembrando o produtor de que o prazo é curto e a oportunidade, concreta.

### Legenda sugerida ###
Inscrições do Programa Milho 100% em Barra do Ribeiro vão até 24 de junho e destinam sementes à agricultura familiar.

### Palavras-chave ###
Programa Milho 100%, Barra do Ribeiro, agricultura familiar, sementes de milho, sorgo, CAF, Costa Doce
""",

    "5279b35c5e2ae09eaa701098ea38a2d9a06c800c": """### Título ###
Tapes abre inscrições para cursos gratuitos de qualificação profissional

### Artigo ###
Quem busca uma oportunidade no mercado de trabalho tem uma porta aberta em Tapes. A Prefeitura, por meio da Secretaria Municipal de Assistência Social, está com inscrições abertas para cursos gratuitos de qualificação profissional pelo Programa RS Qualificação Recomeçar, na região da Costa Doce. A iniciativa tem como objetivo ampliar as chances de emprego e a geração de renda, oferecendo capacitação em áreas com grande demanda de mão de obra. Cursos gratuitos de qualificação cumprem um papel decisivo no interior. Eles permitem que jovens e adultos desenvolvam novas habilidades, melhorem o currículo e aumentem as chances de conquistar uma vaga, sem que o custo seja um obstáculo. Para muitas famílias, é a oportunidade de recomeçar, mudar de área ou ingressar no mercado formal de trabalho com mais preparo. Investir em qualificação é investir no desenvolvimento da própria cidade. Mão de obra mais capacitada atrai negócios, fortalece o comércio e os serviços, agrega valor às atividades locais e contribui para fixar talentos na região, reduzindo a necessidade de deslocamento para os grandes centros em busca de oportunidades. É um ganho que se reflete em toda a comunidade. Para quem tem interesse, o caminho é simples: ficar atento ao período de inscrição e procurar a Secretaria Municipal de Assistência Social, responsável pela organização das turmas. A orientação é não deixar para a última hora, já que as vagas costumam ser concorridas. Iniciativas como essa mostram que a qualificação profissional não é privilégio dos grandes centros e pode chegar com força às cidades da Costa Doce. Ao abrir essas turmas, Tapes reforça que educação e trabalho caminham juntos na construção de oportunidades concretas para a população.

### Legenda sugerida ###
Tapes está com inscrições abertas para cursos gratuitos de qualificação profissional pelo Programa RS Qualificação Recomeçar.

### Palavras-chave ###
cursos gratuitos, Tapes, qualificação profissional, RS Qualificação Recomeçar, emprego, renda, Costa Doce
""",

    "c6d53cb66b19db47387d26a05094ab2ffa6c9a0d": """### Título ###
Arambaré prorroga até 26 de junho inscrições para escolha de Peão e Prenda 2026

### Artigo ###
As tradições gaúchas ganham nova chance de representação em Arambaré. A Prefeitura prorrogou até 26 de junho as inscrições para o Concurso de Escolha do Peão e da Prenda 2026, que integra a 35ª Semana Farroupilha do município, na orla da Lagoa dos Patos. A ampliação do prazo abre espaço para que mais jovens orgulhosos das tradições se candidatem a representar a cidade em um dos momentos mais importantes da cultura local. Ser peão ou prenda vai muito além de um título. Os escolhidos passam a ser embaixadores da cultura gaúcha, presentes em eventos, datas cívicas e celebrações que mantêm vivos os costumes, a vestimenta, a música e os valores do povo do interior. É um papel de responsabilidade e de orgulho, que conecta as novas gerações com a história e a identidade do Rio Grande do Sul. A Semana Farroupilha é o ponto alto desse calendário. Em sua 35ª edição em Arambaré, a celebração reúne a comunidade em torno das tradições, movimenta o município e reforça o sentimento de pertencimento que caracteriza as cidades gaúchas. Concursos como o de Peão e Prenda envolvem famílias inteiras e despertam o interesse dos mais jovens pela cultura regional. Para participar, os interessados devem ficar atentos ao novo prazo e seguir as orientações da organização do concurso. A prorrogação é um convite para que ninguém fique de fora dessa oportunidade. Manter viva a tradição é um esforço coletivo, que depende do engajamento da comunidade a cada edição. Ao prorrogar as inscrições, Arambaré reafirma o valor que dá à cultura gaúcha e à Semana Farroupilha, mostrando que, na orla da Lagoa dos Patos, as raízes do Rio Grande do Sul seguem firmes e celebradas com orgulho.

### Legenda sugerida ###
Inscrições para a escolha de Peão e Prenda 2026 de Arambaré, na 35ª Semana Farroupilha, vão até 26 de junho.

### Palavras-chave ###
Arambaré, Peão e Prenda, Semana Farroupilha, tradições gaúchas, cultura, Costa Doce, Lagoa dos Patos
""",

    "75cb051a9ff492106aa226496841fe21557279db": """### Título ###
Dom Feliciano e Cristal se enfrentam em amistoso de futsal nesta terça-feira

### Artigo ###
O esporte reúne a comunidade nesta terça-feira em Dom Feliciano. As seleções de Dom Feliciano e de Cristal, dois municípios da Costa Doce, se enfrentam em um amistoso de futsal às 21h30, no Ginásio Municipal, em partida aberta à torcida. O confronto promete grandes jogadas, espírito esportivo e o calor das arquibancadas, em mais uma noite dedicada ao esporte no interior gaúcho. Amistosos como esse têm um valor que vai além do placar. Eles incentivam a prática esportiva, valorizam os atletas que representam os municípios e aproximam comunidades vizinhas em torno de um clima saudável de rivalidade. Para muitos jovens, ver de perto uma partida da seleção da cidade é o que desperta o interesse pelo esporte e a vontade de um dia vestir a camisa do município. O futsal é uma das modalidades mais populares no interior, justamente por exigir pouca estrutura e reunir jogadores de todas as idades. Em cidades como Dom Feliciano e Cristal, as quadras e os ginásios são pontos de encontro da comunidade, espaços onde o esporte se mistura com o lazer e o convívio social. Promover jogos e amistosos é também uma forma de cuidar da saúde e do bem-estar da população. A expectativa é de boa presença de público no Ginásio Municipal de Dom Feliciano. O apoio da torcida faz diferença para os atletas e transforma o amistoso em uma verdadeira festa do esporte. Iniciativas que aproximam os municípios e fortalecem o calendário esportivo merecem incentivo. Nesta terça-feira, a bola rola na Costa Doce, e a quadra promete ser palco de emoção, dedicação e do orgulho de duas cidades que valorizam o esporte como ferramenta de integração comunitária.

### Legenda sugerida ###
Seleções de Dom Feliciano e Cristal jogam amistoso de futsal nesta terça, às 21h30, no Ginásio Municipal de Dom Feliciano.

### Palavras-chave ###
futsal, Dom Feliciano, Cristal, amistoso, esporte, Costa Doce, comunidade
""",

    "036d741218cd3b2147eb733fb0abbcc447cea41f": """### Título ###
Canguçu recebe pré-lançamento do livro 'Estradas do Tempo – Versos Nativos'

### Artigo ###
A cultura do interior ganha mais uma página em Canguçu. A cidade recebe o pré-lançamento do livro 'Estradas do Tempo – Versos Nativos', obra que valoriza a identidade e as tradições canguçuenses e reforça a literatura nativista do Rio Grande do Sul. O evento celebra a produção cultural local e coloca em destaque a poesia que nasce do campo, da lida e da memória das comunidades do interior gaúcho. A literatura nativista tem um papel especial na cultura do Estado. Por meio dos versos, ela registra o modo de vida, os valores e as paisagens que formam a identidade do povo gaúcho, transmitindo de geração em geração histórias que poderiam se perder com o tempo. Obras como essa são, ao mesmo tempo, expressão artística e documento cultural de uma região. O pré-lançamento de um livro também é um momento de encontro. Reúne autores, leitores, admiradores da cultura nativista e a comunidade em torno da valorização das letras produzidas longe dos grandes centros. Eventos assim incentivam novos escritores, estimulam o hábito da leitura e mostram que o interior tem voz e talento próprios para contar as suas histórias. Para Canguçu, receber o pré-lançamento é motivo de orgulho. A cidade reafirma a sua vocação cultural e abre espaço para que a produção local alcance mais leitores. Valorizar a literatura nativista é também valorizar a história e a identidade da comunidade, fortalecendo o sentimento de pertencimento que une as pessoas. Ao acolher 'Estradas do Tempo – Versos Nativos', Canguçu mostra que a cultura segue viva e em movimento no interior gaúcho, e que a poesia continua sendo uma ponte poderosa entre o passado, o presente e as futuras gerações.

### Legenda sugerida ###
Canguçu recebe o pré-lançamento do livro 'Estradas do Tempo – Versos Nativos', que valoriza a cultura nativista local.

### Palavras-chave ###
Canguçu, Estradas do Tempo, versos nativos, literatura nativista, cultura, poesia, interior gaúcho
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
            print(f"[angular] sem angulação para {h} — bloqueando")
            angul = _skip("BLOQUEAR", "Sem angulação configurada — descartado pelo guardrail")
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


if __name__ == "__main__":
    main()
