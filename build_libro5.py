# -*- coding: utf-8 -*-
"""build_libro5.py - Edicion LIBRO final: + Apendice C 'Algoritmos en figura' (figuras.py),
indice analitico como Apendice D, y nota de fuentes en revision. Salida: PBM-libro.pdf"""
import pathlib
import build_libro4 as B
from build_doc import CSS
from build_dossier import DOSSIER_CSS, ANCLA, IDEACION, ORDER, get_title
import importlib, html as _html
import figuras

BASE = pathlib.Path(__file__).resolve().parent
esc = B.esc

def build_figuras():
    head = B.part_divider("Apendice C", "Algoritmos en figura", "Diagramas de flujo de los procesos clave de la serie.", "ap-fig")
    out = ['<div class="matter" id="cap-fig"><div class="matter-h">Algoritmos en figura</div>']
    for num, title, cap, svg in figuras.FIGURAS:
        out.append('<div class="figbox"><div class="fig-t">Figura %d. %s</div>%s<div class="fig-c">%s</div></div>'
                   % (num, esc(title), svg, cap))
    out.append('</div>')
    return head + "".join(out)

def build_indice_D():
    head = B.part_divider("Apendice D", "Indice analitico", "Terminos clave con la pagina del capitulo donde se desarrollan.", "ap-ix")
    entries = sorted(B.INDICE, key=lambda t: B.sortkey(_html.unescape(t[0])))
    out = ['<div class="matter" id="cap-ix"><div class="matter-h">&Iacute;ndice anal&iacute;tico</div><div class="ix">']
    cur = ""
    for term, code in entries:
        letter = B.sortkey(_html.unescape(term))[0].upper()
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
               '<b>Edici&oacute;n:</b> 2026 (v1.0). <b>Autor e ideaci&oacute;n:</b> Emilio Garc&iacute;a Hern&aacute;ndez (CAUSA / SACYL).</p>'
               '<p>Obra <b>docente</b> para anestesi&oacute;logos adjuntos y residentes; &uacute;til para hematolog&iacute;a, cirug&iacute;a y enfermer&iacute;a perioperatoria. '
               'Las cifras proceden de <b>fuentes primarias verificadas contra PubMed</b> y de gu&iacute;as de sociedad (AABB, ESAIC, EACTS, BSH, NBA).</p>'
               '<p><b>Fuentes en revisi&oacute;n (no indexadas en PubMed, pendientes de verificaci&oacute;n por su web oficial):</b> WHO <i>Guidance on Implementing PBM</i> (mar-2025); '
               'NICE NG24 (actualizaci&oacute;n TXA, borrador nov-2025); revisi&oacute;n de hierro en <i>Blood Transfusion</i> (ene-2025). No se citan como ancla hasta confirmarse.</p>'
               '<p><b>Aviso:</b> no es un dispositivo m&eacute;dico ni una gu&iacute;a oficial. <b>No sustituye al juicio cl&iacute;nico ni a los protocolos locales vigentes.</b> '
               'Pr&oacute;xima revisi&oacute;n prevista: 2027.</p>'
               '<p>%s</p></section>' % IDEACION)
    prologo = ('<section class="frontmatter" id="prologo"><h1 class="parttitle">Pr&oacute;logo</h1>'
               '<p>La transfusi&oacute;n es una de las terapias m&aacute;s usadas y, a la vez, una de las que m&aacute;s se beneficia de un cambio de enfoque. '
               'Este libro re&uacute;ne la serie formativa sobre <b>Patient Blood Management</b> y hemostasia perioperatoria en un solo volumen, '
               'organizado alrededor de los <b>tres pilares</b> del PBM m&aacute;s el <b>eje transversal de la hemostasia</b>.</p>'
               '<p>Cada cap&iacute;tulo mantiene un <b>tono honesto</b> sobre la evidencia: lo bien establecido (tranex&aacute;mico precoz, umbrales restrictivos, '
               'hierro en la ferropenia real) y lo m&aacute;s discutido (PREVENTT neutro, la excepci&oacute;n del SCA, la incertidumbre de la viscoel&aacute;stica o del rFVIIa). '
               'El objetivo no es transfundir menos por ahorro, sino <b>tratar mejor</b>.</p>'
               '<p>El volumen se cierra con un <b>cuestionario de 200 preguntas</b>, un <b>glosario</b>, la <b>bibliograf&iacute;a maestra</b>, los <b>algoritmos en figura</b> y un <b>&iacute;ndice anal&iacute;tico</b>.</p>'
               '<p style="text-align:right; font-style:italic">Emilio Garc&iacute;a Hern&aacute;ndez &middot; Salamanca, 2026</p></section>')

    units = []; toc = []
    for code, mod_name in ORDER:
        try: mod = importlib.import_module(mod_name)
        except ModuleNotFoundError: print("  [omitido]", code); continue
        if code in B.PARTS:
            num, title, desc, anchor = B.PARTS[code]
            units.append(B.part_divider(num, title, desc, anchor, first=(code == "PBM-01")))
            toc.append('<tr><td colspan="3" class="mod"><a class="tl" href="#%s">%s &mdash; %s</a></td></tr>' % (anchor, esc(num), esc(title)))
        units.append('<div class="doc-unit" id="cap-%s">%s%s%s<div class="footer-note">%s<br>%s</div></div>'
                     % (code, mod.COVER, mod.BODY, mod.REFS, mod.META["footer"], IDEACION))
        at, ac = ANCLA[code]
        toc.append('<tr><td class="c1">%s</td><td><a class="tl" href="#cap-%s">%s</a> <span class="bdg bg-%s" style="font-size:6.5pt;color:#fff;border-radius:3px;padding:0 4px">%s</span></td><td class="pg"><a href="#cap-%s"></a></td></tr>'
                   % (code, code, get_title(mod.COVER), ac, at, code))

    quiz, nq = B.build_quiz()
    units.append(quiz)
    toc.append('<tr><td colspan="3" class="mod"><a class="tl" href="#parte-7">Parte VII &mdash; Evaluaci&oacute;n</a></td></tr>')
    toc.append('<tr><td class="c1">EVAL</td><td><a class="tl" href="#cap-eval">Cuestionario (200 preguntas) + soluciones</a></td><td class="pg"><a href="#cap-eval"></a></td></tr>')

    gloss = B.build_glossary(); biblio = B.build_biblio(); figs = build_figuras(); indice = build_indice_D()
    toc.append('<tr><td colspan="3" class="mod">Ap&eacute;ndices</td></tr>')
    toc.append('<tr><td class="c1">A</td><td><a class="tl" href="#cap-glos">Glosario</a></td><td class="pg"><a href="#cap-glos"></a></td></tr>')
    toc.append('<tr><td class="c1">B</td><td><a class="tl" href="#cap-bib">Bibliograf&iacute;a maestra</a></td><td class="pg"><a href="#cap-bib"></a></td></tr>')
    toc.append('<tr><td class="c1">C</td><td><a class="tl" href="#cap-fig">Algoritmos en figura</a></td><td class="pg"><a href="#cap-fig"></a></td></tr>')
    toc.append('<tr><td class="c1">D</td><td><a class="tl" href="#cap-ix">&Iacute;ndice anal&iacute;tico</a></td><td class="pg"><a href="#cap-ix"></a></td></tr>')

    toc_html = ('<section class="dsr-toc"><h2>&Iacute;ndice tem&aacute;tico</h2><table class="dsrtoc"><tbody>'
                '<tr><td colspan="3" class="mod">Preliminares</td></tr>'
                '<tr><td class="c1">&middot;</td><td><a class="tl" href="#prologo">Pr&oacute;logo</a></td><td class="pg"><a href="#prologo"></a></td></tr>'
                '%s</tbody></table></section>' % ("".join(toc)))

    style = CSS + DOSSIER_CSS + B.BOOK_CSS + B.QUIZ_CSS + figuras.FIG_CSS
    html = ('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><style>%s</style></head><body>%s%s%s%s%s%s</body></html>'
            % (style, cover, credits, prologo, toc_html, "".join(units), gloss + biblio + figs + indice))
    out = BASE / "PBM-libro.html"
    out.write_text(html, encoding="utf-8")
    from weasyprint import HTML
    HTML(str(out)).write_pdf(str(BASE / "PBM-libro.pdf"))
    print("PDF :", BASE / "PBM-libro.pdf", "| preguntas:", nq, "| figuras:", len(figuras.FIGURAS))

if __name__ == "__main__":
    main()
