import { useState } from 'react';
import { Disclaimer } from '../components/Disclaimer';
import { MablCalc } from '../components/calc/MablCalc';
import { RbcCalc } from '../components/calc/RbcCalc';
import { PlateletCalc } from '../components/calc/PlateletCalc';
import { PlasmaCalc } from '../components/calc/PlasmaCalc';
import { TxaCalc } from '../components/calc/TxaCalc';
import { HemstopCalc } from '../components/calc/HemstopCalc';
import { AntithromboticCalc } from '../components/calc/AntithromboticCalc';
import { IronCalc } from '../components/calc/IronCalc';
import { IronSucroseCalc } from '../components/calc/IronSucroseCalc';
import { EpoCalc } from '../components/calc/EpoCalc';
import { HemostaticDrugsCalc } from '../components/calc/HemostaticDrugsCalc';
import { AnticoagReversalCalc } from '../components/calc/AnticoagReversalCalc';
import { AnemiaDxCalc } from '../components/calc/AnemiaDxCalc';
import { FeEpoElectivaCalc } from '../components/calc/FeEpoElectivaCalc';
import { FeEpoUrgenteCalc } from '../components/calc/FeEpoUrgenteCalc';
import { AnemiaPostopCalc } from '../components/calc/AnemiaPostopCalc';

interface Tool {
  key: string;
  title: string;
  desc: string;
  icon: string;
  tint: string; // color del icono (tinte de fondo)
  Comp: () => JSX.Element;
}

const TOOLS: Record<string, Tool> = {
  'anemia-dx': { key: 'anemia-dx', title: 'Diagnóstico de anemia y ferropenia', desc: 'Umbral por riesgo, DAH/DFH y regla de derivación (Fig. 5/7)', icon: '🩸', tint: 'var(--accent-soft)', Comp: AnemiaDxCalc },
  'fe-epo-electiva': { key: 'fe-epo-electiva', title: 'Terapia combinada Fe + EPO', desc: 'Algoritmo Hb × Ferritina — cirugía electiva (Fig. 12)', icon: '📊', tint: 'var(--accent2-soft)', Comp: FeEpoElectivaCalc },
  carboximaltosa: { key: 'carboximaltosa', title: 'Hierro carboximaltosa (Ganzoni)', desc: 'Calcular déficit y dosis IV acumulada', icon: '💊', tint: 'var(--accent2-soft)', Comp: IronCalc },
  sacarosa: { key: 'sacarosa', title: 'Hierro sacarosa', desc: 'Déficit y nº de sesiones (200 mg ×2-3/sem)', icon: '💊', tint: '#E3F0E8', Comp: IronSucroseCalc },
  epo: { key: 'epo', title: 'Indicación EPO', desc: 'Eritropoyetina recombinante: candidatura y pauta', icon: '💉', tint: '#FBE9D8', Comp: EpoCalc },
  hemstop: { key: 'hemstop', title: 'HEMSTOP', desc: 'Cribado de riesgo hemorrágico preoperatorio', icon: '🧪', tint: 'var(--accent-soft)', Comp: HemstopCalc },
  antitromboticos: { key: 'antitromboticos', title: 'Antitrombóticos', desc: 'Manejo perioperatorio + BRIDGE', icon: '🧬', tint: 'var(--accent2-soft)', Comp: AntithromboticCalc },

  mabl: { key: 'mabl', title: 'Pérdida sanguínea máxima permisible', desc: 'MABL — Nadler + fórmula de Gross', icon: '📉', tint: 'var(--accent-soft)', Comp: MablCalc },
  txa: { key: 'txa', title: 'Ácido tranexámico (TXA)', desc: 'Dosis según escenario', icon: '🩹', tint: '#FBE9D8', Comp: TxaCalc },
  hematies: { key: 'hematies', title: 'Umbral de hematíes', desc: 'Umbrales restrictivos por escenario', icon: '🟥', tint: 'var(--accent-soft)', Comp: RbcCalc },
  plaquetas: { key: 'plaquetas', title: 'Plaquetas', desc: 'Umbrales AABB/ICTMG 2025', icon: '🟡', tint: '#FBF3D8', Comp: PlateletCalc },
  plasma: { key: 'plasma', title: 'Plasma / fibrinógeno', desc: 'Indicación y dosis', icon: '💧', tint: 'var(--accent2-soft)', Comp: PlasmaCalc },

  'fe-epo-urgente': { key: 'fe-epo-urgente', title: 'Cirugía urgente (24–48 h)', desc: 'IST × Función renal × Ferritina (Fig. 13)', icon: '⏱️', tint: '#FBF3D8', Comp: FeEpoUrgenteCalc },
  'farmacos-hemostaticos': { key: 'farmacos-hemostaticos', title: 'Fármacos hemostáticos', desc: 'CCP, fibrinógeno, desmopresina y rFVIIa', icon: '⚗️', tint: 'var(--accent-soft)', Comp: HemostaticDrugsCalc },
  'reversion-anticoagulantes': { key: 'reversion-anticoagulantes', title: 'Antídotos anticoagulantes', desc: 'Vit. K, protamina, idarucizumab y andexanet', icon: '🛡️', tint: 'var(--accent2-soft)', Comp: AnticoagReversalCalc },

  postop: { key: 'postop', title: 'Anemia postoperatoria', desc: 'Algoritmo Hb × Ferritina + transfusión (Fig. 16)', icon: '🛌', tint: 'var(--accent2-soft)', Comp: AnemiaPostopCalc },
};

