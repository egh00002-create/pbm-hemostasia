# -*- coding: utf-8 -*-
"""PBM-14 - Optimizacion de la tolerancia a la anemia: fisiologia y limites. Ancla REV."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-14 Tolerancia a la anemia. Ancla REV.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-14 - Modulo 4 (Pilar 3) - ancla REV - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-14</span>
    <span class="badge b-rev">REV &middot; revisi&oacute;n / s&iacute;ntesis</span>
    <span class="module-tag">M&oacute;dulo 4 &middot; Pilar 3: tolerancia a la anemia y transfusi&oacute;n</span>
  </div>
  <div class="kicker">Tolerancia a la anemia &middot; Entrega de ox&iacute;geno &middot; L&iacute;mites fisiol&oacute;gicos</div>
  <h1 class="title">Optimizaci&oacute;n de la tolerancia a la anemia: fisiolog&iacute;a y l&iacute;mites</h1>
  <div class="subtitle">Por qu&eacute; los umbrales restrictivos funcionan &mdash; y d&oacute;nde est&aacute; el l&iacute;mite de lo tolerable</div>
  <div class="meta-row">
    <span class="meta-chip">Entrega de ox&iacute;geno (DO<sub>2</sub>)</span>
    <span class="meta-chip">Mecanismos compensatorios</span>
    <span class="meta-chip">Anemia crítica</span>
    <span class="meta-chip">C&oacute;mo optimizar la tolerancia</span>
    <span class="meta-chip">L&iacute;mites por paciente</span>
  </div>
  <div class="refbar">
    <b>Ancla de evidencia (referencia vertebral):</b> Carson JL, Stanworth SJ, Dennis JA, et&nbsp;al.
    <i>Transfusion thresholds and other strategies for guiding red blood cell transfusion.</i>
    Cochrane Database Syst Rev 2025;10(10):CD002042. <span class="mono">doi:10.1002/14651858.CD002042.pub6 &middot; PMID&nbsp;41114449</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> el organismo <b>tolera</b> grados moderados de anemia gracias a mecanismos compensatorios que
    mantienen la entrega de ox&iacute;geno; optimizar esa tolerancia (normovolemia, ox&iacute;geno, reducir consumo) es la base
    fisiol&oacute;gica del pilar 3. Pero la tolerancia tiene <b>l&iacute;mites</b> que dependen del paciente &mdash;sobre todo la reserva
    cardíaca y coronaria&mdash;.
  </div>
  <div class="lead">
    <p>El tercer pilar del PBM &mdash;optimizar y tolerar la anemia&mdash; descansa en una pregunta fisiol&oacute;gica: &iquest;por qu&eacute; un paciente
    soporta una Hb de 7&nbsp;g/dl sin da&ntilde;o? La respuesta est&aacute; en la <b>entrega de ox&iacute;geno</b> y en los mecanismos que la
    preservan cuando cae la hemoglobina.</p>
    <p>Esta revisi&oacute;n explica la fisiolog&iacute;a de la tolerancia a la anemia, c&oacute;mo optimizarla y, con honestidad, d&oacute;nde est&aacute;n sus
    <b>l&iacute;mites</b> &mdash;el sustrato fisiol&oacute;gico que justifica los umbrales de PBM-12 y sus excepciones&mdash;.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>La entrega de ox&iacute;geno y sus determinantes</li>
  <li>Mecanismos compensatorios de la anemia</li>
  <li>La anemia crítica: d&oacute;nde falla la compensaci&oacute;n</li>
  <li>C&oacute;mo optimizar la tolerancia</li>
  <li>L&iacute;mites por paciente</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>La entrega de ox&iacute;geno y sus determinantes</h2>
<p>La <b>entrega de ox&iacute;geno (DO<sub>2</sub>)</b> es el producto del gasto cardíaco por el contenido arterial de ox&iacute;geno, que
depende sobre todo de la <b>hemoglobina</b> y su saturaci&oacute;n. Cuando la Hb cae, la DO<sub>2</sub> tiende a bajar, pero el
organismo dispone de un amplio margen porque en reposo la <b>extracci&oacute;n</b> tisular de ox&iacute;geno es baja (&asymp; 25&nbsp;%): hay
reserva para extraer m&aacute;s [1].</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>La DO<sub>2</sub> depende del <b>gasto cardíaco</b> y del <b>contenido arterial de O<sub>2</sub></b> (Hb y SaO<sub>2</sub>).</li>
  <li>La anemia se compensa aumentando el gasto y la <b>extracci&oacute;n</b> de ox&iacute;geno; por eso se tolera hasta cierto punto [1].</li>
  <li>El <b>l&iacute;mite</b> lo marca la reserva cardíaca/coronaria: por eso el SCA es la gran excepci&oacute;n (PBM-12).</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Mecanismos compensatorios de la anemia</h2>
<p>Ante la anemia normovol&eacute;mica, el organismo: <b>aumenta el gasto cardíaco</b> (mayor frecuencia y volumen sist&oacute;lico,
favorecido por la menor viscosidad), <b>redistribuye</b> el flujo a &oacute;rganos vitales, <b>incrementa la extracci&oacute;n</b> de
ox&iacute;geno y, a medio plazo, eleva el <b>2,3-DPG</b> desplazando la curva de disociaci&oacute;n para ceder m&aacute;s ox&iacute;geno a los
tejidos [1]. La <b>normovolemia</b> es condici&oacute;n indispensable: la hipovolemia anula estas compensaciones.</p>

<h2 class="sec"><span class="num">3.</span>La anemia crítica: d&oacute;nde falla la compensaci&oacute;n</h2>
<p>Existe un punto &mdash;la <b>anemia crítica</b>&mdash; en el que la DO<sub>2</sub> ya no cubre el consumo y aparece metabolismo
anaerobio. Ese umbral var&iacute;a enormemente entre pacientes y situaciones: lo adelantan la <b>hipovolemia</b>, la enfermedad
<b>coronaria</b>, el aumento del consumo (fiebre, dolor, esfuerzo) y la limitaci&oacute;n del gasto cardíaco. El coraz&oacute;n es
especialmente vulnerable porque ya extrae ox&iacute;geno casi al m&aacute;ximo en condiciones basales [1].</p>

<h2 class="sec"><span class="num">4.</span>C&oacute;mo optimizar la tolerancia</h2>
<div class="tbl-title">Tabla 1 &middot; Palancas para mejorar la tolerancia a la anemia</div>
<table class="avoid-break">
  <thead><tr><th style="width:34%">Palanca</th><th>Acci&oacute;n</th></tr></thead>
  <tbody>
    <tr><td><b>Mantener normovolemia</b></td><td>Reposici&oacute;n adecuada: la hipovolemia anula la compensaci&oacute;n del gasto cardíaco.</td></tr>
    <tr><td><b>Optimizar la oxigenaci&oacute;n</b></td><td>Asegurar SaO<sub>2</sub> alta; ox&iacute;geno suplementario seg&uacute;n necesidad.</td></tr>
    <tr><td><b>Reducir el consumo de O<sub>2</sub></b></td><td>Analgesia, normotermia, sedaci&oacute;n cuando proceda, tratar fiebre y agitaci&oacute;n.</td></tr>
    <tr><td><b>Sostener el gasto cardíaco</b></td><td>Soporte hemodin&aacute;mico adecuado en el paciente con reserva limitada.</td></tr>
    <tr><td><b>Vigilancia dirigida</b></td><td>Signos de mala tolerancia (isquemia, lactato, SvO<sub>2</sub> baja) que indican transfundir.</td></tr>
  </tbody>
  <caption>Estas palancas amplían el margen de anemia tolerable y son el sustrato fisiol&oacute;gico de los umbrales restrictivos [1].</caption>
</table>

<h2 class="sec"><span class="num">5.</span>L&iacute;mites por paciente</h2>
<p>La tolerancia no es igual para todos. El paciente <b>joven, normovol&eacute;mico y sin cardiopat&iacute;a</b> tolera Hb muy bajas; el
paciente con <b>enfermedad coronaria</b> o reserva cardíaca limitada tiene un margen mucho menor &mdash;de ah&iacute; los umbrales m&aacute;s
altos en cirug&iacute;a cardíaca y, sobre todo, en el <b>s&iacute;ndrome coronario agudo</b> (PBM-12)&mdash;. La revisi&oacute;n Cochrane subraya que
un <b>umbral &uacute;nico de Hb</b> es una simplificaci&oacute;n: el futuro pasa por integrar par&aacute;metros fisiol&oacute;gicos individuales [1].</p>

<div class="box rev avoid-break"><span class="box-h">Honestidad sobre el umbral &uacute;nico</span>
  <p>La fisiolog&iacute;a explica por qu&eacute; los umbrales restrictivos funcionan en general y por qu&eacute; fallan en algunos contextos. El
  umbral de Hb es una <b>aproximaci&oacute;n &uacute;til</b>, no una verdad fisiol&oacute;gica universal: la tolerancia real depende del paciente,
  y los disparadores fisiol&oacute;gicos podr&iacute;an afinar la decisi&oacute;n en el futuro [1].</p>
</div>

<h2 class="sec"><span class="num">6.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> el organismo tolera la anemia moderada gracias a mecanismos compensatorios que
preservan la entrega de ox&iacute;geno, y optimizar esa tolerancia (normovolemia, oxigenaci&oacute;n, menor consumo) es la base del
pilar 3; pero la tolerancia tiene l&iacute;mites individuales, marcados sobre todo por la reserva cardíaca y coronaria, que
explican las excepciones a los umbrales restrictivos.</p>
<p>Conecta con <b>PBM-12</b> (umbrales y su excepci&oacute;n en SCA), <b>PBM-01</b> (tercer pilar) y con el conjunto del pilar 1
(optimizar la Hb previa para ampliar el margen).</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>La anemia se tolera porque el cuerpo compensa la entrega de ox&iacute;geno &mdash;manten normovolemia, oxigena y reduce consumo
  para ampliar el margen; pero recuerda que el coraz&oacute;n isqu&eacute;mico marca el l&iacute;mite&mdash;.</p>
</div>

<h2 class="sec"><span class="num">7.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>REV</b> anclado en la revisi&oacute;n Cochrane 2025 [1] y respaldado por ESAIC [2] y TRICC [3], verificados contra
PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Los conceptos fisiol&oacute;gicos (DO<sub>2</sub>, extracci&oacute;n, 2,3-DPG, anemia
crítica) son consenso fisiol&oacute;gico establecido; la limitaci&oacute;n del <b>umbral &uacute;nico</b> y la variabilidad individual se recogen
expl&iacute;citamente en la fuente [1].</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">8.</span>Referencias</h2>
<ol class="refs">
  <li>Carson JL, Stanworth SJ, Dennis JA, Fergusson DA, Pagano MB, Roubinian NH, et al. Transfusion thresholds and other strategies for guiding red blood cell transfusion. <i>Cochrane Database Syst Rev</i> 2025;10(10):CD002042. <span class="doi">doi:10.1002/14651858.CD002042.pub6</span> &middot; PMID 41114449.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
  <li>H&eacute;bert PC, Wells G, Blajchman MA, Marshall J, Martin C, Pagliarello G, et al. A multicenter, randomized, controlled clinical trial of transfusion requirements in critical care (TRICC). <i>N Engl J Med</i> 1999;340(6):409&ndash;417. <span class="doi">doi:10.1056/NEJM199902113400601</span> &middot; PMID 9971864.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-14-tolerancia-anemia.html")
    print("HTML:", h); print("PDF :", p)
