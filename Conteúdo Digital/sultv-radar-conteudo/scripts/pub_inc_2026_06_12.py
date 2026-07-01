#!/usr/bin/env python3
"""
pub_inc_2026_06_04.py — publicador INCREMENTAL e resumível (cowork-faz-tudo).

Necessário porque o sandbox Cowork mata processos em background (--die-with-parent)
e cada chamada bash tem teto de 45s. Este driver publica em lotes pequenos,
com estado persistente, de forma idempotente:

  - Matérias: publicar_materia_com_texto() já deduplica via wix_dedup
    (historico_publicacoes.json). Re-rodar é seguro: já publicadas são puladas.
  - Posts FB/IG: NÃO têm dedup nativo. Este driver rastreia em
    state/social_posted_2026-06-12.json (id_hash -> resultado) e pula o que já saiu.

Uso:
  python3 pub_inc_2026_06_04.py materias --max 1     # publica 1 matéria pendente
  python3 pub_inc_2026_06_04.py posts    --max 2     # publica 2 posts pendentes
  python3 pub_inc_2026_06_04.py status               # mostra o que falta
"""
from __future__ import annotations
import os, sys, json
from dataclasses import fields
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
HOJE = "2026-06-12"


def _load_env_file():
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "'"):
            v = v[1:-1]
        if k and k not in os.environ:
            os.environ[k] = v


_load_env_file()

from curador import MateriaPronta
from produzir_materia import publicar_materia_com_texto
from publicar_post import publicar_post

PAUTA = ROOT / "state" / f"pauta_{HOJE}.json"
MATERIAS_DIR = ROOT / "state" / f"materias_{HOJE}"
SOCIAL_STATE = ROOT / "state" / f"social_posted_{HOJE}.json"
URLMAP_STATE = ROOT / "state" / f"url_por_hash_{HOJE}.json"
HIST = ROOT / "state" / "historico_publicacoes.json"


def _load_json(p, default):
    if Path(p).exists():
        try:
            return json.loads(Path(p).read_text(encoding="utf-8"))
        except Exception:
            return default
    return default


def _save_json(p, obj):
    Path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def _materias_objs():
    data = _load_json(PAUTA, {})
    pauta = data.get("pauta", [])
    valid = {f.name for f in fields(MateriaPronta)}
    return [MateriaPronta(**{k: v for k, v in d.items() if k in valid}) for d in pauta]


def _hist_today():
    """id_hash -> post_url de matérias registradas HOJE no histórico."""
    h = _load_json(HIST, {"publicacoes": []})
    out = {}
    for p in h.get("publicacoes", []):
        ts = p.get("publicado_em", "") or p.get("registrado_em", "") or ""
        if ts.startswith(HOJE):
            out[p["id_hash"]] = p.get("post_url", "")
    return out


def _hist_all_ids():
    h = _load_json(HIST, {"publicacoes": []})
    return {p["id_hash"] for p in h.get("publicacoes", [])}


def cmd_status():
    objs = _materias_objs()
    pub = [m for m in objs if m.decisao_final == "PUBLICAR"]
    mats = [m for m in pub if m.formato_sugerido in ("materia_longa", "nota_curta")]
    posts = [m for m in pub if m.formato_sugerido in ("post_instagram", "card_carrossel")]
    hist_ids = _hist_all_ids()
    social = _load_json(SOCIAL_STATE, {})
    print(f"=== STATUS {HOJE} ===")
    print(f"PUBLICAR total: {len(pub)} | matérias: {len(mats)} | posts standalone: {len(posts)}")
    print("--- matérias ---")
    for m in mats:
        st = "JÁ NO HIST (skip)" if m.id_hash in hist_ids else "PENDENTE"
        print(f"  [{st}] {m.id_hash[:8]} {m.titulo_sultv[:55]}")
    print("--- posts standalone ---")
    for m in posts:
        st = "POSTADO" if m.id_hash in social else "PENDENTE"
        print(f"  [{st}] {m.id_hash[:8]} {m.titulo_sultv[:55]}")
    # matérias de hoje a promover socialmente
    today_urls = {**_hist_today(), **_load_json(URLMAP_STATE, {})}
    print("--- promoção social de matérias publicadas HOJE ---")
    for m in mats:
        if m.id_hash in today_urls:
            st = "PROMOVIDO" if ("promo:" + m.id_hash) in social else "PENDENTE"
            print(f"  [{st}] {m.id_hash[:8]} -> {today_urls[m.id_hash]}")


