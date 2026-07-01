#!/usr/bin/env python3
"""
angular_dia_2026_06_08.py — angulação editorial + redação (fluxo cowork-faz-tudo).

Pauta de 2026-06-08. Lê state/aprovadas_2026-06-08.json, gera
state/pauta_2026-06-08.json com decisao_final e escreve
state/materias_2026-06-08/<id_hash>.md para cada PUBLICAR + materia_longa.

Regra 12 (INEGOCIÁVEL): nenhum texto menciona veículos/fontes de comunicação.
Atribuição apenas a fontes primárias institucionais.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-08"


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
    # #0 Camaquã — Murilo Cardoso, título mundial de jiu-jitsu — PUBLICAR materia_longa
    "1fb11c1f31a01fb5ce1038c92ebe74fa30835b80": {
        "titulo_sultv": "Atleta de Camaquã conquista título inédito no Mundial de Jiu-Jitsu",
        "chamada_faixa": "Camaquense é campeão mundial de jiu-jitsu",
        "subtitulo": "Murilo Cardoso celebrou a conquista na faixa azul e creditou o resultado ao apoio recebido da comunidade camaquense.",
        "lead": "O atleta camaquense Murilo Cardoso conquistou um título inédito no Mundial de Jiu-Jitsu na faixa azul e levou o nome de Camaquã ao pódio internacional. O resultado coroa anos de treino e o apoio constante da comunidade local, lembrado pelo próprio atleta após a vitória.",
        "ganchos_3": [
            "Camaquense conquista título mundial inédito de jiu-jitsu na faixa azul",
            "Murilo Cardoso credita a conquista ao apoio da comunidade",
            "Esporte de Camaquã ganha projeção internacional"
        ],
        "angulo_editorial": "Esporte e comunidade em cidade-núcleo (Camaquã) — conquista positiva, identidade local forte, projeção internacional de um atleta da Costa Doce. Tom celebrativo e institucional.",
        "fontes_complementares_sugeridas": ["Prefeitura de Camaquã", "Secretaria Municipal de Esportes", "academias de jiu-jitsu locais"],
        "lead_materia_longa": "O atleta camaquense Murilo Cardoso conquistou um título inédito no Mundial de Jiu-Jitsu na faixa azul, levando o nome de Camaquã ao pódio internacional.",
        "post_instagram": {
            "caption": "De Camaquã para o mundo. O atleta Murilo Cardoso conquistou um título inédito no Mundial de Jiu-Jitsu na faixa azul e fez questão de lembrar o apoio que sempre recebeu da comunidade camaquense. Mais um nome da Costa Doce brilhando no esporte. Parabéns, campeão!",
            "hashtags": ["#Camaquã", "#JiuJitsu", "#Esporte", "#CostaDoce", "#Campeão", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "De Camaquã para o mundo.",
            "desenvolvimento_45s": "O atleta camaquense Murilo Cardoso conquistou um título inédito no Mundial de Jiu-Jitsu na faixa azul. A vitória coloca Camaquã no mapa internacional do esporte e coroa anos de dedicação aos tatames. Depois da conquista, o atleta fez questão de lembrar o apoio que sempre recebeu da comunidade camaquense, dos treinadores e da família, que acompanharam de perto cada etapa dessa trajetória.",
            "fechamento_8s": "Mais um orgulho da Costa Doce.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental épico leve"
        },
        "tag_thumbnail": "Campeão mundial de Camaquã",
        "briefing_visual": {
            "descricao_pt": "Atleta de jiu-jitsu com quimono e faixa azul em pose de vitória sobre tatame de ginásio, sem rosto identificável",
            "query_en": ["jiu jitsu athlete blue belt gi", "brazilian jiu jitsu podium victory", "bjj competition tatami"],
            "evitar": ["rosto identificável de pessoa específica", "marcas", "texto", "logos"],
            "prompt_ia": "A jiu-jitsu athlete wearing a gi with a blue belt standing victorious on a gymnasium tatami, face not clearly identifiable, dramatic light, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Conquista esportiva concreta e positiva em cidade-núcleo (Camaquã), com forte identidade local e projeção internacional"
    },

    # #1 Camaquã — previsão do tempo da semana — PUBLICAR materia_longa
    "aec2e9473018e7bb5e535fe6c05fa1c0adf6f243": {
        "titulo_sultv": "Chuva forte abre a semana em Camaquã, com melhora do tempo ate quarta",
        "chamada_faixa": "Semana comeca chuvosa em Camaqua",
        "subtitulo": "Segunda-feira concentra o maior volume de chuva; sol volta a aparecer entre nuvens a partir de quarta-feira na regiao.",
        "lead": "A semana começa com chuva forte em Camaquã e na Costa Doce, com a segunda-feira concentrando o maior volume de precipitação. A tendência é de melhora gradual nos dias seguintes, com o sol voltando a aparecer entre nuvens a partir de quarta-feira, um cenário importante para o planejamento das atividades no campo e na cidade.",
        "ganchos_3": [
            "Segunda-feira concentra o maior volume de chuva na semana",
            "Tempo melhora gradualmente até quarta-feira",
            "Cenário interessa a produtores e à rotina urbana da Costa Doce"
        ],
        "angulo_editorial": "Previsão do tempo de serviço para cidade-núcleo (Camaquã) — utilidade imediata para rotina urbana e planejamento agrícola da Costa Doce. Tom prático e direto.",
        "fontes_complementares_sugeridas": ["órgãos de meteorologia", "Defesa Civil municipal", "Emater/RS-Ascar"],
        "lead_materia_longa": "A semana começa com chuva forte em Camaquã e na Costa Doce, com a segunda-feira concentrando o maior volume de precipitação e melhora gradual até quarta-feira.",
        "post_instagram": {
            "caption": "Prepare o guarda-chuva: a semana começa com chuva forte em Camaquã, e a segunda-feira deve concentrar o maior volume. A boa notícia é que o tempo melhora gradualmente, com o sol voltando a aparecer entre nuvens a partir de quarta-feira. Fique de olho na previsão para organizar a rotina no campo e na cidade.",
            "hashtags": ["#Camaquã", "#PrevisãoDoTempo", "#Clima", "#CostaDoce", "#Chuva", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Semana começa com chuva em Camaquã.",
            "desenvolvimento_45s": "A semana abre com chuva forte em Camaquã e na Costa Doce. A segunda-feira deve concentrar o maior volume de precipitação, exigindo atenção redobrada no trânsito e nas áreas mais baixas. A partir de terça, a tendência é de melhora, e o sol volta a aparecer entre nuvens já na quarta-feira. Para quem trabalha no campo, é momento de ajustar o planejamento das atividades à janela de tempo firme que se aproxima.",
            "fechamento_8s": "Tempo firme volta no meio da semana.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Previsão do tempo Camaquã",
        "briefing_visual": {
            "descricao_pt": "Céu carregado de nuvens escuras de chuva sobre lavoura ou rua de cidade do interior do Rio Grande do Sul, sem pessoas",
            "query_en": ["dark rain clouds over field", "storm clouds rural town brazil", "heavy rain countryside sky"],
            "evitar": ["pessoas", "marcas", "texto", "logos"],
            "prompt_ia": "Heavy dark rain clouds gathering over a rural field and small town in southern Brazil, dramatic overcast sky, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Previsão do tempo de serviço, oportuna (semana atual) e de utilidade imediata para cidade-núcleo (Camaquã)"
    },

    # #2 Tapes/RS — Fiergs robótica nas escolas públicas — PUBLICAR materia_longa
    "71d8e4c166749fecf87911b126851418544f1bfb": {
        "titulo_sultv": "Robótica chega às escolas públicas do RS com nova formação para alunos e professores",
        "chamada_faixa": "Robotica chega as escolas publicas do RS",
        "subtitulo": "Projeto leva a robótica às escolas municipais gaúchas e capacita docentes, com o objetivo de modernizar a educação pública.",
        "lead": "Um novo projeto de formação em robótica vai levar a tecnologia às escolas municipais do Rio Grande do Sul, capacitando alunos e professores da rede pública. A iniciativa busca aproximar os estudantes do pensamento computacional e da inovação desde cedo, com impacto direto na qualidade da educação gaúcha.",
        "ganchos_3": [
            "Robótica vai chegar às escolas municipais gaúchas",
            "Formação capacita alunos e professores da rede pública",
            "Objetivo é modernizar a educação e a inovação no RS"
        ],
        "angulo_editorial": "Inovação e educação no RS — pauta de tecnologia aplicada à escola pública, de interesse de famílias e educadores; alinhada ao foco de inovação da SulTV. Tom positivo e institucional.",
        "fontes_complementares_sugeridas": ["Sistema Fiergs", "secretarias municipais de Educação", "escolas da rede pública"],
        "lead_materia_longa": "Um novo projeto de formação em robótica vai levar a tecnologia às escolas municipais do Rio Grande do Sul, capacitando alunos e professores da rede pública.",
        "post_instagram": {
            "caption": "A robótica vai entrar na sala de aula. Um novo projeto leva formação em robótica às escolas municipais do Rio Grande do Sul, capacitando alunos e professores da rede pública. A ideia é aproximar os estudantes do pensamento computacional e da inovação desde cedo, preparando a próxima geração para o futuro do trabalho.",
            "hashtags": ["#Educação", "#Robótica", "#Inovação", "#RioGrandeDoSul", "#Tecnologia", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Robótica na escola pública gaúcha.",
            "desenvolvimento_45s": "Um novo projeto de formação em robótica vai levar a tecnologia às escolas municipais do Rio Grande do Sul. A iniciativa capacita tanto os alunos quanto os professores da rede pública, com o objetivo de aproximar os estudantes do pensamento computacional e da inovação desde os primeiros anos. A aposta é que o contato com a robótica desperte vocações e prepare a próxima geração de gaúchos para um mercado de trabalho cada vez mais tecnológico.",
            "fechamento_8s": "Educação e inovação de mãos dadas.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental tecnológico otimista"
        },
        "tag_thumbnail": "Robótica na escola pública",
        "briefing_visual": {
            "descricao_pt": "Crianças em sala de aula montando um pequeno robô educacional sobre a mesa, mãos e peças em foco, sem rostos identificáveis",
            "query_en": ["kids robotics classroom education", "students building educational robot", "STEM robotics school kit"],
            "evitar": ["rostos identificáveis de crianças", "marcas", "texto", "logos"],
            "prompt_ia": "Students in a public school classroom assembling a small educational robot on a desk, focus on hands and robot parts, faces not identifiable, bright daylight, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Inovação e educação pública no RS — alinhado ao foco editorial; fato concreto (lançamento de projeto), sem viés partidário"
    },

    # #3 Tapes — último dia Enem 2026 — REBAIXAR (serviço expirado)
    "e8243e7e1901a6c9be6fc53a4655813d09f9cca9": _skip(
        "REBAIXAR",
        "Conteúdo de serviço com prazo já encerrado (inscrição do Enem terminou em 05/06); publicar em 08/06 induziria o leitor a erro"
    ),

    # #4 Arambaré — cursos gratuitos (datado 16/04) — REBAIXAR (defasado)
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "REBAIXAR",
        "Notícia datada de 16/04/2026 capturada de página antiga; inscrições provavelmente encerradas — sem fato novo para publicar"
    ),

    # #5 Arambaré — plataforma de pesca (datado 19/01) — REBAIXAR (defasado)
    "7328151d0f689699ca147e00ec7ffb87008ee51e": _skip(
        "REBAIXAR",
        "Notícia datada de 19/01/2026 capturada de página antiga; sem atualização que justifique republicação"
    ),

    # #6 Chuvisca — edital de penalidade — BLOQUEAR
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR",
        "Edital procedural (penalidade administrativa) — não é matéria jornalística"
    ),

    # #7 Chuvisca — edital de prazo — BLOQUEAR
    "7dc8c84f6a2274ce2305fbd2b2e9844f2ada167c": _skip(
        "BLOQUEAR",
        "Edital procedural (abertura de prazo) — não é matéria jornalística"
    ),

    # #8 Sentinela do Sul — aviso de audiência pública — BLOQUEAR
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR",
        "Cabeçalho/aviso procedural sem corpo de texto — sem fato concreto"
    ),

    # #9 Sentinela do Sul — emissão de notas fiscais — BLOQUEAR
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR",
        "Comunicado administrativo procedural (emissor de NF) — não é matéria jornalística"
    ),

    # #10 Barra do Ribeiro — cabeçalho Secretaria Administração — BLOQUEAR
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": _skip(
        "BLOQUEAR",
        "Cabeçalho de seção administrativa (contracheques) capturado pelo scraper — não é matéria"
    ),

    # #11 Barra do Ribeiro — lei proíbe fogos com estampido — PUBLICAR materia_longa
    "6d583901d0b2623e718e91c071da59f2069c1522": {
        "titulo_sultv": "Barra do Ribeiro proíbe fogos com estampido por lei municipal",
        "chamada_faixa": "Barra do Ribeiro proibe fogos com estampido",
        "subtitulo": "Lei Municipal nº 2850/2025 veta o uso de fogos de artifício com barulho, em medida que protege animais e pessoas sensíveis a ruídos.",
        "lead": "Barra do Ribeiro passou a proibir o uso de fogos de artifício com estampido em todo o município, por força da Lei Municipal nº 2850/2025. A medida acompanha uma tendência crescente em cidades gaúchas e busca proteger animais domésticos e silvestres, além de pessoas mais sensíveis ao barulho, como autistas, idosos e bebês.",
        "ganchos_3": [
            "Lei municipal proíbe fogos com estampido em Barra do Ribeiro",
            "Medida protege animais e pessoas sensíveis a ruídos",
            "Cidade acompanha tendência de fogos silenciosos no RS"
        ],
        "angulo_editorial": "Legislação municipal concreta com forte apelo de comunidade e bem-estar animal — pauta positiva e de serviço, sem viés partidário. Interessa a famílias, tutores de animais e produtores rurais da Costa Doce.",
        "fontes_complementares_sugeridas": ["Prefeitura de Barra do Ribeiro", "Câmara de Vereadores", "Secretaria de Agricultura e Meio Ambiente"],
        "lead_materia_longa": "Barra do Ribeiro passou a proibir o uso de fogos de artifício com estampido em todo o município, por força da Lei Municipal nº 2850/2025.",
        "post_instagram": {
            "caption": "Barra do Ribeiro disse não ao barulho. A Lei Municipal nº 2850/2025 proíbe o uso de fogos de artifício com estampido em todo o município. A medida protege animais domésticos e silvestres, além de pessoas mais sensíveis ao ruído, como autistas, idosos e bebês. Comemorar sem assustar quem a gente ama é possível.",
            "hashtags": ["#BarraDoRibeiro", "#BemEstarAnimal", "#FogosSilenciosos", "#CostaDoce", "#Legislação", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Adeus aos fogos barulhentos.",
            "desenvolvimento_45s": "Barra do Ribeiro proibiu o uso de fogos de artifício com estampido em todo o município, por meio da Lei Municipal nº 2850 de 2025. A medida acompanha uma tendência que cresce nas cidades gaúchas e tem dois objetivos principais: proteger animais domésticos e silvestres, que sofrem com o barulho intenso, e resguardar pessoas mais sensíveis ao ruído, como autistas, idosos e bebês. Os fogos sem estampido, que produzem apenas efeitos visuais, seguem permitidos.",
            "fechamento_8s": "Festa pode continuar, sem o susto.",
            "cta_5s": "Detalhes no SulTV.",
            "trilha_sugerida": "instrumental suave"
        },
        "tag_thumbnail": "Fogos com estampido proibidos",
        "briefing_visual": {
            "descricao_pt": "Cão doméstico assustado encolhido em ambiente residencial, ou fogos de artifício silenciosos coloridos no céu noturno, sem pessoas",
            "query_en": ["scared dog hiding fireworks", "silent fireworks colorful night sky", "pet anxiety loud noise"],
            "evitar": ["pessoas identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Colorful silent fireworks lighting up a night sky over a small Brazilian town, no loud burst, calm atmosphere, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Lei municipal concreta com apelo de comunidade e bem-estar animal em cidade da Costa Doce; pauta positiva e de serviço"
    },

    # #12 Cristal — Rua Camaquã, obras de calçamento — PUBLICAR materia_longa
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": {
        "titulo_sultv": "Rua Camaquã, em Cristal, recebe preparação para obras de calçamento",
        "chamada_faixa": "Cristal prepara calcamento da Rua Camaqua",
        "subtitulo": "Serviços de terraplanagem e preparo do leito antecedem a pavimentação da via, que vai beneficiar moradores e o tráfego local.",
        "lead": "A Rua Camaquã, em Cristal, começou a receber os serviços de preparação que antecedem as obras de calçamento. A intervenção, conduzida pela prefeitura, marca o início de mais uma etapa de pavimentação na cidade-núcleo da Costa Doce e deve melhorar a mobilidade e as condições de tráfego para os moradores da região.",
        "ganchos_3": [
            "Rua Camaquã começa a ser preparada para o calçamento",
            "Obra melhora mobilidade e tráfego em Cristal",
            "Mais uma etapa de pavimentação na cidade da Costa Doce"
        ],
        "angulo_editorial": "Infraestrutura urbana em cidade-núcleo (Cristal) — pauta de serviço e melhoria local, de interesse direto dos moradores. Tom institucional e positivo.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria de Obras", "moradores da Rua Camaquã"],
        "lead_materia_longa": "A Rua Camaquã, em Cristal, começou a receber os serviços de preparação que antecedem as obras de calçamento.",
        "post_instagram": {
            "caption": "Obra à vista em Cristal! A Rua Camaquã começou a receber os serviços de preparação que antecedem o calçamento. É mais uma etapa de pavimentação na cidade, que promete melhorar a mobilidade e o dia a dia de quem mora e circula pela região. Acompanhe o avanço das obras.",
            "hashtags": ["#Cristal", "#Infraestrutura", "#Pavimentação", "#CostaDoce", "#ObrasPúblicas", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cristal avança na pavimentação.",
            "desenvolvimento_45s": "A Rua Camaquã, em Cristal, começou a receber os serviços de preparação do leito que antecedem as obras de calçamento. A intervenção marca o início de mais uma etapa de pavimentação na cidade e deve melhorar a mobilidade e as condições de tráfego para os moradores. Obras como essa reduzem a poeira no tempo seco e a lama nos dias de chuva, melhorando o acesso e a qualidade de vida nos bairros atendidos.",
            "fechamento_8s": "Mais uma rua a caminho do asfalto.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental neutro"
        },
        "tag_thumbnail": "Obras de calçamento em Cristal",
        "briefing_visual": {
            "descricao_pt": "Rua de terra em cidade do interior recebendo terraplanagem e preparo para pavimentação, máquina ao fundo, sem pessoas identificáveis",
            "query_en": ["road construction earthwork small town", "street paving preparation machinery", "dirt road grading brazil"],
            "evitar": ["rostos identificáveis", "marcas de máquinas legíveis", "texto", "logos"],
            "prompt_ia": "A dirt street in a small Brazilian town being graded and prepared for paving, construction machinery in the background, daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Infraestrutura urbana concreta em cidade-núcleo (Cristal); pauta de serviço e melhoria local"
    },

    # #13 São Lourenço do Sul — selo vacina (duplicata sem resumo) — REBAIXAR
    "4ceb630b463e5a73d241cc134657509620995c00": _skip(
        "REBAIXAR",
        "Duplicata do mesmo fato (selo Amigo da Vacina) — versão sem resumo; mantida a versão com conteúdo (ff08...)"
    ),

    # #14 São Lourenço do Sul — selo prata Amigo da Vacina — PUBLICAR nota_curta
    "ff08241618128d19c4b248113b1c116cebb5459a": {
        "titulo_sultv": "São Lourenço do Sul conquista selo prata 'Amigo da Vacina'",
        "chamada_faixa": "Sao Lourenco ganha selo Amigo da Vacina",
        "subtitulo": "Reconhecimento estadual premia o cumprimento das metas de cobertura vacinal; município agora busca ampliar a adesão das crianças.",
        "lead": "São Lourenço do Sul foi certificado com o selo Amigo da Vacina, na categoria Prata, pelo cumprimento das metas de cobertura vacinal no Rio Grande do Sul. O reconhecimento, segundo a Secretaria Municipal da Saúde, valoriza o engajamento da população nas campanhas de imunização e impulsiona o município a ampliar a adesão das crianças.",
        "ganchos_3": [
            "São Lourenço do Sul recebe selo prata 'Amigo da Vacina'",
            "Reconhecimento premia o cumprimento das metas de cobertura vacinal",
            "Município quer ampliar a adesão das crianças às campanhas"
        ],
        "angulo_editorial": "Conquista institucional de saúde pública em cidade-núcleo (São Lourenço do Sul) — reconhecimento positivo, sem teor médico-prescritivo nem identificação de pacientes; foco no mérito municipal e no engajamento da comunidade.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal da Saúde de São Lourenço do Sul", "Secretaria Estadual da Saúde"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Motivo de orgulho em São Lourenço do Sul: o município conquistou o selo Amigo da Vacina, na categoria Prata, pelo cumprimento das metas de cobertura vacinal no Rio Grande do Sul. O reconhecimento valoriza o engajamento da comunidade, e agora a meta é ampliar ainda mais a adesão das crianças. Vacina é proteção!",
            "hashtags": ["#SãoLourençoDoSul", "#AmigoDaVacina", "#SaúdePública", "#CostaDoce", "#Vacinação", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "São Lourenço é amigo da vacina.",
            "desenvolvimento_45s": "São Lourenço do Sul foi certificado com o selo Amigo da Vacina, na categoria Prata, em nível estadual. O reconhecimento veio pelo cumprimento das metas de cobertura vacinal, com destaque para o engajamento da população nas campanhas de imunização. Agora, o município trabalha para ampliar ainda mais a adesão das crianças, mantendo as taxas de cobertura em dia.",
            "fechamento_8s": "Cidade referência em vacinação.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental positivo"
        },
        "tag_thumbnail": "Selo Amigo da Vacina",
        "briefing_visual": {
            "descricao_pt": "Posto de saúde ou unidade de vacinação em cidade do interior do RS, ambiente acolhedor, sem pacientes identificáveis",
            "query_en": ["vaccination health clinic interior", "public health vaccine campaign", "health post small town brazil"],
            "evitar": ["pacientes identificáveis", "crianças com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Interior of a friendly municipal health clinic prepared for a vaccination campaign in a small Brazilian town, no identifiable people, warm daylight, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Conquista institucional de saúde pública em cidade-núcleo; reconhecimento positivo sem teor médico-prescritivo nem identificação de pacientes"
    },

    # #15 Cristal — Av. Passo do Mendonça limpeza — REBAIXAR (redundante c/ #12)
    "804da2cbe08274dd604274d8db6acc48cc218fed": _skip(
        "REBAIXAR",
        "Serviço urbano de menor relevância e redundante com outra pauta de obras de Cristal já priorizada no dia; vira nota interna"
    ),

    # #16 Pelotas — produtores de morango / associação / Emater — PUBLICAR materia_longa
    "5243be736e2649528d6bc837fd8bbde97e1353d1": {
        "titulo_sultv": "Produtores de morango de Pelotas debatem criação de associação",
        "chamada_faixa": "Morangueiros de Pelotas debatem associacao",
        "subtitulo": "Cerca de 30 produtores discutiram, em reunião apoiada pela Emater/RS-Ascar, os ganhos da organização coletiva na comercialização e no acesso a políticas públicas.",
        "lead": "Cerca de 30 produtores de morango de Pelotas se reuniram para discutir a criação de uma associação que fortaleça o setor na região. O encontro, promovido com apoio da Emater/RS-Ascar, debateu os benefícios da organização coletiva, especialmente na comercialização, no acesso a políticas públicas e no fortalecimento da representatividade da categoria na Costa Doce.",
        "ganchos_3": [
            "Cerca de 30 produtores de morango discutem criação de associação",
            "Organização coletiva amplia força na comercialização",
            "Emater/RS-Ascar apoia o fortalecimento do setor em Pelotas"
        ],
        "angulo_editorial": "Agro de proximidade na Costa Doce ampliada (Pelotas) — fruticultura familiar, organização coletiva e apoio institucional da Emater; pauta central para a audiência rural da SulTV. Tom institucional e propositivo.",
        "fontes_complementares_sugeridas": ["Emater/RS-Ascar", "Secretaria Municipal de Desenvolvimento Rural de Pelotas", "produtores de morango"],
        "lead_materia_longa": "Cerca de 30 produtores de morango de Pelotas se reuniram para discutir a criação de uma associação que fortaleça o setor na região, em encontro promovido com apoio da Emater/RS-Ascar.",
        "post_instagram": {
            "caption": "Juntos, os morangueiros são mais fortes. Cerca de 30 produtores de morango de Pelotas se reuniram, com apoio da Emater/RS-Ascar, para discutir a criação de uma associação. A organização coletiva traz ganhos na comercialização, no acesso a políticas públicas e na representatividade do setor. A fruticultura da Costa Doce de olho no futuro.",
            "hashtags": ["#Pelotas", "#Morango", "#Agro", "#Emater", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Morangueiros se unem em Pelotas.",
            "desenvolvimento_45s": "Cerca de 30 produtores de morango de Pelotas se reuniram para discutir a criação de uma associação que represente o setor na região. O encontro, apoiado pela Emater/RS-Ascar, mostrou os benefícios da organização coletiva: mais força na hora de comercializar, acesso facilitado a políticas públicas e maior representatividade da categoria. É a fruticultura familiar da Costa Doce buscando se profissionalizar e crescer de forma sustentável.",
            "fechamento_8s": "União para fortalecer o campo.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental rural otimista"
        },
        "tag_thumbnail": "Produtores de morango se unem",
        "briefing_visual": {
            "descricao_pt": "Lavoura de morango com frutas vermelhas maduras em primeiro plano e estufa ao fundo no Sul do Brasil, sem pessoas identificáveis",
            "query_en": ["strawberry farm field red berries", "strawberry greenhouse cultivation", "strawberry harvest brazil"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Close-up of ripe red strawberries in a cultivated field with a greenhouse in the background in southern Brazil, soft daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agro de proximidade com fonte primária institucional (Emater) na Costa Doce ampliada; pauta central para a audiência rural"
    },

    # #17 Pelotas — Justiça do Trabalho R$156,8mi — REBAIXAR (estadual, âncora fraca)
    "a6885d87261ed899066eaed1e127d684baa35ba1": _skip(
        "REBAIXAR",
        "Pauta estadual de conciliação trabalhista com âncora local fraca em Pelotas; conteúdo seco e institucional — vira nota interna"
    ),

    # #18 Porto Alegre — parlamentares concessões/PPPs — BLOQUEAR (política partidária)
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "BLOQUEAR",
        "Manifestações parlamentares sobre privatizações e concessões — tema político-partidário (guardrail)"
    ),

    # #19 Porto Alegre — Funcriança / destinação de recursos — REBAIXAR (procedural)
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR",
        "Conteúdo procedural sobre destinação de recursos a fundo; baixo apelo de audiência e fora das cidades-núcleo"
    ),

    # #20 RS — neve há um ano / El Niño — PUBLICAR materia_longa
    "01e4af8f22701aee0014a55e168747935cd1d8cd": {
        "titulo_sultv": "Um ano após a neve, El Niño deve dificultar nevadas no inverno de 2026",
        "chamada_faixa": "El Nino deve dificultar neve no inverno",
        "subtitulo": "Há um ano, o Sul registrava neve com acumulação em pleno mês de maio; para 2026, as condições de grande escala jogam contra a repetição do fenômeno.",
        "lead": "Há um ano, em maio de 2025, o Sul do Brasil registrava neve com acumulação no Rio Grande do Sul e em Santa Catarina, um fenômeno incomum para a época. Para o inverno de 2026, as análises meteorológicas indicam um cenário diferente: a presença do El Niño tende a dificultar a ocorrência de novas nevadas na região.",
        "ganchos_3": [
            "Neve de maio de 2025 completa um ano",
            "El Niño tende a dificultar nevadas no inverno de 2026",
            "Regime de chuvas é o que mais importa para o produtor"
        ],
        "angulo_editorial": "Clima e safra no RS — pauta de interesse amplo (memória da neve + previsão de inverno) com gancho prático para o produtor rural, que depende do regime de chuvas do El Niño. Tom explicativo e institucional, sem citar veículos.",
        "fontes_complementares_sugeridas": ["órgãos e institutos de meteorologia", "Emater/RS-Ascar", "Defesa Civil"],
        "lead_materia_longa": "Há um ano, em maio de 2025, o Sul do Brasil registrava neve com acumulação no Rio Grande do Sul e em Santa Catarina; para o inverno de 2026, o El Niño tende a dificultar a ocorrência de novas nevadas.",
        "post_instagram": {
            "caption": "Lembra da neve do ano passado? Em maio de 2025, o Sul do Brasil teve neve com acumulação, algo raro para a época. Para o inverno de 2026, o cenário muda: a presença do El Niño tende a dificultar novas nevadas. O frio não some, mas o que mais interessa ao campo é o regime de chuvas, que influencia diretamente o planejamento da safra.",
            "hashtags": ["#Clima", "#ElNiño", "#Inverno2026", "#RioGrandeDoSul", "#Agro", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A neve volta em 2026?",
            "desenvolvimento_45s": "Há um ano, em maio de 2025, o Sul do Brasil registrava neve com acumulação no Rio Grande do Sul e em Santa Catarina, algo raro para a época. Para o inverno de 2026, o cenário é outro: a presença do El Niño tende a dificultar a formação de neve. Isso não significa que o frio vai faltar, mas as condições de grande escala jogam contra o espetáculo branco. Para o produtor rural, o sinal mais importante do El Niño é o regime de chuvas, que afeta o planejamento da safra.",
            "fechamento_8s": "De olho no inverno que vem.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental contemplativo"
        },
        "tag_thumbnail": "El Niño e o inverno de 2026",
        "briefing_visual": {
            "descricao_pt": "Paisagem de campo gaúcho coberto por geada ou neve fina ao amanhecer na Serra, sem pessoas",
            "query_en": ["frost field winter morning", "snow southern brazil highlands", "frozen pasture sunrise"],
            "evitar": ["pessoas", "marcas", "texto", "logos"],
            "prompt_ia": "A rural field in the southern Brazilian highlands covered with light frost at sunrise, cold winter atmosphere, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima de interesse amplo no RS com gancho prático para o produtor (regime de chuvas/safra); reescrita sem citar veículo de meteorologia"
    },

    # #21 RS — renegociação de dívidas rurais / Senado — PUBLICAR materia_longa
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": {
        "titulo_sultv": "Produtores do RS temem que renegociação de dívidas rurais trave no Senado",
        "chamada_faixa": "Campo gaucho teme travar renegociacao de dividas",
        "subtitulo": "Setor receia ficar sem acesso ao crédito rural para a próxima safra caso a proposta não avance; endividamento se agravou com estiagens e enchentes.",
        "lead": "Produtores rurais do Rio Grande do Sul vivem a expectativa pela votação da renegociação de dívidas no Senado e temem ficar sem acesso ao crédito rural para financiar a próxima safra. O receio atinge em cheio regiões produtoras como a Costa Doce, onde o arroz e a soja sustentam a economia de dezenas de municípios.",
        "ganchos_3": [
            "Produtores temem que renegociação de dívidas não avance no Senado",
            "Risco é ficar sem crédito para a próxima safra",
            "Estiagens e enchentes agravaram o endividamento do campo"
        ],
        "angulo_editorial": "Economia do agro e crédito rural — tema central para a audiência rural da SulTV, com gancho regional forte (arroz e soja na Costa Doce). Enquadramento econômico/setorial, sem viés partidário, sem citar veículos.",
        "fontes_complementares_sugeridas": ["entidades do agronegócio gaúcho", "Farsul", "cooperativas de crédito rural"],
        "lead_materia_longa": "Produtores rurais do Rio Grande do Sul vivem a expectativa pela votação da renegociação de dívidas no Senado e temem ficar sem acesso ao crédito rural para financiar a próxima safra.",
        "post_instagram": {
            "caption": "O campo gaúcho não dorme tranquilo. Produtores do RS aguardam a votação da renegociação de dívidas no Senado e temem ficar sem crédito rural para a próxima safra. O endividamento se agravou com estiagens e enchentes, e o calendário agrícola não espera: decisões sobre insumos e financiamento precisam ser tomadas já. Um tema que mexe com toda a Costa Doce.",
            "hashtags": ["#Agro", "#CréditoRural", "#RioGrandeDoSul", "#Safra", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tensão no campo gaúcho.",
            "desenvolvimento_45s": "Produtores rurais do Rio Grande do Sul vivem a expectativa pela votação da renegociação de dívidas no Senado. O principal receio do setor é ficar sem acesso ao crédito rural para financiar a próxima safra, um risco que atinge em cheio regiões produtoras como a Costa Doce. O endividamento do campo se agravou nos últimos anos com estiagens severas e enchentes históricas. Enquanto a votação não acontece, cresce a apreensão, porque o calendário agrícola não espera.",
            "fechamento_8s": "Decisão do Senado é aguardada.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Dívidas rurais no Senado",
        "briefing_visual": {
            "descricao_pt": "Lavoura de soja ou arroz no Rio Grande do Sul com céu aberto, vista ampla, sem pessoas",
            "query_en": ["soybean field wide brazil", "rice paddy rio grande do sul", "farmland horizon south brazil"],
            "evitar": ["pessoas identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Wide shot of a soybean field in Rio Grande do Sul under an open sky, vast farmland to the horizon, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Economia do agro e crédito rural — tema central para a audiência, com gancho regional forte (arroz/soja na Costa Doce); reescrito sem citar veículo"
    },

    # #22 RS — apreensão de alimentos impróprios / MP-RS — PUBLICAR materia_longa
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": {
        "titulo_sultv": "Fiscalização apreende cinco toneladas de alimentos impróprios em mercados gaúchos",
        "chamada_faixa": "Fiscalizacao apreende 5 toneladas de alimentos",
        "subtitulo": "Força-tarefa recolheu produtos estragados em três estabelecimentos; um deles foi interditado e o responsável, preso. Entre os itens, vinhos vencidos há nove anos.",
        "lead": "Uma força-tarefa de fiscalização apreendeu cerca de cinco toneladas de produtos impróprios para consumo em três mercados gaúchos. Entre os itens recolhidos estavam vinhos vencidos havia nove anos. Um dos estabelecimentos foi interditado totalmente e o responsável, preso, em uma das piores situações sanitárias já registradas pelas equipes.",
        "ganchos_3": [
            "Cinco toneladas de alimentos impróprios apreendidas em mercados gaúchos",
            "Vinhos vencidos há nove anos estavam à venda",
            "Estabelecimento é interditado e responsável é preso"
        ],
        "angulo_editorial": "Defesa do consumidor e segurança alimentar no RS — ação concreta de fiscalização com fonte primária institucional (Ministério Público), sem identificação nominal de réu. Pauta de serviço e alerta ao consumidor.",
        "fontes_complementares_sugeridas": ["Ministério Público do RS", "Vigilância Sanitária", "Procon"],
        "lead_materia_longa": "Uma força-tarefa de fiscalização apreendeu cerca de cinco toneladas de produtos impróprios para consumo em três mercados gaúchos, entre eles vinhos vencidos havia nove anos.",
        "post_instagram": {
            "caption": "Atenção, consumidor. Uma força-tarefa de fiscalização apreendeu cerca de cinco toneladas de produtos impróprios para consumo em três mercados gaúchos. Entre os itens, vinhos vencidos havia nove anos. Um dos estabelecimentos foi interditado e o responsável, preso. Confira sempre a validade e a procedência do que você compra.",
            "hashtags": ["#DefesaDoConsumidor", "#SegurançaAlimentar", "#RioGrandeDoSul", "#Fiscalização", "#Saúde", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Cinco toneladas fora das prateleiras.",
            "desenvolvimento_45s": "Uma força-tarefa de fiscalização apreendeu cerca de cinco toneladas de produtos impróprios para consumo em três mercados gaúchos. Entre os itens recolhidos estavam vinhos vencidos havia nove anos. A situação foi descrita como uma das piores já vistas pelas equipes: um dos estabelecimentos foi interditado totalmente e o responsável acabou preso. O caso reforça a importância de o consumidor sempre conferir a validade e a procedência dos produtos.",
            "fechamento_8s": "Fique atento ao que compra.",
            "cta_5s": "Detalhes no SulTV.",
            "trilha_sugerida": "instrumental tenso leve"
        },
        "tag_thumbnail": "Apreensão de alimentos vencidos",
        "briefing_visual": {
            "descricao_pt": "Prateleira de mercado com produtos diversos, ou caixas de produtos apreendidos empilhadas, sem pessoas identificáveis e sem marcas legíveis",
            "query_en": ["supermarket shelf inspection", "expired food products seized", "food safety inspection store"],
            "evitar": ["rostos identificáveis", "marcas comerciais legíveis", "texto", "logos"],
            "prompt_ia": "Stacked boxes of seized grocery products in a store storage area during a food safety inspection, no identifiable people, no readable brand labels, daylight, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Defesa do consumidor com fonte primária institucional (MP-RS), sem réu identificado nominalmente; pauta de serviço e alerta"
    },

    # #23 RS — 630kg alimentos (mesma operação que #22) — REBAIXAR (duplicata)
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": _skip(
        "REBAIXAR",
        "Mesma operação de fiscalização do item 8c10... (apreensão de alimentos impróprios) — duplicata de ângulo; mantida a versão principal"
    ),

    # #24 Santa Maria — UFSM Rede HU+ — REBAIXAR (fora do núcleo, formato post)
    "014b0c7e7ebe83a7e9d2818d435714326ff6390e": _skip(
        "REBAIXAR",
        "Pauta de Santa Maria (fora das cidades-núcleo/Costa Doce), score 6, formato post; baixa prioridade no dia"
    ),

    # #25 Santa Maria — Moodle indisponível — BLOQUEAR (procedural)
    "52a34cdaeffd6c322e99946d7c0ec9b186f6071c": _skip(
        "BLOQUEAR",
        "Aviso de manutenção de sistema (Moodle UFSM) — comunicado procedural, não é matéria"
    ),

    # #26 Venâncio Aires — crochê — REBAIXAR (cidade distante, soft feature)
    "4927b0d6923c68a64c924a70207daa5c238e3884": _skip(
        "REBAIXAR",
        "Feature leve de cidade distante das áreas-núcleo (Venâncio Aires); baixo apelo regional para a audiência da Costa Doce"
    ),

    # #27 Venâncio Aires — Copa Serrana (esporte região distante) — BLOQUEAR
    "6cc550d6e5e50aefc7ec2b64a52497fbf495843d": _skip(
        "BLOQUEAR",
        "Esporte amador de região distante (Venâncio Aires) — guardrail de esporte de região distante"
    ),

    # #28 Bento Gonçalves — Luciano Hang escala 5x2 — BLOQUEAR (política/polêmica + distante)
    "fd4e1e2da7efa5d63c701abcb6ccb64107c18b8c": _skip(
        "BLOQUEAR",
        "Tema político-trabalhista polêmico (escala 5x2) com figura controversa e cidade distante (Bento Gonçalves) — guardrail"
    ),

    # #29 Bento Gonçalves — TacchiMed sorteio ExpoBento — REBAIXAR (promocional, distante)
    "afe430799de79547d2d9b7086008075f10225dbc": _skip(
        "REBAIXAR",
        "Conteúdo promocional/comercial de cidade distante (Bento Gonçalves); sem interesse jornalístico regional"
    ),
}


MATERIAS = {
    # #0 Murilo Cardoso — jiu-jitsu
    "1fb11c1f31a01fb5ce1038c92ebe74fa30835b80": """### Título ###
