import { useState } from 'react';
import {
  pccDoseForAvkReversal,
  fibrinogenConcentrateDoseG,
  desmopressinDoseUg,
  rfviiaDoseUg,
} from '../../lib/calculators';
import { SourceNote } from './SourceNote';

export function HemostaticDrugsCalc() {
  const [weight, setWeight] = useState('80');
  const [inr, setInr] = useState('3');

  const w = parseFloat(weight.replace(',', '.'));
  const inrVal = parseFloat(inr.replace(',', '.'));
  const wValid = Number.isFinite(w) && w > 0;
  const inrValid = Number.isFinite(inrVal) && inrVal > 0;

  const pcc = wValid && inrValid ? pccDoseForAvkReversal(w, inrVal) : null;
  const fib = wValid ? fibrinogenConcentrateDoseG(w) : null;
  const ddavp = wValid ? desmopressinDoseUg(w) : null;
  const rfviia = wValid ? rfviiaDoseUg(w) : null;

  return (
    <div className="card">
      <h3>Fármacos hemostáticos: dosis</h3>
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="hd-w">Peso (kg)</label>
          <input id="hd-w" inputMode="decimal" value={weight} onChange={(e) => setWeight(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="hd-inr">INR (para reversión de AVK)</label>
          <input id="hd-inr" inputMode="decimal" value={inr} onChange={(e) => setInr(e.target.value)} />
        </div>
      </div>

      <div className="result-box" aria-live="polite">
        <div>
          <strong>4F-CCP (reversión urgente de AVK):</strong>{' '}
          {pcc != null ? (
            <>
              <span className="big">{pcc.totalIU.toLocaleString('es-ES')} UI</span> ({pcc.iuPerKg} UI/kg
              {pcc.capped ? `, topado a ${pcc.cap.toLocaleString('es-ES')} UI` : ''})
            </>
          ) : (
            <span className="source-note">introduce peso e INR válidos</span>
          )}
        </div>
        <p style={{ margin: '4px 0 0', fontSize: '0.85rem' }}>
          Dosis dirigida por INR (25 / 35 / 50 UI/kg) y peso. Asociar SIEMPRE vitamina K.
        </p>

        <div style={{ marginTop: 10 }}>
          <strong>Concentrado de fibrinógeno:</strong>{' '}
          {fib != null ? (
            <span className="big">
              {fib.minG}–{fib.maxG} g
            </span>
          ) : (
            <span className="source-note">introduce un peso válido</span>
          )}
        </div>
        <p style={{ margin: '4px 0 0', fontSize: '0.85rem' }}>
          25–50 mg/kg cuando fibrinógeno &lt; 1,5 g/l en sangrado activo (o guiado por viscoelástica).
        </p>

        <div style={{ marginTop: 10 }}>
          <strong>Desmopresina (DDAVP):</strong>{' '}
          {ddavp != null ? (
            <span className="big">{ddavp} µg</span>
          ) : (
            <span className="source-note">introduce un peso válido</span>
          )}
        </div>
        <p style={{ margin: '4px 0 0', fontSize: '0.85rem' }}>
          0,3 µg/kg IV en enfermedad de von Willebrand respondedora o disfunción plaquetaria (urémica,
          por antiagregantes). Vigilar hiponatremia; taquifilaxia con dosis repetidas.
        </p>

        <div style={{ marginTop: 10 }}>
          <strong>rFVIIa (NovoSeven):</strong>{' '}
          {rfviia != null ? (
            <span className="big">{rfviia.toLocaleString('es-ES')} µg</span>
          ) : (
            <span className="source-note">introduce un peso válido</span>
          )}
          {rfviia != null && (
            <span className="badge eca" style={{ marginLeft: 8 }}>
              FUERA DE INDICACIÓN
            </span>
          )}
        </div>
        <p style={{ margin: '4px 0 0', fontSize: '0.85rem' }}>
          90 µg/kg (dosis de referencia en hemofilia con inhibidores, repetible cada 2–3 h). Su uso como
          rescate en hemorragia masiva refractaria es fuera de indicación: NO rutinario y con riesgo trombótico.
        </p>
      </div>

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>
          El rFVIIa (NovoSeven) no es un hemostático de primera línea: antes corregir acidosis, hipotermia,
          calcio, fibrinógeno y plaquetas. Confirmar dosis con la ficha técnica y el protocolo local del
          preparado disponible.
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'Kietaibl S et al. ESAIC guideline. Eur J Anaesthesiol 2023', doi: '10.1097/EJA.0000000000001803' },
          { label: 'Mumford AD et al. BSH guideline (rare bleeding disorders). Br J Haematol 2014', doi: '10.1111/bjh.13058' },
          { label: 'Fichas técnicas de 4F-CCP, fibrinógeno y desmopresina' },
        ]}
      />
    </div>
  );
}
