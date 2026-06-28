# -*- coding: utf-8 -*-
"""PBM-07 - Hemostasia perioperatoria: fisiologia y estrategia de minimizacion. Ancla REV."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-07 Hemostasia perioperatoria. Ancla REV.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-07 - Modulo 3 (Pilar 2) - ancla REV - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de guias y fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-07</span>
    <span class="badge b-rev">REV &middot; revisi&oacute;n / s&iacute;ntesis</span>
    <span class="module-tag">M&oacute;dulo 3 &middot; Pilar 2: minimizar la p&eacute;rdida sangu&iacute;nea</span>
  </div>
  <div class="kicker">Hemostasia perioperatoria &middot; Fisiolog&iacute;a &middot; Estrategia multimodal</div>
  <h1 class="title">Hemostasia perioperatoria: fisiolog&iacute;a y estrategia de minimizaci&oacute;n</h1>
  <div class="subtitle">Minimizar el sangrado no es un solo gesto: es un paquete de medidas a lo largo de todo el periodo</div>
  <div class="meta-row">
    <span class="meta-chip">Fisiolog&iacute;a de la hemostasia</span>
    <span class="meta-chip">El modelo celular</span>
    <span class="meta-chip">Determinantes del sangrado</span>
    <span class="meta-chip">Estrategia multimodal</span>
    <span class="meta-chip">Normotermia, pH, calcio</span>
  </div>
  <div class="refbar">
    <b>Ancla de evidencia (referencia vertebral):</b> Kietaibl S, Ahmed A, Afshari A, et&nbsp;al.
    <i>Management of severe peri-operative bleeding: Guidelines from the ESAIC: Second update 2022.</i>
    Eur J Anaesthesiol 2023;40(4):226&ndash;304. <span class="mono">doi:10.1097/EJA.0000000000001803 &middot; PMID&nbsp;36855941</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> el sangrado perioperatorio se minimiza con una <b>estrategia multimodal</b>, no con una sola
    medida: hemostasia quir&uacute;rgica meticulosa, antifibrinol&iacute;ticos, mantenimiento del &laquo;entorno&raquo; de la coagulaci&oacute;n
    (<b>normotermia, pH, calcio</b>) y correcci&oacute;n dirigida de los d&eacute;ficits. Comprender la fisiolog&iacute;a permite intervenir en
    el eslab&oacute;n correcto.
  </div>
  <div class="lead">
    <p>El <b>pilar 2</b> del PBM &mdash;minimizar la p&eacute;rdida sangu&iacute;nea&mdash; descansa sobre la comprensi&oacute;n de la hemostasia. La
    coagulaci&oacute;n no es una cascada aislada en un tubo: es un proceso <b>celular</b>, dependiente de plaquetas, factores,
    fibrin&oacute;geno y de un entorno fisiol&oacute;gico adecuado.</p>
    <p>Esta revisi&oacute;n abre el m&oacute;dulo fijando la <b>fisiolog&iacute;a</b> y la <b>estrategia general</b> de minimizaci&oacute;n; las
    herramientas concretas &mdash;tranex&aacute;mico, viscoel&aacute;stica, recuperador celular, MABL&mdash; se desarrollan en PBM-08 a PBM-11.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>Fisiolog&iacute;a: el modelo celular de la hemostasia</li>
  <li>Qu&eacute; determina el sangrado quir&uacute;rgico</li>
  <li>El &laquo;entorno&raquo; de la coagulaci&oacute;n: normotermia, pH, calcio</li>
  <li>La estrategia multimodal de minimizaci&oacute;n</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>Fisiolog&iacute;a: el modelo celular de la hemostasia</h2>
<p>La hemostasia combina la <b>hemostasia primaria</b> (plaquetas + factor de von Willebrand forman el tap&oacute;n) y la
<b>secundaria</b> (la cascada de factores genera trombina, que convierte el fibrin&oacute;geno en fibrina). El modelo moderno es
<b>celular</b>: iniciaci&oacute;n sobre la c&eacute;lula portadora de factor tisular, amplificaci&oacute;n y propagaci&oacute;n sobre la superficie
plaquetaria, con un papel central de la <b>trombina</b> y del <b>fibrin&oacute;geno</b> como sustrato final [1]. La
<b>fibrin&oacute;lisis</b> (plasmina) regula y disuelve el co&aacute;gulo; su exceso perioperatorio favorece el sangrado &mdash;de ah&iacute; el
valor de los antifibrinol&iacute;ticos (PBM-08)&mdash;.</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>La hemostasia es <b>celular</b>: plaquetas, factores y fibrin&oacute;geno actuando sobre superficies, no una cascada aislada.</li>
  <li>El <b>fibrin&oacute;geno</b> es el primer factor que cae en la hemorragia masiva; su reposici&oacute;n es prioritaria (PBM-02, PBM-18).</li>
  <li>La <b>hiperfibrin&oacute;lisis</b> agrava el sangrado: justifica el uso de antifibrinol&iacute;ticos (PBM-08).</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Qu&eacute; determina el sangrado quir&uacute;rgico</h2>
<p>El sangrado perioperatorio resulta de la interacci&oacute;n entre el <b>componente quir&uacute;rgico</b> (t&eacute;cnica, hemostasia
mec&aacute;nica, anatom&iacute;a) y el <b>componente hemost&aacute;tico</b> del paciente (plaquetas, factores, f&aacute;rmacos antitrombóticos,
coagulopat&iacute;a). Distinguir un sangrado <b>quir&uacute;rgico</b> (que requiere control mec&aacute;nico) de uno <b>coagulop&aacute;tico</b> (que
requiere correcci&oacute;n hemost&aacute;tica) es una decisi&oacute;n cl&iacute;nica clave que la viscoel&aacute;stica ayuda a orientar (PBM-09) [1].</p>

<h2 class="sec"><span class="num">3.</span>El &laquo;entorno&raquo; de la coagulaci&oacute;n: normotermia, pH, calcio</h2>
<p>La cascada enzim&aacute;tica de la coagulaci&oacute;n depende de condiciones fisiol&oacute;gicas. La <b>tr&iacute;ada letal</b> &mdash;hipotermia,
acidosis y coagulopat&iacute;a&mdash; describe c&oacute;mo el fr&iacute;o y el pH bajo deterioran la funci&oacute;n de factores y plaquetas. A ello se
suma el <b>calcio i&oacute;nico</b> (factor IV), imprescindible para la coagulaci&oacute;n y consumido/quelado en la transfusi&oacute;n masiva.
Mantener <b>normotermia, corregir la acidosis y vigilar el calcio</b> es hemostasia b&aacute;sica y barata [1].</p>

<div class="box pearl avoid-break"><span class="box-h">Perla</span>
  <p>Antes de pedir m&aacute;s hemoderivados ante un sangrado &laquo;que no para&raquo;, comprueba lo barato: <b>temperatura, pH y calcio
  i&oacute;nico</b>. Un paciente fr&iacute;o, acid&oacute;tico e hipocalc&eacute;mico no coagula por mucho factor que reciba [1].</p>
</div>

<h2 class="sec"><span class="num">4.</span>La estrategia multimodal de minimizaci&oacute;n</h2>
<div class="tbl-title">Tabla 1 &middot; Paquete multimodal de minimizaci&oacute;n del sangrado (pilar 2)</div>
<table class="avoid-break">
  <thead><tr><th style="width:26%">Medida</th><th>Contenido</th><th style="width:16%">Documento</th></tr></thead>
  <tbody>
    <tr><td><b>Hemostasia quir&uacute;rgica</b></td><td>T&eacute;cnica meticulosa, dispositivos de sellado, posici&oacute;n, control de la presi&oacute;n.</td><td class="c">PBM-07</td></tr>
    <tr><td><b>Antifibrinol&iacute;ticos</b></td><td>&Aacute;cido tranex&aacute;mico de forma amplia en cirug&iacute;a con sangrado relevante.</td><td class="c">PBM-08</td></tr>
    <tr><td><b>Monitorizaci&oacute;n dirigida</b></td><td>Viscoel&aacute;stica (ROTEM/TEG) para guiar la correcci&oacute;n por componentes.</td><td class="c">PBM-09</td></tr>
    <tr><td><b>Ahorro de sangre</b></td><td>Recuperador celular, hemodiluci&oacute;n, t&eacute;cnicas anest&eacute;sicas.</td><td class="c">PBM-10</td></tr>
    <tr><td><b>Planificaci&oacute;n</b></td><td>P&eacute;rdida admisible (MABL), disponibilidad, l&iacute;mites de transfusi&oacute;n.</td><td class="c">PBM-11</td></tr>
    <tr><td><b>Entorno fisiol&oacute;gico</b></td><td>Normotermia, correcci&oacute;n de pH, calcio i&oacute;nico.</td><td class="c">PBM-07</td></tr>
  </tbody>
  <caption>El pilar 2 es un <b>paquete</b>: su efecto procede de la suma de medidas, no de una sola [1]. Cada fila se desarrolla en su documento.</caption>
</table>

<h2 class="sec"><span class="num">5.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> minimizar el sangrado es una <b>estrategia multimodal</b> que combina control
quir&uacute;rgico, antifibrinol&iacute;ticos, monitorizaci&oacute;n dirigida, ahorro de sangre, planificaci&oacute;n y un entorno fisiol&oacute;gico
adecuado. Comprender la hemostasia celular permite intervenir en el eslab&oacute;n correcto y distinguir el sangrado quir&uacute;rgico del
coagulop&aacute;tico.</p>
<p>Conecta con todo el M&oacute;dulo 3 (<b>PBM-08 a PBM-11</b>), con <b>PBM-13</b> (hemorragia masiva) y con el eje de hemostasia
del M&oacute;dulo 5; comparte fisiolog&iacute;a con <b>PBM-17/18</b>.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Minimiza el sangrado con un paquete: cirug&iacute;a cuidadosa + tranex&aacute;mico + monitorizaci&oacute;n + ahorro de sangre +
  planificaci&oacute;n, sobre una base de normotermia, pH y calcio.</p>
</div>

<h2 class="sec"><span class="num">6.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento de tipo <b>REV</b>, anclado en la gu&iacute;a ESAIC de sangrado perioperatorio grave [1], el consenso de Frankfurt [2]
y la gu&iacute;a EACTS 2024 [3], verificados contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Los conceptos
fisiol&oacute;gicos (modelo celular, tr&iacute;ada letal, papel del fibrin&oacute;geno y del calcio) son consenso establecido recogido en estas
fuentes.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">7.</span>Referencias</h2>
<ol class="refs">
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
  <li>Mueller MM, Van Remoortel H, Meybohm P, Aranko K, Aubron C, Burger R, et al. Patient Blood Management: Recommendations From the 2018 Frankfurt Consensus Conference. <i>JAMA</i> 2019;321(10):983&ndash;997. <span class="doi">doi:10.1001/jama.2019.0554</span> &middot; PMID 30860564.</li>
  <li>Casselman FPA, Lance MD, Ahmed A, Ascari A, Blanco-Morillo J, Bolliger D, et al. 2024 EACTS/EACTAIC Guidelines on patient blood management in adult cardiac surgery in collaboration with EBCP. <i>Eur J Cardiothorac Surg</i> 2025;67(5):ezae352. <span class="doi">doi:10.1093/ejcts/ezae352</span> &middot; PMID 39385500.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-07-hemostasia-perioperatoria.html")
    print("HTML:", h); print("PDF :", p)
