// Funciones puras de cálculo clínico. Valores y fórmulas EXACTOS y verificados;
// no modificar. Cada calculadora muestra su fuente y el descargo en la UI.

export type Sex = 'varon' | 'mujer';

// ===================== 1) MABL (Nadler + Gross) =====================
//
// Nadler volumen sanguíneo estimado (VSE) en litros:
//   varón: 0.3669*talla^3 + 0.03219*peso + 0.6041
//   mujer: 0.3561*talla^3 + 0.03308*peso + 0.1833
// (talla en metros, peso en kg)
// Gross MABL = VSE_ml * (Hto_ini - Hto_diana) / ((Hto_ini + Hto_diana)/2)

export interface MablInput {
  sex: Sex;
  weightKg: number;
  heightM: number;
  htoInitial: number; // % (p.ej. 42)
  htoTarget: number; // % (p.ej. 28)
}

export interface MablResult {
  bloodVolumeL: number; // VSE en litros
  bloodVolumeMl: number;
  mablMl: number;
}

/** Volumen sanguíneo estimado de Nadler (litros). */
export function nadlerBloodVolumeL(sex: Sex, weightKg: number, heightM: number): number {
  const h3 = heightM ** 3;
  return sex === 'varon'
    ? 0.3669 * h3 + 0.03219 * weightKg + 0.6041
    : 0.3561 * h3 + 0.03308 * weightKg + 0.1833;
}

/** Pérdida sanguínea admisible (Gross). Devuelve VSE y MABL. */
export function computeMabl(input: MablInput): MablResult {
  const { sex, weightKg, heightM, htoInitial, htoTarget } = input;
  const bloodVolumeL = nadlerBloodVolumeL(sex, weightKg, heightM);
  const bloodVolumeMl = bloodVolumeL * 1000;
  const meanHto = (htoInitial + htoTarget) / 2;
  const mablMl = meanHto > 0 ? (bloodVolumeMl * (htoInitial - htoTarget)) / meanHto : 0;
  return { bloodVolumeL, bloodVolumeMl, mablMl };
}

// ===================== 2) Umbral de hematíes =====================

export type RbcScenario =
  | 'estable'
  | 'critico'
  | 'septico'
  | 'cardiaca'
  | 'ortopedia'
  | 'ecv-cronica'
  | 'sca';

export interface RbcThreshold {
  scenario: RbcScenario;
  label: string;
  thresholdGdl: number;
  liberal: boolean; // true = umbral liberal (SCA)
  note: string;
}

export const RBC_THRESHOLDS: RbcThreshold[] = [
  {
    scenario: 'estable',
    label: 'Adulto estable hospitalizado',
    thresholdGdl: 7,
    liberal: false,
    note: 'Umbral restrictivo: transfundir por debajo de 7 g/dl.',
  },
  {
    scenario: 'critico',
    label: 'Paciente crítico (UCI)',
    thresholdGdl: 7,
    liberal: false,
    note: 'TRICC/TRISS: restrictivo (<7) no inferior y a menudo mejor.',
  },
  {
    scenario: 'septico',
    label: 'Sepsis / shock séptico',
    thresholdGdl: 7,
    liberal: false,
    note: 'TRISS: umbral <7 g/dl seguro en shock séptico.',
  },
  {
    scenario: 'cardiaca',
    label: 'Cirugía cardíaca',
    thresholdGdl: 7.5,
    liberal: false,
    note: 'TRICS-III: restrictivo (<7,5) no inferior al liberal.',
  },
  {
    scenario: 'ortopedia',
    label: 'Ortopedia / cirugía con ECV crónica',
    thresholdGdl: 8,
    liberal: false,
    note: 'FOCUS: umbral <8 g/dl o síntomas en pacientes con riesgo cardiovascular.',
  },
  {
    scenario: 'ecv-cronica',
    label: 'Enfermedad cardiovascular crónica estable',
    thresholdGdl: 8,
    liberal: false,
    note: 'Umbral <8 g/dl o síntomas.',
  },
  {
    scenario: 'sca',
    label: 'Síndrome coronario agudo (SCA)',
    thresholdGdl: 10,
    liberal: true,
    note: 'REALITY/MINT: en SCA se favorece umbral LIBERAL (≈10 g/dl), en contra del restrictivo.',
  },
];

export function rbcThreshold(scenario: RbcScenario): RbcThreshold {
  return RBC_THRESHOLDS.find((t) => t.scenario === scenario) ?? RBC_THRESHOLDS[0];
}

/** Decide si transfundir según Hb y escenario, y estima unidades (1 U ≈ +1 g/dl). */
export interface RbcDecision {
  threshold: RbcThreshold;
  transfuse: boolean;
  unitsToTarget: number; // unidades estimadas para alcanzar el umbral
}

export function rbcDecision(scenario: RbcScenario, hbGdl: number): RbcDecision {
  const threshold = rbcThreshold(scenario);
  const transfuse = hbGdl < threshold.thresholdGdl;
  // 1 U ≈ +1 g/dl; redondeo al alza hasta alcanzar el umbral.
  const deficit = threshold.thresholdGdl - hbGdl;
  const unitsToTarget = transfuse ? Math.max(1, Math.ceil(deficit)) : 0;
  return { threshold, transfuse, unitsToTarget };
}

