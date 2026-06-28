# -*- coding: utf-8 -*-
"""PBM-12 - Umbrales restrictivos de transfusion (TRICC, TRISS, REALITY). Ancla ECA. Nucleo."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-12 Umbrales restrictivos de transfusion. Ancla ECA. Documento nucleo.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-12 - Modulo 4 (Pilar 3) - ancla ECA - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de ensayos pivotales indexados verificados contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-12</span>
    <span class="badge b-eca">ECA &middot; ensayo pivotal</span>
    <span class="module-tag">M&oacute;dulo 4 &middot; Pilar 3: tolerancia a la anemia y transfusi&oacute;n</span>
  </div>
  <div class="kicker">Umbrales restrictivos &middot; TRICC &middot; TRISS &middot; REALITY &middot; el matiz del SCA</div>
  <h1 class="title">Umbrales restrictivos de transfusi&oacute;n</h1>
  <div class="subtitle">Menos es igual o mejor &mdash; salvo donde no lo es: el s&iacute;ndrome coronario agudo</div>
  <div class="meta-row">
    <span class="meta-chip">La idea restrictiva</span>
    <span class="meta-chip">TRICC</span>
    <span class="meta-chip">TRISS</span>
    <span class="meta-chip">REALITY y el SCA</span>
    <span class="meta-chip">S&iacute;ntesis Cochrane / CHEST</span>
  </div>
  <div class="refbar guiabar">
    <b>Ancla de evidencia (referencia vertebral):</b> H&eacute;bert PC, Wells G, Blajchman MA, et&nbsp;al.
    <i>A multicenter, randomized, controlled clinical trial of transfusion requirements in critical care (TRICC).</i>
    N Engl J Med 1999;340(6):409&ndash;417. <span class="mono">doi:10.1056/NEJM199902113400601 &middot; PMID&nbsp;9971864</span>.
  </div>
  <div class="tagline">
    2026 &middot; 6 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> en la mayor&iacute;a de los pacientes estables, una estrategia <b>restrictiva</b> (Hb &lt; 7&ndash;8&nbsp;g/dl) es
    <b>no inferior y a menudo mejor</b> que la liberal, y ahorra mucha sangre. Pero <b>no es universal</b>: en el <b>s&iacute;ndrome
    coronario agudo</b> la evidencia reciente favorece un umbral m&aacute;s <b>liberal</b> (&asymp;10&nbsp;g/dl).
  </div>
  <div class="lead">
    <p>El <b>pilar 3</b> del PBM se apoya en una de las ideas mejor respaldadas de la medicina transfusional: transfundir con
    umbrales <b>restrictivos</b> no empeora &mdash;y a veces mejora&mdash; los desenlaces, mientras reduce drásticamente la exposici&oacute;n a
    hemoderivados.</p>
    <p>Este documento n&uacute;cleo recorre los ensayos pivotales (TRICC, TRISS, REALITY), la s&iacute;ntesis Cochrane y las guías CHEST, y
    presenta con honestidad el <b>matiz cr&iacute;tico</b>: el s&iacute;ndrome coronario agudo, donde lo restrictivo puede no ser lo
    mejor.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>La idea restrictiva y por qu&eacute; funciona</li>
  <li>TRICC: el ensayo fundacional</li>
  <li>TRISS: shock s&eacute;ptico</li>
  <li>REALITY y el matiz del s&iacute;ndrome coronario agudo</li>
  <li>S&iacute;ntesis: Cochrane y CHEST</li>
  <li>Umbrales por contexto</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>La idea restrictiva y por qu&eacute; funciona</h2>
<p>La estrategia <b>restrictiva</b> retrasa la transfusi&oacute;n hasta un umbral de Hb m&aacute;s bajo (t&iacute;picamente 7&ndash;8&nbsp;g/dl) frente
a la <b>liberal</b> (9&ndash;10&nbsp;g/dl). Funciona porque el paciente <b>tolera</b> grados moderados de anemia mediante mecanismos
compensatorios (aumento del gasto, extracci&oacute;n de O<sub>2</sub>), mientras que la transfusi&oacute;n a&ntilde;ade riesgos (PBM-03). El
resultado neto en la mayor&iacute;a de poblaciones es <b>equivalencia o beneficio</b> con mucho menos consumo de sangre [6].</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>Restrictivo &asymp; <b>Hb &lt; 7&ndash;8&nbsp;g/dl</b>; reduce la exposici&oacute;n sin empeorar (y a veces mejorando) desenlaces [1,6].</li>
  <li>La excepci&oacute;n m&aacute;s s&oacute;lida es el <b>s&iacute;ndrome coronario agudo</b>: favorece un umbral m&aacute;s liberal [4,5].</li>
  <li>El umbral es una <b>referencia</b>: integra s&iacute;ntomas, sangrado activo y comorbilidad.</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>TRICC: el ensayo fundacional</h2>
<p><b>TRICC</b> (838 pacientes cr&iacute;ticos) compar&oacute; un umbral restrictivo (Hb &lt; 7, mantener 7&ndash;9) frente a liberal (&lt; 10,
mantener 10&ndash;12). La mortalidad a 30&nbsp;d&iacute;as fue similar (18,7&nbsp;% vs 23,3&nbsp;%; p=0,11), pero <b>menor con la estrategia
restrictiva</b> en pacientes menos graves (APACHE &le; 20) y m&aacute;s j&oacute;venes (&lt; 55&nbsp;a&ntilde;os), y la mortalidad hospitalaria fue
significativamente menor (22,2&nbsp;% vs 28,1&nbsp;%) [1]. Sus propios autores se&ntilde;alaron como posible excepci&oacute;n a los pacientes con
<b>cardiopat&iacute;a isqu&eacute;mica aguda</b>.</p>

<h2 class="sec"><span class="num">3.</span>TRISS: shock s&eacute;ptico</h2>
<p><b>TRISS</b> (998 pacientes con shock s&eacute;ptico) compar&oacute; umbrales de 7 frente a 9&nbsp;g/dl. La mortalidad a 90&nbsp;d&iacute;as fue
equivalente (43,0&nbsp;% vs 45,0&nbsp;%; RR 0,94; IC95&nbsp;% 0,78&ndash;1,09), con la mitad de transfusiones en el grupo restrictivo y
sin m&aacute;s eventos isqu&eacute;micos [2]. Refuerza la seguridad del umbral restrictivo incluso en el paciente s&eacute;ptico grave.</p>

<h2 class="sec"><span class="num">4.</span>REALITY y el matiz del s&iacute;ndrome coronario agudo</h2>
<p><b>REALITY</b> (668 pacientes con <b>infarto</b> y anemia) hall&oacute; que un umbral restrictivo (&le; 8) era <b>no inferior</b> al
liberal (&le; 10) para eventos cardiovasculares mayores a 30&nbsp;d&iacute;as (11,0&nbsp;% vs 14,0&nbsp;%), pero el intervalo de confianza
<b>inclu&iacute;a un posible da&ntilde;o</b> [3]. El metaan&aacute;lisis de datos individuales en infarto (MINT, REALITY y otros; 4.311
pacientes) mostr&oacute; <b>mayor muerte cardíaca a 30&nbsp;d&iacute;as</b> con la estrategia restrictiva (5,5&nbsp;% vs 3,7&nbsp;%; RR 1,47) y
mayor mortalidad global a 6&nbsp;meses [4]. Por eso las guías <b>CHEST 2024</b> recomiendan <b>en contra</b> de la estrategia
restrictiva en el SCA [5].</p>

<div class="box alert avoid-break"><span class="box-h">El matiz que cambia la conducta</span>
  <p>La regla &laquo;restrictivo por defecto&raquo; <b>se invierte en el s&iacute;ndrome coronario agudo</b>: ah&iacute; conviene un umbral m&aacute;s
  <b>liberal</b> (&asymp; 10&nbsp;g/dl), porque el miocardio isqu&eacute;mico tolera peor la anemia [4,5]. Es el ejemplo paradigm&aacute;tico de
  que el umbral no es universal.</p>
</div>

<h2 class="sec"><span class="num">5.</span>S&iacute;ntesis: Cochrane y CHEST</h2>
<p>La revisi&oacute;n <b>Cochrane 2025</b> (61 ensayos, 27.639 adultos) confirma que la estrategia restrictiva <b>reduce un 42&nbsp;%</b>
la proporci&oacute;n de pacientes transfundidos (RR 0,58) <b>sin aumentar la mortalidad a 30&nbsp;d&iacute;as</b> (RR 1,01) ni la mayor&iacute;a de
complicaciones [6]. Detecta dos contextos con se&ntilde;al propia: en <b>hemorragia digestiva</b> lo restrictivo redujo la
mortalidad, y en <b>lesi&oacute;n cerebral</b> los desenlaces neurol&oacute;gicos fueron mejores con estrategia liberal [6]. CHEST 2024
sintetiza para el cr&iacute;tico: restrictivo (7&ndash;8) por defecto, <b>salvo SCA</b> [5].</p>

<h2 class="sec"><span class="num">6.</span>Umbrales por contexto</h2>
<div class="tbl-title">Tabla 1 &middot; Umbral de hemoglobina orientativo por contexto</div>
<table class="avoid-break">
  <thead><tr><th>Contexto</th><th>Umbral orientativo</th><th style="width:16%">Respaldo</th></tr></thead>
  <tbody>
    <tr><td>Cr&iacute;tico estable / general hospitalizado</td><td>Hb &lt; 7&nbsp;g/dl</td><td class="c"><span class="gr gr-fuerte">FUERTE</span></td></tr>
    <tr><td>Shock s&eacute;ptico estable</td><td>Hb &lt; 7&nbsp;g/dl</td><td class="c"><span class="gr gr-fuerte">FUERTE</span></td></tr>
    <tr><td>Cirug&iacute;a cardíaca / enfermedad cardiovascular cr&oacute;nica</td><td>Hb &lt; 7,5&ndash;8&nbsp;g/dl</td><td class="c"><span class="gr gr-mod">MODERADA</span></td></tr>
    <tr><td><b>S&iacute;ndrome coronario agudo</b></td><td><b>Liberal &asymp; 10&nbsp;g/dl</b> (en contra de restrictivo)</td><td class="c"><span class="gr gr-no">MATIZ</span></td></tr>
    <tr><td>Lesi&oacute;n cerebral aguda</td><td>Considerar umbral m&aacute;s liberal</td><td class="c"><span class="gr gr-debil">D&Eacute;BIL</span></td></tr>
  </tbody>
  <caption>S&iacute;ntesis de TRICC [1], TRISS [2], REALITY [3], el metaan&aacute;lisis del SCA [4], CHEST [5] y Cochrane [6]. Umbrales orientativos; la decisi&oacute;n integra el cuadro cl&iacute;nico. Resumen en P-QR-02.</caption>
</table>

<h2 class="sec"><span class="num">7.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> la estrategia restrictiva (Hb &lt; 7&ndash;8&nbsp;g/dl) es no inferior y a menudo mejor que la
liberal en la mayor&iacute;a de los pacientes, y ahorra mucha sangre; la excepci&oacute;n s&oacute;lida es el <b>s&iacute;ndrome coronario agudo</b>,
donde conviene un umbral m&aacute;s liberal, y posiblemente la lesi&oacute;n cerebral. El umbral es una referencia que integra la
cl&iacute;nica.</p>
<p>Conecta con <b>PBM-02</b> (hematíes), <b>PBM-03</b> (riesgos que la restricci&oacute;n evita), <b>PBM-13</b> (la hemorragia masiva
sigue otra l&oacute;gica) y <b>PBM-14</b> (fisiolog&iacute;a de la tolerancia). Resumen en <b>P-QR-02</b>.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Transfunde restrictivo (Hb &lt; 7&ndash;8) por defecto &mdash;ahorra sangre sin empeorar desenlaces&mdash;, pero s&eacute; m&aacute;s liberal
  (&asymp;10) en el s&iacute;ndrome coronario agudo.</p>
</div>

<h2 class="sec"><span class="num">8.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>ECA</b> basado en ensayos pivotales y s&iacute;ntesis verificados contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o,
DOI/PMID). Cifras: TRICC mortalidad 18,7 vs 23,3&nbsp;% e intrahospitalaria 22,2 vs 28,1&nbsp;% [1]; TRISS 43,0 vs 45,0&nbsp;% (RR
0,94) [2]; REALITY MACE 11,0 vs 14,0&nbsp;% con IC que incluye da&ntilde;o [3]; metaan&aacute;lisis SCA muerte cardíaca RR 1,47 [4]; CHEST
en contra de restrictivo en SCA [5]; Cochrane RR 0,58 transfusi&oacute;n y RR 1,01 mortalidad [6]. Se declara expl&iacute;citamente el
<b>matiz del SCA</b> como excepci&oacute;n a la regla restrictiva.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">9.</span>Referencias</h2>
<ol class="refs">
  <li>H&eacute;bert PC, Wells G, Blajchman MA, Marshall J, Martin C, Pagliarello G, et al. A multicenter, randomized, controlled clinical trial of transfusion requirements in critical care (TRICC). <i>N Engl J Med</i> 1999;340(6):409&ndash;417. <span class="doi">doi:10.1056/NEJM199902113400601</span> &middot; PMID 9971864.</li>
  <li>Holst LB, Haase N, Wetterslev J, Wernerman J, Guttormsen AB, Karlsson S, et al. Lower versus higher hemoglobin threshold for transfusion in septic shock. <i>N Engl J Med</i> 2014;371(15):1381&ndash;1391. <span class="doi">doi:10.1056/NEJMoa1406617</span> &middot; PMID 25270275.</li>
  <li>Ducrocq G, Gonzalez-Juanatey JR, Puymirat E, Lemesle G, Cachanado M, Durand-Zaleski I, et al. Effect of a Restrictive vs Liberal Blood Transfusion Strategy on Major Cardiovascular Events Among Patients With Acute Myocardial Infarction and Anemia: The REALITY Randomized Clinical Trial. <i>JAMA</i> 2021;325(6):552&ndash;560. <span class="doi">doi:10.1001/jama.2021.0135</span> &middot; PMID 33560322.</li>
  <li>Carson JL, Fergusson DA, Noveck H, Mallick R, Simon T, Rao SV, et al. Restrictive versus Liberal Transfusion in Myocardial Infarction - A Patient-Level Meta-Analysis. <i>NEJM Evid</i> 2024;4(2):EVIDoa2400223. <span class="doi">doi:10.1056/EVIDoa2400223</span> &middot; PMID 39714935.</li>
  <li>Coz Yataco AO, Soghier I, H&eacute;bert PC, Belley-Cote E, Disselkamp M, Flynn D, et al. Red Blood Cell Transfusion in Critically Ill Adults: An American College of Chest Physicians Clinical Practice Guideline. <i>Chest</i> 2025;167(2):477&ndash;489. <span class="doi">doi:10.1016/j.chest.2024.09.016</span> &middot; PMID 39341492.</li>
  <li>Carson JL, Stanworth SJ, Dennis JA, Fergusson DA, Pagano MB, Roubinian NH, et al. Transfusion thresholds and other strategies for guiding red blood cell transfusion. <i>Cochrane Database Syst Rev</i> 2025;10(10):CD002042. <span class="doi">doi:10.1002/14651858.CD002042.pub6</span> &middot; PMID 41114449.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-12-umbrales-restrictivos.html")
    print("HTML:", h); print("PDF :", p)
