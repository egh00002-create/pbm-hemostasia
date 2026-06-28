import { useEffect, useMemo, useRef, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { useData } from '../data/DataContext';
import { AnchorBadge, LevelBadge, CoreBadge } from '../components/Badges';

interface TocEntry {
  id: string;
  text: string;
}

/** Convierte DOIs y PMIDs en enlaces dentro de un contenedor (solo refs). */
function linkifyReferences(root: HTMLElement) {
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  const targets: Text[] = [];
  let node: Node | null;
  while ((node = walker.nextNode())) {
    const t = node as Text;
    if (t.parentElement?.closest('a')) continue;
    if (/10\.\d{4,}\/\S+|PMID\s*\d{5,}/i.test(t.textContent || '')) targets.push(t);
  }
  for (const t of targets) {
    const text = t.textContent || '';
    const frag = document.createDocumentFragment();
    let last = 0;
    const re = /(10\.\d{4,}\/[^\s,;)]+)|PMID\s*(\d{5,9})/gi;
    let m: RegExpExecArray | null;
    while ((m = re.exec(text))) {
      if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      const a = document.createElement('a');
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      if (m[1]) {
        a.href = `https://doi.org/${m[1].replace(/[.,;]$/, '')}`;
        a.textContent = m[0];
      } else {
        a.href = `https://pubmed.ncbi.nlm.nih.gov/${m[2]}/`;
        a.textContent = m[0];
      }
      frag.appendChild(a);
      last = m.index + m[0].length;
    }
    if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
    t.parentNode?.replaceChild(frag, t);
  }
}

export function Reader() {
  const { code } = useParams();
  const { docs, byCode, docTitle } = useData();
  const bodyRef = useRef<HTMLDivElement>(null);
  const [toc, setToc] = useState<TocEntry[]>([]);

  const doc = code ? byCode.get(code) : undefined;

  // Documentos en orden para prev/next.
  const ordered = useMemo(() => docs.map((d) => d.code), [docs]);
  const idx = doc ? ordered.indexOf(doc.code) : -1;
  const prev = idx > 0 ? docs[idx - 1] : null;
  const next = idx >= 0 && idx < docs.length - 1 ? docs[idx + 1] : null;

  useEffect(() => {
    const el = bodyRef.current;
    if (!el || !doc) return;
    // Asignar ids a las secciones y construir el índice lateral.
    const secs = Array.from(el.querySelectorAll<HTMLHeadingElement>('h2.sec'));
    const entries: TocEntry[] = secs.map((h, i) => {
      const id = `sec-${i + 1}`;
      h.id = id;
      return { id, text: h.textContent?.trim() || `Sección ${i + 1}` };
    });
    setToc(entries);
    // Enlazar DOIs/PMID en la bibliografía.
    linkifyReferences(el);
    // Subir al inicio al cambiar de documento.
    window.scrollTo({ top: 0 });
  }, [doc]);

  if (!doc) {
    return (
      <div className="empty" role="alert">
        <h2>Documento no encontrado</h2>
        <p>
          El código <code>{code}</code> no existe. <Link to="/indice">Ir al índice</Link>.
        </p>
      </div>
    );
  }

  const html = doc.coverHtml + doc.bodyHtml + doc.refsHtml;

  return (
    <article>
      <div style={{ marginBottom: 12 }}>
        <Link to="/indice" className="chip">
          ← Índice
        </Link>
      </div>
      <div className="toolbar" aria-hidden="false">
        <AnchorBadge anchor={doc.anchor} />
        <LevelBadge level={doc.level} />
        {doc.core && <CoreBadge />}
      </div>

      <div className={`reader-layout${toc.length > 2 ? ' with-toc' : ''}`}>
        <div>
          {/* Contenido del documento renderizado con los estilos de la serie */}
          <div
            className="doc"
            ref={bodyRef}
            // El contenido procede de app-data (contenido propio de confianza).
            dangerouslySetInnerHTML={{ __html: html }}
          />

          <nav className="reader-nav" aria-label="Navegación entre documentos">
            {prev ? (
              <Link to={`/doc/${prev.code}`} className="card" rel="prev">
                <span className="pc-tag">← Anterior</span>
                <h3 style={{ fontSize: '0.98rem' }}>
                  {prev.code} · {docTitle(prev.code)}
                </h3>
              </Link>
            ) : (
              <span />
            )}
            {next ? (
              <Link
                to={`/doc/${next.code}`}
                className="card"
                rel="next"
                style={{ textAlign: 'right' }}
              >
                <span className="pc-tag">Siguiente →</span>
                <h3 style={{ fontSize: '0.98rem' }}>
                  {next.code} · {docTitle(next.code)}
                </h3>
              </Link>
            ) : (
              <span />
            )}
          </nav>
        </div>

        {toc.length > 2 && (
          <aside className="reader-toc">
            <nav aria-label="Índice del documento">
              <h2>En este documento</h2>
              {toc.map((t) => (
                <a key={t.id} href={`#${t.id}`}>
                  {t.text}
                </a>
              ))}
            </nav>
          </aside>
        )}
      </div>
    </article>
  );
}
