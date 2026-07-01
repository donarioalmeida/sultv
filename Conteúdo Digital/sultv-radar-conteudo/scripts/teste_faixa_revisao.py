#!/usr/bin/env python3
"""
teste_faixa_revisao.py — teste de REGRESSÃO da revisão da faixa-legenda.

Garante (Donário 2026-05-30) que toda publicação FB/IG sempre tenha:
  1. logo SulTV presente;
  2. chamada coerente (sem preposição/artigo pendurado no fim);
  3. texto centralizado.

Inclui como caso de regressão o bug real de 2026-05-30
("...PLACAS SOLARES DA"). Gera imagens em /tmp/faixa_revisao/ e sai com
código != 0 se algum caso reprovar na revisão.

Rodar:  PYTHONPATH=/tmp/pylibs_<uid> python3 scripts/teste_faixa_revisao.py
"""
import io
import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(__file__))
import imagens as IM


def _foto_fake(w=1080, h=1350):
    img = Image.new('RGB', (w, h), (60, 90, 120))
    d = ImageDraw.Draw(img)
    for y in range(h):
        d.line([(0, y), (w, y)], fill=(40 + y // 12, 80 + y // 20, 110 + y // 30))
    buf = io.BytesIO()
    img.save(buf, format='JPEG')
    return buf.getvalue()


CASOS = [
    'Camaquã aprova projeto de R$ 3,8 milhões',
    'Arambaré ganha novo centro de eventos',
    'Pelotas inaugura sistema de irrigação por sensores',
    'Escola de Venâncio Aires recebe placas solares da',  # regressão do bug 30/05
]


def main():
    os.makedirs('/tmp/faixa_revisao', exist_ok=True)
    falhas = 0
    for i, ch in enumerate(CASOS, 1):
        out = IM.aplicar_faixa_legenda(_foto_fake(), ch)  # função OFICIAL do pipeline
        p = f'/tmp/faixa_revisao/faixa_{i}.jpg'
        with open(p, 'wb') as f:
            f.write(out)

        chamada_lp = IM.sanitizar_chamada(ch)
        _, origem = IM._logo_para_faixa(60)
        draw = ImageDraw.Draw(Image.new('RGB', (1080, 1350)))
        linhas, _ = IM.auto_fit_lines(
            draw, chamada_lp.upper(), IM.find_font_bold(),
            int(1080 * 0.6), start_size=54, min_size=22, max_lines=2)
        ok, motivos = IM.revisar_faixa_legenda(chamada_lp, origem, linhas)
        status = 'PASS' if ok else 'FAIL'
        if not ok:
            falhas += 1
        print(f'[{status}] {p}')
        print(f'        original  : {ch!r}')
        print(f'        sanitizada: {chamada_lp!r}')
        print(f'        logo      : {origem}')
        if motivos:
            print(f'        motivos   : {motivos}')

    print(f'\nResumo: {len(CASOS) - falhas}/{len(CASOS)} casos PASS')
    sys.exit(1 if falhas else 0)


if __name__ == '__main__':
    main()
