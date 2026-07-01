#!/usr/bin/env python3
"""angular_2026-06-13.py — angulação editorial + redação (cowork-faz-tudo).

Decisões do dia (Claude na sessão):
- 10 PUBLICAR (quota máx 10) — 7 materia_longa + 3 nota_curta.
- Demais aprovados caem em BLOQUEAR (default) — cabeçalhos de seção, editais
  procedurais, política partidária, pauta nacional/internacional sem âncora
  Sul-RS, e item com temática de menores/abuso (guardrail).
Regra 12 aplicada: nenhum texto menciona veículo/portal/rádio/jornal.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOJE = datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _skip(decisao: str, motivo: str) -> dict:
    return {
        "titulo_sultv": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "", "decisao_final": decisao, "decisao_motivo": motivo,
    }


PAUTA_ANGULADA = {
    # 1. Arambaré — vacina da gripe liberada para toda a população — materia_longa
    "394b624e90eb180abfce5ed085d50699b0cba0cf": {
        "titulo_sultv": "Arambaré libera vacina da gripe para toda a população a partir de 15 de junho",
        "chamada_faixa": "Arambaré libera vacina da gripe a todos",
        "subtitulo": "A partir de segunda-feira (15), a dose contra a gripe estará disponível para moradores acima dos 6 meses de idade.",
        "lead": "A partir desta segunda-feira (15), a vacina contra a gripe estará liberada para toda a população de Arambaré a partir dos 6 meses de idade. A ampliação atende moradores que estavam fora dos grupos prioritários e reforça a proteção da comunidade no período mais frio do ano na Costa Doce.",
        "ganchos_3": [
            "Vacina da gripe liberada para toda a população de Arambaré",
            "Doses disponíveis a partir de 15 de junho para maiores de 6 meses",
            "Ampliação chega no auge do período frio na Costa Doce"
        ],
        "angulo_editorial": "Saúde pública de utilidade imediata em cidade-núcleo SulTV — ampliação concreta de campanha de vacinação, sem teor médico-prescritivo, com data e público bem definidos.",
        "fontes_complementares_sugeridas": ["Prefeitura de Arambaré", "Secretaria Municipal de Saúde de Arambaré"],
        "lead_materia_longa": "A partir desta segunda-feira (15), a vacina contra a gripe estará liberada para toda a população de Arambaré a partir dos 6 meses de idade.",
        "post_instagram": {
            "caption": "A vacina contra a gripe está liberada para toda a população de Arambaré a partir desta segunda-feira (15), para quem tem 6 meses de idade ou mais. A ampliação chega no auge do frio, quando os casos de doenças respiratórias aumentam. Vale procurar a unidade de saúde mais próxima e manter a carteirinha em dia.",
            "hashtags": ["#Arambaré", "#VacinaDaGripe", "#Saúde", "#CostaDoce", "#Vacinação", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Gripe: vacina liberada em Arambaré.",
            "desenvolvimento_45s": "A partir de segunda-feira, 15 de junho, a vacina contra a gripe está liberada para toda a população de Arambaré a partir dos 6 meses de idade. A ampliação chega no período mais frio do ano, quando aumentam os casos de doenças respiratórias. A orientação é procurar a unidade de saúde mais próxima levando documento e carteira de vacinação.",
            "fechamento_8s": "Proteção ampliada para toda a cidade.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Vacina da gripe",
        "briefing_visual": {
            "descricao_pt": "Aplicação de vacina no braço em unidade de saúde, sem rosto identificável, ambiente claro",
            "query_en": ["flu vaccine arm clinic", "vaccination health center", "nurse giving vaccine"],
            "evitar": ["rosto identificável", "marcas", "texto", "logos"],
            "prompt_ia": "Close-up of a flu vaccine being administered in an arm at a bright health clinic in southern Brazil, face not visible, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço de saúde concreto em cidade-núcleo, data e público definidos, sem conteúdo médico-prescritivo"
    },

    # 2. São Lourenço do Sul — Defesa Civil monitora chuvas (84mm) — materia_longa
    "e20c1c924e3c8c691279f7b5e6788daf274bbf9f": {
        "titulo_sultv": "São Lourenço do Sul monitora chuvas após 84 mm registrados no interior",
        "chamada_faixa": "São Lourenço monitora chuvas no interior",
        "subtitulo": "Defesa Civil acompanha as condições hidrometeorológicas; localidade do interior registrou 84 mm em 12 horas.",
        "lead": "A Defesa Civil de São Lourenço do Sul segue acompanhando as condições hidrometeorológicas do município, em especial nas regiões do interior, onde foram registrados 84 milímetros de chuva em apenas 12 horas. O monitoramento integra as ações preventivas diante da previsão de instabilidade na Costa Doce.",
        "ganchos_3": [
            "84 mm de chuva em 12 horas no interior de São Lourenço do Sul",
            "Defesa Civil reforça monitoramento hidrometeorológico",
            "Ações preventivas concentradas nas regiões do interior"
        ],
        "angulo_editorial": "Clima e prevenção em cidade-núcleo SulTV — dado quantitativo oficial, utilidade direta para o produtor rural e moradores do interior, tom institucional de serviço.",
        "fontes_complementares_sugeridas": ["Defesa Civil de São Lourenço do Sul", "Prefeitura de São Lourenço do Sul"],
        "lead_materia_longa": "A Defesa Civil de São Lourenço do Sul segue acompanhando as condições hidrometeorológicas do município, em especial nas regiões do interior, onde foram registrados 84 milímetros de chuva em apenas 12 horas.",
        "post_instagram": {
            "caption": "A Defesa Civil de São Lourenço do Sul está de olho nas chuvas: a localidade do interior conhecida como Passo do registrou 84 mm em apenas 12 horas. As equipes seguem monitorando rios e estradas, com atenção especial às regiões do interior. Moradores devem acompanhar os comunicados oficiais e evitar áreas alagáveis.",
            "hashtags": ["#SãoLourençoDoSul", "#DefesaCivil", "#Chuva", "#CostaDoce", "#Prevenção", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Chuva forte no interior.",
            "desenvolvimento_45s": "A Defesa Civil de São Lourenço do Sul segue monitorando as condições do tempo após o registro de 84 milímetros de chuva em 12 horas em uma localidade do interior. As equipes acompanham o nível de rios e a situação das estradas, com atenção redobrada às áreas rurais. A orientação é acompanhar os comunicados oficiais e evitar áreas alagáveis.",
            "fechamento_8s": "Monitoramento segue ativo.",
            "cta_5s": "Atualizações no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Chuvas na Costa Doce",
        "briefing_visual": {
            "descricao_pt": "Estrada rural molhada e céu nublado carregado no Sul do RS, campo alagado ao fundo, sem pessoas",
            "query_en": ["flooded rural road rain", "heavy rain countryside brazil", "overcast sky wet field"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto", "logos"],
            "prompt_ia": "Wet rural road under a heavy overcast sky with a flooded field in the background in southern Brazil, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima/prevenção com dado oficial quantitativo em cidade-núcleo; alta utilidade regional"
    },

    # 3. Cristal — sorteio Programa Milho 100% — materia_longa
    "ed8d120b785029e0cb62e3da9a91f9a966a30562": {
        "titulo_sultv": "Cristal sorteia beneficiários do Programa Milho 100% após alta procura",
        "chamada_faixa": "Cristal sorteia beneficiários do Milho 100%",
        "subtitulo": "Número de inscrições superou as sacas disponíveis; sorteio público foi adotado para garantir transparência na distribuição.",
        "lead": "A Prefeitura de Cristal realizou nesta sexta-feira (12) o sorteio dos beneficiários do Programa Milho 100%, na Costa Doce. A medida foi adotada porque o número de inscrições superou a quantidade de sacas disponíveis para o município, e o sorteio público foi a forma escolhida para garantir transparência na distribuição.",
        "ganchos_3": [
            "Cristal realiza sorteio do Programa Milho 100%",
            "Procura superou a quantidade de sacas disponíveis",
            "Sorteio público adotado para garantir transparência"
        ],
        "angulo_editorial": "Agro e política pública em cidade-núcleo SulTV — ação concreta de apoio ao pequeno produtor, com transparência na distribuição; fato datado e de interesse direto do campo.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria Municipal de Agricultura de Cristal"],
        "lead_materia_longa": "A Prefeitura de Cristal realizou nesta sexta-feira (12) o sorteio dos beneficiários do Programa Milho 100%, medida adotada após o número de inscrições superar a quantidade de sacas disponíveis para o município.",
        "post_instagram": {
            "caption": "Em Cristal, a procura pelo Programa Milho 100% foi tanta que o número de inscritos passou da quantidade de sacas disponíveis. Para garantir transparência, a distribuição foi definida por sorteio público nesta sexta-feira (12). O programa apoia diretamente o pequeno produtor da Costa Doce.",
            "hashtags": ["#Cristal", "#Agro", "#Milho100", "#ProdutorRural", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Milho 100% sorteado em Cristal.",
            "desenvolvimento_45s": "A Prefeitura de Cristal realizou o sorteio dos beneficiários do Programa Milho 100%. A procura pela iniciativa foi tão grande que o número de inscritos superou a quantidade de sacas disponíveis para o município. Para garantir transparência, a distribuição foi definida por sorteio público. O programa é mais um apoio ao pequeno produtor da região.",
            "fechamento_8s": "Distribuição transparente garantida.",
            "cta_5s": "Detalhes no SulTV.",
            "trilha_sugerida": "instrumental campeiro leve"
        },
        "tag_thumbnail": "Programa Milho 100%",
        "briefing_visual": {
            "descricao_pt": "Sacas de sementes de milho empilhadas em galpão rural no Sul do Brasil, sem pessoas identificáveis",
            "query_en": ["corn seed bags warehouse", "stacked grain sacks farm", "maize seeds agriculture"],
            "evitar": ["rosto identificável", "marcas", "texto", "logos"],
            "prompt_ia": "Stacked bags of corn seed in a rural warehouse in southern Brazil, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Política pública agro concreta e datada em cidade-núcleo, interesse direto do produtor"
    },

    # 4. Tapes — prefeito e Colônia Z-43 tratam de medidas preventivas — materia_longa
    "a3533cde66a8c4980dc360e776b8a90f9bd35335": {
        "titulo_sultv": "Tapes discute medidas preventivas com a Colônia de Pescadores Z-43",
        "chamada_faixa": "Tapes alinha prevenção com pescadores",
        "subtitulo": "Prefeitura e Colônia Z-43 trataram de ações diante do período de chuvas e da elevação dos níveis das águas.",
        "lead": "A Prefeitura de Tapes recebeu a representante da Colônia de Pescadores Z-43, Kelly Rigon, para alinhar medidas preventivas diante do período de chuvas e da possível elevação dos níveis das águas na Costa Doce. O encontro tratou de ações de proteção às comunidades pesqueiras ribeirinhas.",
        "ganchos_3": [
            "Tapes alinha prevenção com a Colônia de Pescadores Z-43",
            "Pauta foi o período de chuvas e a elevação das águas",
            "Comunidades pesqueiras ribeirinhas no foco das ações"
        ],
        "angulo_editorial": "Prevenção e comunidade tradicional em cidade-núcleo SulTV — articulação institucional concreta com a pesca artesanal, setor sensível às cheias da Lagoa dos Patos; tom de serviço.",
        "fontes_complementares_sugeridas": ["Prefeitura de Tapes", "Colônia de Pescadores Z-43", "Defesa Civil de Tapes"],
        "lead_materia_longa": "A Prefeitura de Tapes recebeu a representante da Colônia de Pescadores Z-43, Kelly Rigon, para alinhar medidas preventivas diante do período de chuvas e da possível elevação dos níveis das águas.",
        "post_instagram": {
            "caption": "Em Tapes, a Prefeitura e a Colônia de Pescadores Z-43 se reuniram para alinhar medidas preventivas diante do período de chuvas e da elevação das águas. As comunidades pesqueiras ribeirinhas estão entre as mais sensíveis às cheias da Lagoa dos Patos — e a prevenção começa pelo diálogo.",
            "hashtags": ["#Tapes", "#PescaArtesanal", "#Prevenção", "#LagoaDosPatos", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tapes pensa na prevenção.",
            "desenvolvimento_45s": "A Prefeitura de Tapes recebeu a representante da Colônia de Pescadores Z-43 para tratar de medidas preventivas diante do período de chuvas e da elevação dos níveis das águas. O diálogo foca a proteção das comunidades pesqueiras ribeirinhas, entre as mais sensíveis às cheias da Lagoa dos Patos. As ações devem ser detalhadas nas próximas semanas.",
            "fechamento_8s": "Prevenção pela conversa.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental calmo"
        },
        "tag_thumbnail": "Prevenção em Tapes",
        "briefing_visual": {
            "descricao_pt": "Barcos de pesca artesanal ancorados às margens da Lagoa dos Patos sob céu nublado, sem pessoas identificáveis",
            "query_en": ["small fishing boats lagoon", "artisanal fishing boats shore", "cloudy sky lake brazil"],
            "evitar": ["rosto identificável", "marcas", "texto", "logos"],
            "prompt_ia": "Artisanal fishing boats moored on the shore of a large lagoon under a cloudy sky in southern Brazil, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Prevenção concreta com comunidade tradicional em cidade-núcleo; sem guardrail"
    },

    # 5. Chuvisca — formação do 1º Grupo do Programa de Controle do Tabagismo — materia_longa
    "a22b25799503d48eeceab4081c50af0fec9b3527": {
        "titulo_sultv": "Chuvisca forma primeiro grupo do Programa de Controle do Tabagismo",
        "chamada_faixa": "Chuvisca forma grupo antitabagismo",
        "subtitulo": "Iniciativa da Secretaria de Saúde reúne moradores que querem parar de fumar, com acompanhamento em grupo.",
        "lead": "A Secretaria Municipal de Saúde de Chuvisca formou o primeiro grupo do Programa de Controle do Tabagismo, na Costa Doce. A iniciativa reúne moradores que desejam parar de fumar e oferece acompanhamento coletivo, voltado à promoção da saúde e à melhoria da qualidade de vida da população.",
        "ganchos_3": [
            "Chuvisca forma o 1º grupo do Programa de Controle do Tabagismo",
            "Iniciativa oferece acompanhamento coletivo para parar de fumar",
            "Foco na promoção da saúde da comunidade"
        ],
        "angulo_editorial": "Saúde pública comunitária em cidade-núcleo SulTV — programa de apoio coletivo, sem prescrição médica nem diagnóstico; pauta de serviço e cidadania.",
        "fontes_complementares_sugeridas": ["Prefeitura de Chuvisca", "Secretaria Municipal de Saúde de Chuvisca"],
        "lead_materia_longa": "A Secretaria Municipal de Saúde de Chuvisca formou o primeiro grupo do Programa de Controle do Tabagismo, iniciativa que reúne moradores que desejam parar de fumar e oferece acompanhamento coletivo.",
        "post_instagram": {
            "caption": "Chuvisca deu um passo importante na saúde: a Secretaria de Saúde formou o primeiro grupo do Programa de Controle do Tabagismo. A proposta é acompanhar, em grupo, quem quer parar de fumar — porque largar o cigarro fica mais fácil com apoio. Quem tem interesse pode procurar a unidade de saúde.",
            "hashtags": ["#Chuvisca", "#Saúde", "#Tabagismo", "#QualidadeDeVida", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Largar o cigarro com apoio.",
            "desenvolvimento_45s": "A Secretaria Municipal de Saúde de Chuvisca formou o primeiro grupo do Programa de Controle do Tabagismo. A iniciativa reúne moradores que querem parar de fumar e oferece acompanhamento coletivo, com foco na promoção da saúde. Quem tem interesse em participar pode procurar a unidade de saúde do município.",
            "fechamento_8s": "Saúde que se constrói em grupo.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental otimista leve"
        },
        "tag_thumbnail": "Controle do Tabagismo",
        "briefing_visual": {
            "descricao_pt": "Roda de pessoas em reunião comunitária em sala de unidade de saúde no Sul do Brasil, vista de longe, sem rostos identificáveis",
            "query_en": ["community health group meeting", "support group circle room", "health center workshop"],
            "evitar": ["rosto identificável", "cigarro em destaque", "marcas", "texto", "logos"],
            "prompt_ia": "A community support group meeting in a health center room in southern Brazil, seen from a distance, faces not identifiable, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Programa de saúde comunitária em cidade-núcleo; apoio coletivo, sem prescrição/diagnóstico"
    },

    # 6. Bagé — PC e BM prendem dois homens com 28 kg de maconha — materia_longa
    "80b4312fa130db698ac33a2c754a2101d278c735": {
        "titulo_sultv": "Operação na fronteira prende dois homens com mais de 28 kg de maconha em Bagé",
        "chamada_faixa": "28 kg de maconha apreendidos em Bagé",
        "subtitulo": "Ação conjunta da Polícia Civil e da Brigada Militar resultou em duas prisões em flagrante por tráfico de drogas.",
        "lead": "Uma ação conjunta da Polícia Civil e da Brigada Militar prendeu em flagrante dois homens com mais de 28 quilos de maconha em Bagé, na fronteira do Rio Grande do Sul. A operação integra o trabalho de enfrentamento ao crime organizado na região de fronteira.",
        "ganchos_3": [
            "Mais de 28 kg de maconha apreendidos em Bagé",
            "Dois homens presos em flagrante por tráfico",
            "Ação conjunta de Polícia Civil e Brigada Militar na fronteira"
        ],
        "angulo_editorial": "Segurança pública na fronteira — fato concreto com números, ação policial integrada, sem vítima identificada; atribuição a fontes primárias institucionais.",
        "fontes_complementares_sugeridas": ["Polícia Civil RS", "Brigada Militar RS"],
        "lead_materia_longa": "Uma ação conjunta da Polícia Civil e da Brigada Militar prendeu em flagrante dois homens com mais de 28 quilos de maconha em Bagé, na fronteira do Rio Grande do Sul.",
        "post_instagram": {
            "caption": "Em Bagé, na fronteira, uma ação conjunta da Polícia Civil e da Brigada Militar prendeu dois homens em flagrante com mais de 28 quilos de maconha. A apreensão integra o trabalho de enfrentamento ao tráfico e ao crime organizado na região.",
            "hashtags": ["#Bagé", "#Segurança", "#Fronteira", "#PolíciaCivil", "#BrigadaMilitar", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Golpe no tráfico na fronteira.",
            "desenvolvimento_45s": "Uma ação conjunta da Polícia Civil e da Brigada Militar prendeu em flagrante dois homens com mais de 28 quilos de maconha em Bagé, na fronteira do Rio Grande do Sul. A operação integra o enfrentamento ao crime organizado na região de fronteira. Os presos e o material apreendido foram encaminhados às autoridades competentes.",
            "fechamento_8s": "Investigação segue em andamento.",
            "cta_5s": "Detalhes no SulTV.",
            "trilha_sugerida": "instrumental tenso leve"
        },
        "tag_thumbnail": "Apreensão em Bagé",
        "formato_sugerido": "materia_longa",
        "briefing_visual": {
            "descricao_pt": "Viatura policial com giroflex em estrada na fronteira do RS ao entardecer, sem pessoas identificáveis",
            "query_en": ["police car patrol road dusk", "police operation highway", "law enforcement vehicle brazil"],
            "evitar": ["rostos identificáveis", "presos", "drogas em close", "marcas", "texto", "logos"],
            "prompt_ia": "A police patrol car with light bar on a road near the border in southern Brazil at dusk, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Segurança pública com fato concreto e números; sem vítima identificada; fontes primárias"
    },

    # 7. Sertão Santana — Termo de Fomento com CTG Tio Raymundo — materia_longa
    "bde33368856dbdeb6aa6cd6c59085d2ea2c4960c": {
        "titulo_sultv": "Sertão Santana destina R$ 9,7 mil ao CTG Tio Raymundo para preservar a tradição",
        "chamada_faixa": "Sertão Santana apoia o CTG Tio Raymundo",
        "subtitulo": "Termo de Fomento prevê repasse para ações de preservação e valorização da cultura gaúcha.",
        "lead": "A Prefeitura de Sertão Santana assinou nesta sexta-feira o Termo de Fomento nº 009/2026 com o CTG Tio Raymundo, que prevê o repasse de R$ 9,7 mil à entidade. O recurso será destinado a ações de preservação e valorização da cultura tradicionalista gaúcha no município da Costa Doce.",
        "ganchos_3": [
            "Sertão Santana repassa R$ 9,7 mil ao CTG Tio Raymundo",
            "Termo de Fomento apoia a cultura tradicionalista gaúcha",
            "Recurso voltado à preservação das tradições do município"
        ],
        "angulo_editorial": "Cultura tradicionalista e fomento público — fato concreto com valor definido, valoriza a identidade gaúcha do interior; tom institucional positivo.",
        "fontes_complementares_sugeridas": ["Prefeitura de Sertão Santana", "CTG Tio Raymundo"],
        "lead_materia_longa": "A Prefeitura de Sertão Santana assinou nesta sexta-feira o Termo de Fomento nº 009/2026 com o CTG Tio Raymundo, que prevê o repasse de R$ 9,7 mil à entidade para ações de preservação e valorização da cultura tradicionalista gaúcha.",
        "post_instagram": {
            "caption": "Em Sertão Santana, a tradição ganha reforço: a Prefeitura assinou um Termo de Fomento com o CTG Tio Raymundo, com repasse de R$ 9,7 mil para ações de preservação e valorização da cultura gaúcha. Apoiar o CTG é investir na identidade e na história do interior.",
            "hashtags": ["#SertãoSantana", "#Tradição", "#CTG", "#CulturaGaúcha", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Tradição com apoio em Sertão Santana.",
            "desenvolvimento_45s": "A Prefeitura de Sertão Santana assinou o Termo de Fomento com o CTG Tio Raymundo, prevendo o repasse de R$ 9,7 mil à entidade. O recurso será usado em ações de preservação e valorização da cultura tradicionalista gaúcha. Apoiar o CTG é investir na identidade e na história das comunidades do interior.",
            "fechamento_8s": "Cultura gaúcha valorizada.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental gaúcho leve"
        },
        "tag_thumbnail": "Fomento ao CTG",
        "briefing_visual": {
            "descricao_pt": "Galpão de CTG com mangueira de couro e adereços tradicionalistas gaúchos, sem pessoas identificáveis",
            "query_en": ["gaucho traditional hall brazil", "south brazil rustic barn interior", "traditional rural decor"],
            "evitar": ["rosto identificável", "marcas", "texto", "logos"],
            "prompt_ia": "Interior of a traditional gaucho cultural center hall with rustic wood and regional decorations in southern Brazil, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fomento cultural concreto com valor definido; valoriza tradição regional"
    },

    # 8. Tapes — coleta gratuita de eletrônicos cancelada — nota_curta
    "545abfde72ea5629e9fe58fcd3b8ab6a3f9952dc": {
        "titulo_sultv": "Tapes cancela coleta gratuita de eletrônicos por causa do tempo",
        "chamada_faixa": "Tapes adia coleta de eletrônicos",
        "subtitulo": "Ação prevista para sexta-feira (12) foi cancelada devido às condições climáticas; nova data será divulgada.",
        "lead": "A coleta gratuita de eletrônicos que aconteceria nesta sexta-feira (12) em Tapes foi cancelada devido às condições climáticas adversas. Uma nova data será definida e divulgada à comunidade, mantendo o compromisso com o descarte correto desse tipo de resíduo.",
        "ganchos_3": [
            "Coleta gratuita de eletrônicos é cancelada em Tapes",
            "Motivo foi o tempo adverso desta sexta-feira (12)",
            "Nova data será divulgada à comunidade"
        ],
        "angulo_editorial": "Serviço urbano em cidade-núcleo SulTV — informação de utilidade imediata sobre mudança de agenda pública; nota curta objetiva.",
        "fontes_complementares_sugeridas": ["Prefeitura de Tapes"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Atenção, Tapes: a coleta gratuita de eletrônicos marcada para esta sexta-feira (12) foi cancelada por causa do tempo. Uma nova data será divulgada em breve. Quem separou aparelhos para descarte pode guardar até o reagendamento.",
            "hashtags": ["#Tapes", "#ColetaDeEletrônicos", "#Sustentabilidade", "#CostaDoce", "#Serviço", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Mudança de agenda em Tapes.",
            "desenvolvimento_45s": "A coleta gratuita de eletrônicos que aconteceria nesta sexta-feira em Tapes foi cancelada por causa das condições do tempo. Uma nova data será definida e divulgada à comunidade. Quem já separou aparelhos para o descarte correto pode guardá-los até o reagendamento.",
            "fechamento_8s": "Nova data em breve.",
            "cta_5s": "Fique de olho no SulTV.",
            "trilha_sugerida": "instrumental leve"
        },
        "tag_thumbnail": "Coleta de eletrônicos",
        "formato_sugerido": "nota_curta",
        "briefing_visual": {
            "descricao_pt": "Pilha de aparelhos eletrônicos antigos para descarte e reciclagem, sem marcas visíveis",
            "query_en": ["electronic waste recycling pile", "old electronics disposal", "e-waste collection"],
            "evitar": ["marcas", "logos", "texto", "rosto identificável"],
            "prompt_ia": "A pile of old electronic devices ready for recycling and proper disposal, no visible brands, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço urbano de utilidade imediata em cidade-núcleo"
    },

    # 9. RS — formação de ciclone extratropical no Sul — nota_curta
    "6b1af70ea7412b46c9581e1683136f67453e3665": {
        "titulo_sultv": "Ciclone extratropical se forma no Sul do Brasil e traz chuva ao Rio Grande do Sul",
        "chamada_faixa": "Ciclone forma-se no Sul do Brasil",
        "subtitulo": "Imagens de satélite registram a formação do sistema, que deixa o dia nublado e chuvoso em diversos pontos do RS.",
        "lead": "Imagens de satélite registraram nesta sexta-feira (12) a formação de um ciclone extratropical no Sul do Brasil. O sistema traz um dia de muitas nuvens e chuva em diversos pontos do Rio Grande do Sul, reforçando a atenção de moradores e produtores rurais às condições do tempo.",
        "ganchos_3": [
            "Ciclone extratropical se forma no Sul do Brasil",
            "Sistema traz nuvens e chuva a diversos pontos do RS",
            "Atenção redobrada para moradores e produtores rurais"
        ],
        "angulo_editorial": "Clima de impacto estadual com forte interesse rural — fato meteorológico do dia; atribuição apenas a 'imagens de satélite', sem citar plataforma.",
        "fontes_complementares_sugeridas": ["Instituto Nacional de Meteorologia (INMET)", "Defesa Civil RS"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Um ciclone extratropical se formou no Sul do Brasil nesta sexta-feira (12), segundo imagens de satélite. O sistema deixa o dia nublado e chuvoso em diversos pontos do Rio Grande do Sul. Moradores e produtores devem ficar atentos às atualizações e à possibilidade de chuva mais forte.",
            "hashtags": ["#RioGrandeDoSul", "#Ciclone", "#Clima", "#Chuva", "#Tempo", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Ciclone no radar.",
            "desenvolvimento_45s": "Imagens de satélite registraram a formação de um ciclone extratropical no Sul do Brasil. O sistema traz um dia de muitas nuvens e chuva em diversos pontos do Rio Grande do Sul. A orientação é acompanhar as atualizações do tempo e redobrar a atenção em áreas sujeitas a alagamentos e a ventos mais fortes.",
            "fechamento_8s": "Tempo segue instável.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Ciclone no Sul",
        "briefing_visual": {
            "descricao_pt": "Imagem de céu carregado com nuvens densas de tempestade sobre paisagem do Sul do Brasil, sem pessoas",
            "query_en": ["storm clouds dramatic sky", "extratropical cyclone satellite", "dark rain clouds landscape"],
            "evitar": ["marcas", "logos", "texto", "rosto identificável"],
            "prompt_ia": "Dramatic dark storm clouds over a southern Brazil landscape signaling an incoming cyclone, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Clima de impacto estadual e rural; fato do dia, atribuído a satélite sem citar plataforma"
    },

    # 10. Canguçu — abertas as encomendas de semente de batata — nota_curta
    "796c2834066f6048e6312d9168dab9139a7b4a6c": {
        "titulo_sultv": "Canguçu abre encomendas de sementes de batata para produtores",
        "chamada_faixa": "Canguçu abre pedidos de semente de batata",
        "subtitulo": "Secretaria de Agricultura recebe pedidos de oito variedades; iniciativa apoia a produção local.",
        "lead": "A Secretaria Municipal de Agricultura de Canguçu abriu as encomendas de sementes de batata para os produtores do município. Estão disponíveis oito variedades — Baronesa, Macaca, Asterix, Bel, Gaia, Potira, Ana e Ágata —, em iniciativa que apoia a produção local e o planejamento da safra.",
        "ganchos_3": [
            "Canguçu abre encomendas de sementes de batata",
            "Oito variedades disponíveis aos produtores",
            "Iniciativa apoia a produção local e o planejamento da safra"
        ],
        "angulo_editorial": "Agro de serviço — informação prática e datada para o produtor de batata da região; nota curta objetiva.",
        "fontes_complementares_sugeridas": ["Prefeitura de Canguçu", "Secretaria Municipal de Agricultura de Canguçu"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Produtor de Canguçu: já estão abertas as encomendas de sementes de batata na Secretaria de Agricultura. São oito variedades disponíveis — Baronesa, Macaca, Asterix, Bel, Gaia, Potira, Ana e Ágata. Vale procurar a secretaria para garantir o pedido e planejar a safra.",
            "hashtags": ["#Canguçu", "#Agro", "#Batata", "#ProdutorRural", "#Safra", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Semente de batata em Canguçu.",
            "desenvolvimento_45s": "A Secretaria Municipal de Agricultura de Canguçu abriu as encomendas de sementes de batata para os produtores. São oito variedades disponíveis: Baronesa, Macaca, Asterix, Bel, Gaia, Potira, Ana e Ágata. A orientação é procurar a secretaria para fazer o pedido e planejar a próxima safra.",
            "fechamento_8s": "Pedidos abertos.",
            "cta_5s": "Saiba mais no SulTV.",
            "trilha_sugerida": "instrumental campeiro leve"
        },
        "tag_thumbnail": "Semente de batata",
        "formato_sugerido": "nota_curta",
        "briefing_visual": {
            "descricao_pt": "Batatas-semente em caixas de madeira prontas para o plantio, ambiente rural, sem pessoas",
            "query_en": ["seed potatoes wooden crates", "potato planting agriculture", "potato tubers farm"],
            "evitar": ["marcas", "logos", "texto", "rosto identificável"],
            "prompt_ia": "Seed potatoes in wooden crates ready for planting in a rural setting in southern Brazil, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agro de serviço, informação prática e datada para o produtor"
    },
}


MATERIAS = {
    "394b624e90eb180abfce5ed085d50699b0cba0cf": """### Título ###
