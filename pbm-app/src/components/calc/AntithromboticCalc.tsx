import { useState } from 'react';
import {
  antithromboticAdvice,
  type ThromboticRisk,
  type BleedingRisk,
} from '../../lib/calculators';
import { SourceNote } from './SourceNote';

const DRUGS = [
  'AAS (ácido acetilsalicílico)',
  'Clopidogrel / prasugrel / ticagrelor',
  'Warfarina / acenocumarol (AVK)',
  'Apixabán / rivaroxabán / edoxabán (ACOD)',
  'Dabigatrán (ACOD)',
  'HBPM a dosis terapéutica',
];

export function AntithromboticCalc() {
  const [drug, setDrug] = useState(DRUGS[0]);
  const [thrombotic, setThrombotic] = useState<ThromboticRisk>('bajo');
  const [bleeding, setBleeding] = useState<BleedingRisk>('alto');
  const [af, setAf] = useState(false);

  const advice = antithromboticAdvice({
    drug,
    thrombotic,
    bleeding,
    isAtrialFibrillation: af,
  });

  return (
    <div className="card">
      <h3>Manejo perioperatorio de antitrombóticos</h3>
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="at-drug">Fármaco</label>
          <select id="at-drug" value={drug} onChange={(e) => setDrug(e.target.value)}>
            {DRUGS.map((d) => (
              <option key={d} value={d}>
                {d}
              </option>
            ))}
          </select>
        </div>
        <div className="field">
          <label htmlFor="at-throm">Riesgo trombótico</label>
          <select
            id="at-throm"
            value={thrombotic}
            onChange={(e) => setThrombotic(e.target.value as ThromboticRisk)}
          >
            <option value="bajo">Bajo</option>
            <option value="alto">Alto</option>
          </select>
        </div>
        <div className="field">
          <label htmlFor="at-bleed">Riesgo hemorrágico del procedimiento</label>
          <select
            id="at-bleed"
            value={bleeding}
            onChange={(e) => setBleeding(e.target.value as BleedingRisk)}
          >
            <option value="bajo">Bajo</option>
            <option value="alto">Alto</option>
          </select>
        </div>
        <div className="field">
          <label>
            <input
              type="checkbox"
              checked={af}
              onChange={(e) => setAf(e.target.checked)}
              style={{ minHeight: 'auto', width: 'auto', marginRight: 8 }}
            />
            Indicación = fibrilación auricular (FA)
          </label>
          <span className="hint">Relevante para la decisión de puente (BRIDGE).</span>
        </div>
      </div>

      <div className="result-box" aria-live="polite">
        <p style={{ marginTop: 0 }}>
          <strong>Recomendación general:</strong> {advice.guidance}
        </p>
        <p style={{ margin: '6px 0' }}>
          <strong>Puente (bridging):</strong>{' '}
          <span
            className={`badge ${advice.bridge === 'no' ? 'meta' : 'eca'}`}
            style={{ marginLeft: 4 }}
          >
            {advice.bridge === 'no' ? 'NO indicado' : 'Considerar'}
          </span>
        </p>
        <p style={{ margin: '6px 0 0', fontSize: '0.9rem' }}>{advice.bridgeNote}</p>
      </div>

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>{advice.disclaimer}</span>
      </p>

      <SourceNote
        sources={[
          { label: 'BRIDGE (Douketis). NEJM 2015', doi: '10.1056/NEJMoa1501035' },
          {
            label: 'Moral V et al. Manejo perioperatorio antitrombóticos. Cir Esp 2024',
            doi: '10.1016/j.cireng.2024.10.008',
          },
        ]}
      />
    </div>
  );
}