Atleta de Camaquã conquista título inédito no Mundial de Jiu-Jitsu

### Artigo ###
O atleta camaquense Murilo Cardoso conquistou um título inédito no Mundial de Jiu-Jitsu na faixa azul, levando o nome de Camaquã ao pódio internacional do esporte. A conquista coroa anos de dedicação aos tatames e representa um marco para a cidade da Costa Doce, que vê um de seus filhos brilhar em uma das competições mais disputadas da modalidade. Depois da vitória, o próprio atleta fez questão de destacar a importância do apoio que sempre recebeu da comunidade camaquense, dos treinadores e da família, que acompanharam de perto cada etapa da sua trajetória. O jiu-jitsu, esporte que exige técnica, disciplina e preparo físico e mental, tem formado cada vez mais atletas no interior do Rio Grande do Sul, e resultados como esse ajudam a inspirar novas gerações a buscar o esporte como caminho de desenvolvimento pessoal. A faixa azul é uma das graduações intermediárias da modalidade e reúne competidores de alto nível em torneios internacionais, o que torna o título ainda mais expressivo. Para Camaquã, a conquista reforça o potencial dos atletas locais e a importância de iniciativas que estimulem a prática esportiva entre crianças e jovens. O resultado entra para a história recente do esporte na cidade e serve de exemplo de que, com apoio e perseverança, é possível levar o nome da Costa Doce para o mundo.

