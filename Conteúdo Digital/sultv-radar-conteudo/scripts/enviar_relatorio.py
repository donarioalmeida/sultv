"""
enviar_relatorio.py — e-mail diário de status (08:05)
======================================================
Resume o run do dia em formato executivo para donario@donario.com.
"""
from __future__ import annotations
import os
import smtplib
from datetime import datetime, timezone
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def _build_html(persistidas: list) -> str:
    if isinstance(persistidas, list) and persistidas and isinstance(persistidas[0], dict):
        items = persistidas
    else:
        items = [m.__dict__ for m in persistidas]

    publicar = [m for m in items if m.get("decisao_final") == "PUBLICAR"]
    rebaixar = [m for m in items if m.get("decisao_final") == "REBAIXAR"]
    bloquear = [m for m in items if m.get("decisao_final") == "BLOQUEAR"]
    alerta = [m for m in items if m.get("decisao_final") == "ALERTA_HUMANO"]

    top5 = sorted(publicar, key=lambda x: -x.get("score_combinado", 0))[:5]

    rows = "".join(
        f"<tr><td>{m.get('score_combinado', 0):.1f}</td>"
        f"<td><strong>{m.get('titulo_sultv', m.get('titulo'))}</strong><br>"
        f"<small style='color:#666'>{m.get('fonte_nome')} · {m.get('cidade')}</small></td>"
        f"<td>{m.get('formato_sugerido', '')}</td></tr>"
        for m in top5
    )

    alerta_html = ""
    if alerta:
        alerta_html = "<h3 style='color:#C62828'>⚠️ Aguardam revisão humana:</h3><ul>" + "".join(
            f"<li><strong>{m.get('titulo_sultv', m.get('titulo'))}</strong> — {m.get('decisao_motivo')}</li>"
            for m in alerta
        ) + "</ul>"

    return f"""
    <html><body style="font-family:Arial,sans-serif;max-width:680px;margin:auto">
      <h2 style="color:#0F4C2C">SulTV Radar — {datetime.now(timezone.utc).strftime('%d/%m/%Y')}</h2>
      <p>Resumo do run das 06:00.</p>
      <table cellpadding="6" style="border-collapse:collapse">
        <tr><td>📥 Coletados (após dedup)</td><td><strong>{len(items)}</strong></td></tr>
        <tr><td>✅ Publicar</td><td><strong>{len(publicar)}</strong> de {os.getenv('QUOTA_DIARIA','10')}</td></tr>
        <tr><td>📋 Rebaixados (rascunho)</td><td>{len(rebaixar)}</td></tr>
        <tr><td>🚫 Bloqueados</td><td>{len(bloquear)}</td></tr>
        <tr><td>⚠️ Alerta humano</td><td>{len(alerta)}</td></tr>
      </table>
      <h3>Top 5 da pauta</h3>
      <table style="border-collapse:collapse;width:100%">
        <tr style="background:#F1F8E9"><th>Score</th><th>Matéria</th><th>Formato</th></tr>
        {rows}
      </table>
      {alerta_html}
      <p style="margin-top:24px;font-size:11px;color:#666">
        Pauta completa: <a href="https://docs.google.com/spreadsheets/d/{os.getenv('SULTV_RADAR_SPREADSHEET_ID','')}">Google Sheets</a><br>
        Dashboard live: artefato <code>sultv-radar-pauta-dia</code> no Cowork
      </p>
    </body></html>
    """


def enviar_relatorio_diario(persistidas: list):
    smtp_host = os.getenv("SMTP_HOST")
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")
    if not smtp_host:
        print("[relatorio] SMTP não configurado — pulando envio")
        return

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"SulTV Radar — pauta de {datetime.now(timezone.utc).strftime('%d/%m/%Y')}"
    # From com display name distinto reduz chance de cair em spam (self-send com From puro tende a ser flagrado)
    msg["From"] = f"SulTV Radar <{smtp_user}>"
    msg["To"] = "donario@donario.com"
    msg["Reply-To"] = smtp_user
    msg.attach(MIMEText(_build_html(persistidas), "html", "utf-8"))

    port = int(os.getenv("SMTP_PORT", "465"))
    try:
        if port == 587:
            # STARTTLS path (Network Solutions, Gmail, Outlook, etc.)
            with smtplib.SMTP(smtp_host, port) as s:
                s.starttls()
                s.login(smtp_user, smtp_pass)
                s.send_message(msg)
        else:
            # Implicit SSL (Fastmail :465, Network Solutions :465)
            with smtplib.SMTP_SSL(smtp_host, port) as s:
                s.login(smtp_user, smtp_pass)
                s.send_message(msg)
        print(f"[relatorio] Enviado para donario@donario.com via {smtp_host}:{port}")
    except Exception as e:
        print(f"[relatorio] FALHA: {e}")