Arambaré libera vacina da gripe para toda a população a partir de 15 de junho

### Artigo ###
A partir desta segunda-feira, 15 de junho, a vacina contra a gripe estará liberada para toda a população de Arambaré a partir dos 6 meses de idade. A ampliação atende moradores que até então estavam fora dos grupos prioritários e chega no auge do período mais frio do ano na Costa Doce, justamente quando aumentam os casos de doenças respiratórias. A vacinação é apontada pelas equipes de saúde como a forma mais eficaz de reduzir as complicações causadas pelo vírus da gripe, especialmente entre crianças pequenas, idosos, gestantes e pessoas com doenças crônicas. Ao ampliar o acesso para toda a população, o município amplia também a chamada proteção coletiva: quanto mais gente vacinada, menor a circulação do vírus na comunidade, o que ajuda a proteger inclusive quem não pode se vacinar. A orientação é procurar a unidade de saúde mais próxima levando documento de identificação e a carteira de vacinação, para que o registro seja feito corretamente e o histórico de doses fique atualizado. A vacina da gripe é segura e atualizada a cada ano para acompanhar as cepas do vírus em circulação, e pode ser aplicada junto com outras vacinas do calendário. Em municípios menores, campanhas como essa têm impacto direto na rotina das famílias e na redução da procura por atendimento de urgência durante o inverno. A população pode buscar informações sobre horários e locais de atendimento diretamente nos canais oficiais da Prefeitura de Arambaré e da Secretaria Municipal de Saúde.

