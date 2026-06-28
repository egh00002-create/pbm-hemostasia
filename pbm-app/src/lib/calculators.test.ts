import { describe, it, expect } from 'vitest';
import {
  computeMabl,
  nadlerBloodVolumeL,
  rbcDecision,
  plateletDecision,
  plasmaDose,
  fibrinogenIndicated,
  hemstopScore,
  antithromboticAdvice,
  assessPreopAnemia,
  ironStatusOf,
  ganzoniIronDeficitMg,
  fcmCumulativeDoseMg,
  ironSucroseSessions,
  epoWeeklyDoseIU,
  assessEpo,
  pccDoseForAvkReversal,
  fibrinogenConcentrateDoseG,
  desmopressinDoseUg,
  rfviiaDoseUg,
  protamineForHeparinMg,
  protamineForEnoxaparinMg,
  andexanetRegimen,
  IDARUCIZUMAB_DOSE_G,
  preopAnemiaThreshold,
  epoWeeklyVialUI,
  ironDiagnosisCausa,
  causaPreopPlan,
  causaPostopPlan,
} from './calculators';

describe('MABL (Nadler + Gross)', () => {
  // Caso de test del prompt: varón 80 kg, 1,75 m, Hto 42→28%
  // ⇒ VSE ≈ 5,15 L, MABL ≈ 2060 ml.
  it('caso varón 80 kg / 1,75 m / 42→28%', () => {
    const r = computeMabl({
      sex: 'varon',
      weightKg: 80,
      heightM: 1.75,
      htoInitial: 42,
      htoTarget: 28,
    });
    expect(r.bloodVolumeL).toBeCloseTo(5.15, 1);
    // Valor exacto de las fórmulas = 2058,3 ml; el prompt lo aproxima a ≈2060.
    expect(r.mablMl).toBeCloseTo(2058.3, 1);
    expect(Math.round(r.mablMl / 10) * 10).toBe(2060); // redondeo a decenas ⇒ 2060
  });

  it('fórmula de Nadler mujer difiere de varón', () => {
    const v = nadlerBloodVolumeL('varon', 70, 1.7);
    const m = nadlerBloodVolumeL('mujer', 70, 1.7);
    expect(v).not.toBeCloseTo(m, 2);
  });
});

describe('Umbral de hematíes', () => {
  it('estable: transfundir si Hb < 7', () => {
    expect(rbcDecision('estable', 6.5).transfuse).toBe(true);
    expect(rbcDecision('estable', 7.2).transfuse).toBe(false);
  });

  it('SCA usa umbral liberal ≈10 (matiz de honestidad)', () => {
    const d = rbcDecision('sca', 9.5);
    expect(d.threshold.thresholdGdl).toBe(10);
    expect(d.threshold.liberal).toBe(true);
    expect(d.transfuse).toBe(true);
  });

  it('estima unidades a objetivo (1 U ≈ +1 g/dl)', () => {
    expect(rbcDecision('estable', 5).unitsToTarget).toBe(2);
    expect(rbcDecision('estable', 8).unitsToTarget).toBe(0);
  });
});

describe('Plaquetas (AABB/ICTMG 2025)', () => {
  it('profilaxis: transfundir <10', () => {
    expect(plateletDecision('profilaxis', 8).transfuse).toBe(true);
    expect(plateletDecision('profilaxis', 12).transfuse).toBe(false);
  });

  it('escenarios de NO transfusión devuelven null', () => {
    expect(plateletDecision('cardiaca-sin-sangrado', 40).transfuse).toBeNull();
    expect(plateletDecision('hic-no-quirurgica', 130).transfuse).toBeNull();
  });
});