// ===================== 3) Plaquetas (AABB/ICTMG 2025) =====================

export interface PlateletScenario {
  key: string;
  label: string;
  thresholdK: number | null; // ×10^9/L; null = no transfundir por umbral
  note: string;
}

export const PLATELET_SCENARIOS: PlateletScenario[] = [
  {
    key: 'profilaxis',
    label: 'Profilaxis (estable) / colocación de CVC compresible',
    thresholdK: 10,
    note: 'Transfundir si <10 ×10⁹/L.',
  },
  {
    key: 'pl-ri-bajo',
    label: 'Punción lumbar / procedimiento de bajo riesgo',
    thresholdK: 20,
    note: 'Objetivo ≥20 ×10⁹/L.',
  },
  {
    key: 'cirugia-mayor',
    label: 'Cirugía mayor no neuroaxial / procedimiento de alto riesgo',
    thresholdK: 50,
    note: 'Objetivo ≥50 ×10⁹/L.',
  },
  {
    key: 'cardiaca-sin-sangrado',
    label: 'Cirugía cardiovascular sin sangrado',
    thresholdK: null,
    note: 'NO transfundir de forma profiláctica sin sangrado.',
  },
  {
    key: 'hic-no-quirurgica',
    label: 'HIC no quirúrgica con plaquetas >100 (incl. antiagregantes)',
    thresholdK: null,
    note: 'NO transfundir: sin beneficio e incluso daño (PATCH).',
  },
];

export interface PlateletDecision {
  scenario: PlateletScenario;
  transfuse: boolean | null; // null = no aplica umbral (recomendación: no transfundir)
}

export function plateletDecision(key: string, plateletsK: number): PlateletDecision {
  const scenario =
    PLATELET_SCENARIOS.find((s) => s.key === key) ?? PLATELET_SCENARIOS[0];
  if (scenario.thresholdK === null) {
    return { scenario, transfuse: null };
  }
  return { scenario, transfuse: plateletsK < scenario.thresholdK };
}

// ===================== 4) Plasma / fibrinógeno =====================

export interface PlasmaInput {
  weightKg: number;
  activeBleeding: boolean;
  coagulopathy: boolean; // alteración relevante de la coagulación
}

export interface PlasmaResult {
  indicated: boolean;
  doseMinMl: number; // 10 ml/kg
  doseMaxMl: number; // 15 ml/kg
  message: string;
}

/** Plasma 10–15 ml/kg solo con sangrado/procedimiento + coagulopatía. */
export function plasmaDose(input: PlasmaInput): PlasmaResult {
  const indicated = input.activeBleeding && input.coagulopathy;
  return {
    indicated,
    doseMinMl: Math.round(input.weightKg * 10),
    doseMaxMl: Math.round(input.weightKg * 15),
    message: indicated
      ? 'Indicado: 10–15 ml/kg ante sangrado/procedimiento con coagulopatía.'
      : 'No indicado por INR/TTPa levemente alterado sin sangrado.',
  };
}

export interface FibrinogenInput {
  fibrinogenGl: number; // g/L
  functionalDeficit: boolean;
}

export function fibrinogenIndicated(input: FibrinogenInput): {
  indicated: boolean;
  message: string;
} {
  const indicated = input.fibrinogenGl < 1.5 || input.functionalDeficit;
  return {
    indicated,
    message: indicated
      ? 'Reponer fibrinógeno/crioprecipitado: <1,5 g/L o déficit funcional.'
      : 'Fibrinógeno ≥1,5 g/L sin déficit funcional: no reponer.',
  };
}

// ===================== 5) TXA por escenario =====================

export interface TxaScenario {
  key: string;
  label: string;
  regimen: string;
  window: string;
  caution?: string;
}

export const TXA_SCENARIOS: TxaScenario[] = [
  {
    key: 'trauma',
    label: 'Trauma con hemorragia',
    regimen: '1 g IV en 10 min + 1 g en infusión durante 8 h',
    window: 'Iniciar < 3 h desde el traumatismo (CRASH-2).',
  },
  {
    key: 'hpp',
    label: 'Hemorragia posparto (HPP)',
    regimen: '1 g IV, repetible a los 30 min si persiste',
    window: 'Lo antes posible (WOMAN).',
  },
  {
    key: 'tce',
    label: 'TCE leve-moderado',
    regimen: '1 g IV + 1 g en 8 h',
    window: '< 3 h.',
    caution: 'Beneficio limitado/ausente en TCE grave (CRASH-3).',
  },
  {
    key: 'cirugia',
    label: 'Cirugía electiva (profilaxis)',
    regimen: 'Bolo + infusión según protocolo quirúrgico',
    window: 'Perioperatorio.',
    caution: 'Vigilar convulsiones a dosis altas (ATACAS).',
  },
];

