# -*- coding: utf-8 -*-
"""PBM-11 - Perdida sanguinea admisible (MABL): calculo y planificacion. Ancla REV."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-11 Perdida sanguinea admisible (MABL). Ancla REV.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-11 - Modulo 3 (Pilar 2) - ancla REV - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Formulas procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-11</span>
    <span class="badge b-rev">REV &middot; revisi&oacute;n / s&iacute;ntesis</span>
    <span class="module-tag">M&oacute;dulo 3 &middot; Pilar 2: minimizar la p&eacute;rdida sangu&iacute;nea</span>
  </div>
  <div class="kicker">P&eacute;rdida sangu&iacute;nea admisible &middot; Volumen de Nadler &middot; F&oacute;rmula de Gross</div>
  <h1 class="title">P&eacute;rdida sangu&iacute;nea admisible (MABL): c&aacute;lculo y planificaci&oacute;n</h1>
  <div class="subtitle">Anticipar cu&aacute;nto puede sangrar este paciente antes de necesitar transfusi&oacute;n &mdash; una herramienta de planificaci&oacute;n</div>
  <div class="meta-row">
    <span class="meta-chip">Volumen sangu&iacute;neo (Nadler)</span>
    <span class="meta-chip">MABL (Gross)</span>
    <span class="meta-chip">Ejemplo de c&aacute;lculo</span>
    <span class="meta-chip">Usos y limitaciones</span>
    <span class="meta-chip">Del n&uacute;mero al plan</span>
  </div>
  <div class="refbar">
    <b>Anclas de evidencia (referencias vertebrales):</b> Nadler SB, Hidalgo JH, Bloch T.
    <i>Prediction of blood volume in normal human adults.</i> Surgery 1962;51(2):224&ndash;232 (PMID&nbsp;21936146). &middot;
    Gross JB. <i>Estimating allowable blood loss: corrected for dilution.</i> Anesthesiology 1983;58(3):277&ndash;280
    <span class="mono">doi:10.1097/00000542-198303000-00016 &middot; PMID&nbsp;6829965</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> la p&eacute;rdida sangu&iacute;nea admisible (MABL) estima <b>cu&aacute;nto puede perder un paciente</b> hasta alcanzar
    un hematocrito/Hb diana, a partir de su <b>volumen sangu&iacute;neo</b> (Nadler) y de la f&oacute;rmula de <b>Gross</b>. Es una
    <b>herramienta de planificaci&oacute;n</b>, no un disparador de transfusi&oacute;n: orienta, no sustituye la valoraci&oacute;n cl&iacute;nica.
  </div>
  <div class="lead">
    <p>Planificar el pilar 2 exige una estimaci&oacute;n cuantitativa: &iquest;cu&aacute;nto margen de sangrado tiene este paciente antes de que
    su hemoglobina baje del umbral deseado? La <b>p&eacute;rdida sangu&iacute;nea m&aacute;xima admisible (MABL)</b> responde a esa pregunta y
    ayuda a anticipar disponibilidad de hemoderivados y t&eacute;cnicas de ahorro.</p>
    <p>Este documento, con anclas <b>cl&aacute;sicas</b> (Nadler y Gross), presenta las f&oacute;rmulas, un ejemplo de c&aacute;lculo y, sobre
    todo, sus <b>limitaciones</b>: la MABL es una gu&iacute;a de planificaci&oacute;n, no una cifra absoluta.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>El volumen sangu&iacute;neo estimado (Nadler)</li>
  <li>La p&eacute;rdida admisible (Gross)</li>
  <li>Ejemplo de c&aacute;lculo paso a paso</li>
  <li>Usos, limitaciones y errores frecuentes</li>
  <li>Del n&uacute;mero al plan</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>El volumen sangu&iacute;neo estimado (Nadler)</h2>
<p>El primer paso es estimar el <b>volumen sangu&iacute;neo (VSE)</b> del paciente. Las ecuaciones de <b>Nadler</b> (1962) lo
calculan a partir de talla y peso [1]:</p>
<div class="box note avoid-break"><span class="box-h">Ecuaciones de Nadler (VSE en litros; talla en metros, peso en kg)</span>
  <p class="mono">Var&oacute;n: VSE = 0,3669 &times; talla&sup3; + 0,03219 &times; peso + 0,6041</p>
  <p class="mono">Mujer: VSE = 0,3561 &times; talla&sup3; + 0,03308 &times; peso + 0,1833</p>
  <p>Regla aproximada de cabecera: &asymp; <b>70&nbsp;ml/kg</b> (var&oacute;n) y <b>65&nbsp;ml/kg</b> (mujer) en el adulto.</p>
</div>

<h2 class="sec"><span class="num">2.</span>La p&eacute;rdida admisible (Gross)</h2>
<p>Con el VSE y los hematocritos inicial y diana, la f&oacute;rmula de <b>Gross</b> (1983), corregida por diluci&oacute;n, estima la
p&eacute;rdida admisible [2]:</p>
<div class="box note avoid-break"><span class="box-h">F&oacute;rmula de Gross</span>
  <p class="mono">MABL = VSE &times; (Hct<sub>inicial</sub> &minus; Hct<sub>diana</sub>) / Hct<sub>medio</sub></p>
  <p>donde Hct<sub>medio</sub> es la media de Hct<sub>inicial</sub> y Hct<sub>diana</sub>. Puede usarse Hb en lugar de Hct con la misma estructura.</p>
</div>

<h2 class="sec"><span class="num">3.</span>Ejemplo de c&aacute;lculo paso a paso</h2>
<p>Var&oacute;n de 80&nbsp;kg y 1,75&nbsp;m, Hct inicial 42&nbsp;%, Hct diana 28&nbsp;%:</p>
<div class="flow avoid-break">
  <div class="step"><b>1. VSE (Nadler):</b> 0,3669 &times; 1,75&sup3; + 0,03219 &times; 80 + 0,6041 &asymp; <b>5,15&nbsp;L</b> (&asymp; 5150&nbsp;ml).</div>
  <div class="step"><b>2. Hct medio:</b> (42 + 28) / 2 = <b>35&nbsp;%</b>.</div>
  <div class="step a"><b>3. MABL (Gross):</b> 5150 &times; (42 &minus; 28) / 35 &asymp; <b>2060&nbsp;ml</b>.</div>
</div>
<p>Es decir, este paciente podr&iacute;a perder del orden de <b>2&nbsp;litros</b> antes de descender a un Hct del 28&nbsp;% (&asymp; Hb
9&nbsp;g/dl), asumiendo normovolemia mantenida con reposici&oacute;n. El umbral diana se elige seg&uacute;n el contexto (PBM-12).</p>

<h2 class="sec"><span class="num">4.</span>Usos, limitaciones y errores frecuentes</h2>
<p>La MABL sirve para <b>planificar</b>: decidir reservas, activar recuperador celular (PBM-10), anticipar la necesidad de
hemoderivados. Sus <b>limitaciones</b> son importantes: asume normovolemia y reposici&oacute;n ideal, no contempla la coagulopat&iacute;a
por diluci&oacute;n ni la p&eacute;rdida continuada, y el Hct medido intraoperatorio puede retrasarse respecto a la p&eacute;rdida real.</p>

<div class="box alert avoid-break"><span class="box-h">Error frecuente</span>
  <p>Tratar la MABL como un <b>permiso</b> de sangrado o como un disparador autom&aacute;tico de transfusi&oacute;n. Es una <b>estimaci&oacute;n
  de planificaci&oacute;n</b>: la decisi&oacute;n de transfundir integra el umbral de Hb, la situaci&oacute;n hemodin&aacute;mica y el sangrado activo
  (PBM-12), no solo el n&uacute;mero calculado.</p>
</div>

<h2 class="sec"><span class="num">5.</span>Del n&uacute;mero al plan</h2>
<p>La MABL traduce el riesgo en una cifra accionable: si la p&eacute;rdida esperada de la cirug&iacute;a se acerca o supera la MABL,
conviene <b>optimizar la Hb previa</b> (pilar 1: PBM-04/05/06), <b>minimizar la p&eacute;rdida</b> (TXA, recuperador, viscoel&aacute;stica)
y <b>planificar la disponibilidad</b> de hemoderivados. As&iacute;, la MABL conecta los tres pilares en una decisi&oacute;n anticipada.</p>

<h2 class="sec"><span class="num">6.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> la MABL, calculada con el volumen de Nadler y la f&oacute;rmula de Gross, estima el margen
de sangrado hasta el Hct diana y es una <b>herramienta de planificaci&oacute;n</b> que ayuda a anticipar; no es un disparador de
transfusi&oacute;n ni una cifra absoluta, pues asume condiciones ideales que la cl&iacute;nica no siempre cumple.</p>
<p>Conecta con <b>PBM-12</b> (elecci&oacute;n del umbral diana), <b>PBM-10</b> (recuperador), <b>PBM-08</b> (TXA) y el pilar 1
(<b>PBM-04/05/06</b>). Se condensa en la tarjeta <b>P-QR-04</b>.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Estima el volumen con Nadler y la p&eacute;rdida admisible con Gross para <b>planificar</b> &mdash;no para decidir la transfusi&oacute;n,
  que depende del umbral y del cuadro cl&iacute;nico&mdash;.</p>
</div>

<h2 class="sec"><span class="num">7.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>REV</b> basado en dos f&oacute;rmulas cl&aacute;sicas verificadas contra PubMed: el volumen sangu&iacute;neo de Nadler [1] y la
p&eacute;rdida admisible corregida por diluci&oacute;n de Gross [2], complementadas por la gu&iacute;a ESAIC [3]. Las ecuaciones se reproducen
tal como las publicaron sus autores; el ejemplo es ilustrativo. Se subraya su car&aacute;cter de <b>estimaci&oacute;n de planificaci&oacute;n</b>
y sus limitaciones.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">8.</span>Referencias</h2>
<ol class="refs">
  <li>Nadler SB, Hidalgo JH, Bloch T. Prediction of blood volume in normal human adults. <i>Surgery</i> 1962;51(2):224&ndash;232. &middot; PMID 21936146.</li>
  <li>Gross JB. Estimating allowable blood loss: corrected for dilution. <i>Anesthesiology</i> 1983;58(3):277&ndash;280. <span class="doi">doi:10.1097/00000542-198303000-00016</span> &middot; PMID 6829965.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-11-perdida-sanguinea-admisible.html")
    print("HTML:", h); print("PDF :", p)