describe('Plasma / fibrinógeno', () => {
  it('plasma solo con sangrado + coagulopatía', () => {
    expect(plasmaDose({ weightKg: 70, activeBleeding: true, coagulopathy: true }).indicated).toBe(
      true,
    );
    expect(
      plasmaDose({ weightKg: 70, activeBleeding: false, coagulopathy: true }).indicated,
    ).toBe(false);
  });

  it('dosis 10–15 ml/kg', () => {
    const r = plasmaDose({ weightKg: 80, activeBleeding: true, coagulopathy: true });
    expect(r.doseMinMl).toBe(800);
    expect(r.doseMaxMl).toBe(1200);
  });

  it('fibrinógeno: reponer si <1,5 g/L o déficit funcional', () => {
    expect(fibrinogenIndicated({ fibrinogenGl: 1.2, functionalDeficit: false }).indicated).toBe(
      true,
    );
    expect(fibrinogenIndicated({ fibrinogenGl: 2.0, functionalDeficit: false }).indicated).toBe(
      false,
    );
    expect(fibrinogenIndicated({ fibrinogenGl: 2.0, functionalDeficit: true }).indicated).toBe(
      true,
    );
  });
});

describe('HEMSTOP', () => {
  it('≥2 ítems → positivo (estudio + hematología)', () => {
    expect(hemstopScore({ hematoma: true, surgery: true }).positive).toBe(true);
    expect(hemstopScore({ hematoma: true }).positive).toBe(false);
    expect(hemstopScore({}).score).toBe(0);
  });
});

describe('Antitrombóticos / BRIDGE', () => {
  it('FA: nunca puente sistemático (matiz BRIDGE)', () => {
    const a = antithromboticAdvice({
      drug: 'Warfarina',
      thrombotic: 'alto',
      bleeding: 'alto',
      isAtrialFibrillation: true,
    });
    expect(a.bridge).toBe('no');
    expect(a.bridgeNote).toMatch(/BRIDGE/);
  });

  it('no-FA con riesgo trombótico alto: considerar puente', () => {
    const a = antithromboticAdvice({
      drug: 'Válvula mecánica',
      thrombotic: 'alto',
      bleeding: 'alto',
      isAtrialFibrillation: false,
    });
    expect(a.bridge).toBe('considerar');
  });

  it('bajo riesgo hemorrágico: puede mantenerse', () => {
    const a = antithromboticAdvice({
      drug: 'AAS',
      thrombotic: 'bajo',
      bleeding: 'bajo',
      isAtrialFibrillation: false,
    });
    expect(a.continueIfPossible).toBe(true);
  });
});

describe('Optimización preoperatoria (anemia + ferropenia)', () => {
  it('umbral OMS por sexo y detección de anemia', () => {
    const r = assessPreopAnemia({ sex: 'varon', hbGdl: 11, ferritin: 20 });
    expect(r.hbThreshold).toBe(13);
    expect(r.anemia).toBe(true);
    const m = assessPreopAnemia({ sex: 'mujer', hbGdl: 12.5, ferritin: 50, tsatPct: 25 });
    expect(m.hbThreshold).toBe(12);
    expect(m.anemia).toBe(false);
  });

  it('ferritina <30 = ferropenia absoluta', () => {
    expect(ironStatusOf({ sex: 'varon', hbGdl: 11, ferritin: 20 })).toBe('absoluta');
  });

  it('30–100 con IST baja o inflamación = funcional', () => {
    expect(
      ironStatusOf({ sex: 'varon', hbGdl: 11, ferritin: 60, tsatPct: 15 }),
    ).toBe('funcional');
    expect(
      ironStatusOf({ sex: 'varon', hbGdl: 11, ferritin: 60, inflammation: true }),
    ).toBe('funcional');
  });

  it('absoluta con margen → oral; con poco tiempo o intolerancia → IV', () => {
    expect(assessPreopAnemia({ sex: 'varon', hbGdl: 11, ferritin: 20, weeksToSurgery: 8 }).route).toBe(
      'oral',
    );
    expect(assessPreopAnemia({ sex: 'varon', hbGdl: 11, ferritin: 20, weeksToSurgery: 2 }).route).toBe(
      'iv',
    );
    expect(
      assessPreopAnemia({ sex: 'varon', hbGdl: 11, ferritin: 20, weeksToSurgery: 8, oralIntolerance: true })
        .route,
    ).toBe('iv');
  });

  it('funcional → IV ± EPO', () => {
    expect(
      assessPreopAnemia({ sex: 'varon', hbGdl: 11, ferritin: 60, tsatPct: 15 }).route,
    ).toBe('iv+epo');
  });
});