export const TXA_FIXED_MESSAGE = 'Cuanto antes, mejor.';

export function txaScenario(key: string): TxaScenario {
  return TXA_SCENARIOS.find((s) => s.key === key) ?? TXA_SCENARIOS[0];
}

// ===================== 6) HEMSTOP =====================

export interface HemstopItem {
  key: string;
  letter: string;
  label: string;
}

// 7 ítems: Hematoma, hEmorragia, Menorragia, Surgery, Tooth, Obstetrics, Parents
export const HEMSTOP_ITEMS: HemstopItem[] = [
  { key: 'hematoma', letter: 'H', label: '¿Hematomas frecuentes o sin causa aparente?' },
  {
    key: 'hemorragia',
    letter: 'E',
    label: '¿hEmorragia que requiriera consulta médica o tratamiento?',
  },
  { key: 'menorragia', letter: 'M', label: '¿Menorragia / reglas abundantes?' },
  {
    key: 'surgery',
    letter: 'S',
    label: '¿Sangrado prolongado/anómalo tras una cirugía (Surgery)?',
  },
  { key: 'tooth', letter: 'T', label: '¿Sangrado prolongado tras extracción dental (Tooth)?' },
  {
    key: 'obstetrics',
    letter: 'O',
    label: '¿Hemorragia obstétrica relevante (Obstetrics)?',
  },
  {
    key: 'parents',
    letter: 'P',
    label: '¿Antecedentes familiares de trastorno hemorrágico (Parents)?',
  },
];

export interface HemstopResult {
  score: number;
  positive: boolean; // ≥2
  message: string;
}

/** ≥2 respuestas afirmativas → estudio dirigido + valoración por hematología. */
export function hemstopScore(answers: Record<string, boolean>): HemstopResult {
  const score = HEMSTOP_ITEMS.reduce((acc, it) => acc + (answers[it.key] ? 1 : 0), 0);
  const positive = score >= 2;
  return {
    score,
    positive,
    message: positive
      ? '≥2 ítems positivos → estudio de hemostasia dirigido y valoración por hematología.'
      : '0–1 ítems: cribado negativo. No precisa estudio dirigido salvo otros datos clínicos.',
  };
}

// ===================== 7) Antitrombóticos =====================

export type ThromboticRisk = 'bajo' | 'alto';
export type BleedingRisk = 'bajo' | 'alto';

export interface AntithromboticInput {
  drug: string; // etiqueta legible del fármaco
  thrombotic: ThromboticRisk;
  bleeding: BleedingRisk;
  isAtrialFibrillation: boolean; // para la regla BRIDGE
}

export interface AntithromboticAdvice {
  continueIfPossible: boolean;
  bridge: 'no' | 'considerar';
  guidance: string;
  bridgeNote: string;
  disclaimer: string;
}

/**
 * Lógica genérica de decisión (educativa). Los tiempos exactos de suspensión
 * SIEMPRE se toman del protocolo local y la ficha técnica.
 */
export function antithromboticAdvice(input: AntithromboticInput): AntithromboticAdvice {
  const { thrombotic, bleeding, isAtrialFibrillation } = input;

  // Procedimiento de bajo riesgo hemorrágico → a menudo no es necesario suspender.
  const continueIfPossible = bleeding === 'bajo';

  // BRIDGE: en FA no se recomienda el puente sistemático (no inferior, menos hemorragia).
  let bridge: 'no' | 'considerar' = 'no';
  let bridgeNote: string;
  if (isAtrialFibrillation) {
    bridge = 'no';
    bridgeNote =
      'FA: NO realizar puente con HBPM de forma sistemática (BRIDGE: no inferior y menos hemorragia).';
  } else if (thrombotic === 'alto') {
    bridge = 'considerar';
    bridgeNote =
      'Riesgo trombótico alto no-FA (p.ej. válvula mecánica, ETV reciente): considerar puente según protocolo.';
  } else {
    bridge = 'no';
    bridgeNote = 'Riesgo trombótico bajo: no se requiere puente.';
  }

  let guidance: string;
  if (bleeding === 'bajo') {
    guidance =
      'Procedimiento de bajo riesgo hemorrágico: con frecuencia puede mantenerse el antitrombótico.';
  } else if (thrombotic === 'alto') {
    guidance =
      'Alto riesgo hemorrágico + alto riesgo trombótico: suspender el tiempo mínimo necesario y coordinar con el equipo.';
  } else {
    guidance =
      'Alto riesgo hemorrágico + bajo riesgo trombótico: suspender según ficha técnica; reanudar con hemostasia asegurada.';
  }

  return {
    continueIfPossible,
    bridge,
    guidance,
    bridgeNote,
    disclaimer:
      'Los tiempos exactos de suspensión y reinicio se toman del protocolo local y la ficha técnica.',
  };
}

// ===================== 8) Optimización preoperatoria: anemia + ferropenia =====================
//
// El diagnóstico y la derivación viven en un único motor: sección 14 (protocolo CAUSA).

// ===================== 9) Dosis de hierro (Ganzoni + carboximaltosa) =====================

