# -*- coding: utf-8 -*-
"""build_dossier_full.py - Dosier UNICO ampliado: 23 documentos + cuestionario (200 preguntas),
con portada, indice y marcadores PDF (bookmarks). Salida: PBM-dosier-completo-cuestionario.pdf"""
import re, importlib, pathlib, json, html as _html
from build_doc import CSS
from build_dossier import DOSSIER_CSS, ANCLA, MODULES_LABEL, IDEACION, ORDER, get_title

BASE = pathlib.Path(__file__).resolve().parent
LETTERS = ["A", "B", "C", "D"]

QUIZ_CSS = """
  .qz-q{ break-inside:avoid; margin:0 0 8px; padding:6px 10px; border:1px solid var(--line); border-left:4px solid var(--accent2); border-radius:0 5px 5px 0; }
  .qz-h{ font-family:"DejaVu Sans Mono",monospace; font-size:7pt; color:var(--muted); letter-spacing:.04em; }
  .qz-stem{ font-size:9pt; font-weight:600; color:var(--ink); margin:3px 0 5px; }
  .qz-opt{ font-size:8.4pt; margin:2px 0 2px 6px; }
  .qz-opt .L{ font-family:"DejaVu Sans Mono",monospace; font-weight:700; color:var(--accent2); margin-right:5px; }
  .sol{ break-inside:avoid; font-size:8pt; margin:0 0 5px; padding:5px 9px; border-left:3px solid var(--pearl); background:var(--pearl-bg); border-radius:0 4px 4px 0; }
  .sol .ans{ font-family:"DejaVu Sans Mono",monospace; font-weight:700; color:var(--accent); }
  .grid2{ columns:2; column-gap:18px; }
  .lvltag{ display:inline-block; font-family:"DejaVu Sans Mono",monospace; font-size:6.4pt; font-weight:700; padding:1px 5px; border-radius:8px; }
  .lvl-b{ background:#E7EDF1; color:#3A5563; } .lvl-a{ background:#F4E3E6; color:#8E2433; }
"""

def esc(s): return _html.escape(s, quote=False)

def build_quiz_unit():
    Q = json.load(open(BASE / "app-data" / "questions.json", encoding="utf-8"))
    cover = ('<h1 class="title">Cuestionario de evaluaci&oacute;n &mdash; 200 preguntas</h1>'
             '<div class="subtitle">Autoevaluaci&oacute;n tipo test sobre los 23 documentos, con soluciones razonadas y fuente (PMID)</div>'
             '<div class="tagline">Preguntas fundamentadas en la serie y verificadas contra PubMed &middot; B&aacute;sico / Avanzado &middot; CAUSA / SACYL</div>')
    exam = ['<h2 class="sec"><span class="num">A.</span>Examen (200 preguntas)</h2>']
    cur = None
    for i, q in enumerate(Q, 1):
        if q["doc"] != cur:
            cur = q["doc"]; exam.append(f'<h3 style="margin-top:9px">{esc(cur)}</h3>')
        lvl = 'lvl-a' if q["level"] == "avanzado" else 'lvl-b'
        opts = "".join(f'<div class="qz-opt"><span class="L">{LETTERS[j]}</span>{esc(o)}</div>' for j, o in enumerate(q["options"]))
        exam.append(f'<div class="qz-q"><span class="qz-h">{esc(q["id"])} &middot; {esc(q["doc"])} '
                    f'<span class="lvltag {lvl}">{q["level"].upper()}</span></span>'
                    f'<div class="qz-stem">{i}. {esc(q["q"])}</div>{opts}</div>')
    sols = ['<h2 class="sec"><span class="num">B.</span>Soluciones razonadas</h2><div class="grid2">']
    for i, q in enumerate(Q, 1):
        sols.append(f'<div class="sol"><b>{i}. {esc(q["id"])}</b> &mdash; Respuesta: <span class="ans">{LETTERS[q["answer"]]}</span>. '
                    f'{esc(q["explanation"])} <i>({esc(q["ref"])} &middot; {esc(q["doc"])})</i></div>')
    sols.append('</div>')
    footer = ("Cuestionario de la Serie PBM - 200 preguntas - 2026. Preguntas y soluciones fundamentadas en los 23 documentos, "
              "verificadas contra PubMed (CAUSA / SACYL). Material docente; no sustituye al juicio clinico ni a los protocolos locales vigentes.")
    return ('<div class="doc-unit">%s%s%s<div class="footer-note">%s<br>%s</div></div>'
            % (cover, "".join(exam), "".join(sols), footer, IDEACION)), len(Q)

def main():
    units = []; toc = []
    for code, mod_name in ORDER:
        try: mod = importlib.import_module(mod_name)
        except ModuleNotFoundError: print("  [omitido]", code); continue
        units.append('<div class="doc-unit">%s%s%s<div class="footer-note">%s<br>%s</div></div>'
                     % (mod.COVER, mod.BODY, mod.REFS, mod.META["footer"], IDEACION))
        if code in MODULES_LABEL: toc.append('<tr><td colspan="3" class="mod">%s</td></tr>' % MODULES_LABEL[code])
        at, ac = ANCLA[code]
        toc.append('<tr><td class="c1">%s</td><td>%s</td><td class="c3"><span class="bdg bg-%s">%s</span></td></tr>' % (code, get_title(mod.COVER), ac, at))
    quiz_unit, nq = build_quiz_unit()
    units.append(quiz_unit)
    toc.append('<tr><td colspan="3" class="mod">Evaluacion</td></tr>')
    toc.append('<tr><td class="c1">EVAL</td><td>Cuestionario de evaluacion (%d preguntas) + soluciones</td><td class="c3"><span class="bdg bg-alg">TEST</span></td></tr>' % nq)

    cover = ('<section class="dsr-cover"><div class="dsr-kicker">Serie formativa - CAUSA - SACYL - 2026</div>'
             '<h1 class="dsr-title">Hemostasia y Medicina Transfusional Perioperatoria (PBM)</h1>'
             '<div class="dsr-sub">Dosier docente completo + cuestionario de evaluacion</div>'
             '<div class="dsr-spine"><b>Los 3 pilares del PBM + el eje de la hemostasia:</b> (1) optimizar la masa eritrocitaria - '
             '(2) minimizar la perdida sanguinea - (3) optimizar y tolerar la anemia - + eje: evaluacion y manejo del sangrado.</div>'
             '<div class="dsr-meta">18 documentos (PBM-01 ... PBM-18) + 5 quick-reference (P-QR-01 ... P-QR-05) + cuestionario de 200 preguntas<br>'
             'Anclas: GUIA - META - ECA - REV - ALG. Cifras de fuentes primarias verificadas (PubMed) y guias (NBA/BSH/SEDAR).</div>'
             '<div class="dsr-ideacion">%s</div></section>' % IDEACION)
    toc_html = '<section class="dsr-toc"><h2>Indice del dosier</h2><table class="dsrtoc"><tbody>%s</tbody></table></section>' % ("".join(toc))
    html = '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><style>%s</style></head><body>%s%s%s</body></html>' % (
        CSS + DOSSIER_CSS + QUIZ_CSS, cover, toc_html, "".join(units))
    out = BASE / "PBM-dosier-completo-cuestionario.html"
    out.write_text(html, encoding="utf-8")
    from weasyprint import HTML
    HTML(str(out)).write_pdf(str(out.with_suffix(".pdf")))
    print("PDF :", out.with_suffix(".pdf"), "| preguntas:", nq)

if __name__ == "__main__":
    main()