describe('Dosis de hierro', () => {
  it('Ganzoni: peso×(Hb objetivo−actual)×2,4 + 500', () => {
    // 70 kg, Hb 10→15: 70*5*2.4 + 500 = 1340 mg
    expect(ganzoniIronDeficitMg(70, 10, 15, 500)).toBe(1340);
  });

  it('carboximaltosa simplificada por peso y Hb', () => {
    expect(fcmCumulativeDoseMg(60, 9)).toBe(1500);
    expect(fcmCumulativeDoseMg(80, 9)).toBe(2000);
    expect(fcmCumulativeDoseMg(60, 11)).toBe(1000);
    expect(fcmCumulativeDoseMg(80, 11)).toBe(1500);
    expect(fcmCumulativeDoseMg(60, 15)).toBe(500);
    expect(fcmCumulativeDoseMg(30, 9)).toBeNull(); // <35 kg
  });

  it('hierro sacarosa: 200 mg/sesión, máx 600/semana', () => {
    // déficit 1340 mg → ceil(1340/200)=7 sesiones → ceil(7/3)=3 semanas
    expect(ironSucroseSessions(1340)).toEqual({ sessionMg: 200, sessions: 7, weeks: 3 });
    expect(ironSucroseSessions(400)).toEqual({ sessionMg: 200, sessions: 2, weeks: 1 });
  });
});

describe('EPO / ESA', () => {
  it('dosis 600 UI/kg/semana', () => {
    expect(epoWeeklyDoseIU(70)).toBe(42000);
  });
  it('candidato solo con anemia + hierro tratado + ≥3 semanas', () => {
    expect(
      assessEpo({ weightKg: 70, anemia: true, ironAddressed: true, weeksToSurgery: 4 }).candidate,
    ).toBe(true);
    expect(
      assessEpo({ weightKg: 70, anemia: true, ironAddressed: true, weeksToSurgery: 1 }).candidate,
    ).toBe(false);
    expect(
      assessEpo({ weightKg: 70, anemia: true, ironAddressed: false, weeksToSurgery: 4 }).candidate,
    ).toBe(false);
  });
});

describe('CCP / fibrinógeno / desmopresina', () => {
  it('CCP por INR y peso con tope', () => {
    const a = pccDoseForAvkReversal(80, 3);
    expect(a.iuPerKg).toBe(25);
    expect(a.totalIU).toBe(2000);
    expect(a.capped).toBe(false);
    const b = pccDoseForAvkReversal(80, 5);
    expect(b.iuPerKg).toBe(35);
    expect(b.totalIU).toBe(2800);
    const c = pccDoseForAvkReversal(120, 7);
    expect(c.iuPerKg).toBe(50);
    expect(c.totalIU).toBe(5000); // 6000 → topado a 5000
    expect(c.capped).toBe(true);
  });

  it('fibrinógeno 25–50 mg/kg', () => {
    const f = fibrinogenConcentrateDoseG(70);
    expect(f.minG).toBeCloseTo(1.8, 1);
    expect(f.maxG).toBeCloseTo(3.5, 1);
  });

  it('desmopresina 0,3 µg/kg', () => {
    expect(desmopressinDoseUg(70)).toBe(21);
  });

  it('rFVIIa 90 µg/kg por defecto (NovoSeven)', () => {
    expect(rfviiaDoseUg(70)).toBe(6300);
    expect(rfviiaDoseUg(80, 90)).toBe(7200);
  });
});