/**
 * Déficit total de hierro de Ganzoni (mg):
 *   peso(kg) × (Hb objetivo − Hb actual)(g/dl) × 2,4 + depósito de reserva (mg).
 * Hb objetivo habitual 15 g/dl; depósito 500 mg (peso ≥ 35 kg).
 */
export function ganzoniIronDeficitMg(
  weightKg: number,
  hbActualGdl: number,
  hbTargetGdl = 15,
  storesMg = 500,
): number {
  const deficit = weightKg * (hbTargetGdl - hbActualGdl) * 2.4 + storesMg;
  return Math.max(0, Math.round(deficit));
}

/**
 * Dosis acumulada simplificada de carboximaltosa férrica (ficha técnica, ≥35 kg).
 * Devuelve null por debajo de 35 kg (usar pauta pediátrica/ponderal).
 */
export function fcmCumulativeDoseMg(weightKg: number, hbGdl: number): number | null {
  if (weightKg < 35) return null;
  const heavy = weightKg >= 70;
  if (hbGdl >= 14) return 500;
  if (hbGdl >= 10) return heavy ? 1500 : 1000;
  return heavy ? 2000 : 1500;
}

/**
 * Hierro sacarosa: 200 mg por sesión a días alternos, sin sobrepasar 600 mg/semana
 * (máx. 3 sesiones/semana). Devuelve el nº de sesiones y semanas para cubrir el déficit.
 */
export function ironSucroseSessions(deficitMg: number): {
  sessionMg: number;
  sessions: number;
  weeks: number;
} {
  const sessionMg = 200;
  const sessions = Math.max(1, Math.ceil(deficitMg / sessionMg));
  const weeks = Math.ceil(sessions / 3);
  return { sessionMg, sessions, weeks };
}

// ===================== 10) EPO / ESA =====================

export interface EpoCandidacy {
  anemia: boolean;
  ironAddressed: boolean; // ferropenia ya tratada/descartada
  weeksToSurgery: number | null;
}

export interface EpoResult {
  candidate: boolean;
  weeklyDoseIU: number; // 600 UI/kg/semana
  reason: string;
}

/** Pauta de epoyetina alfa perioperatoria: 600 UI/kg/semana (con hierro), 3–4 semanas antes. */
export function epoWeeklyDoseIU(weightKg: number): number {
  return Math.round(weightKg * 600);
}

export function assessEpo(input: EpoCandidacy & { weightKg: number }): EpoResult {
  const enoughTime = input.weeksToSurgery != null && input.weeksToSurgery >= 3;
  const candidate = input.anemia && input.ironAddressed && enoughTime;
  let reason: string;
  if (!input.anemia) reason = 'Sin anemia: la ESA no está indicada.';
  else if (!input.ironAddressed)
    reason = 'Trata o descarta primero la ferropenia: la ESA sin hierro suficiente es ineficaz.';
  else if (!enoughTime)
    reason = 'Margen insuficiente: la ESA necesita iniciarse ~3–4 semanas antes de la cirugía.';
  else
    reason =
      'Candidato: anemia con ferropenia ya tratada y ≥3–4 semanas de margen → ESA dosis alta + hierro (preferible IV).';
  return { candidate, weeklyDoseIU: epoWeeklyDoseIU(input.weightKg), reason };
}

// ===================== 11) Concentrado de complejo protrombínico (CCP) =====================
//
// Reversión urgente de AVK con 4F-CCP, dosis dirigida por INR y peso (ficha técnica tipo
// Beriplex/Octaplex/Kcentra), con tope por dosis. Siempre asociar vitamina K.

export interface PccResult {
  iuPerKg: number;
  cap: number;
  totalIU: number;
  capped: boolean;
}

export function pccDoseForAvkReversal(weightKg: number, inr: number): PccResult {
  let iuPerKg: number;
  let cap: number;
  if (inr < 4) {
    iuPerKg = 25;
    cap = 2500;
  } else if (inr <= 6) {
    iuPerKg = 35;
    cap = 3500;
  } else {
    iuPerKg = 50;
    cap = 5000;
  }
  const raw = Math.round(weightKg * iuPerKg);
  const totalIU = Math.min(raw, cap);
  return { iuPerKg, cap, totalIU, capped: raw > cap };
}

// ===================== 12) Fibrinógeno y desmopresina =====================

/** Concentrado de fibrinógeno: 25–50 mg/kg cuando fibrinógeno < 1,5 g/l en sangrado. */
export function fibrinogenConcentrateDoseG(weightKg: number): { minG: number; maxG: number } {
  return {
    minG: Math.round((weightKg * 25) / 100) / 10,
    maxG: Math.round((weightKg * 50) / 100) / 10,
  };
}

/** Desmopresina (DDAVP) 0,3 µg/kg IV en vW respondedora o disfunción plaquetaria. */
export function desmopressinDoseUg(weightKg: number): number {
  return Math.round(weightKg * 0.3 * 10) / 10;
}

