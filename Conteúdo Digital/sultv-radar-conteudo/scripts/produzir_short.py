"""
produzir_short.py — hook para sultv-shorts-diarios
====================================================
Recebe MateriaPronta com roteiro_short_60s já gerado pelo Sonnet
e dispara o pipeline existente de geração de Short.

Reaproveita scripts da skill sultv-shorts-diarios:
  - gerar_audio.py
  - gerar_cards.py
  - gerar_videos.py
  - upload_youtube.py (com dedup em 3 camadas e bloqueio de ASR)
"""
from __future__ import annotations
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

def _resolve_shorts_skill_path():
    # 1) override por env (.env)
    env = os.environ.get("SULTV_SHORTS_SKILL_DIR", "").strip()
    if env and os.path.isdir(env):
        return Path(env)
    # 2) cópia local vendored dentro do próprio projeto (PADRÃO no Mac local)
    project_root = Path(__file__).resolve().parent.parent
    vendored = project_root / "code" / "shorts_skill_scripts"
    if vendored.is_dir() and (vendored / "gerar_audio.py").is_file():
        return vendored
    # 3) procura na sessão Cowork ativa (sandbox /sessions/<X>/...)
    import glob
    for p in glob.glob("/sessions/*/mnt/.claude/skills/sultv-shorts-diarios/scripts"):
        if os.path.isdir(p):
            return Path(p)
    # 4) fallback final — /var/folders cache da Cowork (host macOS)
    for p in glob.glob("/var/folders/*/*/T/claude-hostloop-plugins/*/skills/sultv-shorts-diarios/scripts"):
        if os.path.isdir(p):
            return Path(p)
    # último recurso: vendored mesmo que ainda não exista (erro mais explícito que o antigo)
    return vendored


SHORTS_SKILL = _resolve_shorts_skill_path()


def produzir_short(m):
    """m: MateriaPronta com roteiro_short_60s preenchido."""
    if not m.roteiro_short_60s:
        print(f"[short] Sem roteiro para matéria {m.id_hash[:8]} — pulando")
        return None

    # Pasta de saída padrão SulTV — override via env SHORTS_OUT_DIR
    base = os.environ.get("SHORTS_OUT_DIR", "").strip()
    if not base:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        base = os.path.join(os.path.dirname(project_root), "Shorts")
    out_dir = Path(base) / datetime.now().strftime("%Y-%m-%d") / f"radar_{m.id_hash[:8]}"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Grava o briefing que sultv-shorts-diarios consome
    briefing = {
        "tipo": "radar_pauta",
        "titulo_sultv": m.titulo_sultv,
        "subtitulo": m.subtitulo,
        "tag_thumbnail": m.tag_thumbnail,
        "roteiro": m.roteiro_short_60s,
        "fonte_origem": {"nome": m.fonte_nome, "url": m.url, "cidade": m.cidade},
        "score_combinado": m.score_combinado,
        "tag_principal": m.tag_principal,
    }
    (out_dir / "briefing_radar.json").write_text(
        json.dumps(briefing, ensure_ascii=False, indent=2), encoding="utf-8")

    # Dispara o pipeline em etapas (compatível com timeout de 45s do sandbox)
    print(f"[short] Gerando Short para: {m.titulo_sultv}")
    try:
        # 1) gerar_short_radar.py — pipeline unificado (audio + card + video)
        #    Substitui as chamadas legadas a gerar_audio/gerar_cards/gerar_videos
        #    que eram daily-shorts (precos/clima) e quebravam ao receber --briefing.
        gerador = SHORTS_SKILL / "gerar_short_radar.py"
        if not gerador.is_file():
            # fallback de emergência — caso a vendored ainda não tenha sido atualizada
            gerador = Path(__file__).resolve().parent.parent / "code" / "shorts_skill_scripts" / "gerar_short_radar.py"
        subprocess.run(["python3", str(gerador),
                        "--briefing", str(out_dir / "briefing_radar.json"),
                        "--out", str(out_dir)], check=True, timeout=40)
        # 2) upload pra YouTube — usa o uploader específico do radar
        #    (upload_youtube.py legado é hardcoded pra precos/clima e não publica radar)
        uploader = SHORTS_SKILL / "upload_youtube_radar.py"
        if not uploader.is_file():
            uploader = Path(__file__).resolve().parent.parent / "code" / "shorts_skill_scripts" / "upload_youtube_radar.py"
        subprocess.run(["python3", str(uploader),
                        "--step", "upload", "--pasta", str(out_dir)],
                       check=True, timeout=40)
        # ASR poll precisa rodar depois (não bloqueia)
        return str(out_dir)
    except subprocess.TimeoutExpired:
        print(f"[short] Timeout em etapa — reexecute mesmo step que retoma do state")
        return None
    except subprocess.CalledProcessError as e:
        print(f"[short] FALHA: {e}")
        return None
