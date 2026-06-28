import { useEffect, useMemo, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { useData } from '../data/DataContext';
import { useQuiz } from '../hooks/useQuiz';
import { useProgress } from '../hooks/useProgress';
import { useLocalStorage } from '../hooks/useLocalStorage';
import { MODULES } from '../lib/structure';
import { urlFromRefString } from '../lib/references';
import type { QuizMode } from '../lib/quiz';
import type { QuizHistoryEntry } from '../types';
import { Disclaimer } from '../components/Disclaimer';

const HISTORY_KEY = 'pbm_quiz_history';
const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F'];
const REVIEW_LIMIT = 30; // tope de tarjetas por sesión de repaso
const NEW_LIMIT = 10; // tope de preguntas nuevas por sesión

type QuizApi = ReturnType<typeof useQuiz>;
type ProgressApi = ReturnType<typeof useProgress>;

export function Quiz() {
  const { questions: bank } = useData();
  const quiz = useQuiz(bank);
  const progress = useProgress(bank);

  if (quiz.phase === 'setup') return <Setup quiz={quiz} progress={progress} />;
  if (quiz.phase === 'results') return <Results quiz={quiz} />;
  return <Runner quiz={quiz} progress={progress} />;
}

// ===================== Setup =====================

function Setup({ quiz, progress }: { quiz: QuizApi; progress: ProgressApi }) {
  const { questions: bank, docs, docTitle } = useData();
  const [history] = useLocalStorage<QuizHistoryEntry[]>(HISTORY_KEY, []);

  const [moduleN, setModuleN] = useState<number>(1);
  const [pillarKey, setPillarKey] = useState<string>('Pilar 1');
  const [docCode, setDocCode] = useState<string>(docs[0]?.code ?? 'PBM-01');
  const [level, setLevel] = useState<'basico' | 'avanzado'>('basico');

  const countFor = useMemo(() => {
    const byModule: Record<number, number> = {};
    const byDoc: Record<string, number> = {};
    const byLevel: Record<string, number> = { basico: 0, avanzado: 0 };
    for (const q of bank) {
      byModule[q.module] = (byModule[q.module] ?? 0) + 1;
      byDoc[q.doc] = (byDoc[q.doc] ?? 0) + 1;
      byLevel[q.level] = (byLevel[q.level] ?? 0) + 1;
    }
    return { byModule, byDoc, byLevel };
  }, [bank]);

  const pillarModules = (key: string): number[] => {
    const m = MODULES.find((x) => x.key === key);
    return m ? [m.n] : [];
  };

  const startRapido = () => quiz.start({ kind: 'rapido' }, 'Rápido (10 al azar)');
  const startCompleto = () => quiz.start({ kind: 'completo' }, `Completo (${bank.length})`);
  const startModule = () => {
    const m = MODULES.find((x) => x.n === moduleN);
    quiz.start({ kind: 'modulo', module: moduleN } as QuizMode, `Módulo: ${m?.pillarTag}`);
  };
  const startPillar = () =>
    quiz.start(
      { kind: 'pilar', pillarKey, modules: pillarModules(pillarKey) } as QuizMode,
      `Pilar: ${pillarKey}`,
    );
  const startDoc = () =>
    quiz.start({ kind: 'documento', doc: docCode } as QuizMode, `Documento: ${docCode}`);
  const startLevel = () =>
    quiz.start(
      { kind: 'nivel', level } as QuizMode,
      `Nivel: ${level === 'basico' ? 'Básico' : 'Avanzado'}`,
    );

  const dueIds = progress.due.slice(0, REVIEW_LIMIT);
  const newIds = progress.unseen.slice(0, NEW_LIMIT);
  const startRepaso = () =>
    quiz.start({ kind: 'custom', ids: dueIds } as QuizMode, `Repaso espaciado (${dueIds.length})`);
  const startNuevas = () =>
    quiz.start({ kind: 'custom', ids: newIds } as QuizMode, `Preguntas nuevas (${newIds.length})`);

  return (
    <div>
      <section className="page-head">
        <p className="kicker-line">Evaluación</p>
        <h1>200 preguntas con corrección razonada</h1>
        <p>Elige un modo. Las preguntas y sus opciones se barajan en cada intento.</p>
      </section>

      <Disclaimer />

      <ProgressPanel
        progress={progress}
        dueCount={dueIds.length}
        newCount={newIds.length}
        onRepaso={startRepaso}
        onNuevas={startNuevas}
      />

      <h2 style={{ fontSize: '1.15rem', margin: '22px 0 10px' }}>Modos de práctica</h2>
      <div className="grid cols-2">
        <div className="card">
          <h3>Rápido</h3>
          <p>10 preguntas al azar de toda la serie.</p>
          <button type="button" className="btn btn-primary" onClick={startRapido}>
            Empezar rápido
          </button>
        </div>

        <div className="card">
          <h3>Completo</h3>
          <p>Las {bank.length} preguntas, en orden aleatorio.</p>
          <button type="button" className="btn btn-primary" onClick={startCompleto}>
            Empezar completo
          </button>
        </div>

        <div className="card">
          <h3>Por módulo</h3>
          <div className="field">
            <label htmlFor="q-mod">Módulo</label>
            <select id="q-mod" value={moduleN} onChange={(e) => setModuleN(Number(e.target.value))}>
              {MODULES.map((m) => (
                <option key={m.key} value={m.n}>
                  {m.label} ({countFor.byModule[m.n] ?? 0})
                </option>
              ))}
            </select>
          </div>
          <button type="button" className="btn btn-ghost" onClick={startModule}>
            Empezar
          </button>
        </div>

        <div className="card">
          <h3>Por pilar</h3>
          <div className="field">
            <label htmlFor="q-pil">Pilar / eje</label>
            <select id="q-pil" value={pillarKey} onChange={(e) => setPillarKey(e.target.value)}>
              {MODULES.filter((m) => m.n >= 1).map((m) => (
                <option key={m.key} value={m.key}>
                  {m.pillarTag}
                </option>
              ))}
            </select>
          </div>
          <button type="button" className="btn btn-ghost" onClick={startPillar}>
            Empezar
          </button>
        </div>

        <div className="card">
          <h3>Por documento</h3>
          <div className="field">
            <label htmlFor="q-doc">Documento</label>
            <select id="q-doc" value={docCode} onChange={(e) => setDocCode(e.target.value)}>
              {docs.map((d) => (
                <option key={d.code} value={d.code}>
                  {d.code} · {docTitle(d.code)} ({countFor.byDoc[d.code] ?? 0})
                </option>
              ))}
            </select>
          </div>
          <button type="button" className="btn btn-ghost" onClick={startDoc}>
            Empezar
          </button>
        </div>

        <div className="card">
          <h3>Por nivel</h3>
          <div className="field">
            <label htmlFor="q-lvl">Nivel</label>
            <select
              id="q-lvl"
              value={level}
              onChange={(e) => setLevel(e.target.value as 'basico' | 'avanzado')}
            >
              <option value="basico">Básico ({countFor.byLevel.basico})</option>
              <option value="avanzado">Avanzado ({countFor.byLevel.avanzado})</option>
            </select>
          </div>
          <button type="button" className="btn btn-ghost" onClick={startLevel}>
            Empezar
          </button>
        </div>
      </div>

      {history.length > 0 && <HistoryPanel history={history} />}
    </div>
  );
}

function HistoryPanel({ history }: { history: QuizHistoryEntry[] }) {
  const [, , reset] = useLocalStorage<QuizHistoryEntry[]>(HISTORY_KEY, []);
  const recent = history.slice(-8).reverse();
  return (
    <section style={{ marginTop: 24 }}>
      <div className="toolbar">
        <h2 style={{ fontSize: '1.1rem', margin: 0, flex: 1 }}>Histórico</h2>
        <button type="button" className="chip" onClick={reset}>
          Borrar histórico
        </button>
      </div>
      <ul className="clean">
        {recent.map((h, i) => (
          <li key={i} className="doc-row">
            <span className="t">{h.mode}</span>
            <span className="badges">
              <span className="badge level">
                {h.correct}/{h.total}
              </span>
              <span
                className="badge"
                style={{
                  background:
                    h.percent >= 70 ? '#0e6e6b' : h.percent >= 50 ? 'var(--accent2)' : 'var(--warm)',
                }}
              >
                {h.percent}%
              </span>
            </span>
          </li>
        ))}
      </ul>
    </section>
  );
}

// ===================== Progreso + repaso espaciado =====================

function ProgressPanel({
  progress,
  dueCount,
  newCount,
  onRepaso,
  onNuevas,
}: {
  progress: ProgressApi;
  dueCount: number;
  newCount: number;
  onRepaso: () => void;
  onNuevas: () => void;
}) {
  const { stats, byModule, resetStore } = progress;
  const seenPct = stats.total ? Math.round((stats.seen / stats.total) * 100) : 0;

  return (
    <section
      className="card"
      aria-label="Tu progreso y repaso espaciado"
      style={{ borderTop: '4px solid var(--accent2)' }}
    >
      <div className="toolbar" style={{ marginBottom: 10 }}>
        <h2 style={{ fontSize: '1.15rem', margin: 0, flex: 1 }}>Tu progreso · repaso espaciado</h2>
        {stats.seen > 0 && (
          <button
            type="button"
            className="chip"
            onClick={() => {
              if (confirm('¿Borrar todo el progreso y el repaso espaciado de este navegador?'))
                resetStore();
            }}
          >
            Reiniciar progreso
          </button>
        )}
      </div>

      <p className="source-note" style={{ marginTop: 0 }}>
        Sistema Leitner: cada respuesta programa cuándo conviene repasar esa pregunta. Se guarda
        solo en este navegador.
      </p>

      <div className="stat-grid" style={{ marginBottom: 12 }}>
        <div className="stat">
          <div className="v">{dueCount}</div>
          <div className="l">Para repasar hoy</div>
        </div>
        <div className="stat">
          <div className="v">
            {stats.seen}/{stats.total}
          </div>
          <div className="l">Vistas ({seenPct}%)</div>
        </div>
        <div className="stat">
          <div className="v">{stats.mastered}</div>
          <div className="l">Dominadas</div>
        </div>
        <div className="stat">
          <div className="v">{stats.reps ? `${stats.accuracy}%` : '—'}</div>
          <div className="l">Acierto global</div>
        </div>
      </div>

      <div className="reader-nav" style={{ marginTop: 0 }}>
        <button
          type="button"
          className="btn btn-primary"
          onClick={onRepaso}
          disabled={dueCount === 0}
          title={dueCount === 0 ? 'No hay tarjetas vencidas ahora mismo' : ''}
        >
          {dueCount > 0 ? `Repasar ${dueCount} vencida${dueCount === 1 ? '' : 's'}` : 'Nada que repasar'}
        </button>
        <button
          type="button"
          className="btn btn-ghost"
          onClick={onNuevas}
          disabled={newCount === 0}
          title={newCount === 0 ? 'Ya has visto todas las preguntas' : ''}
        >
          {newCount > 0 ? `${newCount} preguntas nuevas` : 'Sin nuevas'}
        </button>
      </div>

      {stats.seen > 0 && (
        <details style={{ marginTop: 12 }}>
          <summary style={{ cursor: 'pointer', fontWeight: 600 }}>Detalle por módulo</summary>
          <ul className="clean" style={{ marginTop: 8 }}>
            {MODULES.filter((m) => byModule[m.n]).map((m) => {
              const b = byModule[m.n];
              return (
                <li key={m.key} className="doc-row">
                  <span className="t">{m.label}</span>
                  <span className="badges">
                    <span className="badge level">
                      {b.seen}/{b.total} vistas
                    </span>
                    {b.due > 0 && (
                      <span className="badge" style={{ background: 'var(--warm)' }}>
                        {b.due} pend.
                      </span>
                    )}
                    {b.mastered > 0 && (
                      <span className="badge" style={{ background: '#0e6e6b' }}>
                        {b.mastered} ✓
                      </span>
                    )}
                  </span>
                </li>
              );
            })}
          </ul>
        </details>
      )}
    </section>
  );
}

// ===================== Runner =====================

function Runner({ quiz, progress }: { quiz: QuizApi; progress: ProgressApi }) {
  const { refByPmid } = useData();
  const q = quiz.current;
  if (!q) return null;
  const answered = quiz.selected !== null;
  const total = quiz.questions.length;
  const isLast = quiz.index === total - 1;
  const allAnswered = quiz.answeredCount === total;
  const sourceUrl = urlFromRefString(q.ref, refByPmid);

  return (
    <div>
      <div className="toolbar">
        <button type="button" className="chip" onClick={quiz.reset}>
          ← Salir
        </button>
        <span style={{ flex: 1 }} />
        <span className="badge level">{q.doc}</span>
        <span className="badge level">{q.level === 'basico' ? 'Básico' : 'Avanzado'}</span>
      </div>

      <div className="progress" aria-hidden="true">
        <span style={{ width: `${((quiz.index + 1) / total) * 100}%` }} />
      </div>
      <p className="source-note" aria-live="polite" style={{ margin: '6px 2px 14px' }}>
        Pregunta {quiz.index + 1} de {total} · {quiz.answeredCount} contestadas
      </p>

      <div className="card">
        <h2 style={{ fontSize: '1.15rem', marginTop: 0 }}>{q.q}</h2>

        <div role="group" aria-label="Opciones de respuesta">
          {q.options.map((opt, i) => {
            let cls = 'opt';
            if (answered) {
              if (i === q.answer) cls += ' correct';
              else if (i === quiz.selected) cls += ' wrong';
            }
            return (
              <button
                key={i}
                type="button"
                className={cls}
                disabled={answered}
                aria-pressed={quiz.selected === i}
                onClick={() => {
                  if (answered) return;
                  quiz.answer(i);
                  // Registrar el resultado en la repetición espaciada (una vez por pregunta).
                  progress.recordAnswer(q.id, i === q.answer);
                }}
              >
                <span className="mark" aria-hidden="true">
                  {answered && i === q.answer ? '✓' : answered && i === quiz.selected ? '✗' : LETTERS[i]}
                </span>
                <span>{opt}</span>
              </button>
            );
          })}
        </div>

        {answered && (
          <div className="explain" role="region" aria-label="Explicación">
            <p style={{ marginTop: 0 }}>
              <strong>
                {quiz.selected === q.answer ? '✓ Correcto. ' : '✗ Incorrecto. '}
              </strong>
              {q.explanation}
            </p>
            <p className="source-note" style={{ marginBottom: 0 }}>
              Fuente:{' '}
              {sourceUrl ? (
                <a href={sourceUrl} target="_blank" rel="noopener noreferrer">
                  {q.ref}
                </a>
              ) : (
                q.ref
              )}{' '}
              · <Link to={`/doc/${q.doc}`}>Repasar {q.doc}</Link>
            </p>
          </div>
        )}
      </div>

      <div className="reader-nav">
        <button
          type="button"
          className="btn btn-ghost"
          onClick={quiz.prev}
          disabled={quiz.index === 0}
        >
          ← Anterior
        </button>
        {isLast ? (
          <button
            type="button"
            className="btn btn-primary"
            onClick={() => quiz.finish()}
            disabled={!allAnswered}
            title={allAnswered ? '' : 'Contesta todas para ver el resultado'}
          >
            Ver resultado
          </button>
        ) : (
          <button type="button" className="btn btn-primary" onClick={quiz.next}>
            Siguiente →
          </button>
        )}
      </div>

      {isLast && !allAnswered && (
        <p className="source-note" style={{ textAlign: 'center' }}>
          Te quedan {total - quiz.answeredCount} preguntas sin contestar.
        </p>
      )}
    </div>
  );
}

// ===================== Results =====================

function Results({ quiz }: { quiz: QuizApi }) {
  const { refByPmid, docTitle } = useData();
  const [, setHistory] = useLocalStorage<QuizHistoryEntry[]>(HISTORY_KEY, []);
  const s = quiz.score!;
  const savedRef = useRef(false);

  // Guardar en histórico una sola vez al montar la pantalla de resultados.
  useEffect(() => {
    if (savedRef.current) return;
    savedRef.current = true;
    const entry: QuizHistoryEntry = {
      date: Date.now(),
      mode: quiz.modeLabel,
      total: s.total,
      correct: s.correct,
      percent: s.percent,
    };
    setHistory((prev) => [...prev.slice(-49), entry]);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const wrong = quiz.questions
    .map((q, i) => ({ q, chosen: quiz.answers[i] }))
    .filter(({ q, chosen }) => chosen !== q.answer);

  return (
    <div>
      <section className="page-head">
        <p className="kicker-line">Resultado · {quiz.modeLabel}</p>
        <h1>
          {s.correct} / {s.total} aciertos ({s.percent}%)
        </h1>
      </section>

      <div className="stat-grid" style={{ marginBottom: 18 }}>
        <div className="stat">
          <div className="v">{s.percent}%</div>
          <div className="l">Global</div>
        </div>
        <div className="stat">
          <div className="v">
            {s.byLevel.basico.correct}/{s.byLevel.basico.total}
          </div>
          <div className="l">Básico</div>
        </div>
        <div className="stat">
          <div className="v">
            {s.byLevel.avanzado.correct}/{s.byLevel.avanzado.total}
          </div>
          <div className="l">Avanzado</div>
        </div>
      </div>

      <h2 style={{ fontSize: '1.1rem' }}>Por módulo / pilar</h2>
      <ul className="clean" style={{ marginBottom: 18 }}>
        {MODULES.filter((m) => s.byModule[m.n]).map((m) => {
          const b = s.byModule[m.n];
          const pct = b.total ? Math.round((b.correct / b.total) * 100) : 0;
          return (
            <li key={m.key} className="doc-row">
              <span className="t">{m.label}</span>
              <span className="badges">
                <span className="badge level">
                  {b.correct}/{b.total}
                </span>
                <span
                  className="badge"
                  style={{
                    background: pct >= 70 ? '#0e6e6b' : pct >= 50 ? 'var(--accent2)' : 'var(--warm)',
                  }}
                >
                  {pct}%
                </span>
              </span>
            </li>
          );
        })}
      </ul>

      {wrong.length > 0 && (
        <>
          <h2 style={{ fontSize: '1.1rem' }}>Para repasar ({wrong.length})</h2>
          <ul className="clean">
            {wrong.map(({ q, chosen }) => {
              const url = urlFromRefString(q.ref, refByPmid);
              return (
                <li key={q.id} className="card" style={{ marginBottom: 10 }}>
                  <p style={{ marginTop: 0, fontWeight: 600 }}>{q.q}</p>
                  <p style={{ margin: '4px 0', color: 'var(--warm)' }}>
                    Tu respuesta: {chosen !== null ? q.options[chosen] : '— sin contestar'}
                  </p>
                  <p style={{ margin: '4px 0', color: '#0e6e6b' }}>
                    Correcta: {q.options[q.answer]}
                  </p>
                  <p className="source-note" style={{ marginBottom: 0 }}>
                    {q.explanation}
                    <br />
                    <Link to={`/doc/${q.doc}`}>
                      Repasar {q.doc} · {docTitle(q.doc)}
                    </Link>
                    {url && (
                      <>
                        {' · '}
                        <a href={url} target="_blank" rel="noopener noreferrer">
                          {q.ref}
                        </a>
                      </>
                    )}
                  </p>
                </li>
              );
            })}
          </ul>
        </>
      )}

      <div className="reader-nav" style={{ marginTop: 16 }}>
        <button type="button" className="btn btn-ghost" onClick={quiz.reset}>
          ← Otro modo
        </button>
        <button type="button" className="btn btn-primary" onClick={quiz.reset}>
          Hecho
        </button>
      </div>
    </div>
  );
}