/**
 * Factor VII activado recombinante (rFVIIa, NovoSeven). Bolo ponderal en µg.
 * Dosis de referencia 90 µg/kg (hemofilia con inhibidores; repetible cada 2–3 h).
 * El uso como rescate en hemorragia masiva refractaria es FUERA de indicación.
 */
export function rfviiaDoseUg(weightKg: number, doseUgPerKg = 90): number {
  return Math.round(weightKg * doseUgPerKg);
}

// ===================== 13) Antídotos / reversión de anticoagulantes =====================

/**
 * Protamina para heparina NO fraccionada (HNF): 1 mg neutraliza ~100 UI de HNF
 * administradas en la última ~2–3 h. Dosis única máxima recomendada ≈ 50 mg
 * (riesgo de hipotensión/anafilaxia y efecto anticoagulante paradójico a dosis altas).
 */
export function protamineForHeparinMg(heparinUnits: number, maxMg = 50): {
  mg: number;
  capped: boolean;
} {
  const raw = Math.round((heparinUnits / 100) * 10) / 10;
  const mg = Math.min(raw, maxMg);
  return { mg, capped: raw > maxMg };
}

/**
 * Protamina para HBPM (enoxaparina): reversión solo parcial.
 *   < 8 h desde la dosis: 1 mg de protamina por cada 1 mg de enoxaparina.
 *   ≥ 8 h: 0,5 mg por cada 1 mg. (anti-Xa de HBPM solo se neutraliza ~60 %.)
 */
export function protamineForEnoxaparinMg(enoxaparinMg: number, hoursSinceDose: number): number {
  const ratio = hoursSinceDose < 8 ? 1 : 0.5;
  return Math.round(enoxaparinMg * ratio * 10) / 10;
}

export interface AndexanetRegimen {
  level: 'baja' | 'alta';
  bolusMg: number;
  infusionMg: number;
  rationale: string;
}

/**
 * Andexanet alfa (anti-Xa: apixabán/rivaroxabán). Dosis baja vs alta según el
 * fármaco, la dosis y el tiempo desde la última toma (ficha técnica/ANNEXA-4):
 *   BAJA: 400 mg bolo + 480 mg en infusión.
 *   ALTA: 800 mg bolo + 960 mg en infusión.
 * Dosis alta si rivaroxabán >10 mg / apixabán >5 mg Y < 8 h desde la toma.
 */
export function andexanetRegimen(input: {
  drug: 'apixaban' | 'rivaroxaban';
  lastDoseMg: number;
  hoursSinceDose: number;
}): AndexanetRegimen {
  const threshold = input.drug === 'rivaroxaban' ? 10 : 5;
  const highDose = input.lastDoseMg > threshold && input.hoursSinceDose < 8;
  return highDose
    ? {
        level: 'alta',
        bolusMg: 800,
        infusionMg: 960,
        rationale: 'Dosis alta: última toma elevada y < 8 h.',
      }
    : {
        level: 'baja',
        bolusMg: 400,
        infusionMg: 480,
        rationale: 'Dosis baja: dosis estándar/baja o ≥ 8 h desde la toma.',
      };
}

/** Idarucizumab (Praxbind): reversión de dabigatrán, dosis FIJA 5 g (2 × 2,5 g) IV. */
export const IDARUCIZUMAB_DOSE_G = 5;

/**
 * Vitamina K (fitomenadiona) para AVK, según escenario.
 * Texto de referencia; el rango exacto depende del INR y del protocolo local.
 */
export interface VitaminKScenario {
  key: string;
  label: string;
  dose: string;
  note: string;
}

export const VITAMIN_K_SCENARIOS: VitaminKScenario[] = [
  {
    key: 'hemorragia-grave',
    label: 'Hemorragia grave / cirugía urgente',
    dose: '10 mg IV lenta',
    note: 'Asociar SIEMPRE 4F-CCP (efecto inmediato); la vitamina K mantiene la reversión.',
  },
  {
    key: 'inr-alto-sin-sangrado',
    label: 'INR muy alto sin sangrado relevante',
    dose: '1–2 mg vía oral o IV',
    note: 'Evitar dosis altas si se desea reanudar el AVK después.',
  },
  {
    key: 'cirugia-programada',
    label: 'Reversión programada preoperatoria',
    dose: '1–5 mg vía oral 1–3 días antes',
    note: 'Suspender el AVK con antelación; comprobar INR el día previo.',
  },
];

// ===================== 14) Protocolo anemia preoperatoria (CAUSA/SACYL, consenso ES 2024) =====================
//
// Reproduce el algoritmo del PTC-ANR-22-01-01 (18/12/2025): definición por riesgo
// quirúrgico, regla de derivación por IST, y matrices de tratamiento Fe+EPO
// electiva (Figura 12) y urgente con función renal (Figura 13). NO modificar cifras.

/** Riesgo de sangrado quirúrgico: 'alto' = TCH > 10 % o sangrado > 500 ml / > 10 % volemia. */
export type SurgicalBleedingRisk = 'alto' | 'bajo';
export type PreopSex = 'varon' | 'mujer';

