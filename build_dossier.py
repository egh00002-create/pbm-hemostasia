# -*- coding: utf-8 -*-
"""build_dossier.py - Ensambla el DOSIER UNICO de la serie PBM (portada + indice + documentos)."""
import re, importlib, pathlib
from build_doc import CSS
BASE = pathlib.Path(__file__).resolve().parent
ORDER = [("PBM-%02d"%i, "_build_pbm%02d"%i) for i in range(1,19)] + [("P-QR-%02d"%i, "_build_pqr%02d"%i) for i in range(1,6)]
TITLE_RE = re.compile(r'<h1 class="title">(.*?)</h1>', re.S)
def get_title(c):
    m=TITLE_RE.search(c); return re.sub(r"\s+"," ",m.group(1)).strip() if m else ""
DOSSIER_CSS = r"""
  h1.title { bookmark-level: 1; bookmark-label: content(text); }
  h2.sec   { bookmark-level: 2; bookmark-label: content(text); }
  .doc-unit { break-before: page; } .doc-unit:first-of-type { break-before: avoid; }
  .dsr-cover { break-after: page; bookmark-level: 1; bookmark-label: "Portada"; }
  .dsr-kicker{ font-family:"DejaVu Sans Mono",monospace; font-size:8pt; letter-spacing:.18em; text-transform:uppercase; color:var(--accent2); font-weight:700; margin-bottom:10px; }
  .dsr-title { font-family:"DejaVu Serif",Georgia,serif; font-size:27pt; line-height:1.12; color:var(--ink); margin:0 0 8px 0; border-bottom:4px solid var(--accent); padding-bottom:16px; }
  .dsr-sub   { font-size:13pt; color:var(--ink2); font-style:italic; font-family:"DejaVu Serif",Georgia,serif; margin:14px 0; }
  .dsr-spine { background:var(--accent-soft); border-left:4px solid var(--accent); border-radius:0 6px 6px 0; padding:12px 16px; margin:18px 0; font-size:9pt; color:var(--ink2); }
  .dsr-meta  { font-family:"DejaVu Sans Mono",monospace; font-size:8pt; color:var(--muted); line-height:1.7; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding:10px 0; margin:16px 0; }
  .dsr-ideacion{ margin-top:26px; padding:12px 16px; background:var(--accent2-soft); border-left:4px solid var(--accent2); border-radius:0 6px 6px 0; font-size:9pt; color:var(--ink2); }
  .dsr-toc { break-after: page; bookmark-level: 1; bookmark-label: "Indice del dosier"; }
  .dsr-toc h2{ font-size:15pt; color:var(--accent); border-bottom:2px solid var(--ink); padding-bottom:6px; margin:0 0 12px; }
  .dsr-toc .mod{ font-family:"DejaVu Sans Mono",monospace; font-size:8pt; letter-spacing:.06em; text-transform:uppercase; color:var(--accent2); font-weight:700; margin:14px 0 4px; }
  table.dsrtoc{ width:100%; border-collapse:collapse; font-size:8.6pt; margin:0; }
  table.dsrtoc td{ border:none; border-bottom:1px solid var(--line); padding:4px 6px; vertical-align:top; }
  table.dsrtoc .c1{ font-family:"DejaVu Sans Mono",monospace; font-weight:700; color:var(--accent); white-space:nowrap; width:64px; }
  table.dsrtoc .c3{ font-family:"DejaVu Sans Mono",monospace; font-size:7pt; color:#fff; text-align:center; width:46px; }
  .bdg{ border-radius:3px; padding:1px 5px; }
  .bg-guia{background:#8E2433;} .bg-meta{background:#4F6B7A;} .bg-eca{background:#7A3E6E;} .bg-rev{background:#6E6358;} .bg-alg{background:#4E5A66;}
  @page :first { @bottom-center { content: none; } }
"""
ANCLA = {"PBM-01":("GUÍA","guia"),"PBM-02":("GUÍA","guia"),"PBM-03":("GUÍA","guia"),
  "PBM-04":("GUÍA","guia"),"PBM-05":("META","meta"),"PBM-06":("META","meta"),
  "PBM-07":("REV","rev"),"PBM-08":("ECA","eca"),"PBM-09":("META","meta"),"PBM-10":("META","meta"),"PBM-11":("REV","rev"),
  "PBM-12":("ECA","eca"),"PBM-13":("GUÍA","guia"),"PBM-14":("REV","rev"),
  "PBM-15":("REV","rev"),"PBM-16":("GUÍA","guia"),"PBM-17":("REV","rev"),"PBM-18":("REV","rev"),
  "P-QR-01":("ALG","alg"),"P-QR-02":("ALG","alg"),"P-QR-03":("ALG","alg"),"P-QR-04":("ALG","alg"),"P-QR-05":("ALG","alg")}
