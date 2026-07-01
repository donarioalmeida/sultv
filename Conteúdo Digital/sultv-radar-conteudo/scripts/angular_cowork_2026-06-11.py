# -*- coding: utf-8 -*-
"""Angulação editorial Cowork — 2026-06-11. Gerado pelo Claude na sessão."""
import json, os
from datetime import datetime, timezone

HOJE = "2026-06-11"
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APROV = os.path.join(BASE, "state", f"aprovadas_{HOJE}.json")
OUT_PAUTA = os.path.join(BASE, "state", f"pauta_{HOJE}.json")
OUT_DIR = os.path.join(BASE, "state", f"materias_{HOJE}")
os.makedirs(OUT_DIR, exist_ok=True)

d = json.load(open(APROV))
items = d if isinstance(d, list) else d.get("aprovadas", d.get("itens", []))

# decisões por índice
A = {}

A[0] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Serviço de saúde concreto em cidade-núcleo, fonte com fato verificável.",
    titulo_sultv="Camaquã leva atendimento multiprofissional de saúde a sete UBSs",
    subtitulo="Nutricionista, psicóloga, farmacêutica e assistente social atendem nas unidades básicas nos próximos meses",
    lead="Sete unidades básicas de saúde de Camaquã passam a contar com atendimentos de uma equipe multiprofissional nos próximos meses.",
    chamada_faixa="SAÚDE REFORÇADA NAS UBSS DE CAMAQUÃ",
    ganchos_3=["Sete UBSs contempladas no cronograma", "Quatro especialidades na equipe eMulti", "Atendimento gratuito pela rede municipal"],
    angulo_editorial="Serviço ao morador de Camaquã: onde e como acessar o atendimento ampliado da rede municipal de saúde.",
    fontes_complementares_sugeridas=["Secretaria Municipal de Saúde de Camaquã"],
    lead_materia_longa="Sete unidades básicas de saúde de Camaquã recebem, ao longo dos próximos meses, atendimentos de uma equipe multiprofissional formada por nutricionista, psicóloga, farmacêutica e assistente social.",
    post_instagram=dict(caption="Camaquã amplia o atendimento nas UBSs: equipe multiprofissional com nutricionista, psicóloga, farmacêutica e assistente social percorre sete unidades nos próximos meses. Informações na unidade de saúde mais próxima.", hashtags=["camaqua", "saude", "costadoce", "sultv", "riograndedosul"]),
    roteiro_short_60s=dict(abertura_2s="Sete UBSs de Camaquã com atendimento reforçado", desenvolvimento_45s="Equipe eMulti com nutricionista, psicóloga, farmacêutica e assistente social atende na rede municipal nos próximos meses, com cronograma por unidade.", fechamento_8s="O serviço é gratuito e vale para toda a comunidade.", cta_5s="Acompanhe a SulTV para mais informações da Costa Doce.", trilha_sugerida="institucional leve"),
    tag_thumbnail="SAÚDE",
    briefing_visual=dict(
        descricao_pt="Fachada ou recepção de posto de saúde municipal brasileiro, ambiente claro, sem pessoas identificáveis",
        query_en=["community health clinic brazil", "public health center reception", "doctor office waiting room"],
        evitar=["rostos identificáveis", "pacientes", "logos", "texto"],
        prompt_ia="Bright community health clinic reception in a small Brazilian town, clean and welcoming, no people, no text, editorial photojournalism style",
    ),
)

