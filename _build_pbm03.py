# -*- coding: utf-8 -*-
"""PBM-03 - Seguridad transfusional: identificacion, trazabilidad y reacciones adversas. Ancla GUIA."""
from build_doc import build

META = {
    "comment": "SERIE PBM - PBM-03 Seguridad transfusional. Ancla GUIA.",
    "footer": ("Serie Hemostasia y Medicina Transfusional Perioperatoria (PBM) - Documento PBM-03 - Modulo 1 - ancla GUIA - 2026. "
               "Sintesis docente en espanol para adjuntos y residentes (CAUSA / SACYL). "
               "Cifras procedentes de fuentes primarias indexadas verificadas contra PubMed. "
               "No sustituye al juicio clinico ni a los protocolos locales vigentes."),
}

COVER = r"""
<section class="cover">
  <div class="docref">
    <span class="doc-code">PBM-03</span>
    <span class="badge b-guia">GU&Iacute;A &middot; gu&iacute;a / consenso formal</span>
    <span class="module-tag">M&oacute;dulo 1 &middot; Fundamentos: PBM y medicina transfusional</span>
  </div>
  <div class="kicker">Seguridad transfusional &middot; Identificaci&oacute;n &middot; Trazabilidad &middot; Reacciones</div>
  <h1 class="title">Seguridad transfusional: identificaci&oacute;n, trazabilidad y reacciones adversas</h1>
  <div class="subtitle">El riesgo m&aacute;s grave ya no es el virus: es el error de identificaci&oacute;n &mdash; y la sobrecarga de volumen</div>
  <div class="meta-row">
    <span class="meta-chip">La cadena de identificaci&oacute;n</span>
    <span class="meta-chip">Trazabilidad y hemovigilancia</span>
    <span class="meta-chip">Reacciones agudas</span>
    <span class="meta-chip">Reacciones diferidas</span>
    <span class="meta-chip">TACO y TRALI</span>
  </div>
  <div class="refbar guiabar">
    <b>Ancla de evidencia (referencia vertebral):</b> Delaney M, Wendel S, Bercovitz RS, et&nbsp;al.
    <i>Transfusion reactions: prevention, diagnosis, and treatment.</i> Lancet 2016;388(10061):2825&ndash;2836.
    <span class="mono">doi:10.1016/S0140-6736(15)01313-6 &middot; PMID&nbsp;27083327</span>.
  </div>
  <div class="tagline">
    2026 &middot; 3 referencias indexadas verificadas en PubMed &middot; S&iacute;ntesis docente para adjuntos y residentes (CAUSA / SACYL)<br>
    <b>Mensaje nuclear:</b> la transfusi&oacute;n moderna es muy segura frente a la infecci&oacute;n, pero los riesgos dominantes hoy son
    <b>no infecciosos</b>: el <b>error de identificaci&oacute;n</b> (transfusi&oacute;n ABO incompatible, casi siempre evitable) y las
    reacciones por <b>sobrecarga de volumen (TACO)</b> y pulmonares (TRALI). La seguridad se juega en la <b>cabecera del
    paciente</b>, no solo en el laboratorio.
  </div>
  <div class="lead">
    <p>El cribado de donantes y las pruebas de &aacute;cidos nucleicos han reducido el riesgo de transmisi&oacute;n viral a cifras
    &iacute;nfimas. El resultado parad&oacute;jico es que los <b>riesgos no infecciosos</b> &mdash;errores administrativos y reacciones
    inmunes o por volumen&mdash; son hoy la principal causa de morbimortalidad transfusional [1].</p>
    <p>Este documento cierra el bloque de fundamentos con la dimensi&oacute;n de <b>seguridad</b>: la cadena de identificaci&oacute;n que
    previene la transfusi&oacute;n equivocada, la trazabilidad y hemovigilancia que cierran el c&iacute;rculo, y el reconocimiento y
    manejo de las <b>reacciones adversas</b>. Es el complemento imprescindible de las indicaciones de PBM-02.</p>
  </div>
</section>
"""

