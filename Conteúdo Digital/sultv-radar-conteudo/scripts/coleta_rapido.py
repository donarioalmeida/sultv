#!/usr/bin/env python3
"""
coleta_rapido.py — coleta com tempo limite total e timeout curto por fonte.
Usado quando precisamos garantir que a coleta termine dentro de janela curta.
Salva brutos e candidatos no state, então sai.
"""
from __future__ import annotations
import os, sys, time, json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

# Carrega .env
for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#") or "=" not in line: continue
    k, v = line.split("=", 1)
    if v and v[0] in ('"', "'") and v[-1] == v[0]: v = v[1:-1]
    os.environ.setdefault(k.strip(), v.strip())

import coletor as cl
# Encurta timeouts por fonte
cl.TIMEOUT = 6
cl.MAX_WORKERS = 32

from dedup import dedup_pipeline_completo
from sheets_writer import ler_hashes_recentes
from guardrails import passa_stop_list

STATE_FILE = ROOT / "state" / "ultimo_run.json"
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

from datetime import datetime, timezone

def _log(stage, payload):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    with open(LOG_DIR / f"{today}.json", "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"ts": datetime.now(timezone.utc).isoformat(),
                             "stage": stage, **payload}, ensure_ascii=False) + "\n")

def _save_state(key, data):
    state = {}
    if STATE_FILE.exists(): state = json.loads(STATE_FILE.read_text())
    state[key] = data
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, default=str, indent=2))

def _load_state(key, default=None):
    if not STATE_FILE.exists(): return default
    return json.loads(STATE_FILE.read_text()).get(key, default)


# Coleta paralela com tempo limite TOTAL
def coletar_com_deadline(deadline_seg: int):
    fontes = cl.carregar_banco()
    out = []
    deadline = time.time() + deadline_seg
    with ThreadPoolExecutor(max_workers=cl.MAX_WORKERS) as ex:
        futures = {ex.submit(cl._dispatch, f): f for f in fontes}
        completed = 0
        for fut in as_completed(futures):
            if time.time() > deadline:
                # cancela o que sobrou
                for f in futures:
                    f.cancel()
                break
            try:
                out.extend(fut.result(timeout=max(0.1, deadline - time.time())))
                completed += 1
            except Exception:
                pass
    print(f"[coleta-rapido] {completed}/{len(fontes)} fontes concluídas em {time.time()-(deadline-deadline_seg):.1f}s, {len(out)} brutos", flush=True)
    return out


def main():
    deadline = int(os.environ.get("COLETA_DEADLINE", "20"))
    t0 = time.time()
    print(f"[coleta-rapido] Coletando com deadline={deadline}s, workers={cl.MAX_WORKERS}, timeout/fonte={cl.TIMEOUT}s", flush=True)
    brutos = coletar_com_deadline(deadline)
    _log("coleta", {"total_brutos": len(brutos)})
    _save_state("brutos", [b.__dict__ for b in brutos])

    # Dedup
    print("[coleta-rapido] Dedup...", flush=True)
    try:
        hashes = ler_hashes_recentes(horas=48)
    except Exception as e:
        print(f"[coleta-rapido] AVISO: Sheets indisponível ({e.__class__.__name__}). Usando hashes locais.", flush=True)
        prev = (_load_state("aprovadas", []) or []) + (_load_state("persistidas", []) or [])
        hashes = {d.get("id_hash") for d in prev if d.get("id_hash")}
    dedupados = dedup_pipeline_completo(brutos, hashes)
    _log("dedup", {"antes": len(brutos), "depois": len(dedupados)})

    candidatos = [it for it in dedupados if passa_stop_list(it.titulo + " " + it.resumo)]
    _save_state("candidatos", [it.__dict__ for it in candidatos])
    print(f"[coleta-rapido] {len(brutos)} brutos → {len(dedupados)} dedup → {len(candidatos)} candidatos. Total: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
