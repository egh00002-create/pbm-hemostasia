# -*- coding: utf-8 -*-
"""build_libro3.py - Edicion LIBRO del dosier PBM con: indice con numeros de pagina (target-counter),
cabeceras de pagina (running headers parte/capitulo), numeracion romana en preliminares + arabiga en el cuerpo,
e indice analitico alfabetico (Apendice C). Salida: PBM-libro.pdf"""
import importlib, pathlib, json, html as _html, unicodedata
from build_doc import CSS
from build_dossier import DOSSIER_CSS, ANCLA, IDEACION, ORDER, get_title

BASE = pathlib.Path(__file__).resolve().parent
LETTERS = ["A", "B", "C", "D"]
def esc(s): return _html.escape(s, quote=False)
def sortkey(s): return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")

BOOK_CSS = r"""
  /* Marcadores: Parte > Capitulo > Seccion */
  .part h1.parttitle { bookmark-level: 1; bookmark-label: content(text); string-set: parttitle content(text); }
  .matter h1.parttitle { bookmark-level: 1; bookmark-label: content(text); }
  .dsr-toc { bookmark-label: "Indice tematico"; }
  h1.title { bookmark-level: 2; bookmark-label: content(text); string-set: chaptitle content(text); }
  h2.sec   { bookmark-level: 3; bookmark-label: content(text); }
  /* Cabeceras y numeracion */
  @page { @top-left{ content: string(parttitle); font-family:"DejaVu Sans Mono",monospace; font-size:7pt; color:#8A7E83; }
          @top-right{ content: string(chaptitle); font-family:"DejaVu Serif",Georgia,serif; font-size:7.5pt; font-style:italic; color:#8A7E83; } }
  @page front { @top-left{ content:none } @top-right{ content:none } @bottom-center{ content: counter(page, lower-roman); } }
  @page :first { @top-left{ content:none } @top-right{ content:none } @bottom-center{ content: none; } }
  .book-cover, .credits, .frontmatter, .dsr-toc { page: front; }
  .matter-h{ font-family:"DejaVu Serif",Georgia,serif; font-size:20pt; color:var(--accent); border-bottom:3px solid var(--accent); padding-bottom:10px; margin:0 0 14px;  string-set: chaptitle content(text); }
  .book-cover { break-after: page; height: 95vh; display:flex; flex-direction:column; justify-content:center; bookmark-level:1; bookmark-label:"Portada"; text-align:center; }
  .bc-kicker{ font-family:"DejaVu Sans Mono",monospace; font-size:10pt; letter-spacing:.22em; text-transform:uppercase; color:var(--accent2); font-weight:700; }
  .bc-title{ font-family:"DejaVu Serif",Georgia,serif; font-size:33pt; line-height:1.1; color:var(--accent); margin:18px 0 6px; }
  .bc-rule{ width:120px; height:4px; background:var(--accent); margin:14px auto; }
  .bc-sub{ font-family:"DejaVu Serif",Georgia,serif; font-style:italic; font-size:14pt; color:var(--ink2); margin:6px 0 24px; }
  .bc-pillars{ font-family:"DejaVu Sans Mono",monospace; font-size:8.5pt; color:var(--muted); line-height:1.9; }
  .bc-author{ margin-top:34px; font-size:10.5pt; color:var(--ink); }
  .bc-author b{ color:var(--accent); }
  .credits { break-after: page; font-size:8.6pt; color:var(--ink2); line-height:1.6; }
  .credits h3{ color:var(--accent); font-size:11pt; }
  .matter, .frontmatter { break-before: page; }
  .matter p, .frontmatter p{ font-size:9.4pt; line-height:1.6; }
  .frontmatter h1.parttitle{ font-family:"DejaVu Serif",Georgia,serif; font-size:20pt; color:var(--accent); border-bottom:3px solid var(--accent); padding-bottom:10px; margin:0 0 14px; bookmark-level:1; bookmark-label:content(text); }
  .part { break-before: page; break-after: page; height: 80vh; display:flex; flex-direction:column; justify-content:center; }
  .part .pnum{ font-family:"DejaVu Sans Mono",monospace; font-size:12pt; letter-spacing:.2em; color:var(--accent2); font-weight:700; }
  .part h1.parttitle{ font-family:"DejaVu Serif",Georgia,serif; font-size:26pt; color:var(--accent); margin:8px 0; border:0; }
  .part .pdesc{ font-size:10pt; color:var(--ink2); font-style:italic; max-width:80%; }
  .part .prule{ width:90px; height:4px; background:var(--accent); margin:14px 0; }
  /* Indice tematico con numeros de pagina */
  table.dsrtoc .tl{ color:var(--ink); text-decoration:none; }
  table.dsrtoc td.pg{ text-align:right; font-family:"DejaVu Sans Mono",monospace; font-size:8pt; color:var(--accent); white-space:nowrap; width:34px; }
  table.dsrtoc td.pg a{ color:var(--accent); text-decoration:none; }
  table.dsrtoc td.pg a::after{ content: target-counter(attr(href), page); }
  /* Glosario */
  .gloss { columns:2; column-gap:22px; font-size:8.4pt; }
  .gloss dt{ font-weight:700; color:var(--accent); margin-top:6px; break-after:avoid; }
  .gloss dd{ margin:0 0 2px; line-height:1.42; }
  .gloss-sub{ break-before:avoid; font-family:"DejaVu Sans Mono",monospace; font-size:8pt; letter-spacing:.06em; text-transform:uppercase; color:var(--accent2); font-weight:700; margin:12px 0 4px; column-span:all; }
  ol.biblio{ font-size:8pt; line-height:1.45; padding-left:22px; }
  ol.biblio li{ margin-bottom:5px; }
  ol.biblio .doi{ color:var(--accent); font-family:"DejaVu Sans Mono",monospace; font-size:7.4pt; }
  /* Indice analitico */
  .ix{ columns:2; column-gap:26px; font-size:8.6pt; }
  .ix .ixe{ break-inside:avoid; margin:0 0 3px; }
  .ix .ixe a{ color:var(--ink); text-decoration:none; }
  .ix .ixe a::after{ content: " " leader('.') " " target-counter(attr(href), page); color:var(--accent); font-family:"DejaVu Sans Mono",monospace; font-size:7.6pt; }
  .ix-letter{ column-span:all; font-family:"DejaVu Serif",Georgia,serif; font-weight:700; color:var(--accent2); font-size:10pt; margin:8px 0 2px; border-bottom:1px solid var(--line); }
"""