describe('Antídotos / reversión de anticoagulantes', () => {
  it('protamina HNF: 1 mg / 100 UI, topado a 50 mg', () => {
    expect(protamineForHeparinMg(3000).mg).toBe(30);
    expect(protamineForHeparinMg(3000).capped).toBe(false);
    const big = protamineForHeparinMg(8000);
    expect(big.mg).toBe(50);
    expect(big.capped).toBe(true);
  });

  it('protamina enoxaparina: ratio 1 si <8 h, 0,5 si ≥8 h', () => {
    expect(protamineForEnoxaparinMg(80, 4)).toBe(80);
    expect(protamineForEnoxaparinMg(80, 10)).toBe(40);
  });

  it('andexanet: dosis alta si toma elevada y <8 h, si no baja', () => {
    const alta = andexanetRegimen({ drug: 'rivaroxaban', lastDoseMg: 20, hoursSinceDose: 3 });
    expect(alta.level).toBe('alta');
    expect(alta.bolusMg).toBe(800);
    expect(alta.infusionMg).toBe(960);
    const baja = andexanetRegimen({ drug: 'apixaban', lastDoseMg: 5, hoursSinceDose: 3 });
    expect(baja.level).toBe('baja');
    expect(baja.bolusMg).toBe(400);
    const bajaTiempo = andexanetRegimen({ drug: 'rivaroxaban', lastDoseMg: 20, hoursSinceDose: 10 });
    expect(bajaTiempo.level).toBe('baja');
  });

  it('idarucizumab dosis fija 5 g', () => {
    expect(IDARUCIZUMAB_DOSE_G).toBe(5);
  });
});

