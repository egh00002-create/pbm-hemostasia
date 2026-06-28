import { useState } from 'react';
import { assessEpo, epoWeeklyVialUI } from '../../lib/calculators';
import { SourceNote } from './SourceNote';
import { ProtocolStamp } from './ProtocolStamp';

export function EpoCalc() {
  const [weight, setWeight] = useState('70');
  const [anemia, setAnemia] = useState(true);
  const [ironAddressed, setIronAddressed] = useState(true);
  const [weeks, setWeeks] = useState('4');

  const w = parseFloat(weight.replace(',', '.'));
  const weeksVal = weeks.trim() === '' ? null : parseFloat(weeks.replace(',', '.'));
  const valid = Number.isFinite(w) && w > 0;

  const res = valid
    ? assessEpo({
        weightKg: w,
        anemia,
        ironAddressed,
        weeksToSurgery: weeksVal != null && Number.isFinite(weeksVal) ? weeksVal : null,
      })
    : null;

  return (
    <div className="card">
      <h3>Eritropoyetina (ESA) perioperatoria</h3>
      <ProtocolStamp />
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="epo-w">Peso (kg)</label>
          <input id="epo-w" inputMode="decimal" value={weight} onChange={(e) => setWeight(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="epo-weeks">Semanas hasta la cirugía</label>
          <input id="epo-weeks" inputMode="decimal" value={weeks} onChange={(e) => setWeeks(e.target.value)} />
        </div>
        <div className="field">
          <label>
            <input
              type="checkbox"
              checked={anemia}
              onChange={(e) => setAnemia(e.target.checked)}
              style={{ minHeight: 'auto', width: 'auto', marginRight: 8 }}
            />
            Anemia confirmada
          </label>
          <label>
            <input
              type="checkbox"
              checked={ironAddressed}
              onChange={(e) => setIronAddressed(e.target.checked)}
              style={{ minHeight: 'auto', width: 'auto', marginRight: 8 }}
            />
            Ferropenia ya tratada o descartada
          </label>
        </div>
      </div>

      {res ? (
        <div className="result-box" aria-live="polite">
          <div>
            Pauta del protocolo (CAUSA):{' '}
            <span className="big">{epoWeeklyVialUI(w).toLocaleString('es-ES')} UI/semana SC</span>{' '}
            <span className="source-note">({w >= 55 ? '≥' : '<'} 55 kg)</span>
          </div>
          <p style={{ margin: '4px 0 0', fontSize: '0.85rem' }}>
            1 vial semanal: 40.000 UI si ≥ 55 kg, 30.000 UI si &lt; 55 kg. Iniciar ≥ 3 semanas antes (dosis días −14
            y −7). Suspender al alcanzar Hb &gt; 13 g/dl (&gt; 12 en oncológicos). Asociar SIEMPRE hierro IV.
          </p>
          <p style={{ margin: '4px 0 0', fontSize: '0.8rem', color: 'var(--muted)' }}>
            Alternativa por ficha técnica (epoetina alfa ponderal): {res.weeklyDoseIU.toLocaleString('es-ES')} UI/semana (600 UI/kg).
          </p>
          <div style={{ marginTop: 10 }}>
            {res.candidate ? (
              <span className="big" style={{ fontSize: '1.2rem' }}>
                Candidato a ESA
              </span>
            ) : (
              <span className="big" style={{ fontSize: '1.2rem', color: 'var(--warm)' }}>
                No candidato en este momento
              </span>
            )}
          </div>
          <p style={{ margin: '8px 0 0', fontSize: '0.92rem' }}>{res.reason}</p>
        </div>
      ) : (
        <p className="source-note" role="status">
          Introduce un peso válido.
        </p>
      )}

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>
          La ESA reduce la exposición transfusional, pero sin señal clara de beneficio en mortalidad y con
          riesgo trombótico; precisa consentimiento y profilaxis antitrombótica. Contraindica si TAS &gt; 180 /
          TAD &gt; 100 mmHg o +20% sobre el basal, HTA no controlada o ETV previa.
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'Protocolo anemia perioperatoria PTC-ANR-22-01-01 (CAUSA/SACYL, 2025)' },
          { label: 'Lasocki S et al. ESAs in perioperative anaemia. Best Pract Res Clin Anaesthesiol 2023', doi: '10.1016/j.bpa.2023.10.002' },
          { label: 'Kietaibl S et al. ESAIC guideline. Eur J Anaesthesiol 2023', doi: '10.1097/EJA.0000000000001803' },
        ]}
      />
    </div>
  );
}