### Legenda sugerida ###
Arambaré libera a vacina da gripe para todos a partir de 15 de junho, para quem tem 6 meses ou mais.

### Palavras-chave ###
Arambaré, vacina da gripe, vacinação, saúde pública, inverno, doenças respiratórias, Costa Doce, Secretaria de Saúde
""",

    "e20c1c924e3c8c691279f7b5e6788daf274bbf9f": """### Título ###
São Lourenço do Sul monitora chuvas após 84 mm registrados no interior

### Artigo ###
A Defesa Civil de São Lourenço do Sul segue acompanhando as condições hidrometeorológicas do município, com atenção especial às regiões do interior, onde foram registrados 84 milímetros de chuva em apenas 12 horas. O volume expressivo, concentrado em um curto intervalo, acende o alerta para a elevação do nível de arroios e para a possibilidade de pontos de alagamento em estradas vicinais e áreas rurais. O monitoramento integra as ações preventivas adotadas diante da previsão de instabilidade no tempo sobre a Costa Doce, região historicamente sensível a episódios de chuva intensa por sua geografia de planícies e proximidade com a Lagoa dos Patos. As equipes acompanham o comportamento dos rios e o estado das vias, de modo a orientar rapidamente a população caso haja necessidade. Para os moradores do interior e para os produtores rurais, a recomendação é redobrar a atenção, evitar transitar por estradas alagadas ou pontes submersas, proteger animais e equipamentos em áreas baixas e manter contato com os canais oficiais para receber atualizações. Chuvas concentradas também exigem cuidado com a qualidade da água e com a integridade de açudes e barragens em propriedades rurais. A Defesa Civil reforça que o monitoramento é contínuo e que novas orientações podem ser emitidas conforme a evolução do tempo. Moradores podem acompanhar as informações atualizadas pelos canais oficiais da Prefeitura de São Lourenço do Sul e da Defesa Civil municipal.

