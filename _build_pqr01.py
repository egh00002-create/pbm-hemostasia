# -*- coding: utf-8 -*-
"""P-QR-01 - Los 3 pilares del PBM de un vistazo. Ancla ALG."""
from build_doc import build

META = {
    "comment": "SERIE PBM - P-QR-01 Los 3 pilares del PBM de un vistazo. Ancla ALG.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Tarjeta P-QR-01 - ancla ALG - 2026. "
               "Tarjeta de consulta rapida; sintetiza PBM-01. No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">P-QR-01</span>
    <span class="badge b-alg">ALG &middot; tarjeta de consulta r&aacute;pida</span>
    <span class="module-tag">Quick-reference &middot; sintetiza PBM-01</span>
  </div>
  <div class="kicker">Los 3 pilares del PBM de un vistazo</div>
  <h1 class="title">Los 3 pilares del PBM de un vistazo</h1>
  <div class="subtitle">Tarjeta de consulta r&aacute;pida &mdash; el marco conceptual de toda la serie en una p&aacute;gina</div>
  <div class="tagline">
    2026 &middot; Tarjeta derivada de PBM-01 &middot; CAUSA / SACYL<br>
    <b>Idea:</b> gestionar la sangre del paciente en tres pilares + el eje de la hemostasia; transfundir solo cuando aporta beneficio.
  </div>
</section>
"""

BODY = r"""
<div class="pillars avoid-break">
  <div class="pillar"><h4>Pilar 1 &middot; Masa eritrocitaria</h4><b>Optimizar</b>: detectar y tratar la <b>anemia preoperatoria</b>
    (ferropenia, hierro, EPO) con tiempo. <span class="mono">&rarr; PBM-04 a 06</span></div>
  <div class="pillar"><h4>Pilar 2 &middot; P&eacute;rdida sangu&iacute;nea</h4><b>Minimizar</b>: hemostasia quir&uacute;rgica, <b>tranex&aacute;mico</b>,
    viscoel&aacute;stica, recuperador celular, MABL. <span class="mono">&rarr; PBM-07 a 11</span></div>
  <div class="pillar p5"><h4>Pilar 3 &middot; Tolerancia a la anemia</h4><b>Tolerar</b>: umbrales <b>restrictivos</b> y soporte
    fisiol&oacute;gico de la entrega de ox&iacute;geno. <span class="mono">&rarr; PBM-12 a 14</span></div>
</div>

<div class="box key avoid-break"><span class="box-h">Eje transversal &middot; Hemostasia y sangrado</span>
  <p>Cribado del riesgo hemorr&aacute;gico (HEMSTOP), manejo de antitrombóticos, coagulopat&iacute;as y f&aacute;rmacos hemost&aacute;ticos.
  <span class="mono">&rarr; PBM-15 a 18</span></p>
</div>

<div class="tbl-title">Qu&eacute; hacer en cada momento del periodo perioperatorio</div>
<table class="avoid-break">
  <thead><tr><th style="width:16%">Momento</th><th>Pilar 1 (masa)</th><th>Pilar 2 (p&eacute;rdida)</th><th>Pilar 3 (tolerancia)</th></tr></thead>
  <tbody>
    <tr><td><b>Preoperatorio</b></td><td>Cribar y tratar anemia/ferropenia con tiempo</td><td>Revisar antitrombóticos; planificar (MABL)</td><td>Definir umbral diana seg&uacute;n contexto</td></tr>
    <tr><td><b>Intraoperatorio</b></td><td>&mdash;</td><td>Tranex&aacute;mico, recuperador, viscoel&aacute;stica, normotermia</td><td>Normovolemia, oxigenaci&oacute;n, menor consumo</td></tr>
    <tr><td><b>Postoperatorio</b></td><td>Tratar anemia postoperatoria</td><td>Vigilar sangrado; reanudar antitrombóticos</td><td>Umbral restrictivo; transfusi&oacute;n unitaria</td></tr>
  </tbody>
  <caption>S&iacute;ntesis docente de los 3 pilares [1,2]. Detalle y excepciones en los documentos correspondientes (p.&nbsp;ej. SCA en PBM-12).</caption>
</table>

<div class="box pearl avoid-break"><span class="box-h">Regla de oro</span>
  <p>La mejor unidad de sangre es la que <b>no hace falta transfundir</b>: optimiza la masa, minimiza la p&eacute;rdida y tolera la anemia.</p>
</div>
"""

REFS = r"""
<h2 class="sec"><span class="num">&middot;</span>Referencias</h2>
<ol class="refs">
  <li>Mueller MM, Van Remoortel H, Meybohm P, Aranko K, Aubron C, Burger R, et al. Patient Blood Management: Recommendations From the 2018 Frankfurt Consensus Conference. <i>JAMA</i> 2019;321(10):983&ndash;997. <span class="doi">doi:10.1001/jama.2019.0554</span> &middot; PMID 30860564.</li>
  <li>Althoff FC, Neb H, Herrmann E, Trentino KM, Vernich L, F&uuml;llenbach C, et al. Multimodal Patient Blood Management Program Based on a Three-pillar Strategy: A Systematic Review and Meta-analysis. <i>Ann Surg</i> 2019;269(5):794&ndash;804. <span class="doi">doi:10.1097/SLA.0000000000003095</span> &middot; PMID 30418206.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "P-QR-01-tres-pilares.html")
    print("HTML:", h); print("PDF :", p)
