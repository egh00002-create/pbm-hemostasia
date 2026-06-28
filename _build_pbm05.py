# -*- coding: utf-8 -*-
"""PBM-05 - Ferropenia y hierro intravenoso. Ancla META."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-05 Ferropenia y hierro intravenoso. Ancla META.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-05 - Modulo 2 (Pilar 1) - ancla META - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-05</span>
    <span class="badge b-meta">META &middot; revisi&oacute;n sistem&aacute;tica / metaan&aacute;lisis</span>
    <span class="module-tag">M&oacute;dulo 2 &middot; Pilar 1: optimizar la masa eritrocitaria</span>
  </div>
  <div class="kicker">Ferropenia &middot; Hierro oral e intravenoso &middot; Qu&eacute; espera realmente la evidencia</div>
  <h1 class="title">Ferropenia y hierro intravenoso</h1>
  <div class="subtitle">El hierro corrige la ferropenia &mdash; pero &laquo;corregir la analítica&raquo; y &laquo;mejorar desenlaces&raquo; no son lo mismo</div>
  <div class="meta-row">
    <span class="meta-chip">Ferropenia absoluta y funcional</span>
    <span class="meta-chip">Hierro oral: c&oacute;mo dosificarlo</span>
    <span class="meta-chip">Hierro IV: cu&aacute;ndo</span>
    <span class="meta-chip">La lecci&oacute;n de PREVENTT</span>
    <span class="meta-chip">Honestidad sobre desenlaces</span>
  </div>
  <div class="refbar">
    <b>Ancla de evidencia (referencia vertebral):</b> Richards T, Baikady RR, Clevenger B, et&nbsp;al.
    <i>Preoperative intravenous iron to treat anaemia before major abdominal surgery (PREVENTT): a randomised, double-blind, controlled trial.</i>
    Lancet 2020;396(10259):1353&ndash;1361. <span class="mono">doi:10.1016/S0140-6736(20)31539-7 &middot; PMID&nbsp;32896294</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> el hierro &mdash;oral si hay tiempo, intravenoso si no&mdash; es el tratamiento de la <b>anemia
    ferrop&eacute;nica</b> preoperatoria y aumenta la hemoglobina. Pero la evidencia es <b>matizada</b>: el ensayo PREVENTT no
    demostr&oacute; reducci&oacute;n de transfusiones con hierro IV en cirug&iacute;a abdominal mayor. El beneficio es mayor cuando hay
    <b>ferropenia real, anemia significativa y tiempo</b>; menos claro como medida universal.
  </div>
  <div class="lead">
    <p>La ferropenia es la causa m&aacute;s frecuente de anemia preoperatoria y, a la vez, la m&aacute;s tratable. El hierro repone los
    dep&oacute;sitos y permite la eritropoyesis; la pregunta cl&iacute;nica no es <i>si</i> corrige la ferritina, sino <b>cu&aacute;ndo se
    traduce en mejores desenlaces</b>.</p>
    <p>Este documento, con ancla <b>META/ECA</b>, presenta el uso del hierro con honestidad: c&oacute;mo dosificar el oral, cu&aacute;ndo
    elegir el intravenoso y qu&eacute; ense&ntilde;a el ensayo PREVENTT sobre los l&iacute;mites del &laquo;hierro para todos&raquo; [1].</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>Ferropenia absoluta y funcional</li>
  <li>Hierro oral: c&oacute;mo dosificarlo bien</li>
  <li>Hierro intravenoso: cu&aacute;ndo elegirlo</li>
  <li>La lecci&oacute;n de PREVENTT</li>
  <li>S&iacute;ntesis pr&aacute;ctica y honestidad sobre la evidencia</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>Ferropenia absoluta y funcional</h2>
<p>La <b>ferropenia absoluta</b> es el agotamiento de los dep&oacute;sitos (ferritina baja); la <b>funcional</b> es la
incapacidad de movilizar el hierro a pesar de dep&oacute;sitos aparentemente normales, t&iacute;pica de la inflamaci&oacute;n (saturaci&oacute;n de
transferrina baja con ferritina normal-alta) [2]. Distinguirlas importa: la absoluta responde bien al hierro; la funcional
responde peor al hierro oral y puede requerir hierro IV &plusmn; EPO.</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>El objetivo es tratar la <b>ferropenia</b>, no &laquo;normalizar un n&uacute;mero&raquo;: la indicaci&oacute;n nace del d&eacute;ficit + la anemia + el contexto.</li>
  <li>El hierro <b>oral</b> sirve si hay tiempo y tolerancia; el <b>IV</b>, si hay intolerancia, mala absorci&oacute;n, poco margen o ferropenia funcional [2].</li>
  <li>La evidencia de mejora de <b>desenlaces duros</b> es desigual: clara en correcci&oacute;n de Hb, m&aacute;s d&eacute;bil en transfusi&oacute;n/mortalidad [1].</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Hierro oral: c&oacute;mo dosificarlo bien</h2>
<p>El hierro oral es barato y eficaz en la ferropenia absoluta <b>con margen de semanas</b>. La fisiolog&iacute;a de la hepcidina
ha cambiado la pauta: dosis <b>m&aacute;s bajas y menos frecuentes</b> (por ejemplo, una toma al d&iacute;a, o en d&iacute;as alternos) mejoran
la absorci&oacute;n fraccional y la tolerancia frente a las pautas cl&aacute;sicas de varias tomas diarias [2]. Requiere
<b>tiempo</b> (semanas) para reponer dep&oacute;sitos.</p>

<h2 class="sec"><span class="num">3.</span>Hierro intravenoso: cu&aacute;ndo elegirlo</h2>
<p>El hierro IV (formulaciones modernas en dosis &uacute;nica alta) repone dep&oacute;sitos con rapidez y evita los problemas de
absorci&oacute;n y tolerancia digestiva. Es la opci&oacute;n preferente ante <b>intolerancia o ineficacia del oral, malabsorci&oacute;n,
anemia moderada-grave, ferropenia funcional o poco tiempo hasta la cirug&iacute;a</b> [2]. Su perfil de seguridad es bueno con
las formulaciones actuales; las reacciones graves son raras.</p>

<h2 class="sec"><span class="num">4.</span>La lecci&oacute;n de PREVENTT</h2>
<p>El ensayo <b>PREVENTT</b> aleatoriz&oacute; a 487 pacientes an&eacute;micos a hierro IV (carboximaltosa f&eacute;rrica 1000&nbsp;mg) o placebo
10&ndash;42&nbsp;d&iacute;as antes de cirug&iacute;a abdominal mayor. <b>No</b> redujo el desenlace combinado de muerte o transfusi&oacute;n
(riesgo relativo 1,03; IC95&nbsp;% 0,78&ndash;1,37) ni el n&uacute;mero de transfusiones a los 30&nbsp;d&iacute;as [1]. Es la pieza de honestidad
del tema: administrar hierro IV de forma <b>indiscriminada</b> en cirug&iacute;a abdominal no mejor&oacute; los desenlaces primarios,
aunque s&iacute; aument&oacute; la Hb y mejor&oacute; algunos desenlaces secundarios a largo plazo.</p>

<div class="box rev avoid-break"><span class="box-h">C&oacute;mo leer PREVENTT sin sobreinterpretarlo</span>
  <p>PREVENTT no dice &laquo;el hierro no sirve&raquo;: dice que <b>darlo a todo an&eacute;mico tarde y sin filiar el d&eacute;ficit</b> no rinde en
  transfusi&oacute;n. El mensaje PBM coherente es <b>diagnosticar la ferropenia, tratarla con tiempo y reservar el hierro IV</b>
  para quien lo necesita, no usarlo como gesto universal de &uacute;ltima hora [1,2].</p>
</div>

<h2 class="sec"><span class="num">5.</span>S&iacute;ntesis pr&aacute;ctica y honestidad sobre la evidencia</h2>
<div class="tbl-title">Tabla 1 &middot; Elecci&oacute;n de la vía del hierro seg&uacute;n el escenario</div>
<table class="avoid-break">
  <thead><tr><th style="width:30%">Escenario</th><th>Opci&oacute;n preferente</th><th style="width:18%">Certeza</th></tr></thead>
  <tbody>
    <tr><td>Ferropenia absoluta, &ge; 6&ndash;8 semanas de margen, buena tolerancia</td><td>Hierro <b>oral</b> a dosis baja diaria o en d&iacute;as alternos</td><td class="c"><span class="gr gr-mod">MODERADA</span></td></tr>
    <tr><td>Intolerancia/ineficacia oral, malabsorci&oacute;n, anemia moderada-grave o poco tiempo</td><td>Hierro <b>intravenoso</b> (dosis &uacute;nica alta)</td><td class="c"><span class="gr gr-mod">MODERADA</span></td></tr>
    <tr><td>Ferropenia funcional / inflamatoria</td><td>Hierro <b>IV</b> &plusmn; EPO (&rarr; PBM-06)</td><td class="c"><span class="gr gr-debil">D&Eacute;BIL</span></td></tr>
    <tr><td>Hierro IV universal sin filiar d&eacute;ficit en cirug&iacute;a abdominal</td><td><b>No</b> reduce transfusi&oacute;n (PREVENTT)</td><td class="c"><span class="gr gr-no">EN CONTRA</span></td></tr>
  </tbody>
  <caption>S&iacute;ntesis a partir de PREVENTT [1] y de la gu&iacute;a BSH [2]. La certeza refleja la heterogeneidad real de la evidencia por escenario.</caption>
</table>

<h2 class="sec"><span class="num">6.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> el hierro es el tratamiento de la anemia ferrop&eacute;nica y eleva la hemoglobina, pero
su impacto en transfusi&oacute;n y desenlaces depende de <b>tratar al paciente correcto, con el d&eacute;ficit correcto y con tiempo</b>;
el uso indiscriminado de hierro IV de &uacute;ltima hora no rinde (PREVENTT). Diagnosticar bien y anticipar es lo que convierte el
hierro en una herramienta &uacute;til de PBM, en l&iacute;nea con el marco del consenso internacional [3].</p>
<p>Conecta con <b>PBM-04</b> (diagn&oacute;stico de la anemia), <b>PBM-06</b> (EPO, para ferropenia funcional/inflamatoria y rechazo
de transfusi&oacute;n) y con <b>PBM-12</b> (umbrales restrictivos que reducen la exposici&oacute;n a transfusi&oacute;n).</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Hierro oral a dosis baja si hay tiempo, hierro IV si no o si la ferropenia es funcional &mdash;pero diagnostica primero:
  el hierro universal de &uacute;ltima hora no reduce transfusiones&mdash;.</p>
</div>

<h2 class="sec"><span class="num">7.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento de tipo <b>META/ECA</b>. Las cifras de PREVENTT (RR 1,03; IC95&nbsp;% 0,78&ndash;1,37 para muerte o transfusi&oacute;n) [1] y
las recomendaciones de dosificaci&oacute;n y elecci&oacute;n de vía [2] proceden de fuentes primarias verificadas contra PubMed
(autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Se declara expl&iacute;citamente el resultado <b>neutro</b> de PREVENTT en su desenlace
primario para evitar sobreestimar el beneficio del hierro IV universal.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">8.</span>Referencias</h2>
<ol class="refs">
  <li>Richards T, Baikady RR, Clevenger B, Butcher A, Abeysiri S, Chau M, et al. Preoperative intravenous iron to treat anaemia before major abdominal surgery (PREVENTT): a randomised, double-blind, controlled trial. <i>Lancet</i> 2020;396(10259):1353&ndash;1361. <span class="doi">doi:10.1016/S0140-6736(20)31539-7</span> &middot; PMID 32896294.</li>
  <li>Hands K, Daru J, Evans C, Kotze A, Lewis C, Narayan S, et al. Identification and management of preoperative anaemia in adults: A British Society for Haematology Guideline update. <i>Br J Haematol</i> 2024;205(1):88&ndash;99. <span class="doi">doi:10.1111/bjh.19440</span> &middot; PMID 38664944.</li>
  <li>Mueller MM, Van Remoortel H, Meybohm P, Aranko K, Aubron C, Burger R, et al. Patient Blood Management: Recommendations From the 2018 Frankfurt Consensus Conference. <i>JAMA</i> 2019;321(10):983&ndash;997. <span class="doi">doi:10.1001/jama.2019.0554</span> &middot; PMID 30860564.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-05-ferropenia-hierro-iv.html")
    print("HTML:", h); print("PDF :", p)
