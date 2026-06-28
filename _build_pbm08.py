# -*- coding: utf-8 -*-
"""PBM-08 - Antifibrinoliticos: acido tranexamico (CRASH-2/3, WOMAN, ATACAS). Ancla ECA."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-08 Antifibrinoliticos: acido tranexamico. Ancla ECA. Documento nucleo.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-08 - Modulo 3 (Pilar 2) - ancla ECA - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de ensayos pivotales indexados verificados contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-08</span>
    <span class="badge b-eca">ECA &middot; ensayo pivotal</span>
    <span class="module-tag">M&oacute;dulo 3 &middot; Pilar 2: minimizar la p&eacute;rdida sangu&iacute;nea</span>
  </div>
  <div class="kicker">&Aacute;cido tranex&aacute;mico &middot; CRASH-2/3 &middot; WOMAN &middot; ATACAS</div>
  <h1 class="title">Antifibrinol&iacute;ticos: &aacute;cido tranex&aacute;mico</h1>
  <div class="subtitle">Barato, seguro y eficaz para reducir el sangrado &mdash; con un mensaje claro: cuanto antes, mejor</div>
  <div class="meta-row">
    <span class="meta-chip">C&oacute;mo act&uacute;a</span>
    <span class="meta-chip">Trauma: CRASH-2</span>
    <span class="meta-chip">Hemorragia posparto: WOMAN</span>
    <span class="meta-chip">TCE: CRASH-3</span>
    <span class="meta-chip">Cirug&iacute;a: ATACAS</span>
    <span class="meta-chip">Dosis por escenario</span>
  </div>
  <div class="refbar guiabar">
    <b>Ancla de evidencia (referencia vertebral):</b> CRASH-2 trial collaborators (Shakur H, Roberts I, et&nbsp;al.).
    <i>Effects of tranexamic acid on death, vascular occlusive events, and blood transfusion in trauma patients with significant haemorrhage (CRASH-2).</i>
    Lancet 2010;376(9734):23&ndash;32. <span class="mono">doi:10.1016/S0140-6736(10)60835-5 &middot; PMID&nbsp;20554319</span>.
  </div>
  <div class="tagline">
    2026 &middot; 4 ensayos pivotales (PubMed) + actualizaci&oacute;n NICE NG24 2026 &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> el &aacute;cido tranex&aacute;mico (TXA) reduce el sangrado y la <b>muerte por hemorragia</b> en el trauma y el
    posparto, y disminuye la transfusi&oacute;n en cirug&iacute;a, con <b>bajo riesgo trombótico</b>. El beneficio es <b>tiempo-dependiente</b>
    (m&aacute;ximo en las primeras horas) y no es universal: en el TCE grave establecido el efecto es limitado.
  </div>
  <div class="lead">
    <p>El &aacute;cido tranex&aacute;mico es probablemente la intervenci&oacute;n farmacol&oacute;gica de PBM con mejor relaci&oacute;n
    beneficio-coste-riesgo. Inhibe la fibrin&oacute;lisis (bloquea la conversi&oacute;n de plasmin&oacute;geno en plasmina) y as&iacute;
    <b>estabiliza el co&aacute;gulo</b> ya formado.</p>
    <p>Este documento n&uacute;cleo, con ancla <b>ECA</b>, resume la evidencia pivotal por escenario &mdash;trauma, posparto, traumatismo
    craneoencef&aacute;lico y cirug&iacute;a&mdash; y la traduce en dosis pr&aacute;cticas, con honestidad sobre d&oacute;nde el beneficio es s&oacute;lido y d&oacute;nde
    es limitado.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>C&oacute;mo act&uacute;a y por qu&eacute; importa el tiempo</li>
  <li>Trauma: CRASH-2</li>
  <li>Hemorragia posparto: WOMAN</li>
  <li>Traumatismo craneoencef&aacute;lico: CRASH-3</li>
  <li>Cirug&iacute;a cardíaca: ATACAS</li>
  <li>Dosis por escenario y seguridad</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>C&oacute;mo act&uacute;a y por qu&eacute; importa el tiempo</h2>
<p>El TXA es un an&aacute;logo de la lisina que bloquea los sitios de uni&oacute;n del plasmin&oacute;geno a la fibrina, inhibiendo la
<b>fibrin&oacute;lisis</b>. As&iacute; impide la disoluci&oacute;n prematura del co&aacute;gulo. Como act&uacute;a sobre un co&aacute;gulo que debe formarse pronto,
su eficacia es <b>tiempo-dependiente</b>: cuanto antes se administra tras el inicio del sangrado, mayor es el beneficio
[1,2].</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>El TXA reduce la <b>muerte por hemorragia</b> en trauma y posparto, y la <b>transfusi&oacute;n</b> en cirug&iacute;a [1,2,4].</li>
  <li>El beneficio cae con el tiempo: <b>administrar precozmente</b> (idealmente &lt; 3&nbsp;h) [1,2].</li>
  <li>El riesgo de eventos trombóticos fue <b>bajo</b> en los grandes ensayos; en cirug&iacute;a cardíaca, m&aacute;s convulsiones a dosis altas [4].</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Trauma: CRASH-2</h2>
<p><b>CRASH-2</b> aleatoriz&oacute; a 20.211 pacientes con trauma y hemorragia (o riesgo) a TXA (1&nbsp;g en 10&nbsp;min + 1&nbsp;g en
8&nbsp;h) o placebo en las primeras 8&nbsp;h. El TXA redujo la <b>mortalidad por cualquier causa</b> (14,5&nbsp;% vs 16,0&nbsp;%; RR
0,91; IC95&nbsp;% 0,85&ndash;0,97) y la <b>muerte por hemorragia</b> (4,9&nbsp;% vs 5,7&nbsp;%; RR 0,85; IC95&nbsp;% 0,76&ndash;0,96), sin aumento
de eventos vasculares oclusivos [1]. An&aacute;lisis posteriores mostraron que el beneficio es mayor cuanto m&aacute;s precoz.</p>

<h2 class="sec"><span class="num">3.</span>Hemorragia posparto: WOMAN</h2>
<p><b>WOMAN</b> aleatoriz&oacute; a 20.060 mujeres con hemorragia posparto a TXA (1&nbsp;g) o placebo. Redujo la <b>muerte por
hemorragia</b> (1,5&nbsp;% vs 1,9&nbsp;%; RR 0,81; IC95&nbsp;% 0,65&ndash;1,00), efecto mayor cuando se administr&oacute; <b>en las 3&nbsp;h
siguientes</b> al parto (RR 0,69; IC95&nbsp;% 0,52&ndash;0,91). <b>No</b> redujo la histerectomía (la decisi&oacute;n sol&iacute;a tomarse al
incluir) ni aument&oacute; los eventos tromboembólicos [2].</p>

<h2 class="sec"><span class="num">4.</span>Traumatismo craneoencef&aacute;lico: CRASH-3</h2>
<p><b>CRASH-3</b> (12.737 pacientes con TCE) no redujo la mortalidad relacionada con la lesi&oacute;n craneal en el conjunto, pero
s&iacute; en el subgrupo de TCE <b>leve-moderado</b> (RR 0,78; IC95&nbsp;% 0,64&ndash;0,95), sin se&ntilde;al clara en el TCE grave [3]. Es la
pieza de honestidad: el TXA <b>no es universalmente eficaz</b> &mdash;en la lesi&oacute;n cerebral grave establecida el efecto es
limitado&mdash;, aunque es seguro y &uacute;til administrado pronto en TCE no grave.</p>

<h2 class="sec"><span class="num">5.</span>Cirug&iacute;a cardíaca: ATACAS</h2>
<p><b>ATACAS</b> (4.631 pacientes de cirug&iacute;a coronaria) mostr&oacute; que el TXA <b>reduce la hemorragia y la transfusi&oacute;n</b> (4.331
vs 7.994 unidades transfundidas; reoperaci&oacute;n por sangrado 1,4&nbsp;% vs 2,8&nbsp;%) sin aumentar muerte ni complicaciones
trombóticas a 30&nbsp;d&iacute;as; el precio fue un ligero aumento de <b>convulsiones</b> (0,7&nbsp;% vs 0,1&nbsp;%) [4]. Confirma el
papel del TXA como ahorrador de sangre en cirug&iacute;a.</p>

<h2 class="sec"><span class="num">6.</span>Dosis por escenario y seguridad</h2>
<div class="tbl-title">Tabla 1 &middot; &Aacute;cido tranex&aacute;mico: escenario, pauta y evidencia</div>
<table class="avoid-break">
  <thead><tr><th style="width:22%">Escenario</th><th>Pauta del ensayo</th><th>Efecto clave</th><th style="width:12%">Ensayo</th></tr></thead>
  <tbody>
    <tr><td><b>Trauma con hemorragia</b></td><td>1&nbsp;g en 10&nbsp;min + 1&nbsp;g/8&nbsp;h, &lt; 3&nbsp;h</td><td>&darr; mortalidad (RR 0,91) y muerte por sangrado</td><td class="c">CRASH-2 [1]</td></tr>
    <tr><td><b>Hemorragia posparto</b></td><td>1&nbsp;g IV (repetible)</td><td>&darr; muerte por hemorragia (RR 0,81)</td><td class="c">WOMAN [2]</td></tr>
    <tr><td><b>TCE leve-moderado</b></td><td>1&nbsp;g + 1&nbsp;g/8&nbsp;h, &lt; 3&nbsp;h</td><td>&darr; muerte por TCE en leve-moderado; no en grave</td><td class="c">CRASH-3 [3]</td></tr>
    <tr><td><b>Cirug&iacute;a (cardíaca)</b></td><td>Bolo/infusi&oacute;n perioperatoria</td><td>&darr; transfusi&oacute;n y reoperaci&oacute;n; &uarr; convulsiones</td><td class="c">ATACAS [4]</td></tr>
  </tbody>
  <caption>Pautas tal como se administraron en los ensayos. La administraci&oacute;n <b>precoz</b> es el factor com&uacute;n de eficacia. Las dosis exactas por procedimiento se condensan en la tarjeta P-QR-03.</caption>
</table>

<div class="box rev avoid-break"><span class="box-h">Actualizaci&oacute;n NICE NG24 (febrero 2026)</span>
  <p>NICE actualiz&oacute; su gu&iacute;a de transfusi&oacute;n (NG24) y <b>simplific&oacute; la indicaci&oacute;n</b> de TXA en cirug&iacute;a: deja de exigir una
  <b>estimaci&oacute;n previa de la p&eacute;rdida sangu&iacute;nea</b> y recomienda ofrecerlo en <b>cualquier procedimiento con riesgo
  hemorr&aacute;gico</b>. Para cirug&iacute;a fuera de quir&oacute;fano (radiolog&iacute;a intervencionista, urgencias), ofrecer si la p&eacute;rdida
  prevista supera 500&nbsp;ml en adultos, y considerarlo en ni&ntilde;os de 1&ndash;15&nbsp;a&ntilde;os si supera el 10&nbsp;% del volumen
  sangu&iacute;neo [5]. Va en la l&iacute;nea de los ensayos: <b>bajo umbral para usar TXA, y pronto</b>.</p>
</div>

<h2 class="sec"><span class="num">7.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> el &aacute;cido tranex&aacute;mico reduce la muerte por hemorragia en trauma y posparto y la
transfusi&oacute;n en cirug&iacute;a, con bajo riesgo trombótico y administrado <b>cuanto antes</b>; no es universalmente eficaz (TCE
grave) y a dosis altas en cirug&iacute;a cardíaca aumenta levemente las convulsiones. Es una intervenci&oacute;n de alto valor del
pilar 2.</p>
<p>Conecta con <b>PBM-07</b> (fibrin&oacute;lisis), <b>PBM-13</b> (hemorragia masiva, donde el TXA precoz forma parte del protocolo)
y con la serie hermana de <b>traumatolog&iacute;a</b>. Dosis pr&aacute;cticas en <b>P-QR-03</b>.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Da tranex&aacute;mico pronto en el sangrado de trauma, posparto y cirug&iacute;a &mdash;reduce muerte por hemorragia y transfusi&oacute;n con
  bajo riesgo&mdash;; en el TCE grave establecido su beneficio es limitado.</p>
</div>

<h2 class="sec"><span class="num">8.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento de tipo <b>ECA</b> basado en cuatro ensayos pivotales verificados contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o,
DOI/PMID). Las cifras &mdash;CRASH-2 RR 0,91 mortalidad y 0,85 muerte por sangrado [1]; WOMAN RR 0,81 (0,69 si &lt; 3&nbsp;h) [2];
CRASH-3 RR 0,78 en TCE leve-moderado [3]; ATACAS reducci&oacute;n de transfusi&oacute;n y aumento de convulsiones [4]&mdash; proceden
directamente de las fuentes. La <b>actualizaci&oacute;n NICE NG24 (2026)</b> [5] se ha verificado contra la web oficial de NICE
(gu&iacute;a, no indexada en PubMed). Se declara expl&iacute;citamente la <b>limitaci&oacute;n</b> del TXA en el TCE grave y el matiz de las
convulsiones en cirug&iacute;a cardíaca.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">9.</span>Referencias</h2>
<ol class="refs">
  <li>Shakur H, Roberts I, Bautista R, Caballero J, Coats T, Dewan Y, et al. (CRASH-2 trial collaborators). Effects of tranexamic acid on death, vascular occlusive events, and blood transfusion in trauma patients with significant haemorrhage (CRASH-2): a randomised, placebo-controlled trial. <i>Lancet</i> 2010;376(9734):23&ndash;32. <span class="doi">doi:10.1016/S0140-6736(10)60835-5</span> &middot; PMID 20554319.</li>
  <li>WOMAN Trial Collaborators. Effect of early tranexamic acid administration on mortality, hysterectomy, and other morbidities in women with post-partum haemorrhage (WOMAN): an international, randomised, double-blind, placebo-controlled trial. <i>Lancet</i> 2017;389(10084):2105&ndash;2116. <span class="doi">doi:10.1016/S0140-6736(17)30638-4</span> &middot; PMID 28456509.</li>
  <li>CRASH-3 trial collaborators. Effects of tranexamic acid on death, disability, vascular occlusive events and other morbidities in patients with acute traumatic brain injury (CRASH-3): a randomised, placebo-controlled trial. <i>Lancet</i> 2019;394(10210):1713&ndash;1723. <span class="doi">doi:10.1016/S0140-6736(19)32233-0</span> &middot; PMID 31623894.</li>
  <li>Myles PS, Smith JA, Forbes A, Silbert B, Jayarajah M, Painter T, et al. Tranexamic Acid in Patients Undergoing Coronary-Artery Surgery. <i>N Engl J Med</i> 2017;376(2):136&ndash;148. <span class="doi">doi:10.1056/NEJMoa1606424</span> &middot; PMID 27774838.</li>
  <li>National Institute for Health and Care Excellence (NICE). Blood transfusion (NG24): tranexamic acid &mdash; actualizaci&oacute;n. Londres: NICE; 26 feb 2026. Disponible en: <span class="mono">https://www.nice.org.uk/guidance/ng24</span>. <i>(Gu&iacute;a verificada en la web oficial de NICE; no indexada en PubMed.)</i></li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-08-acido-tranexamico.html")
    print("HTML:", h); print("PDF :", p)