/** Umbral de anemia preoperatoria: Hb < 13 indep. del sexo en alto riesgo; OMS en bajo riesgo. */
export function preopAnemiaThreshold(risk: SurgicalBleedingRisk, sex: PreopSex): number {
  if (risk === 'alto') return 13;
  return sex === 'mujer' ? 12 : 13;
}

/** Vial semanal de epoyetina del protocolo: ≥ 55 kg → 40.000 UI; < 55 kg → 30.000 UI. */
export function epoWeeklyVialUI(weightKg: number): number {
  return weightKg >= 55 ? 40000 : 30000;
}

/** Campo de laboratorio tecleado por el usuario: vacío, inválido o valor utilizable. */
export type LabField = { kind: 'vacio' } | { kind: 'invalido' } | { kind: 'ok'; value: number };

/**
 * Lee un valor de laboratorio (admite coma decimal). No numérico, negativo o por encima de `max`
 * → 'invalido': la pantalla debe bloquear el resultado, nunca tratarlo como dato ausente.
 */
export function parseLabField(raw: string, opts: { max?: number } = {}): LabField {
  const s = raw.trim();
  if (s === '') return { kind: 'vacio' };
  const v = Number(s.replace(',', '.'));
  if (!Number.isFinite(v) || v < 0 || (opts.max != null && v > opts.max)) return { kind: 'invalido' };
  return { kind: 'ok', value: v };
}

export function labValue(f: LabField): number | null {
  return f.kind === 'ok' ? f.value : null;
}

/** Nombres de los campos inválidos, en el orden recibido. */
export function invalidLabFields(fields: Record<string, LabField>): string[] {
  return Object.entries(fields)
    .filter(([, f]) => f.kind === 'invalido')
    .map(([name]) => name);
}

/**
 * Regla única de derivación del protocolo: anemia con IST ≥ 20 % → Consultas de
 * M. Interna / Hematología. La consumen el diagnóstico (Fig. 5) y la matriz electiva (Fig. 12).
 */
export function causaDerivar(input: { anemia: boolean; tsat?: number | null }): boolean {
  return input.anemia && input.tsat != null && input.tsat >= 20;
}

/** Clasificación de ferropenia del protocolo (Figura 7, con Ret-Hb opcional). */
export type IronDxCausa = 'DAH' | 'DFH' | 'inflamatoria' | 'normal' | 'indeterminada';

const isValidLab = (v: number | null | undefined) => v == null || (Number.isFinite(v) && v >= 0);

export function ironDiagnosisCausa(input: {
  ferritin: number;
  tsat?: number | null; // IST %
  retHbPg?: number | null;
  pcrMgL?: number | null;
}): IronDxCausa {
  const { ferritin, tsat, retHbPg, pcrMgL } = input;
  // Un dato inválido nunca puede desembocar en "normal" (las pantallas ya lo bloquean antes).
  if (!Number.isFinite(ferritin) || ferritin < 0 || ![tsat, retHbPg, pcrMgL].every(isValidLab)) {
    return 'indeterminada';
  }
  // Déficit absoluto: ferritina < 30.
  if (ferritin < 30) return 'DAH';
  const istBaja = tsat != null && tsat < 20;
  const inflam = pcrMgL != null && pcrMgL > 5;
  // Con IST baja: la Ret-Hb afina (Figura 7) si está disponible.
  if (istBaja) {
    if (retHbPg != null) {
      if (retHbPg < 25) return 'DAH';
      if (retHbPg <= 28) return 'DFH'; // Fig. 7: 25–28 pg, 28 incluido

      return 'normal';
    }
    // Sin Ret-Hb: ferritina 30–100 con IST baja = déficit funcional/inflamatorio.
    if (ferritin <= 100) return 'DFH';
    return 'inflamatoria'; // ferritina > 100 + IST < 20
  }
  if (inflam) return 'inflamatoria';
  return tsat != null ? 'normal' : 'indeterminada';
}

const IRON_DX_LABEL: Record<IronDxCausa, string> = {
  DAH: 'Déficit absoluto de hierro (DAH) → hierro IV',
  DFH: 'Déficit funcional de hierro (DFH) → hierro IV ± EPO',
  inflamatoria: 'Anemia inflamatoria (ferritina alta, IST baja) → EPO ± hierro IV',
  normal: 'Metabolismo férrico normal → considerar otras causas',
  indeterminada: 'Estudio férrico incompleto (falta IST)',
};

/**
 * Texto del diagnóstico. Sin PCR, "normal" solo describe el patrón férrico: la inflamación
 * no se ha evaluado y no puede darse por descartada.
 */
export function ironDxLabel(dx: IronDxCausa, opts: { pcrAportada: boolean }): string {
  if (dx === 'normal' && !opts.pcrAportada) {
    return 'Patrón férrico normal — inflamación no evaluada (PCR no aportada)';
  }
  return IRON_DX_LABEL[dx];
}

export type EpoScheme = 'no' | 'una' | 'dos' | 'reducida';

