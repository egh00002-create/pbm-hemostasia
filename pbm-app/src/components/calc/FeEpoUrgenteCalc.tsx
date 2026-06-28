import { useState } from 'react';
import { causaPreopPlan, epoWeeklyVialUI } from '../../lib/calculators';
import { SourceNote } from './SourceNote';
import { ProtocolStamp } from './ProtocolStamp';

export function FeEpoUrgenteCalc() {
  const [weight, setWeight] = useState('70');
  const [hb, setHb] = useState('9');
  const [ferritin, setFerritin] = useState('60');
  const [renal, setRenal] = useState(false);

  const num = (s: string) => (s.trim() === '' ? null : parseFloat(s.replace(',', '.')));
  const w = num(weight);
  const hbV = num(hb);
  const ferV = num(ferritin);
  const valid = w != null && w > 0 && hbV != null && Number.isFinite(hbV) && ferV != null && Number.isFinite(ferV);

  const plan = valid ? causaPreopPlan({ setting: 'urgente', hb: hbV!, ferritin: ferV!, renalImpaired: renal }) : null;
  const vialUI = w != null && w > 0 ? epoWeeklyVialUI(w) : null;
  const epoText =
    plan && vialUI != null
      ? plan.epo === 'no'
        ? '—'
        : plan.epo === 'reducida'
          ? '10.000 UI/semana SC (ERC)'
          : plan.epo === 'una'
            ? `${vialUI.toLocaleString('es-ES')} UI SC (dosis única)`
            : `${vialUI.toLocaleString('es-ES')} UI/semana SC ×2`
      : '—';

  return (
    <div className="card">
      <h3>Anemia en cirugía urgente / diferida (24–48 h, Fig. 13)</h3>
      <ProtocolStamp />
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="u13-w">Peso (kg)</label>
          <input id="u13-w" inputMode="decimal" value={weight} onChange={(e) => setWeight(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="u13-hb">Hemoglobina (g/dl)</label>
          <input id="u13-hb" inputMode="decimal" value={hb} onChange={(e) => setHb(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="u13-fer">Ferritina (ng/ml)</label>
          <input id="u13-fer" inputMode="decimal" value={ferritin} onChange={(e) => setFerritin(e.target.value)} />
        </div>
        <div className="field">
          <label>
            <input
              type="checkbox"
              checked={renal}
              onChange={(e) => setRenal(e.target.checked)}
              style={{ minHeight: 'auto', width: 'auto', marginRight: 8 }}
            />
            Función renal alterada (FG &lt; 60)
          </label>
        </div>
      </div>

      {valid && plan ? (
        <div className="result-box" aria-live="polite">
          <div>
            Hierro IV:{' '}
            <span className="big">{plan.ironMg != null ? (plan.ironMg >= 1000 ? `${plan.ironMg / 1000} g` : `${plan.ironMg} mg`) : '—'}</span>
            {plan.ironMg != null && <span className="source-note"> (carboximaltosa)</span>}
          </div>
          <div style={{ marginTop: 6 }}>
            EPO: <span className="big">{epoText}</span>
          </div>
          {plan.note && <p style={{ margin: '8px 0 0', fontSize: '0.9rem' }}>{plan.note}</p>}
        </div>
      ) : (
        <p className="source-note" role="status">Introduce peso, Hb y ferritina válidos.</p>
      )}

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">⚠</span>
        <span>
          Requiere IST &lt; 20%. Matriz ferritina (&lt;30 / 30–100 / &gt;100) × función renal. Administrar YA (día 0)
          sin condicionar la programación. EPO reducida 10.000 UI/sem si ERC. No sustituye al protocolo vigente.
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'Protocolo anemia perioperatoria PTC-ANR-22-01-01 (CAUSA/SACYL, 2025) — Figura 13' },
          { label: 'Moral V et al. Manejo de la anemia periquirúrgica (Delphi-UCLA). Rev Esp Anestesiol 2024', doi: '10.1016/j.cireng.2024.10.008' },
        ]}
      />
    </div>
  );
}
