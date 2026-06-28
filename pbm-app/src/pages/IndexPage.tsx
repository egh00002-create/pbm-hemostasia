import { Link, useSearchParams } from 'react-router-dom';
import { useMemo } from 'react';
import { useData } from '../data/DataContext';
import { MODULES } from '../lib/structure';
import { AnchorBadge, LevelBadge, CoreBadge } from '../components/Badges';
import type { PbmDoc } from '../types';

export function IndexPage() {
  const { docs, docTitle } = useData();
  const [params, setParams] = useSearchParams();
  const pilar = params.get('pilar');

  const groups = useMemo(() => {
    return MODULES.map((m) => ({
      module: m,
      docs: docs.filter((d) => d.pillar === m.key),
    })).filter((g) => g.docs.length > 0);
  }, [docs]);

  const visibleGroups = pilar ? groups.filter((g) => g.module.key === pilar) : groups;

  const setFilter = (key: string | null) => {
    if (key) setParams({ pilar: key });
    else setParams({});
  };

  return (
    <div>
      <section className="page-head">
        <p className="kicker-line">Índice maestro</p>
        <h1>La serie por módulos</h1>
        <p>3 pilares + eje de hemostasia + tarjetas quick-reference. ★ = documento núcleo.</p>
      </section>

      <div className="toolbar" role="group" aria-label="Filtrar por pilar/módulo">
        <button
          type="button"
          className={`chip${!pilar ? ' active' : ''}`}
          aria-pressed={!pilar}
          onClick={() => setFilter(null)}
        >
          Todos
        </button>
        {MODULES.map((m) => (
          <button
            key={m.key}
            type="button"
            className={`chip${pilar === m.key ? ' active' : ''}`}
            aria-pressed={pilar === m.key}
            onClick={() => setFilter(m.key)}
          >
            {m.pillarTag}
          </button>
        ))}
      </div>

      {visibleGroups.map((g) => (
        <section className="module-block" key={g.module.key}>
          <h2>{g.module.label}</h2>
          <ul className="clean">
            {g.docs.map((d) => (
              <DocRow key={d.code} doc={d} title={docTitle(d.code)} />
            ))}
          </ul>
        </section>
      ))}
    </div>
  );
}

function DocRow({ doc, title }: { doc: PbmDoc; title: string }) {
  return (
    <li>
      <Link to={`/doc/${doc.code}`} className="doc-row">
        <span className="code">{doc.code}</span>
        <span className="t">
          {doc.core && (
            <span className="star" aria-label="núcleo" title="Documento núcleo">
              ★{' '}
            </span>
          )}
          {title}
        </span>
        <span className="badges">
          <AnchorBadge anchor={doc.anchor} />
          <LevelBadge level={doc.level} />
          {doc.core && <CoreBadge />}
        </span>
      </Link>
    </li>
  );
}
