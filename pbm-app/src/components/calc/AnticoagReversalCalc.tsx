import { useState } from 'react';
import {
  protamineForHeparinMg,
  protamineForEnoxaparinMg,
  andexanetRegimen,
  IDARUCIZUMAB_DOSE_G,
  VITAMIN_K_SCENARIOS,
} from '../../lib/calculators';
import { SourceNote } from './SourceNote';

type Agent = 'avk' | 'hnf' | 'hbpm' | 'dabigatran' | 'antixa';

const AGENTS: { key: Agent; label: string }[] = [
  { key: 'avk', label: 'AVK (acenocumarol / warfarina)' },
  { key: 'hnf', label: 'Heparina no fraccionada (HNF)' },
  { key: 'hbpm', label: 'HBPM (enoxaparina)' },
  { key: 'dabigatran', label: 'Dabigatrán (anti-IIa)' },
  { key: 'antixa', label: 'Apixabán / rivaroxabán (anti-Xa)' },
];

export function AnticoagReversalCalc() {
  const [agent, setAgent] = useState<Agent>('antixa');

  // AVK
  const [vitkScenario, setVitkScenario] = useState(VITAMIN_K_SCENARIOS[0].key);
  // HNF
  const [heparinUnits, setHeparinUnits] = useState('3000');
  // HBPM
  const [enoxMg, setEnoxMg] = useState('80');
  const [enoxHours, setEnoxHours] = useState('4');
  // anti-Xa
  const [xaDrug, setXaDrug] = useState<'apixaban' | 'rivaroxaban'>('rivaroxaban');
  const [xaDose, setXaDose] = useState('20');
  const [xaHours, setXaHours] = useState('3');

  const num = (s: string) => parseFloat(s.replace(',', '.'));

  return (
    <div className="card">
      <h3>Antídotos / reversión de anticoagulantes</h3>

      <div className="grid cols-2">
        <div className="field">
          <label htmlFor="rev-agent">Anticoagulante a revertir</label>
          <select id="rev-agent" value={agent} onChange={(e) => setAgent(e.target.value as Agent)}>
            {AGENTS.map((a) => (
              <option key={a.key} value={a.key}>
                {a.label}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* ---------- AVK → vitamina K (+ 4F-CCP) ---------- */}
      {agent === 'avk' && (
        <>
          <div className="grid cols-2">
            <div className="field">
              <label htmlFor="rev-vitk">Escenario</label>
              <select id="rev-vitk" value={vitkScenario} onChange={(e) => setVitkScenario(e.target.value)}>
                {VITAMIN_K_SCENARIOS.map((s) => (
                  <option key={s.key} value={s.key}>
                    {s.label}
                  </option>
                ))}
              </select>
            </div>
          </div>
          {(() => {
            const s = VITAMIN_K_SCENARIOS.find((x) => x.key === vitkScenario)!;
            return (
              <div className="result-box" aria-live="polite">
                <div>
                  Vitamina K (fitomenadiona): <span className="big">{s.dose}</span>
                </div>
                <p style={{ margin: '8px 0 0', fontSize: '0.9rem' }}>{s.note}</p>
                <p style={{ margin: '6px 0 0', fontSize: '0.85rem' }}>
                  Reversión inmediata de hemorragia grave: 4F-CCP dirigido por INR y peso (ver «Fármacos
                  hemostáticos»). La vitamina K sola tarda horas.
                </p>
              </div>
            );
          })()}
        </>
      )}

      {/* ---------- HNF → protamina ---------- */}
      {agent === 'hnf' && (
        <>
          <div className="grid cols-2">
            <div className="field">
              <label htmlFor="rev-hnf">HNF administrada en la última ~2–3 h (UI)</label>
              <input id="rev-hnf" inputMode="decimal" value={heparinUnits} onChange={(e) => setHeparinUnits(e.target.value)} />
            </div>
          </div>
          {(() => {
            const u = num(heparinUnits);
            if (!Number.isFinite(u) || u <= 0)
              return <p className="source-note">Introduce las UI de heparina.</p>;
            const r = protamineForHeparinMg(u);
            return (
              <div className="result-box" aria-live="polite">
                <div>
                  Protamina: <span className="big">{r.mg} mg</span>
                  {r.capped && (
                    <span className="badge eca" style={{ marginLeft: 8 }}>
                      TOPADO 50 mg
                    </span>
                  )}
                </div>
                <p style={{ margin: '8px 0 0', fontSize: '0.9rem' }}>
                  1 mg neutraliza ~100 UI de HNF. Infusión IV lenta (riesgo de hipotensión/anafilaxia);
                  a dosis altas, efecto anticoagulante paradójico.
                </p>
              </div>
            );
          })()}
        </>
      )}

      {/* ---------- HBPM → protamina (parcial) ---------- */}
      {agent === 'hbpm' && (
        <>
          <div className="grid cols-2">
            <div className="field">
              <label htmlFor="rev-enox">Enoxaparina de la última dosis (mg)</label>
              <input id="rev-enox" inputMode="decimal" value={enoxMg} onChange={(e) => setEnoxMg(e.target.value)} />
            </div>
            <div className="field">
              <label htmlFor="rev-enoxh">Horas desde la última dosis</label>
              <input id="rev-enoxh" inputMode="decimal" value={enoxHours} onChange={(e) => setEnoxHours(e.target.value)} />
            </div>
          </div>
          {(() => {
            const mg = num(enoxMg);
            const h = num(enoxHours);
            if (!Number.isFinite(mg) || mg <= 0 || !Number.isFinite(h) || h < 0)
              return <p className="source-note">Introduce dosis y horas válidas.</p>;
            const dose = protamineForEnoxaparinMg(mg, h);
            return (
              <div className="result-box" aria-live="polite">
                <div>
                  Protamina: <span className="big">{dose} mg</span>{' '}
                  <span className="badge eca" style={{ marginLeft: 4 }}>
                    REVERSIÓN PARCIAL
                  </span>
                </div>
                <p style={{ margin: '8px 0 0', fontSize: '0.9rem' }}>
                  {h < 8 ? '1 mg por mg de enoxaparina (< 8 h).' : '0,5 mg por mg de enoxaparina (≥ 8 h).'}{' '}
                  La protamina solo neutraliza ~60 % de la actividad anti-Xa de la HBPM.
                </p>
              </div>
            );
          })()}
        </>
      )}

      {/* ---------- Dabigatrán → idarucizumab ---------- */}
      {agent === 'dabigatran' && (
        <div className="result-box" aria-live="polite">
          <div>
            Idarucizumab (Praxbind): <span className="big">{IDARUCIZUMAB_DOSE_G} g IV</span> (2 × 2,5 g)
          </div>
          <p style={{ margin: '8px 0 0', fontSize: '0.9rem' }}>
            Dosis FIJA, no ponderal. Reversión específica e inmediata del dabigatrán. Puede repetirse una
            segunda dosis si reaparece sangrado con coagulación prolongada. Considerar diálisis si no se dispone.
          </p>
        </div>
      )}

      {/* ---------- anti-Xa → andexanet ---------- */}
      {agent === 'antixa' && (
        <>
          <div className="grid cols-2">
            <div className="field">
              <label htmlFor="rev-xadrug">Fármaco</label>
              <select id="rev-xadrug" value={xaDrug} onChange={(e) => setXaDrug(e.target.value as 'apixaban' | 'rivaroxaban')}>
                <option value="rivaroxaban">Rivaroxabán</option>
                <option value="apixaban">Apixabán</option>
              </select>
            </div>
            <div className="field">
              <label htmlFor="rev-xadose">Última dosis (mg)</label>
              <input id="rev-xadose" inputMode="decimal" value={xaDose} onChange={(e) => setXaDose(e.target.value)} />
            </div>
            <div className="field">
              <label htmlFor="rev-xah">Horas desde la última toma</label>
              <input id="rev-xah" inputMode="decimal" value={xaHours} onChange={(e) => setXaHours(e.target.value)} />
            </div>
          </div>
          {(() => {
            const d = num(xaDose);
            const h = num(xaHours);
            if (!Number.isFinite(d) || d <= 0 || !Number.isFinite(h) || h < 0)
              return <p className="source-note">Introduce dosis y horas válidas.</p>;
            const r = andexanetRegimen({ drug: xaDrug, lastDoseMg: d, hoursSinceDose: h });
            return (
              <div className="result-box" aria-live="polite">
                <div>
                  Andexanet alfa (Ondexxya), dosis <strong>{r.level}</strong>:{' '}
                  <span className="big">
                    {r.bolusMg} mg bolo + {r.infusionMg} mg en infusión (2 h)
                  </span>
                </div>
                <p style={{ margin: '8px 0 0', fontSize: '0.9rem' }}>{r.rationale}</p>
                <p style={{ margin: '6px 0 0', fontSize: '0.85rem' }}>
                  Alternativa si no se dispone: 4F-CCP 25–50 UI/kg (uso no específico). Riesgo trombótico tras
                  la reversión: reanudar anticoagulación en cuanto sea seguro.
                </p>
              </div>
            );
          })()}
        </>
      )}

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>
          Las dosis exactas, los topes y los tiempos se confirman con la ficha técnica y el protocolo local.
          Antes de cualquier antídoto: medidas de soporte, control del foco y corrección de la coagulopatía global.
        </span>
      </p>

      <SourceNote
        sources={[
          { label: 'Kietaibl S et al. ESAIC guideline. Eur J Anaesthesiol 2023', doi: '10.1097/EJA.0000000000001803' },
          { label: 'Fichas técnicas: protamina, fitomenadiona, Praxbind (idarucizumab) y Ondexxya (andexanet alfa)' },
        ]}
      />
    </div>
  );
}
