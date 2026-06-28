import { useState } from 'react';
import { HEMSTOP_ITEMS, hemstopScore } from '../../lib/calculators';
import { SourceNote } from './SourceNote';

export function HemstopCalc() {
  const [answers, setAnswers] = useState<Record<string, boolean>>({});
  const res = hemstopScore(answers);

  const toggle = (key: string, value: boolean) =>
    setAnswers((prev) => ({ ...prev, [key]: value }));

  return (
    <div className="card">
      <h3>Cribado HEMSTOP de riesgo hemorrágico</h3>
      <p className="source-note" style={{ marginTop: 0 }}>
        Responde sí/no a los 7 ítems. ≥2 respuestas afirmativas indican estudio dirigido.
      </p>

      <ul className="clean">
        {HEMSTOP_ITEMS.map((it) => (
          <li
            key={it.key}
            style={{
              display: 'flex',
              gap: 10,
              alignItems: 'center',
              padding: '10px 0',
              borderBottom: '1px solid var(--line)',
            }}
          >
            <span className="code" aria-hidden="true">
              {it.letter}
            </span>
            <span style={{ flex: 1 }}>{it.label}</span>
            <span role="group" aria-label={it.label} style={{ display: 'flex', gap: 6 }}>
              <button
                type="button"
                className={`chip${answers[it.key] === true ? ' active' : ''}`}
                aria-pressed={answers[it.key] === true}
                onClick={() => toggle(it.key, true)}
              >
                Sí
              </button>
              <button
                type="button"
                className={`chip${answers[it.key] === false ? ' active' : ''}`}
                aria-pressed={answers[it.key] === false}
                onClick={() => toggle(it.key, false)}
              >
                No
              </button>
            </span>
          </li>
        ))}
      </ul>

      <div className="result-box" aria-live="polite">
        <div>
          Puntuación: <span className="big">{res.score} / 7</span>
        </div>
        <p
          style={{
            margin: '6px 0 0',
            fontWeight: 600,
            color: res.positive ? 'var(--warm)' : 'var(--accent2)',
          }}
        >
          {res.message}
        </p>
      </div>

      <p className="disclaimer" role="note" style={{ marginTop: 12 }}>
        <span className="ic" aria-hidden="true">
          ⚠
        </span>
        <span>Herramienta de cribado; no sustituye una anamnesis hemorrágica completa.</span>
      </p>

      <SourceNote
        sources={[
          {
            label: 'Bonhomme F et al. HEMSTOP. Can J Anaesth 2016',
            doi: '10.1007/s12630-016-0688-9',
          },
        ]}
      />
    </div>
  );
}
