import { useState } from 'react';
import { causaPreopPlan, epoWeeklyVialUI, parseLabField, labValue, invalidLabFields } from '../../lib/calculators';
import { SourceNote } from './SourceNote';
import { ProtocolStamp } from './ProtocolStamp';

export function FeEpoUrgenteCalc() {
  const [weight, setWeight] = useState('70');
  const [hb, setHb] = useState('9');
  const [ferritin, setFerritin] = useState('60');
  const [tsat, setTsat] = useState('15');
  const [renal, setRenal] = useState(false);

  const fields = {
    Peso: parseLabField(weight),
    Hemoglobina: parseLabField(hb),
    Ferritina: parseLabField(ferritin),
    IST: parseLabField(tsat, { max: 100 }),
  };
  const invalid = invalidLabFields(fields);
  const w = labValue(fields.Peso);
  const hbV = labValue(fields.Hemoglobina);
  const ferV = labValue(fields.Ferritina);
  const tsatV = labValue(fields.IST);
  const valid = invalid.length === 0 && w != null && w > 0 && hbV != null && ferV != null;

  const plan = valid
    ? causaPreopPlan({ setting: 'urgente', hb: hbV!, ferritin: ferV!, tsat: tsatV, renalImpaired: renal })
    : null;
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
          <label htmlFor="u13-ist">IST / saturación transferrina (%)</label>
          <input id="u13-ist" inputMode="decimal" value={tsat} onChange={(e) => setTsat(e.target.value)} />
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

      {invalid.length > 0 ? (
        <p className="source-note" role="alert" style={{ color: 'var(--warm)', fontWeight: 600 }}>
          Valor no válido en: {invalid.join(', ')}. Introduce un número ≥ 0 (IST ≤ 100 %).
        </p>
      ) : valid && plan ? (
        plan.fueraAlgoritmo ? (
          <div className="result-box" aria-live="polite">
            <span className="big" style={{ fontSize: '1.1rem', color: 'var(--warm)' }}>Sin pauta del protocolo</span>
            <p style={{ margin: '6px 0 0', fontSize: '0.9rem' }}>{plan.note}</p>
          </div>
        ) : (
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
        )
      ) : (
        <p className="source-note" role="status">Introduce peso (&gt; 0), Hb y ferritina.</p>
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