A[1] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Fato econômico forte em cidade-núcleo: R$ 3 mi na agricultura familiar.",
    titulo_sultv="Operação Terra Forte injeta R$ 3 milhões na agricultura familiar de Camaquã",
    subtitulo="Primeiros cartões foram entregues a 14 famílias; 100 propriedades do município foram contempladas",
    lead="Cem propriedades rurais de Camaquã foram contempladas pela Operação Terra Forte, programa estadual que deve movimentar cerca de R$ 3 milhões na economia local.",
    chamada_faixa="R$ 3 MILHÕES NO CAMPO DE CAMAQUÃ",
    ganchos_3=["14 famílias receberam os primeiros cartões", "Até R$ 30 mil por propriedade", "Resposta às enchentes de 2024"],
    angulo_editorial="Dinheiro novo na agricultura familiar da Costa Doce: quem recebe, quanto e para quê.",
    fontes_complementares_sugeridas=["Secretaria de Desenvolvimento Rural de Camaquã", "Emater-RS", "Banrisul"],
    lead_materia_longa="Cem propriedades rurais de Camaquã foram contempladas pela Operação Terra Forte, programa do Governo do Estado que deve movimentar cerca de R$ 3 milhões na economia local até 2026.",
    post_instagram=dict(caption="A agricultura familiar de Camaquã recebeu os primeiros cartões da Operação Terra Forte. São 100 propriedades contempladas, com até R$ 30 mil por família — cerca de R$ 3 milhões movimentando o meio rural do município.", hashtags=["camaqua", "agriculturafamiliar", "agro", "costadoce", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="R$ 3 milhões chegando ao campo de Camaquã", desenvolvimento_45s="A Operação Terra Forte entregou os primeiros cartões a 14 famílias. Ao todo, 100 propriedades do município vão receber até R$ 30 mil cada para recuperar áreas produtivas e se preparar para eventos climáticos extremos.", fechamento_8s="O programa nasceu após as enchentes de 2024.", cta_5s="Siga a SulTV para acompanhar o agro da Costa Doce.", trilha_sugerida="dinâmica otimista"),
    tag_thumbnail="AGRO",
    briefing_visual=dict(
        descricao_pt="Pequena propriedade rural no Sul do RS com lavoura e galpão, luz de fim de tarde, sem pessoas",
        query_en=["family farm southern brazil", "small farm field sunset", "rural property crops brazil"],
        evitar=["rostos", "marcas", "texto", "logos"],
        prompt_ia="Small family farm in southern Brazil with green fields and a wooden shed at golden hour, no people, no text, editorial photojournalism style",
    ),
)

A[2] = dict(decisao_final="REBAIXAR", decisao_motivo="Tema já publicado pela SulTV em edição anterior (Declaração Anual de Rebanho até 30/06) — duplicata editorial.")

