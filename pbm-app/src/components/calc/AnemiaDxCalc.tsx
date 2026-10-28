import { useState } from 'react';
import {
  preopAnemiaThreshold,
  ironDiagnosisCausa,
  ironDxLabel,
  causaDerivar,
  parseLabField,
  labValue,
  invalidLabFields,
  type SurgicalBleedingRisk,
  type PreopSex,
} from '../../lib/calculators';
import { SourceNote } from './SourceNote';
import { ProtocolStamp } from './ProtocolStamp';

export function AnemiaDxCalc() {
  const [sex, setSex] = useState<PreopSex>('mujer');
  const [risk, setRisk] = useState<SurgicalBleedingRisk>('alto');
  const [hb, setHb] = useState('10.5');
  const [ferritin, setFerritin] = useState('60');
  const [tsat, setTsat] = useState('15');
  const [retHb, setRetHb] = useState('');

  const hbF = parseLabField(hb);
  const ferF = parseLabField(ferritin);
  const tsatF = parseLabField(tsat, { max: 100 });
  const retF = parseLabField(retHb);
  const invalid = invalidLabFields({ Hemoglobina: hbF, Ferritina: ferF, IST: tsatF, 'Ret-Hb': retF });
  const hbV = labValue(hbF);
  const ferV = labValue(ferF);
  const tsatV = labValue(tsatF);
  // Esta pantalla no recoge PCR: la inflamación queda sin evaluar.
  const pcrV: number | null = null;

  const threshold = preopAnemiaThreshold(risk, sex);
  const valid = invalid.length === 0 && hbV != null && ferV != null;
  const anemia = valid && hbV! < threshold;
  const dx = valid ? ironDiagnosisCausa({ ferritin: ferV!, tsat: tsatV, retHbPg: labValue(retF), pcrMgL: pcrV }) : null;
  const derivar = valid && causaDerivar({ anemia, tsat: tsatV });

  return (
    <div className="card">
      <h3>Diagnóstico de anemia y ferropenia (Fig. 5/7)</h3>
      <ProtocolStamp />
      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="dx-risk">Riesgo de sangrado quirúrgico</label>
          <select id="dx-risk" value={risk} onChange={(e) => setRisk(e.target.value as SurgicalBleedingRisk)}>
            <option value="alto">Alto (TCH &gt;10% o sangrado &gt;500 ml)</option>
            <option value="bajo">Bajo</option>
          </select>
        </div>
        <div className="field">
          <label htmlFor="dx-sex">Sexo</label>
          <select id="dx-sex" value={sex} onChange={(e) => setSex(e.target.value as PreopSex)}>
            <option value="mujer">Mujer</option>
            <option value="varon">Varón</option>
          </select>
        </div>
        <div className="field">
          <label htmlFor="dx-hb">Hemoglobina (g/dl)</label>
          <input id="dx-hb" inputMode="decimal" value={hb} onChange={(e) => setHb(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="dx-fer">Ferritina (ng/ml)</label>
          <input id="dx-fer" inputMode="decimal" value={ferritin} onChange={(e) => setFerritin(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="dx-ist">IST / saturación transferrina (%)</label>
          <input id="dx-ist" inputMode="decimal" value={tsat} onChange={(e) => setTsat(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="dx-ret">Ret-Hb (pg) — opcional</label>
          <input id="dx-ret" inputMode="decimal" value={retHb} onChange={(e) => setRetHb(e.target.value)} placeholder="afina DAH/DFH" />
        </div>
      </div>

      {invalid.length > 0 ? (
        <p className="source-note" role="alert" style={{ color: 'var(--warm)', fontWeight: 600 }}>
          Valor no válido en: {invalid.join(', ')}. Introduce un número ≥ 0 (IST ≤ 100 %).
        </p>
      ) : valid && dx ? (
        <div className="result-box" aria-live="polite">
          <div>
            Umbral de anemia: <strong>Hb &lt; {threshold} g/dl</strong> →{' '}
            {anemia ? <span className="badge guia">ANEMIA</span> : <span style={{ color: 'var(--accent2)' }}>sin anemia por la cifra</span>}
          </div>
          <div style={{ marginTop: 8 }}>
            Diagnóstico férrico:{' '}
            <span className="big" style={{ fontSize: '1.05rem' }}>
              {ironDxLabel(dx, { pcrAportada: pcrV != null })}
            </span>
          </div>
          {derivar && (
            <p style={{ margin: '10px 0 0', color: 'var(--warm)', fontWeight: 600 }}>
              IST ≥ 20% con anemia → DERIVAR a Consultas de M. Interna / Hematología.
            </p>
          )}
        </div>
      ) : (
        <p className="source-note" role="status">Introduce Hb y ferritina.</p>
      )}

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">⚠</span>
        <span>
          Déficit de hierro preoperatorio: ferritina &lt; 30 (absoluto) o &lt; 100 con IST &lt; 20% (funcional). La
          ferritina es reactante de fase aguda; la Ret-Hb / Delta-He no se afectan por inflamación. No sustituye al
          protocolo vigente.
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'Protocolo anemia perioperatoria PTC-ANR-22-01-01 (CAUSA/SACYL, 2025)' },
          { label: 'Muñoz M et al. Resumen ejecutivo consenso anemia perioperatoria. Rev Clin Esp 2024', doi: '10.1016/j.rce.2024.02.001' },
        ]}
      />
    </div>
  );
}