### Legenda sugerida ###
Defesa Civil de São Lourenço do Sul monitora chuvas após 84 mm em 12 horas no interior do município.

### Palavras-chave ###
São Lourenço do Sul, Defesa Civil, chuvas, 84 mm, monitoramento, prevenção, Costa Doce, interior
""",

    "ed8d120b785029e0cb62e3da9a91f9a966a30562": """### Título ###
Cristal sorteia beneficiários do Programa Milho 100% após alta procura

### Artigo ###
A Prefeitura de Cristal realizou na manhã desta sexta-feira (12) o sorteio dos beneficiários do Programa Milho 100%, iniciativa de apoio ao produtor rural na Costa Doce. A medida foi adotada porque o número de inscrições superou a quantidade de sacas disponíveis para o município, e o sorteio público foi a forma escolhida para definir os contemplados com transparência e isonomia. Programas de distribuição de sementes e insumos como esse têm peso direto na economia das pequenas propriedades, ao reduzir o custo de implantação da lavoura e estimular a produção local de grãos. O milho, em especial, é estratégico para a agricultura familiar da região, seja para a comercialização, seja para a alimentação animal nas propriedades que combinam lavoura e criação. A grande procura registrada em Cristal evidencia tanto o interesse dos produtores quanto a importância de políticas públicas voltadas ao campo em municípios de base agrícola. Ao optar pelo sorteio, a administração buscou dar tratamento igualitário a todos os inscritos diante da limitação de recursos, prática recomendada para a distribuição de benefícios quando a demanda supera a oferta. Os produtores contemplados devem acompanhar as orientações sobre a retirada das sacas e os prazos a serem seguidos. A Prefeitura de Cristal e a Secretaria Municipal de Agricultura devem divulgar os próximos passos do programa, além de informações sobre eventuais novas etapas de distribuição ao longo do ano.

