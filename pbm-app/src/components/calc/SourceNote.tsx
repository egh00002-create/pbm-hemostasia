import { DISCLAIMER_TEXT } from '../Disclaimer';

export interface Source {
  label: string;
  doi?: string;
  pmid?: string;
}

/** Pie de fuente + descargo, obligatorio en cada calculadora. */
export function SourceNote({ sources }: { sources: Source[] }) {
  return (
    <p className="source-note">
      <strong>Fuente: </strong>
      {sources.map((s, i) => {
        const url = s.doi
          ? `https://doi.org/${s.doi}`
          : s.pmid
            ? `https://pubmed.ncbi.nlm.nih.gov/${s.pmid}/`
            : null;
        return (
          <span key={i}>
            {i > 0 ? ' · ' : ''}
            {url ? (
              <a href={url} target="_blank" rel="noopener noreferrer">
                {s.label}
              </a>
            ) : (
              s.label
            )}
          </span>
        );
      })}
      <br />
      <em>{DISCLAIMER_TEXT}</em>
    </p>
  );
}