### Legenda sugerida ###
Murilo Cardoso conquista título inédito no Mundial de Jiu-Jitsu na faixa azul e leva Camaquã ao pódio internacional.

### Palavras-chave ###
Camaquã, jiu-jitsu, mundial, faixa azul, esporte, Costa Doce, atleta, Murilo Cardoso
""",

    # #1 Camaquã — clima
    "aec2e9473018e7bb5e535fe6c05fa1c0adf6f243": """### Título ###
Chuva forte abre a semana em Camaquã, com melhora do tempo até quarta

### Artigo ###
A semana começa com chuva forte em Camaquã e na Costa Doce, exigindo atenção de moradores e produtores rurais. A segunda-feira deve concentrar o maior volume de precipitação, com potencial para acúmulo de água em áreas mais baixas e reflexos no trânsito e na rotina das cidades da região. A partir de terça-feira, a tendência é de melhora gradual das condições do tempo, e o sol volta a aparecer entre nuvens já na quarta-feira, abrindo uma janela de tempo mais firme. A variação é típica do período e reforça a importância de acompanhar as atualizações da previsão ao longo dos dias. Para o produtor rural, o cenário é especialmente relevante: o volume de chuva no início da semana influencia o estado do solo e o planejamento de atividades no campo, enquanto a melhora prevista para o meio da semana cria oportunidade para tarefas que dependem de tempo seco. Nas áreas urbanas, a recomendação é redobrar os cuidados no deslocamento durante os períodos de chuva mais intensa, evitando pontos de alagamento e dirigindo com cautela. A combinação de chuva no começo e melhora gradual ao longo dos dias permite que moradores e trabalhadores organizem a rotina de acordo com a janela de tempo firme que se aproxima na Costa Doce.

