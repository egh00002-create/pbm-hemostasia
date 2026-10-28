import { useState } from 'react';
import { causaPreopPlan, epoWeeklyVialUI, parseLabField, labValue, invalidLabFields } from '../../lib/calculators';
import { SourceNote } from './SourceNote';
import { ProtocolStamp } from './ProtocolStamp';

export function FeEpoElectivaCalc() {
  const [weight, setWeight] = useState('70');
  const [hb, setHb] = useState('9.5');
  const [ferritin, setFerritin] = useState('60');
  const [tsat, setTsat] = useState('15');

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

  const plan = valid ? causaPreopPlan({ setting: 'electiva', hb: hbV!, ferritin: ferV!, tsat: tsatV }) : null;
  const vialUI = w != null && w > 0 ? epoWeeklyVialUI(w) : null;
  const epoText =
    plan && vialUI != null
      ? plan.epo === 'no'
        ? '—'
        : plan.epo === 'una'
          ? `${vialUI.toLocaleString('es-ES')} UI SC (dosis única)`
          : `${vialUI.toLocaleString('es-ES')} UI/semana SC ×2 (días −14 y −7)`
      : '—';

  return (
    <div className="card">
      <h3>Terapia combinada Fe + EPO — cirugía electiva (Fig. 12)</h3>
      <ProtocolStamp />
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="e12-w">Peso (kg)</label>
          <input id="e12-w" inputMode="decimal" value={weight} onChange={(e) => setWeight(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="e12-hb">Hemoglobina (g/dl)</label>
          <input id="e12-hb" inputMode="decimal" value={hb} onChange={(e) => setHb(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="e12-fer">Ferritina (ng/ml)</label>
          <input id="e12-fer" inputMode="decimal" value={ferritin} onChange={(e) => setFerritin(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="e12-ist">IST / saturación transferrina (%)</label>
          <input id="e12-ist" inputMode="decimal" value={tsat} onChange={(e) => setTsat(e.target.value)} />
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
        ) : plan.derivar ? (
          <div className="result-box" aria-live="polite">
            <span className="big" style={{ fontSize: '1.2rem', color: 'var(--warm)' }}>DERIVAR a M. Interna / Hematología</span>
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
            {plan.epo !== 'no' && (
              <p style={{ margin: '6px 0 0', fontSize: '0.85rem' }}>
                Suplementar Fe carboximaltosa si ferritina &lt; 500 (500 mg si Hb &lt; 10; 200 mg si Hb &gt; 10).
                Suspender EPO al alcanzar Hb &gt; 13 g/dl (&gt; 12 onco). Iniciar ≥ 3 semanas antes.
              </p>
            )}
          </div>
        )
      ) : (
        <p className="source-note" role="status">Introduce peso (&gt; 0), Hb y ferritina.</p>
      )}

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">⚠</span>
        <span>
          Matriz Hb (&lt;8 / 8–10 / &gt;10) × ferritina (&lt;30 / 30–300 / &gt;300) del protocolo. EPO requiere
          consentimiento, control de TA y profilaxis antitrombótica. No sustituye al protocolo vigente.
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'Protocolo anemia perioperatoria PTC-ANR-22-01-01 (CAUSA/SACYL, 2025) — Figura 12' },
          { label: 'Moral V et al. Manejo de la anemia periquirúrgica (Delphi-UCLA). Rev Esp Anestesiol 2024', doi: '10.1016/j.cireng.2024.10.008' },
        ]}
      />
    </div>
  );
}
