"""
sheets_writer.py — persistência no Google Sheets master
========================================================
Spreadsheet: SULTV_RADAR_SPREADSHEET_ID (env var)

Abas esperadas:
  - Radar_Diario      — top 30 do dia (sobrescrito a cada manhã)
  - Radar_Historico   — append-only (acervo permanente)
  - Logs              — execuções e erros
"""
from __future__ import annotations
import json
import os
from datetime import datetime, timezone, timedelta

try:
    import gspread
    from google.oauth2.service_account import Credentials
except ImportError:
    gspread = None
    Credentials = None


def _resolve_sa_credentials():
    """
    Resolve credencial do service account em ordem de prioridade:
      1. GOOGLE_SERVICE_ACCOUNT_JSON_INLINE  — JSON serializado direto na env
      2. GOOGLE_SERVICE_ACCOUNT_JSON         — caminho absoluto OU relativo
                                               à raiz do projeto da skill
      3. Fallback: ./credentials/sa.json     — caminho convencional dentro do projeto
    """
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    inline = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON_INLINE", "").strip()
    if inline:
        info = json.loads(inline)
        return Credentials.from_service_account_info(info, scopes=SCOPES)

    raw_path = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip()
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    candidatos = []
    if raw_path:
        candidatos.append(raw_path)
        candidatos.append(os.path.join(project_root, raw_path))
    candidatos.append(os.path.join(project_root, "credentials", "sa.json"))

    for p in candidatos:
        if p and os.path.exists(p):
            return Credentials.from_service_account_file(p, scopes=SCOPES)

    raise FileNotFoundError(
        "Service account não encontrada. Defina GOOGLE_SERVICE_ACCOUNT_JSON_INLINE, "
        "ou aponte GOOGLE_SERVICE_ACCOUNT_JSON para um caminho válido, "
        "ou coloque o JSON em credentials/sa.json dentro da skill. "
        f"Caminhos testados: {candidatos}"
    )


def _client():
    if not gspread or not Credentials:
        raise RuntimeError("gspread/google-auth não instalados — pip install gspread google-auth")
    creds = _resolve_sa_credentials()
    return gspread.authorize(creds)


def _spreadsheet():
    sid = os.environ["SULTV_RADAR_SPREADSHEET_ID"]
    return _client().open_by_key(sid)


# ============================================================
# Schema de linha
# ============================================================
COLUNAS = [
    "data_run", "id_hash", "score_combinado", "bloco", "tag_principal",
    "fonte_nome", "cidade", "publicado_em", "url",
    "titulo_sultv", "subtitulo", "lead", "angulo_editorial",
    "formato_sugerido", "decisao_final", "decisao_motivo",
    "roteiro_short_json", "post_instagram_json", "card_carrossel_json",
    "tag_thumbnail",
]


def materia_to_row(m, data_run: str | None = None) -> list:
    return [
        data_run or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        m.id_hash, m.score_combinado, m.bloco, m.tag_principal,
        m.fonte_nome, m.cidade, m.publicado_em, m.url,
        getattr(m, "titulo_sultv", "") or m.titulo,
        getattr(m, "subtitulo", ""),
        getattr(m, "lead", ""),
        getattr(m, "angulo_editorial", ""),
        m.formato_sugerido, getattr(m, "decisao_final", ""), getattr(m, "decisao_motivo", ""),
        json.dumps(getattr(m, "roteiro_short_60s", {}), ensure_ascii=False),
        json.dumps(getattr(m, "post_instagram", {}), ensure_ascii=False),
        json.dumps(getattr(m, "card_carrossel", {}), ensure_ascii=False),
        getattr(m, "tag_thumbnail", ""),
    ]


def write_radar_diario(materias: list):
    """Sobrescreve a aba Radar_Diario com a pauta do dia."""
    ss = _spreadsheet()
    try:
        ws = ss.worksheet("Radar_Diario")
    except Exception:
        ws = ss.add_worksheet("Radar_Diario", rows=200, cols=len(COLUNAS))
    ws.clear()
    ws.update([COLUNAS] + [materia_to_row(m) for m in materias])


def write_historico(materias: list):
    """Append-only no Radar_Historico."""
    ss = _spreadsheet()
    try:
        ws = ss.worksheet("Radar_Historico")
    except Exception:
        ws = ss.add_worksheet("Radar_Historico", rows=10000, cols=len(COLUNAS))
        ws.update([COLUNAS])
    rows = [materia_to_row(m) for m in materias]
    ws.append_rows(rows, value_input_option="RAW")


def ler_hashes_recentes(horas: int = 48) -> set[str]:
    """Lê hashes do Radar_Historico nas últimas N horas."""
    ss = _spreadsheet()
    try:
        ws = ss.worksheet("Radar_Historico")
    except Exception:
        return set()
    rows = ws.get_all_records()
    cutoff = datetime.now(timezone.utc) - timedelta(hours=horas)
    out = set()
    for r in rows:
        try:
            d = datetime.fromisoformat(r["data_run"])
            if d.replace(tzinfo=timezone.utc) >= cutoff:
                out.add(r["id_hash"])
        except Exception:
            continue
    return out
