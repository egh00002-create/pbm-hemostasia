# -*- coding: utf-8 -*-
"""PBM-02 - Componentes sanguineos y sus indicaciones (hematies, plasma, plaquetas). Ancla GUIA."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-02 Componentes sanguineos y sus indicaciones (hematies, plasma, plaquetas). Ancla GUIA.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-02 - Modulo 1 - ancla GUIA - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de guias y fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-02</span>
    <span class="badge b-guia">GU&Iacute;A &middot; gu&iacute;a / consenso formal</span>
    <span class="module-tag">M&oacute;dulo 1 &middot; Fundamentos: PBM y medicina transfusional</span>
  </div>
  <div class="kicker">Componentes sangu&iacute;neos &middot; Indicaciones &middot; Umbrales por producto</div>
  <h1 class="title">Componentes sangu&iacute;neos y sus indicaciones: hemat&iacute;es, plasma y plaquetas</h1>
  <div class="subtitle">Tres productos, tres l&oacute;gicas distintas &mdash; qu&eacute; transfundir, cu&aacute;ndo y con qu&eacute; umbral, seg&uacute;n las gu&iacute;as</div>
  <div class="meta-row">
    <span class="meta-chip">De la sangre total a los componentes</span>
    <span class="meta-chip">Hemat&iacute;es: umbral restrictivo</span>
    <span class="meta-chip">Plaquetas: profilaxis vs terapia</span>
    <span class="meta-chip">Plasma: indicaciones reales</span>
    <span class="meta-chip">Crioprecipitado / fibrin&oacute;geno</span>
  </div>
  <div class="refbar guiabar">
    <b>Ancla de evidencia (referencia vertebral):</b> Carson JL, Stanworth SJ, Guyatt G, et&nbsp;al.
    <i>Red Blood Cell Transfusion: 2023 AABB International Guidelines.</i> JAMA 2023;330(19):1892&ndash;1902.
    <span class="mono">doi:10.1001/jama.2023.12914 &middot; PMID&nbsp;37824153</span>.
  </div>
  <div class="tagline">
    2026 &middot; 4 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> cada componente tiene una <b>indicaci&oacute;n y un umbral propios</b> respaldados por gu&iacute;as:
    los hemat&iacute;es se rigen por un <b>umbral restrictivo de Hb</b> (&asymp;7&ndash;8&nbsp;g/dl), las plaquetas por el <b>recuento y el escenario</b>
    (10, 20 o 50&nbsp;&times;10<sup>9</sup>/l) y el plasma por la <b>coagulopat&iacute;a con sangrado</b>, no por una cifra anal&iacute;tica aislada.
    Transfundir &laquo;por el n&uacute;mero&raquo; sin contexto cl&iacute;nico es la fuente m&aacute;s com&uacute;n de uso inapropiado.
  </div>
  <div class="lead">
    <p>La sangre donada casi nunca se transfunde entera: se <b>fracciona</b> en componentes &mdash;concentrado de hemat&iacute;es,
    plaquetas y plasma&mdash; para tratar <b>el d&eacute;ficit concreto</b> de cada paciente y aprovechar cada donaci&oacute;n [1].
    Esto exige conocer, para cada producto, <b>qu&eacute; corrige, cu&aacute;ndo est&aacute; indicado y con qu&eacute; umbral</b>.</p>
    <p>Este documento es la pieza pr&aacute;ctica que sigue a la cabeza de serie: aterriza el principio del PBM &mdash;transfundir
    solo cuando aporta beneficio&mdash; en las <b>indicaciones por componente</b> que fijan las gu&iacute;as de la <b>AABB</b>,
    la <b>BSH</b> y la <b>ESAIC</b>. El hilo conductor es que el umbral correcto rara vez es una cifra sola: es la
    cifra <b>m&aacute;s</b> el contexto cl&iacute;nico (sangrado, estabilidad, procedimiento previsto).</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>De la sangre total a los componentes</li>
  <li>Concentrado de hemat&iacute;es: indicaci&oacute;n y umbral</li>
  <li>Plaquetas: profilaxis frente a terapia</li>
  <li>Plasma fresco congelado: indicaciones reales</li>
  <li>Crioprecipitado y fibrin&oacute;geno</li>
  <li>Tabla integradora de indicaciones y umbrales</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>De la sangre total a los componentes</h2>
<p>Una donaci&oacute;n de sangre total se separa por centrifugaci&oacute;n en sus fracciones, de modo que cada paciente recibe
<b>solo el componente que necesita</b>. As&iacute; se evita exponerlo a vol&uacute;menes y elementos in&uacute;tiles y se optimiza el recurso:
de una sola donaci&oacute;n pueden beneficiarse varios receptores [1]. Los tres componentes celulares/plasm&aacute;ticos de uso
perioperatorio corriente son el <b>concentrado de hemat&iacute;es</b> (transporte de ox&iacute;geno), las <b>plaquetas</b> (hemostasia
primaria) y el <b>plasma fresco congelado</b> (factores de la coagulaci&oacute;n). Cada uno corrige un d&eacute;ficit distinto y, por
tanto, tiene una indicaci&oacute;n y un umbral propios &mdash;no son intercambiables&mdash;.</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>Tres componentes, <b>tres l&oacute;gicas</b>: hemat&iacute;es = ox&iacute;geno; plaquetas = hemostasia primaria; plasma = factores.</li>
  <li>El umbral correcto es <b>cifra + contexto</b> (sangrado activo, estabilidad, procedimiento), no un n&uacute;mero aislado.</li>
  <li>El error m&aacute;s frecuente es transfundir <b>profil&aacute;cticamente por una analítica</b> en un paciente que no sangra.</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>Concentrado de hemat&iacute;es: indicaci&oacute;n y umbral</h2>
<p>El concentrado de hemat&iacute;es se transfunde para <b>mejorar el transporte de ox&iacute;geno</b> cuando la anemia compromete la
oxigenaci&oacute;n tisular. La evidencia acumulada &mdash;45 ensayos aleatorizados con m&aacute;s de 20.000 participantes&mdash; sustenta una
<b>estrategia restrictiva</b>: en el adulto hospitalizado y hemodin&aacute;micamente estable, la AABB <b>recomienda</b> considerar
la transfusi&oacute;n con Hb &lt; 7&nbsp;g/dl (recomendaci&oacute;n fuerte, certeza moderada) [1]. Para escenarios concretos, el panel
admite umbrales algo superiores en l&iacute;nea con los ensayos: <b>7,5&nbsp;g/dl en cirug&iacute;a cardíaca</b> y <b>8&nbsp;g/dl en cirug&iacute;a
ortop&eacute;dica o en pacientes con enfermedad cardiovascular preexistente</b> [1].</p>
<p>Regla pr&aacute;ctica de dosis: en el adulto, <b>una unidad eleva la Hb &asymp; 1&nbsp;g/dl</b> (o el hematocrito &asymp; 3&nbsp;%). La
filosof&iacute;a PBM es transfundir <b>de unidad en unidad y reevaluar</b>, en lugar de pautar dos unidades por defecto.</p>

<div class="box note avoid-break"><span class="box-h">El umbral no es un autom&aacute;tico</span>
  <p>Las cifras (7 / 7,5 / 8&nbsp;g/dl) marcan <b>cu&aacute;ndo considerar</b> transfundir, no un disparador obligatorio. La decisi&oacute;n
  integra s&iacute;ntomas de anemia, sangrado activo, reserva cardiopulmonar y alternativas disponibles; las propias gu&iacute;as
  recuerdan valorar el <b>contexto cl&iacute;nico global</b> y las alternativas a la transfusi&oacute;n [1]. En el <b>s&iacute;ndrome coronario
  agudo</b> con anemia, la evidencia reciente cuestiona la estrategia restrictiva (&rarr; PBM-12).</p>
</div>

<h2 class="sec"><span class="num">3.</span>Plaquetas: profilaxis frente a terapia</h2>
<p>Las plaquetas se transfunden para <b>prevenir</b> (profilaxis) o <b>tratar</b> (terapia) la hemorragia asociada a
trombocitopenia o disfunci&oacute;n plaquetaria. Las <b>guías AABB/ICTMG 2025</b> &mdash;que actualizan la cl&aacute;sica de 2015&mdash;
fijan umbrales <b>por escenario</b>, con una filosof&iacute;a netamente <b>restrictiva</b> [2]:</p>
<ul>
  <li><b>10&nbsp;&times;10<sup>9</sup>/l</b> &mdash; profilaxis en trombocitopenia hipoproliferativa por quimioterapia o
  trasplante alog&eacute;nico de progenitores, en paciente sin sangrado (recomendaci&oacute;n fuerte). Dosis: hasta <b>una unidad de
  af&eacute;resis</b> o equivalente; dosis mayores no son m&aacute;s eficaces.</li>
  <li><b>10&nbsp;&times;10<sup>9</sup>/l</b> &mdash; tambi&eacute;n para colocaci&oacute;n de cat&eacute;ter venoso central en sitios anat&oacute;micos
  <b>compresibles</b>.</li>
  <li><b>20&nbsp;&times;10<sup>9</sup>/l</b> &mdash; antes de punci&oacute;n lumbar; y en radiolog&iacute;a intervencionista de bajo riesgo.</li>
  <li><b>50&nbsp;&times;10<sup>9</sup>/l</b> &mdash; antes de cirug&iacute;a mayor no neuroaxial; y en radiolog&iacute;a intervencionista de
  alto riesgo.</li>
</ul>
<p>Dos recomendaciones <b>en contra</b> de transfundir, novedosas y pr&aacute;cticas: en <b>cirug&iacute;a cardiovascular</b> (incluida
circulaci&oacute;n extracorp&oacute;rea) sin hemorragia mayor y sin trombocitopenia, <b>no</b> se transfunde de forma profil&aacute;ctica; y en
la <b>hemorragia intracraneal no quir&uacute;rgica</b> con plaquetas &gt; 100&nbsp;&times;10<sup>9</sup>/l, <b>incluso bajo
antiagregantes</b>, <b>no</b> se transfunde [2].</p>

<div class="box alert avoid-break"><span class="box-h">Qu&eacute; cambia respecto a 2015</span>
  <p>La actualizaci&oacute;n de 2025 <b>baja</b> dos dinteles cl&aacute;sicos: punci&oacute;n lumbar <b>de 50 a 20</b>&nbsp;&times;10<sup>9</sup>/l
  y cat&eacute;ter venoso central <b>de 20 a 10</b>&nbsp;&times;10<sup>9</sup>/l, y a&ntilde;ade la recomendaci&oacute;n expl&iacute;cita de <b>no</b>
  transfundir en la HIC no quir&uacute;rgica con antiagregantes (en l&iacute;nea con el ensayo PATCH) [2]. Para procedimientos de muy
  alto riesgo (p.&nbsp;ej. neurocirug&iacute;a) suelen perseguirse cifras superiores seg&uacute;n protocolo local. En la hemorragia
  masiva, las plaquetas se manejan dentro del <b>protocolo de transfusi&oacute;n masiva</b> (&rarr; PBM-13), no por estos umbrales
  profil&aacute;cticos.</p>
</div>

<h2 class="sec"><span class="num">4.</span>Plasma fresco congelado: indicaciones reales</h2>
<p>El plasma fresco congelado (PFC) aporta <b>factores de la coagulaci&oacute;n</b> y est&aacute; indicado, esencialmente, en el
<b>paciente que sangra (o va a someterse a un procedimiento invasivo) con coagulopat&iacute;a documentada</b>, y en la reversi&oacute;n
urgente de anticoagulantes cuando no se dispone de concentrado de complejo protrombínico. La dosis habitual es de
<b>10&ndash;15&nbsp;ml/kg</b>. La gu&iacute;a de la BSH es expl&iacute;cita en lo que <b>no</b> es indicaci&oacute;n: no debe usarse para
&laquo;corregir&raquo; alteraciones leves de las pruebas de coagulaci&oacute;n antes de procedimientos en ausencia de sangrado, ni como
expansor de volumen, ni para revertir warfarina cuando hay alternativas mejores [3].</p>

<div class="box rev avoid-break"><span class="box-h">Lo que el plasma no es</span>
  <p>Transfundir PFC por un INR o un TTPa levemente alterados en un paciente que <b>no sangra</b> es una de las
  indicaciones inapropiadas m&aacute;s frecuentes: corrige poco esos par&aacute;metros, no mejora desenlaces y a&ntilde;ade riesgo (TACO,
  TRALI, reacciones) [3]. La decisi&oacute;n debe basarse en el <b>contexto cl&iacute;nico</b>, no en la cifra aislada.</p>
</div>

<h2 class="sec"><span class="num">5.</span>Crioprecipitado y fibrin&oacute;geno</h2>
<p>El crioprecipitado es la fracci&oacute;n rica en <b>fibrin&oacute;geno</b>, factor&nbsp;VIII, factor&nbsp;XIII, factor de von Willebrand y
fibronectina que se obtiene del plasma. Su uso perioperatorio principal es la <b>reposici&oacute;n de fibrin&oacute;geno</b> en la
hemorragia con hipofibrinogenemia. La gu&iacute;a europea de sangrado perioperatorio grave (ESAIC) recomienda mantener el
fibrin&oacute;geno y aportar concentrado de fibrin&oacute;geno o crioprecipitado cuando, en el contexto de sangrado, el fibrin&oacute;geno
plasm&aacute;tico es <b>&lt; 1,5&nbsp;g/l</b> (o hay un d&eacute;ficit funcional en viscoel&aacute;stica) [4]. En muchos pa&iacute;ses europeos el
<b>concentrado de fibrin&oacute;geno</b> ha desplazado al crioprecipitado por su estandarizaci&oacute;n y seguridad; se desarrolla en
PBM-18.</p>

<h2 class="sec"><span class="num">6.</span>Tabla integradora de indicaciones y umbrales</h2>
<div class="tbl-title">Tabla 1 &middot; Componentes sangu&iacute;neos: qu&eacute; corrigen, indicaci&oacute;n y umbral orientativo</div>
<table class="avoid-break">
  <thead><tr><th style="width:16%">Componente</th><th style="width:18%">Qu&eacute; aporta</th><th>Indicaci&oacute;n / umbral orientativo</th><th style="width:14%">Respaldo</th></tr></thead>
  <tbody>
    <tr><td><b>Hemat&iacute;es</b></td><td>Transporte de O<sub>2</sub></td>
      <td>Estrategia restrictiva: Hb &lt; 7&nbsp;g/dl (estable). 7,5 en cirug&iacute;a cardíaca; 8 en ortopedia o enfermedad cardiovascular. 1&nbsp;U &asymp; +1&nbsp;g/dl de Hb [1].</td>
      <td class="c"><span class="gr gr-fuerte">FUERTE</span></td></tr>
    <tr><td><b>Plaquetas</b></td><td>Hemostasia primaria</td>
      <td>Profilaxis si &lt; 10&times;10<sup>9</sup>/l (trombocitopenia hipoproliferativa; tambi&eacute;n CVC compresible); &lt; 20 para punci&oacute;n lumbar o RI de bajo riesgo; &lt; 50 para cirug&iacute;a mayor no neuroaxial o RI de alto riesgo. <b>En contra</b>: cirug&iacute;a cardiovascular sin sangrado e HIC no quir&uacute;rgica con plaquetas &gt; 100. 1 af&eacute;resis por dosis [2].</td>
      <td class="c"><span class="gr gr-fuerte">FUERTE</span> / <span class="gr gr-debil">D&Eacute;BIL</span></td></tr>
    <tr><td><b>Plasma (PFC)</b></td><td>Factores de coagulaci&oacute;n</td>
      <td>Sangrado o procedimiento invasivo con coagulopat&iacute;a documentada; 10&ndash;15&nbsp;ml/kg. <b>No</b> para corregir analíticas leves sin sangrado [3].</td>
      <td class="c"><span class="gr gr-mod">GU&Iacute;A</span></td></tr>
    <tr><td><b>Crioprecipitado / fibrin&oacute;geno</b></td><td>Fibrin&oacute;geno (y FVIII, FXIII, FvW)</td>
      <td>Reposici&oacute;n de fibrin&oacute;geno en sangrado con fibrin&oacute;geno &lt; 1,5&nbsp;g/l o d&eacute;ficit funcional [4].</td>
      <td class="c"><span class="gr gr-mod">GU&Iacute;A</span></td></tr>
  </tbody>
  <caption>Umbrales orientativos de las gu&iacute;as AABB hemat&iacute;es [1], AABB/ICTMG plaquetas 2025 [2], BSH [3] y ESAIC [4]; los grados (fuerte/d&eacute;bil) son los de la fuente. Cada decisi&oacute;n integra el contexto cl&iacute;nico y los protocolos locales. CVC: cat&eacute;ter venoso central; RI: radiolog&iacute;a intervencionista; HIC: hemorragia intracraneal.</caption>
</table>

<h2 class="sec"><span class="num">7.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> cada componente sangu&iacute;neo corrige un d&eacute;ficit distinto y se rige por una
indicaci&oacute;n y un umbral propios respaldados por gu&iacute;as &mdash;hemat&iacute;es por umbral restrictivo de Hb, plaquetas por recuento y
escenario, plasma por coagulopat&iacute;a con sangrado&mdash;. El umbral es una <b>referencia, no un autom&aacute;tico</b>: la decisi&oacute;n
correcta combina la cifra con el contexto cl&iacute;nico, y muchas recomendaciones (sobre todo en plaquetas y plasma) son de
certeza baja, por lo que conviene aplicarlas con honestidad sobre su fuerza real.</p>
<p>Este documento <b>conecta con PBM-03</b> (seguridad transfusional: identificaci&oacute;n, trazabilidad y reacciones),
<b>con PBM-12</b> (umbrales restrictivos de hemat&iacute;es en detalle: TRICC, TRISS, REALITY, y el matiz del s&iacute;ndrome coronario
agudo), <b>con PBM-13</b> (hemorragia crítica y transfusi&oacute;n masiva, donde el manejo por componentes cambia) y <b>con
PBM-18</b> (fibrin&oacute;geno y f&aacute;rmacos hemost&aacute;ticos). El resumen de umbrales por componente se condensa en la tarjeta
<b>P-QR-02</b>.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>Tres componentes, tres l&oacute;gicas: transfunde hemat&iacute;es por un umbral restrictivo de Hb, plaquetas por recuento y
  escenario, y plasma solo ante coagulopat&iacute;a con sangrado &mdash;siempre cifra <i>m&aacute;s</i> contexto, no la cifra sola&mdash;.</p>
</div>

<h2 class="sec"><span class="num">8.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento de tipo <b>GUÍA</b>, apoyado en guías de pr&aacute;ctica cl&iacute;nica internacionales. Las referencias se han verificado
contra PubMed (autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Las cifras proceden directamente de las fuentes primarias:
umbral restrictivo de Hb &lt; 7&nbsp;g/dl con variantes de 7,5 (cardíaca) y 8&nbsp;g/dl (ortopedia/enfermedad cardiovascular)
[1]; umbrales plaquetarios de 10, 20 y 50&nbsp;&times;10<sup>9</sup>/l por escenario, con las recomendaciones en contra
(cirug&iacute;a cardiovascular, HIC) de las <b>guías AABB/ICTMG 2025</b> &mdash;basadas en metodolog&iacute;a GRADE sobre 21 ECA y 13
estudios observacionales, que actualizan y rebajan los dinteles de 2015 (punci&oacute;n lumbar 50&rarr;20; CVC 20&rarr;10)&mdash; [2];
indicaciones y no indicaciones del plasma [3]; y dintel de fibrin&oacute;geno &lt; 1,5&nbsp;g/l en sangrado [4]. Se declara
expl&iacute;citamente que varias recomendaciones (plaquetas en procedimientos, plasma) son de <b>certeza baja o muy baja</b>
seg&uacute;n las propias gu&iacute;as.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">9.</span>Referencias</h2>
<ol class="refs">
  <li>Carson JL, Stanworth SJ, Guyatt G, Valentine S, Dennis J, Bakhtary S, et al. Red Blood Cell Transfusion: 2023 AABB International Guidelines. <i>JAMA</i> 2023;330(19):1892&ndash;1902. <span class="doi">doi:10.1001/jama.2023.12914</span> &middot; PMID 37824153.</li>
  <li>Metcalf RA, Nahirniak S, Guyatt G, Bathla A, White SK, Al-Riyami AZ, et al. Platelet Transfusion: 2025 AABB and ICTMG International Clinical Practice Guidelines. <i>JAMA</i> 2025;334(7):606&ndash;617. <span class="doi">doi:10.1001/jama.2025.7529</span> &middot; PMID 40440268. <span style="color:#6E6168">[Actualiza a Kaufman RM, et al. <i>Ann Intern Med</i> 2015;162(3):205&ndash;213, doi:10.7326/M14-1589.]</span></li>
  <li>Green L, Bolton-Maggs P, Beattie C, Cardigan R, Kallis Y, Stanworth SJ, et al. British Society of Haematology Guidelines on the spectrum of fresh frozen plasma and cryoprecipitate products: their handling and use in various patient groups in the absence of major bleeding. <i>Br J Haematol</i> 2018;181(1):54&ndash;67. <span class="doi">doi:10.1111/bjh.15167</span> &middot; PMID 29527654.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-02-componentes-sanguineos.html")
    print("HTML:", h); print("PDF :", p)