### Legenda sugerida ###
Cristal define por sorteio os beneficiários do Programa Milho 100% após a procura superar as sacas disponíveis.

### Palavras-chave ###
Cristal, Programa Milho 100%, sorteio, agricultura familiar, produtor rural, sementes, Costa Doce, política pública
""",

    "a3533cde66a8c4980dc360e776b8a90f9bd35335": """### Título ###
Tapes discute medidas preventivas com a Colônia de Pescadores Z-43

### Artigo ###
A Prefeitura de Tapes recebeu a representante da Colônia de Pescadores Z-43, Kelly Rigon, para uma conversa sobre as ações preventivas diante do período de chuvas e da possível elevação dos níveis das águas na Costa Doce. O encontro teve como foco a proteção das comunidades pesqueiras ribeirinhas, que estão entre as mais expostas às oscilações da Lagoa dos Patos e dos arroios que cortam o município. A pesca artesanal é uma atividade tradicional e economicamente importante para Tapes, e episódios de cheia podem comprometer embarcações, equipamentos e o próprio sustento das famílias que dependem do trabalho nas águas. Por isso, o diálogo entre o poder público e as entidades representativas do setor é apontado como passo essencial para antecipar riscos e organizar respostas rápidas. A articulação prévia permite mapear as áreas mais vulneráveis, definir pontos de apoio e estabelecer canais de comunicação direta com os pescadores em caso de elevação das águas. Ações desse tipo costumam envolver também a orientação sobre o recolhimento de redes e barcos, a identificação de abrigos e o acompanhamento das previsões de tempo. Ao colocar a comunidade pesqueira no centro das medidas preventivas, o município reconhece a importância social e econômica do setor e busca reduzir os impactos de eventuais cheias. As ações definidas a partir do encontro devem ser detalhadas e comunicadas à população pelos canais oficiais da Prefeitura de Tapes.

