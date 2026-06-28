import { useNavigate, Link } from 'react-router-dom';
import { useState } from 'react';
import { useData } from '../data/DataContext';
import { useProgress } from '../hooks/useProgress';
import { PILLAR_CARDS } from '../lib/structure';
import { Disclaimer } from '../components/Disclaimer';

export function Home() {
  const { docs, questions } = useData();
  const { due, stats } = useProgress(questions);
  const navigate = useNavigate();
  const [query, setQuery] = useState('');

  const coreDocs = docs.filter((d) => d.core).length;

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    const q = query.trim();
    navigate(q ? `/buscar?q=${encodeURIComponent(q)}` : '/buscar');
  };

  return (
    <div>
      <section className="page-head">
        <p className="kicker-line">Patient Blood Management · serie formativa</p>
        <h1>Hemostasia y Medicina Transfusional Perioperatoria</h1>
        <p>
          Lector de la serie ({docs.length} documentos, {coreDocs} núcleo), calculadoras
          clínicas y evaluación de 200 preguntas. En español, 100% offline.
        </p>
      </section>

      {(due.length > 0 || stats.seen > 0) && (
        <Link
          to="/evaluacion"
          className="card"
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 12,
            marginBottom: 16,
            borderLeft: '4px solid var(--accent2)',
          }}
        >
          <span aria-hidden="true" style={{ fontSize: '1.6rem' }}>
            🔁
          </span>
          <span style={{ flex: 1 }}>
            <strong>
              {due.length > 0
                ? `${due.length} pregunta${due.length === 1 ? '' : 's'} para repasar hoy`
                : 'Repaso al día'}
            </strong>
            <br />
            <span className="brand__sub" style={{ textTransform: 'none', letterSpacing: 0 }}>
              {stats.seen}/{stats.total} vistas · {stats.mastered} dominadas · repetición espaciada
            </span>
          </span>
          <span className="chip" aria-hidden="true">
            Ir →
          </span>
        </Link>
      )}

      <form className="searchbar" role="search" onSubmit={submit} style={{ marginBottom: 18 }}>
        <span aria-hidden="true">🔍</span>
        <input
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Buscar en toda la serie (texto completo)…"
          aria-label="Buscar en toda la serie"
        />
        <button type="submit" className="btn btn-primary" style={{ minWidth: 'auto' }}>
          Buscar
        </button>
      </form>

      <h2 style={{ fontSize: '1.15rem', margin: '6px 0 10px' }}>Los 3 pilares + el eje</h2>
      <div className="grid cols-2">
        {PILLAR_CARDS.map((p) => (
          <Link
            key={p.pillarKey}
            to={`/indice?pilar=${encodeURIComponent(p.pillarKey)}`}
            className={`card pillar-card${p.axis ? ' axis' : ''}`}
          >
            <span className="pc-tag">{p.tag}</span>
            <h3>{p.title}</h3>
            <p>{p.desc}</p>
          </Link>
        ))}
      </div>

      <h2 style={{ fontSize: '1.15rem', margin: '22px 0 10px' }}>Herramientas</h2>
      <div className="grid cols-3">
        <Link to="/indice" className="card">
          <h3>📚 Índice maestro</h3>
          <p>Los 23 documentos por módulo, con ancla de evidencia, nivel y núcleo.</p>
        </Link>
        <Link to="/calculadoras" className="card">
          <h3>🧮 Calculadoras</h3>
          <p>MABL, umbrales de hematíes/plaquetas/plasma, TXA, HEMSTOP, antitrombóticos.</p>
        </Link>
        <Link to="/evaluacion" className="card">
          <h3>✔️ Evaluación</h3>
          <p>200 preguntas con corrección, explicación y fuente. Varios modos.</p>
        </Link>
      </div>

      <div style={{ marginTop: 18 }}>
        <Disclaimer />
      </div>
    </div>
  );
}
