# -*- coding: utf-8 -*-
"""P-QR-03 - Acido tranexamico: dosis por escenario. Ancla ALG."""
from build_doc import build

META = {
    "comment": "SERIE PBM - P-QR-03 Acido tranexamico: dosis por escenario. Ancla ALG.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Tarjeta P-QR-03 - ancla ALG - 2026. "
               "Tarjeta de consulta rapida; sintetiza PBM-08. Pautas de los ensayos pivotales verificados contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">P-QR-03</span>
    <span class="badge b-alg">ALG &middot; tarjeta de consulta r&aacute;pida</span>
    <span class="module-tag">Quick-reference &middot; sintetiza PBM-08</span>
  </div>
  <div class="kicker">&Aacute;cido tranex&aacute;mico: dosis por escenario</div>
  <h1 class="title">&Aacute;cido tranex&aacute;mico: dosis por escenario</h1>
  <div class="subtitle">Tarjeta de consulta r&aacute;pida &mdash; el factor com&uacute;n es administrarlo pronto</div>
  <div class="tagline">
    2026 &middot; Tarjeta derivada de PBM-08 &middot; CAUSA / SACYL<br>
    <b>Idea:</b> el TXA reduce muerte por hemorragia (trauma, posparto) y transfusi&oacute;n (cirug&iacute;a); <b>cuanto antes, mejor</b>.
  </div>
</section>
"""

BODY = r"""
<div class="tbl-title">Pautas por escenario (tal como en los ensayos)</div>
<table class="avoid-break">
  <thead><tr><th style="width:22%">Escenario</th><th>Pauta</th><th>Efecto / matiz</th><th style="width:12%">Ensayo</th></tr></thead>
  <tbody>
    <tr><td><b>Trauma con hemorragia</b></td><td>1&nbsp;g IV en 10&nbsp;min + 1&nbsp;g en 8&nbsp;h; iniciar &lt; 3&nbsp;h de la lesi&oacute;n</td><td>&darr; mortalidad (RR 0,91); m&aacute;ximo si precoz</td><td class="c">CRASH-2 [1]</td></tr>
    <tr><td><b>Hemorragia posparto</b></td><td>1&nbsp;g IV; repetible a los 30&nbsp;min si persiste</td><td>&darr; muerte por hemorragia (RR 0,81; 0,69 si &lt; 3&nbsp;h)</td><td class="c">WOMAN [2]</td></tr>
    <tr><td><b>TCE leve-moderado</b></td><td>1&nbsp;g + 1&nbsp;g/8&nbsp;h; &lt; 3&nbsp;h</td><td>&darr; muerte por TCE en leve-moderado; <b>no</b> en grave</td><td class="c">CRASH-3 [3]</td></tr>
    <tr><td><b>Cirug&iacute;a (cardíaca/mayor)</b></td><td>Bolo + infusi&oacute;n perioperatoria</td><td>&darr; transfusi&oacute;n y reoperaci&oacute;n; &uarr; convulsiones a dosis altas</td><td class="c">ATACAS [4]</td></tr>
  </tbody>
  <caption>Pautas de los ensayos pivotales. Ajustar a protocolo local y ficha t&eacute;cnica; vigilar dosis altas en insuficiencia renal y cirug&iacute;a cardíaca (convulsiones).</caption>
</table>

<div class="box pearl avoid-break"><span class="box-h">Regla de oro</span>
  <p>En el sangrado de trauma y posparto, el TXA salva vidas <b>solo si se da pronto</b> (idealmente &lt; 3&nbsp;h). No lo
  retrases esperando pruebas.</p>
</div>

<div class="box alert avoid-break"><span class="box-h">D&oacute;nde NO esperar gran beneficio</span>
  <p>En el <b>TCE grave establecido</b> el efecto es limitado [3]. A <b>dosis altas en cirug&iacute;a cardíaca</b>, vigilar
  convulsiones [4].</p>
</div>

<div class="box rev avoid-break"><span class="box-h">Actualizaci&oacute;n NICE NG24 (2026)</span>
  <p>NICE ya <b>no exige estimar la p&eacute;rdida sangu&iacute;nea</b>: ofrece TXA en <b>cualquier procedimiento con riesgo
  hemorr&aacute;gico</b>. Fuera de quir&oacute;fano (radiolog&iacute;a intervencionista, urgencias), si la p&eacute;rdida prevista supera 500&nbsp;ml
  (adultos) o el 10&nbsp;% del volumen sangu&iacute;neo (ni&ntilde;os 1&ndash;15&nbsp;a&ntilde;os) [5].</p>
</div>
"""

REFS = r"""
<h2 class="sec"><span class="num">&middot;</span>Referencias</h2>
<ol class="refs">
  <li>CRASH-2 trial collaborators (Shakur H, Roberts I, et al.). Effects of tranexamic acid... (CRASH-2). <i>Lancet</i> 2010;376(9734):23&ndash;32. <span class="doi">doi:10.1016/S0140-6736(10)60835-5</span> &middot; PMID 20554319.</li>
  <li>WOMAN Trial Collaborators. Effect of early tranexamic acid administration... (WOMAN). <i>Lancet</i> 2017;389(10084):2105&ndash;2116. <span class="doi">doi:10.1016/S0140-6736(17)30638-4</span> &middot; PMID 28456509.</li>
  <li>CRASH-3 trial collaborators. Effects of tranexamic acid... traumatic brain injury (CRASH-3). <i>Lancet</i> 2019;394(10210):1713&ndash;1723. <span class="doi">doi:10.1016/S0140-6736(19)32233-0</span> &middot; PMID 31623894.</li>
  <li>Myles PS, Smith JA, Forbes A, et al. Tranexamic Acid in Patients Undergoing Coronary-Artery Surgery. <i>N Engl J Med</i> 2017;376(2):136&ndash;148. <span class="doi">doi:10.1056/NEJMoa1606424</span> &middot; PMID 27774838.</li>
  <li>National Institute for Health and Care Excellence (NICE). Blood transfusion (NG24): tranexamic acid &mdash; actualizaci&oacute;n. Londres: NICE; 26 feb 2026. Disponible en: <span class="mono">https://www.nice.org.uk/guidance/ng24</span>. <i>(Gu&iacute;a verificada en la web oficial de NICE; no indexada en PubMed.)</i></li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "P-QR-03-tranexamico-dosis.html")
    print("HTML:", h); print("PDF :", p)