export interface PreopTreatmentPlan {
  derivar: boolean; // IST ≥ 20 % en electiva → derivar a M. Interna / Hematología
  fueraAlgoritmo: boolean; // sin IST (electiva) o sin IST < 20 % (urgente): no hay pauta del protocolo
  ironMg: number | null; // dosis de hierro IV (mg); null = no pauta de hierro fija
  ironLabel: string;
  epo: EpoScheme;
  epoLabel: string;
  note: string;
}

const EPO_SCHEME_LABEL: Record<EpoScheme, string> = {
  no: 'Sin EPO',
  una: 'EPO 1 dosis',
  dos: 'EPO 2 dosis/semana (días −14 y −7)',
  reducida: 'EPO dosis reducida 10.000 UI/semana (ERC)',
};

/**
 * Plan de tratamiento Fe + EPO preoperatorio del protocolo.
 *  - electiva: matriz Hb (<8 / 8–10 / >10) × ferritina (<30 / 30–300 / >300) [Figura 12];
 *    sin IST → fueraAlgoritmo; IST ≥ 20 % → derivar.
 *  - urgente: matriz ferritina (<30 / 30–100 / >100) × función renal (normal / FG<60) [Figura 13],
 *    solo con IST < 20 %; IST ≥ 20 % o ausente → fueraAlgoritmo, sin pauta.
 * Fe coadyuvante a EPO (ferritina alta): 500 mg si Hb ≤ 10, 200 mg si Hb > 10 (si ferritina < 500).
 */
export function causaPreopPlan(input: {
  setting: 'electiva' | 'urgente';
  hb: number;
  ferritin: number;
  tsat?: number | null;
  renalImpaired?: boolean; // FG < 60 (solo urgente)
}): PreopTreatmentPlan {
  const { setting, hb, ferritin, tsat } = input;
  const coadyuvanteMg = hb <= 10 ? 500 : 200;

  if (setting === 'electiva') {
    // 8.7: IST ≥ 20 % se deriva y la matriz se aplica "con IST < 20 %". Sin IST no se sabe en qué
    // grupo está el paciente: no se pauta.
    if (tsat == null) {
      return {
        derivar: false,
        fueraAlgoritmo: true,
        ironMg: null,
        ironLabel: 'Sin pauta',
        epo: 'no',
        epoLabel: 'Sin pauta',
        note: 'IST necesaria para aplicar la matriz de tratamiento o descartar derivación.',
      };
    }
    // La Figura 12 se aplica a pacientes con anemia; la derivación es la regla única.
    if (causaDerivar({ anemia: true, tsat })) {
      return {
        derivar: true,
        fueraAlgoritmo: false,
        ironMg: null,
        ironLabel: 'No iniciar pauta marcial empírica',
        epo: 'no',
        epoLabel: 'Pendiente de estudio',
        note:
          'IST ≥ 20 % con anemia → DERIVAR a Consultas de M. Interna / Hematología (la anemia no es ferropenia simple).',
      };
    }
    const feLow = ferritin < 30;
    const feMid = ferritin <= 300;
    let ironMg: number | null;
    let epo: EpoScheme;
    let note = '';
    if (hb < 8) {
      if (feLow) {
        ironMg = 1000;
        epo = 'una';
      } else if (feMid) {
        ironMg = 500;
        epo = 'dos';
      } else {
        ironMg = null;
        epo = 'dos';
        note = '± Fe IV si Hb < 8 / ERC / quimioterapia neoadyuvante / síndrome mielodisplásico.';
      }
    } else if (hb <= 10) {
      if (feLow) {
        ironMg = 1000;
        epo = 'no';
      } else if (feMid) {
        ironMg = 500;
        epo = 'no';
      } else {
        ironMg = null;
        epo = 'dos';
        note = '± Fe IV si Hb < 8 / ERC / quimioterapia neoadyuvante / síndrome mielodisplásico.';
      }
    } else {
      // Hb > 10
      if (feLow || feMid) {
        ironMg = 500;
        epo = 'no';
      } else {
        ironMg = null;
        epo = 'no';
        note = 'Ferritina > 300 con Hb > 10: sin pauta marcial ni EPO.';
      }
    }
    return {
      derivar: false,
      fueraAlgoritmo: false,
      ironMg,
      ironLabel: ironMg != null ? `Hierro IV ${ironMg >= 1000 ? `${ironMg / 1000} g` : `${ironMg} mg`}` : 'Sin hierro IV',
      epo,
      epoLabel: EPO_SCHEME_LABEL[epo],
      note,
    };
  }

  // ---- URGENTE (Figura 13): la tabla solo cubre IST < 20 %; bandas ferritina <30 / 30–100 / >100 ----
  // Con IST ≥ 20 % o sin IST el protocolo no da pauta: no se calcula ninguna.
  if (tsat == null || tsat >= 20) {
    return {
      derivar: false,
      fueraAlgoritmo: true,
      ironMg: null,
      ironLabel: 'Sin pauta',
      epo: 'no',
      epoLabel: 'Sin pauta',
      note: 'Fuera del algoritmo de la Figura 13 (requiere IST < 20 %). Valorar individualmente.',
    };
  }
  const renal = input.renalImpaired === true;
  const feLow = ferritin < 30;
  const feMid = ferritin <= 100;
  let ironMg: number | null;
  let epo: EpoScheme;
  let note = 'Administrar YA (día 0) sin condicionar la programación quirúrgica.';

  if (feLow) {
    ironMg = 1000;
    epo = renal ? 'reducida' : 'no';
  } else if (feMid) {
    ironMg = 500;
    epo = renal ? 'reducida' : 'una';
  } else {
    // ferritina > 100: Fe coadyuvante (si ferritina < 500) + EPO
    ironMg = ferritin < 500 ? coadyuvanteMg : null;
    epo = renal ? 'reducida' : 'dos';
    note +=
      ' Fe coadyuvante a EPO (favorecer respuesta, no por déficit absoluto) si ferritina < 500: 500 mg si Hb ≤ 10, 200 mg si Hb > 10.';
  }
  return {
    derivar: false,
    fueraAlgoritmo: false,
    ironMg,
    ironLabel: ironMg != null ? `Hierro IV ${ironMg >= 1000 ? `${ironMg / 1000} g` : `${ironMg} mg`}` : 'Sin hierro IV',
    epo,
    epoLabel: EPO_SCHEME_LABEL[epo],
    note,
  };
}

