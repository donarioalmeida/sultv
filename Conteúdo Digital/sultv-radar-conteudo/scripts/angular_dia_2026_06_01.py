#!/usr/bin/env python3
"""
angular_dia_2026_06_01.py — angulação editorial cowork-faz-tudo do dia 2026-06-01.

Run degradado: rede do sandbox limitou a coleta a 18 feeds reais (subset do banco
de 167 fontes). 202 candidatos -> 8 aprovados, todos post_instagram (score 5-6,
nenhuma cidade-núcleo no subset, portanto nenhuma matéria longa hoje).

Lê state/aprovadas_2026-06-01.json e escreve state/pauta_2026-06-01.json.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-01"


PAUTA_ANGULADA = {
    # 1. O Sul — "A nova presidência do TSE..." — BLOQUEAR (política partidária nacional)
    "1de9796272d333ac5c958f770b1199d27d6059b1": {
        "titulo_sultv": "", "chamada_faixa": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Guardrail política partidária — pauta institucional nacional (presidência do TSE), sem qualquer âncora no Sul do RS",
    },

    # 2. O Sul — CMPC Celulose / Guaíba — PUBLICAR (economia/desenvolvimento regional)
    "98b04896bfe7aec0575f8289ddf1fb1267ebdda1": {
        "titulo_sultv": "Ampliação da CMPC Celulose mobiliza prefeituras da região de Guaíba e Barra do Ribeiro",
        "chamada_faixa": "Ampliação da CMPC mobiliza região de Guaíba",
        "subtitulo": "Investimento na fábrica de celulose é tratado como prioridade de desenvolvimento por municípios do entorno de Porto Alegre.",
        "lead": "A ampliação da fábrica de celulose da CMPC, na região de Guaíba e Barra do Ribeiro, voltou ao centro do debate econômico no Rio Grande do Sul, tratada por lideranças municipais como uma prioridade de desenvolvimento para toda a região. O projeto envolve investimentos de grande porte e tem potencial de gerar empregos e movimentar a economia do entorno de Porto Alegre.",
        "ganchos_3": [
            "Investimento de grande porte no setor de celulose gaúcho",
            "Geração de empregos e cadeia florestal no entorno de Porto Alegre",
            "Municípios tratam o projeto como prioridade regional"
        ],
        "angulo_editorial": "Economia e desenvolvimento regional no RS — o foco é o investimento industrial da cadeia florestal/celulose e seu impacto em empregos e renda, não a disputa político-partidária. Pauta de economia.",
        "fontes_complementares_sugeridas": ["CMPC Celulose", "Prefeitura de Guaíba", "Prefeitura de Barra do Ribeiro", "Sedec-RS"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "A ampliação da fábrica de celulose da CMPC, na região de Guaíba e Barra do Ribeiro, voltou ao centro do debate econômico gaúcho. Tratado como prioridade de desenvolvimento por lideranças da região, o projeto tem potencial de gerar empregos e movimentar a cadeia florestal no entorno de Porto Alegre.",
            "hashtags": ["#RioGrandeDoSul", "#Economia", "#Celulose", "#Investimento", "#Guaíba", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Investimento bilionário no RS.",
            "desenvolvimento_45s": "A ampliação da fábrica de celulose da CMPC, na região de Guaíba e Barra do Ribeiro, voltou ao centro do debate econômico no Rio Grande do Sul. Lideranças municipais tratam o projeto como prioridade de desenvolvimento para toda a região, pelo potencial de gerar empregos e movimentar a cadeia florestal no entorno de Porto Alegre. Projetos desse porte costumam ter efeito em toda a economia local, da indústria aos serviços.",
            "fechamento_8s": "Desenvolvimento e empregos em pauta.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental corporativo leve"
        },
        "tag_thumbnail": "CMPC Celulose",
        "briefing_visual": {
            "descricao_pt": "Vista de complexo industrial de celulose às margens de rio no Rio Grande do Sul, plantio de eucalipto ao fundo, dia claro, sem pessoas",
            "query_en": ["pulp mill industrial complex river", "eucalyptus plantation aerial brazil", "cellulose factory landscape"],
            "evitar": ["pessoas com rosto visível", "marcas", "texto legível", "logos"],
            "prompt_ia": "Wide view of a pulp and cellulose industrial complex by a river in southern Brazil with eucalyptus plantations in the background, clear daylight, no people, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato econômico relevante e regional (investimento industrial da cadeia florestal no RS) — angulado em desenvolvimento e empregos, sem viés partidário",
    },

    # 3. O Sul — "Leilão, solidariedade e saúde" (coluna agregada) — REBAIXAR
    "0ec2064243d7c1deb11f976d3ae2911dbdd54a51": {
        "titulo_sultv": "", "chamada_faixa": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Título 'Leilão, solidariedade e saúde' é cabeçalho de coluna que agrega vários assuntos (leilão de cabanha + solidariedade + saúde) — sem fato único ancorável",
    },

    # 4. O Sul — Anne Hathaway efeito lifting — BLOQUEAR (celebridade internacional)
    "c3096bf0a43f59f9f0aad833f831d500b74a0461": {
        "titulo_sultv": "", "chamada_faixa": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "BLOQUEAR",
        "decisao_motivo": "Celebridade internacional / beleza, fora da linha editorial agro-regional do Radar e sem âncora no Sul do RS",
    },

    # 5. Folha do Mate — Venâncio vacinação contra gripe — PUBLICAR (serviço público / utilidade)
    "4a04dc6a81f6558b8e21fc0f740cc807018c8c4f": {
        "titulo_sultv": "Venâncio Aires abre vacinação contra a gripe para toda a população nesta segunda-feira",
        "chamada_faixa": "Venâncio abre vacina da gripe para todos",
        "subtitulo": "Município amplia a cobertura vacinal diante do aumento de casos de síndrome respiratória grave.",
        "lead": "Venâncio Aires liberou, a partir desta segunda-feira, a vacinação contra a gripe para toda a população. A medida amplia o público que pode se imunizar e busca elevar a cobertura vacinal no município diante do aumento de casos de síndrome respiratória grave registrado na região.",
        "ganchos_3": [
            "Vacinação liberada para todas as idades",
            "Resposta ao aumento de casos respiratórios",
            "Imunização disponível a partir desta segunda"
        ],
        "angulo_editorial": "Serviço público de saúde / utilidade imediata — informação prática sobre uma campanha de vacinação aberta a todos, com interesse direto para a população. Não é orientação médica individual.",
        "fontes_complementares_sugeridas": ["Secretaria Municipal de Saúde de Venâncio Aires", "Prefeitura de Venâncio Aires"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Venâncio Aires liberou a vacinação contra a gripe para toda a população a partir desta segunda-feira. A medida amplia quem pode se imunizar e busca aumentar a cobertura vacinal diante do crescimento de casos de síndrome respiratória grave na região. Procure a unidade de saúde mais próxima e mantenha a vacina em dia.",
            "hashtags": ["#VenâncioAires", "#Vacinação", "#Gripe", "#Saúde", "#ServiçoPúblico", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Vacina da gripe liberada.",
            "desenvolvimento_45s": "Venâncio Aires liberou, a partir desta segunda-feira, a vacinação contra a gripe para toda a população. Antes restrita a grupos prioritários, a imunização agora está disponível para todas as idades. A medida busca ampliar a cobertura vacinal diante do aumento de casos de síndrome respiratória grave na região. Quem ainda não se vacinou deve procurar a unidade de saúde mais próxima e conferir os horários de atendimento.",
            "fechamento_8s": "Imunização aberta a todos.",
            "cta_5s": "Mais informações no SulTV.",
            "trilha_sugerida": "instrumental informativo"
        },
        "tag_thumbnail": "Vacina da gripe",
        "briefing_visual": {
            "descricao_pt": "Frascos e seringa de vacina sobre bancada de unidade de saúde, ambiente clínico limpo, sem pessoas nem rostos, foco editorial",
            "query_en": ["flu vaccine vial syringe", "vaccination clinic table", "influenza immunization supplies"],
            "evitar": ["rostos identificáveis", "menores", "marcas de fabricante", "texto legível"],
            "prompt_ia": "Close-up of flu vaccine vials and a syringe on a clean health clinic counter, soft clinical lighting, no people, no readable brand text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Serviço público de saúde com utilidade imediata e fato concreto (campanha aberta hoje) em cidade do RS — utilidade pública, não orientação médica individual",
    },

    # 6. Folha do Mate — Assespe x River Plate (Copa Serrana, futebol amador) — REBAIXAR
    "3819e7ad0e414ee6d723a3a8de4a5bc2d611a07d": {
        "titulo_sultv": "", "chamada_faixa": "", "subtitulo": "", "lead": "", "ganchos_3": [],
        "angulo_editorial": "", "fontes_complementares_sugeridas": [],
        "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
        "tag_thumbnail": "",
        "decisao_final": "REBAIXAR",
        "decisao_motivo": "Esporte amador local (Copa Serrana, Venâncio Aires) — baixo interesse para a audiência estadual de TV aberta; fora do núcleo/Costa Doce",
    },

    # 7. Serranossa/Diário do Aço — BR-470 Serra das Antas (DNIT) — PUBLICAR (infraestrutura)
    "5cc1ebae70367c91ef88eca6b5c71461a80bc6a5": {
        "titulo_sultv": "DNIT afirma que obra da BR-470 na Serra das Antas está 80% concluída e sem risco de parar",
        "chamada_faixa": "BR-470 na Serra das Antas tem 80% de obra",
        "subtitulo": "Departamento garante que todos os contratos da reconstrução entre Bento Gonçalves e Veranópolis seguem ativos.",
        "lead": "O DNIT informou que a reconstrução da BR-470 na Serra das Antas, entre Bento Gonçalves e Veranópolis, está 80% concluída e segue sem risco de paralisação. Segundo a autarquia federal, todos os contratos das obras permanecem ativos, afastando temores sobre a interrupção de uma das principais ligações rodoviárias da Serra gaúcha.",
        "ganchos_3": [
            "Obra da BR-470 já está 80% concluída",
            "DNIT garante contratos ativos e sem paralisação",
            "Ligação estratégica da Serra gaúcha"
        ],
        "angulo_editorial": "Infraestrutura e mobilidade no RS — fato concreto e oficial (DNIT) sobre o andamento de uma rodovia estratégica para o escoamento e a circulação na Serra. Pauta de infraestrutura/trânsito.",
        "fontes_complementares_sugeridas": ["DNIT", "Governo do RS — Secretaria de Logística e Transportes"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "O DNIT informou que a reconstrução da BR-470 na Serra das Antas, entre Bento Gonçalves e Veranópolis, está 80% concluída e segue sem risco de paralisação. Todos os contratos das obras seguem ativos, afastando temores sobre a interrupção de uma das principais ligações rodoviárias da Serra gaúcha.",
            "hashtags": ["#BR470", "#SerraDasAntas", "#Infraestrutura", "#RioGrandeDoSul", "#DNIT", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "BR-470 a 80% da obra.",
            "desenvolvimento_45s": "O DNIT informou que a reconstrução da BR-470 na Serra das Antas, entre Bento Gonçalves e Veranópolis, está 80% concluída e segue sem risco de paralisação. Segundo a autarquia federal, todos os contratos das obras permanecem ativos. A rodovia é uma das principais ligações da Serra gaúcha e a conclusão dos trabalhos é aguardada por motoristas e pelo setor produtivo, que dependem da via para o transporte de cargas e pessoas.",
            "fechamento_8s": "Contratos ativos, obra a todo vapor.",
            "cta_5s": "Acompanhe no SulTV.",
            "trilha_sugerida": "instrumental neutro"
        },
        "tag_thumbnail": "BR-470 Serra das Antas",
        "briefing_visual": {
            "descricao_pt": "Obra de reconstrução de rodovia em região serrana do Sul do Brasil, máquinas e trecho de pista nova entre montanhas, dia claro, sem rostos",
            "query_en": ["highway construction mountains brazil", "road reconstruction machinery valley", "mountain road works"],
            "evitar": ["rostos identificáveis", "marcas", "placas legíveis", "logos"],
            "prompt_ia": "Highway reconstruction works winding through a mountainous region of southern Brazil, machinery and a stretch of new pavement between green slopes, clear daylight, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Fato oficial e concreto (DNIT) sobre rodovia estratégica do RS — infraestrutura e mobilidade de interesse estadual",
    },

    # 8. Serranossa/Diário do Aço — Evento longevidade Tacchini/Bento+20 — PUBLICAR (evento regional)
    "6bcc9a942c255c7b0742fab9cb38ce0dacbacf55": {
        "titulo_sultv": "Bento Gonçalves recebe evento sobre longevidade com documentário e o médico Yukio Moriguchi em 24 de junho",
        "chamada_faixa": "Bento debate longevidade em evento dia 24",
        "subtitulo": "Tacchini Saúde e Bento+20 promovem encontro gratuito sobre qualidade de vida e envelhecimento saudável no CIC-BG.",
        "lead": "Bento Gonçalves vai sediar, no dia 24 de junho, um evento dedicado à longevidade e ao envelhecimento saudável, promovido pelo Tacchini Saúde e pelo movimento Bento+20. O encontro, marcado para as 19h no CIC-BG, terá exibição de documentário e palestra do médico Yukio Moriguchi, referência nacional em estudos sobre o tema.",
        "ganchos_3": [
            "Documentário e palestra sobre envelhecimento saudável",
            "Referência nacional em longevidade na programação",
            "Evento gratuito no CIC-BG em 24 de junho"
        ],
        "angulo_editorial": "Evento de comunidade e qualidade de vida no RS — agenda cultural/educativa concreta com data e local definidos. Pauta de evento, não de orientação médica.",
        "fontes_complementares_sugeridas": ["Tacchini Saúde", "Bento+20", "Prefeitura de Bento Gonçalves"],
        "lead_materia_longa": "",
        "post_instagram": {
            "caption": "Bento Gonçalves recebe no dia 24 de junho um evento dedicado à longevidade e ao envelhecimento saudável, promovido pelo Tacchini Saúde e pelo Bento+20. A partir das 19h, no CIC-BG, o encontro terá exibição de documentário e palestra do médico Yukio Moriguchi, referência nacional no tema. Uma boa oportunidade para refletir sobre qualidade de vida.",
            "hashtags": ["#BentoGonçalves", "#Longevidade", "#QualidadeDeVida", "#Evento", "#RioGrandeDoSul", "#SulTV"]
        },
        "roteiro_short_60s": {
            "abertura_2s": "Longevidade em pauta em Bento.",
            "desenvolvimento_45s": "Bento Gonçalves vai sediar, no dia 24 de junho, um evento dedicado à longevidade e ao envelhecimento saudável, promovido pelo Tacchini Saúde e pelo movimento Bento+20. O encontro, às 19h no CIC-BG, terá exibição de documentário e palestra do médico Yukio Moriguchi, referência nacional no estudo do envelhecimento. A entrada é uma oportunidade para a comunidade refletir sobre hábitos e qualidade de vida ao longo dos anos.",
            "fechamento_8s": "Dia 24 de junho, às 19h, no CIC-BG.",
            "cta_5s": "Agenda no SulTV.",
            "trilha_sugerida": "instrumental inspirador leve"
        },
        "tag_thumbnail": "Longevidade em Bento",
        "briefing_visual": {
            "descricao_pt": "Plateia de auditório durante palestra em centro de eventos no Sul do Brasil, vista de trás, sem rostos identificáveis, iluminação de palco",
            "query_en": ["conference audience auditorium back view", "lecture event hall stage", "seminar audience silhouette"],
            "evitar": ["rostos identificáveis", "marcas", "texto legível", "logos"],
            "prompt_ia": "Auditorium audience seen from behind during a lecture at an events center in southern Brazil, warm stage lighting, no identifiable faces, no text, editorial photojournalism style"
        },
        "decisao_final": "PUBLICAR",
        "decisao_motivo": "Evento regional concreto (data, hora e local definidos) sobre qualidade de vida no RS — agenda de comunidade, sem orientação médica individual",
    },
}


MATERIAS: dict[str, str] = {}  # nenhuma matéria longa hoje (todos post_instagram)


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
        if h not in PAUTA_ANGULADA:
            print(f"[angular] sem angulação para {h} — bloqueando")
            angul = {
                "titulo_sultv": item.get("titulo", "")[:100],
                "chamada_faixa": "", "subtitulo": "", "lead": "", "ganchos_3": [],
                "angulo_editorial": "", "fontes_complementares_sugeridas": [],
                "lead_materia_longa": "", "post_instagram": {}, "roteiro_short_60s": {},
                "tag_thumbnail": "",
                "decisao_final": "BLOQUEAR",
                "decisao_motivo": "Sem angulação configurada — descartado pelo guardrail",
            }
        else:
            angul = PAUTA_ANGULADA[h]

        if angul["decisao_final"] == "PUBLICAR" and pub_count >= 10:
            angul = {**angul, "decisao_final": "REBAIXAR", "decisao_motivo": "Quota diária esgotada"}
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

    from collections import Counter
    print("[angular] decisões:", Counter(p["decisao_final"] for p in pauta))

    materias_dir.mkdir(exist_ok=True)
    nwrite = 0
    for p in pauta:
        if p["decisao_final"] == "PUBLICAR" and p.get("formato_sugerido") == "materia_longa":
            corpo = MATERIAS.get(p["id_hash"])
            if corpo:
                (materias_dir / f"{p['id_hash']}.md").write_text(corpo, encoding="utf-8")
                nwrite += 1
    print(f"[angular] {nwrite} matérias longas escritas (0 esperado hoje)")


if __name__ == "__main__":
    main()
