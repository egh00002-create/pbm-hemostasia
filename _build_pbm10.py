# -*- coding: utf-8 -*-
"""PBM-10 - Recuperacion celular intraoperatoria y tecnicas de ahorro. Ancla META."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-10 Recuperacion celular y tecnicas de ahorro. Ancla META.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-10 - Modulo 3 (Pilar 2) - ancla META - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-10</span>
    <span class="badge b-meta">META &middot; revisi&oacute;n sistem&aacute;tica / metaan&aacute;lisis</span>
    <span class="module-tag">M&oacute;dulo 3 &middot; Pilar 2: minimizar la p&eacute;rdida sangu&iacute;nea</span>
  </div>
  <div class="kicker">Recuperador celular &middot; Hemodiluci&oacute;n &middot; T&eacute;cnicas de ahorro</div>
  <h1 class="title">Recuperaci&oacute;n celular intraoperatoria y t&eacute;cnicas de ahorro</h1>
  <div class="subtitle">Reutilizar la propia sangre del paciente &mdash; eficacia real, pero dependiente del contexto quir&uacute;rgico</div>
  <div class="meta-row">
    <span class="meta-chip">C&oacute;mo funciona el recuperador</span>
    <span class="meta-chip">Indicaciones y contraindicaciones</span>
    <span class="meta-chip">Hemodiluci&oacute;n normovol&eacute;mica</span>
    <span class="meta-chip">Qu&eacute; dice el metaan&aacute;lisis</span>
    <span class="meta-chip">D&oacute;nde s&iacute; y d&oacute;nde no</span>
  </div>
  <div class="refbar">
    <b>Ancla de evidencia (referencia vertebral):</b> Lloyd TD, Geneen LJ, Bernhardt K, et&nbsp;al.
    <i>Cell salvage for minimising perioperative allogeneic blood transfusion in adults undergoing elective surgery.</i>
    Cochrane Database Syst Rev 2023;9(9):CD001888. <span class="mono">doi:10.1002/14651858.CD001888.pub5 &middot; PMID&nbsp;37681564</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> el <b>recuperador celular</b> reaprovecha la sangre del campo quir&uacute;rgico y puede reducir la
    transfusi&oacute;n al&oacute;gena, pero <b>el beneficio depende del tipo de cirug&iacute;a</b>: claro en algunos contextos (raquis, ciertos
    cardiovasculares), incierto en otros. Es una herramienta del pilar 2 que debe indicarse seg&uacute;n la p&eacute;rdida esperada.
  </div>
  <div class="lead">
    <p>Las t&eacute;cnicas de ahorro de sangre permiten <b>reutilizar o preservar</b> la sangre del propio paciente. La m&aacute;s usada es
    la <b>recuperaci&oacute;n celular intraoperatoria</b> (cell salvage): se aspira la sangre del campo, se lava y se reinfunde,
    evitando exposici&oacute;n al&oacute;gena.</p>
    <p>Este documento, con ancla <b>META</b>, presenta el recuperador y la hemodiluci&oacute;n con honestidad: d&oacute;nde la evidencia
    respalda su uso y d&oacute;nde el beneficio es incierto [1].</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>C&oacute;mo funciona el recuperador celular</li>
  <li>Indicaciones y contraindicaciones</li>
  <li>Hemodiluci&oacute;n normovol&eacute;mica aguda</li>
  <li>Qu&eacute; dice el metaan&aacute;lisis (por tipo de cirug&iacute;a)</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>C&oacute;mo funciona el recuperador celular</h2>
<p>El recuperador aspira la sangre del campo quir&uacute;rgico, la anticoagula, la <b>lava y concentra</b> los hematíes, y los
reinfunde al paciente. As&iacute; se recupera masa eritrocitaria propia y se evita la transfusi&oacute;n al&oacute;gena con sus riesgos. El
producto reinfundido son <b>hematíes lavados</b> (sin plasma ni plaquetas), por lo que no corrige coagulopat&iacute;a [1].</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>Reinfunde <b>hematíes propios lavados</b>: evita exposici&oacute;n al&oacute;gena, pero no aporta factores ni plaquetas [1].</li>
  <li>Su rendimiento es mayor cuanto <b>mayor es la p&eacute;rdida esperada</b>; en cirug&iacute;a de bajo sangrado aporta poco.</li>
  <li>El beneficio en reducci&oacute;n de transfusi&oacute;n <b>var&iacute;a por tipo de cirug&iacute;a</b> [1].</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Indicaciones y contraindicaciones</h2>
<p>Se indica en cirug&iacute;a con <b>p&eacute;rdida sangu&iacute;nea esperada elevada</b> (cardiovascular, raquis, algunos trasplantes,
obstetricia seleccionada, ortopedia mayor). Las precauciones cl&aacute;sicas &mdash;campo contaminado o cirug&iacute;a oncol&oacute;gica&mdash; se han
matizado: con t&eacute;cnicas como la <b>filtraci&oacute;n por deplecci&oacute;n leucocitaria o la irradiaci&oacute;n</b> su uso se ha extendido a
escenarios antes vetados, seg&uacute;n protocolo. La decisi&oacute;n se basa en la p&eacute;rdida esperada y el contexto [1].</p>

<h2 class="sec"><span class="num">3.</span>Hemodiluci&oacute;n normovol&eacute;mica aguda</h2>
<p>La <b>hemodiluci&oacute;n normovol&eacute;mica aguda</b> consiste en extraer sangre del paciente al inicio (reponiendo volumen con
cristaloides/coloides) y reinfundirla tras la fase de mayor sangrado: la sangre perdida durante la cirug&iacute;a est&aacute; m&aacute;s
diluida y la sangre extra&iacute;da, rica en c&eacute;lulas y factores, se devuelve despu&eacute;s. Es una t&eacute;cnica de ahorro de uso m&aacute;s
selectivo, dependiente de la log&iacute;stica y la situaci&oacute;n del paciente.</p>

<h2 class="sec"><span class="num">4.</span>Qu&eacute; dice el metaan&aacute;lisis (por tipo de cirug&iacute;a)</h2>
<p>La revisi&oacute;n Cochrane (106 ensayos, 14.528 participantes) concluye que el recuperador celular <b>puede reducir</b> la
necesidad de transfusi&oacute;n al&oacute;gena en algunos tipos de cirug&iacute;a, con certeza variable: el beneficio es <b>m&aacute;s claro en cirug&iacute;a
de raquis</b> (RR 0,44; certeza moderada) y en ciertos contextos cardiovasculares sin bypass (RR 0,82), mientras que en
otros (cadera, rodilla, mixta) la certeza es baja o muy baja y el efecto, incierto; en obstetricia no hubo diferencia en
el volumen medio transfundido [1]. No se observaron diferencias relevantes en eventos adversos [1].</p>

<div class="box rev avoid-break"><span class="box-h">Honestidad sobre la evidencia</span>
  <p>El recuperador <b>no es universalmente beneficioso</b>: rinde donde el sangrado es alto (raquis, cardiovascular
  seleccionado) y aporta poco donde el sangrado es bajo. Indicarlo seg&uacute;n la <b>p&eacute;rdida esperada</b> (PBM-11), no por rutina,
  es lo coherente con la evidencia [1].</p>
</div>

<h2 class="sec"><span class="num">5.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> el recuperador celular reaprovecha la sangre propia y reduce la transfusi&oacute;n al&oacute;gena
en cirug&iacute;as de sangrado alto (raquis, cardiovascular seleccionado), con beneficio incierto en otras; debe indicarse seg&uacute;n
la p&eacute;rdida esperada, no por rutina. Reinfunde hematíes lavados, no corrige coagulopat&iacute;a.</p>
<p>Conecta con <b>PBM-11</b> (planificaci&oacute;n por MABL), <b>PBM-07</b> (estrategia multimodal) y <b>PBM-12</b> (umbrales que,
junto al ahorro, reducen la exposici&oacute;n).</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Usa el recuperador celular donde el sangrado esperado es alto (raquis, cardiovascular seleccionado) &mdash;reduce la
  transfusi&oacute;n al&oacute;gena ah&iacute;; en cirug&iacute;a de bajo sangrado aporta poco&mdash;.</p>
</div>

<h2 class="sec"><span class="num">6.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>META</b> anclado en la revisi&oacute;n Cochrane de Lloyd et&nbsp;al. [1], respaldado por ESAIC [2] y el consenso de
Frankfurt [3], verificados contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Las cifras por tipo de cirug&iacute;a (raquis
RR 0,44; cardiovascular sin bypass RR 0,82) y la <b>certeza variable</b> proceden directamente de la fuente [1].</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">7.</span>Referencias</h2>
<ol class="refs">
  <li>Lloyd TD, Geneen LJ, Bernhardt K, McClune W, Fernquest SJ, Brown T, et al. Cell salvage for minimising perioperative allogeneic blood transfusion in adults undergoing elective surgery. <i>Cochrane Database Syst Rev</i> 2023;9(9):CD001888. <span class="doi">doi:10.1002/14651858.CD001888.pub5</span> &middot; PMID 37681564.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
  <li>Mueller MM, Van Remoortel H, Meybohm P, Aranko K, Aubron C, Burger R, et al. Patient Blood Management: Recommendations From the 2018 Frankfurt Consensus Conference. <i>JAMA</i> 2019;321(10):983&ndash;997. <span class="doi">doi:10.1001/jama.2019.0554</span> &middot; PMID 30860564.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-10-recuperacion-celular.html")
    print("HTML:", h); print("PDF :", p)
