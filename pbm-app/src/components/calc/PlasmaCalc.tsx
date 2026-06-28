import { useState } from 'react';
import { plasmaDose, fibrinogenIndicated } from '../../lib/calculators';
import { SourceNote } from './SourceNote';

export function PlasmaCalc() {
  const [weight, setWeight] = useState('70');
  const [bleeding, setBleeding] = useState(true);
  const [coag, setCoag] = useState(true);
  const [fib, setFib] = useState('1.4');
  const [funcDef, setFuncDef] = useState(false);

  const w = parseFloat(weight.replace(',', '.'));
  const validW = Number.isFinite(w) && w > 0;
  const plasma = validW
    ? plasmaDose({ weightKg: w, activeBleeding: bleeding, coagulopathy: coag })
    : null;

  const fibVal = parseFloat(fib.replace(',', '.'));
  const validFib = Number.isFinite(fibVal) && fibVal >= 0;
  const fibRes = validFib
    ? fibrinogenIndicated({ fibrinogenGl: fibVal, functionalDeficit: funcDef })
    : null;

  return (
    <div className="card">
      <h3>Plasma fresco congelado</h3>
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="pl-w">Peso (kg)</label>
          <input id="pl-w" inputMode="decimal" value={weight} onChange={(e) => setWeight(e.target.value)} />
        </div>
        <div className="field">
          <label>
            <input
              type="checkbox"
              checked={bleeding}
              onChange={(e) => setBleeding(e.target.checked)}
              style={{ minHeight: 'auto', width: 'auto', marginRight: 8 }}
            />
            Sangrado activo / procedimiento invasivo
          </label>
          <label>
            <input
              type="checkbox"
              checked={coag}
              onChange={(e) => setCoag(e.target.checked)}
              style={{ minHeight: 'auto', width: 'auto', marginRight: 8 }}
            />
            Coagulopatía relevante (no solo INR/TTPa leve)
          </label>
        </div>
      </div>

      {plasma && (
        <div className="result-box" aria-live="polite">
          <div className="big" style={{ fontSize: '1.25rem' }}>
            {plasma.indicated ? `${plasma.doseMinMl}–${plasma.doseMaxMl} ml (10–15 ml/kg)` : 'No indicado'}
          </div>
          <p style={{ margin: '6px 0 0', fontSize: '0.9rem' }}>{plasma.message}</p>
        </div>
      )}

      <h4 style={{ marginTop: 16 }}>Fibrinógeno / crioprecipitado</h4>
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="pl-fib">Fibrinógeno (g/L)</label>
          <input id="pl-fib" inputMode="decimal" value={fib} onChange={(e) => setFib(e.target.value)} />
        </div>
        <div className="field">
          <label>
            <input
              type="checkbox"
              checked={funcDef}
              onChange={(e) => setFuncDef(e.target.checked)}
              style={{ minHeight: 'auto', width: 'auto', marginRight: 8 }}
            />
            Déficit funcional (viscoelástica)
          </label>
        </div>
      </div>
      {fibRes && (
        <div className="result-box" aria-live="polite">
          <div className="big" style={{ fontSize: '1.2rem' }}>
            {fibRes.indicated ? 'Reponer fibrinógeno' : 'No reponer'}
          </div>
          <p style={{ margin: '6px 0 0', fontSize: '0.9rem' }}>{fibRes.message}</p>
        </div>
      )}

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>No transfundir plasma por INR/TTPa levemente alterado sin sangrado.</span>
      </p>

      <SourceNote
        sources={[
          { label: 'Green L et al. BSH FFP/cryo. Br J Haematol 2018', doi: '10.1111/bjh.15167' },
          {
            label: 'Kietaibl S et al. ESAIC severe perioperative bleeding 2023',
            doi: '10.1097/EJA.0000000000001803',
          },
        ]}
      />
    </div>
  );
}
