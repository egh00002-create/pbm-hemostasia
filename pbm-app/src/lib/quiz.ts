// Lógica pura del quiz: barajado de preguntas y de opciones (recalculando el
// índice de la respuesta correcta), y selección por modo. Sin efectos secundarios.
import type { QuizQuestion } from '../types';

/** PRNG determinista (mulberry32) para barajados reproducibles y testeables. */
export function mulberry32(seed: number): () => number {
  let a = seed >>> 0;
  return function () {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** Fisher–Yates puro: devuelve un array nuevo, no muta la entrada. */
export function shuffle<T>(arr: readonly T[], rng: () => number = Math.random): T[] {
  const out = arr.slice();
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

/**
 * Pregunta con las opciones ya barajadas. `answer` apunta SIEMPRE a la opción
 * correcta dentro del nuevo array `options`.
 */
export interface ShuffledQuestion extends QuizQuestion {
  /** índices originales de cada opción, por trazabilidad/test */
  originalOrder: number[];
}

/** Baraja las opciones de UNA pregunta recalculando el índice correcto. */
export function shuffleOptions(
  question: QuizQuestion,
  rng: () => number = Math.random,
): ShuffledQuestion {
  const indices = question.options.map((_, i) => i);
  const order = shuffle(indices, rng);
  const options = order.map((i) => question.options[i]);
  const answer = order.indexOf(question.answer);
  return { ...question, options, answer, originalOrder: order };
}

/** Modos de evaluación disponibles. */
export type QuizMode =
  | { kind: 'rapido' }
  | { kind: 'modulo'; module: number }
  | { kind: 'pilar'; pillarKey: string; modules: number[] }
  | { kind: 'documento'; doc: string }
  | { kind: 'nivel'; level: 'basico' | 'avanzado' }
  | { kind: 'completo' }
  // Lista explícita de ids (repaso espaciado, preguntas nuevas, etc.).
  // Conserva el orden recibido (p.ej. vencidas primero).
  | { kind: 'custom'; ids: string[] };

/** Filtra el banco según el modo (sin barajar todavía). */
export function selectByMode(all: QuizQuestion[], mode: QuizMode): QuizQuestion[] {
  switch (mode.kind) {
    case 'rapido':
    case 'completo':
      return all.slice();
    case 'modulo':
      return all.filter((q) => q.module === mode.module);
    case 'pilar':
      return all.filter((q) => mode.modules.includes(q.module));
    case 'documento':
      return all.filter((q) => q.doc === mode.doc);
    case 'nivel':
      return all.filter((q) => q.level === mode.level);
    case 'custom': {
      const byId = new Map(all.map((q) => [q.id, q]));
      return mode.ids.map((id) => byId.get(id)).filter((q): q is QuizQuestion => Boolean(q));
    }
  }
}

/**
 * Construye la tanda final: filtra por modo, baraja preguntas, recorta (modo
 * rápido = 10) y baraja las opciones de cada una.
 */
export function buildQuiz(
  all: QuizQuestion[],
  mode: QuizMode,
  rng: () => number = Math.random,
): ShuffledQuestion[] {
  const selected = selectByMode(all, mode);
  // 'custom' (repaso) conserva el orden recibido (vencidas primero); el resto se baraja.
  const pool = mode.kind === 'custom' ? selected : shuffle(selected, rng);
  const limited = mode.kind === 'rapido' ? pool.slice(0, 10) : pool;
  return limited.map((q) => shuffleOptions(q, rng));
}

export interface QuizScore {
  total: number;
  correct: number;
  percent: number;
  byModule: Record<number, { total: number; correct: number }>;
  byLevel: Record<'basico' | 'avanzado', { total: number; correct: number }>;
}

/**
 * Puntúa un conjunto de respuestas. `answers[i]` es el índice elegido para la
 * pregunta `questions[i]` (o null si no contestada).
 */
export function scoreQuiz(
  questions: ShuffledQuestion[],
  answers: (number | null)[],
): QuizScore {
  const byModule: QuizScore['byModule'] = {};
  const byLevel: QuizScore['byLevel'] = {
    basico: { total: 0, correct: 0 },
    avanzado: { total: 0, correct: 0 },
  };
  let correct = 0;
  questions.forEach((q, i) => {
    const ok = answers[i] === q.answer;
    if (ok) correct++;
    byModule[q.module] ??= { total: 0, correct: 0 };
    byModule[q.module].total++;
    if (ok) byModule[q.module].correct++;
    byLevel[q.level].total++;
    if (ok) byLevel[q.level].correct++;
  });
  const total = questions.length;
  return {
    total,
    correct,
    percent: total ? Math.round((correct / total) * 100) : 0,
    byModule,
    byLevel,
  };
}
