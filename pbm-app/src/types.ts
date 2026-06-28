// Tipos del dominio PBM. Reflejan exactamente la forma de los datos en app-data/.

export type Anchor = 'GUIA' | 'META' | 'ECA' | 'REV' | 'ALG';
export type DocLevel = 'BASICO' | 'AVANZADO';

/** Documento de la serie (content.json). */
export interface PbmDoc {
  code: string; // p.ej. "PBM-01" / "P-QR-01"
  title: string; // HTML con entidades
  module: string; // p.ej. "Modulo 1 - Fundamentos"
  pillar: string; // "Fundamentos" | "Pilar 1" | ... | "Tarjetas"
  anchor: Anchor;
  level: DocLevel;
  core: boolean;
  coverHtml: string;
  bodyHtml: string;
  refsHtml: string;
}

/** Referencia bibliográfica (references.json). */
export interface PbmReference {
  citation: string;
  doi: string;
  pmid: string;
}

/** Pregunta de evaluación (questions.json). */
export interface QuizQuestion {
  id: string;
  doc: string; // código de documento, p.ej. "PBM-01"
  module: number; // 0 (Quick-reference) .. 5
  level: 'basico' | 'avanzado';
  q: string;
  options: string[]; // 4 opciones
  answer: number; // 0..3 índice de la correcta
  explanation: string;
  ref: string; // "PMID 12345678"
}

/** Registro de un intento de quiz guardado en localStorage. */
export interface QuizHistoryEntry {
  date: number; // epoch ms
  mode: string; // etiqueta legible del modo
  total: number;
  correct: number;
  percent: number;
}
