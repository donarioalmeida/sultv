#!/usr/bin/env python3
"""
angular_2026-06-18.py — angulação editorial + redação (cowork-faz-tudo).
Pauta de 2026-06-18. Regra 12 INEGOCIÁVEL aplicada: nenhum veículo de
comunicação é citado em títulos, leads, captions ou matérias. Atribuição
apenas a fontes primárias institucionais. Quota 10 PUBLICAR (regra 14).
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
HOJE = datetime.now(timezone.utc).strftime("%Y-%m-%d")


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

    # 0. Costa Doce — Canal Junco, desassoreamento Tapes↔São Lourenço — PUBLICAR materia_longa
    "e7969854f9765783413a7df1f664437b051d8ecd": {
        "titulo_sultv": "Desassoreamento do Canal Junco avança em trecho de 90 km entre Tapes e São Lourenço",
        "chamada_faixa": "Canal Junco entra em nova etapa de obras",
        "subtitulo": "Trabalho de retirada de sedimentos no canal busca melhorar o escoamento de água e a navegabilidade na Costa Doce.",
        "lead": "As obras de desassoreamento do Canal Junco entraram em uma nova etapa no trecho de cerca de 90 quilômetros que liga Tapes a São Lourenço do Sul. A intervenção concentra-se na retirada de sedimentos acumulados ao longo dos anos, com o objetivo de recuperar a capacidade de escoamento de água e melhorar as condições de navegabilidade na região da Costa Doce.",
        "ganchos_3": [
            "Canal Junco recebe nova etapa de desassoreamento entre Tapes e São Lourenço",
            "Trecho em obras tem cerca de 90 quilômetros",
            "Retirada de sedimentos melhora escoamento de água e drenagem da região"
        ],
        "angulo_editorial": "Infraestrutura hídrica concreta em corredor entre duas cidades-núcleo da Costa Doce — fato com extensão definida (90 km), impacto direto em drenagem agrícola e prevenção de cheias; pauta de serviço positiva e de interesse rural e urbano.",
        "fontes_complementares_sugeridas": ["Prefeitura de Tapes", "Prefeitura de São Lourenço do Sul", "Secretaria Estadual do Meio Ambiente e Infraestrutura"],
        "lead_materia_longa": "As obras de desassoreamento do Canal Junco entraram em uma nova etapa no trecho de cerca de 90 quilômetros que liga Tapes a São Lourenço do Sul, com a retirada de sedimentos acumulados para recuperar o escoamento de água na Costa Doce.",
        "post_instagram": {
            "caption": "Boa notícia para a Costa Doce: as obras de desassoreamento do Canal Junco entraram em nova etapa no trecho de cerca de 90 quilômetros entre Tapes e São Lourenço do Sul. A retirada dos sedimentos acumulados ajuda a recuperar o escoamento da água, melhora a drenagem das áreas próximas e qualifica a navegabilidade — um trabalho que faz diferença direta para quem vive e produz na região.",
            "hashtags": ["#Tapes", "#SãoLourençoDoSul", "#CostaDoce", "#CanalJunco", "#Infraestrutura", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Obra grande na Costa Doce.",
            "desenvolvimento_45s": "As obras de desassoreamento do Canal Junco entraram em uma nova etapa, no trecho de cerca de 90 quilômetros que liga Tapes a São Lourenço do Sul. O trabalho retira os sedimentos que se acumularam ao longo dos anos no fundo do canal. Com isso, melhora o escoamento da água, a drenagem das áreas próximas e a navegabilidade na região. É uma intervenção importante para a Costa Doce, que ajuda na prevenção de alagamentos e beneficia tanto a produção rural quanto as comunidades urbanas.",
            "fechamento_8s": "Mais água escoando, menos risco de cheia.",
            "cta_5s": "Acompanhe com o SulTV.",
            "trilha_sugerida": "instrumental sóbrio regional"
        },
        "tag_thumbnail": "Canal Junco",
        "briefing_visual": {
            "descricao_pt": "Canal de água largo cortando área rural alagadiça no Sul do Rio Grande do Sul, vista ampla, maquinário de dragagem ao longe, sem pessoas",
            "query_en": ["water canal dredging rural", "river channel wetland aerial brazil", "drainage canal countryside"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Wide shot of a long water canal cutting through flat rural wetlands in southern Brazil, an excavator dredging sediment in the distance, overcast soft light, no people in foreground, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Infraestrutura hídrica concreta (90 km) entre duas cidades-núcleo da Costa Doce; interesse rural e urbano, prevenção de cheias"
    },

    # 1. Camaquã — colisão no centro — PUBLICAR materia_longa (factual, sóbrio)
    "2096ccf73ef4a2a60be99f7798edeee5124a6266": {
        "titulo_sultv": "Colisão entre moto e carro mobiliza atenção no centro de Camaquã",
        "chamada_faixa": "Acidente no centro de Camaquã reacende alerta",
        "subtitulo": "Ocorrência envolvendo uma motocicleta e um automóvel reforça a discussão sobre segurança viária na área central da cidade.",
        "lead": "Uma colisão entre uma motocicleta e um automóvel foi registrada no início da noite de quarta-feira (17) na Rua Capitão Adolfo Castro, no centro de Camaquã. Após o impacto, o motociclista parou na calçada próxima a um posto de combustíveis na esquina. A ocorrência reacende o debate sobre a segurança no trânsito em uma das áreas de maior circulação da cidade.",
        "ganchos_3": [
            "Colisão entre moto e carro é registrada no centro de Camaquã",
            "Acidente ocorreu na Rua Capitão Adolfo Castro, em via de grande circulação",
            "Ocorrência reforça atenção à segurança viária na área central"
        ],
        "angulo_editorial": "Trânsito em cidade-núcleo, abordagem factual e sóbria, sem dramatização e sem identificação de envolvidos (regras 3 e guardrail de tragédia); gancho para prevenção e segurança viária no centro.",
        "fontes_complementares_sugeridas": ["Departamento de Trânsito de Camaquã", "Brigada Militar"],
        "lead_materia_longa": "Uma colisão entre uma motocicleta e um automóvel foi registrada no início da noite de quarta-feira (17) na Rua Capitão Adolfo Castro, no centro de Camaquã, em uma das áreas de maior circulação da cidade.",
        "post_instagram": {
            "caption": "Uma colisão entre uma motocicleta e um automóvel foi registrada no início da noite de quarta-feira (17) na Rua Capitão Adolfo Castro, no centro de Camaquã. O ponto é um dos de maior circulação da cidade. Ocorrências assim reforçam a importância de redobrar a atenção no trânsito, respeitar a sinalização e manter a velocidade adequada — principalmente nas esquinas mais movimentadas do centro.",
            "hashtags": ["#Camaquã", "#Trânsito", "#SegurançaViária", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Atenção no trânsito de Camaquã.",
            "desenvolvimento_45s": "Uma colisão entre uma motocicleta e um automóvel foi registrada no início da noite de quarta-feira na Rua Capitão Adolfo Castro, no centro de Camaquã. Após o impacto, o motociclista parou na calçada perto de um posto de combustíveis na esquina. O ponto é um dos de maior circulação da cidade. Ocorrências como essa reforçam a importância de redobrar a atenção, respeitar a sinalização e manter a velocidade adequada, sobretudo nas esquinas mais movimentadas da área central.",
            "fechamento_8s": "Atenção redobrada salva vidas.",
            "cta_5s": "Dirija com cuidado.",
            "trilha_sugerida": "instrumental neutro"
        },
        "tag_thumbnail": "Trânsito Camaquã",
        "briefing_visual": {
            "descricao_pt": "Cruzamento urbano movimentado no centro de uma cidade do interior gaúcho ao entardecer, semáforo e faixa de pedestres, sem rostos identificáveis e sem placas de veículos legíveis",
            "query_en": ["urban intersection dusk small town", "city crossing traffic light evening", "street corner brazil town"],
            "evitar": ["rostos identificáveis", "placas de veículo legíveis", "marcas", "texto", "logos", "sangue ou vítimas"],
            "prompt_ia": "A busy urban street corner in a small southern Brazilian town at dusk, traffic light and crosswalk visible, soft evening light, no identifiable faces, no readable license plates, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Trânsito em cidade-núcleo, sem vítima identificada nem fatalidade; abordagem factual e de prevenção viária"
    },

    # 2. Tapes — invernada em programa de TV — REBAIXAR (regra 12: emissora)
    "d8189c7822ac26058b70a9ab1b87574be545b727": _skip(
        "REBAIXAR",
        "Gancho central é aparição em programa de emissora de TV concorrente — citar inviabilizado pela regra 12 e promoveria veículo de terceiros; vira nota interna"
    ),

    # 3. Tapes — coleta de eletrônicos — REBAIXAR (data já ocorrida; nova data já publicada)
    "38fc79ea769fec46b28d1e349f2cdaf943970f9b": _skip(
        "REBAIXAR",
        "Ação de coleta com data já transcorrida (17); a versão com nova data já consta no histórico de publicações"
    ),

    # 4. Arambaré — Saúde na Estrada — REBAIXAR (já publicado)
    "612ffb08a1ba713e460e43a35aebc9d85358c4c8": _skip(
        "REBAIXAR",
        "Conteúdo idêntico já publicado em ciclo anterior (consta no histórico); evita duplicata"
    ),

    # 5. Arambaré — cursos gratuitos — BLOQUEAR (notícia de abril, defasada)
    "5ab0f2f181de4c5cbc3c8836b4420288a6261ba2": _skip(
        "BLOQUEAR",
        "Notícia datada de 16 de abril de 2026 — conteúdo defasado, inscrições provavelmente encerradas"
    ),

    # 6. Cristal — reunião sobre limpeza urbana — REBAIXAR (reunião de rotina; prefeito já em pauta recente)
    "6d4334f756e8e21932963970c56e3ad757bf1c64": _skip(
        "REBAIXAR",
        "Reunião administrativa de rotina sobre serviços de limpeza, sem fato concreto novo; agenda do mesmo gestor já contemplada recentemente"
    ),

    # 7. Chuvisca — limpeza de açude em São Brás — PUBLICAR materia_longa
    "596644b6d24982399ea9051ef6513e2cedc59dd0": {
        "titulo_sultv": "Limpeza de açude em São Brás amplia reserva de água para a produção em Chuvisca",
        "chamada_faixa": "Chuvisca amplia reserva de água em São Brás",
        "subtitulo": "Serviço de desassoreamento aumenta a capacidade de armazenamento do reservatório e melhora o uso da água na propriedade rural atendida.",
        "lead": "Uma ação de limpeza de açude foi realizada na localidade de São Brás, no interior de Chuvisca, com o objetivo de ampliar a capacidade de armazenamento de água e melhorar as condições de uso do reservatório. O serviço reforça o apoio à produção rural em uma região onde a disponibilidade de água é fator decisivo para a atividade no campo.",
        "ganchos_3": [
            "Açude de São Brás recebe limpeza e amplia reserva de água em Chuvisca",
            "Serviço aumenta a capacidade de armazenamento do reservatório",
            "Ação apoia a produção rural e a segurança hídrica da localidade"
        ],
        "angulo_editorial": "Segurança hídrica e apoio à produção rural em cidade-núcleo — fato concreto e positivo, de interesse direto do produtor; tema sensível diante de estiagens e da gestão de água no interior gaúcho.",
        "fontes_complementares_sugeridas": ["Prefeitura de Chuvisca", "Secretaria Municipal de Agricultura de Chuvisca", "Emater/RS"],
        "lead_materia_longa": "Uma ação de limpeza de açude foi realizada na localidade de São Brás, no interior de Chuvisca, com o objetivo de ampliar a capacidade de armazenamento de água e melhorar as condições de uso do reservatório na propriedade atendida.",
        "post_instagram": {
            "caption": "Água é o que move a produção no campo. Em Chuvisca, uma ação de limpeza de açude na localidade de São Brás ampliou a capacidade de armazenamento do reservatório e melhorou as condições de uso da água na propriedade atendida. Serviços como esse ajudam o produtor a enfrentar períodos de estiagem e dão mais segurança hídrica para quem vive e trabalha no interior.",
            "hashtags": ["#Chuvisca", "#Agro", "#SegurançaHídrica", "#Açude", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Água garantida no campo.",
            "desenvolvimento_45s": "Uma ação de limpeza de açude foi realizada na localidade de São Brás, no interior de Chuvisca. O serviço de desassoreamento retira o material acumulado no fundo do reservatório e amplia a capacidade de armazenamento de água. Com isso, melhora o uso da água na propriedade e dá mais segurança ao produtor em períodos de estiagem. Ações como essa fortalecem a produção rural e mostram a importância de cuidar da reserva hídrica no interior gaúcho.",
            "fechamento_8s": "Mais água armazenada, mais segurança.",
            "cta_5s": "Acompanhe com o SulTV.",
            "trilha_sugerida": "instrumental campeiro leve"
        },
        "tag_thumbnail": "Açude Chuvisca",
        "briefing_visual": {
            "descricao_pt": "Açude rural cheio de água cercado por campo verde no interior gaúcho, escavadeira fazendo limpeza na margem, dia claro, sem pessoas",
            "query_en": ["farm reservoir pond countryside", "excavator cleaning pond rural", "water reservoir green field brazil"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "A rural farm reservoir full of water surrounded by green fields in southern Brazil, an excavator dredging the bank, clear daylight, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Segurança hídrica e apoio à produção rural em cidade-núcleo; fato concreto e positivo de interesse do produtor"
    },

    # 8. São Lourenço — edital de convocação — BLOQUEAR (procedural)
    "d7802c3a36602887466c509c1027f665ad9a7c22": _skip(
        "BLOQUEAR",
        "Convocação de processo seletivo — edital procedimental, sem interesse editorial amplo"
    ),

    # 9. São Lourenço — atualização de vacinação — REBAIXAR (data já ocorrida; já publicado)
    "30a1e2c79d28bac9d592e51269a0709cf8f404a6": _skip(
        "REBAIXAR",
        "Ação com data já transcorrida (17) e conteúdo equivalente já consta no histórico"
    ),

    # 10. Chuvisca — edital de penalidade — BLOQUEAR (procedural + defasado)
    "e01838afcd9335ee307b79a73b8b0bf111bfe4ba": _skip(
        "BLOQUEAR",
        "Edital de penalidade datado de 30/03/2026 — documento procedimental e defasado"
    ),

    # 11. Cristal — reforma da UBS Formosa — PUBLICAR materia_longa
    "ce6b76ed288b0d8236d3030d6e2bdf4897ba33e6": {
        "titulo_sultv": "UBS Formosa vai passar por grande reforma e amplia atendimento de saúde em Cristal",
        "chamada_faixa": "UBS Formosa será reformada em Cristal",
        "subtitulo": "Unidade contemplada por programa de qualificação da atenção básica recebe obras para melhorar a estrutura e o atendimento à comunidade.",
        "lead": "A Unidade Básica de Saúde Formosa, em Cristal, vai passar por uma grande reforma nos próximos dias. Contemplada por um programa de qualificação da rede de atenção básica, a unidade receberá melhorias estruturais com o objetivo de ampliar o conforto e a qualidade do atendimento oferecido à comunidade.",
        "ganchos_3": [
            "UBS Formosa, em Cristal, vai passar por grande reforma",
            "Unidade foi contemplada por programa de qualificação da atenção básica",
            "Obras buscam melhorar estrutura e atendimento à comunidade"
        ],
        "angulo_editorial": "Investimento em infraestrutura de saúde (não orientação médica) em cidade-núcleo — fato concreto e positivo, com impacto direto no acesso da população à atenção básica.",
        "fontes_complementares_sugeridas": ["Prefeitura de Cristal", "Secretaria Municipal de Saúde de Cristal"],
        "lead_materia_longa": "A Unidade Básica de Saúde Formosa, em Cristal, vai passar por uma grande reforma nos próximos dias, com melhorias estruturais voltadas a ampliar o conforto e a qualidade do atendimento oferecido à comunidade.",
        "post_instagram": {
            "caption": "Saúde mais perto e com mais estrutura: a UBS Formosa, em Cristal, vai passar por uma grande reforma nos próximos dias. A unidade foi contemplada por um programa de qualificação da atenção básica e receberá melhorias para ampliar o conforto e a qualidade do atendimento à comunidade. Investir na estrutura das unidades de saúde é investir no acesso de todos a um atendimento melhor.",
            "hashtags": ["#Cristal", "#Saúde", "#AtençãoBásica", "#UBS", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Reforma na saúde de Cristal.",
            "desenvolvimento_45s": "A Unidade Básica de Saúde Formosa, em Cristal, vai passar por uma grande reforma nos próximos dias. A unidade foi contemplada por um programa de qualificação da rede de atenção básica e receberá melhorias na sua estrutura. O objetivo é ampliar o conforto e a qualidade do atendimento oferecido à comunidade. Investir na estrutura das unidades de saúde é uma forma de garantir um atendimento melhor e mais próximo da população que depende do serviço público.",
            "fechamento_8s": "Estrutura nova para atender melhor.",
            "cta_5s": "Acompanhe com o SulTV.",
            "trilha_sugerida": "instrumental positivo leve"
        },
        "tag_thumbnail": "UBS Cristal",
        "briefing_visual": {
            "descricao_pt": "Fachada de uma unidade básica de saúde de cidade pequena no interior do Sul do Brasil, prédio simples, dia claro, sem pessoas identificáveis",
            "query_en": ["small public health clinic building", "community health center facade", "primary care clinic exterior"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Exterior facade of a small public primary health care clinic in a small southern Brazilian town, simple building, clear daylight, no identifiable people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Investimento em infraestrutura de saúde em cidade-núcleo; fato concreto e positivo, sem orientação médica"
    },

    # 12. Barra do Ribeiro — Velejaço solidário — BLOQUEAR (cabeçalho de seção/garbled)
    "2ca9c6c05b652779fe1185d698a6d67e649d2e53": _skip(
        "BLOQUEAR",
        "Título corrompido com cabeçalho de seção do portal; conteúdo ausente"
    ),

    # 13. Barra do Ribeiro — contracheques — BLOQUEAR (cabeçalho de seção)
    "74c3f70dce8c8fcb2ce5a5a811ff73b358a3d7e0": _skip(
        "BLOQUEAR",
        "Aviso administrativo / cabeçalho de seção sem fato editorial"
    ),

    # 14. Sentinela do Sul — audiência pública — BLOQUEAR (procedural, sem conteúdo)
    "09dca743ce1ebf0dc175bb3445b37a7e2f1c0220": _skip(
        "BLOQUEAR",
        "Aviso de audiência pública procedimental, sem detalhamento de pauta ou data útil"
    ),

    # 15. Sentinela do Sul — notas fiscais — BLOQUEAR (procedural + defasado)
    "c77c704f766cfa913b42a8d2b37cfc4c03320244": _skip(
        "BLOQUEAR",
        "Comunicado administrativo datado de 05/05/2026 — procedimental e defasado"
    ),

    # 16. ENEM — prazo de taxa — REBAIXAR (nacional sem âncora regional)
    "6f39d5487a3fd0ffac083dd87e89ef11d12e5efd": _skip(
        "REBAIXAR",
        "Pauta nacional (MEC/ENEM) sem âncora concreta no Sul-RS; serviço genérico"
    ),

    # 17. Pelotas — audiências do Plano de Contingência — PUBLICAR materia_longa
    "879591811dafc700bcf106a7f4dfa811189f23ac": {
        "titulo_sultv": "Pelotas leva audiências públicas aos bairros para apresentar Plano de Contingência",
        "chamada_faixa": "Pelotas debate Plano de Contingência nos bairros",
        "subtitulo": "Encontros seguem até sexta-feira (19) em diferentes localidades para apresentar as ações de prevenção e resposta a emergências.",
        "lead": "A Prefeitura de Pelotas promove uma série de audiências públicas em diferentes bairros para apresentar o Plano de Contingência do município. As agendas seguem até sexta-feira (19), com a proposta de envolver a população na discussão das medidas de prevenção e resposta a situações de emergência, tema sensível para uma cidade que conviveu com eventos climáticos extremos nos últimos anos.",
        "ganchos_3": [
            "Pelotas apresenta Plano de Contingência em audiências nos bairros",
            "Encontros seguem até sexta-feira (19) em diferentes localidades",
            "Objetivo é envolver a população na prevenção e resposta a emergências"
        ],
        "angulo_editorial": "Proteção e defesa civil em cidade da Costa Doce ampliada — fato concreto com calendário e localidades; tema de alta relevância pós-enchentes, com chamada à participação popular.",
        "fontes_complementares_sugeridas": ["Prefeitura de Pelotas", "Secretaria de Proteção e Defesa Civil de Pelotas"],
        "lead_materia_longa": "A Prefeitura de Pelotas promove uma série de audiências públicas em diferentes bairros para apresentar o Plano de Contingência do município, com agendas que seguem até sexta-feira (19) em diversas localidades.",
        "post_instagram": {
            "caption": "Estar preparado salva vidas. Pelotas está levando audiências públicas aos bairros para apresentar o Plano de Contingência do município, com encontros que seguem até sexta-feira (19) em diferentes localidades. O objetivo é envolver a população na discussão das medidas de prevenção e de resposta a emergências — um tema que ganhou ainda mais peso depois dos eventos climáticos extremos dos últimos anos.",
            "hashtags": ["#Pelotas", "#DefesaCivil", "#PlanoDeContingência", "#Prevenção", "#CostaDoce", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Pelotas se prepara para emergências.",
            "desenvolvimento_45s": "A Prefeitura de Pelotas está promovendo audiências públicas em diferentes bairros para apresentar o Plano de Contingência do município. As agendas seguem até sexta-feira, com a proposta de envolver a população na discussão das medidas de prevenção e de resposta a situações de emergência. Depois dos eventos climáticos extremos dos últimos anos, planejar e informar a comunidade virou prioridade. A participação dos moradores nessas audiências é fundamental para que o plano realmente funcione na hora que mais importa.",
            "fechamento_8s": "Prevenção começa com informação.",
            "cta_5s": "Participe e acompanhe o SulTV.",
            "trilha_sugerida": "instrumental sóbrio"
        },
        "tag_thumbnail": "Defesa Civil Pelotas",
        "briefing_visual": {
            "descricao_pt": "Auditório ou salão comunitário com plateia em audiência pública municipal no Sul do Brasil, vista de fundo da sala, sem rostos identificáveis em primeiro plano",
            "query_en": ["public hearing community meeting hall", "town hall meeting audience back view", "municipal assembly room people"],
            "evitar": ["rostos identificáveis em primeiro plano", "marcas", "texto", "logos"],
            "prompt_ia": "A community hall during a municipal public hearing in southern Brazil, audience seen from the back of the room, neutral lighting, no identifiable faces in foreground, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Defesa civil e prevenção em cidade da Costa Doce ampliada; fato concreto com calendário e forte relevância pós-enchentes"
    },

    # 18. ALERS — privatizações / plebiscito — BLOQUEAR (política partidária)
    "d00105e7a6cd3b4091aeb1dabbb95c81fb53b39e": _skip(
        "BLOQUEAR",
        "Debate sobre privatizações, concessões e plebiscito com manifestação partidária — guardrail de política partidária"
    ),

    # 19. ALERS — Funcriança — REBAIXAR (legislativo/defasado)
    "49348b06a39337d964518e54a7715142418ea220": _skip(
        "REBAIXAR",
        "Conteúdo legislativo com data aparentemente defasada; tema institucional fora do eixo Sul-RS"
    ),

    # 20. RS — renegociação de dívidas — REBAIXAR (já publicado)
    "ddcd388ff38cf8bb1e89d08320447b73c9be844a": _skip(
        "REBAIXAR",
        "Conteúdo já consta no histórico de publicações; evita duplicata"
    ),

    # 21. RS — vinhos apreendidos — REBAIXAR (estadual, sem âncora Sul; sensacional)
    "8c10d704aa76774d2be1bdb6d93ca335fbf9061b": _skip(
        "REBAIXAR",
        "Apreensão estadual sem âncora no eixo Costa Doce/Sul; abordagem sensacionalista"
    ),

    # 22. RS — apreensão de alimentos — REBAIXAR (estadual, sem âncora)
    "169887fad4143c5f8357298a7ea4f6f2c6e1f1bf": _skip(
        "REBAIXAR",
        "Operação estadual genérica sem âncora local; tema correlato a item já rebaixado"
    ),

    # 23. RS — Multifeira de Esteio — BLOQUEAR (evento já encerrado, região metro)
    "e6fff2725635f8da6e880c351f39276a44142f44": _skip(
        "BLOQUEAR",
        "Evento realizado de 13 a 17 — já encerrado — e em região metropolitana fora do eixo de cobertura"
    ),

    # 24. Sertão Santana — termos de fomento — REBAIXAR (rotina política local)
    "ebf159c5f7b5bea63d6c3d9d891f7e9f650a352b": _skip(
        "REBAIXAR",
        "Entrega de termos de fomento via emendas — rotina político-administrativa em cidade de segunda camada"
    ),

    # 25. Amaral Ferrador — visita SINDITABACO — REBAIXAR (rotina de gabinete)
    "63a6ac2ca1d31f81d6777c345692d7019b5f80f9": _skip(
        "REBAIXAR",
        "Visita protocolar de gabinete sem fato concreto; baixo interesse editorial amplo"
    ),

    # 26. Amaral Ferrador — audiência DAER — REBAIXAR (reunião de rotina)
    "d495dcc8e3b569216b364db3fb2ef094cb5cddbd": _skip(
        "REBAIXAR",
        "Audiência administrativa sobre estradas sem encaminhamento concreto anunciado"
    ),

    # 27. Canguçu — CRAS em Festa — REBAIXAR (evento social de rotina, 2ª camada)
    "b4b061717159ae29b1657be9dae327dfcda47167": _skip(
        "REBAIXAR",
        "Evento social comunitário de rotina em cidade de segunda camada; sem âncora forte"
    ),

    # 28. Canguçu — Mini Prefeito — REBAIXAR (rotina cívica escolar)
    "b3d70d8c5eb2f0dd45340af8383fa79c715630fe": _skip(
        "REBAIXAR",
        "Divulgação de resultado de atividade escolar cívica; interesse restrito"
    ),

    # 29. Encruzilhada — campeonato de orientação — BLOQUEAR (esporte já ocorrido, região distante)
    "63f9123fce99a8d3679d5b3d14a9fe3456f8c761": _skip(
        "BLOQUEAR",
        "Etapa esportiva realizada em 13 e 14 — já encerrada — em região fora do eixo de cobertura"
    ),

    # 30. Encruzilhada — seminário educação fiscal — REBAIXAR (rotina, data passada)
    "34adc318a37868ec8c7de53198545049ac9db29e": _skip(
        "REBAIXAR",
        "Participação em seminário com data já transcorrida; conteúdo administrativo de rotina"
    ),

    # 31. Sertão Santana — convênio grade aradora — REBAIXAR (rotina administrativa)
    "2e2bdcdbb04de728c4d45a48821e689471d8490a": _skip(
        "REBAIXAR",
        "Assinatura de convênio de equipamento — rotina; baixa densidade para matéria própria"
    ),

    # 32. Santa Maria — Revista Entrelaços UFSM — REBAIXAR (sem âncora núcleo; tema sensível)
    "c7142b3eee617cb022f8cbc846e30651acbd93e0": _skip(
        "REBAIXAR",
        "Lançamento acadêmico fora do eixo de cobertura; tema sensível que demanda cautela editorial"
    ),

    # 33. Eldorado do Sul — aula inaugural — REBAIXAR (rotina)
    "99833c0fd192e116c1ff4904530e41fde5a0d0cc": _skip(
        "REBAIXAR",
        "Aula inaugural de qualificação — rotina institucional; baixo gancho"
    ),

    # 34. Rio Grande — rede de água para 130 famílias — PUBLICAR post_instagram
    "c83c7e1497d24ba2dbd4db9b966b5bee50d0dbeb": {
        "titulo_sultv": "Rio Grande inicia rede de água que vai beneficiar mais de 130 famílias no bairro Rural",
        "chamada_faixa": "Água tratada chega a 130 famílias em Rio Grande",
        "subtitulo": "Obras de abastecimento na antiga Rua das Cocheiras atendem moradores que aguardavam o acesso há anos.",
        "lead": "Começaram em Rio Grande as obras de implantação da rede de abastecimento de água na Rua Arlindo Rodrigues da Silva, a antiga Rua das Cocheiras, no bairro Rural. A intervenção vai beneficiar mais de 130 famílias que aguardavam, há anos, o acesso à água tratada.",
        "ganchos_3": [
            "Rio Grande inicia rede de água no bairro Rural",
            "Obra vai beneficiar mais de 130 famílias",
            "Moradores aguardavam o acesso à água tratada há anos"
        ],
        "angulo_editorial": "Infraestrutura básica e direito ao saneamento na faixa sul do estado — fato concreto, número de famílias atendidas, impacto social direto.",
        "fontes_complementares_sugeridas": ["Prefeitura do Rio Grande", "Companhia de saneamento responsável"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Uma espera de anos chega ao fim no bairro Rural, em Rio Grande: começaram as obras de implantação da rede de abastecimento de água na Rua Arlindo Rodrigues da Silva, a antiga Rua das Cocheiras. A ação vai beneficiar mais de 130 famílias com acesso à água tratada. Saneamento é saúde, dignidade e qualidade de vida — e cada nova ligação representa uma conquista para a comunidade.",
            "hashtags": ["#RioGrande", "#Saneamento", "#ÁguaTratada", "#Infraestrutura", "#RioGrandeDoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Água tratada chegando.",
            "desenvolvimento_45s": "Começaram em Rio Grande as obras de implantação da rede de abastecimento de água na antiga Rua das Cocheiras, no bairro Rural. A ação vai beneficiar mais de 130 famílias que aguardavam, há anos, o acesso à água tratada. Saneamento básico é saúde e qualidade de vida, e cada nova ligação representa uma conquista importante para a comunidade.",
            "fechamento_8s": "Saneamento é dignidade.",
            "cta_5s": "Acompanhe com o SulTV.",
            "trilha_sugerida": "instrumental positivo"
        },
        "tag_thumbnail": "Água Rio Grande",
        "briefing_visual": {
            "descricao_pt": "Operários instalando tubulação de água em vala em rua de bairro periférico, obra de saneamento, sem rostos identificáveis",
            "query_en": ["water pipe installation trench street", "water supply construction works", "pipeline laying residential road"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "Construction workers laying water supply pipes in a trench along a residential street in a Brazilian town, sanitation infrastructure work, daylight, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Saneamento básico com número concreto de famílias atendidas; impacto social direto na faixa sul do estado"
    },

    # 35. Rio Grande — visita APA Lagoa Verde — REBAIXAR (rotina)
    "f81ab07e3f8534dff7271340a91003868a8e98d4": _skip(
        "REBAIXAR",
        "Visita guiada institucional de articulação ambiental — sem fato concreto novo"
    ),

    # 36. Santa Maria — lançamento da Feisma hoje — PUBLICAR post_instagram (timely)
    "c40b2a43064fc96d6277137d4dbac5d6f2595a56": {
        "titulo_sultv": "Multifeira de Santa Maria está de volta e tem lançamento oficial nesta quinta",
        "chamada_faixa": "Feisma 2026 tem lançamento oficial em Santa Maria",
        "subtitulo": "Evento de lançamento com apresentação dos parceiros acontece nesta quinta-feira (18), marcando o retorno da multifeira.",
        "lead": "A Multifeira de Santa Maria, a Feisma, está de volta em 2026, e o lançamento oficial do evento acontece nesta quinta-feira (18), com a apresentação dos parceiros. O retorno da feira movimenta a agenda econômica e de entretenimento da região central do estado.",
        "ganchos_3": [
            "Feisma 2026 tem lançamento oficial nesta quinta-feira (18)",
            "Multifeira de Santa Maria está de volta",
            "Lançamento marca o retorno de um dos grandes eventos da região"
        ],
        "angulo_editorial": "Agenda econômica e de entretenimento na região central — fato com data (lançamento hoje), gancho de calendário regional.",
        "fontes_complementares_sugeridas": ["Prefeitura de Santa Maria", "Organização da Feisma"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "A Multifeira de Santa Maria, a Feisma, está de volta em 2026! O lançamento oficial acontece nesta quinta-feira (18), com a apresentação dos parceiros do evento. O retorno da feira é uma boa notícia para a economia e para o entretenimento da região central do estado, reunindo expositores, atrações e público em um dos eventos mais tradicionais do calendário local.",
            "hashtags": ["#SantaMaria", "#Feisma", "#Eventos", "#Economia", "#RioGrandeDoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "A Feisma está de volta.",
            "desenvolvimento_45s": "A Multifeira de Santa Maria, a Feisma, está de volta em 2026. O lançamento oficial do evento acontece nesta quinta-feira, com a apresentação dos parceiros. O retorno da feira movimenta a economia e o entretenimento da região central do estado, reunindo expositores, atrações e público em um dos eventos mais tradicionais do calendário local.",
            "fechamento_8s": "Boa notícia para a região.",
            "cta_5s": "Acompanhe com o SulTV.",
            "trilha_sugerida": "instrumental animado"
        },
        "tag_thumbnail": "Feisma Santa Maria",
        "briefing_visual": {
            "descricao_pt": "Parque de feira ou exposição com estandes e luzes ao entardecer no Sul do Brasil, ambiente de evento, sem rostos identificáveis",
            "query_en": ["trade fair pavilion lights evening", "exhibition fairground stands", "county fair event ground"],
            "evitar": ["rostos identificáveis", "marcas", "texto", "logos"],
            "prompt_ia": "An exhibition fairground with stands and warm lights at dusk in southern Brazil, festive event atmosphere, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Agenda econômica e de entretenimento com lançamento marcado para hoje; gancho de calendário regional"
    },

    # 37. Dom Feliciano — jantar baile CTG — REBAIXAR (convite/evento de baixo score)
    "892be9289866a1348efb866206afbef7a3ddfad5": _skip(
        "REBAIXAR",
        "Convite a evento social de CTG — baixo gancho editorial; vira nota interna"
    ),

    # 38. Dom Feliciano — oficina de costura CRAS — REBAIXAR (serviço pontual)
    "0b7ee95d1ff2a2bf9796a4a0274d482a7917de18": _skip(
        "REBAIXAR",
        "Oficina pontual em CRAS — serviço de alcance restrito"
    ),

    # 39. Encantado — transporte universitário — REBAIXAR (edital, fora do eixo)
    "ebadcaf9a1a72d19086712e0aa4e03bb3cdecf17": _skip(
        "REBAIXAR",
        "Edital de transporte universitário — procedimental e em cidade fora do eixo de cobertura"
    ),

    # 40. Bagé — IA e Direito — REBAIXAR (off-topic, opinião institucional)
    "0c808e564b7055a38c3dbf400337a0d63db5ee62": _skip(
        "REBAIXAR",
        "Conteúdo opinativo sobre IA e Direito sem âncora factual regional"
    ),

    # 41. Venâncio Aires — Corsan prazo — REBAIXAR (fala só citada por veículo; regra 12)
    "027b1d2f90ca1a414601a0f68d18495cd2415ab9": _skip(
        "REBAIXAR",
        "Núcleo da informação é entrevista a veículo de comunicação (regra 12); fora do eixo de cobertura"
    ),

    # 42. Venâncio Aires — coluna fiscalização — REBAIXAR (opinião/veículo)
    "63d120a74a619266de68e59a3184b9e18fe00616": _skip(
        "REBAIXAR",
        "Conteúdo de coluna de opinião ancorado em entrevista a veículo (regra 12); fora do eixo"
    ),

    # 43. Bento Gonçalves — exposição história — REBAIXAR (região distante, cultural local)
    "62ff80870c2148aae022d7cb5d05837b77ed5867": _skip(
        "REBAIXAR",
        "Exposição cultural local na Serra — fora do eixo de cobertura da Costa Doce/Sul"
    ),

    # 44. Bento Gonçalves — vacinação gripe — REBAIXAR (serviço, região distante)
    "16391dcdb93208983d47d03efa085d01964669a6": _skip(
        "REBAIXAR",
        "Serviço de saúde local na Serra — fora do eixo de cobertura"
    ),
}


MATERIAS = {
    "e7969854f9765783413a7df1f664437b051d8ecd": """### Título ###
