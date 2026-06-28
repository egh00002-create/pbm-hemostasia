# -*- coding: utf-8 -*-
"""PBM-15 - Cribado del riesgo hemorragico preoperatorio (HEMSTOP). Ancla REV."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-15 Cribado del riesgo hemorragico (HEMSTOP). Ancla REV.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-15 - Modulo 5 (eje hemostasia) - ancla REV - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-15</span>
    <span class="badge b-rev">REV &middot; revisi&oacute;n / s&iacute;ntesis</span>
    <span class="module-tag">M&oacute;dulo 5 &middot; Hemostasia clínica y riesgo hemorr&aacute;gico</span>
  </div>
  <div class="kicker">Cribado del riesgo hemorr&aacute;gico &middot; HEMSTOP &middot; Anamnesis estructurada</div>
  <h1 class="title">Cribado del riesgo hemorr&aacute;gico preoperatorio (HEMSTOP)</h1>
  <div class="subtitle">La mejor prueba de coagulaci&oacute;n preoperatoria es una buena historia clínica &mdash; no el TP/TTPa de rutina</div>
  <div class="meta-row">
    <span class="meta-chip">Por qu&eacute; no cribar con TP/TTPa</span>
    <span class="meta-chip">El cuestionario HEMSTOP</span>
    <span class="meta-chip">Interpretaci&oacute;n del score</span>
    <span class="meta-chip">A qui&eacute;n estudiar m&aacute;s</span>
    <span class="meta-chip">L&iacute;mites</span>
  </div>
  <div class="refbar">
    <b>Ancla de evidencia (referencia vertebral):</b> Bonhomme F, Boehlen F, Clergue F, de Moerloose P.
    <i>Preoperative hemostatic assessment: a new and simple bleeding questionnaire (HEMSTOP).</i>
    Can J Anaesth 2016;63(9):1007&ndash;1015. <span class="mono">doi:10.1007/s12630-016-0688-9 &middot; PMID&nbsp;27369959</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> el cribado de coagulaci&oacute;n con <b>TP/TTPa de rutina</b> en pacientes asintom&aacute;ticos es <b>ineficiente</b>
    y genera falsos positivos. La estrategia correcta es una <b>anamnesis estructurada</b> del riesgo hemorr&aacute;gico (como el
    cuestionario HEMSTOP) y reservar las pruebas para quien tenga historia o cl&iacute;nica sugestiva.
  </div>
  <div class="lead">
    <p>Pedir TP y TTPa &laquo;por protocolo&raquo; a todo paciente antes de cirug&iacute;a parece prudente, pero no lo es: detecta mal los
    trastornos hemorr&aacute;gicos relevantes (muchos cursan con coagulaci&oacute;n b&aacute;sica normal) y produce hallazgos an&oacute;malos sin
    significado que retrasan y encarecen [1].</p>
    <p>Este documento abre el eje de hemostasia clínica con la herramienta de cribado correcta: la <b>anamnesis
    estructurada</b>. Presenta el cuestionario <b>HEMSTOP</b>, su interpretaci&oacute;n y sus l&iacute;mites, como puerta de entrada al
    manejo del paciente con riesgo hemorr&aacute;gico (PBM-16 a 18).</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>Por qu&eacute; el TP/TTPa de rutina no sirve para cribar</li>
  <li>El cuestionario HEMSTOP</li>
  <li>Interpretaci&oacute;n y rendimiento</li>
  <li>A qui&eacute;n estudiar m&aacute;s y c&oacute;mo actuar</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>Por qu&eacute; el TP/TTPa de rutina no sirve para cribar</h2>
<p>Las pruebas de coagulaci&oacute;n convencionales se dise&ntilde;aron para <b>diagnosticar</b> coagulopat&iacute;as conocidas, no para
<b>cribar</b> poblaciones asintom&aacute;ticas. En el paciente sin historia hemorr&aacute;gica tienen <b>bajo valor predictivo</b>: muchos
trastornos relevantes (enfermedad de von Willebrand, disfunci&oacute;n plaquetaria) cursan con TP/TTPa normales, mientras que
alteraciones an&aacute;lisis sin traducci&oacute;n cl&iacute;nica generan estudios y demoras innecesarias [1]. Por eso las guías recomiendan
<b>no cribar de forma indiscriminada</b> con coagulaci&oacute;n b&aacute;sica.</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>El cribado correcto es la <b>anamnesis estructurada</b>, no el TP/TTPa de rutina [1].</li>
  <li>HEMSTOP es un cuestionario de <b>7 &iacute;tems</b> con alta especificidad para detectar a quien precisa estudio [1].</li>
  <li>Un cribado cl&iacute;nico positivo &mdash;no un n&uacute;mero an&oacute;malo aislado&mdash; es lo que indica profundizar.</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>El cuestionario HEMSTOP</h2>
<p><b>HEMSTOP</b> es un cuestionario dicot&oacute;mico de siete preguntas cuyo acr&oacute;nimo resume los dominios explorados [1]:</p>
<div class="box note avoid-break"><span class="box-h">Dominios HEMSTOP</span><ul>
  <li><b>H</b>ematoma &mdash; hematomas frecuentes/desproporcionados.</li>
  <li><b>E</b>morragia (hemorragia) &mdash; sangrado que precis&oacute; atenci&oacute;n m&eacute;dica.</li>
  <li><b>M</b>enorragia &mdash; reglas abundantes (en mujeres).</li>
  <li><b>S</b>urgery (cirug&iacute;a) &mdash; sangrado anormal en cirug&iacute;as previas.</li>
  <li><b>T</b>ooth (extracci&oacute;n dental) &mdash; sangrado prolongado tras extracciones.</li>
  <li><b>O</b>bstetrics (obstetricia) &mdash; hemorragia en el parto.</li>
  <li><b>P</b>arents (familiares) &mdash; antecedentes familiares de trastorno hemorr&aacute;gico.</li>
</ul></div>

<h2 class="sec"><span class="num">3.</span>Interpretaci&oacute;n y rendimiento</h2>
<p>En el estudio de validaci&oacute;n, una puntuaci&oacute;n <b>&ge; 2</b> identific&oacute; a los pacientes que requer&iacute;an precauciones
hemost&aacute;ticas perioperatorias con una <b>especificidad del 98,6&nbsp;%</b> y una <b>sensibilidad del 89,5&nbsp;%</b>, muy superior al
rendimiento de las pruebas de coagulaci&oacute;n est&aacute;ndar (sensibilidad &asymp; 26&nbsp;%) [1]. Es decir: el cuestionario discrimina
mucho mejor que el TP/TTPa qui&eacute;n tiene un riesgo hemorr&aacute;gico real.</p>

<div class="box pearl avoid-break"><span class="box-h">Perla</span>
  <p>Un HEMSTOP <b>&ge; 2</b> debe llevar a estudio dirigido de hemostasia antes de cirug&iacute;a de riesgo; un HEMSTOP de 0 en un
  paciente sin f&aacute;rmacos antitrombóticos hace muy improbable un trastorno hemorr&aacute;gico oculto y evita pruebas in&uacute;tiles [1].</p>
</div>

<h2 class="sec"><span class="num">4.</span>A qui&eacute;n estudiar m&aacute;s y c&oacute;mo actuar</h2>
<p>Ante un cribado positivo (o historia clara), conviene <b>estudio dirigido</b>: hemograma con plaquetas, coagulaci&oacute;n,
y seg&uacute;n sospecha, estudio de von Willebrand, funci&oacute;n plaquetaria o factores espec&iacute;ficos, idealmente con apoyo de
hematolog&iacute;a [1]. Tambi&eacute;n debe revisarse de forma sistem&aacute;tica la <b>medicaci&oacute;n antitrombótica</b> (antiagregantes y
anticoagulantes), cuyo manejo perioperatorio se desarrolla en PBM-16. La gu&iacute;a ESAIC respalda este enfoque escalonado
basado en la historia [2].</p>

<h2 class="sec"><span class="num">5.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> el cribado del riesgo hemorr&aacute;gico debe basarse en una <b>anamnesis estructurada</b>
(p.&nbsp;ej. HEMSTOP), no en el TP/TTPa de rutina, que tiene bajo rendimiento y genera falsos positivos; HEMSTOP &ge; 2 detecta
con alta especificidad a quien precisa estudio. La herramienta orienta, y la decisi&oacute;n final integra la historia y la
medicaci&oacute;n.</p>
<p>Conecta con <b>PBM-16</b> (manejo de antitrombóticos), <b>PBM-17</b> (coagulopat&iacute;as) y <b>PBM-18</b> (f&aacute;rmacos
hemost&aacute;ticos); es la puerta de entrada del eje de hemostasia. Resumen operativo en <b>P-QR-05</b>.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Criba el riesgo hemorr&aacute;gico con preguntas (HEMSTOP), no con TP/TTPa de rutina &mdash;estudia a fondo solo a quien tiene
  historia o un score &ge; 2&mdash;.</p>
</div>

<h2 class="sec"><span class="num">6.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>REV</b> anclado en el estudio de validaci&oacute;n de HEMSTOP [1] y respaldado por la gu&iacute;a ESAIC [2] y el consenso de
Frankfurt [3], verificados contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Las cifras de rendimiento
(especificidad 98,6&nbsp;%, sensibilidad 89,5&nbsp;% para score &ge; 2; sensibilidad &asymp; 26&nbsp;% de las pruebas est&aacute;ndar) proceden
directamente de la fuente [1], que se presenta como herramienta de cribado a validar en m&aacute;s contextos.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">7.</span>Referencias</h2>
<ol class="refs">
  <li>Bonhomme F, Boehlen F, Clergue F, de Moerloose P. Preoperative hemostatic assessment: a new and simple bleeding questionnaire (HEMSTOP). <i>Can J Anaesth</i> 2016;63(9):1007&ndash;1015. <span class="doi">doi:10.1007/s12630-016-0688-9</span> &middot; PMID 27369959.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
  <li>Mueller MM, Van Remoortel H, Meybohm P, Aranko K, Aubron C, Burger R, et al. Patient Blood Management: Recommendations From the 2018 Frankfurt Consensus Conference. <i>JAMA</i> 2019;321(10):983&ndash;997. <span class="doi">doi:10.1001/jama.2019.0554</span> &middot; PMID 30860564.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-15-cribado-hemstop.html")
    print("HTML:", h); print("PDF :", p)
