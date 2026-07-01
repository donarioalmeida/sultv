# -*- coding: utf-8 -*-
"""Wrapper rápido do pub_inc_2026_06_12: clampa timeouts HTTP da cascata de
imagem para caber no teto de 45s do bash Cowork. Uso:
  python3 pub_fast_2026_06_12.py materias --max 1
  python3 pub_fast_2026_06_12.py posts --max 1
  python3 pub_fast_2026_06_12.py status
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import buscar_imagem_limpa as _b

_orig = _b._http_get
_BLOQUEADOS = ("live.staticflickr.com", "staticflickr.com", "flickr.com")
def _fast_http_get(url, timeout=6, **kw):
    # staticflickr não responde no sandbox Cowork (2026-06-12) — pula direto
    if any(h in (url or "") for h in _BLOQUEADOS):
        return None
    return _orig(url, timeout=min(int(timeout or 6), 6), **kw)
_b._http_get = _fast_http_get
_b.TIMEOUT = 6

import importlib
pub = importlib.import_module("pub_inc_2026_06_12")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    maxn = 1
    if "--max" in sys.argv:
        maxn = int(sys.argv[sys.argv.index("--max") + 1])
    if cmd == "materias":
        pub.cmd_materias(maxn)
    elif cmd == "posts":
        pub.cmd_posts(maxn)
    else:
        pub.cmd_status()
