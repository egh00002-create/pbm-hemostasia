# -*- coding: utf-8 -*-
"""PBM-18 - Farmacos hemostaticos (CCP, fibrinogeno, rFVIIa, desmopresina). Ancla REV."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-18 Farmacos hemostaticos. Ancla REV.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-18 - Modulo 5 (eje hemostasia) - ancla REV - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-18</span>
    <span class="badge b-rev">REV &middot; revisi&oacute;n / s&iacute;ntesis</span>
    <span class="module-tag">M&oacute;dulo 5 &middot; Hemostasia clínica y riesgo hemorr&aacute;gico</span>
  </div>
  <div class="kicker">F&aacute;rmacos hemost&aacute;ticos &middot; CCP &middot; Fibrin&oacute;geno &middot; rFVIIa &middot; Desmopresina</div>
  <h1 class="title">F&aacute;rmacos hemost&aacute;ticos: CCP, fibrin&oacute;geno, rFVIIa y desmopresina</h1>
  <div class="subtitle">Herramientas dirigidas para corregir d&eacute;ficits concretos &mdash; potentes y, algunas, con riesgo trombótico</div>
  <div class="meta-row">
    <span class="meta-chip">Concentrado de complejo protrombínico</span>
    <span class="meta-chip">Concentrado de fibrin&oacute;geno</span>
    <span class="meta-chip">Factor VII activado</span>
    <span class="meta-chip">Desmopresina</span>
    <span class="meta-chip">Uso dirigido</span>
  </div>
  <div class="refbar">
    <b>Ancla de evidencia (referencia vertebral):</b> Kietaibl S, Ahmed A, Afshari A, et&nbsp;al.
    <i>Management of severe peri-operative bleeding: Guidelines from the ESAIC: Second update 2022.</i>
    Eur J Anaesthesiol 2023;40(4):226&ndash;304. <span class="mono">doi:10.1097/EJA.0000000000001803 &middot; PMID&nbsp;36855941</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> los f&aacute;rmacos hemost&aacute;ticos corrigen <b>d&eacute;ficits concretos</b>: el <b>CCP</b> revierte los AVK y aporta
    factores; el <b>fibrin&oacute;geno</b> repone el primer factor que cae; la <b>desmopresina</b> ayuda en la von Willebrand
    respondedora y la disfunci&oacute;n plaquetaria; el <b>rFVIIa</b> es un recurso de rescate <b>off-label</b> con riesgo trombótico.
    Se usan <b>dirigidos</b>, no a ciegas.
  </div>
  <div class="lead">
    <p>Cuando la hemostasia b&aacute;sica (cirug&iacute;a, normotermia, calcio, antifibrinol&iacute;ticos) no basta, disponemos de f&aacute;rmacos que
    corrigen d&eacute;ficits espec&iacute;ficos de la coagulaci&oacute;n. Su valor depende de usarlos <b>dirigidos al d&eacute;ficit</b> &mdash;idealmente
    guiados por viscoel&aacute;stica (PBM-09)&mdash;, no como gesto gen&eacute;rico.</p>
    <p>Este documento cierra la serie repasando los principales agentes hemost&aacute;ticos, sus indicaciones y sus riesgos, con el
    tono honesto de la serie: son potentes, pero algunos (rFVIIa) tienen un balance beneficio-riesgo estrecho.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>Concentrado de complejo protrombínico (CCP)</li>
  <li>Concentrado de fibrin&oacute;geno</li>
  <li>Factor VII activado recombinante (rFVIIa)</li>
  <li>Desmopresina (DDAVP)</li>
  <li>Tabla integradora de uso dirigido</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>Concentrado de complejo protrombínico (CCP)</h2>
<p>El <b>CCP</b> aporta factores dependientes de vitamina K (II, VII, IX, X). Su indicaci&oacute;n m&aacute;s clara es la <b>reversi&oacute;n
urgente de los antagonistas de la vitamina K</b> (con vitamina K) en hemorragia grave o cirug&iacute;a inaplazable, donde es m&aacute;s
r&aacute;pido y eficaz que el plasma [1]. Tambi&eacute;n se emplea, guiado por viscoel&aacute;stica, en la coagulopat&iacute;a por d&eacute;ficit de
factores en la hemorragia perioperatoria. Conlleva cierto <b>riesgo trombótico</b>, por lo que se dosifica de forma
dirigida [1].</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li><b>CCP</b>: reversi&oacute;n urgente de AVK (con vitamina K); m&aacute;s r&aacute;pido que el plasma [1].</li>
  <li><b>Fibrin&oacute;geno</b>: reponer cuando &lt; 1,5&nbsp;g/l o d&eacute;ficit funcional en sangrado [1].</li>
  <li><b>rFVIIa</b>: rescate <b>off-label</b> con riesgo trombótico; no de primera l&iacute;nea [1].</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Concentrado de fibrin&oacute;geno</h2>
<p>El fibrin&oacute;geno es el <b>primer factor que desciende</b> en la hemorragia masiva y el sustrato final del co&aacute;gulo. Su
reposici&oacute;n &mdash;con <b>concentrado de fibrin&oacute;geno</b> o crioprecipitado&mdash; est&aacute; indicada cuando, en contexto de sangrado, el
fibrin&oacute;geno plasm&aacute;tico es <b>&lt; 1,5&nbsp;g/l</b> o hay d&eacute;ficit funcional en viscoel&aacute;stica [1]. En Europa, el concentrado de
fibrin&oacute;geno ha desplazado en gran medida al crioprecipitado por su estandarizaci&oacute;n y seguridad (PBM-02).</p>

<h2 class="sec"><span class="num">3.</span>Factor VII activado recombinante (rFVIIa)</h2>
<p>El <b>rFVIIa</b> potencia la generaci&oacute;n de trombina en el sitio de la lesi&oacute;n. Su uso aprobado es limitado (p.&nbsp;ej.
hemofilia con inhibidores); en la hemorragia perioperatoria masiva refractaria es un <b>recurso de rescate off-label</b>,
tras optimizar plaquetas, fibrin&oacute;geno, calcio, temperatura y pH. Su eficacia en este escenario es incierta y se asocia a
<b>eventos trombóticos</b>, por lo que <b>no es un f&aacute;rmaco de primera l&iacute;nea</b> [1].</p>

<div class="box alert avoid-break"><span class="box-h">Precauci&oacute;n con el rFVIIa</span>
  <p>El rFVIIa no sustituye el control quir&uacute;rgico ni la correcci&oacute;n del entorno (calcio, temperatura, pH, fibrin&oacute;geno). Su
  uso off-label en hemorragia refractaria debe ser una decisi&oacute;n meditada por el riesgo trombótico y la evidencia limitada [1].</p>
</div>

<h2 class="sec"><span class="num">4.</span>Desmopresina (DDAVP)</h2>
<p>La <b>desmopresina</b> libera factor de von Willebrand y factor VIII de los dep&oacute;sitos endoteliales. Es &uacute;til en la
<b>enfermedad de von Willebrand tipo 1 respondedora</b> y en la <b>disfunci&oacute;n plaquetaria</b> (ur&eacute;mica o inducida por
f&aacute;rmacos), como alternativa o complemento a los hemoderivados [1]. Debe vigilarse la <b>hiponatremia</b> por su efecto
antidiur&eacute;tico, especialmente con dosis repetidas.</p>

<h2 class="sec"><span class="num">5.</span>Tabla integradora de uso dirigido</h2>
<div class="tbl-title">Tabla 1 &middot; F&aacute;rmacos hemost&aacute;ticos: d&eacute;ficit diana, indicaci&oacute;n y cautela</div>
<table class="avoid-break">
  <thead><tr><th style="width:22%">F&aacute;rmaco</th><th>Indicaci&oacute;n dirigida</th><th style="width:24%">Cautela</th></tr></thead>
  <tbody>
    <tr><td><b>CCP</b></td><td>Reversi&oacute;n urgente de AVK; d&eacute;ficit de factores en sangrado</td><td>Riesgo trombótico; dosis dirigida [1]</td></tr>
    <tr><td><b>Fibrin&oacute;geno / crio</b></td><td>Fibrin&oacute;geno &lt; 1,5&nbsp;g/l o d&eacute;ficit funcional en sangrado</td><td>Reponer guiado por objetivo [1]</td></tr>
    <tr><td><b>rFVIIa</b></td><td>Rescate off-label en hemorragia refractaria (tras optimizar todo)</td><td>Eventos trombóticos; no 1.&ordf; l&iacute;nea [1]</td></tr>
    <tr><td><b>Desmopresina</b></td><td>vW tipo 1 respondedora; disfunci&oacute;n plaquetaria</td><td>Hiponatremia; taquifilaxia [1]</td></tr>
  </tbody>
  <caption>S&iacute;ntesis a partir de la gu&iacute;a ESAIC [1]. El uso dirigido &mdash;al d&eacute;ficit demostrado, idealmente guiado por viscoel&aacute;stica&mdash; es el principio com&uacute;n.</caption>
</table>

<h2 class="sec"><span class="num">6.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> los f&aacute;rmacos hemost&aacute;ticos corrigen d&eacute;ficits concretos y son muy &uacute;tiles usados de
forma <b>dirigida</b> (CCP para AVK, fibrin&oacute;geno para hipofibrinogenemia, desmopresina para vW/disfunci&oacute;n plaquetaria); el
<b>rFVIIa</b> es un recurso de rescate off-label con riesgo trombótico y evidencia limitada. Ninguno sustituye el control
quir&uacute;rgico ni el entorno fisiol&oacute;gico.</p>
<p>Conecta con <b>PBM-02</b> (fibrin&oacute;geno/crio), <b>PBM-09</b> (guía por viscoel&aacute;stica), <b>PBM-13</b> (hemorragia masiva),
<b>PBM-16</b> (reversi&oacute;n de anticoagulantes) y <b>PBM-17</b> (coagulopat&iacute;as). Cierra el eje de hemostasia de la serie.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Usa el f&aacute;rmaco hemost&aacute;tico que corresponde al d&eacute;ficit (CCP, fibrin&oacute;geno, desmopresina), guiado por viscoel&aacute;stica
  &mdash;y reserva el rFVIIa como rescate off-label por su riesgo trombótico&mdash;.</p>
</div>

<h2 class="sec"><span class="num">7.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>REV</b> anclado en la gu&iacute;a ESAIC de sangrado perioperatorio grave [1], complementada por la gu&iacute;a de trastornos
raros [2] y la gu&iacute;a BSH de plasma/crioprecipitado [3], verificadas contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID).
El dintel de fibrin&oacute;geno (&lt; 1,5&nbsp;g/l), las indicaciones del CCP y la cautela con el rFVIIa proceden de estas fuentes; se
declara expl&iacute;citamente el car&aacute;cter <b>off-label</b> y el riesgo trombótico del rFVIIa.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">8.</span>Referencias</h2>
<ol class="refs">
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
  <li>Mumford AD, Ackroyd S, Alikhan R, Bowles L, Chowdary P, Grainger J, et al. Guideline for the diagnosis and management of the rare coagulation disorders (UKHCDO / British Committee for Standards in Haematology). <i>Br J Haematol</i> 2014;167(3):304&ndash;326. <span class="doi">doi:10.1111/bjh.13058</span> &middot; PMID 25100430.</li>
  <li>Green L, Bolton-Maggs P, Beattie C, Cardigan R, Kallis Y, Stanworth SJ, et al. British Society of Haematology Guidelines on the spectrum of fresh frozen plasma and cryoprecipitate products. <i>Br J Haematol</i> 2018;181(1):54&ndash;67. <span class="doi">doi:10.1111/bjh.15167</span> &middot; PMID 29527654.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-18-farmacos-hemostaticos.html")
    print("HTML:", h); print("PDF :", p)
