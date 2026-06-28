import { useState } from 'react';
import { plateletDecision, PLATELET_SCENARIOS } from '../../lib/calculators';
import { SourceNote } from './SourceNote';

export function PlateletCalc() {
  const [key, setKey] = useState(PLATELET_SCENARIOS[0].key);
  const [plt, setPlt] = useState('15');

  const pltVal = parseFloat(plt.replace(',', '.'));
  const valid = Number.isFinite(pltVal) && pltVal >= 0;
  const scenario = PLATELET_SCENARIOS.find((s) => s.key === key)!;
  const d = valid ? plateletDecision(key, pltVal) : null;
  const noThreshold = scenario.thresholdK === null;

  return (
    <div className="card">
      <h3>Umbral de transfusión de plaquetas</h3>
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="plt-sc">Escenario</label>
          <select id="plt-sc" value={key} onChange={(e) => setKey(e.target.value)}>
            {PLATELET_SCENARIOS.map((s) => (
              <option key={s.key} value={s.key}>
                {s.label}
              </option>
            ))}
          </select>
        </div>
        {!noThreshold && (
          <div className="field">
            <label htmlFor="plt-v">Plaquetas (×10⁹/L)</label>
            <input id="plt-v" inputMode="decimal" value={plt} onChange={(e) => setPlt(e.target.value)} />
          </div>
        )}
      </div>

      <div className="result-box" aria-live="polite">
        {noThreshold ? (
          <div className="big" style={{ fontSize: '1.25rem', color: 'var(--accent2)' }}>
            No transfundir de forma profiláctica
          </div>
        ) : (
          <div>
            Umbral: <strong>&lt; {scenario.thresholdK} ×10⁹/L</strong>
            {d && (
              <div className="big" style={{ fontSize: '1.25rem', marginTop: 4 }}>
                {d.transfuse ? 'Por debajo → valorar transfusión' : 'Por encima → no transfundir'}
              </div>
            )}
          </div>
        )}
        <p style={{ margin: '8px 0 0', fontSize: '0.9rem' }}>{scenario.note}</p>
      </div>

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>
          No transfundir en cirugía cardiovascular sin sangrado, ni en HIC no quirúrgica con
          plaquetas &gt;100 (incluso con antiagregantes).
        </span>
      </p>

      <SourceNote
        sources={[
          {
            label: 'Metcalf RA et al. Platelet Transfusion (AABB/ICTMG). JAMA 2025',
            doi: '10.1001/jama.2025.7529',
          },
        ]}
      />
    </div>
  );
}
