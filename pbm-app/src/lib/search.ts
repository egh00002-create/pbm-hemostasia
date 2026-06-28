import { normalize } from './html';

export interface DocSegment {
  code: string;
  text: string; // texto plano del documento
  normalized: string; // texto normalizado para búsqueda
}

/**
 * Parte content.md en segmentos por documento usando los delimitadores
 * `<!-- CODE -->`. Devuelve texto plano por código de documento.
 */
export function parseSegments(md: string): DocSegment[] {
  const re = /<!--\s*(P-QR-\d{2}|PBM-\d{2})\s*-->/g;
  const segments: DocSegment[] = [];
  const matches: { code: string; start: number }[] = [];
  let m: RegExpExecArray | null;
  while ((m = re.exec(md))) {
    matches.push({ code: m[1], start: m.index + m[0].length });
  }
  for (let i = 0; i < matches.length; i++) {
    const start = matches[i].start;
    const end = i + 1 < matches.length ? md.indexOf('<!--', start) : md.length;
    const text = md.slice(start, end === -1 ? md.length : end).trim();
    segments.push({ code: matches[i].code, text, normalized: normalize(text) });
  }
  return segments;
}

export interface SearchHit {
  code: string;
  title: string;
  score: number;
  snippet: string; // con marcadores 〈〈 〉〉 alrededor de la coincidencia
  matchStart: number;
}

const OPEN = '〈〈';
const CLOSE = '〉〉';

/** Busca el término en título + texto, devolviendo hits ordenados por relevancia. */
export function searchSegments(
  segments: DocSegment[],
  titleOf: (code: string) => string,
  rawQuery: string,
): SearchHit[] {
  const q = normalize(rawQuery.trim());
  if (q.length < 2) return [];
  const terms = q.split(/\s+/).filter(Boolean);

  const hits: SearchHit[] = [];
  for (const seg of segments) {
    const title = titleOf(seg.code);
    const ntitle = normalize(title);
    let score = 0;
    let firstIdx = -1;

    for (const term of terms) {
      const inTitle = ntitle.includes(term);
      const idx = seg.normalized.indexOf(term);
      if (inTitle) score += 5;
      if (idx >= 0) {
        score += 1;
        // contar ocurrencias (hasta un máximo razonable)
        let count = 0;
        let from = idx;
        while (from >= 0 && count < 20) {
          count++;
          from = seg.normalized.indexOf(term, from + term.length);
        }
        score += Math.min(count, 10) * 0.3;
        if (firstIdx === -1 || idx < firstIdx) firstIdx = idx;
      }
    }

    if (score > 0) {
      hits.push({
        code: seg.code,
        title,
        score,
        snippet: makeSnippet(seg.text, seg.normalized, terms, firstIdx),
        matchStart: firstIdx,
      });
    }
  }
  return hits.sort((a, b) => b.score - a.score);
}

function makeSnippet(
  text: string,
  normalized: string,
  terms: string[],
  firstIdx: number,
): string {
  let center = firstIdx;
  if (center < 0) {
    for (const t of terms) {
      const i = normalized.indexOf(t);
      if (i >= 0) {
        center = i;
        break;
      }
    }
  }
  if (center < 0) center = 0;
  const start = Math.max(0, center - 60);
  const end = Math.min(text.length, center + 140);
  let snippet = (start > 0 ? '…' : '') + text.slice(start, end) + (end < text.length ? '…' : '');

  // Resaltar cada término ignorando acentos.
  for (const term of terms) {
    if (term) snippet = wrapAccentInsensitive(snippet, term);
  }
  return snippet;
}

/**
 * Envuelve coincidencias del término (normalizado, sin acentos) en el texto
 * original. NFD elimina solo marcas combinantes, por lo que las posiciones de
 * los caracteres base se conservan y el recorrido carácter a carácter es fiable.
 */
function wrapAccentInsensitive(text: string, term: string): string {
  const nText = normalize(text);
  let result = '';
  let i = 0;
  while (i < text.length) {
    if (nText.startsWith(term, i) && !result.endsWith(OPEN)) {
      result += OPEN + text.slice(i, i + term.length) + CLOSE;
      i += term.length;
    } else {
      result += text[i];
      i += 1;
    }
  }
  return result;
}

export { OPEN as SNIPPET_OPEN, CLOSE as SNIPPET_CLOSE };
