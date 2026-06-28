import { useState } from 'react';
import { ganzoniIronDeficitMg, ironSucroseSessions } from '../../lib/calculators';
import { SourceNote } from './SourceNote';
import { ProtocolStamp } from './ProtocolStamp';

export function IronSucroseCalc() {
  const [weight, setWeight] = useState('70');
  const [hb, setHb] = useState('10');
  const [hbTarget, setHbTarget] = useState('15');

  const num = (s: string) => parseFloat(s.replace(',', '.'));
  const w = num(weight);
  const hbV = num(hb);
  const tgt = num(hbTarget);
  const valid = Number.isFinite(w) && w > 0 && Number.isFinite(hbV) && hbV > 0 && Number.isFinite(tgt) && tgt > hbV;

  const deficit = valid ? ganzoniIronDeficitMg(w, hbV, tgt, 500) : null;
  const plan = deficit != null ? ironSucroseSessions(deficit) : null;

  return (
    <div className="card">
      <h3>Hierro sacarosa — déficit y nº de sesiones</h3>
      <ProtocolStamp />
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="fs-w">Peso (kg)</label>
          <input id="fs-w" inputMode="decimal" value={weight} onChange={(e) => setWeight(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="fs-hb">Hemoglobina actual (g/dl)</label>
          <input id="fs-hb" inputMode="decimal" value={hb} onChange={(e) => setHb(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="fs-tgt">Hemoglobina objetivo (g/dl)</label>
          <input id="fs-tgt" inputMode="decimal" value={hbTarget} onChange={(e) => setHbTarget(e.target.value)} />
        </div>
      </div>

      {valid && deficit != null && plan ? (
        <div className="result-box" aria-live="polite">
          <div>
            Déficit total (Ganzoni): <span className="big">{deficit} mg</span>
          </div>
          <p style={{ margin: '4px 0 0', fontSize: '0.85rem' }}>peso × (Hb objetivo − Hb actual) × 2,4 + 500 mg.</p>
          <div style={{ marginTop: 10 }}>
            Pauta: <span className="big">{plan.sessions} sesiones de 200 mg</span>
            <span className="source-note"> (días alternos, máx. 600 mg/semana → ~{plan.weeks} semana{plan.weeks > 1 ? 's' : ''})</span>
          </div>
        </div>
      ) : (
        <p className="source-note" role="status">Introduce datos válidos (objetivo &gt; Hb actual).</p>
      )}

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">⚠</span>
        <span>
          200 mg/sesión a días alternos sin sobrepasar 600 mg/semana. Preferible en ERC en hemodiálisis (máx. 200
          mg/día) o cuando se requiere dosis test. Requiere más sesiones que la carboximaltosa. No sustituye al
          protocolo vigente.
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'Protocolo anemia perioperatoria PTC-ANR-22-01-01 (CAUSA/SACYL, 2025)' },
          { label: 'Ganzoni AM. Schweiz Med Wochenschr 1970 (fórmula clásica del déficit de hierro)' },
        ]}
      />
    </div>
  );
}
