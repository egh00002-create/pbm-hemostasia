# -*- coding: utf-8 -*-
"""PBM-16 - Manejo perioperatorio de antiagregantes y anticoagulantes. Ancla GUIA."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-16 Manejo perioperatorio de antiagregantes y anticoagulantes. Ancla GUIA.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-16 - Modulo 5 (eje hemostasia) - ancla GUIA - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-16</span>
    <span class="badge b-guia">GU&Iacute;A &middot; gu&iacute;a / consenso formal</span>
    <span class="module-tag">M&oacute;dulo 5 &middot; Hemostasia clínica y riesgo hemorr&aacute;gico</span>
  </div>
  <div class="kicker">Antiagregantes &middot; Anticoagulantes &middot; Equilibrio trombosis&ndash;sangrado</div>
  <h1 class="title">Manejo perioperatorio de antiagregantes y anticoagulantes</h1>
  <div class="subtitle">Cada suspensi&oacute;n es una balanza: el riesgo de sangrar frente al riesgo de trombosar</div>
  <div class="meta-row">
    <span class="meta-chip">El doble riesgo</span>
    <span class="meta-chip">Antiagregantes</span>
    <span class="meta-chip">Anticoagulantes (AVK y ACOD)</span>
    <span class="meta-chip">El mito del puente</span>
    <span class="meta-chip">Reanudaci&oacute;n</span>
  </div>
  <div class="refbar guiabar">
    <b>Ancla de evidencia (referencia vertebral):</b> Douketis JD, Spyropoulos AC, Kaatz S, et&nbsp;al.
    <i>Perioperative Bridging Anticoagulation in Patients with Atrial Fibrillation (BRIDGE).</i>
    N Engl J Med 2015;373(9):823&ndash;833. <span class="mono">doi:10.1056/NEJMoa1501035 &middot; PMID&nbsp;26095867</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> el manejo perioperatorio de antitrombóticos equilibra dos riesgos opuestos &mdash;<b>trombosis</b> si se
    suspenden y <b>hemorragia</b> si se mantienen&mdash;. La decisi&oacute;n depende del f&aacute;rmaco, del riesgo trombótico del paciente y del
    riesgo hemorr&aacute;gico del procedimiento. El ensayo BRIDGE desmont&oacute; el <b>puente sistem&aacute;tico</b> con heparina en fibrilaci&oacute;n
    auricular.
  </div>
  <div class="lead">
    <p>Cada vez m&aacute;s pacientes quir&uacute;rgicos toman antiagregantes o anticoagulantes. Decidir si suspenderlos, cu&aacute;ndo y si hace
    falta &laquo;puente&raquo; es una de las consultas perioperatorias m&aacute;s frecuentes &mdash;y una balanza entre <b>sangrar</b> y
    <b>trombosar</b>&mdash;.</p>
    <p>Este documento, con ancla <b>GUÍA</b>, ofrece el marco de decisi&oacute;n por familias de f&aacute;rmacos, integra la evidencia clave
    (BRIDGE) y subraya un principio: la conducta se <b>individualiza</b> seg&uacute;n el riesgo trombótico del paciente y el
    hemorr&aacute;gico del procedimiento, siempre conforme al protocolo local.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>El doble riesgo: trombosis frente a sangrado</li>
  <li>Antiagregantes</li>
  <li>Anticoagulantes: AVK y ACOD</li>
  <li>El mito del puente: la lecci&oacute;n de BRIDGE</li>
  <li>Reanudaci&oacute;n postoperatoria</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>El doble riesgo: trombosis frente a sangrado</h2>
<p>Toda decisi&oacute;n sobre antitrombóticos perioperatorios es un <b>balance</b>: suspender reduce el sangrado pero expone a
<b>trombosis</b> (ictus, s&iacute;ndrome coronario, tromboembolismo); mantener protege de la trombosis pero aumenta la
<b>hemorragia</b>. La conducta correcta cruza tres ejes: el <b>f&aacute;rmaco</b> (y su vida media), el <b>riesgo trombótico</b> del
paciente (motivo de la terapia) y el <b>riesgo hemorr&aacute;gico</b> del procedimiento [2].</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>Decisi&oacute;n individualizada: <b>f&aacute;rmaco &times; riesgo trombótico &times; riesgo hemorr&aacute;gico</b> [2].</li>
  <li>Muchos procedimientos de bajo riesgo hemorr&aacute;gico <b>no exigen suspender</b> la terapia.</li>
  <li>El <b>puente</b> sistem&aacute;tico con heparina suele a&ntilde;adir sangrado sin reducir la trombosis [1].</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Antiagregantes</h2>
<p>En la antiagregaci&oacute;n, la <b>aspirina</b> en prevenci&oacute;n secundaria a menudo puede <b>mantenerse</b> en cirug&iacute;a de riesgo
hemorr&aacute;gico bajo-moderado, mientras que los inhibidores de P2Y<sub>12</sub> (clopidogrel, ticagrelor, prasugrel) suelen
<b>suspenderse</b> unos d&iacute;as antes de cirug&iacute;a mayor por su mayor efecto hemorr&aacute;gico. El caso crítico es el paciente con
<b>stent coronario reciente</b> bajo doble antiagregaci&oacute;n: posponer la cirug&iacute;a electiva hasta superar el periodo de riesgo
de trombosis del stent y, si es inaplazable, decidir en equipo (cardiolog&iacute;a) [2].</p>

<h2 class="sec"><span class="num">3.</span>Anticoagulantes: AVK y ACOD</h2>
<p>Los <b>antagonistas de la vitamina K</b> (warfarina, acenocumarol) requieren suspensi&oacute;n con varios d&iacute;as de antelaci&oacute;n y
control del INR; su efecto se revierte, si urge, con <b>concentrado de complejo protrombínico</b> y vitamina K (PBM-18). Los
<b>anticoagulantes orales de acci&oacute;n directa (ACOD)</b> tienen vida media corta y manejo m&aacute;s predecible: se suspenden un
n&uacute;mero de d&iacute;as seg&uacute;n el f&aacute;rmaco, la funci&oacute;n renal y el riesgo hemorr&aacute;gico del procedimiento, habitualmente <b>sin necesidad
de puente</b> [2]. Existen agentes de reversi&oacute;n espec&iacute;ficos para situaciones de hemorragia grave (PBM-18).</p>

<h2 class="sec"><span class="num">4.</span>El mito del puente: la lecci&oacute;n de BRIDGE</h2>
<p>El ensayo <b>BRIDGE</b> (1.884 pacientes con fibrilaci&oacute;n auricular que interrump&iacute;an warfarina) compar&oacute; <b>puente</b> con
heparina de bajo peso molecular frente a <b>no puente</b>. No hacer puente fue <b>no inferior</b> para tromboembolismo
arterial (0,4&nbsp;% vs 0,3&nbsp;%) y <b>redujo la hemorragia mayor</b> (1,3&nbsp;% vs 3,2&nbsp;%; RR 0,41) [1]. Conclusi&oacute;n pr&aacute;ctica: en
la mayor&iacute;a de los pacientes con FA, <b>el puente sistem&aacute;tico a&ntilde;ade sangrado sin proteger de la trombosis</b>; se reserva para
casos de riesgo trombótico muy alto seleccionados.</p>

<div class="box alert avoid-break"><span class="box-h">Cambio de conducta</span>
  <p>BRIDGE invirti&oacute; una pr&aacute;ctica arraigada: el &laquo;puente para todos&raquo; con heparina en FA es <b>perjudicial</b> en la mayor&iacute;a.
  El puente queda para indicaciones de muy alto riesgo trombótico, valoradas individualmente [1].</p>
</div>

<h2 class="sec"><span class="num">5.</span>Reanudaci&oacute;n postoperatoria</h2>
<p>La reanudaci&oacute;n debe equilibrar la <b>hemostasia quir&uacute;rgica lograda</b> con el riesgo trombótico: se reinician los
antitrombóticos cuando el riesgo de sangrado postoperatorio es aceptable, de forma escalonada y seg&uacute;n el procedimiento.
La <b>comunicaci&oacute;n entre equipos</b> (anestesia, cirug&iacute;a, cardiolog&iacute;a/hematolog&iacute;a) y la adhesi&oacute;n al protocolo local son
esenciales para no dejar ventanas de riesgo [2].</p>

<h2 class="sec"><span class="num">6.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> el manejo de antitrombóticos perioperatorios es un balance individualizado entre
trombosis y sangrado que depende del f&aacute;rmaco, del paciente y del procedimiento; muchos procedimientos de bajo riesgo no
exigen suspender, y el <b>puente sistem&aacute;tico</b> con heparina en FA es perjudicial salvo en alto riesgo trombótico
(BRIDGE).</p>
<p>Conecta con <b>PBM-15</b> (cribado del riesgo hemorr&aacute;gico), <b>PBM-18</b> (reversi&oacute;n: CCP, agentes espec&iacute;ficos) y con
<b>PBM-13</b> (hemorragia grave bajo antitrombóticos). Resumen operativo en <b>P-QR-05</b>.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Decide f&aacute;rmaco a f&aacute;rmaco seg&uacute;n riesgo trombótico y hemorr&aacute;gico &mdash;mant&eacute;n la aspirina cuando puedas, suspende los ACOD
  seg&uacute;n vida media y funci&oacute;n renal, y evita el puente sistem&aacute;tico en FA&mdash;.</p>
</div>

<h2 class="sec"><span class="num">7.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>GUÍA</b> apoyado en BRIDGE [1], la gu&iacute;a ESAIC [2] y la gu&iacute;a EACTS/EACTAIC 2024 [3], verificados contra PubMed
(autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Las cifras de BRIDGE (tromboembolismo 0,4 vs 0,3&nbsp;%; hemorragia mayor 1,3 vs
3,2&nbsp;%, RR 0,41) [1] proceden de la fuente. Los tiempos exactos de suspensi&oacute;n por f&aacute;rmaco deben tomarse de los protocolos
locales y la ficha t&eacute;cnica vigentes; aqu&iacute; se da el marco de decisi&oacute;n, no dosis-d&iacute;a concretas.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">8.</span>Referencias</h2>
<ol class="refs">
  <li>Douketis JD, Spyropoulos AC, Kaatz S, Becker RC, Caprini JA, Dunn AS, et al. Perioperative Bridging Anticoagulation in Patients with Atrial Fibrillation. <i>N Engl J Med</i> 2015;373(9):823&ndash;833. <span class="doi">doi:10.1056/NEJMoa1501035</span> &middot; PMID 26095867.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
  <li>Casselman FPA, Lance MD, Ahmed A, Ascari A, Blanco-Morillo J, Bolliger D, et al. 2024 EACTS/EACTAIC Guidelines on patient blood management in adult cardiac surgery in collaboration with EBCP. <i>Eur J Cardiothorac Surg</i> 2025;67(5):ezae352. <span class="doi">doi:10.1093/ejcts/ezae352</span> &middot; PMID 39385500.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-16-antiagregantes-anticoagulantes.html")
    print("HTML:", h); print("PDF :", p)