Desassoreamento do Canal Junco avança em trecho de 90 km entre Tapes e São Lourenço

### Artigo ###
As obras de desassoreamento do Canal Junco entraram em uma nova etapa no trecho de cerca de 90 quilômetros que liga Tapes a São Lourenço do Sul, na região da Costa Doce. A intervenção concentra-se na retirada dos sedimentos que se acumularam ao longo dos anos no leito do canal, processo natural que reduz a profundidade e compromete a passagem da água. Com o desassoreamento, o objetivo é recuperar a capacidade de escoamento e melhorar as condições de navegabilidade no trecho. O Canal Junco cumpre um papel estratégico para a região, ao interligar corpos d'água e auxiliar na drenagem de extensas áreas planas, muitas delas ocupadas por lavouras e por comunidades ribeirinhas. Quando o canal está assoreado, a água encontra mais dificuldade para escoar, o que aumenta o risco de alagamentos em períodos de chuva intensa e prejudica o manejo hídrico das propriedades rurais próximas. A retirada do material acumulado tende a beneficiar diretamente a atividade agrícola, especialmente a lavoura de arroz, que depende de um sistema eficiente de irrigação e de drenagem. Ao mesmo tempo, a obra contribui para a segurança das comunidades urbanas situadas no entorno, num momento em que a prevenção de cheias se tornou prioridade no Rio Grande do Sul após os eventos climáticos extremos dos últimos anos. A recuperação de canais e a manutenção da infraestrutura hídrica são apontadas como medidas essenciais para reduzir a vulnerabilidade de regiões baixas como a Costa Doce, banhada pela Lagoa dos Patos. O avanço dos trabalhos entre Tapes e São Lourenço do Sul sinaliza um esforço de qualificação dessa infraestrutura, com impacto que se estende do campo às cidades. As etapas seguintes e o cronograma da obra devem ser acompanhados junto às administrações municipais e aos órgãos responsáveis pela gestão hídrica na região.