QUIZ_CSS = r"""
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

# code -> (numero, titulo, desc, anchor)
PARTS = {
 "PBM-01": ("Parte I", "Fundamentos: PBM y medicina transfusional", "Que es el Patient Blood Management, los componentes sanguineos y la seguridad transfusional.", "parte-1"),
 "PBM-04": ("Parte II", "Pilar 1 - Optimizar la masa eritrocitaria", "Diagnostico y tratamiento de la anemia preoperatoria: hierro y agentes estimuladores de la eritropoyesis.", "parte-2"),
 "PBM-07": ("Parte III", "Pilar 2 - Minimizar la perdida sanguinea", "Hemostasia, antifibrinoliticos, viscoelastica, recuperador celular y planificacion (MABL).", "parte-3"),
 "PBM-12": ("Parte IV", "Pilar 3 - Tolerancia a la anemia y transfusion", "Umbrales restrictivos, hemorragia critica y fisiologia de la tolerancia a la anemia.", "parte-4"),
 "PBM-15": ("Parte V", "Eje transversal - Hemostasia clinica y riesgo hemorragico", "Cribado del riesgo, antitromboticos, coagulopatias y farmacos hemostaticos.", "parte-5"),
 "P-QR-01": ("Parte VI", "Quick-reference - Tarjetas de consulta rapida", "Resumenes operativos de un vistazo de los temas nucleo de la serie.", "parte-6"),
}

def part_divider(num, title, desc, anchor, first=False):
    cls = "part bodystart" if first else "part"
    return ('<section class="%s" id="%s"><div class="pnum">%s</div><h1 class="parttitle">%s</h1>'
            '<div class="prule"></div><div class="pdesc">%s</div></section>' % (cls, anchor, num, esc(title), esc(desc)))

def build_quiz():
    Q = json.load(open(BASE / "app-data" / "questions.json", encoding="utf-8"))
    head = part_divider("Parte VII", "Evaluacion", "Cuestionario de autoevaluacion de 200 preguntas con soluciones razonadas y fuente.", "parte-7")
    cov = ('<div class="doc-unit" id="cap-eval"><h1 class="title">Cuestionario de evaluaci&oacute;n &mdash; 200 preguntas</h1>'
           '<div class="subtitle">Autoevaluaci&oacute;n tipo test sobre los 23 cap&iacute;tulos, con soluciones razonadas y referencia (PMID)</div>')
    exam = ['<h2 class="sec"><span class="num">A.</span>Examen (200 preguntas)</h2>']
    cur = None
    for i, q in enumerate(Q, 1):
        if q["doc"] != cur:
            cur = q["doc"]; exam.append('<h3 style="margin-top:9px">%s</h3>' % esc(cur))
        lvl = 'lvl-a' if q["level"] == "avanzado" else 'lvl-b'
        opts = "".join('<div class="qz-opt"><span class="L">%s</span>%s</div>' % (LETTERS[j], esc(o)) for j, o in enumerate(q["options"]))
        exam.append('<div class="qz-q"><span class="qz-h">%s &middot; %s <span class="lvltag %s">%s</span></span>'
                    '<div class="qz-stem">%d. %s</div>%s</div>' % (esc(q["id"]), esc(q["doc"]), lvl, q["level"].upper(), i, esc(q["q"]), opts))
    sols = ['<h2 class="sec"><span class="num">B.</span>Soluciones razonadas</h2><div class="grid2">']
    for i, q in enumerate(Q, 1):
        sols.append('<div class="sol"><b>%d. %s</b> &mdash; Respuesta: <span class="ans">%s</span>. %s <i>(%s &middot; %s)</i></div>'
                    % (i, esc(q["id"]), LETTERS[q["answer"]], esc(q["explanation"]), esc(q["ref"]), esc(q["doc"])))
    sols.append('</div></div>')
    return head + cov + "".join(exam) + "".join(sols), len(Q)

GLOSARIO = {
 "Conceptos clave": [
  ("Patient Blood Management (PBM)", "Gesti&oacute;n de la sangre del paciente: estrategias multimodales para optimizar la propia sangre y reservar la transfusi&oacute;n para cuando aporta beneficio."),
  ("Tres pilares", "(1) Optimizar la masa eritrocitaria; (2) minimizar la p&eacute;rdida sangu&iacute;nea; (3) optimizar y tolerar la anemia."),
  ("Anemia", "Hb &lt; 130 g/l en el var&oacute;n y &lt; 120 g/l en la mujer (criterio operativo)."),
  ("Ferropenia", "D&eacute;ficit de hierro: absoluta (dep&oacute;sitos agotados) o funcional (no se moviliza pese a dep&oacute;sitos, t&iacute;pica de inflamaci&oacute;n)."),
  ("Ferritina", "Marcador de dep&oacute;sitos de hierro y reactante de fase aguda; interpretar junto a la PCR."),
  ("Hepcidina", "Hormona reguladora del hierro; explica la mejor absorci&oacute;n del hierro oral a dosis bajas/alternas."),
  ("ESA / EPO", "Agentes estimuladores de la eritropoyesis; estimulan la producci&oacute;n de hemat&iacute;es, siempre con hierro adecuado."),
  ("Umbral restrictivo / liberal", "Estrategia de transfusi&oacute;n con Hb baja (&asymp;7-8 g/dl) frente a alta (9-10 g/dl)."),
  ("Entrega de ox&iacute;geno (DO2)", "Producto del gasto card&iacute;aco por el contenido arterial de O2 (Hb y SaO2)."),
  ("Anemia cr&iacute;tica", "Punto en que la entrega de O2 ya no cubre el consumo; var&iacute;a seg&uacute;n el paciente."),
  ("MABL", "P&eacute;rdida sangu&iacute;nea m&aacute;xima admisible hasta un Hto/Hb diana; herramienta de planificaci&oacute;n."),
  ("Hemostasia", "Proceso celular de formaci&oacute;n del co&aacute;gulo: primaria (plaquetas) y secundaria (factores)."),
  ("Fibrin&oacute;lisis", "Disoluci&oacute;n del co&aacute;gulo por la plasmina; su exceso favorece el sangrado."),
  ("Viscoel&aacute;stica", "Pruebas (ROTEM/TEG) que miden en tiempo real la formaci&oacute;n, firmeza y lisis del co&aacute;gulo."),
  ("Recuperador celular", "Sistema que lava y reinfunde los hemat&iacute;es propios del campo quir&uacute;rgico (cell salvage)."),
  ("Transfusi&oacute;n masiva", "&asymp; un volumen sangu&iacute;neo en 24 h; se maneja por protocolo."),
  ("Tr&iacute;ada letal", "Hipotermia + acidosis + coagulopat&iacute;a, que se retroalimentan en la hemorragia."),
  ("Hemovigilancia", "Sistema de notificaci&oacute;n y an&aacute;lisis de incidentes transfusionales (p. ej. SHOT)."),
  ("Coagulopat&iacute;a", "Alteraci&oacute;n de la coagulaci&oacute;n, cong&eacute;nita (von Willebrand, hemofilia) o adquirida (hep&aacute;tica, CID, diluci&oacute;n)."),
 ],
 "Acronimos": [
  ("Hb / Hto", "Hemoglobina / Hematocrito."),
  ("PFC", "Plasma fresco congelado."),
  ("CCP", "Concentrado de complejo protromb&iacute;nico (II, VII, IX, X); revierte los AVK."),
  ("rFVIIa", "Factor VII activado recombinante; rescate off-label con riesgo trombótico."),
  ("DDAVP", "Desmopresina; libera factor de von Willebrand y FVIII."),
  ("TXA", "&Aacute;cido tranex&aacute;mico (antifibrinol&iacute;tico)."),
  ("CID", "Coagulaci&oacute;n intravascular diseminada."),
  ("TACO", "Sobrecarga circulatoria asociada a transfusi&oacute;n."),
  ("TRALI", "Lesi&oacute;n pulmonar aguda asociada a transfusi&oacute;n."),
  ("TA-GVHD", "Enfermedad injerto contra hu&eacute;sped asociada a transfusi&oacute;n (prevenible con irradiaci&oacute;n)."),
  ("HEMSTOP", "Cuestionario de cribado del riesgo hemorr&aacute;gico (7 &iacute;tems; &ge;2 = estudio)."),
  ("AVK", "Antagonistas de la vitamina K (warfarina, acenocumarol)."),
  ("ACOD", "Anticoagulantes orales de acci&oacute;n directa (apixab&aacute;n, rivaroxab&aacute;n, edoxab&aacute;n, dabigatr&aacute;n)."),
  ("SCA", "S&iacute;ndrome coronario agudo (excepci&oacute;n del umbral restrictivo: liberal &asymp;10 g/dl)."),
  ("HPP / HIC / TCE", "Hemorragia posparto / intracraneal / Traumatismo craneoencef&aacute;lico."),
 ],
 "Ensayos y guias citados": [
  ("TRICC / TRISS", "Umbral restrictivo en cr&iacute;ticos (NEJM 1999) y en shock s&eacute;ptico (NEJM 2014)."),
  ("REALITY", "Restrictivo vs liberal en infarto + anemia (JAMA 2021)."),
  ("CRASH-2 / CRASH-3", "TXA en trauma (Lancet 2010) y en TCE (Lancet 2019)."),
  ("WOMAN / ATACAS", "TXA en hemorragia posparto (Lancet 2017) y en cirug&iacute;a coronaria (NEJM 2017)."),
  ("PREVENTT", "Hierro IV preoperatorio en cirug&iacute;a abdominal: resultado neutro (Lancet 2020)."),
  ("PROPPR", "Ratio 1:1:1 vs 1:1:2 en trauma masivo (JAMA 2015)."),
  ("BRIDGE", "Puente de anticoagulaci&oacute;n en FA: en contra del puente sistem&aacute;tico (NEJM 2015)."),
  ("AABB / ESAIC / EACTS / BSH", "Gu&iacute;as de sociedad de referencia de la serie."),
 ],
}

# Indice analitico: termino -> codigo de capitulo (ancla #cap-CODE)
INDICE = [
 ("&Aacute;cido tranex&aacute;mico", "PBM-08"), ("Anemia preoperatoria", "PBM-04"), ("Antiagregantes", "PBM-16"),
 ("Anticoagulantes (AVK/ACOD)", "PBM-16"), ("ATACAS", "PBM-08"), ("BRIDGE (puente)", "PBM-16"),
 ("Calcio i&oacute;nico", "PBM-13"), ("Coagulopat&iacute;as", "PBM-17"), ("Complejo protromb&iacute;nico (CCP)", "PBM-18"),
 ("Componentes sangu&iacute;neos", "PBM-02"), ("CRASH-2", "PBM-08"), ("CRASH-3", "PBM-08"),
 ("Crioprecipitado", "PBM-02"), ("Desmopresina", "PBM-18"), ("Entrega de ox&iacute;geno (DO2)", "PBM-14"),
 ("Eritropoyetina (EPO/ESA)", "PBM-06"), ("Ferritina", "PBM-04"), ("Ferropenia", "PBM-05"),
 ("Fibrin&oacute;geno", "PBM-18"), ("Hemorragia cr&iacute;tica", "PBM-13"), ("Hemostasia perioperatoria", "PBM-07"),
 ("HEMSTOP", "PBM-15"), ("Hierro intravenoso", "PBM-05"), ("MABL", "PBM-11"),
 ("Nadler (volumen sangu&iacute;neo)", "PBM-11"), ("Pilares del PBM", "PBM-01"), ("Plaquetas (transfusi&oacute;n)", "PBM-02"),
 ("Plasma fresco congelado", "PBM-02"), ("PREVENTT", "PBM-05"), ("PROPPR", "PBM-13"),
 ("REALITY", "PBM-12"), ("Recuperador celular", "PBM-10"), ("rFVIIa", "PBM-18"),
 ("ROTEM / TEG", "PBM-09"), ("Seguridad transfusional", "PBM-03"), ("TACO", "PBM-03"),
 ("Tolerancia a la anemia", "PBM-14"), ("TRALI", "PBM-03"), ("Transfusi&oacute;n masiva", "PBM-13"),
 ("Trazabilidad", "PBM-03"), ("Tr&iacute;ada letal", "PBM-07"), ("TRICC", "PBM-12"), ("TRISS", "PBM-12"),
 ("Umbrales restrictivos", "PBM-12"), ("Viscoel&aacute;stica", "PBM-09"), ("von Willebrand", "PBM-17"), ("WOMAN", "PBM-08"),
]

def build_glossary():
    head = part_divider("Apendice A", "Glosario", "Terminos, acronimos y ensayos/guias citados en el libro.", "ap-glos")
    body = ['<div class="matter" id="cap-glos"><div class="matter-h">Glosario</div>']
    for sub, items in GLOSARIO.items():
        body.append('<div class="gloss-sub">%s</div><dl class="gloss">' % esc(sub))
        for term, dfn in items:
            body.append('<dt>%s</dt><dd>%s</dd>' % (term, dfn))
        body.append('</dl>')
    body.append('</div>')
    return head + "".join(body)

def build_biblio():
    refs = json.load(open(BASE / "app-data" / "references.json", encoding="utf-8"))
    refs_sorted = sorted(refs, key=lambda r: r["citation"])
    head = part_divider("Apendice B", "Bibliografia maestra", "Referencias indexadas verificadas contra PubMed (autoria, titulo, revista, ano, DOI/PMID).", "ap-bib")
    items = []
    for r in refs_sorted:
        doi = ('<span class="doi">doi:%s</span> &middot; ' % esc(r["doi"])) if r.get("doi") else ""
        pmid = ('PMID %s' % esc(r["pmid"])) if r.get("pmid") else ""
        items.append('<li>%s %s%s</li>' % (esc(r["citation"]), doi, pmid))
    return head + '<div class="matter" id="cap-bib"><div class="matter-h">Bibliograf&iacute;a maestra</div><ol class="biblio">%s</ol><div class="footer-note">%s</div></div>' % ("".join(items), IDEACION)

def build_indice():
    head = part_divider("Apendice C", "Indice analitico", "Terminos clave con la pagina del capitulo donde se desarrollan.", "ap-ix")
    entries = sorted(INDICE, key=lambda t: sortkey(_html.unescape(t[0])))
    out = ['<div class="matter" id="cap-ix"><div class="matter-h">&Iacute;ndice anal&iacute;tico</div><div class="ix">']
    cur = ""
    for term, code in entries:
        letter = sortkey(_html.unescape(term))[0].upper()
        if letter != cur:
            cur = letter; out.append('<div class="ix-letter">%s</div>' % letter)
        out.append('<div class="ixe"><a href="#cap-%s">%s</a></div>' % (code, term))
    out.append('</div></div>')
    return head + "".join(out)

def main():
    cover = ('<section class="book-cover"><div class="bc-kicker">Serie formativa &middot; CAUSA &middot; SACYL</div>'
             '<div class="bc-title">Hemostasia y Medicina<br>Transfusional Perioperatoria</div>'
             '<div class="bc-rule"></div>'
             '<div class="bc-sub">Patient Blood Management (PBM) &mdash; manual docente con autoevaluaci&oacute;n</div>'
             '<div class="bc-pillars">Pilar 1 &middot; Masa eritrocitaria &nbsp;|&nbsp; Pilar 2 &middot; Minimizar la p&eacute;rdida<br>'
             'Pilar 3 &middot; Tolerar la anemia &nbsp;|&nbsp; Eje &middot; Hemostasia y sangrado</div>'
             '<div class="bc-author">Autor e ideaci&oacute;n: <b>Emilio Garc&iacute;a Hern&aacute;ndez</b><br>'
             'Licenciado Especialista en Anestesiolog&iacute;a y Reanimaci&oacute;n &middot; CAUSA &middot; SACYL &middot; 2026</div></section>')
    credits = ('<section class="credits"><h3>Cr&eacute;ditos y nota legal</h3>'
               '<p><b>T&iacute;tulo:</b> Hemostasia y Medicina Transfusional Perioperatoria (PBM) &mdash; manual docente con autoevaluaci&oacute;n. '
               '<b>Edici&oacute;n:</b> 2026. <b>Autor e ideaci&oacute;n:</b> Emilio Garc&iacute;a Hern&aacute;ndez (CAUSA / SACYL).</p>'
               '<p>Obra <b>docente</b> para anestesi&oacute;logos adjuntos y residentes; &uacute;til para hematolog&iacute;a, cirug&iacute;a y enfermer&iacute;a perioperatoria. '
               'Las cifras proceden de <b>fuentes primarias verificadas contra PubMed</b> y de gu&iacute;as de sociedad (AABB, ESAIC, EACTS, BSH, NBA).</p>'
               '<p><b>Aviso:</b> no es un dispositivo m&eacute;dico ni una gu&iacute;a oficial. <b>No sustituye al juicio cl&iacute;nico ni a los protocolos locales vigentes.</b></p>'
               '<p>%s</p></section>' % IDEACION)
    prologo = ('<section class="frontmatter"><h1 class="parttitle">Pr&oacute;logo</h1>'
               '<p>La transfusi&oacute;n es una de las terapias m&aacute;s usadas y, a la vez, una de las que m&aacute;s se beneficia de un cambio de enfoque. '
               'Este libro re&uacute;ne la serie formativa sobre <b>Patient Blood Management</b> y hemostasia perioperatoria en un solo volumen, '
               'organizado alrededor de los <b>tres pilares</b> del PBM m&aacute;s el <b>eje transversal de la hemostasia</b>.</p>'
               '<p>Cada cap&iacute;tulo mantiene un <b>tono honesto</b> sobre la evidencia: lo bien establecido (tranex&aacute;mico precoz, umbrales restrictivos, '
               'hierro en la ferropenia real) y lo m&aacute;s discutido (PREVENTT neutro, la excepci&oacute;n del SCA, la incertidumbre de la viscoel&aacute;stica o del rFVIIa). '
               'El objetivo no es transfundir menos por ahorro, sino <b>tratar mejor</b>.</p>'
               '<p>El volumen se cierra con un <b>cuestionario de 200 preguntas</b>, un <b>glosario</b>, la <b>bibliograf&iacute;a maestra</b> y un <b>&iacute;ndice anal&iacute;tico</b>.</p>'
               '<p style="text-align:right; font-style:italic">Emilio Garc&iacute;a Hern&aacute;ndez &middot; Salamanca, 2026</p></section>')

    units = []; toc = []
    for code, mod_name in ORDER:
        try: mod = importlib.import_module(mod_name)
        except ModuleNotFoundError: print("  [omitido]", code); continue
        if code in PARTS:
            num, title, desc, anchor = PARTS[code]
            units.append(part_divider(num, title, desc, anchor, first=(code == "PBM-01")))
            toc.append('<tr><td colspan="3" class="mod"><a class="tl" href="#%s">%s &mdash; %s</a></td></tr>' % (anchor, esc(num), esc(title)))
        units.append('<div class="doc-unit" id="cap-%s">%s%s%s<div class="footer-note">%s<br>%s</div></div>'
                     % (code, mod.COVER, mod.BODY, mod.REFS, mod.META["footer"], IDEACION))
        at, ac = ANCLA[code]
        toc.append('<tr><td class="c1">%s</td><td><a class="tl" href="#cap-%s">%s</a> <span class="bdg bg-%s" style="font-size:6.5pt;color:#fff;border-radius:3px;padding:0 4px">%s</span></td><td class="pg"><a href="#cap-%s"></a></td></tr>'
                   % (code, code, get_title(mod.COVER), ac, at, code))

    quiz, nq = build_quiz()
    units.append(quiz)
    toc.append('<tr><td colspan="3" class="mod"><a class="tl" href="#parte-7">Parte VII &mdash; Evaluaci&oacute;n</a></td></tr>')
    toc.append('<tr><td class="c1">EVAL</td><td><a class="tl" href="#cap-eval">Cuestionario (200 preguntas) + soluciones</a></td><td class="pg"><a href="#cap-eval"></a></td></tr>')
    gloss = build_glossary(); biblio = build_biblio(); indice = build_indice()
    toc.append('<tr><td colspan="3" class="mod">Ap&eacute;ndices</td></tr>')
    toc.append('<tr><td class="c1">A</td><td><a class="tl" href="#cap-glos">Glosario</a></td><td class="pg"><a href="#cap-glos"></a></td></tr>')
    toc.append('<tr><td class="c1">B</td><td><a class="tl" href="#cap-bib">Bibliograf&iacute;a maestra</a></td><td class="pg"><a href="#cap-bib"></a></td></tr>')
    toc.append('<tr><td class="c1">C</td><td><a class="tl" href="#cap-ix">&Iacute;ndice anal&iacute;tico</a></td><td class="pg"><a href="#cap-ix"></a></td></tr>')

    toc_html = ('<section class="dsr-toc"><h2>&Iacute;ndice tem&aacute;tico</h2><table class="dsrtoc"><tbody>'
                '<tr><td colspan="3" class="mod">Preliminares</td></tr>'
                '<tr><td class="c1">&middot;</td><td><a class="tl" href="#prologo">Pr&oacute;logo</a></td><td class="pg"><a href="#prologo"></a></td></tr>'
                '%s</tbody></table></section>' % ("".join(toc)))
    prologo = prologo.replace('<section class="frontmatter">', '<section class="frontmatter" id="prologo">')

    html = ('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><style>%s</style></head><body>%s%s%s%s%s%s</body></html>'
            % (CSS + DOSSIER_CSS + BOOK_CSS + QUIZ_CSS, cover, credits, prologo, toc_html, "".join(units), gloss + biblio + indice))
    out = BASE / "PBM-libro.html"
    out.write_text(html, encoding="utf-8")
    from weasyprint import HTML
    HTML(str(out)).write_pdf(str(BASE / "PBM-libro.pdf"))
    print("PDF :", BASE / "PBM-libro.pdf", "| preguntas:", nq)

if __name__ == "__main__":
    main()
