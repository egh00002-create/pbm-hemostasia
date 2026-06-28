# -*- coding: utf-8 -*-
"""PBM-06 - Eritropoyetina (EPO) en PBM: evidencia y uso. Ancla META."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-06 Eritropoyetina (EPO) en PBM. Ancla META.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-06 - Modulo 2 (Pilar 1) - ancla META - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-06</span>
    <span class="badge b-meta">META &middot; revisi&oacute;n sistem&aacute;tica / metaan&aacute;lisis</span>
    <span class="module-tag">M&oacute;dulo 2 &middot; Pilar 1: optimizar la masa eritrocitaria</span>
  </div>
  <div class="kicker">Eritropoyetina &middot; ESA + hierro &middot; Indicaciones selectivas</div>
  <h1 class="title">Eritropoyetina (EPO) en PBM: evidencia y uso</h1>
  <div class="subtitle">Una herramienta potente y selectiva &mdash; no un sustituto del hierro ni una medida universal</div>
  <div class="meta-row">
    <span class="meta-chip">Qu&eacute; son los ESA</span>
    <span class="meta-chip">EPO + hierro 3&ndash;4 semanas antes</span>
    <span class="meta-chip">Indicaciones m&aacute;s s&oacute;lidas</span>
    <span class="meta-chip">Riesgo tromboembólico</span>
    <span class="meta-chip">Balance beneficio-riesgo</span>
  </div>
  <div class="refbar">
    <b>Ancla de evidencia (referencia vertebral):</b> Lasocki S, Campfort M, Leger M, Rineau E.
    <i>ESAs in perioperative anemia management: Who, what, how and why?</i>
    Best Pract Res Clin Anaesthesiol 2023;37(4):519&ndash;526. <span class="mono">doi:10.1016/j.bpa.2023.10.002 &middot; PMID&nbsp;39764839</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> los agentes estimuladores de la eritropoyesis (ESA), asociados a hierro y administrados
    <b>3&ndash;4 semanas antes</b> de la cirug&iacute;a, elevan la hemoglobina y reducen la transfusi&oacute;n en escenarios seleccionados.
    Pero son caros, exigen <b>hierro adecuado</b> y conllevan un <b>riesgo tromboembólico</b> que obliga a una indicaci&oacute;n
    selectiva, no universal.
  </div>
  <div class="lead">
    <p>La eritropoyetina recombinante y otros ESA estimulan directamente la producci&oacute;n de hematíes. En PBM son una opci&oacute;n
    de <b>segunda l&iacute;nea selectiva</b> dentro del pilar 1, especialmente cuando el hierro solo no basta o cuando el paciente
    rechaza la transfusi&oacute;n.</p>
    <p>Este documento, con ancla <b>META</b>, sit&uacute;a la EPO con honestidad: d&oacute;nde la evidencia es m&aacute;s s&oacute;lida, c&oacute;mo usarla
    (siempre con hierro y con antelaci&oacute;n) y qu&eacute; riesgos vigilar [1].</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>Qu&eacute; son los ESA y c&oacute;mo act&uacute;an</li>
  <li>C&oacute;mo se usan: EPO + hierro, con antelaci&oacute;n</li>
  <li>D&oacute;nde la evidencia es m&aacute;s s&oacute;lida</li>
  <li>Riesgos y balance beneficio-riesgo</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>Qu&eacute; son los ESA y c&oacute;mo act&uacute;an</h2>
<p>Los agentes estimuladores de la eritropoyesis (ESA) &mdash;eritropoyetina recombinante y derivados&mdash; reproducen la se&ntilde;al
de la EPO end&oacute;gena y estimulan la m&eacute;dula para aumentar la masa eritrocitaria. Desarrollados en los a&ntilde;os 80 para la anemia
renal y oncol&oacute;gica, se aplican en el perioperatorio para <b>elevar la Hb antes de cirug&iacute;as con riesgo hemorr&aacute;gico
moderado-alto</b> [1]. Requieren <b>sustrato</b>: sin hierro suficiente, la respuesta es pobre.</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>La EPO <b>no sustituye al hierro</b>: se administra <b>con</b> hierro (preferentemente IV) para ser eficaz [1].</li>
  <li>Necesita <b>tiempo</b>: pauta t&iacute;pica de alta dosis <b>3&ndash;4 semanas antes</b> de la cirug&iacute;a [1].</li>
  <li>Conlleva riesgo <b>tromboembólico</b>: indicaci&oacute;n selectiva y valoraci&oacute;n individual del balance [1].</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>C&oacute;mo se usan: EPO + hierro, con antelaci&oacute;n</h2>
<p>La estrategia con mejor respaldo combina <b>ESA en dosis alta + hierro (idealmente IV)</b>, iniciada <b>3&ndash;4 semanas
antes</b> de la intervenci&oacute;n; as&iacute; se eleva la Hb perioperatoria y se reduce la necesidad de transfusi&oacute;n en cirug&iacute;as
seleccionadas (ortop&eacute;dica y cardíaca, sobre todo) [1]. Caben dos enfoques: tratar de forma sistem&aacute;tica por debajo de un
dintel de Hb (p.&nbsp;ej. &lt; 13&nbsp;g/dl) o un abordaje <b>personalizado</b> dirigido a la anemia inflamatoria o renal [1].</p>

<h2 class="sec"><span class="num">3.</span>D&oacute;nde la evidencia es m&aacute;s s&oacute;lida</h2>
<p>Las indicaciones con mejor relaci&oacute;n beneficio-riesgo son: el <b>paciente an&eacute;mico que rechaza la transfusi&oacute;n</b> (p.&nbsp;ej.
Testigos de Jehov&aacute;), la <b>anemia de proceso cr&oacute;nico/renal</b> y la <b>ferropenia funcional</b> que responde mal al hierro
solo [1]. La gu&iacute;a europea de cirug&iacute;a cardíaca (EACTS/EACTAIC 2024) respalda el uso de hierro y ESA en la optimizaci&oacute;n
preoperatoria de la anemia en ese contexto [3]. El beneficio se concreta sobre todo en <b>reducci&oacute;n de transfusi&oacute;n</b>;
la se&ntilde;al en <b>mortalidad</b> es escasa o nula, coherente con el tono honesto del PBM.</p>

<h2 class="sec"><span class="num">4.</span>Riesgos y balance beneficio-riesgo</h2>
<p>El principal riesgo de los ESA es el <b>tromboembolismo</b>, especialmente con objetivos de Hb altos. El balance debe
sopesarse con cuidado en <b>pacientes de alto riesgo</b>, particularmente en <b>cirug&iacute;a oncol&oacute;gica</b> (preocupaci&oacute;n por
progresi&oacute;n tumoral). La <b>coste-efectividad</b> sigue siendo discutida [1]. Por todo ello, la EPO es una herramienta de
indicaci&oacute;n <b>selectiva y razonada</b>, no un tratamiento por defecto.</p>

<div class="box alert avoid-break"><span class="box-h">Precauci&oacute;n</span>
  <p>No usar ESA sin asegurar hierro adecuado, sin tiempo suficiente, ni con objetivos de Hb elevados: se pierde eficacia y
  aumenta el riesgo trombótico. Valorar individualmente en cirug&iacute;a oncol&oacute;gica [1].</p>
</div>

<h2 class="sec"><span class="num">5.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> los ESA, con hierro y administrados con antelaci&oacute;n, elevan la Hb y reducen la
transfusi&oacute;n en escenarios seleccionados, pero su coste y su riesgo tromboembólico obligan a una indicaci&oacute;n selectiva; la
evidencia de mejora en mortalidad es escasa. Son un complemento del hierro, no su sustituto.</p>
<p>Conecta con <b>PBM-04</b> (diagn&oacute;stico), <b>PBM-05</b> (hierro, imprescindible para que el ESA funcione) y con la cirug&iacute;a
cardíaca de <b>EACTS</b> [3]; relevante para el paciente que rechaza transfusi&oacute;n.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>EPO + hierro, 3&ndash;4 semanas antes, en pacientes seleccionados (rechazo de transfusi&oacute;n, anemia renal/inflamatoria)
  &mdash;vigilando el riesgo trombótico y sin esperar beneficio en mortalidad&mdash;.</p>
</div>

<h2 class="sec"><span class="num">6.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>META</b> apoyado en una revisi&oacute;n especializada [1], el consenso de Frankfurt [2] y la gu&iacute;a EACTS/EACTAIC
2024 [3], verificados contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Se presentan con honestidad tanto el
beneficio (Hb y transfusi&oacute;n en escenarios seleccionados) como las limitaciones (riesgo tromboembólico, coste, ausencia de
se&ntilde;al clara en mortalidad) [1].</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">7.</span>Referencias</h2>
<ol class="refs">
  <li>Lasocki S, Campfort M, Leger M, Rineau E. ESAs in perioperative anemia management: Who, what, how and why? <i>Best Pract Res Clin Anaesthesiol</i> 2023;37(4):519&ndash;526. <span class="doi">doi:10.1016/j.bpa.2023.10.002</span> &middot; PMID 39764839.</li>
  <li>Mueller MM, Van Remoortel H, Meybohm P, Aranko K, Aubron C, Burger R, et al. Patient Blood Management: Recommendations From the 2018 Frankfurt Consensus Conference. <i>JAMA</i> 2019;321(10):983&ndash;997. <span class="doi">doi:10.1001/jama.2019.0554</span> &middot; PMID 30860564.</li>
  <li>Casselman FPA, Lance MD, Ahmed A, Ascari A, Blanco-Morillo J, Bolliger D, et al. 2024 EACTS/EACTAIC Guidelines on patient blood management in adult cardiac surgery in collaboration with EBCP. <i>Eur J Cardiothorac Surg</i> 2025;67(5):ezae352. <span class="doi">doi:10.1093/ejcts/ezae352</span> &middot; PMID 39385500.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-06-eritropoyetina.html")
    print("HTML:", h); print("PDF :", p)
