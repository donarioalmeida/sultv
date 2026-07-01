#!/usr/bin/env python3
"""
coleta_deadline.py — versão da coleta com deadline global rígido.

Usado pelo Cowork quando a infraestrutura tem timeout de 45s por chamada bash.
Roda as 167 fontes em paralelo (16 workers) e devolve o que conseguiu até o deadline.
Escreve state/candidatos_<date>.json no mesmo formato que cowork_pipeline.py espera.
"""
from __future__ import annotations
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

# Carrega .env minimal
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

import coletor  # noqa
# rede lenta; com feed_url validado os feeds reais resolvem rápido (Donário 2026-06-01)
coletor.TIMEOUT = int(os.environ.get("TIMEOUT_FONTE", "10"))
from coletor import _dispatch, carregar_banco  # noqa
from guardrails import passa_stop_list  # noqa

DEADLINE_S = int(os.environ.get("COLETA_DEADLINE_S", "30"))


def _hoje() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def main():
    inicio = time.time()
    fontes = carregar_banco()
    print(f"[coleta-deadline] {len(fontes)} fontes, deadline {DEADLINE_S}s")
    out = []
    completos = 0
    timeouts = 0

    ex = ThreadPoolExecutor(max_workers=32)
    futures = {ex.submit(_dispatch, f): f for f in fontes}
    deadline = inicio + DEADLINE_S
    try:
        for fut in as_completed(futures, timeout=DEADLINE_S):
            try:
                resultado = fut.result(timeout=1)
                out.extend(resultado)
                completos += 1
            except Exception:
                timeouts += 1
            if time.time() >= deadline:
                break
    except Exception as e:
        print(f"[coleta-deadline] timeout global atingido: {e}")
    # cancela tudo que sobrou, sem aguardar
    pendentes = 0
    for fut in futures:
        if not fut.done():
            fut.cancel()
            pendentes += 1
    timeouts += pendentes
    # NÃO chama ex.shutdown(wait=True) — vai sair com daemon threads ainda rodando
    print(f"[coleta-deadline] {pendentes} fontes pendentes, abandonando pool")
    ex.shutdown(wait=False)

    print(f"[coleta-deadline] {completos} fontes concluídas, {timeouts} timeout/canceled, {len(out)} brutos")

    # Stop list lexical
    filtrados = [it for it in out if passa_stop_list(it.titulo + " " + it.resumo)]
    print(f"[coleta-deadline] {len(filtrados)} após stop-list lexical")

    # Dedup local simples (por id_hash). Skip Voyage embeddings — não temos tempo.
    vistos = set()
    finais = []
    for it in filtrados:
        if it.id_hash in vistos:
            continue
        vistos.add(it.id_hash)
        finais.append(it)
    print(f"[coleta-deadline] {len(finais)} após dedup local")

    payload = {
        "data": _hoje(),
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "total": len(finais),
        "completos_fontes": completos,
        "timeouts_fontes": timeouts,
        "candidatos": [asdict(it) for it in finais],
    }
    out_path = ROOT / "state" / f"candidatos_{_hoje()}.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[coleta-deadline] -> {out_path}")
    print(f"[coleta-deadline] tempo: {time.time()-inicio:.1f}s")


if __name__ == "__main__":
    main()
