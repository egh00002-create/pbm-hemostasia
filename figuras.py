# -*- coding: utf-8 -*-
"""figuras.py - Algoritmos en figura (SVG) para la serie PBM, con la paleta granate/acero.
Expone FIGURAS = [(num, titulo, caption, svg)] y FIG_CSS. Reutilizable por el libro."""
import html as _html
def esc(s): return _html.escape(s, quote=False)

FIG_CSS = r"""
  .figbox{ break-inside:avoid; margin:14px 0 18px; }
  .figbox .fig-t{ font-family:"DejaVu Serif",Georgia,serif; font-weight:700; color:var(--accent); font-size:11pt; margin:0 0 4px; }
  .figbox svg{ width:100%; height:auto; border:1px solid var(--line); border-radius:6px; background:#fff; }
  .figbox .fig-c{ font-size:7.6pt; color:var(--muted); line-height:1.4; margin:5px 2px 0; }
"""

# kind -> (fill, stroke, textcolor)
KIND = {
 'start':    ('#8E2433', '#8E2433', '#ffffff'),
 'step':     ('#FBF7F8', '#4F6B7A', '#211A1C'),
 'decision': ('#E7EDF1', '#4F6B7A', '#21343E'),
 'action':   ('#F6E8D8', '#B0682B', '#7A3E1E'),
 'good':     ('#D7EFEC', '#0E6E6B', '#0B524F'),
 'warn':     ('#F4E3E6', '#8E2433', '#8E2433'),
}

def flow(steps):
    """steps: lista de (lines:list[str], kind). Devuelve SVG de flujo vertical."""
    W = 600; bw = 552; x = (W - bw) / 2; y = 10; gap = 18
    body = []
    n = len(steps)
    for i, (lines, kind) in enumerate(steps):
        fill, stroke, tc = KIND[kind]
        h = 20 + 15 * len(lines)
        body.append('<rect x="%g" y="%g" width="%g" height="%g" rx="7" fill="%s" stroke="%s" stroke-width="1.5"/>'
                    % (x, y, bw, h, fill, stroke))
        ty = y + h / 2 - (len(lines) - 1) * 7 + 4
        for k, ln in enumerate(lines):
            weight = '700' if k == 0 else '400'
            body.append('<text x="%g" y="%g" text-anchor="middle" font-family="DejaVu Sans,Arial,sans-serif" '
                        'font-size="%s" font-weight="%s" fill="%s">%s</text>'
                        % (W / 2, ty + k * 14, '10' if k == 0 else '9', weight, tc, esc(ln)))
        if i < n - 1:
            ay = y + h; by = y + h + gap
            body.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="#8A7E83" stroke-width="1.4"/>' % (W/2, ay, W/2, by-3))
            body.append('<path d="M%g %g l-4 -6 l8 0 z" fill="#8A7E83"/>' % (W/2, by-1))
        y += h + gap
    H = y + 2
    return ('<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img">%s</svg>'
            % (W, int(H), "".join(body)))

FIGURAS = [
 (1, "Estudio y tratamiento de la anemia preoperatoria",
  "Ferritina &lt; 30 &micro;g/l = ferropenia absoluta; con inflamaci&oacute;n, ferritina hasta &asymp;100 con saturaci&oacute;n baja sigue sugiriendo ferropenia. Cap. PBM-04/05/06.",
  flow([
   (["Candidato a cirugía mayor con sangrado relevante"], 'start'),
   (["Cribado precoz al indicar la cirugía", "hemograma + índices eritrocitarios"], 'step'),
   (["¿Hb < 130 (♂) / < 120 (♀) g/l?", "No → optimizar y operar"], 'decision'),
   (["Sí: estudio del hierro", "ferritina + saturación de transferrina + PCR"], 'step'),
   (["Tratar la causa", "hierro oral (≥6-8 sem) o IV (poco tiempo/intolerancia) ± EPO"], 'action'),
   (["Reevaluar Hb antes de la cirugía"], 'good'),
  ])),
 (2, "Umbral de transfusión de hematíes por contexto",
  "El umbral es una referencia que integra síntomas y sangrado activo. 1 U &asymp; +1 g/dl. Cap. PBM-12.",
  flow([
   (["Anemia: ¿transfundir hematíes?"], 'start'),
   (["¿Síndrome coronario agudo?"], 'decision'),
   (["SÍ → umbral LIBERAL ≈ 10 g/dl", "(en contra de restrictivo)"], 'warn'),
   (["NO → estrategia RESTRICTIVA por contexto"], 'step'),
   (["Estable/crítico/séptico: Hb < 7", "Cardíaca: < 7,5  ·  Ortopedia/ECV crónica: < 8"], 'step'),
   (["Transfundir de unidad en unidad y reevaluar"], 'good'),
  ])),
 (3, "Hemorragia crítica y protocolo de transfusión masiva",
  "Resucitación de control de daños: limitar cristaloides. PROPPR: 1:1:1 logró más hemostasia. Cap. PBM-13.",
  flow([
   (["Hemorragia crítica no controlada", "activar el protocolo de transfusión masiva"], 'start'),
   (["Ácido tranexámico PRECOZ", "1 g en 10 min + 1 g / 8 h  (< 3 h)"], 'action'),
   (["Transfusión equilibrada ≈ 1:1:1", "plasma : plaquetas : hematíes"], 'step'),
   (["Reponer fibrinógeno si < 1,5 g/l"], 'step'),
   (["Controlar el entorno", "Calcio iónico  ·  Normotermia  ·  pH"], 'warn'),
   (["Transitar a manejo guiado por viscoelástica"], 'good'),
  ])),
 (4, "Manejo perioperatorio de antitrombóticos",
  "Decisión individualizada; los tiempos exactos de suspensión, del protocolo local y la ficha técnica. Cap. PBM-16.",
  flow([
   (["Paciente con antiagregante/anticoagulante + cirugía"], 'start'),
   (["Cruzar: fármaco × riesgo trombótico × riesgo hemorrágico"], 'decision'),
   (["Aspirina (prev. 2ª): a menudo MANTENER", "en riesgo hemorrágico bajo-moderado"], 'step'),
   (["P2Y12: suspender unos días", "stent reciente → posponer / decidir en equipo"], 'step'),
   (["AVK: suspender + INR  (rev. urgente: CCP + vit. K)", "ACOD: suspender según fármaco y función renal, SIN puente"], 'step'),
   (["Puente en FA: NO sistemático (BRIDGE)", "solo alto riesgo trombótico seleccionado"], 'warn'),
  ])),
 (5, "Manejo de la hemorragia guiado por viscoelástica (ROTEM/TEG)",
  "Secuencia dirigida: TXA → fibrinógeno → plaquetas → factores. Evidencia favorable de baja certeza. Cap. PBM-09.",
  flow([
   (["Hemorragia con coagulopatía — ROTEM/TEG"], 'start'),
   (["¿Lisis acelerada?  →  ácido tranexámico"], 'action'),
   (["¿Firmeza baja por vía del fibrinógeno?  →  fibrinógeno/crio"], 'action'),
   (["¿Firmeza baja con fibrinógeno normal?  →  plaquetas"], 'action'),
   (["¿Tiempo de inicio prolongado?  →  plasma / CCP"], 'action'),
  ])),
]
