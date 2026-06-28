# -*- coding: utf-8 -*-
"""PBM-17 - Coagulopatias congenitas y adquiridas en cirugia. Ancla REV."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-17 Coagulopatias congenitas y adquiridas en cirugia. Ancla REV.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-17 - Modulo 5 (eje hemostasia) - ancla REV - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-17</span>
    <span class="badge b-rev">REV &middot; revisi&oacute;n / s&iacute;ntesis</span>
    <span class="module-tag">M&oacute;dulo 5 &middot; Hemostasia clínica y riesgo hemorr&aacute;gico</span>
  </div>
  <div class="kicker">Coagulopat&iacute;as &middot; Cong&eacute;nitas y adquiridas &middot; Manejo perioperatorio</div>
  <h1 class="title">Coagulopat&iacute;as cong&eacute;nitas y adquiridas en cirug&iacute;a</h1>
  <div class="subtitle">De la enfermedad de von Willebrand a la coagulopat&iacute;a del paciente crítico &mdash; reconocer para planificar</div>
  <div class="meta-row">
    <span class="meta-chip">Cong&eacute;nitas: vW, hemofilias, raras</span>
    <span class="meta-chip">Adquiridas: hep&aacute;tica, CID, diluci&oacute;n</span>
    <span class="meta-chip">Plan perioperatorio</span>
    <span class="meta-chip">Cu&aacute;ndo derivar a hematolog&iacute;a</span>
    <span class="meta-chip">Principios de tratamiento</span>
  </div>
  <div class="refbar">
    <b>Ancla de evidencia (referencia vertebral):</b> Mumford AD, Ackroyd S, Alikhan R, et&nbsp;al.
    <i>Guideline for the diagnosis and management of the rare coagulation disorders (UKHCDO / British Committee for Standards in Haematology).</i>
    Br J Haematol 2014;167(3):304&ndash;326. <span class="mono">doi:10.1111/bjh.13058 &middot; PMID&nbsp;25100430</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> las coagulopat&iacute;as <b>cong&eacute;nitas</b> (von Willebrand, hemofilias, d&eacute;ficits raros) exigen
    <b>planificaci&oacute;n con hematolog&iacute;a y tratamiento espec&iacute;fico</b>; las <b>adquiridas</b> (hep&aacute;tica, CID, diluci&oacute;n, f&aacute;rmacos)
    se tratan corrigiendo la causa y el d&eacute;ficit dirigido. Reconocer el tipo es lo que cambia el plan.
  </div>
  <div class="lead">
    <p>Una coagulopat&iacute;a no manejada convierte una cirug&iacute;a rutinaria en una hemorragia. Conviene distinguir las
    <b>cong&eacute;nitas</b> &mdash;conocidas o detectadas en el cribado (PBM-15), que requieren plan espec&iacute;fico&mdash; de las
    <b>adquiridas</b>, frecuentes en el paciente quir&uacute;rgico y crítico.</p>
    <p>Este documento, con ancla <b>REV</b>, ofrece un mapa pr&aacute;ctico de ambas familias y los principios de manejo
    perioperatorio, remitiendo a PBM-18 para los f&aacute;rmacos hemost&aacute;ticos concretos y subrayando cu&aacute;ndo es imprescindible la
    <b>colaboraci&oacute;n con hematolog&iacute;a</b>.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>Coagulopat&iacute;as cong&eacute;nitas</li>
  <li>Coagulopat&iacute;as adquiridas</li>
  <li>Principios de manejo perioperatorio</li>
  <li>Cu&aacute;ndo derivar y planificar con hematolog&iacute;a</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>Coagulopat&iacute;as cong&eacute;nitas</h2>
<p>La m&aacute;s frecuente es la <b>enfermedad de von Willebrand</b>, a menudo infradiagnosticada y con coagulaci&oacute;n b&aacute;sica normal
(de ah&iacute; el valor del cribado por anamnesis, PBM-15). Le siguen las <b>hemofilias A y B</b> (d&eacute;ficit de factor VIII y IX) y
los <b>trastornos raros de la coagulaci&oacute;n</b> (d&eacute;ficits de fibrin&oacute;geno, FII, FV, FVII, FX, FXI, FXIII), cuyo diagn&oacute;stico y
manejo requieren factores espec&iacute;ficos y guía experta [1]. Todas comparten un principio: <b>plan perioperatorio
anticipado</b> con objetivos de factor y cobertura definidos por hematolog&iacute;a.</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>La <b>von Willebrand</b> es la coagulopat&iacute;a cong&eacute;nita m&aacute;s com&uacute;n y suele cursar con TP/TTPa normales [1].</li>
  <li>Las cong&eacute;nitas exigen <b>plan anticipado</b>, tratamiento <b>espec&iacute;fico</b> (factor/desmopresina) y hematolog&iacute;a [1].</li>
  <li>Las adquiridas se tratan <b>corrigiendo la causa</b> y el d&eacute;ficit dirigido, no con &laquo;recetas&raquo; fijas.</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Coagulopat&iacute;as adquiridas</h2>
<p>Son las m&aacute;s frecuentes en el quir&oacute;fano y la UCI: la <b>coagulopat&iacute;a hep&aacute;tica</b> (s&iacute;ntesis deficiente de factores, con un
equilibrio fr&aacute;gil que el TP no refleja bien), la <b>coagulaci&oacute;n intravascular diseminada (CID)</b>, la <b>coagulopat&iacute;a por
diluci&oacute;n y consumo</b> de la hemorragia masiva (PBM-13), la <b>coagulopat&iacute;a traum&aacute;tica</b> y la inducida por <b>f&aacute;rmacos</b>
antitrombóticos (PBM-16). El tratamiento se dirige a la <b>causa</b> y al d&eacute;ficit demostrado, idealmente guiado por
viscoel&aacute;stica (PBM-09) [2].</p>

<h2 class="sec"><span class="num">3.</span>Principios de manejo perioperatorio</h2>
<div class="tbl-title">Tabla 1 &middot; Principios de manejo seg&uacute;n tipo de coagulopat&iacute;a</div>
<table class="avoid-break">
  <thead><tr><th style="width:26%">Tipo</th><th>Principio de manejo</th></tr></thead>
  <tbody>
    <tr><td><b>Von Willebrand</b></td><td>Desmopresina (en tipos respondedores) o concentrado de FvW/FVIII; plan con hematolog&iacute;a [1].</td></tr>
    <tr><td><b>Hemofilia A/B</b></td><td>Reposici&oacute;n del factor deficitario a objetivos seg&uacute;n cirug&iacute;a; evitar antiagregantes [1].</td></tr>
    <tr><td><b>D&eacute;ficits raros</b></td><td>Factor espec&iacute;fico o plasma seg&uacute;n disponibilidad; guía experta [1].</td></tr>
    <tr><td><b>Coagulopat&iacute;a hep&aacute;tica</b></td><td>Corregir lo corregible; no transfundir plasma por un INR alterado sin sangrado (PBM-02) [2].</td></tr>
    <tr><td><b>CID</b></td><td>Tratar la causa; soporte con componentes seg&uacute;n sangrado y par&aacute;metros [2].</td></tr>
    <tr><td><b>Diluci&oacute;n / masiva</b></td><td>Protocolo de transfusi&oacute;n masiva, fibrin&oacute;geno, calcio, normotermia (PBM-13) [2].</td></tr>
  </tbody>
  <caption>S&iacute;ntesis de la gu&iacute;a de trastornos raros [1] y de la gu&iacute;a ESAIC [2]. La correcci&oacute;n se dirige a la causa y al d&eacute;ficit demostrado.</caption>
</table>

<h2 class="sec"><span class="num">4.</span>Cu&aacute;ndo derivar y planificar con hematolog&iacute;a</h2>
<p>Toda <b>coagulopat&iacute;a cong&eacute;nita conocida o sospechada</b> (cribado positivo, historia familiar) debe planificarse <b>con
antelaci&oacute;n</b> junto a hematolog&iacute;a: definir objetivos de factor, profilaxis, disponibilidad de concentrados y plan de
rescate. En las adquiridas, la colaboraci&oacute;n es &uacute;til ante CID, hepatopat&iacute;a avanzada o hemorragia que no responde. La regla
de oro es <b>anticipar</b>: el peor momento para descubrir una coagulopat&iacute;a es durante la hemorragia [1,2].</p>

<h2 class="sec"><span class="num">5.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> distinguir coagulopat&iacute;a cong&eacute;nita de adquirida cambia el plan: las cong&eacute;nitas exigen
anticipaci&oacute;n, tratamiento espec&iacute;fico y hematolog&iacute;a; las adquiridas, corregir la causa y el d&eacute;ficit dirigido (mejor guiado
por viscoel&aacute;stica). No tratar &laquo;n&uacute;meros&raquo; sin sangrado.</p>
<p>Conecta con <b>PBM-15</b> (cribado), <b>PBM-09</b> (viscoel&aacute;stica), <b>PBM-13</b> (coagulopat&iacute;a de la hemorragia masiva) y
<b>PBM-18</b> (f&aacute;rmacos hemost&aacute;ticos espec&iacute;ficos).</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Reconoce el tipo: cong&eacute;nita &rarr; plan anticipado con hematolog&iacute;a y factor espec&iacute;fico; adquirida &rarr; corrige la causa y
  el d&eacute;ficit demostrado &mdash;sin transfundir por una analítica sin sangrado&mdash;.</p>
</div>

<h2 class="sec"><span class="num">6.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>REV</b> apoyado en la gu&iacute;a de trastornos raros de la coagulaci&oacute;n [1], la gu&iacute;a ESAIC [2] y la gu&iacute;a BSH de
plasma/crioprecipitado [3], verificados contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Los principios de manejo
(plan anticipado en cong&eacute;nitas, correcci&oacute;n dirigida en adquiridas, no transfundir plasma por INR sin sangrado) proceden de
estas fuentes.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">7.</span>Referencias</h2>
<ol class="refs">
  <li>Mumford AD, Ackroyd S, Alikhan R, Bowles L, Chowdary P, Grainger J, et al. Guideline for the diagnosis and management of the rare coagulation disorders: a United Kingdom Haemophilia Centre Doctors' Organization guideline on behalf of the British Committee for Standards in Haematology. <i>Br J Haematol</i> 2014;167(3):304&ndash;326. <span class="doi">doi:10.1111/bjh.13058</span> &middot; PMID 25100430.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
  <li>Green L, Bolton-Maggs P, Beattie C, Cardigan R, Kallis Y, Stanworth SJ, et al. British Society of Haematology Guidelines on the spectrum of fresh frozen plasma and cryoprecipitate products. <i>Br J Haematol</i> 2018;181(1):54&ndash;67. <span class="doi">doi:10.1111/bjh.15167</span> &middot; PMID 29527654.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-17-coagulopatias.html")
    print("HTML:", h); print("PDF :", p)