### Legenda sugerida ###
Desassoreamento do Canal Junco avança em trecho de cerca de 90 km entre Tapes e São Lourenço do Sul, recuperando o escoamento de água na Costa Doce.

### Palavras-chave ###
Canal Junco, desassoreamento, Tapes, São Lourenço do Sul, Costa Doce, drenagem, prevenção de cheias, infraestrutura hídrica
""",

    "2096ccf73ef4a2a60be99f7798edeee5124a6266": """### Título ###
Colisão entre moto e carro mobiliza atenção no centro de Camaquã

### Artigo ###
Uma colisão entre uma motocicleta e um automóvel foi registrada no início da noite de quarta-feira (17), na Rua Capitão Adolfo Castro, na área central de Camaquã. Após o impacto, o motociclista parou na calçada próxima a um posto de combustíveis situado na esquina onde ocorreu o acidente. O ponto é um dos de maior circulação de veículos e pedestres na cidade, o que costuma exigir atenção redobrada de motoristas e condutores de motocicletas. Ocorrências de trânsito em vias centrais reacendem, periodicamente, a discussão sobre segurança viária nos municípios do interior, onde o aumento da frota e o intenso fluxo em determinados horários elevam a exposição a colisões. Cruzamentos movimentados, em especial nas proximidades de estabelecimentos comerciais e de serviços, concentram boa parte dessas ocorrências, sobretudo no fim da tarde e no início da noite, quando se somam o retorno do trabalho e a redução da luminosidade. Especialistas em segurança no trânsito costumam reforçar orientações simples e eficazes para reduzir riscos: respeitar a sinalização e os limites de velocidade, manter distância segura, redobrar a atenção ao se aproximar de esquinas e garantir o uso correto dos equipamentos de proteção, como o capacete no caso dos motociclistas. A presença de sinalização adequada e a fiscalização contínua também são fatores que ajudam a organizar o tráfego e a prevenir acidentes em áreas críticas. Para a comunidade, episódios como esse servem de alerta sobre a importância de uma condução responsável, que protege não apenas quem está ao volante ou sobre a moto, mas todos os que dividem o espaço urbano. A organização do trânsito no centro das cidades segue como um desafio permanente para o poder público e para os próprios condutores.