def cmd_materias(maxn):
    objs = _materias_objs()
    mats = [m for m in objs if m.decisao_final == "PUBLICAR"
            and m.formato_sugerido in ("materia_longa", "nota_curta")]
    hist_ids = _hist_all_ids()
    urlmap = _load_json(URLMAP_STATE, {})
    done = 0
    for m in mats:
        if done >= maxn:
            break
        if m.id_hash in hist_ids:
            print(f"[skip-hist] {m.id_hash[:8]} já consta no histórico (Wix) — não republica")
            continue
        if m.id_hash in urlmap:
            print(f"[skip-feito] {m.id_hash[:8]} já publicada nesta sessão")
            continue
        md = MATERIAS_DIR / f"{m.id_hash}.md"
        if not md.exists():
            print(f"[erro] sem .md para {m.id_hash[:8]} — pulando")
            continue
        corpo = md.read_text(encoding="utf-8")
        print(f"[materia] publicando {m.id_hash[:8]} {m.titulo_sultv[:50]} ...")
        try:
            url = publicar_materia_com_texto(m, corpo)
        except Exception as e:
            print(f"[materia] ✗ falha {m.id_hash[:8]}: {e}")
            continue
        if url:
            if "/post/" in url or "sultv.com.br" in url:
                urlmap[m.id_hash] = url
                _save_json(URLMAP_STATE, urlmap)
            print(f"[materia] OK: {url}")
            done += 1
        else:
            print(f"[materia] sem URL retornada para {m.id_hash[:8]}")
    print(f"[materias] publicadas nesta chamada: {done}")


def cmd_posts(maxn):
    objs = _materias_objs()
    pub = [m for m in objs if m.decisao_final == "PUBLICAR"]
    posts_standalone = [m for m in pub if m.formato_sugerido in ("post_instagram", "card_carrossel")]
    mats = [m for m in pub if m.formato_sugerido in ("materia_longa", "nota_curta")]
    by_hash = {m.id_hash: m for m in objs}

    social = _load_json(SOCIAL_STATE, {})
    today_urls = {**_hist_today(), **_load_json(URLMAP_STATE, {})}
    done = 0

    # fila: (chave_estado, MateriaPronta, link_artigo)
    fila = []
    # 1) posts standalone (sem link de matéria)
    for m in posts_standalone:
        if m.id_hash not in social:
            fila.append((m.id_hash, m, ""))
    # 2) promoção social de matérias publicadas HOJE (link direto pro artigo)
    for m in mats:
        url = today_urls.get(m.id_hash)
        if url and ("promo:" + m.id_hash) not in social and getattr(m, "post_instagram", None):
            fila.append(("promo:" + m.id_hash, m, url))

    for chave, m, link in fila:
        if done >= maxn:
            break
        print(f"[post] publicando {chave} {m.titulo_sultv[:45]} (link={'sim' if link else 'não'}) ...")
        try:
            res = publicar_post(m, link_artigo=link)
        except Exception as e:
            print(f"[post] ✗ falha {chave}: {e}")
            continue
        if res:
            social[chave] = {"res": res, "titulo": m.titulo_sultv}
            _save_json(SOCIAL_STATE, social)
            print(f"[post] OK {chave}: {res}")
            done += 1
        else:
            print(f"[post] sem resultado para {chave}")
    print(f"[posts] publicados nesta chamada: {done}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    maxn = 1
    if "--max" in sys.argv:
        maxn = int(sys.argv[sys.argv.index("--max") + 1])
    if cmd == "materias":
        cmd_materias(maxn)
    elif cmd == "posts":
        cmd_posts(maxn)
    else:
        cmd_status()
