import { useEffect, useMemo, useState, Fragment } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { useData } from '../data/DataContext';
import {
  parseSegments,
  searchSegments,
  SNIPPET_OPEN,
  SNIPPET_CLOSE,
  type SearchHit,
} from '../lib/search';
import { AnchorBadge } from '../components/Badges';

/** Renderiza un snippet con marcadores 〈〈 〉〉 como <mark>. */
function Snippet({ text }: { text: string }) {
  let open = false;
  const nodes: React.ReactNode[] = [];
  let acc = '';
  let key = 0;
  for (let i = 0; i < text.length; ) {
    if (text.startsWith(SNIPPET_OPEN, i)) {
      if (acc) {
        nodes.push(<Fragment key={key++}>{acc}</Fragment>);
        acc = '';
      }
      open = true;
      i += SNIPPET_OPEN.length;
    } else if (text.startsWith(SNIPPET_CLOSE, i)) {
      if (acc) {
        nodes.push(<mark key={key++}>{acc}</mark>);
        acc = '';
      }
      open = false;
      i += SNIPPET_CLOSE.length;
    } else {
      acc += text[i];
      i += 1;
    }
  }
  if (acc) nodes.push(open ? <mark key={key++}>{acc}</mark> : <Fragment key={key++}>{acc}</Fragment>);
  return <span className="snippet">{nodes}</span>;
}

export function Search() {
  const { contentMd, docTitle, byCode } = useData();
  const [params, setParams] = useSearchParams();
  const [query, setQuery] = useState(params.get('q') ?? '');

  const segments = useMemo(() => parseSegments(contentMd), [contentMd]);

  const hits: SearchHit[] = useMemo(() => {
    if (query.trim().length < 2) return [];
    return searchSegments(segments, docTitle, query);
  }, [segments, docTitle, query]);

  // Sincronizar el query con la URL (sin recargar).
  useEffect(() => {
    const current = params.get('q') ?? '';
    if (query !== current) {
      const t = setTimeout(() => {
        setParams(query.trim() ? { q: query.trim() } : {}, { replace: true });
      }, 250);
      return () => clearTimeout(t);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [query]);

  return (
    <div>
      <section className="page-head">
        <p className="kicker-line">Buscador</p>
        <h1>Búsqueda de texto completo</h1>
        <p>Sobre los títulos y el texto de los 23 documentos.</p>
      </section>

      <div className="searchbar" role="search">
        <span aria-hidden="true">🔍</span>
        <input
          type="search"
          autoFocus
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="p.ej. tranexámico, ferropenia, umbral restrictivo…"
          aria-label="Buscar en toda la serie"
        />
        {query && (
          <button
            type="button"
            className="iconbtn"
            onClick={() => setQuery('')}
            aria-label="Limpiar búsqueda"
          >
            ✕
          </button>
        )}
      </div>

      <p className="source-note" aria-live="polite" style={{ margin: '10px 2px' }}>
        {query.trim().length < 2
          ? 'Escribe al menos 2 caracteres.'
          : `${hits.length} documento${hits.length === 1 ? '' : 's'} con coincidencias.`}
      </p>

      <div>
        {hits.map((h) => {
          const doc = byCode.get(h.code);
          return (
            <Link key={h.code} to={`/doc/${h.code}`} className="search-result">
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, flexWrap: 'wrap' }}>
                <span className="code">{h.code}</span>
                <strong>{h.title}</strong>
                {doc && <AnchorBadge anchor={doc.anchor} />}
              </div>
              <Snippet text={h.snippet} />
            </Link>
          );
        })}
      </div>
    </div>
  );
}