### Legenda sugerida ###
Prefeitura de Tapes e Colônia de Pescadores Z-43 alinham medidas preventivas para o período de chuvas.

### Palavras-chave ###
Tapes, Colônia de Pescadores Z-43, pesca artesanal, prevenção, chuvas, Lagoa dos Patos, Costa Doce
""",

    "a22b25799503d48eeceab4081c50af0fec9b3527": """### Título ###
Chuvisca forma primeiro grupo do Programa de Controle do Tabagismo

### Artigo ###
A Secretaria Municipal de Saúde de Chuvisca realizou a formação do primeiro grupo do Programa de Controle do Tabagismo, iniciativa voltada à promoção da saúde e à melhoria da qualidade de vida da população da Costa Doce. O programa reúne moradores que desejam parar de fumar e oferece acompanhamento coletivo, em uma proposta que combina apoio mútuo e orientação das equipes de saúde do município. Largar o cigarro é um processo que envolve aspectos físicos e comportamentais, e o trabalho em grupo é reconhecido como uma estratégia que ajuda a manter a motivação e a enfrentar as dificuldades comuns desse período. Ao reunir pessoas com o mesmo objetivo, o programa cria uma rede de apoio em que cada participante pode compartilhar experiências, dúvidas e conquistas, fortalecendo a decisão de abandonar o tabaco. O tabagismo está associado a uma série de problemas de saúde e representa um custo importante tanto para as famílias quanto para o sistema público, de modo que iniciativas de prevenção e cessação têm impacto que vai além do indivíduo. A formação do primeiro grupo em Chuvisca marca o início de um trabalho que tende a ser ampliado, à medida que novos moradores busquem o acompanhamento. Quem tem interesse em participar das próximas turmas ou em obter mais informações sobre o programa pode procurar a unidade de saúde do município ou os canais oficiais da Prefeitura de Chuvisca.