A[3] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Fato concreto de qualificação profissional na região de cobertura.",
    titulo_sultv="Barão do Triunfo abre 50 vagas em cursos gratuitos de qualificação",
    subtitulo="Programa RS Qualificação – Recomeçar oferece certificado e possibilidade de bolsa permanência",
    lead="Cinquenta vagas em cursos gratuitos de qualificação profissional estão abertas em Barão do Triunfo pelo programa RS Qualificação – Recomeçar.",
    chamada_faixa="50 VAGAS GRATUITAS EM BARÃO DO TRIUNFO",
    ganchos_3=["50 vagas com certificado de conclusão", "Metade das vagas prioritárias para mulheres", "Possibilidade de bolsa permanência"],
    angulo_editorial="Oportunidade de emprego e renda: quem pode se inscrever e como funciona o programa estadual no município.",
    fontes_complementares_sugeridas=["Prefeitura de Barão do Triunfo", "Secretaria Estadual de Trabalho"],
    lead_materia_longa="Cinquenta vagas em cursos gratuitos de qualificação profissional estão abertas em Barão do Triunfo por meio do programa RS Qualificação – Recomeçar, parceria da prefeitura com o Governo do Estado.",
    post_instagram=dict(caption="Barão do Triunfo está com 50 vagas abertas em cursos gratuitos de qualificação profissional. Tem certificado, possibilidade de bolsa permanência e metade das vagas é prioritária para mulheres. Para quem tem 16 anos ou mais.", hashtags=["baraodotriunfo", "qualificacao", "emprego", "riograndedosul", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Curso gratuito com bolsa em Barão do Triunfo", desenvolvimento_45s="O RS Qualificação – Recomeçar abriu 50 vagas no município. Pode participar quem tem 16 anos ou mais, com prioridade para desempregados, inscritos no CadÚnico e mulheres, que ficam com metade das vagas.", fechamento_8s="Tem certificado e possibilidade de bolsa permanência.", cta_5s="Mais oportunidades da região na SulTV.", trilha_sugerida="institucional leve"),
    tag_thumbnail="EMPREGO",
    briefing_visual=dict(
        descricao_pt="Sala de aula de curso profissionalizante com cadernos e computadores, sem rostos identificáveis",
        query_en=["vocational training classroom", "adult education class hands", "job training workshop"],
        evitar=["rostos identificáveis", "logos", "texto legível"],
        prompt_ia="Vocational training classroom in Brazil with notebooks and computers, hands writing, no faces, no text, editorial photojournalism style",
    ),
)

A[4] = dict(decisao_final="BLOQUEAR", decisao_motivo="Duplicata: matéria de cursos em Arambaré já publicada (consta no histórico de publicações).")
A[5] = dict(decisao_final="BLOQUEAR", decisao_motivo="Pauta antiga (publicação de 19 de janeiro de 2026 no site da prefeitura) — sem fato novo.")
A[6] = dict(decisao_final="BLOQUEAR", decisao_motivo="Edital procedural de penalidade — sem valor editorial.")
A[7] = dict(decisao_final="BLOQUEAR", decisao_motivo="Edital procedural (abertura de prazo para requerimentos) — acompanhar desdobramento, não publicar edital.")
A[8] = dict(decisao_final="REBAIXAR", decisao_motivo="Aviso administrativo interno a servidores — vira nota interna, sem matéria.")

A[9] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Lei municipal de interesse público direto (bem-estar animal e saúde auditiva), com canais de denúncia.",
    titulo_sultv="Fogos com estampido são proibidos em Barra do Ribeiro; saiba como denunciar",
    subtitulo="Lei municipal protege crianças, idosos e animais do barulho excessivo dos fogos de artifício",
    lead="Soltar fogos de artifício com estampido é proibido em Barra do Ribeiro, conforme a Lei Municipal nº 2850/2025.",
    chamada_faixa="FOGOS COM ESTAMPIDO PROIBIDOS NA BARRA",
    ganchos_3=["Lei Municipal nº 2850/2025 em vigor", "Proteção a crianças, idosos e animais", "Denúncias pela Brigada Militar e Secretaria de Meio Ambiente"],
    angulo_editorial="Serviço e cidadania: o que a lei proíbe, por que existe e para quem ligar em caso de descumprimento.",
    fontes_complementares_sugeridas=["Prefeitura de Barra do Ribeiro", "Brigada Militar"],
    lead_materia_longa="Soltar fogos de artifício com estampido é proibido em Barra do Ribeiro. A regra está na Lei Municipal nº 2850/2025 e vale para todo o território do município.",
    post_instagram=dict(caption="Em Barra do Ribeiro, fogos de artifício com estampido são proibidos por lei municipal. A medida protege crianças, idosos e animais. Denúncias: Brigada Militar (51) 98526-5600 e Secretaria de Agricultura e Meio Ambiente (51) 99396-6335.", hashtags=["barradoribeiro", "bemestaranimal", "leimunicipal", "riograndedosul", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Fogos com estampido? Na Barra é proibido", desenvolvimento_45s="A Lei Municipal 2850/2025 proíbe fogos de artifício com barulho em Barra do Ribeiro. A regra protege crianças, idosos, pessoas sensíveis ao som e os animais. Quem flagrar pode denunciar à Brigada Militar ou à Secretaria de Agricultura e Meio Ambiente.", fechamento_8s="Anota os telefones na descrição.", cta_5s="SulTV, a TV da nossa região.", trilha_sugerida="neutra informativa"),
    tag_thumbnail="LEI MUNICIPAL",
    briefing_visual=dict(
        descricao_pt="Cachorro abrigado em casa olhando pela janela, ambiente doméstico, remetendo a proteção dos animais contra barulho",
        query_en=["dog hiding home window", "scared dog indoors", "pet at home calm"],
        evitar=["fogos explodindo glorificados", "rostos", "texto", "marcas"],
        prompt_ia="A dog resting safely indoors by a window in a cozy Brazilian home, soft light, no people, no text, editorial photojournalism style",
    ),
)

A[10] = dict(decisao_final="REBAIXAR", decisao_motivo="Aviso de audiência pública — registro em nota interna; sem corpo para matéria.")
A[11] = dict(decisao_final="BLOQUEAR", decisao_motivo="Comunicado procedural antigo (05/05) sobre emissor de notas fiscais.")

A[12] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Obra pública concreta em cidade-núcleo, com impacto no trânsito e cronograma de ruas.",
    titulo_sultv="Rua Camaquã, em Cristal, entra em preparação para obras de calçamento",
    subtitulo="Remoção de pedras perto do acesso ao Balneário antecede pavimentação e construção de calçada; outras seis vias estão na sequência",
    lead="A Rua Camaquã, em Cristal, está recebendo serviços de remoção de pedras nas proximidades do acesso ao Balneário, etapa que antecede as obras de calçamento da via.",
    chamada_faixa="CALÇAMENTO COMEÇA NA RUA CAMAQUÃ",
    ganchos_3=["Etapa prepara calçamento e calçada nova", "Máquinas no trecho exigem atenção no trânsito", "Mais seis vias entram na sequência"],
    angulo_editorial="Obra e trânsito: o que muda agora para quem circula na região do Balneário e quais ruas vêm a seguir.",
    fontes_complementares_sugeridas=["Prefeitura de Cristal"],
    lead_materia_longa="A Rua Camaquã, em Cristal, está recebendo serviços de remoção de pedras nas proximidades do acesso ao Balneário, etapa necessária para o início das obras de calçamento da via e construção de calçada.",
    post_instagram=dict(caption="Obras à vista em Cristal: a Rua Camaquã recebe remoção de pedras para o calçamento e a calçada nova. Atenção redobrada no trânsito perto do acesso ao Balneário. Na sequência: Garibaldi, Polônia, São Lourenço, Canguçu, Travessa Chuí e Final da Formosa.", hashtags=["cristal", "obras", "costadoce", "riograndedosul", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Calçamento chegando na Rua Camaquã, em Cristal", desenvolvimento_45s="A prefeitura começou a remoção de pedras perto do acesso ao Balneário, etapa que prepara o calçamento e a construção da calçada. Com máquinas e caminhões no trecho, a orientação é reduzir a velocidade e manter distância dos equipamentos.", fechamento_8s="Depois vêm Garibaldi, Polônia, São Lourenço, Canguçu, Travessa Chuí e Final da Formosa.", cta_5s="Acompanhe as obras da região na SulTV.", trilha_sugerida="neutra informativa"),
    tag_thumbnail="OBRAS",
    briefing_visual=dict(
        descricao_pt="Rua de cidade pequena do interior gaúcho em obras de calçamento, máquinas e pedras, sem pessoas identificáveis",
        query_en=["street paving works small town", "cobblestone road construction", "road machinery gravel street"],
        evitar=["rostos", "placas com texto legível", "marcas de empresas"],
        prompt_ia="Street paving construction in a small town in southern Brazil, machinery and stones on an unpaved road, no people, no text, editorial photojournalism style",
    ),
)

A[13] = dict(decisao_final="BLOQUEAR", decisao_motivo="Duplicata interna do item 14 (mesmo edital Aldir Blanc).")

A[14] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Prazo concreto (19/06) de edital cultural em cidade-núcleo, com orientação de autoridade municipal.",
    titulo_sultv="São Lourenço do Sul recebe inscrições do edital Aldir Blanc até 19 de junho",
    subtitulo="Assessora de Cultura orienta agentes culturais a preparar projetos e documentação para concorrer aos recursos",
    lead="Agentes culturais de São Lourenço do Sul têm até 19 de junho para se inscrever no edital da Política Nacional Aldir Blanc no município.",
    chamada_faixa="ALDIR BLANC: INSCRIÇÕES ATÉ 19 DE JUNHO",
    ganchos_3=["Prazo final em 19 de junho", "Recursos da Política Nacional Aldir Blanc", "Orientação para preparar documentação"],
    angulo_editorial="Prazo e oportunidade para a cena cultural lourenciana: quem pode concorrer e o que preparar.",
    fontes_complementares_sugeridas=["Assessoria de Cultura de São Lourenço do Sul"],
    lead_materia_longa="Agentes culturais de São Lourenço do Sul têm até 19 de junho para se inscrever no edital da Política Nacional Aldir Blanc (PNAB) no município.",
    post_instagram=dict(caption="Atenção, fazedores de cultura de São Lourenço do Sul: as inscrições do edital Aldir Blanc seguem abertas até 19 de junho. Hora de preparar o projeto e a documentação para concorrer aos recursos.", hashtags=["saolourencodosul", "cultura", "aldirblanc", "costadoce", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Edital Aldir Blanc aberto em São Lourenço do Sul", desenvolvimento_45s="As inscrições vão até 19 de junho. A orientação da Assessoria de Cultura é preparar desde já o projeto e a documentação para concorrer aos recursos da Política Nacional Aldir Blanc.", fechamento_8s="Não deixa para a última hora.", cta_5s="Cultura da região é na SulTV.", trilha_sugerida="leve cultural"),
    tag_thumbnail="CULTURA",
    briefing_visual=dict(
        descricao_pt="Palco ou instrumentos musicais em ambiente cultural, luz cênica, remetendo a produção cultural local",
        query_en=["stage lights theater empty", "acoustic guitar stage", "cultural event backstage"],
        evitar=["rostos identificáveis", "marcas", "texto"],
        prompt_ia="Empty small-town theater stage with warm spotlights and a guitar, evoking local culture in Brazil, no people, no text, editorial photojournalism style",
    ),
)

A[15] = dict(decisao_final="REBAIXAR", decisao_motivo="Conteúdo agregado/confuso (página índice, pauta de Lajeado fora da área-foco).")
A[16] = dict(decisao_final="REBAIXAR", decisao_motivo="Serviço de rotina (limpeza de canteiro) — registro em nota, sem matéria.")
A[17] = dict(decisao_final="BLOQUEAR", decisao_motivo="Pauta desatualizada (classificações divulgadas em 13 de maio).")
A[18] = dict(decisao_final="BLOQUEAR", decisao_motivo="Cabeçalho de seção capturado pelo scraper — não é matéria.")

A[19] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Tema de alto impacto para o produtor gaúcho: renegociação de dívidas e acesso ao crédito da próxima safra.",
    titulo_sultv="Produtores do RS pressionam por renegociação de dívidas no Senado",
    subtitulo="Setor teme ficar sem acesso ao crédito rural para a próxima safra caso a proposta não avance",
    lead="Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da renegociação de dívidas do agro no Senado.",
    chamada_faixa="DÍVIDAS DO AGRO: TENSÃO NO SENADO",
    ganchos_3=["Votação decisiva para o agro gaúcho", "Risco de travamento do crédito da próxima safra", "Sequência de quebras de safra e enchentes pesa nas contas"],
    angulo_editorial="O que está em jogo para o produtor da nossa região se a renegociação não for aprovada — crédito, plantio e fluxo de caixa.",
    fontes_complementares_sugeridas=["Farsul", "Federarroz", "Senadores da bancada gaúcha"],
    lead_materia_longa="Produtores rurais do Rio Grande do Sul acompanham com apreensão a tramitação da proposta de renegociação de dívidas do agro no Senado, com receio de ficar sem acesso ao crédito rural para a próxima safra.",
    post_instagram=dict(caption="O campo gaúcho está de olho em Brasília: a renegociação das dívidas do agro aguarda votação no Senado, e o receio dos produtores é ficar sem crédito para a próxima safra. Tema decisivo para quem planta no RS.", hashtags=["agro", "creditorural", "riograndedosul", "soja", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="O agro gaúcho não dorme tranquilo", desenvolvimento_45s="A renegociação das dívidas do setor aguarda votação no Senado. Depois de quebras de safra e enchentes, o produtor teme não conseguir crédito para plantar a próxima safra se a proposta não passar.", fechamento_8s="Decisão deve mexer com todo o campo do RS.", cta_5s="Acompanhe o agro na SulTV.", trilha_sugerida="tensão leve jornalística"),
    tag_thumbnail="AGRO",
    briefing_visual=dict(
        descricao_pt="Lavoura de soja no RS com céu carregado, trator ao fundo, clima de apreensão, sem pessoas",
        query_en=["soybean field cloudy sky", "tractor field storm brazil", "farm field dramatic clouds"],
        evitar=["rostos", "logos", "texto", "bandeiras partidárias"],
        prompt_ia="Wide soybean field in southern Brazil under heavy clouds with a distant tractor, tense mood, no people, no text, editorial photojournalism style",
    ),
)

A[20] = dict(decisao_final="REBAIXAR", decisao_motivo="Sem âncora regional Sul clara; pauta estadual difusa.")
A[21] = dict(decisao_final="REBAIXAR", decisao_motivo="Sem âncora regional Sul clara; pauta estadual difusa.")

A[22] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Marco de inovação/sustentabilidade no RS com relevância estadual — nota curta.",
    titulo_sultv="PUCRS se torna a única universidade Carbono Neutro do Brasil",
    subtitulo="Reconhecimento coloca instituição gaúcha na vanguarda da agenda climática no ensino superior",
    lead="A PUCRS, em Porto Alegre, é a única universidade do Brasil com a certificação de Carbono Neutro.",
    chamada_faixa="PUCRS É CARBONO NEUTRO — ÚNICA DO BRASIL",
    ganchos_3=["Única universidade do país com o selo", "RS na vanguarda da agenda climática", "Sinal para o mercado de carbono regional"],
    angulo_editorial="Inovação gaúcha em destaque: o que significa uma universidade carbono neutro e por que isso importa para o RS.",
    fontes_complementares_sugeridas=["PUCRS", "Tecnopuc"],
    lead_materia_longa="",
    post_instagram=dict(caption="Orgulho gaúcho: a PUCRS é a única universidade Carbono Neutro do Brasil. O reconhecimento coloca o RS na vanguarda da agenda climática no ensino superior.", hashtags=["pucrs", "carbononeutro", "inovacao", "portoalegre", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="A única universidade Carbono Neutro do Brasil é gaúcha", desenvolvimento_45s="A PUCRS, em Porto Alegre, alcançou a neutralidade de carbono — caso único entre as universidades do país, unindo gestão ambiental, energia e compensação de emissões.", fechamento_8s="RS na frente da agenda climática.", cta_5s="Inovação do Sul é na SulTV.", trilha_sugerida="moderna inspiradora"),
    tag_thumbnail="INOVAÇÃO",
    briefing_visual=dict(
        descricao_pt="Campus universitário arborizado com prédios modernos e vegetação, ar de sustentabilidade, sem pessoas em destaque",
        query_en=["green university campus trees", "modern campus building sustainability", "solar panels university"],
        evitar=["rostos", "logos de universidades", "texto"],
        prompt_ia="Modern university campus with abundant trees and green areas in Brazil, sustainability mood, no people, no text, editorial photojournalism style",
    ),
)

A[23] = dict(decisao_final="REBAIXAR", decisao_motivo="Conteúdo institucional/promocional; envolve parceiro (Tecnopuc) — sem fato regional direto.")
A[24] = dict(decisao_final="REBAIXAR", decisao_motivo="Pauta institucional fora da área-foco.")
A[25] = dict(decisao_final="REBAIXAR", decisao_motivo="Pauta institucional fora da área-foco.")
A[26] = dict(decisao_final="REBAIXAR", decisao_motivo="Campanha de vacinação — borda do guardrail de saúde; sem matéria.")

A[27] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Fato administrativo de interesse público (anulação de licitação do lixo).",
    titulo_sultv="Venâncio Aires anula licitação para contratar empresa de manejo do lixo",
    subtitulo="Decisão da prefeitura reabre o processo de contratação do serviço no município",
    lead="A Prefeitura de Venâncio Aires anulou a licitação para contratar a empresa responsável pelo manejo do lixo no município.",
    chamada_faixa="LICITAÇÃO DO LIXO ANULADA EM VENÂNCIO",
    ganchos_3=["Processo de contratação volta à estaca zero", "Serviço essencial em discussão", "Próximos passos da prefeitura"],
    angulo_editorial="Impacto direto no serviço essencial: o que muda para a coleta de lixo e quando sai novo processo.",
    fontes_complementares_sugeridas=["Prefeitura de Venâncio Aires"],
    lead_materia_longa="",
    post_instagram=dict(caption="A Prefeitura de Venâncio Aires anulou a licitação que contrataria a empresa de manejo do lixo no município. O processo de contratação do serviço deve ser refeito.", hashtags=["venancioaires", "lixo", "gestaopublica", "riograndedosul", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Licitação do lixo anulada em Venâncio Aires", desenvolvimento_45s="A prefeitura anulou o processo que contrataria a empresa de manejo do lixo. A contratação do serviço deve ser refeita, e a coleta segue sendo acompanhada pela comunidade.", fechamento_8s="A SulTV acompanha os próximos passos.", cta_5s="Siga a SulTV.", trilha_sugerida="neutra informativa"),
    tag_thumbnail="GESTÃO",
    briefing_visual=dict(
        descricao_pt="Caminhão de coleta de lixo em rua urbana brasileira, contêineres, sem pessoas identificáveis",
        query_en=["garbage truck city street", "waste collection bins urban", "trash containers street"],
        evitar=["rostos", "logos de empresas", "texto legível"],
        prompt_ia="Garbage collection truck on a Brazilian city street with waste bins, overcast day, no people, no text, editorial photojournalism style",
    ),
)

A[28] = dict(decisao_final="REBAIXAR", decisao_motivo="Coberto dentro do item do incêndio na ExpoBento (programação mantida) — evita duplicidade.")

A[29] = dict(
    decisao_final="PUBLICAR",
    decisao_motivo="Fato quente em evento de grande porte do RS; sem vítima identificada (guardrail ok).",
    titulo_sultv="Incêndio atinge Pavilhão B da ExpoBento e Fenavinho em Bento Gonçalves",
    subtitulo="Organização informou que a programação das feiras segue normalmente",
    lead="Um incêndio atingiu o Pavilhão B da ExpoBento e Fenavinho, em Bento Gonçalves; a programação das feiras foi mantida.",
    chamada_faixa="INCÊNDIO ATINGE PAVILHÃO DA EXPOBENTO",
    ganchos_3=["Fogo no Pavilhão B do parque de eventos", "Programação mantida pela organização", "Feiras seguem recebendo público"],
    angulo_editorial="O fato e o serviço: o que aconteceu no pavilhão e o que muda (ou não) para quem vai ao evento.",
    fontes_complementares_sugeridas=["Corpo de Bombeiros de Bento Gonçalves", "Organização da ExpoBento"],
    lead_materia_longa="",
    post_instagram=dict(caption="Um incêndio atingiu o Pavilhão B da ExpoBento e Fenavinho, em Bento Gonçalves. Segundo a organização, a programação das feiras segue normalmente.", hashtags=["bentogoncalves", "expobento", "fenavinho", "riograndedosul", "sultv"]),
    roteiro_short_60s=dict(abertura_2s="Incêndio no pavilhão da ExpoBento", desenvolvimento_45s="O fogo atingiu o Pavilhão B do parque de eventos em Bento Gonçalves. A organização informou que a programação da ExpoBento e da Fenavinho está mantida e o público segue sendo recebido.", fechamento_8s="A SulTV acompanha a apuração.", cta_5s="Siga a SulTV para atualizações.", trilha_sugerida="tensão leve jornalística"),
    tag_thumbnail="URGENTE",
    briefing_visual=dict(
        descricao_pt="Pavilhão de eventos de grande porte visto de fora, ângulo amplo, sem fogo explícito nem pessoas identificáveis",
        query_en=["exhibition pavilion exterior", "event center building wide", "fair pavilion entrance"],
        evitar=["chamas sensacionalistas", "rostos", "logos", "texto"],
        prompt_ia="Large exhibition pavilion exterior in southern Brazil, wide angle, overcast light, no people, no fire, no text, editorial photojournalism style",
    ),
)

pauta = []
for i, m in enumerate(items):
    base = dict(m)
    base["url_fonte"] = m.get("url")
    base.update(A.get(i, dict(decisao_final="REBAIXAR", decisao_motivo="Sem angulação prioritária no dia.")))
    pauta.append(base)

out = {"data": HOJE, "gerado_em": datetime.now(timezone.utc).isoformat(), "total": len(pauta), "pauta": pauta}
json.dump(out, open(OUT_PAUTA, "w"), ensure_ascii=False, indent=2)
pubs = [p for p in pauta if p["decisao_final"] == "PUBLICAR"]
print("pauta escrita:", OUT_PAUTA, "| total:", len(pauta), "| PUBLICAR:", len(pubs),
      "| REBAIXAR:", sum(1 for p in pauta if p["decisao_final"] == "REBAIXAR"),
      "| BLOQUEAR:", sum(1 for p in pauta if p["decisao_final"] == "BLOQUEAR"))
for p in pubs:
    print(" PUB:", p["formato_sugerido"], "|", p["titulo_sultv"])