// ===================== 15) Anemia postoperatoria (Figura 16, CAUSA) =====================
//
// Matriz Hb × ferritina con umbrales de transfusión distintos en cirugía cardíaca
// ("en card"): fila baja Hb < 7 (< 8 card), fila media 7–10 (8–10 card), fila alta > 10.
// El déficit de hierro postoperatorio se define con ferritina postQx < 100 (o < 300 + IST
// < 20 % / Ret-Hb baja; la Fig. 15 lo rotula "< 28 pg"). El criterio diagnóstico de Ret-Hb es
// el de la Figura 7 (25–28 pg, 28 incluido = DFH), implementado en ironDiagnosisCausa; esta
// matriz no usa Ret-Hb. La TCH se decide por clínica, no solo por la cifra.

export interface PostopPlan {
  transfuse: boolean;
  ironLabel: string; // 'Hierro IV 1 g' / '500 mg' / 'Fe oral' / 'Sin hierro'
  ironOral: boolean;
  epoLabel: string; // '' si no procede
  note: string;
}

/**
 * Plan de anemia postoperatoria (Figura 16). weightKg ajusta la dosis alta
 * (1 g → 500 mg si < 50 kg). cardiac eleva el umbral de transfusión de 7 a 8 g/dl.
 */
export function causaPostopPlan(input: {
  cardiac: boolean;
  hb: number;
  ferritin: number;
  weightKg: number;
}): PostopPlan {
  const { cardiac, hb, ferritin, weightKg } = input;
  const lowThreshold = cardiac ? 8 : 7;
  const feLow = ferritin < 100;
  const feMid = ferritin <= 300;
  const highDoseLabel = weightKg < 50 ? 'Hierro IV 500 mg' : 'Hierro IV 1 g';

  // Fila baja → transfusión + hematínicos.
  if (hb < lowThreshold) {
    if (feLow) {
      return {
        transfuse: true,
        ironLabel: highDoseLabel,
        ironOral: false,
        epoLabel: 'EPO 1 dosis',
        note: 'Transfusión guiada por clínica + hematínicos.',
      };
    }
    if (feMid) {
      return {
        transfuse: true,
        ironLabel: 'Hierro IV 500 mg',
        ironOral: false,
        epoLabel: 'EPO 2 dosis (hospital / ambulante)',
        note: 'Transfusión guiada por clínica + hematínicos.',
      };
    }
    return {
      transfuse: true,
      ironLabel: 'Hierro IV solo coadyuvante',
      ironOral: false,
      epoLabel: 'EPO hasta Hb 10',
      note: 'Transfusión guiada por clínica; EPO ± Fe (ferritina > 300).',
    };
  }

  // Fila media (Hb hasta 10).
  if (hb <= 10) {
    if (feLow) {
      return { transfuse: false, ironLabel: highDoseLabel, ironOral: false, epoLabel: '', note: '' };
    }
    if (feMid) {
      return {
        transfuse: false,
        ironLabel: 'Hierro IV 500 mg (o sacarosa 200 mg ×2)',
        ironOral: false,
        epoLabel: '',
        note: '',
      };
    }
    return { transfuse: false, ironLabel: 'Sin tratamiento', ironOral: false, epoLabel: '', note: 'Ferritina > 300: nada.' };
  }

  // Fila alta (Hb > 10).
  if (feLow) {
    return { transfuse: false, ironLabel: 'Hierro oral (1 comp/día)', ironOral: true, epoLabel: '', note: '' };
  }
  return { transfuse: false, ironLabel: 'Sin tratamiento', ironOral: false, epoLabel: '', note: 'Ferritina ≥ 100 con Hb > 10: nada.' };
}