### Legenda sugerida ###
Segunda-feira concentra o maior volume de chuva em Camaquã; tempo melhora gradualmente até quarta-feira.

### Palavras-chave ###
Camaquã, previsão do tempo, chuva, clima, Costa Doce, meteorologia, semana
""",

    # #2 Fiergs robótica
    "71d8e4c166749fecf87911b126851418544f1bfb": """### Título ###
Robótica chega às escolas públicas do RS com formação para alunos e professores

### Artigo ###
Um novo projeto de formação em robótica vai levar a tecnologia às escolas municipais do Rio Grande do Sul, capacitando tanto os alunos quanto os professores da rede pública. A iniciativa tem como objetivo aproximar os estudantes do pensamento computacional, da lógica de programação e da resolução de problemas desde os primeiros anos escolares, preparando a próxima geração de gaúchos para um mercado de trabalho cada vez mais tecnológico. A proposta combina a entrega de materiais e equipamentos com a capacitação dos docentes, peça-chave para que a robótica seja incorporada de forma consistente ao dia a dia das escolas. Ao formar os professores, o projeto garante que o conhecimento permaneça na rede e alcance um número maior de turmas ao longo do tempo. A robótica educacional tem se mostrado uma ferramenta eficiente para despertar o interesse dos estudantes por ciências, matemática e engenharia, além de estimular habilidades como trabalho em equipe, criatividade e autonomia. Para os municípios do interior, levar essa formação às escolas públicas representa um passo importante na redução das desigualdades de acesso à tecnologia, oferecendo a crianças e jovens da Costa Doce e de todo o estado as mesmas oportunidades de aprendizado disponíveis nos grandes centros. A expectativa é que a iniciativa contribua para modernizar a educação pública gaúcha e abrir novos horizontes profissionais para os estudantes.