### Legenda sugerida ###
Chuvisca forma o primeiro grupo do Programa de Controle do Tabagismo, com acompanhamento coletivo.

### Palavras-chave ###
Chuvisca, tabagismo, programa de saúde, parar de fumar, qualidade de vida, Secretaria de Saúde, Costa Doce
""",

    "80b4312fa130db698ac33a2c754a2101d278c735": """### Título ###
Operação na fronteira prende dois homens com mais de 28 kg de maconha em Bagé

### Artigo ###
Uma ação conjunta da Polícia Civil e da Brigada Militar prendeu em flagrante dois homens com mais de 28 quilos de maconha em Bagé, na fronteira do Rio Grande do Sul. A operação ocorreu no âmbito do trabalho de enfrentamento ao crime organizado na região de fronteira, área historicamente utilizada por rotas do tráfico de drogas por sua posição estratégica. Durante a ação, os dois suspeitos foram detidos e o entorpecente foi apreendido, sendo encaminhados às autoridades competentes para os procedimentos cabíveis. A integração entre as forças de segurança é apontada como um dos fatores decisivos para o êxito desse tipo de operação, ao reunir inteligência policial, atuação ostensiva e conhecimento do território. A região de fronteira do Rio Grande do Sul recebe atenção permanente das forças de segurança justamente pela circulação de drogas, armas e outros ilícitos, o que exige patrulhamento contínuo e ações coordenadas. Apreensões como essa, além de retirar uma quantidade expressiva de entorpecente de circulação, fornecem elementos para o avanço das investigações sobre as redes responsáveis pelo transporte e pela distribuição da droga. O combate ao tráfico na fronteira é tratado como prioridade pelas instituições de segurança, que mantêm operações integradas de forma regular. As investigações seguem em andamento para identificar a origem e o destino do material apreendido e responsabilizar todos os envolvidos.

