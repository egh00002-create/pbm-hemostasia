import { useState } from 'react';
import { causaPostopPlan, epoWeeklyVialUI } from '../../lib/calculators';
import { SourceNote } from './SourceNote';
import { ProtocolStamp } from './ProtocolStamp';

export function AnemiaPostopCalc() {
  const [weight, setWeight] = useState('70');
  const [hb, setHb] = useState('8');
  const [ferritin, setFerritin] = useState('80');
  const [cardiac, setCardiac] = useState(false);

  const num = (s: string) => (s.trim() === '' ? null : parseFloat(s.replace(',', '.')));
  const w = num(weight);
  const hbV = num(hb);
  const ferV = num(ferritin);
  const valid = w != null && w > 0 && hbV != null && Number.isFinite(hbV) && ferV != null && Number.isFinite(ferV);

  const plan = valid ? causaPostopPlan({ cardiac, hb: hbV!, ferritin: ferV!, weightKg: w! }) : null;
  const vialUI = w != null && w > 0 ? epoWeeklyVialUI(w) : null;

  return (
    <div className="card">
      <h3>Anemia postoperatoria (Fig. 16)</h3>
      <ProtocolStamp />
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="po-w">Peso (kg)</label>
          <input id="po-w" inputMode="decimal" value={weight} onChange={(e) => setWeight(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="po-hb">Hemoglobina (g/dl)</label>
          <input id="po-hb" inputMode="decimal" value={hb} onChange={(e) => setHb(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="po-fer">Ferritina (ng/ml)</label>
          <input id="po-fer" inputMode="decimal" value={ferritin} onChange={(e) => setFerritin(e.target.value)} />
        </div>
        <div className="field">
          <label>
            <input
              type="checkbox"
              checked={cardiac}
              onChange={(e) => setCardiac(e.target.checked)}
              style={{ minHeight: 'auto', width: 'auto', marginRight: 8 }}
            />
            Cirugía cardíaca (umbral transfusión 8 g/dl)
          </label>
        </div>
      </div>

      {valid && plan ? (
        <div className="result-box" aria-live="polite">
          <div>
            Umbral de transfusión: <strong>Hb &lt; {cardiac ? 8 : 7} g/dl</strong> →{' '}
            {plan.transfuse ? (
              <span className="badge guia">TRANSFUNDIR (guiado por clínica)</span>
            ) : (
              <span style={{ color: 'var(--accent2)' }}>no transfundir solo por la cifra</span>
            )}
          </div>
          <div style={{ marginTop: 8 }}>
            Hierro: <span className="big">{plan.ironLabel}</span>
          </div>
          {plan.epoLabel && (
            <div style={{ marginTop: 6 }}>
              EPO: <span className="big">{plan.epoLabel}</span>
              {vialUI != null && <span className="source-note"> ({vialUI.toLocaleString('es-ES')} UI/sem según peso)</span>}
            </div>
          )}
          {plan.note && <p style={{ margin: '8px 0 0', fontSize: '0.9rem' }}>{plan.note}</p>}
        </div>
      ) : (
        <p className="source-note" role="status">Introduce peso, Hb y ferritina válidos.</p>
      )}

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">⚠</span>
        <span>
          Déficit de hierro postQx: ferritina &lt; 100 (o &lt; 300 + IST &lt; 20% / Ret-Hb &lt; 28 pg). La ferritina
          es reactante de fase aguda tras la cirugía; la Ret-Hb / Delta-He son más fiables (días 4–7). La TCH se
          decide por clínica, con umbral restrictivo.
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'Protocolo anemia perioperatoria PTC-ANR-22-01-01 (CAUSA/SACYL, 2025) — Figura 16' },
        ]}
      />
    </div>
  );
}
