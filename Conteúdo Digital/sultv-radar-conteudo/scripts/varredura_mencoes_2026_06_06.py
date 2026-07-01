#!/usr/bin/env python3
"""varredura_mencoes_2026_06_06.py — varredura retroativa da regra 12 (sem menção
a veículos de comunicação) em TODOS os posts publicados do blog SulTV.

Modos:
  scan          — lista posts com menções (não altera nada), grava fila em state/
  fix --max N   — corrige N posts da fila: remove frases com menção nos nós de
                  PARAGRAPH, PATCH richContent + republish. Resumível.

Estratégia de correção: frase a frase. Remove apenas as FRASES que contêm padrão
de veículo (ex.: "Com informações do X."). Mantém imagens, captions e demais nós.
NÃO toca em nós CAPTION (créditos de foto) nem em títulos.
"""
from __future__ import annotations
import json, sys, os, re, copy
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parent.parent
HOJE = "2026-06-06"
FILA = ROOT / "state" / "varredura_mencoes_fila.json"

for raw in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
    line = raw.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

H = {"Authorization": os.environ["WIX_SITE_TOKEN"], "Content-Type": "application/json"}
if os.getenv("WIX_SITE_ID", "").strip():
    H["wix-site-id"] = os.environ["WIX_SITE_ID"].strip()
API = "https://www.wixapis.com/blog/v3"

# Padrões de menção a veículos (case-insensitive)
PADROES = [
    r"com informa[cç][oõ]es d",
    r"segundo informa[cç][oõ]es d",
    r"segundo (o|a) (portal|jornal|r[aá]dio|site|emissora)",
    r"em entrevista [aà]o? (r[aá]dio|programa|slr|portal|jornal)",
    r"reportagem d[oa] ",
    r"divulgad[oa] pel[oa] (portal|jornal|r[aá]dio|site)",
    r"\bmetsul\b", r"canal rural", r"\bclicr\b", r"clic camaqu[aã]",
    r"ac[uú]stica fm", r"r[aá]dio ga[uú]cha", r"ga[uú]cha atualidade",
    r"s[aã]o louren[cç]o reporter", r"\bslr r[aá]dio\b", r"serranossa",
    r"folha do mate", r"di[aá]rio da manh[aã]", r"di[aá]rio popular",
    r"zero hora", r"\bgzh\b", r"correio do povo", r"di[aá]rio do a[cç]o",
]
RX = [re.compile(p, re.IGNORECASE) for p in PADROES]

# Whitelist institucional: se a frase atribui a uma INSTITUIÇÃO primária e não
# nomeia nenhum veículo, NÃO é menção (regra 12 permite fontes primárias).
RX_INSTITUICAO = re.compile(
    r"administra[cç][aã]o municipal|prefeitura|secretaria|superintend[eê]ncia|"
    r"defesa civil|pol[ií]cia|corpo de bombeiros|bombeiros|emater|governo do estado|"
    r"minist[eé]rio|c[aâ]mara de vereadores|brigada militar|detran|daer|inmet|ibge",
    re.IGNORECASE)
RX_GENERICOS = [re.compile(p, re.IGNORECASE) for p in PADROES[:6]]
RX_NOMES = [re.compile(p, re.IGNORECASE) for p in PADROES[6:]]


def _texto_do_node(n):
    if n.get("type") != "PARAGRAPH":
        return ""
    return "".join(c.get("textData", {}).get("text", "")
                   for c in n.get("nodes", []) if c.get("type") == "TEXT")


def _tem_mencao(txt):
    # nome explícito de veículo -> menção, sempre
    if any(rx.search(txt) for rx in RX_NOMES):
        return True
    # padrão genérico ("segundo informações de...") só conta se NÃO houver
    # instituição primária na mesma frase (falso positivo corrigido 2026-06-06)
    if any(rx.search(txt) for rx in RX_GENERICOS):
        return not RX_INSTITUICAO.search(txt)
    return False


def _limpar_paragrafo(txt):
    """Remove apenas as frases com menção. Devolve (texto_limpo, frases_removidas)."""
    frases = re.split(r"(?<=[.!?])\s+", txt)
    mantidas, removidas = [], []
    for f in frases:
        (removidas if _tem_mencao(f) else mantidas).append(f)
    return " ".join(mantidas).strip(), removidas