### Legenda sugerida ###
Polícia Civil e Brigada Militar prendem dois homens com mais de 28 kg de maconha em Bagé, na fronteira.

### Palavras-chave ###
Bagé, fronteira, tráfico de drogas, maconha, Polícia Civil, Brigada Militar, segurança pública, Rio Grande do Sul
""",

    "bde33368856dbdeb6aa6cd6c59085d2ea2c4960c": """### Título ###
Sertão Santana destina R$ 9,7 mil ao CTG Tio Raymundo para preservar a tradição

### Artigo ###
A Prefeitura de Sertão Santana assinou nesta sexta-feira o Termo de Fomento nº 009/2026 com o CTG Tio Raymundo, prevendo o repasse de R$ 9,7 mil à entidade. O recurso será destinado à execução de ações voltadas à preservação e à valorização da cultura tradicionalista gaúcha no município, reforçando o papel dos Centros de Tradições Gaúchas como guardiões da identidade regional. No Rio Grande do Sul, os CTGs cumprem uma função que vai além das danças e da música: são espaços de convivência comunitária, de transmissão de valores e de manutenção de costumes ligados à vida campeira, ao cavalo, à indumentária e à culinária típica. Em municípios do interior como Sertão Santana, essas entidades costumam concentrar boa parte da agenda cultural e social, envolvendo crianças, jovens e adultos em atividades ao longo de todo o ano. O apoio público por meio de termos de fomento permite que esses grupos mantenham suas estruturas, organizem eventos e ampliem o alcance de seu trabalho junto à comunidade. A formalização do repasse, por meio de instrumento próprio, também assegura transparência e prestação de contas sobre o uso dos recursos. Ao investir na cultura tradicionalista, o município reconhece o valor simbólico e econômico das manifestações que ajudam a fortalecer o sentimento de pertencimento e a atrair visitantes. As ações previstas no termo devem ser desenvolvidas ao longo do período de vigência e acompanhadas pela administração municipal.

### Legenda sugerida ###
Sertão Santana assina Termo de Fomento e repassa R$ 9,7 mil ao CTG Tio Raymundo.

### Palavras-chave ###
Sertão Santana, CTG Tio Raymundo, termo de fomento, cultura gaúcha, tradicionalismo, fomento, interior
""",
}


def main():
    apr_path = ROOT / "state" / f"aprovadas_{HOJE}.json"
    pauta_path = ROOT / "state" / f"pauta_{HOJE}.json"
    materias_dir = ROOT / "state" / f"materias_{HOJE}"

    data = json.loads(apr_path.read_text(encoding="utf-8"))
    apr_list = data.get("aprovadas") or data.get("curadas") or (data if isinstance(data, list) else [])

    pauta = []
    pub_count = 0
    for item in apr_list:
        h = item["id_hash"]
        if h not in PAUTA_ANGULADA:
            angul = _skip("BLOQUEAR", "Cabeçalho de seção / edital procedural / pauta sem âncora Sul-RS / guardrail — descartado na angulação")
            angul["titulo_sultv"] = (item.get("titulo") or "")[:100]
        else:
            angul = PAUTA_ANGULADA[h]
        if angul["decisao_final"] == "PUBLICAR" and pub_count >= 10:
            angul = {**angul, "decisao_final": "REBAIXAR", "decisao_motivo": "Quota diária esgotada (regra 14)"}
        if angul["decisao_final"] == "PUBLICAR":
            pub_count += 1
        pauta.append({**item, **angul})

    out = {"data": HOJE, "gerado_em": datetime.now(timezone.utc).isoformat(),
           "total": len(pauta), "pauta": pauta}
    pauta_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[angular] pauta -> {pauta_path}")

    from collections import Counter
    print("[angular] decisões:", Counter(p["decisao_final"] for p in pauta))

    materias_dir.mkdir(exist_ok=True)
    nwrite = 0
    for p in pauta:
        if p["decisao_final"] == "PUBLICAR" and p["formato_sugerido"] == "materia_longa":
            corpo = MATERIAS.get(p["id_hash"])
            if corpo:
                (materias_dir / f"{p['id_hash']}.md").write_text(corpo, encoding="utf-8")
                nwrite += 1
            else:
                print(f"[angular] AVISO: {p['id_hash']} PUBLICAR/materia_longa sem texto em MATERIAS")
    print(f"[angular] {nwrite} matérias longas escritas em {materias_dir}")


if __name__ == "__main__":
    main()
