import { useState } from 'react';
import { ganzoniIronDeficitMg, fcmCumulativeDoseMg } from '../../lib/calculators';
import { SourceNote } from './SourceNote';
import { ProtocolStamp } from './ProtocolStamp';

export function IronCalc() {
  const [weight, setWeight] = useState('70');
  const [hb, setHb] = useState('10');
  const [hbTarget, setHbTarget] = useState('15');

  const w = parseFloat(weight.replace(',', '.'));
  const hbVal = parseFloat(hb.replace(',', '.'));
  const tgt = parseFloat(hbTarget.replace(',', '.'));
  const valid =
    Number.isFinite(w) && w > 0 && Number.isFinite(hbVal) && hbVal > 0 && Number.isFinite(tgt) && tgt > hbVal;

  const ganzoni = valid ? ganzoniIronDeficitMg(w, hbVal, tgt, 500) : null;
  const fcm = Number.isFinite(w) && w > 0 && Number.isFinite(hbVal) && hbVal > 0 ? fcmCumulativeDoseMg(w, hbVal) : null;

  return (
    <div className="card">
      <h3>Hierro carboximaltosa (Ganzoni) — déficit y dosis IV</h3>
      <ProtocolStamp />
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="fe-w">Peso (kg)</label>
          <input id="fe-w" inputMode="decimal" value={weight} onChange={(e) => setWeight(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="fe-hb">Hemoglobina actual (g/dl)</label>
          <input id="fe-hb" inputMode="decimal" value={hb} onChange={(e) => setHb(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="fe-tgt">Hemoglobina objetivo (g/dl)</label>
          <input id="fe-tgt" inputMode="decimal" value={hbTarget} onChange={(e) => setHbTarget(e.target.value)} />
        </div>
      </div>

      <div className="result-box" aria-live="polite">
        <div>
          Déficit total de hierro (Ganzoni):{' '}
          {ganzoni != null ? (
            <span className="big">{ganzoni} mg</span>
          ) : (
            <span className="source-note">objetivo debe ser &gt; Hb actual</span>
          )}
        </div>
        <p style={{ margin: '4px 0 0', fontSize: '0.85rem' }}>
          peso × (Hb objetivo − Hb actual) × 2,4 + 500 mg de depósito.
        </p>
        <div style={{ marginTop: 10 }}>
          Carboximaltosa férrica (dosis acumulada, ficha técnica):{' '}
          {fcm != null ? (
            <span className="big">{fcm} mg</span>
          ) : (
            <span className="source-note">&lt; 35 kg: usar pauta ponderal/pediátrica</span>
          )}
        </div>
        <p style={{ margin: '4px 0 0', fontSize: '0.85rem' }}>
          Máx. semanal 1.000 mg en dosis única (o 20 mg/kg); fraccionar a la 2.ª semana si la dosis total es mayor.
          No exceder 500 mg acumulados si &lt; 35 kg. En ERC en hemodiálisis, máx. 200 mg/día (usar hierro sacarosa).
        </p>

        <div style={{ marginTop: 10 }}>
          <strong>Dilución e infusión (carboximaltosa):</strong>
          {fcm != null && (
            <span className="source-note">
              {' '}
              {fcm <= 200 ? '· tu dosis: 50 ml SF, sin límite de tiempo' : fcm <= 500 ? '· tu dosis: 100 ml SF, ≥ 6 min' : '· tu dosis (fraccionar a ≤1000 mg): 250 ml SF, ≥ 15 min'}
            </span>
          )}
        </div>
        <ul className="clean" style={{ fontSize: '0.85rem', margin: '4px 0 0', paddingLeft: 0 }}>
          <li>100–200 mg → 50 ml SF 0,9% · sin límite de tiempo</li>
          <li>&gt;200–500 mg → 100 ml SF · mínimo 6 min</li>
          <li>&gt;500–1.000 mg → 250 ml SF · mínimo 15 min</li>
        </ul>
      </div>

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>
          El hierro IV es para ferropenia (absoluta o funcional), no para toda anemia. Contraindicado en sobrecarga
          de hierro e infección activa sin control del foco. Vigilar hipofosfatemia con carboximaltosa. Confirmar
          con la ficha técnica y el protocolo local (PTC-ANR-22-01-01).
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'Ganzoni AM. Schweiz Med Wochenschr 1970 (fórmula clásica del déficit de hierro)' },
          { label: 'Ficha técnica carboximaltosa férrica (dosis acumulada por peso/Hb)' },
          { label: 'Kietaibl S et al. ESAIC guideline. Eur J Anaesthesiol 2023', doi: '10.1097/EJA.0000000000001803' },
        ]}
      />
    </div>
  );
}