interface Section {
  title: string;
  subtitle: string;
  keys: string[];
}

// Algunas herramientas se cross-listan en varias secciones por aplicar a más de un
// momento asistencial (umbrales de transfusión, TXA, MABL, fármacos hemostáticos).
const SECTIONS: Section[] = [
  {
    title: 'Preoperatorio',
    subtitle: 'Valoración y optimización antes de la cirugía',
    keys: ['anemia-dx', 'fe-epo-electiva', 'carboximaltosa', 'sacarosa', 'epo', 'mabl', 'hemstop', 'antitromboticos'],
  },
  {
    title: 'Intraoperatorio',
    subtitle: 'Minimizar la pérdida y transfundir componentes',
    keys: ['mabl', 'txa', 'hematies', 'plaquetas', 'plasma', 'farmacos-hemostaticos'],
  },
  {
    title: 'Urgencia y hemorragia',
    subtitle: 'Cirugía urgente y manejo del sangrado activo',
    keys: [
      'fe-epo-urgente',
      'txa',
      'farmacos-hemostaticos',
      'reversion-anticoagulantes',
      'hematies',
      'plaquetas',
      'plasma',
    ],
  },
  {
    title: 'Postoperatorio',
    subtitle: 'Anemia tras la cirugía y transfusión',
    keys: ['postop', 'hematies'],
  },
];

export function Calculators() {
  const [active, setActive] = useState<string | null>(null);
  const tool = active ? TOOLS[active] : null;

  if (tool) {
    const Comp = tool.Comp;
    return (
      <div>
        <button type="button" className="calc-back" onClick={() => setActive(null)}>
          ← Calculadoras
        </button>
        <section className="page-head" style={{ marginTop: 4 }}>
          <p className="kicker-line">{tool.desc}</p>
          <h1>{tool.title}</h1>
        </section>
        <Disclaimer />
        <Comp />
      </div>
    );
  }

  return (
    <div>
      <section className="page-head">
        <p className="kicker-line">Calculadoras clínicas</p>
        <h1>Herramientas de cálculo</h1>
        <p>Organizadas por momento asistencial. Valores y fórmulas verificados; cada herramienta muestra su fuente.</p>
      </section>

      <Disclaimer />

      {SECTIONS.map((sec) => (
        <section key={sec.title} className="calc-section">
          <div className="calc-section__head">
            <h2>{sec.title}</h2>
            <p>{sec.subtitle}</p>
          </div>
          <div className="calc-list">
            {sec.keys.map((k) => {
              const t = TOOLS[k];
              return (
                <button key={k} type="button" className="calc-card" onClick={() => setActive(k)}>
                  <span className="calc-card__icon" style={{ background: t.tint }} aria-hidden="true">
                    {t.icon}
                  </span>
                  <span className="calc-card__body">
                    <span className="calc-card__title">{t.title}</span>
                    <span className="calc-card__desc">{t.desc}</span>
                  </span>
                  <span className="calc-card__chevron" aria-hidden="true">
                    ›
                  </span>
                </button>
              );
            })}
          </div>
        </section>
      ))}
    </div>
  );
}
