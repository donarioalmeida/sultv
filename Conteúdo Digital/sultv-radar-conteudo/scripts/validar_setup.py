#!/usr/bin/env python3
"""
validar_setup.py — checa toda credencial necessária para o radar rodar full.
Imprime um relatório verde/amarelo/vermelho por componente.
"""
from __future__ import annotations
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load_env():
    env_path = ROOT / ".env"
    if not env_path.exists():
        return {}
    out = {}
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if v and v[0] in ('"', "'") and v[-1] == v[0]:
            v = v[1:-1]
        out[k.strip()] = v.strip()
    return out

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def ok(msg): print(f"{GREEN}✓{RESET} {msg}")
def warn(msg): print(f"{YELLOW}!{RESET} {msg}")
def err(msg): print(f"{RED}✗{RESET} {msg}")

def is_placeholder(v, placeholders=("...", "your-", "EAAL", "ist1.ey", "pa-", "")):
    if not v: return True
    if any(p in v for p in placeholders) and len(v) < 30: return True
    if v.endswith("..."): return True
    if len(v) < 20: return True
    return False

def main():
    env = load_env()
    # popula os.environ com .env se ainda não estiver
    for k, v in env.items():
        os.environ.setdefault(k, v)

    print("=== SulTV Radar Setup Check ===\n")
    erros = 0

    # 1. Anthropic
    print("[1] Anthropic API")
    k = os.environ.get("ANTHROPIC_API_KEY", "")
    if k.startswith("sk-ant-") and len(k) > 50: ok("ANTHROPIC_API_KEY ok")
    else: err("ANTHROPIC_API_KEY ausente ou inválida"); erros += 1

    # 2. Voyage (opcional)
    print("\n[2] Voyage AI (opcional — fallback grava só por hash)")
    k = os.environ.get("VOYAGE_API_KEY", "")
    if k.startswith("pa-") and len(k) > 30: ok("VOYAGE_API_KEY ok")
    else: warn("VOYAGE_API_KEY placeholder — dedup vai usar só hash de URL")

    # 3. Google Service Account
    print("\n[3] Google Sheets (Service Account)")
    inline = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON_INLINE", "").strip()
    raw_path = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip()
    candidatos = []
    if raw_path:
        candidatos.append(raw_path)
        candidatos.append(str(ROOT / raw_path))
    candidatos.append(str(ROOT / "credentials" / "sa.json"))

    if inline:
        try:
            j = json.loads(inline)
            if "client_email" in j: ok(f"INLINE válido — {j['client_email']}")
            else: err("INLINE não tem client_email"); erros += 1
        except Exception as e:
            err(f"INLINE não é JSON válido: {e}"); erros += 1
    else:
        achou = False
        for p in candidatos:
            if p and os.path.exists(p):
                try:
                    j = json.loads(open(p).read())
                    ok(f"sa.json OK em {p} — {j.get('client_email','??')}")
                    achou = True
                    break
                except Exception as e:
                    err(f"sa.json em {p} corrompido: {e}"); erros += 1
        if not achou:
            err(f"Service account não encontrado. Tente: GOOGLE_SERVICE_ACCOUNT_JSON_INLINE, ou um destes paths: {candidatos}"); erros += 1

    # 4. Sheet ID
    print("\n[4] Google Sheet master")
    sid = os.environ.get("SULTV_RADAR_SPREADSHEET_ID", "")
    if len(sid) > 30: ok(f"SULTV_RADAR_SPREADSHEET_ID = {sid[:20]}…")
    else: err("SULTV_RADAR_SPREADSHEET_ID ausente"); erros += 1

    # 5. Wix
    print("\n[5] Wix Blog")
    t = os.environ.get("WIX_SITE_TOKEN", "")
    if not is_placeholder(t): ok("WIX_SITE_TOKEN ok")
    else: warn("WIX_SITE_TOKEN placeholder — matérias longas vão como draft local")

    # 6. Meta
    print("\n[6] Meta Graph API (Instagram + Facebook)")
    t = os.environ.get("META_LONG_LIVED_TOKEN", "")
    ig = os.environ.get("META_IG_BUSINESS_ID", "")
    fb = os.environ.get("META_FB_PAGE_ID", "")
    meta_ok = True
    if is_placeholder(t): warn("META_LONG_LIVED_TOKEN placeholder"); meta_ok = False
    else: ok("META_LONG_LIVED_TOKEN ok")
    if not ig.isdigit() or len(ig) < 10: warn("META_IG_BUSINESS_ID placeholder"); meta_ok = False
    else: ok(f"META_IG_BUSINESS_ID = {ig}")
    if not fb.isdigit() or len(fb) < 5: warn("META_FB_PAGE_ID placeholder"); meta_ok = False
    else: ok(f"META_FB_PAGE_ID = {fb}")
    if not meta_ok: warn("→ Posts IG/FB vão como draft local")

    # 7. SMTP
    print("\n[7] SMTP (relatório diário)")
    pwd = os.environ.get("SMTP_PASS", "")
    if pwd: ok(f"SMTP configurado (host={os.environ.get('SMTP_HOST','?')})")
    else: warn("SMTP_PASS vazio — relatório fica no Gmail Drafts via Cowork MCP")

    # Resumo
    print("\n=== Resumo ===")
    if erros == 0:
        print(f"{GREEN}Setup viável.{RESET} Componentes opcionais marcados em amarelo caem para fallback gracioso.")
    else:
        print(f"{RED}{erros} erro(s) crítico(s).{RESET} Veja SETUP_TOKENS.md.")
    return 0 if erros == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