### Legenda sugerida ###
Projeto leva robótica às escolas municipais do RS e capacita professores para modernizar a educação pública.

### Palavras-chave ###
robótica, educação, escolas públicas, Rio Grande do Sul, inovação, tecnologia, formação, professores
""",

    # #11 Barra do Ribeiro — fogos
    "6d583901d0b2623e718e91c071da59f2069c1522": """### Título ###
Barra do Ribeiro proíbe fogos com estampido por lei municipal

### Artigo ###
Barra do Ribeiro passou a proibir o uso de fogos de artifício com estampido em todo o município, por força da Lei Municipal nº 2850/2025. A medida acompanha uma tendência que cresce nas cidades gaúchas e tem como principal motivação a proteção do bem-estar animal e das pessoas mais sensíveis a ruídos intensos. O barulho dos fogos tradicionais é uma das maiores causas de sofrimento para animais domésticos e silvestres, que possuem audição muito mais sensível que a humana. Cães, gatos, cavalos e aves entram em pânico diante das explosões, podendo se ferir em tentativas de fuga. A restrição também beneficia pessoas com transtorno do espectro autista, idosos, bebês e indivíduos com sensibilidade a ruídos, para quem o estrondo dos fogos pode representar grande desconforto. Com a nova lei, ficam permitidos apenas os fogos sem estampido, que produzem efeitos visuais sem o barulho característico das explosões. Dessa forma, o município busca um equilíbrio entre a tradição das celebrações festivas e o respeito ao bem-estar coletivo. Iniciativas semelhantes já foram adotadas por diversas cidades do Rio Grande do Sul e do país, em um movimento que reconhece a importância de comemorar sem causar sofrimento. A medida vale para todo o território de Barra do Ribeiro e reforça o papel da legislação municipal na construção de uma convivência mais harmoniosa entre moradores, animais e meio ambiente na Costa Doce.