### Legenda sugerida ###
Colisão entre moto e carro é registrada no centro de Camaquã e reforça o alerta sobre segurança viária na área de maior circulação da cidade.

### Palavras-chave ###
Camaquã, trânsito, segurança viária, acidente, área central, prevenção, Costa Doce, mobilidade
""",

    "596644b6d24982399ea9051ef6513e2cedc59dd0": """### Título ###
Limpeza de açude em São Brás amplia reserva de água para a produção em Chuvisca

### Artigo ###
Uma ação de limpeza de açude foi realizada na localidade de São Brás, no interior de Chuvisca, com o objetivo de ampliar a capacidade de armazenamento de água e melhorar as condições de uso do reservatório na propriedade atendida. O serviço de desassoreamento consiste na retirada do material que se deposita no fundo do açude ao longo do tempo, como terra e sedimentos, e que reduz gradualmente o volume de água que o reservatório consegue guardar. Ao recuperar essa capacidade, a propriedade passa a contar com uma reserva maior, fundamental para atravessar períodos de estiagem e para sustentar as atividades do campo. A disponibilidade de água é um dos fatores mais decisivos para a produção rural, seja na irrigação de lavouras, na dessedentação de animais ou no abastecimento das atividades cotidianas da propriedade. Em regiões do interior gaúcho, onde a alternância entre períodos de chuva e de estiagem pode ser acentuada, a manutenção de açudes e a ampliação da capacidade de armazenamento funcionam como uma forma de segurança hídrica para o produtor. Investir na recuperação desses reservatórios é uma medida de baixo custo relativo e de alto impacto, que reduz a vulnerabilidade da produção diante de variações climáticas. Além do benefício direto para a propriedade atendida, ações como essa têm um efeito demonstrativo importante, ao incentivar outros produtores a cuidarem de suas reservas de água e a planejarem o uso do recurso. A gestão adequada da água no meio rural contribui não apenas para a produtividade, mas também para a preservação ambiental e para a resiliência das comunidades do campo. Iniciativas de apoio à infraestrutura hídrica reforçam o papel do poder público no fortalecimento da agricultura familiar e da produção local em municípios como Chuvisca.

