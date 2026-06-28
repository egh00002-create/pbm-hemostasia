import type { PbmReference } from '../types';

/** Extrae el PMID numérico de un campo ref tipo "PMID 30860564". */
export function pmidFromRef(ref: string): string | null {
  const m = ref.match(/(\d{5,9})/);
  return m ? m[1] : null;
}

/** Construye un índice PMID -> referencia. */
export function indexByPmid(refs: PbmReference[]): Map<string, PbmReference> {
  const map = new Map<string, PbmReference>();
  for (const r of refs) {
    if (r.pmid) map.set(r.pmid, r);
  }
  return map;
}

/** URL canónica de una referencia (DOI preferente, si no PubMed). */
export function refUrl(ref: PbmReference | undefined, pmid?: string | null): string | null {
  if (ref?.doi) return `https://doi.org/${ref.doi}`;
  const p = ref?.pmid || pmid;
  if (p) return `https://pubmed.ncbi.nlm.nih.gov/${p}/`;
  return null;
}

/** URL a partir de un string "PMID 1234" usando el índice de referencias. */
export function urlFromRefString(
  ref: string,
  byPmid: Map<string, PbmReference>,
): string | null {
  const pmid = pmidFromRef(ref);
  if (!pmid) return null;
  return refUrl(byPmid.get(pmid), pmid);
}