### Legenda sugerida ###
Lei Municipal nº 2850/2025 proíbe fogos com estampido em Barra do Ribeiro para proteger animais e pessoas sensíveis a ruídos.

### Palavras-chave ###
Barra do Ribeiro, fogos de artifício, estampido, lei municipal, bem-estar animal, fogos silenciosos, Costa Doce
""",

    # #12 Cristal — calçamento
    "5eac1d16fe3f0e1a1ab6ddd6d648bbee9e86c383": """### Título ###
Rua Camaquã, em Cristal, recebe preparação para obras de calçamento

### Artigo ###
A Rua Camaquã, em Cristal, começou a receber os serviços de preparação que antecedem as obras de calçamento, marcando o início de mais uma etapa de pavimentação na cidade da Costa Doce. Os trabalhos incluem a terraplanagem e o preparo do leito da via, etapas fundamentais para garantir a qualidade e a durabilidade do calçamento que será executado na sequência. A intervenção, conduzida pela prefeitura, tem impacto direto na vida dos moradores da região. Ruas pavimentadas reduzem a poeira nos períodos de tempo seco e eliminam a lama e os atoleiros nos dias de chuva, melhorando o acesso às residências, o escoamento da produção e o deslocamento de moradores, estudantes e trabalhadores. Além do ganho em mobilidade, a pavimentação valoriza os imóveis, facilita a passagem de veículos de emergência e contribui para o desenvolvimento dos bairros atendidos. Obras de calçamento estão entre as demandas mais frequentes da população nas cidades do interior, e cada nova via pavimentada representa uma melhoria concreta na qualidade de vida da comunidade. A preparação da Rua Camaquã sinaliza a continuidade dos investimentos em infraestrutura urbana em Cristal, e a expectativa dos moradores é de que a obra avance dentro do cronograma previsto, entregando uma via em melhores condições de tráfego e segurança.