### Legenda sugerida ###
Ação de limpeza de açude em São Brás amplia a capacidade de armazenamento de água e reforça a segurança hídrica da produção rural em Chuvisca.

### Palavras-chave ###
Chuvisca, açude, segurança hídrica, produção rural, desassoreamento, água, estiagem, Costa Doce
""",

    "ce6b76ed288b0d8236d3030d6e2bdf4897ba33e6": """### Título ###
UBS Formosa vai passar por grande reforma e amplia atendimento de saúde em Cristal

### Artigo ###
A Unidade Básica de Saúde Formosa, em Cristal, vai passar por uma grande reforma nos próximos dias. A unidade foi contemplada por um programa de qualificação da rede de atenção básica e receberá melhorias estruturais com o objetivo de ampliar o conforto e a qualidade do atendimento oferecido à comunidade. As intervenções em unidades básicas de saúde costumam envolver a recuperação e a modernização de espaços de espera, consultórios, salas de procedimentos e áreas de acolhimento, de forma a oferecer um ambiente mais adequado tanto para os pacientes quanto para as equipes de saúde. A atenção básica é a porta de entrada do sistema público de saúde e o nível de atendimento mais próximo da população, responsável por ações de prevenção, acompanhamento de condições crônicas, vacinação e encaminhamentos quando necessário. Quando a estrutura física da unidade é qualificada, melhora-se diretamente a experiência de quem busca atendimento e as condições de trabalho dos profissionais. Em municípios de menor porte, as unidades básicas têm papel ainda mais estratégico, pois muitas vezes representam o principal ponto de acesso à saúde para os moradores de bairros e de localidades do interior. Investir na reforma e na ampliação dessas estruturas significa fortalecer o cuidado mais perto de casa, reduzindo a necessidade de deslocamentos e desafogando serviços de maior complexidade. Programas de qualificação da atenção básica, que destinam recursos para obras e melhorias, têm sido um caminho para que os municípios consigam modernizar sua rede de saúde. Para a comunidade atendida pela UBS Formosa, a reforma representa a expectativa de um atendimento mais organizado e confortável. A administração municipal deve divulgar, em seus canais oficiais, os detalhes do cronograma das obras e eventuais ajustes no atendimento durante o período de execução.