BODY = r"""
<nav class="toc avoid-break"><h2>&Iacute;ndice</h2><ol>
  <li>El mapa del riesgo: del virus al error</li>
  <li>La cadena de identificaci&oacute;n: &laquo;sangre correcta, paciente correcto&raquo;</li>
  <li>Trazabilidad y hemovigilancia</li>
  <li>Reacciones agudas (&lt; 24&nbsp;h)</li>
  <li>Reacciones diferidas</li>
  <li>TACO y TRALI: las dos primeras causas de muerte</li>
  <li>Mensaje nuclear y conexiones</li>
  <li>Verificaci&oacute;n bibliogr&aacute;fica</li>
  <li>Referencias</li>
</ol></nav>

<h2 class="sec"><span class="num">1.</span>El mapa del riesgo: del virus al error</h2>
<p>La percepci&oacute;n popular asocia el riesgo transfusional al contagio (VIH, hepatitis). Hoy ese riesgo es extremadamente
bajo gracias al cribado serol&oacute;gico y molecular. Los riesgos relevantes en la pr&aacute;ctica son <b>no infecciosos</b>: el
<b>error de identificaci&oacute;n</b> que conduce a transfusi&oacute;n ABO incompatible y las reacciones por <b>sobrecarga de volumen
(TACO)</b> y pulmonares <b>(TRALI)</b>, que encabezan las series de mortalidad de hemovigilancia [1].</p>

<div class="box key avoid-break"><span class="box-h">Puntos clave</span><ul>
  <li>El mayor riesgo <b>letal evitable</b> es la transfusi&oacute;n ABO incompatible por <b>error administrativo</b>.</li>
  <li><b>TACO</b> (sobrecarga circulatoria) es hoy una de las principales causas de muerte transfusional [1].</li>
  <li>La mejor estrategia de seguridad es <b>transfundir menos y mejor</b> (PBM): el componente no transfundido no causa da&ntilde;o.</li>
</ul></div>

<h2 class="sec"><span class="num">2.</span>La cadena de identificaci&oacute;n: &laquo;sangre correcta, paciente correcto&raquo;</h2>
<p>La mayor&iacute;a de los incidentes graves se originan en <b>errores humanos</b> de identificaci&oacute;n en alguno de los eslabones:
la extracci&oacute;n de la muestra de grupo, el etiquetado, la dispensaci&oacute;n y, sobre todo, la <b>comprobaci&oacute;n final a pie de
cama</b>. La verificaci&oacute;n positiva de la identidad del paciente inmediatamente antes de conectar la unidad es la
&uacute;ltima barrera y la m&aacute;s eficaz [1].</p>

<div class="flow avoid-break">
  <div class="step"><b>1. Muestra:</b> identificar al paciente <i>activamente</i> y etiquetar el tubo <b>junto a la cama</b>, nunca por adelantado.</div>
  <div class="step"><b>2. Laboratorio:</b> grupo, escrutinio de anticuerpos y pruebas cruzadas; regla de la doble determinaci&oacute;n del grupo.</div>
  <div class="step"><b>3. Dispensaci&oacute;n:</b> verificaci&oacute;n de compatibilidad y trazabilidad de la unidad asignada.</div>
  <div class="step a"><b>4. Cabecera (cr&iacute;tico):</b> comprobaci&oacute;n final de identidad paciente&ndash;unidad antes de transfundir; vigilar las primeras constantes.</div>
</div>

<h2 class="sec"><span class="num">3.</span>Trazabilidad y hemovigilancia</h2>
<p>Cada unidad debe poder seguirse desde el donante hasta el receptor y viceversa (<b>trazabilidad bidireccional</b>), una
exigencia legal en la UE. Los sistemas de <b>hemovigilancia</b> (en el Reino Unido, el registro SHOT) recogen y analizan los
incidentes para retroalimentar la mejora: gracias a ellos sabemos que los errores de identificaci&oacute;n y el TACO dominan la
morbimortalidad actual [1]. Notificar los incidentes &mdash;incluidos los &laquo;casi errores&raquo;&mdash; es parte del deber profesional.</p>

<h2 class="sec"><span class="num">4.</span>Reacciones agudas (&lt; 24&nbsp;h)</h2>
<div class="tbl-title">Tabla 1 &middot; Reacciones transfusionales agudas: clave de reconocimiento</div>
<table class="avoid-break">
  <thead><tr><th style="width:24%">Reacci&oacute;n</th><th>Rasgo distintivo y actuaci&oacute;n inicial</th></tr></thead>
  <tbody>
    <tr><td><b>Hemol&iacute;tica aguda (AHTR)</b></td><td>ABO incompatible: fiebre, dolor lumbar/tor&aacute;cico, hipotensi&oacute;n, orina oscura. <b>Parar de inmediato</b>, soporte, fluidos, comprobar identidad y avisar al banco [1].</td></tr>
    <tr><td><b>Febril no hemol&iacute;tica (FNHTR)</b></td><td>Fiebre/escalofr&iacute;os sin hemolisis; diagn&oacute;stico de exclusi&oacute;n. Antit&eacute;rmicos; la leucorreducci&oacute;n la reduce [1].</td></tr>
    <tr><td><b>Al&eacute;rgica / anafilaxia</b></td><td>Urticaria (leve) hasta anafilaxia. Leve: antihistam&iacute;nico y reanudar; grave: parar, adrenalina y soporte [1].</td></tr>
    <tr><td><b>TACO</b></td><td>Sobrecarga: disnea, hipertensi&oacute;n, edema pulmonar en &lt; 6&nbsp;h. Parar, sentar, diur&eacute;tico, O<sub>2</sub>; prevenir con ritmo lento [1].</td></tr>
    <tr><td><b>TRALI</b></td><td>Edema pulmonar no cardiog&eacute;nico &lt; 6&nbsp;h por anticuerpos antileucocitarios. Parar, soporte respiratorio [1].</td></tr>
    <tr><td><b>S&eacute;ptica</b></td><td>Fiebre alta y shock por contaminaci&oacute;n bacteriana (m&aacute;s con plaquetas). Parar, hemocultivos, antibi&oacute;ticos [1].</td></tr>
  </tbody>
  <caption>S&iacute;ntesis a partir de Delaney et&nbsp;al. [1]. Ante cualquier reacci&oacute;n grave: <b>detener la transfusi&oacute;n</b>, mantener la v&iacute;a, reevaluar identidad y notificar al banco de sangre.</caption>
</table>

<h2 class="sec"><span class="num">5.</span>Reacciones diferidas</h2>
<p>M&aacute;s all&aacute; de las 24&nbsp;h aparecen la <b>reacci&oacute;n hemol&iacute;tica diferida</b> (por respuesta an&aacute;mnesica a antígenos
eritrocitarios, con descenso de Hb y test de antiglobulina positivo), la <b>aloinmunizaci&oacute;n</b>, la rara pero grave
<b>enfermedad injerto contra hu&eacute;sped asociada a transfusi&oacute;n (TA-GVHD)</b> &mdash;prevenible con irradiaci&oacute;n de componentes en
pacientes de riesgo&mdash;, la <b>p&uacute;rpura postransfusional</b> y la <b>sobrecarga de hierro</b> en politransfundidos cr&oacute;nicos [1].</p>

<h2 class="sec"><span class="num">6.</span>TACO y TRALI: las dos primeras causas de muerte</h2>
<p>Ambas cursan con <b>disnea aguda y edema pulmonar</b> en las primeras horas, pero su mecanismo difiere: el <b>TACO</b> es
hidrost&aacute;tico (exceso de volumen, m&aacute;s en ancianos, ni&ntilde;os, insuficiencia cardíaca o renal) y el <b>TRALI</b> es una lesi&oacute;n
pulmonar inmunomediada. La distinci&oacute;n guía el tratamiento (diur&eacute;ticos en TACO; soporte respiratorio en TRALI). La
prevenci&oacute;n del TACO &mdash;ritmo lento, una unidad cada vez, valoraci&oacute;n del balance&mdash; conecta directamente con la filosof&iacute;a
restrictiva del PBM [1].</p>

<div class="box pearl avoid-break"><span class="box-h">Perla</span>
  <p>Ante disnea durante o tras una transfusi&oacute;n, piensa <b>TACO</b> primero: es m&aacute;s frecuente y a menudo infradiagnosticado.
  La medida preventiva m&aacute;s simple y eficaz es <b>transfundir despacio y de unidad en unidad</b>, reevaluando.</p>
</div>

<h2 class="sec"><span class="num">7.</span>Mensaje nuclear y conexiones</h2>
<p><b>Mensaje nuclear (equilibrado):</b> la transfusi&oacute;n es muy segura frente a la infecci&oacute;n, pero los riesgos dominantes
son evitables y dependen del proceso: el <b>error de identificaci&oacute;n</b> se previene con la verificaci&oacute;n a pie de cama y el
<b>TACO</b> con una transfusi&oacute;n prudente. La hemovigilancia cierra el c&iacute;rculo de mejora. La mejor medida de seguridad
sigue siendo <b>necesitar menos transfusiones</b> (PBM).</p>
<p>Conecta con <b>PBM-02</b> (indicaciones por componente), con <b>PBM-12</b> (umbrales restrictivos que reducen exposici&oacute;n)
y con <b>PBM-13</b> (hemorragia masiva, donde la seguridad convive con la urgencia). La tarjeta <b>P-QR-02</b> resume umbrales.</p>

<div class="box key avoid-break"><span class="box-h">Resumen en una frase</span>
  <p>La seguridad transfusional se juega en la cabecera: identifica bien, transfunde despacio y de unidad en unidad,
  reconoce TACO/TRALI y notifica &mdash;y, sobre todo, transfunde solo cuando aporta beneficio&mdash;.</p>
</div>

<h2 class="sec"><span class="num">8.</span>Verificaci&oacute;n bibliogr&aacute;fica</h2>
<p>Documento de tipo <b>GUÍA</b> apoyado en una revisi&oacute;n internacional basada en la evidencia [1] y en las guías de la serie.
Las afirmaciones &mdash;predominio actual de los riesgos no infecciosos, error de identificaci&oacute;n como principal causa evitable y
TACO como una de las primeras causas de muerte transfusional&mdash; proceden de la fuente primaria verificada contra PubMed
(autor&iacute;a, t&iacute;tulo, revista, a&ntilde;o, DOI/PMID). Las referencias [2] y [3] aportan el marco de seguridad clínica y de manejo del
sangrado.</p>
"""

