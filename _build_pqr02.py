# -*- coding: utf-8 -*-
"""P-QR-02 - Umbrales de transfusion por componente. Ancla ALG."""
from build_doc import build

META = {
    "comment": "SERIE PBM - P-QR-02 Umbrales de transfusion por componente. Ancla ALG.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Tarjeta P-QR-02 - ancla ALG - 2026. "
               "Tarjeta de consulta rapida; sintetiza PBM-02 y PBM-12. Umbrales orientativos verificados contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">P-QR-02</span>
    <span class="badge b-alg">ALG &middot; tarjeta de consulta r&aacute;pida</span>
    <span class="module-tag">Quick-reference &middot; sintetiza PBM-02 y PBM-12</span>
  </div>
  <div class="kicker">Umbrales de transfusi&oacute;n por componente</div>
  <h1 class="title">Umbrales de transfusi&oacute;n por componente</h1>
  <div class="subtitle">Tarjeta de consulta r&aacute;pida &mdash; cifra + contexto, nunca la cifra sola</div>
  <div class="tagline">
    2026 &middot; Tarjeta derivada de PBM-02 y PBM-12 &middot; CAUSA / SACYL<br>
    <b>Idea:</b> cada componente tiene su umbral; son <b>referencias</b>, no autom&aacute;ticos. Ojo a la excepci&oacute;n del SCA.
  </div>
</section>
"""

BODY = r"""
<div class="tbl-title">Hemat&iacute;es &middot; umbral restrictivo de hemoglobina</div>
<table class="avoid-break">
  <thead><tr><th>Contexto</th><th style="width:34%">Umbral orientativo</th></tr></thead>
  <tbody>
    <tr><td>Adulto estable / cr&iacute;tico estable / shock s&eacute;ptico estable</td><td>Hb &lt; 7&nbsp;g/dl</td></tr>
    <tr><td>Cirug&iacute;a cardíaca</td><td>Hb &lt; 7,5&nbsp;g/dl</td></tr>
    <tr><td>Cirug&iacute;a ortop&eacute;dica / enfermedad cardiovascular cr&oacute;nica</td><td>Hb &lt; 8&nbsp;g/dl</td></tr>
    <tr><td><b>S&iacute;ndrome coronario agudo</b></td><td><b>Liberal &asymp; 10&nbsp;g/dl</b> (en contra de restrictivo)</td></tr>
  </tbody>
  <caption>1&nbsp;U de hematíes &asymp; +1&nbsp;g/dl de Hb. Transfundir de unidad en unidad y reevaluar. Fuentes [1,4].</caption>
</table>

<div class="tbl-title">Plaquetas &middot; umbral por escenario (AABB/ICTMG 2025)</div>
<table class="avoid-break">
  <thead><tr><th>Escenario</th><th style="width:30%">Umbral</th></tr></thead>
  <tbody>
    <tr><td>Profilaxis (trombocitopenia hipoproliferativa) y CVC compresible</td><td>&lt; 10&nbsp;&times;10<sup>9</sup>/l</td></tr>
    <tr><td>Punci&oacute;n lumbar; radiolog&iacute;a intervencionista de bajo riesgo</td><td>&lt; 20&nbsp;&times;10<sup>9</sup>/l</td></tr>
    <tr><td>Cirug&iacute;a mayor no neuroaxial; RI de alto riesgo</td><td>&lt; 50&nbsp;&times;10<sup>9</sup>/l</td></tr>
    <tr><td>Cirug&iacute;a cardiovascular sin sangrado / HIC no quir&uacute;rgica con plaquetas &gt; 100</td><td><b>No transfundir</b></td></tr>
  </tbody>
  <caption>Dosis: hasta 1 unidad de af&eacute;resis. Fuente [2]. Cambios 2025 vs 2015: PL 50&rarr;20; CVC 20&rarr;10.</caption>
</table>

<div class="tbl-title">Plasma y fibrin&oacute;geno</div>
<table class="avoid-break">
  <thead><tr><th>Componente</th><th style="width:50%">Indicaci&oacute;n / umbral</th></tr></thead>
  <tbody>
    <tr><td><b>Plasma (PFC)</b></td><td>Sangrado o procedimiento con coagulopat&iacute;a documentada; 10&ndash;15&nbsp;ml/kg. <b>No</b> por INR/TTPa leve sin sangrado [3].</td></tr>
    <tr><td><b>Fibrin&oacute;geno / crio</b></td><td>Reponer si &lt; 1,5&nbsp;g/l o d&eacute;ficit funcional en sangrado [4].</td></tr>
  </tbody>
  <caption>Fuentes [3,4]. CVC: cat&eacute;ter venoso central; RI: radiolog&iacute;a intervencionista; HIC: hemorragia intracraneal.</caption>
</table>

<div class="box alert avoid-break"><span class="box-h">No olvidar</span>
  <p>El umbral es una <b>referencia</b>: integra s&iacute;ntomas, sangrado activo y comorbilidad. En <b>hemorragia masiva</b> rige el
  protocolo (P-QR derivada de PBM-13), no estos umbrales. En <b>SCA</b>, s&eacute; m&aacute;s liberal (&asymp;10&nbsp;g/dl).</p>
</div>
"""

REFS = r"""
<h2 class="sec"><span class="num">&middot;</span>Referencias</h2>
<ol class="refs">
  <li>Carson JL, Stanworth SJ, Guyatt G, et al. Red Blood Cell Transfusion: 2023 AABB International Guidelines. <i>JAMA</i> 2023;330(19):1892&ndash;1902. <span class="doi">doi:10.1001/jama.2023.12914</span> &middot; PMID 37824153.</li>
  <li>Metcalf RA, Nahirniak S, Guyatt G, et al. Platelet Transfusion: 2025 AABB and ICTMG International Clinical Practice Guidelines. <i>JAMA</i> 2025;334(7):606&ndash;617. <span class="doi">doi:10.1001/jama.2025.7529</span> &middot; PMID 40440268.</li>
  <li>Green L, Bolton-Maggs P, Beattie C, et al. British Society of Haematology Guidelines on fresh frozen plasma and cryoprecipitate products. <i>Br J Haematol</i> 2018;181(1):54&ndash;67. <span class="doi">doi:10.1111/bjh.15167</span> &middot; PMID 29527654.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, et al. Management of severe peri-operative bleeding: ESAIC Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "P-QR-02-umbrales-por-componente.html")
    print("HTML:", h); print("PDF :", p)