### Legenda sugerida ###
UBS Formosa, em Cristal, vai passar por grande reforma após ser contemplada por programa de qualificação da atenção básica, ampliando o atendimento à comunidade.

### Palavras-chave ###
Cristal, UBS Formosa, saúde, atenção básica, reforma, unidade de saúde, infraestrutura, Costa Doce
""",

    "879591811dafc700bcf106a7f4dfa811189f23ac": """### Título ###
Pelotas leva audiências públicas aos bairros para apresentar Plano de Contingência

### Artigo ###
A Prefeitura de Pelotas promove uma série de audiências públicas em diferentes bairros para apresentar o Plano de Contingência do município. As agendas seguem até sexta-feira (19) em diversas localidades, com a proposta de envolver a população na discussão das medidas de prevenção e de resposta a situações de emergência. O Plano de Contingência reúne as diretrizes e os procedimentos que orientam a atuação do poder público e da comunidade diante de eventos como enchentes, temporais e outras situações de risco. Ao levar as audiências para os bairros, a administração busca aproximar o debate da realidade de cada região, ouvindo moradores e detalhando os fluxos de comunicação, os pontos de apoio e as rotas de segurança previstas para momentos críticos. O tema ganhou peso adicional no Rio Grande do Sul após os eventos climáticos extremos dos últimos anos, que evidenciaram a importância do planejamento, da informação e da preparação das comunidades. Pelotas, situada em uma região de baixadas e próxima a importantes corpos d'água, integra o conjunto de municípios que precisam manter atenção permanente à prevenção de desastres. A participação popular nessas audiências é considerada essencial, pois um plano de contingência só é eficaz quando a população conhece os procedimentos e sabe como agir em uma emergência. Saber para onde se dirigir, como receber alertas e quais são os pontos de apoio pode fazer diferença decisiva na proteção de vidas. Iniciativas de defesa civil que envolvem a comunidade fortalecem a chamada cultura de prevenção, em que cada cidadão se torna parte ativa da resposta a situações de risco. Os moradores interessados podem buscar informações sobre as datas e os locais das audiências junto à administração municipal e à estrutura de proteção e defesa civil do município.

### Legenda sugerida ###
Pelotas leva audiências públicas aos bairros até sexta (19) para apresentar o Plano de Contingência e envolver a população na prevenção a emergências.

### Palavras-chave ###
Pelotas, Plano de Contingência, defesa civil, prevenção, audiências públicas, emergência, enchentes, Costa Doce
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
            print(f"[angular] sem angulação para {h} — bloqueando")
            angul = _skip("BLOQUEAR", "Sem angulação configurada — descartado pelo guardrail")
            angul["titulo_sultv"] = item.get("titulo", "")[:100]
        else:
            angul = PAUTA_ANGULADA[h]

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
    print("[angular] decisões:", Counter(p["decisao_final"] for p in pauta))
    print("[angular] PUBLICAR:", pub_count)

    materias_dir.mkdir(exist_ok=True)
    nwrite = 0
    for p in pauta:
        if p["decisao_final"] == "PUBLICAR" and p["formato_sugerido"] == "materia_longa":
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
