import { useState } from 'react';
import { computeMabl, type Sex } from '../../lib/calculators';
import { SourceNote } from './SourceNote';

export function MablCalc() {
  const [sex, setSex] = useState<Sex>('varon');
  const [weight, setWeight] = useState('80');
  const [height, setHeight] = useState('175');
  const [htoIni, setHtoIni] = useState('42');
  const [htoTarget, setHtoTarget] = useState('28');

  const w = parseFloat(weight.replace(',', '.'));
  const hCm = parseFloat(height.replace(',', '.'));
  const hi = parseFloat(htoIni.replace(',', '.'));
  const ht = parseFloat(htoTarget.replace(',', '.'));
  const valid =
    Number.isFinite(w) && Number.isFinite(hCm) && Number.isFinite(hi) && Number.isFinite(ht) && hCm > 0 && w > 0 && hi > ht;

  const res = valid
    ? computeMabl({ sex, weightKg: w, heightM: hCm / 100, htoInitial: hi, htoTarget: ht })
    : null;

  return (
    <div className="card">
      <h3>Pérdida sanguínea admisible (MABL)</h3>
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="mabl-sex">Sexo</label>
          <select id="mabl-sex" value={sex} onChange={(e) => setSex(e.target.value as Sex)}>
            <option value="varon">Varón</option>
            <option value="mujer">Mujer</option>
          </select>
        </div>
        <div className="field">
          <label htmlFor="mabl-w">Peso (kg)</label>
          <input id="mabl-w" inputMode="decimal" value={weight} onChange={(e) => setWeight(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="mabl-h">Talla (cm)</label>
          <input id="mabl-h" inputMode="decimal" value={height} onChange={(e) => setHeight(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="mabl-hi">Hematocrito inicial (%)</label>
          <input id="mabl-hi" inputMode="decimal" value={htoIni} onChange={(e) => setHtoIni(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="mabl-ht">Hematocrito diana (%)</label>
          <input id="mabl-ht" inputMode="decimal" value={htoTarget} onChange={(e) => setHtoTarget(e.target.value)} />
        </div>
      </div>

      {res ? (
        <div className="result-box" aria-live="polite">
          <div>
            Volumen sanguíneo estimado (Nadler):{' '}
            <strong>{res.bloodVolumeL.toFixed(2)} L</strong> ({Math.round(res.bloodVolumeMl)} ml)
          </div>
          <div style={{ marginTop: 6 }}>
            MABL (Gross): <span className="big">{Math.round(res.mablMl)} ml</span>
          </div>
        </div>
      ) : (
        <p className="source-note" role="status">
          Introduce datos válidos (Hto inicial &gt; Hto diana).
        </p>
      )}

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>Estimación de planificación, no disparador de transfusión.</span>
      </p>

      <SourceNote
        sources={[
          { label: 'Nadler SB, Surgery 1962 (volumen sanguíneo)', pmid: '21936146' },
          { label: 'Gross JB, Anesthesiology 1983 (MABL)', doi: '10.1097/00000542-198303000-00016' },
        ]}
      />
    </div>
  );
}
