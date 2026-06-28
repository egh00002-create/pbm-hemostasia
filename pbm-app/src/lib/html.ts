// Utilidades para texto/HTML. El contenido viene con entidades HTML;
// estas funciones decodifican a texto plano cuando hace falta (títulos, búsqueda).

const NAMED: Record<string, string> = {
  amp: '&',
  lt: '<',
  gt: '>',
  quot: '"',
  apos: "'",
  nbsp: ' ',
  middot: '·',
  ndash: '–',
  mdash: '—',
  hellip: '…',
  aacute: 'á',
  eacute: 'é',
  iacute: 'í',
  oacute: 'ó',
  uacute: 'ú',
  Aacute: 'Á',
  Eacute: 'É',
  Iacute: 'Í',
  Oacute: 'Ó',
  Uacute: 'Ú',
  ntilde: 'ñ',
  Ntilde: 'Ñ',
  uuml: 'ü',
  Uuml: 'Ü',
  iquest: '¿',
  iexcl: '¡',
  ordf: 'ª',
  ordm: 'º',
  deg: '°',
  laquo: '«',
  raquo: '»',
  rsquo: '’',
  lsquo: '‘',
  ldquo: '“',
  rdquo: '”',
  times: '×',
  ge: '≥',
  le: '≤',
  plusmn: '±',
  rarr: '→',
  larr: '←',
  trade: '™',
  copy: '©',
  reg: '®',
  micro: 'µ',
  beta: 'β',
  alpha: 'α',
  gamma: 'γ',
  frac12: '½',
};

/** Decodifica entidades HTML (numéricas y nombradas comunes) a texto Unicode. */
export function decodeEntities(input: string): string {
  if (!input) return '';
  return input.replace(/&(#x?[0-9a-fA-F]+|[a-zA-Z]+);/g, (match, ent: string) => {
    if (ent[0] === '#') {
      const code =
        ent[1] === 'x' || ent[1] === 'X'
          ? parseInt(ent.slice(2), 16)
          : parseInt(ent.slice(1), 10);
      if (!Number.isNaN(code)) return String.fromCodePoint(code);
      return match;
    }
    return Object.prototype.hasOwnProperty.call(NAMED, ent) ? NAMED[ent] : match;
  });
}

/** Quita etiquetas HTML y decodifica entidades → texto plano. */
export function stripHtml(html: string): string {
  return decodeEntities(html.replace(/<[^>]+>/g, ' '))
    .replace(/\s+/g, ' ')
    .trim();
}

/** Normaliza para búsqueda: minúsculas y sin diacríticos. */
export function normalize(s: string): string {
  return s
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '');
}

/** Escapa caracteres especiales de regex. */
export function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
