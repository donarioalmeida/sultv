"""
preflight.py — checagens de saúde antes do pipeline rodar
==========================================================
Hoje cobre:
  • saldo Anthropic (credit balance / key inválida / API fora do ar)

Se o saldo estiver zerado:
  • envia e-mail de ABORT para donario@donario.com via SMTP do .env
  • escreve uma linha em logs/preflight.json
  • retorna False — o main aborta o run sem publicar nada (evita matéria com
    fallback texto puro que entra no portal sem angulação editorial SulTV)
"""
from __future__ import annotations
import json
import os
import smtplib
import urllib.error
import urllib.request
from datetime import datetime, timezone
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)


def _log_preflight(payload: dict):
    f = LOG_DIR / "preflight.json"
    line = json.dumps(
        {"ts": datetime.now(timezone.utc).isoformat(), **payload},
        ensure_ascii=False,
    )
    with open(f, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def _enviar_email_abort(motivo: str, detalhe: str) -> None:
    """Envia um e-mail vermelho de ABORT — mesmo SMTP do relatório diário."""
    smtp_host = os.getenv("SMTP_HOST")
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")
    if not smtp_host or not smtp_user or not smtp_pass:
        print("[preflight] SMTP não configurado — não foi possível alertar por e-mail")
        return

    hoje = datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M UTC")
    html = f"""
    <html><body style="font-family:Arial,sans-serif;max-width:680px;margin:auto">
      <h2 style="color:#C62828">SulTV Radar — RUN ABORTADO</h2>
      <p style="font-size:15px"><strong>{motivo}</strong></p>
      <p style="color:#444">{detalhe}</p>
      <hr>
      <p style="color:#666;font-size:13px">
        O pipeline foi interrompido antes de qualquer publicação para evitar que
        matérias subam ao portal sem angulação editorial Sonnet.
      </p>
      <p style="color:#666;font-size:13px">
        <strong>Ação:</strong> recarregue créditos em
        <a href="https://console.anthropic.com/settings/billing">console.anthropic.com/settings/billing</a>
        ou ajuste a key e rode o pipeline manualmente:
        <code>python3 scripts/radar_main.py</code>
      </p>
      <p style="color:#999;font-size:12px">Detectado em {hoje}.</p>
    </body></html>
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "[ABORT] SulTV Radar — RUN ABORTADO (saldo Anthropic)"
    msg["From"] = f"SulTV Radar <{smtp_user}>"
    msg["To"] = "donario@donario.com"
    msg["Reply-To"] = smtp_user
    msg.attach(MIMEText(html, "html", "utf-8"))

    port = int(os.getenv("SMTP_PORT", "465"))
    try:
        if port == 587:
            with smtplib.SMTP(smtp_host, port) as s:
                s.starttls()
                s.login(smtp_user, smtp_pass)
                s.send_message(msg)
        else:
            with smtplib.SMTP_SSL(smtp_host, port) as s:
                s.login(smtp_user, smtp_pass)
                s.send_message(msg)
        print(f"[preflight] E-mail de ABORT enviado para donario@donario.com via {smtp_host}:{port}")
    except Exception as e:
        print(f"[preflight] FALHA ao enviar e-mail de ABORT: {e}")


def checar_creditos_anthropic(timeout: int = 15) -> tuple[bool, str]:
    """Pinga a Messages API com max_tokens=1 e captura especificamente o erro
    de saldo. Retorna (ok, detalhe).
    """
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        return False, "ANTHROPIC_API_KEY ausente do ambiente."

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        data=json.dumps(
            {
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 1,
                "messages": [{"role": "user", "content": "ping"}],
            }
        ).encode(),
    )
    try:
        urllib.request.urlopen(req, timeout=timeout).read()
        return True, "Saldo Anthropic ok (ping respondeu)."
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode()
        except Exception:
            body = ""
        if "credit balance is too low" in body.lower() or "credit_balance" in body.lower():
            return False, "Saldo Anthropic zerado - recarregue em console.anthropic.com/settings/billing"
        if e.code == 401:
            return False, "API key invalida ou revogada (HTTP 401)."
        return False, f"HTTP {e.code} ao pingar Anthropic: {body[:200]}"
    except Exception as e:
        # Sem internet, timeout, etc. - nao derrubamos o pipeline por isso.
        return True, f"Preflight inconclusivo ({e.__class__.__name__}: {e}) - seguindo o pipeline."


def preflight(send_email_on_fail: bool = True, require_anthropic: bool = False) -> bool:
    """Roda todas as checagens. Retorna True se o pipeline pode seguir.

    Modo padrão (require_anthropic=False) é o cowork-faz-tudo: o pipeline
    não usa a API Anthropic, então saldo zerado NÃO bloqueia o run — só loga
    aviso. Para o pipeline antigo (radar_main.py), passe require_anthropic=True.
    """
    ok, detalhe = checar_creditos_anthropic()
    _log_preflight({"check": "anthropic_credits", "ok": ok, "detalhe": detalhe})
    print(f"[preflight] Anthropic: {'OK' if ok else 'FAIL'} - {detalhe}")
    if not ok and require_anthropic:
        if send_email_on_fail:
            _enviar_email_abort("Saldo Anthropic insuficiente", detalhe)
        return False
    elif not ok:
        print(f"[preflight] (cowork-faz-tudo: saldo Anthropic não é mais bloqueante)")
    return True


if __name__ == "__main__":
    import sys
    require = "--require-anthropic" in sys.argv
    ok = preflight(require_anthropic=require)
    sys.exit(0 if ok else 2)
