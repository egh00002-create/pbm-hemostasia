# -*- coding: utf-8 -*-
"""Genera el PDF del cuestionario PBM (examen + soluciones) con el estilo de la serie."""
import json, html, pathlib
from build_doc import CSS

BASE = pathlib.Path(__file__).resolve().parent
Q = json.load(open(BASE / "app-data" / "questions.json", encoding="utf-8"))
LETTERS = ["A", "B", "C", "D"]
ANCLA_DOC = {}  # no usado; mantenemos simple

EXTRA = """
  .qz-q{ break-inside:avoid; margin:0 0 9px; padding:7px 10px; border:1px solid var(--line); border-left:4px solid var(--accent2); border-radius:0 5px 5px 0; }
  .qz-h{ font-family:"DejaVu Sans Mono",monospace; font-size:7pt; color:var(--muted); letter-spacing:.04em; }
  .qz-stem{ font-size:9pt; font-weight:600; color:var(--ink); margin:3px 0 5px; }
  .qz-opt{ font-size:8.4pt; margin:2px 0 2px 6px; }
  .qz-opt .L{ font-family:"DejaVu Sans Mono",monospace; font-weight:700; color:var(--accent2); margin-right:5px; }
  .sol{ break-inside:avoid; font-size:8pt; margin:0 0 5px; padding:5px 9px; border-left:3px solid var(--pearl); background:var(--pearl-bg); border-radius:0 4px 4px 0; }
  .sol b{ color:var(--pearl); }
  .sol .ans{ font-family:"DejaVu Sans Mono",monospace; font-weight:700; color:var(--accent); }
  .grid2{ columns:2; column-gap:18px; }
  .lvl-b{ background:#E7EDF1; color:#3A5563; } .lvl-a{ background:#F4E3E6; color:#8E2433; }
  .lvltag{ display:inline-block; font-family:"DejaVu Sans Mono",monospace; font-size:6.4pt; font-weight:700; padding:1px 5px; border-radius:8px; }
"""

def esc(s): return html.escape(s, quote=False)

# --- portada ---
cover = f"""
<section>
  <div class="docref">
    <span class="doc-code">PBM-EVAL</span>
    <span class="badge b-alg">CUESTIONARIO &middot; 200 preguntas</span>
    <span class="module-tag">Serie PBM &middot; evaluaci&oacute;n formativa</span>
  </div>
  <h1 class="title">Cuestionario de evaluaci&oacute;n &mdash; Serie PBM</h1>
  <div class="subtitle">200 preguntas tipo test sobre Hemostasia y Medicina Transfusional Perioperatoria &mdash; con soluciones razonadas</div>
  <div class="tagline">2026 &middot; Preguntas fundamentadas en los 23 documentos y verificadas contra PubMed &middot; CAUSA / SACYL<br>
  <b>Uso:</b> responde el examen (parte 1) y comprueba en las soluciones (parte 2) la respuesta correcta, la explicaci&oacute;n y la fuente (PMID).</div>
  <div class="lead"><p>Cuestionario derivado de la serie formativa PBM. Cada pregunta indica el documento de origen y su nivel
  (B&aacute;sico / Avanzado). Las soluciones incluyen explicaci&oacute;n breve y referencia indexada. Material docente; no sustituye al
  juicio cl&iacute;nico ni a los protocolos locales vigentes.</p></div>
</section>
"""

# --- parte 1: examen ---
exam = ['<h2 class="sec"><span class="num">1.</span>Examen (200 preguntas)</h2>']
cur = None
for i, q in enumerate(Q, 1):
    if q["doc"] != cur:
        cur = q["doc"]
        exam.append(f'<h3 style="margin-top:10px">{esc(cur)}</h3>')
    lvl = 'lvl-a' if q["level"] == "avanzado" else 'lvl-b'
    opts = "".join(f'<div class="qz-opt"><span class="L">{LETTERS[j]}</span>{esc(o)}</div>' for j, o in enumerate(q["options"]))
    exam.append(
        f'<div class="qz-q"><span class="qz-h">{esc(q["id"])} &middot; {esc(q["doc"])} '
        f'<span class="lvltag {lvl}">{q["level"].upper()}</span></span>'
        f'<div class="qz-stem">{i}. {esc(q["q"])}</div>{opts}</div>')

# --- parte 2: soluciones ---
sols = ['<h2 class="sec"><span class="num">2.</span>Soluciones razonadas</h2><div class="grid2">']
for i, q in enumerate(Q, 1):
    L = LETTERS[q["answer"]]
    sols.append(
        f'<div class="sol"><b>{i}. {esc(q["id"])}</b> &mdash; Respuesta: <span class="ans">{L}</span>. '
        f'{esc(q["explanation"])} <i>({esc(q["ref"])} &middot; {esc(q["doc"])})</i></div>')
sols.append('</div>')

footer = ("Cuestionario de la Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - 200 preguntas - 2026. "
          "Preguntas y soluciones fundamentadas en los 23 documentos de la serie, verificadas contra PubMed (CAUSA / SACYL). "
          "Material docente; no sustituye al juicio clinico ni a los protocolos locales vigentes.")

HTML = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<style>{CSS}{EXTRA}</style></head><body>
{cover}{''.join(exam)}{''.join(sols)}
<div class="footer-note">{footer}<br><strong>Ideacion:</strong> Emilio Garcia Hernandez - Licenciado Especialista en Anestesiologia y Reanimacion - CAUSA - SACYL.</div>
</body></html>"""

out = BASE / "PBM-cuestionario-200.html"
out.write_text(HTML, encoding="utf-8")
try:
    from weasyprint import HTML as WH
    WH(str(out)).write_pdf(str(out.with_suffix(".pdf")))
    print("PDF:", out.with_suffix(".pdf"))
except Exception as e:
    print("PDF-ERROR:", e)
print("Preguntas:", len(Q))