def _todos_posts():
    posts, offset = [], 0
    while True:
        body = {"paging": {"limit": 100, "offset": offset}}
        r = requests.post(f"{API}/posts/query", headers=H, json=body, timeout=30)
        r.raise_for_status()
        lote = r.json().get("posts", [])
        posts.extend(lote)
        if len(lote) < 100:
            break
        offset += 100
    return posts


def cmd_scan():
    # Escopo: apenas posts publicados pelo Radar (historico_publicacoes.json).
    # O blog tem 1700+ posts de outras eras que NAO foram escritos pelo pipeline.
    hist = json.loads((ROOT / "state" / "historico_publicacoes.json").read_text(encoding="utf-8"))
    ids = [e.get("post_id_wix") for e in hist.get("publicacoes", []) if e.get("post_id_wix")]
    print(f"[scan] {len(ids)} posts do Radar no historico")
    fila = []
    for pid in ids:
        r = requests.get(f"{API}/draft-posts/{pid}", headers=H,
                         params={"fieldsets": "RICH_CONTENT"}, timeout=20)
        if r.status_code != 200:
            print(f"[scan] {pid[:8]} GET {r.status_code} — pulando")
            continue
        d = r.json().get("draftPost", {})
        achados = []
        for n in d.get("richContent", {}).get("nodes", []):
            t = _texto_do_node(n)
            if t and _tem_mencao(t):
                achados.append(t[:90])
        if achados:
            fila.append({"id": pid, "titulo": d.get("title", "")[:70],
                         "achados": achados, "status": "pendente"})
            print(f"[scan] MENCAO {pid[:8]} {d.get('title','')[:55]}")
    FILA.write_text(json.dumps({"gerado_em": HOJE, "fila": fila},
                    ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[scan] total com menção: {len(fila)} -> {FILA.name}")


def cmd_fix(maxn):
    data = json.loads(FILA.read_text(encoding="utf-8"))
    fila = data["fila"]
    done = 0
    for item in fila:
        if done >= maxn:
            break
        if item["status"] != "pendente":
            continue
        pid = item["id"]
        r = requests.get(f"{API}/draft-posts/{pid}", headers=H,
                         params={"fieldsets": "RICH_CONTENT"}, timeout=20)
        r.raise_for_status()
        d = r.json().get("draftPost", {})
        rc = copy.deepcopy(d.get("richContent", {}))
        mudou, removidas_total = False, []
        nodes_finais = []
        for n in rc.get("nodes", []):
            t = _texto_do_node(n)
            if t and _tem_mencao(t):
                limpo, removidas = _limpar_paragrafo(t)
                removidas_total.extend(removidas)
                if not limpo:
                    mudou = True
                    continue  # parágrafo era 100% menção — remove o nó
                # substitui o conteúdo do parágrafo por um TEXT único limpo
                n["nodes"] = [{"type": "TEXT", "id": "", "nodes": [],
                               "textData": {"text": limpo, "decorations": []}}]
                mudou = True
            nodes_finais.append(n)
        if not mudou:
            item["status"] = "sem_mudanca"
            continue
        rc["nodes"] = nodes_finais
        patch = {"draftPost": {"id": pid, "richContent": rc}}
        r = requests.patch(f"{API}/draft-posts/{pid}", headers=H, json=patch, timeout=30)
        r.raise_for_status()
        r = requests.post(f"{API}/draft-posts/{pid}/publish", headers=H, timeout=30)
        r.raise_for_status()
        item["status"] = "corrigido"
        item["frases_removidas"] = removidas_total
        done += 1
        print(f"[fix] OK {pid[:8]} {item['titulo'][:50]} (-{len(removidas_total)} frases)")
        FILA.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    pend = sum(1 for i in fila if i["status"] == "pendente")
    print(f"[fix] corrigidos nesta chamada: {done} | pendentes: {pend}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "scan"
    maxn = 3
    if "--max" in sys.argv:
        maxn = int(sys.argv[sys.argv.index("--max") + 1])
    if cmd == "fix":
        cmd_fix(maxn)
    else:
        cmd_scan()
