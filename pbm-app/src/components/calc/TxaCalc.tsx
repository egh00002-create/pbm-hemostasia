import { useState } from 'react';
import { TXA_SCENARIOS, TXA_FIXED_MESSAGE, txaScenario } from '../../lib/calculators';
import { SourceNote } from './SourceNote';

export function TxaCalc() {
  const [key, setKey] = useState(TXA_SCENARIOS[0].key);
  const s = txaScenario(key);

  return (
    <div className="card">
      <h3>Ácido tranexámico (TXA) por escenario</h3>
      <div className="field">
        <label htmlFor="txa-sc">Escenario clínico</label>
        <select id="txa-sc" value={key} onChange={(e) => setKey(e.target.value)}>
          {TXA_SCENARIOS.map((x) => (
            <option key={x.key} value={x.key}>
              {x.label}
            </option>
          ))}
        </select>
      </div>

      <div className="result-box" aria-live="polite">
        <div className="big" style={{ fontSize: '1.2rem' }}>
          {s.regimen}
        </div>
        <p style={{ margin: '6px 0 0' }}>
          <strong>Ventana:</strong> {s.window}
        </p>
        {s.caution && (
          <p style={{ margin: '6px 0 0', color: 'var(--warm)' }}>
            <strong>Matiz:</strong> {s.caution}
          </p>
        )}
      </div>

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>
          <strong>{TXA_FIXED_MESSAGE}</strong> Vigilar convulsiones a dosis altas; beneficio
          limitado/ausente en TCE grave (CRASH-3).
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'CRASH-2 (trauma). Lancet 2010', doi: '10.1016/S0140-6736(10)60835-5' },
          { label: 'WOMAN (HPP). Lancet 2017', doi: '10.1016/S0140-6736(17)30638-4' },
          { label: 'CRASH-3 (TCE). Lancet 2019', doi: '10.1016/S0140-6736(19)32233-0' },
          { label: 'ATACAS (cirugía cardíaca). NEJM 2017', doi: '10.1056/NEJMoa1606424' },
        ]}
      />
    </div>
  );
}