### Legenda sugerida ###
Rua Camaquã, em Cristal, recebe preparação do leito para as obras de calçamento que vão melhorar a mobilidade local.

### Palavras-chave ###
Cristal, Rua Camaquã, calçamento, pavimentação, obras, infraestrutura urbana, Costa Doce, mobilidade
""",

    # #16 Pelotas — morango
    "5243be736e2649528d6bc837fd8bbde97e1353d1": """### Título ###
Produtores de morango de Pelotas debatem criação de associação

### Artigo ###
Cerca de 30 produtores de morango de Pelotas se reuniram para discutir a criação de uma associação que represente e fortaleça o setor na região. O encontro, promovido com o apoio da Emater/RS-Ascar, debateu os benefícios da organização coletiva e os caminhos para estruturar uma entidade que dê mais força à categoria. Entre as vantagens apontadas durante a reunião estão os ganhos na comercialização da produção, o acesso facilitado a políticas públicas e o fortalecimento da representatividade dos produtores diante do poder público e do mercado. Quando organizados em associação, os produtores conseguem negociar melhores condições de venda, planejar a oferta de forma mais eficiente e acessar programas de apoio que muitas vezes exigem a formalização coletiva como requisito. A fruticultura familiar tem papel relevante na economia da região de Pelotas, e o morango é uma das culturas que mais agregam valor à pequena propriedade, gerando renda e ocupando mão de obra ao longo de boa parte do ano. O apoio técnico da Emater/RS-Ascar tem sido fundamental para orientar os produtores tanto nas questões de manejo e produção quanto na organização do setor. A criação de uma associação é vista como um passo importante para profissionalizar a atividade, agregar valor ao produto e dar mais sustentabilidade ao negócio. A expectativa é de que as conversas avancem e resultem na estruturação de uma entidade que represente os interesses dos morangueiros da Costa Doce ampliada.

