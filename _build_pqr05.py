# -*- coding: utf-8 -*-
"""P-QR-05 - Manejo de antitromboticos segun farmaco y riesgo. Ancla ALG."""
from build_doc import build

META = {
    "comment": "SERIE PBM - P-QR-05 Manejo de antitromboticos segun farmaco y riesgo. Ancla ALG.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Tarjeta P-QR-05 - ancla ALG - 2026. "
               "Tarjeta de consulta rapida; sintetiza PBM-16. Marco de decision verificado contra PubMed. "
               "Los tiempos exactos de suspension se toman del protocolo local y la ficha tecnica vigentes. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">P-QR-05</span>
    <span class="badge b-alg">ALG &middot; tarjeta de consulta r&aacute;pida</span>
    <span class="module-tag">Quick-reference &middot; sintetiza PBM-16</span>
  </div>
  <div class="kicker">Antitrombóticos &middot; Marco de decisi&oacute;n perioperatorio</div>
  <h1 class="title">Manejo de antitrombóticos seg&uacute;n f&aacute;rmaco y riesgo</h1>
  <div class="subtitle">Tarjeta de consulta r&aacute;pida &mdash; balance trombosis vs sangrado, individualizado</div>
  <div class="tagline">
    2026 &middot; Tarjeta derivada de PBM-16 &middot; CAUSA / SACYL<br>
    <b>Idea:</b> decidir por <b>f&aacute;rmaco &times; riesgo trombótico &times; riesgo hemorr&aacute;gico</b>. Tiempos exactos: protocolo local.
  </div>
</section>
"""

BODY = r"""
<div class="tbl-title">Marco de decisi&oacute;n por familia de f&aacute;rmaco</div>
<table class="avoid-break">
  <thead><tr><th style="width:24%">F&aacute;rmaco</th><th>Conducta general perioperatoria</th></tr></thead>
  <tbody>
    <tr><td><b>Aspirina (prev. 2.&ordf;)</b></td><td>A menudo <b>mantener</b> en riesgo hemorr&aacute;gico bajo-moderado; valorar seg&uacute;n procedimiento.</td></tr>
    <tr><td><b>Inhibidores P2Y<sub>12</sub></b> (clopidogrel, ticagrelor, prasugrel)</td><td><b>Suspender</b> unos d&iacute;as antes de cirug&iacute;a mayor; decisi&oacute;n en equipo si stent reciente.</td></tr>
    <tr><td><b>Doble antiagregaci&oacute;n + stent reciente</b></td><td><b>Posponer</b> la cirug&iacute;a electiva; si inaplazable, decisi&oacute;n multidisciplinar (cardiolog&iacute;a).</td></tr>
    <tr><td><b>AVK</b> (warfarina, acenocumarol)</td><td>Suspender con antelaci&oacute;n, controlar INR; reversi&oacute;n urgente con <b>CCP + vitamina K</b>.</td></tr>
    <tr><td><b>ACOD</b> (apixab&aacute;n, rivaroxab&aacute;n, edoxab&aacute;n, dabigatr&aacute;n)</td><td>Suspender seg&uacute;n f&aacute;rmaco, funci&oacute;n renal y riesgo hemorr&aacute;gico; <b>habitualmente sin puente</b>.</td></tr>
  </tbody>
  <caption>Marco de decisi&oacute;n [1,2]; los <b>tiempos exactos de suspensi&oacute;n</b> se toman del protocolo local y la ficha t&eacute;cnica.</caption>
</table>

<div class="box alert avoid-break"><span class="box-h">El mito del puente (BRIDGE)</span>
  <p>En fibrilaci&oacute;n auricular, <b>no</b> hacer puente con heparina fue no inferior para tromboembolismo (0,4 vs 0,3&nbsp;%) y
  <b>redujo la hemorragia mayor</b> (1,3 vs 3,2&nbsp;%; RR 0,41) [1]. El puente sistem&aacute;tico <b>a&ntilde;ade sangrado sin proteger</b>;
  resérvalo para alto riesgo trombótico seleccionado.</p>
</div>

<div class="box key avoid-break"><span class="box-h">Tres preguntas antes de decidir</span><ul>
  <li>&iquest;Qu&eacute; <b>f&aacute;rmaco</b> y con qu&eacute; vida media (y funci&oacute;n renal)?</li>
  <li>&iquest;Qu&eacute; <b>riesgo trombótico</b> tiene el paciente (motivo de la terapia)?</li>
  <li>&iquest;Qu&eacute; <b>riesgo hemorr&aacute;gico</b> tiene el procedimiento?</li>
</ul></div>

<div class="box pearl avoid-break"><span class="box-h">Reanudaci&oacute;n</span>
  <p>Reiniciar cuando la hemostasia quir&uacute;rgica lo permita, de forma escalonada y coordinada entre equipos. Reversi&oacute;n y
  rescate: &rarr; PBM-18 (CCP, agentes espec&iacute;ficos).</p>
</div>
"""

REFS = r"""
<h2 class="sec"><span class="num">&middot;</span>Referencias</h2>
<ol class="refs">
  <li>Douketis JD, Spyropoulos AC, Kaatz S, et al. Perioperative Bridging Anticoagulation in Patients with Atrial Fibrillation (BRIDGE). <i>N Engl J Med</i> 2015;373(9):823&ndash;833. <span class="doi">doi:10.1056/NEJMoa1501035</span> &middot; PMID 26095867.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, et al. Management of severe peri-operative bleeding: ESAIC Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "P-QR-05-antitromboticos.html")
    print("HTML:", h); print("PDF :", p)