describe('Protocolo anemia preoperatoria (CAUSA / consenso ES 2024)', () => {
  it('umbral de anemia: Hb<13 indep. sexo en alto riesgo; OMS en bajo', () => {
    expect(preopAnemiaThreshold('alto', 'mujer')).toBe(13);
    expect(preopAnemiaThreshold('alto', 'varon')).toBe(13);
    expect(preopAnemiaThreshold('bajo', 'mujer')).toBe(12);
    expect(preopAnemiaThreshold('bajo', 'varon')).toBe(13);
  });

  it('vial de EPO: ≥55 kg → 40.000; <55 kg → 30.000', () => {
    expect(epoWeeklyVialUI(60)).toBe(40000);
    expect(epoWeeklyVialUI(55)).toBe(40000);
    expect(epoWeeklyVialUI(50)).toBe(30000);
  });

  it('clasificación de ferropenia (Figura 7)', () => {
    expect(ironDiagnosisCausa({ ferritin: 20 })).toBe('DAH');
    expect(ironDiagnosisCausa({ ferritin: 60, tsat: 15 })).toBe('DFH');
    expect(ironDiagnosisCausa({ ferritin: 200, tsat: 15 })).toBe('inflamatoria');
    // Con Ret-Hb afinando (ferritina >30, IST baja)
    expect(ironDiagnosisCausa({ ferritin: 60, tsat: 15, retHbPg: 24 })).toBe('DAH');
    expect(ironDiagnosisCausa({ ferritin: 60, tsat: 15, retHbPg: 26 })).toBe('DFH');
    expect(ironDiagnosisCausa({ ferritin: 60, tsat: 15, retHbPg: 30 })).toBe('normal');
  });

  it('electiva: IST ≥20% → derivar', () => {
    const p = causaPreopPlan({ setting: 'electiva', hb: 10, ferritin: 60, tsat: 25 });
    expect(p.derivar).toBe(true);
    expect(p.ironMg).toBeNull();
  });

  it('electiva: matriz Hb × ferritina (Figura 12)', () => {
    // Hb<8, ferritina<30 → Fe 1g + EPO 1 dosis
    const a = causaPreopPlan({ setting: 'electiva', hb: 7, ferritin: 20, tsat: 10 });
    expect(a.ironMg).toBe(1000);
    expect(a.epo).toBe('una');
    // Hb<8, ferritina 30–300 → Fe 500mg + EPO 2 dosis
    const b = causaPreopPlan({ setting: 'electiva', hb: 7, ferritin: 150, tsat: 10 });
    expect(b.ironMg).toBe(500);
    expect(b.epo).toBe('dos');
    // Hb 8–10, ferritina<30 → Fe 1g, sin EPO
    const c = causaPreopPlan({ setting: 'electiva', hb: 9, ferritin: 20, tsat: 10 });
    expect(c.ironMg).toBe(1000);
    expect(c.epo).toBe('no');
    // Hb>10, ferritina<30 → Fe 500mg
    const d = causaPreopPlan({ setting: 'electiva', hb: 11, ferritin: 20, tsat: 10 });
    expect(d.ironMg).toBe(500);
    expect(d.epo).toBe('no');
    // Hb>10, ferritina>300 → nada
    const e = causaPreopPlan({ setting: 'electiva', hb: 11, ferritin: 400, tsat: 10 });
    expect(e.ironMg).toBeNull();
    expect(e.epo).toBe('no');
  });

  it('urgente: función renal normal vs FG<60 (Figura 13)', () => {
    // Normal, ferritina 30–100 → Fe 500mg + EPO 1 dosis
    const a = causaPreopPlan({ setting: 'urgente', hb: 9, ferritin: 60, tsat: 10 });
    expect(a.ironMg).toBe(500);
    expect(a.epo).toBe('una');
    // FG<60, ferritina<30 → Fe 1g + EPO reducida
    const b = causaPreopPlan({ setting: 'urgente', hb: 9, ferritin: 20, tsat: 10, renalImpaired: true });
    expect(b.ironMg).toBe(1000);
    expect(b.epo).toBe('reducida');
    // Normal, ferritina>100 → EPO 2 dosis + Fe coadyuvante (500 si Hb≤10)
    const c = causaPreopPlan({ setting: 'urgente', hb: 9, ferritin: 150, tsat: 10 });
    expect(c.ironMg).toBe(500);
    expect(c.epo).toBe('dos');
    // Normal, ferritina>100, Hb>10 → Fe coadyuvante 200
    const d = causaPreopPlan({ setting: 'urgente', hb: 11, ferritin: 150, tsat: 10 });
    expect(d.ironMg).toBe(200);
  });

  it('postoperatoria: matriz Hb × ferritina (Figura 16)', () => {
    // Hb<7, ferritina<100 → transfundir + Fe 1g + EPO 1 dosis
    const a = causaPostopPlan({ cardiac: false, hb: 6, ferritin: 50, weightKg: 70 });
    expect(a.transfuse).toBe(true);
    expect(a.ironLabel).toMatch(/1 g/);
    expect(a.epoLabel).toMatch(/1 dosis/);
    // <50 kg baja la dosis alta a 500 mg
    const aLight = causaPostopPlan({ cardiac: false, hb: 6, ferritin: 50, weightKg: 45 });
    expect(aLight.ironLabel).toMatch(/500 mg/);
    // Cirugía cardíaca: umbral de transfusión sube a 8 → Hb 7,5 transfunde
    const card = causaPostopPlan({ cardiac: true, hb: 7.5, ferritin: 50, weightKg: 70 });
    expect(card.transfuse).toBe(true);
    const noCard = causaPostopPlan({ cardiac: false, hb: 7.5, ferritin: 50, weightKg: 70 });
    expect(noCard.transfuse).toBe(false);
    // Hb 7-10, ferritina 100-300 → Fe 500mg, sin transfusión ni EPO
    const b = causaPostopPlan({ cardiac: false, hb: 9, ferritin: 200, weightKg: 70 });
    expect(b.transfuse).toBe(false);
    expect(b.ironLabel).toMatch(/500 mg/);
    expect(b.epoLabel).toBe('');
    // Hb>10, ferritina<100 → hierro oral
    const c = causaPostopPlan({ cardiac: false, hb: 11, ferritin: 50, weightKg: 70 });
    expect(c.ironOral).toBe(true);
    // Hb>10, ferritina>300 → nada
    const d = causaPostopPlan({ cardiac: false, hb: 11, ferritin: 400, weightKg: 70 });
    expect(d.ironLabel).toMatch(/Sin tratamiento/);
  });
});