REFS = r"""
<h2 class="sec"><span class="num">9.</span>Referencias</h2>
<ol class="refs">
  <li>Delaney M, Wendel S, Bercovitz RS, Cid J, Cohn C, Dunbar NM, et al. Transfusion reactions: prevention, diagnosis, and treatment. <i>Lancet</i> 2016;388(10061):2825&ndash;2836. <span class="doi">doi:10.1016/S0140-6736(15)01313-6</span> &middot; PMID 27083327.</li>
  <li>Carson JL, Stanworth SJ, Guyatt G, Valentine S, Dennis J, Bakhtary S, et al. Red Blood Cell Transfusion: 2023 AABB International Guidelines. <i>JAMA</i> 2023;330(19):1892&ndash;1902. <span class="doi">doi:10.1001/jama.2023.12914</span> &middot; PMID 37824153.</li>
  <li>Kietaibl S, Ahmed A, Afshari A, Albaladejo P, Aldecoa C, Barauskas G, et al. Management of severe peri-operative bleeding: Guidelines from the European Society of Anaesthesiology and Intensive Care: Second update 2022. <i>Eur J Anaesthesiol</i> 2023;40(4):226&ndash;304. <span class="doi">doi:10.1097/EJA.0000000000001803</span> &middot; PMID 36855941.</li>
</ol>
"""

if __name__ == "__main__":
    h, p = build(META, COVER, BODY, REFS, "PBM-03-seguridad-transfusional.html")
    print("HTML:", h); print("PDF :", p)
