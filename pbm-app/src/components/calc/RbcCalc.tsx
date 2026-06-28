import { useState } from 'react';
import { rbcDecision, RBC_THRESHOLDS, type RbcScenario } from '../../lib/calculators';
import { SourceNote } from './SourceNote';

export function RbcCalc() {
  const [scenario, setScenario] = useState<RbcScenario>('estable');
  const [hb, setHb] = useState('7.5');

  const hbVal = parseFloat(hb.replace(',', '.'));
  const valid = Number.isFinite(hbVal) && hbVal > 0 && hbVal < 25;
  const d = valid ? rbcDecision(scenario, hbVal) : null;
  const t = RBC_THRESHOLDS.find((x) => x.scenario === scenario)!;

  return (
    <div className="card">
      <h3>Umbral de transfusión de hematíes</h3>
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="rbc-sc">Escenario clínico</label>
          <select
            id="rbc-sc"
            value={scenario}
            onChange={(e) => setScenario(e.target.value as RbcScenario)}
          >
            {RBC_THRESHOLDS.map((x) => (
              <option key={x.scenario} value={x.scenario}>
                {x.label}
              </option>
            ))}
          </select>
        </div>
        <div className="field">
          <label htmlFor="rbc-hb">Hemoglobina actual (g/dl)</label>
          <input id="rbc-hb" inputMode="decimal" value={hb} onChange={(e) => setHb(e.target.value)} />
        </div>
      </div>

      <div className="result-box" aria-live="polite">
        <div>
          Umbral: <strong>&lt; {t.thresholdGdl} g/dl</strong>
          {t.liberal && (
            <span className="badge eca" style={{ marginLeft: 8 }}>
              LIBERAL
            </span>
          )}
        </div>
        {d && (
          <div style={{ marginTop: 6 }}>
            {d.transfuse ? (
              <span className="big" style={{ fontSize: '1.3rem' }}>
                Por debajo del umbral → valorar transfusión
              </span>
            ) : (
              <span className="big" style={{ fontSize: '1.3rem', color: 'var(--accent2)' }}>
                Por encima del umbral → no transfundir solo por la cifra
              </span>
            )}
            {d.transfuse && (
              <div className="source-note">
                Estimación: ~{d.unitsToTarget} U para alcanzar el umbral (1 U ≈ +1 g/dl).
              </div>
            )}
          </div>
        )}
        <p style={{ margin: '8px 0 0', fontSize: '0.9rem' }}>{t.note}</p>
      </div>

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>
          Decisión individualizada: síntomas, velocidad del sangrado y comorbilidad mandan sobre
          la cifra aislada. En SCA se favorece umbral liberal (≈10 g/dl).
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'Carson JL et al. AABB RBC Transfusion. JAMA 2023', doi: '10.1001/jama.2023.12914' },
          { label: 'TRICC (Hébert). NEJM 1999', doi: '10.1056/NEJM199902113400601' },
          { label: 'TRISS (Holst). NEJM 2014', doi: '10.1056/NEJMoa1406617' },
          { label: 'REALITY (Ducrocq). JAMA 2021', doi: '10.1001/jama.2021.0135' },
          { label: 'MINT (Carson). NEJM Evid 2024', doi: '10.1056/EVIDoa2400223' },
        ]}
      />
    </div>
  );
}
