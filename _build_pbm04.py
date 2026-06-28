# -*- coding: utf-8 -*-
"""PBM-04 - Diagnostico y manejo de la anemia preoperatoria. Ancla GUIA."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-04 Anemia preoperatoria. Ancla GUIA.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-04 - Modulo 2 (Pilar 1) - ancla GUIA - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de guias y fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-04</span>
    <span class="badge b-guia">GU&Iacute;A &middot; gu&iacute;a / consenso formal</span>
    <span class="module-tag">M&oacute;dulo 2 &middot; Pilar 1: optimizar la masa eritrocitaria</span>
  </div>
  <div class="kicker">Anemia preoperatoria &middot; Diagn&oacute;stico &middot; Optimizaci&oacute;n con tiempo</div>
  <h1 class="title">Diagn&oacute;stico y manejo de la anemia preoperatoria</h1>
  <div class="subtitle">La anemia previa a la cirug&iacute;a no es un hallazgo banal: es un factor de riesgo modificable &mdash; si hay tiempo</div>
  <div class="meta-row">
    <span class="meta-chip">Por qu&eacute; importa la anemia</span>
    <span class="meta-chip">Cu&aacute;ndo y c&oacute;mo cribar</span>
    <span class="meta-chip">Algoritmo diagn&oacute;stico</span>
    <span class="meta-chip">Ferritina y PCR</span>
    <span class="meta-chip">El factor tiempo</span>
  </div>
  <div class="refbar guiabar">
    <b>Ancla de evidencia (referencia vertebral):</b> Hands K, Daru J, Evans C, et&nbsp;al.
    <i>Identification and management of preoperative anaemia in adults: A British Society for Haematology Guideline update.</i>
    Br J Haematol 2024;205(1):88&ndash;99. <span class="mono">doi:10.1111/bjh.19440 &middot; PMID&nbsp;38664944</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> la anemia preoperatoria es <b>frecuente, asociada a peores desenlaces y, a menudo, tratable</b>;
    su causa m&aacute;s com&uacute;n es la <b>ferropenia</b>. La clave es <b>cribar con antelaci&oacute;n</b> (semanas, no d&iacute;as) para diagnosticar
    y tratar la causa antes de la cirug&iacute;a; transfundir el d&iacute;a de la intervenci&oacute;n &laquo;para subir la Hb&raquo; es el peor abordaje.
  </div>
  <div class="lead">
    <p>La anemia previa a la cirug&iacute;a mayor afecta a una proporci&oacute;n elevada de pacientes y se asocia de forma consistente a
    m&aacute;s transfusiones, complicaciones y estancia [1]. Es el n&uacute;cleo del <b>pilar 1</b> del PBM: optimizar la propia masa
    eritrocitaria del paciente <b>antes</b> de exponerlo a la p&eacute;rdida quir&uacute;rgica.</p>
    <p>Este documento aterriza el <b>diagn&oacute;stico</b> &mdash;cribado precoz, definici&oacute;n de anemia, estudio de la ferropenia con
    ferritina ajustada a la inflamaci&oacute;n&mdash; y la <b>l&oacute;gica de tratamiento</b> seg&uacute;n el tiempo disponible. El hierro, la EPO y
    sus matices de evidencia se desarrollan en PBM-05 y PBM-06.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>Por qu&eacute; la anemia preoperatoria importa</li>
  <li>Definici&oacute;n y a qui&eacute;n cribar</li>
  <li>Algoritmo diagn&oacute;stico</li>
  <li>Ferritina y PCR: la trampa de la inflamaci&oacute;n</li>
  <li>El factor tiempo: qu&eacute; hacer seg&uacute;n los d&iacute;as disponibles</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>Por qu&eacute; la anemia preoperatoria importa</h2>
<p>La anemia preoperatoria es a la vez un <b>marcador</b> de comorbilidad y un <b>factor de riesgo modificable</b>: predice
mayor necesidad transfusional y peores desenlaces perioperatorios [1]. Tratarla es la intervenci&oacute;n de PBM con mayor
rendimiento porque act&uacute;a <b>antes</b> de la hemorragia, no durante ni despu&eacute;s.</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>La causa m&aacute;s frecuente y tratable es la <b>ferropenia</b> (absoluta o funcional) [1].</li>
  <li>El beneficio depende del <b>tiempo</b>: cribar al indicar la cirug&iacute;a, no en el preoperatorio inmediato.</li>
  <li>La transfusi&oacute;n <b>no</b> es el tratamiento de la anemia preoperatoria cr&oacute;nica: trata la causa.</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Definici&oacute;n y a qui&eacute;n cribar</h2>
<p>Se mantiene el umbral diagn&oacute;stico de anemia en <b>Hb &lt; 130&nbsp;g/l en el var&oacute;n y &lt; 120&nbsp;g/l en la mujer</b> (criterio
operativo usado tambi&eacute;n en los ensayos de PBM) [1]. La gu&iacute;a recomienda <b>cribar con hemograma completo</b>, incluyendo
índices eritrocitarios, a <b>todos los candidatos a cirug&iacute;a mayor</b> con sangrado esperado relevante, y hacerlo
<b>precozmente</b> para disponer de margen terap&eacute;utico [1].</p>

<h2 class="sec"><span class="num">3.</span>Algoritmo diagn&oacute;stico</h2>
<div class="flow avoid-break">
  <div class="step q"><b>Paso 1 &mdash; &iquest;Hay anemia?</b> Hb &lt; 130 (var&oacute;n) / &lt; 120&nbsp;g/l (mujer). Si s&iacute;, estudiar antes de operar.</div>
  <div class="step"><b>Paso 2 &mdash; Estudio del hierro:</b> ferritina y saturaci&oacute;n de transferrina, con <b>PCR</b> para interpretar la ferritina.</div>
  <div class="step"><b>Paso 3 &mdash; Clasificar:</b> ferropenia (absoluta o funcional), anemia de proceso cr&oacute;nico/inflamatorio, d&eacute;ficit de B<sub>12</sub>/folato o renal.</div>
  <div class="step a"><b>Paso 4 &mdash; Tratar la causa:</b> hierro (PBM-05), EPO si procede (PBM-06), reponer hematínicos; derivar si causa no filiada (p.&nbsp;ej. p&eacute;rdidas digestivas).</div>
</div>

<h2 class="sec"><span class="num">4.</span>Ferritina y PCR: la trampa de la inflamaci&oacute;n</h2>
<p>La ferritina es el mejor marcador de los dep&oacute;sitos de hierro, pero es un <b>reactante de fase aguda</b>: la inflamaci&oacute;n
la eleva y puede <b>enmascarar una ferropenia real</b>. Por eso la gu&iacute;a recomienda interpretarla junto a la <b>PCR</b> y
elevar el dintel de sospecha de ferropenia en contextos inflamatorios (ferritina hasta &asymp; 100&nbsp;&micro;g/l puede seguir
siendo compatible con d&eacute;ficit) [1]. La saturaci&oacute;n de transferrina ayuda a detectar la <b>ferropenia funcional</b>.</p>

<div class="box note avoid-break"><span class="box-h">Regla pr&aacute;ctica</span>
  <p>Ferritina &lt; 30&nbsp;&micro;g/l = ferropenia absoluta casi segura. Con inflamaci&oacute;n (PCR elevada), una ferritina
  &laquo;normal-baja&raquo; (30&ndash;100&nbsp;&micro;g/l) con saturaci&oacute;n de transferrina baja sugiere ferropenia que merece tratamiento [1].</p>
</div>

<h2 class="sec"><span class="num">5.</span>El factor tiempo: qu&eacute; hacer seg&uacute;n los d&iacute;as disponibles</h2>
<p>El margen temporal condiciona la estrategia. Con <b>varias semanas</b>, el hierro oral o intravenoso puede corregir la
anemia ferrop&eacute;nica antes de operar; con <b>menos margen</b>, el hierro intravenoso (&plusmn; EPO en casos seleccionados)
permite una respuesta m&aacute;s r&aacute;pida [1]. La consecuencia organizativa es clara: el cribado debe activarse <b>en el momento de
indicar la cirug&iacute;a</b>, integrado en la vía perioperatoria (conexi&oacute;n con prehabilitaci&oacute;n y RICA) [3].</p>

<h2 class="sec"><span class="num">6.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> la anemia preoperatoria es frecuente, pron&oacute;sticamente relevante y a menudo
corregible si se detecta a tiempo; la ferropenia es la causa principal y exige interpretar la ferritina a la luz de la
inflamaci&oacute;n. El beneficio de tratarla depende del <b>tiempo disponible</b>, por lo que el cribado precoz es la pieza
organizativa decisiva.</p>
<p>Conecta con <b>PBM-05</b> (ferropenia y hierro intravenoso, con sus matices de evidencia), <b>PBM-06</b> (EPO) y con la
cabeza de serie <b>PBM-01</b>; enlaza con las series hermanas de <b>prehabilitaci&oacute;n/CMA</b> y con la vía <b>RICA</b> [3].</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Criba la anemia al indicar la cirug&iacute;a, estudia el hierro con ferritina + PCR y trata la causa con tiempo &mdash;no
  transfundas para &laquo;subir la Hb&raquo; el d&iacute;a de la operaci&oacute;n&mdash;.</p>
</div>

<h2 class="sec"><span class="num">7.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>GUÍA</b> apoyado en la actualizaci&oacute;n 2024 de la BSH [1], el consenso de Frankfurt [2] y la revisi&oacute;n RICA [3],
verificados contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Los umbrales diagn&oacute;sticos (Hb 130/120&nbsp;g/l), el
ajuste de la ferritina por inflamaci&oacute;n y la recomendaci&oacute;n de cribado precoz proceden directamente de la gu&iacute;a [1]. La
fuerza de la evidencia del tratamiento (hierro, EPO) se matiza en PBM-05 y PBM-06.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">8.</span>Referencias</h2>
<ol class="refs">
  <li>Hands K, Daru J, Evans C, Kotze A, Lewis C, Narayan S, et al. Identification and management of preoperative anaemia in adults: A British Society for Haematology Guideline update. <i>Br J Haematol</i> 2024;205(1):88&ndash;99. <span class="doi">doi:10.1111/bjh.19440</span> &middot; PMID 38664944.</li>
  <li>Mueller MM, Van Remoortel H, Meybohm P, Aranko K, Aubron C, Burger R, et al. Patient Blood Management: Recommendations From the 2018 Frankfurt Consensus Conference. <i>JAMA</i> 2019;321(10):983&ndash;997. <span class="doi">doi:10.1001/jama.2019.0554</span> &middot; PMID 30860564.</li>
  <li>Moral V, Jeric&oacute; C, Abad Motos A, P&aacute;ramo JA, Quintana D&iacute;az M, Garc&iacute;a Erce JA. 2024 critical review of the patient blood management (PBM) recommendations of the Spanish enhanced recovery after major surgery (via RICA). <i>Cir Esp (Engl Ed)</i> 2025;103(2):104&ndash;114. <span class="doi">doi:10.1016/j.cireng.2024.10.008</span> &middot; PMID 39617300.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-04-anemia-preoperatoria.html")
    print("HTML:", h); print("PDF :", p)
