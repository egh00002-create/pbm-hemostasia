# -*- coding: utf-8 -*-
"""PBM-09 - Pruebas viscoelasticas (ROTEM/TEG) y algoritmos guiados. Ancla META."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-09 Pruebas viscoelasticas (ROTEM/TEG). Ancla META.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-09 - Modulo 3 (Pilar 2) - ancla META - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-09</span>
    <span class="badge b-meta">META &middot; revisi&oacute;n sistem&aacute;tica / metaan&aacute;lisis</span>
    <span class="module-tag">M&oacute;dulo 3 &middot; Pilar 2: minimizar la p&eacute;rdida sangu&iacute;nea</span>
  </div>
  <div class="kicker">Viscoel&aacute;stica &middot; ROTEM / TEG &middot; Algoritmos guiados por componentes</div>
  <h1 class="title">Pruebas viscoel&aacute;sticas (ROTEM/TEG) y algoritmos guiados</h1>
  <div class="subtitle">Ver la coagulaci&oacute;n en tiempo real para transfundir lo que falta &mdash; con evidencia heterog&eacute;nea</div>
  <div class="meta-row">
    <span class="meta-chip">Qu&eacute; miden y c&oacute;mo se leen</span>
    <span class="meta-chip">Del par&aacute;metro al componente</span>
    <span class="meta-chip">Algoritmos guiados</span>
    <span class="meta-chip">Qu&eacute; dice el metaan&aacute;lisis</span>
    <span class="meta-chip">L&iacute;mites y heterogeneidad</span>
  </div>
  <div class="refbar">
    <b>Ancla de evidencia (referencia vertebral):</b> Wikkels&oslash; A, Wetterslev J, M&oslash;ller AM, Afshari A.
    <i>Thromboelastography (TEG) or thromboelastometry (ROTEM) to monitor haemostatic treatment versus usual care in adults or children with bleeding.</i>
    Cochrane Database Syst Rev 2016;2016(8):CD007871. <span class="mono">doi:10.1002/14651858.CD007871.pub3 &middot; PMID&nbsp;27552162</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> la viscoel&aacute;stica (ROTEM/TEG) muestra la <b>din&aacute;mica completa</b> del co&aacute;gulo a pie de quir&oacute;fano y
    permite <b>algoritmos guiados</b> que reducen el uso de hemoderivados. La evidencia es <b>favorable pero de baja certeza
    y heterog&eacute;nea</b>, sobre todo en cirug&iacute;a cardíaca; no sustituye al juicio cl&iacute;nico ni a la hemostasia b&aacute;sica.
  </div>
  <div class="lead">
    <p>Las pruebas convencionales (TP, TTPa) se dise&ntilde;aron para diagnosticar coagulopat&iacute;as, no para guiar la transfusi&oacute;n en
    una hemorragia activa: tardan y no informan de la fuerza ni de la lisis del co&aacute;gulo. Las pruebas <b>viscoel&aacute;sticas</b>
    (ROTEM, TEG) miden en tiempo real la formaci&oacute;n, la firmeza y la lisis del co&aacute;gulo en sangre total.</p>
    <p>Este documento, con ancla <b>META</b>, explica c&oacute;mo se leen, c&oacute;mo se traducen en decisiones por componente y qu&eacute; dice
    la evidencia &mdash;con su heterogeneidad&mdash; sobre los algoritmos guiados [1].</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>Qu&eacute; miden ROTEM/TEG</li>
  <li>Del par&aacute;metro al componente</li>
  <li>Algoritmos guiados por viscoel&aacute;stica</li>
  <li>Qu&eacute; dice el metaan&aacute;lisis (y su heterogeneidad)</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>Qu&eacute; miden ROTEM/TEG</h2>
<p>La viscoel&aacute;stica registra, sobre sangre total, la <b>cin&eacute;tica completa</b> del co&aacute;gulo: tiempo hasta el inicio
(formaci&oacute;n de trombina/factores), velocidad de formaci&oacute;n (fibrin&oacute;geno y plaquetas), <b>firmeza m&aacute;xima</b> (contribuci&oacute;n
de plaquetas y fibrin&oacute;geno) y <b>lisis</b> (fibrin&oacute;lisis). Frente a TP/TTPa, aporta una imagen <b>funcional y r&aacute;pida</b>
&uacute;til en la hemorragia activa [1].</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>Mide lo que TP/TTPa no ven: <b>firmeza</b> del co&aacute;gulo y <b>fibrin&oacute;lisis</b>, en tiempo real [1].</li>
  <li>Permite <b>transfundir dirigido</b>: dar el componente deficitario en vez de paquetes fijos.</li>
  <li>La evidencia de beneficio existe pero es de <b>baja certeza</b> y proviene sobre todo de cirug&iacute;a cardíaca [1].</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Del par&aacute;metro al componente</h2>
<div class="tbl-title">Tabla 1 &middot; Lectura orientativa: hallazgo &rarr; d&eacute;ficit &rarr; acci&oacute;n</div>
<table class="avoid-break">
  <thead><tr><th>Hallazgo viscoel&aacute;stico</th><th>D&eacute;ficit sugerido</th><th>Acci&oacute;n dirigida</th></tr></thead>
  <tbody>
    <tr><td>Tiempo de inicio prolongado</td><td>Factores de coagulaci&oacute;n / efecto anticoagulante</td><td>Plasma o concentrado de complejo protrombínico</td></tr>
    <tr><td>Firmeza baja con d&eacute;ficit de la v&iacute;a del fibrin&oacute;geno</td><td>Hipofibrinogenemia</td><td>Fibrin&oacute;geno o crioprecipitado</td></tr>
    <tr><td>Firmeza baja con v&iacute;a del fibrin&oacute;geno normal</td><td>Trombocitopenia / disfunci&oacute;n plaquetaria</td><td>Plaquetas</td></tr>
    <tr><td>Lisis acelerada</td><td>Hiperfibrin&oacute;lisis</td><td>&Aacute;cido tranex&aacute;mico (&rarr; PBM-08)</td></tr>
  </tbody>
  <caption>Esquema docente orientativo coherente con las guías [2,3]; los dinteles concretos dependen del dispositivo (ROTEM/TEG) y del protocolo local.</caption>
</table>

<h2 class="sec"><span class="num">3.</span>Algoritmos guiados por viscoel&aacute;stica</h2>
<p>Integrada en un <b>algoritmo</b>, la viscoel&aacute;stica convierte el manejo de la hemorragia en una secuencia de decisiones
dirigidas: primero descartar/ tratar la hiperfibrin&oacute;lisis (TXA), reponer <b>fibrin&oacute;geno</b>, luego <b>plaquetas</b> y
factores seg&uacute;n los trazados. Las guías europeas (ESAIC, EACTS) recomiendan algoritmos guiados por viscoel&aacute;stica en la
hemorragia perioperatoria, especialmente en cirug&iacute;a cardíaca [2,3].</p>

<h2 class="sec"><span class="num">4.</span>Qu&eacute; dice el metaan&aacute;lisis (y su heterogeneidad)</h2>
<p>La revisi&oacute;n Cochrane (17 ensayos, 1.493 participantes, mayor&iacute;a cirug&iacute;a cardíaca) encontr&oacute; que los algoritmos guiados por
TEG/ROTEM <b>reducen la proporci&oacute;n de pacientes transfundidos</b> con hematíes (RR 0,86), plasma (RR 0,57) y plaquetas
(RR 0,73), con una se&ntilde;al de menor mortalidad (RR 0,52) pero basada en pocos eventos [1]. La <b>certeza es baja</b>: alto
riesgo de sesgo, heterogeneidad y predominio de la cirug&iacute;a cardíaca. Es la pieza de honestidad: la viscoel&aacute;stica
<b>probablemente ahorra hemoderivados</b>, pero el impacto en desenlaces duros y su validez fuera de cirug&iacute;a cardíaca
requieren m&aacute;s evidencia [1].</p>

<div class="box rev avoid-break"><span class="box-h">Honestidad sobre la evidencia</span>
  <p>El beneficio m&aacute;s consistente es la <b>reducci&oacute;n del uso de hemoderivados</b>; la se&ntilde;al de mortalidad es fr&aacute;gil (pocos
  eventos, baja certeza) y la evidencia procede sobre todo de cirug&iacute;a cardíaca. La viscoel&aacute;stica es una herramienta
  &uacute;til, no un or&aacute;culo: complementa &mdash;no sustituye&mdash; la hemostasia b&aacute;sica y el juicio cl&iacute;nico [1].</p>
</div>

<h2 class="sec"><span class="num">5.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> la viscoel&aacute;stica permite un manejo <b>dirigido por componentes</b> de la hemorragia
y, dentro de algoritmos, reduce el uso de hemoderivados; la evidencia es favorable pero de baja certeza y heterog&eacute;nea, sobre
todo derivada de cirug&iacute;a cardíaca. &Uacute;til como guía, no como sustituto del juicio.</p>
<p>Conecta con <b>PBM-07</b> (fisiolog&iacute;a), <b>PBM-08</b> (TXA ante hiperfibrin&oacute;lisis), <b>PBM-02/18</b> (componentes y
fibrin&oacute;geno) y <b>PBM-13</b> (hemorragia masiva guiada).</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>ROTEM/TEG muestran la coagulaci&oacute;n en tiempo real y, en algoritmo, ahorran hemoderivados (TXA &rarr; fibrin&oacute;geno &rarr;
  plaquetas/factores) &mdash;con beneficio probable pero de baja certeza&mdash;.</p>
</div>

<h2 class="sec"><span class="num">6.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento <b>META</b> anclado en la revisi&oacute;n Cochrane de Wikkels&oslash; et&nbsp;al. [1] y respaldado por las guías ESAIC [2] y
EACTS 2024 [3], verificados contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Las cifras (RR 0,86 hematíes; 0,57
plasma; 0,73 plaquetas; 0,52 mortalidad) y la <b>baja certeza</b> con heterogeneidad proceden directamente de la fuente [1].</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">7.</span>Referencias</h2>
<ol class="refs">
  <li>Wikkels&oslash; A, Wetterslev J, M&oslash;ller AM, Afshari A. Thromboelastography (TEG) or thromboelastometry (ROTEM) to monitor haemostatic treatment versus usual care in adults or children with bleeding. <i>Cochrane Database Syst Rev</i> 2016;2016(8):CD007871. <span class="doi">doi:10.1002/14651858.CD007871.pub3</span> &middot; PMID 27552162.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
  <li>Casselman FPA, Lance MD, Ahmed A, Ascari A, Blanco-Morillo J, Bolliger D, et al. 2024 EACTS/EACTAIC Guidelines on patient blood management in adult cardiac surgery in collaboration with EBCP. <i>Eur J Cardiothorac Surg</i> 2025;67(5):ezae352. <span class="doi">doi:10.1093/ejcts/ezae352</span> &middot; PMID 39385500.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-09-viscoelastica-rotem-teg.html")
    print("HTML:", h); print("PDF :", p)
