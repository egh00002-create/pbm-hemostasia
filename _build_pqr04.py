# -*- coding: utf-8 -*-
"""P-QR-04 - MABL rapido (volumen de Nadler + Gross). Ancla ALG."""
from build_doc import build

META = {
    "comment": "SERIE PBM - P-QR-04 MABL rapido (Nadler + Gross). Ancla ALG.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Tarjeta P-QR-04 - ancla ALG - 2026. "
               "Tarjeta de consulta rapida; sintetiza PBM-11. Formulas clasicas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">P-QR-04</span>
    <span class="badge b-alg">ALG &middot; tarjeta de consulta r&aacute;pida</span>
    <span class="module-tag">Quick-reference &middot; sintetiza PBM-11</span>
  </div>
  <div class="kicker">MABL r&aacute;pido &middot; Volumen de Nadler + f&oacute;rmula de Gross</div>
  <h1 class="title">MABL r&aacute;pido: volumen sangu&iacute;neo (Nadler) + Gross</h1>
  <div class="subtitle">Tarjeta de consulta r&aacute;pida &mdash; una herramienta de planificaci&oacute;n, no un disparador de transfusi&oacute;n</div>
  <div class="tagline">
    2026 &middot; Tarjeta derivada de PBM-11 &middot; CAUSA / SACYL<br>
    <b>Idea:</b> estima cu&aacute;nto puede sangrar el paciente hasta el Hct diana para <b>planificar</b>.
  </div>
</section>
"""

BODY = r"""
<div class="box note avoid-break"><span class="box-h">Paso 1 &middot; Volumen sangu&iacute;neo estimado (Nadler)</span>
  <p class="mono">Var&oacute;n: VSE (L) = 0,3669 &times; talla&sup3; + 0,03219 &times; peso + 0,6041</p>
  <p class="mono">Mujer: VSE (L) = 0,3561 &times; talla&sup3; + 0,03308 &times; peso + 0,1833</p>
  <p>talla en metros, peso en kg. Regla r&aacute;pida: &asymp; 70&nbsp;ml/kg (var&oacute;n), 65&nbsp;ml/kg (mujer).</p>
</div>

<div class="box note avoid-break"><span class="box-h">Paso 2 &middot; P&eacute;rdida admisible (Gross)</span>
  <p class="mono">MABL = VSE &times; (Hct<sub>inicial</sub> &minus; Hct<sub>diana</sub>) / Hct<sub>medio</sub></p>
  <p>Hct<sub>medio</sub> = media de inicial y diana. (V&aacute;lido tambi&eacute;n con Hb en lugar de Hct.)</p>
</div>

<div class="tbl-title">Ejemplo &middot; var&oacute;n 80&nbsp;kg, 1,75&nbsp;m, Hct 42&rarr;28&nbsp;%</div>
<table class="avoid-break">
  <thead><tr><th style="width:30%">Paso</th><th>C&aacute;lculo</th><th style="width:20%">Resultado</th></tr></thead>
  <tbody>
    <tr><td>VSE (Nadler)</td><td>0,3669&times;1,75&sup3; + 0,03219&times;80 + 0,6041</td><td>&asymp; 5,15&nbsp;L</td></tr>
    <tr><td>Hct medio</td><td>(42 + 28) / 2</td><td>35&nbsp;%</td></tr>
    <tr><td><b>MABL (Gross)</b></td><td>5150 &times; (42 &minus; 28) / 35</td><td><b>&asymp; 2060&nbsp;ml</b></td></tr>
  </tbody>
  <caption>Fuentes: Nadler [1], Gross [2]. Asume normovolemia y reposici&oacute;n ideal.</caption>
</table>

<div class="box alert avoid-break"><span class="box-h">No olvidar</span>
  <p>La MABL es una <b>estimaci&oacute;n de planificaci&oacute;n</b>, no un permiso de sangrado ni un disparador autom&aacute;tico. La transfusi&oacute;n
  se decide por el umbral de Hb (P-QR-02), el sangrado activo y la cl&iacute;nica. Si la p&eacute;rdida esperada se acerca a la MABL:
  optimiza Hb previa, activa ahorro de sangre (recuperador, TXA) y planifica disponibilidad.</p>
</div>
"""

REFS = r"""
<h2 class="sec"><span class="num">&middot;</span>Referencias</h2>
<ol class="refs">
  <li>Nadler SB, Hidalgo JH, Bloch T. Prediction of blood volume in normal human adults. <i>Surgery</i> 1962;51(2):224&ndash;232. &middot; PMID 21936146.</li>
  <li>Gross JB. Estimating allowable blood loss: corrected for dilution. <i>Anesthesiology</i> 1983;58(3):277&ndash;280. <span class="doi">doi:10.1097/00000542-198303000-00016</span> &middot; PMID 6829965.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "P-QR-04-mabl-rapido.html")
    print("HTML:", h); print("PDF :", p)