MODULES_LABEL = {"PBM-01":"Modulo 1 - Fundamentos: PBM y medicina transfusional","PBM-04":"Modulo 2 - Pilar 1: optimizar la masa eritrocitaria",
  "PBM-07":"Modulo 3 - Pilar 2: minimizar la perdida sanguinea","PBM-12":"Modulo 4 - Pilar 3: tolerancia a la anemia y transfusion",
  "PBM-15":"Modulo 5 - Hemostasia clinica y riesgo hemorragico","P-QR-01":"Quick-reference (tarjetas)"}
IDEACION = "<b>Ideacion:</b> Emilio Garcia Hernandez - Licenciado Especialista en Anestesiologia y Reanimacion - CAUSA - SACYL."
def main():
    units=[]; toc=[]
    for code,mod_name in ORDER:
        try: mod=importlib.import_module(mod_name)
        except ModuleNotFoundError: print("  [omitido]",code); continue
        units.append('<div class="doc-unit">%s%s%s<div class="footer-note">%s<br>%s</div></div>'%(mod.COVER,mod.BODY,mod.REFS,mod.META["footer"],IDEACION))
        if code in MODULES_LABEL: toc.append('<tr><td colspan="3" class="mod">%s</td></tr>'%MODULES_LABEL[code])
        at,ac=ANCLA[code]; toc.append('<tr><td class="c1">%s</td><td>%s</td><td class="c3"><span class="bdg bg-%s">%s</span></td></tr>'%(code,get_title(mod.COVER),ac,at))
    if not units: print("No hay documentos todavia."); return
    cover='<section class="dsr-cover"><div class="dsr-kicker">Serie formativa - CAUSA - SACYL - 2026</div><h1 class="dsr-title">Hemostasia y Medicina Transfusional Perioperatoria (PBM)</h1><div class="dsr-sub">Gestion de la sangre y del sangrado perioperatorio - dosier docente</div><div class="dsr-spine"><b>Los 3 pilares del PBM + el eje de la hemostasia:</b> (1) optimizar la masa eritrocitaria - (2) minimizar la perdida sanguinea - (3) optimizar y tolerar la anemia - + eje: evaluacion y manejo del sangrado.</div><div class="dsr-meta">18 documentos (PBM-01 ... PBM-18) + 5 quick-reference (P-QR-01 ... P-QR-05) - 5 modulos<br>Anclas: GUIA - META - ECA - REV - ALG. Cifras de fuentes primarias verificadas (PubMed) y guias (NBA/BSH/SEDAR).</div><div class="dsr-ideacion">%s</div></section>'%IDEACION
    toc_html='<section class="dsr-toc"><h2>Indice del dosier</h2><table class="dsrtoc"><tbody>%s</tbody></table></section>'%("".join(toc))
    html='<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><style>%s</style></head><body>%s%s%s</body></html>'%(CSS+DOSSIER_CSS,cover,toc_html,"".join(units))
    (BASE/"PBM-dosier-completo.html").write_text(html,encoding="utf-8")
    from weasyprint import HTML
    HTML(str(BASE/"PBM-dosier-completo.html")).write_pdf(str(BASE/"PBM-dosier-completo.pdf"))
    print("PDF :", BASE/"PBM-dosier-completo.pdf")
if __name__=="__main__": main()