### Legenda sugerida ###
Cerca de 30 produtores de morango de Pelotas debatem, com apoio da Emater/RS-Ascar, a criação de uma associação para fortalecer o setor.

### Palavras-chave ###
Pelotas, morango, associação, Emater, fruticultura, agro, Costa Doce, produtores rurais
""",

    # #20 neve / El Niño
    "01e4af8f22701aee0014a55e168747935cd1d8cd": """### Título ###
Um ano após a neve, El Niño deve dificultar nevadas no inverno de 2026

### Artigo ###
Há um ano, em maio de 2025, o Sul do Brasil registrava neve com acumulação no Rio Grande do Sul e em Santa Catarina, um fenômeno incomum para aquele mês e que rendeu imagens marcantes nas áreas mais altas da região. Para o inverno de 2026, no entanto, o cenário tende a ser diferente: as análises meteorológicas indicam que a presença do El Niño deve dificultar a ocorrência de novas nevadas no Sul do país. O El Niño é caracterizado pelo aquecimento anormal das águas do Oceano Pacífico Equatorial e altera os padrões de circulação atmosférica em todo o planeta. No Sul do Brasil, seus invernos costumam ser mais úmidos, com chuvas acima da média, e com menor frequência de massas de ar polar muito intensas. É justamente a combinação de frio extremo com umidade em níveis adequados que permite a formação de neve, e essa combinação tende a ser mais rara sob a influência do fenômeno. Isso não significa que o frio estará ausente: episódios de temperaturas baixas, geadas e até eventos isolados de neve em pontos altos da Serra não ficam descartados. Mas as condições de grande escala jogam contra a repetição do espetáculo branco de 2025. Para o produtor rural da Costa Doce e de todo o estado, o sinal mais relevante do El Niño costuma ser o regime de chuvas, que influencia diretamente o planejamento da safra de inverno e a preparação para o plantio de primavera. O acompanhamento das previsões atualizadas ao longo da estação é recomendado para quem depende do clima no campo.

### Legenda sugerida ###
Neve de maio de 2025 completa um ano; para 2026, o El Niño tende a dificultar novas nevadas no Sul.

### Palavras-chave ###
neve, El Niño, inverno 2026, Rio Grande do Sul, clima, meteorologia, frio, Sul do Brasil, safra
""",

    # #21 renegociação de dívidas
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": """### Título ###
Produtores do RS temem que renegociação de dívidas rurais trave no Senado

### Artigo ###
Produtores rurais do Rio Grande do Sul vivem a expectativa pela votação da renegociação de dívidas no Senado e temem as consequências caso a proposta não seja aprovada. O principal receio do setor é ficar sem acesso ao crédito rural para o financiamento da próxima safra, um risco que atinge em cheio regiões produtoras como a Costa Doce, onde o arroz e a soja sustentam a economia de dezenas de municípios. O endividamento do campo gaúcho se agravou nos últimos anos com a sequência de eventos climáticos extremos: estiagens severas que quebraram safras consecutivas e, na sequência, as enchentes históricas que atingiram o estado. Sem conseguir honrar os compromissos das safras frustradas, muitos produtores acumularam parcelas e perderam capacidade de tomar novos financiamentos, entrando em um ciclo que compromete o custeio do próximo plantio. A renegociação em discussão é vista pelas entidades do setor como condição para restabelecer a capacidade de pagamento e manter o produtor na atividade. Enquanto a votação não acontece, cresce a apreensão no campo, já que o calendário agrícola não espera: as decisões sobre compra de insumos e financiamento da safra de verão precisam ser tomadas nos próximos meses. Lideranças do agronegócio gaúcho têm intensificado a interlocução com a bancada do estado em Brasília para dar celeridade à tramitação. O tema deve seguir no centro do debate econômico do agro nas próximas semanas, e os desdobramentos serão decisivos para o planejamento da safra 2026/2027 no Rio Grande do Sul.

### Legenda sugerida ###
Campo gaúcho teme ficar sem crédito para a próxima safra caso a renegociação de dívidas não avance no Senado.

### Palavras-chave ###
renegociação de dívidas, crédito rural, Senado, Rio Grande do Sul, agro, safra, arroz, soja, endividamento rural
""",

    # #22 apreensão de alimentos
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": """### Título ###
Fiscalização apreende cinco toneladas de alimentos impróprios em mercados gaúchos

### Artigo ###
Uma força-tarefa de fiscalização apreendeu cerca de cinco toneladas de produtos impróprios para consumo em três mercados gaúchos, em uma das piores situações sanitárias já registradas pelas equipes. Entre os itens recolhidos estavam vinhos vencidos havia nove anos, além de outros alimentos fora do prazo de validade ou armazenados em condições inadequadas. Um dos estabelecimentos foi interditado totalmente e o responsável acabou preso, diante da gravidade das irregularidades encontradas. As ações desse tipo são conduzidas com base em denúncias e em rotinas de fiscalização que cruzam informações sobre validade, procedência e condições de armazenamento dos produtos expostos à venda. A apreensão e a destruição de mercadorias impróprias visam proteger a saúde dos consumidores, evitando que alimentos estragados ou vencidos cheguem à mesa das famílias. O caso reforça a importância de o consumidor adotar alguns cuidados básicos no momento da compra: conferir sempre a data de validade nas embalagens, observar o estado de conservação dos produtos, desconfiar de preços muito abaixo do mercado e verificar as condições de higiene e refrigeração do estabelecimento. Qualquer irregularidade pode ser denunciada aos órgãos de defesa do consumidor e à vigilância sanitária, que têm o papel de fiscalizar e autuar comércios que descumprem as normas. A vigilância constante, tanto das autoridades quanto dos próprios consumidores, é a principal ferramenta para garantir a segurança alimentar e coibir práticas que colocam a saúde pública em risco.

### Legenda sugerida ###
Força-tarefa apreende cinco toneladas de alimentos impróprios em três mercados gaúchos; estabelecimento é interditado e responsável, preso.

### Palavras-chave ###
fiscalização, segurança alimentar, defesa do consumidor, Rio Grande do Sul, alimentos vencidos, vigilância sanitária, apreensão
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
            print(f"[angular] sem angulação para {h} — bloqueando")
            angul = _skip("BLOQUEAR", "Sem angulação configurada — descartado pelo guardrail")
            angul["titulo_sultv"] = (item.get("titulo") or "")[:100]
        else:
            angul = PAUTA_ANGULADA[h]

        # Quota: máx 10 publicações/dia (regra 14)
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
    print("[angular] decisões:", Counter(p["decisao_final"] for p in pauta))
    print("[angular] PUBLICAR:", pub_count)

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
                print(f"[angular] AVISO: {p['id_hash']} é PUBLICAR/materia_longa mas sem texto em MATERIAS")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
