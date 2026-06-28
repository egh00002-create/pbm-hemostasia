// Repetición espaciada (sistema Leitner de 5 cajas). Lógica pura y testeable;
// el reloj se inyecta como parámetro `now` (epoch ms). Sin efectos secundarios.
import type { QuizQuestion } from '../types';

export interface CardState {
  id: string;
  box: number; // 1..MAX_BOX
  due: number; // epoch ms del próximo repaso
  lastSeen: number; // epoch ms de la última vez vista
  reps: number; // veces contestada
  correct: number; // aciertos acumulados
  lapses: number; // veces que cayó desde una caja avanzada
}

export type SrsStore = Record<string, CardState>;

export const MAX_BOX = 5;

/** Intervalos por caja (días). Índice = caja - 1. */
export const LEITNER_INTERVALS_DAYS = [0, 1, 3, 7, 16];

const DAY_MS = 86_400_000;
const RELEARN_MS = 10 * 60 * 1000; // fallo → reaparece en ~10 min

/** Intervalo en ms correspondiente a una caja. */
export function intervalForBox(box: number): number {
  const i = Math.min(Math.max(box, 1), MAX_BOX) - 1;
  return LEITNER_INTERVALS_DAYS[i] * DAY_MS;
}

/** Crea el estado inicial de una tarjeta no vista. */
export function newCard(id: string, now: number): CardState {
  return { id, box: 1, due: now, lastSeen: now, reps: 0, correct: 0, lapses: 0 };
}

/**
 * Aplica una respuesta a una tarjeta (Leitner):
 *  - acierto → sube de caja (máx MAX_BOX) y programa el siguiente repaso;
 *  - fallo → vuelve a la caja 1 y reaparece a corto plazo.
 * Devuelve un estado NUEVO; no muta el anterior.
 */
export function reviewCard(
  prev: CardState | undefined,
  id: string,
  correct: boolean,
  now: number,
): CardState {
  const base = prev ?? newCard(id, now);
  let box = base.box;
  let lapses = base.lapses;

  if (correct) {
    box = Math.min(box + 1, MAX_BOX);
  } else {
    if (base.box >= 2) lapses += 1; // solo cuenta lapso si ya estaba progresando
    box = 1;
  }

  const due = correct ? now + intervalForBox(box) : now + RELEARN_MS;

  return {
    id,
    box,
    due,
    lastSeen: now,
    reps: base.reps + 1,
    correct: base.correct + (correct ? 1 : 0),
    lapses,
  };
}

export type CardCategory = 'unseen' | 'learning' | 'review' | 'mastered';

/** Clasifica una tarjeta para el panel de progreso. */
export function categoryOf(card: CardState | undefined): CardCategory {
  if (!card) return 'unseen';
  if (card.box >= MAX_BOX) return 'mastered';
  if (card.box >= 3) return 'review';
  return 'learning';
}

export interface ProgressStats {
  total: number;
  seen: number;
  unseen: number;
  due: number;
  learning: number;
  review: number;
  mastered: number;
  reps: number;
  correct: number;
  accuracy: number; // 0..100
}

/** Estadística global de progreso sobre el banco completo de preguntas. */
export function computeStats(store: SrsStore, allIds: string[], now: number): ProgressStats {
  let seen = 0;
  let due = 0;
  let learning = 0;
  let review = 0;
  let mastered = 0;
  let reps = 0;
  let correct = 0;

  for (const id of allIds) {
    const c = store[id];
    if (!c) continue;
    seen += 1;
    reps += c.reps;
    correct += c.correct;
    if (c.due <= now) due += 1;
    const cat = categoryOf(c);
    if (cat === 'learning') learning += 1;
    else if (cat === 'review') review += 1;
    else if (cat === 'mastered') mastered += 1;
  }

  const total = allIds.length;
  return {
    total,
    seen,
    unseen: total - seen,
    due,
    learning,
    review,
    mastered,
    reps,
    correct,
    accuracy: reps ? Math.round((correct / reps) * 100) : 0,
  };
}

/** IDs de tarjetas vencidas (due ≤ now), ordenadas de más vencida a menos. */
export function dueCardIds(store: SrsStore, allIds: string[], now: number): string[] {
  return allIds
    .filter((id) => store[id] && store[id].due <= now)
    .sort((a, b) => store[a].due - store[b].due);
}

/** IDs de preguntas aún no vistas, en el orden del banco. */
export function unseenCardIds(store: SrsStore, allIds: string[]): string[] {
  return allIds.filter((id) => !store[id]);
}

export interface ModuleProgress {
  module: number;
  total: number;
  seen: number;
  due: number;
  mastered: number;
}

/** Progreso desglosado por módulo (0 = quick-reference). */
export function statsByModule(
  store: SrsStore,
  questions: QuizQuestion[],
  now: number,
): Record<number, ModuleProgress> {
  const out: Record<number, ModuleProgress> = {};
  for (const q of questions) {
    out[q.module] ??= { module: q.module, total: 0, seen: 0, due: 0, mastered: 0 };
    const m = out[q.module];
    m.total += 1;
    const c = store[q.id];
    if (c) {
      m.seen += 1;
      if (c.due <= now) m.due += 1;
      if (categoryOf(c) === 'mastered') m.mastered += 1;
    }
  }
  return out;
}
