# -*- coding: utf-8 -*-
"""PBM-13 - Hemorragia critica y protocolo de transfusion masiva. Ancla GUIA. Nucleo."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-13 Hemorragia critica y transfusion masiva. Ancla GUIA. Documento nucleo.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-13 - Modulo 4 (Pilar 3) - ancla GUIA - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-13</span>
    <span class="badge b-guia">GU&Iacute;A &middot; gu&iacute;a / consenso formal</span>
    <span class="module-tag">M&oacute;dulo 4 &middot; Pilar 3: tolerancia a la anemia y transfusi&oacute;n</span>
  </div>
  <div class="kicker">Hemorragia cr&iacute;tica &middot; Protocolo de transfusi&oacute;n masiva &middot; Resucitaci&oacute;n de control de da&ntilde;os</div>
  <h1 class="title">Hemorragia crítica y protocolo de transfusi&oacute;n masiva</h1>
  <div class="subtitle">Cuando la regla restrictiva se suspende: aqu&iacute; manda la velocidad, la proporci&oacute;n y el protocolo</div>
  <div class="meta-row">
    <span class="meta-chip">Cu&aacute;ndo activar</span>
    <span class="meta-chip">Resucitaci&oacute;n de control de da&ntilde;os</span>
    <span class="meta-chip">Proporciones y PROPPR</span>
    <span class="meta-chip">TXA precoz y fibrin&oacute;geno</span>
    <span class="meta-chip">Calcio, temperatura, pH</span>
  </div>
  <div class="refbar guiabar">
    <b>Ancla de evidencia (referencia vertebral):</b> Holcomb JB, Tilley BC, Baraniuk S, et&nbsp;al.
    <i>Transfusion of plasma, platelets, and red blood cells in a 1:1:1 vs a 1:1:2 ratio and mortality in patients with severe trauma (PROPPR).</i>
    JAMA 2015;313(5):471&ndash;482. <span class="mono">doi:10.1001/jama.2015.12 &middot; PMID&nbsp;25647203</span>.
  </div>
  <div class="tagline">
    2026 &middot; 4 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> en la hemorragia crítica la l&oacute;gica cambia: no se espera a umbrales, se activa un <b>protocolo de
    transfusi&oacute;n masiva</b> con hemoderivados en <b>proporci&oacute;n equilibrada</b> (cercana a 1:1:1), <b>tranex&aacute;mico precoz</b>,
    reposici&oacute;n de <b>fibrin&oacute;geno</b> y control de <b>calcio, temperatura y pH</b>. La rapidez y la organizaci&oacute;n salvan vidas.
  </div>
  <div class="lead">
    <p>La hemorragia crítica &mdash;p&eacute;rdida masiva y r&aacute;pida que amenaza la vida&mdash; es la situaci&oacute;n donde el PBM <b>suspende
    temporalmente</b> la filosof&iacute;a restrictiva: el objetivo inmediato es <b>parar el sangrado y mantener la perfusi&oacute;n y la
    coagulaci&oacute;n</b>. Aqu&iacute; la herramienta no es un umbral, sino un <b>protocolo</b>.</p>
    <p>Este documento n&uacute;cleo, con ancla <b>GUÍA</b>, sintetiza la resucitaci&oacute;n de control de da&ntilde;os: cu&aacute;ndo activar el protocolo
    de transfusi&oacute;n masiva, qu&eacute; proporciones usar (con la lectura honesta de PROPPR), el papel del tranex&aacute;mico y el
    fibrin&oacute;geno, y el control del entorno fisiol&oacute;gico.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>Qu&eacute; es y cu&aacute;ndo activar el protocolo</li>
  <li>Resucitaci&oacute;n de control de da&ntilde;os</li>
  <li>Proporciones de hemoderivados: la lecci&oacute;n de PROPPR</li>
  <li>Tranex&aacute;mico precoz y fibrin&oacute;geno</li>
  <li>El entorno: calcio, temperatura y pH</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>Qu&eacute; es y cu&aacute;ndo activar el protocolo</h2>
<p>La transfusi&oacute;n masiva se define cl&aacute;sicamente como &asymp; un volumen sangu&iacute;neo en 24&nbsp;h (o ritmos equivalentes, como
&ge; 4 concentrados en 1&nbsp;h con sangrado activo). M&aacute;s &uacute;til que la definici&oacute;n es la <b>activaci&oacute;n precoz</b> ante una
hemorragia que no se controla: escalas y el juicio cl&iacute;nico disparan un <b>protocolo</b> que entrega paquetes de
hemoderivados de forma inmediata y repetida, evitando el retraso log&iacute;stico [2].</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>En hemorragia crítica <b>no se aplican umbrales restrictivos</b>: la prioridad es controlar el sangrado y la coagulaci&oacute;n [2].</li>
  <li>Activar el protocolo <b>pronto</b> y administrar hemoderivados en <b>proporci&oacute;n equilibrada</b> [1,2].</li>
  <li><b>Tranex&aacute;mico precoz</b> y reposici&oacute;n de <b>fibrin&oacute;geno</b> son intervenciones de alto valor [2,3].</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Resucitaci&oacute;n de control de da&ntilde;os</h2>
<p>El paradigma es la <b>resucitaci&oacute;n de control de da&ntilde;os</b>: hipotensi&oacute;n permisiva controlada hasta el control quir&uacute;rgico,
<b>limitaci&oacute;n de cristaloides</b> (que diluyen y agravan la coagulopat&iacute;a), transfusi&oacute;n precoz y equilibrada, y correcci&oacute;n
agresiva del entorno fisiol&oacute;gico. El objetivo es romper el c&iacute;rculo de la <b>tr&iacute;ada letal</b> (hipotermia, acidosis,
coagulopat&iacute;a) [2].</p>

<h2 class="sec"><span class="num">3.</span>Proporciones de hemoderivados: la lecci&oacute;n de PROPPR</h2>
<p>El ensayo <b>PROPPR</b> (680 pacientes de trauma con hemorragia masiva) compar&oacute; proporciones de plasma:plaquetas:hematíes
de <b>1:1:1</b> frente a <b>1:1:2</b>. No hubo diferencia significativa en mortalidad a 24&nbsp;h (12,7&nbsp;% vs 17,0&nbsp;%) ni a
30&nbsp;d&iacute;as (22,4&nbsp;% vs 26,1&nbsp;%), <b>pero</b> el grupo 1:1:1 logr&oacute; <b>m&aacute;s hemostasia</b> (86&nbsp;% vs 78&nbsp;%) y <b>menos
muertes por exanguinaci&oacute;n</b> a las 24&nbsp;h (9,2&nbsp;% vs 14,6&nbsp;%), sin m&aacute;s complicaciones [1]. De ah&iacute; la recomendaci&oacute;n de
una proporci&oacute;n <b>equilibrada (cercana a 1:1:1)</b> en la fase inicial, hasta poder guiar por viscoel&aacute;stica (PBM-09).</p>

<div class="box rev avoid-break"><span class="box-h">C&oacute;mo leer PROPPR</span>
  <p>PROPPR no demostr&oacute; diferencia en su desenlace primario (mortalidad), pero s&iacute; <b>ventaja en hemostasia y muerte por
  exanguinaci&oacute;n</b> con 1:1:1. La lectura pr&aacute;ctica: empezar equilibrado y <b>transitar a un manejo guiado por objetivos</b>
  (viscoel&aacute;stica, fibrin&oacute;geno) en cuanto sea posible [1,2].</p>
</div>

<h2 class="sec"><span class="num">4.</span>Tranex&aacute;mico precoz y fibrin&oacute;geno</h2>
<p>El <b>&aacute;cido tranex&aacute;mico</b> administrado <b>precozmente</b> reduce la muerte por hemorragia en el trauma (CRASH-2: RR 0,85
para muerte por sangrado) y debe formar parte del protocolo desde el inicio [3]. La <b>reposici&oacute;n de fibrin&oacute;geno</b> &mdash;el
primer factor que cae&mdash; es prioritaria cuando est&aacute; bajo (&lt; 1,5&nbsp;g/l o d&eacute;ficit funcional), con concentrado de fibrin&oacute;geno
o crioprecipitado [2]. Las <b>plaquetas</b> se manejan dentro del protocolo, no por los umbrales profil&aacute;cticos de PBM-02 [4].</p>

<h2 class="sec"><span class="num">5.</span>El entorno: calcio, temperatura y pH</h2>
<p>La transfusi&oacute;n masiva induce <b>hipocalcemia</b> (el citrato de los hemoderivados quela el calcio): hay que monitorizar y
reponer <b>calcio i&oacute;nico</b>. Mantener la <b>normotermia</b> (calentadores, ambiente) y <b>corregir la acidosis</b> es
imprescindible para que la coagulaci&oacute;n funcione [2]. Estas medidas baratas son tan decisivas como los hemoderivados.</p>

<div class="box pearl avoid-break"><span class="box-h">Perla</span>
  <p>En la transfusi&oacute;n masiva, recuerda la regla de las tres &laquo;C&raquo; del entorno: <b>calcio, calor (temperatura) y correcci&oacute;n
  del pH</b>. Sin ellas, ning&uacute;n ratio de hemoderivados coagula bien [2].</p>
</div>

<h2 class="sec"><span class="num">6.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> en la hemorragia crítica se suspende la l&oacute;gica restrictiva y se activa precozmente un
protocolo de transfusi&oacute;n masiva con proporci&oacute;n equilibrada (cercana a 1:1:1), tranex&aacute;mico precoz, fibrin&oacute;geno y control de
calcio/temperatura/pH; PROPPR no mostr&oacute; diferencia en mortalidad pero s&iacute; mejor hemostasia con 1:1:1. La transici&oacute;n a manejo
guiado por objetivos es lo ideal.</p>
<p>Conecta con <b>PBM-08</b> (TXA), <b>PBM-09</b> (viscoel&aacute;stica), <b>PBM-02/18</b> (componentes y fibrin&oacute;geno), <b>PBM-12</b>
(por contraste: aqu&iacute; no rigen los umbrales) y con la serie hermana de <b>traumatolog&iacute;a</b>.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Activa pronto el protocolo, transfunde equilibrado (&asymp;1:1:1), da tranex&aacute;mico precoz y fibrin&oacute;geno, y cuida calcio,
  temperatura y pH &mdash;luego guía por viscoel&aacute;stica&mdash;.</p>
</div>

<h2 class="sec"><span class="num">7.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>GUÍA</b> apoyado en PROPPR [1], la gu&iacute;a ESAIC [2], CRASH-2 [3] y la gu&iacute;a AABB/ICTMG de plaquetas [4],
verificados contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Cifras de PROPPR (mortalidad 24&nbsp;h 12,7 vs 17,0&nbsp;%;
hemostasia 86 vs 78&nbsp;%; exanguinaci&oacute;n 9,2 vs 14,6&nbsp;%) [1] tomadas de la fuente. Se presenta con honestidad que PROPPR fue
<b>neutro en su desenlace primario</b> pese a las ventajas secundarias del 1:1:1.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">8.</span>Referencias</h2>
<ol class="refs">
  <li>Holcomb JB, Tilley BC, Baraniuk S, Fox EE, Wade CE, Podbielski JM, et al. Transfusion of plasma, platelets, and red blood cells in a 1:1:1 vs a 1:1:2 ratio and mortality in patients with severe trauma: the PROPPR randomized clinical trial. <i>JAMA</i> 2015;313(5):471&ndash;482. <span class="doi">doi:10.1001/jama.2015.12</span> &middot; PMID 25647203.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
  <li>Shakur H, Roberts I, Bautista R, Caballero J, Coats T, Dewan Y, et al. (CRASH-2 trial collaborators). Effects of tranexamic acid on death, vascular occlusive events, and blood transfusion in trauma patients with significant haemorrhage (CRASH-2). <i>Lancet</i> 2010;376(9734):23&ndash;32. <span class="doi">doi:10.1016/S0140-6736(10)60835-5</span> &middot; PMID 20554319.</li>
  <li>Metcalf RA, Nahirniak S, Guyatt G, Bathla A, White SK, Al-Riyami AZ, et al. Platelet Transfusion: 2025 AABB and ICTMG International Clinical Practice Guidelines. <i>JAMA</i> 2025;334(7):606&ndash;617. <span class="doi">doi:10.1001/jama.2025.7529</span> &middot; PMID 40440268.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-13-hemorragia-critica-transfusion-masiva.html")
    print("HTML:", h); print("PDF :", p)
