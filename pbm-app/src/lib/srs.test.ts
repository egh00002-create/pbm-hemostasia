import { describe, it, expect } from 'vitest';
import {
  reviewCard,
  computeStats,
  dueCardIds,
  unseenCardIds,
  categoryOf,
  intervalForBox,
  statsByModule,
  MAX_BOX,
  type SrsStore,
} from './srs';
import type { QuizQuestion } from '../types';

const DAY = 86_400_000;
const T0 = 1_700_000_000_000; // instante de referencia fijo (no usamos Date.now)

describe('reviewCard (Leitner)', () => {
  it('acierto inicial: sube a caja 2 y programa +1 día', () => {
    const c = reviewCard(undefined, 'Q1', true, T0);
    expect(c.box).toBe(2);
    expect(c.reps).toBe(1);
    expect(c.correct).toBe(1);
    expect(c.due).toBe(T0 + 1 * DAY);
  });

  it('fallo: vuelve a caja 1 y reaparece a corto plazo', () => {
    const prev = reviewCard(undefined, 'Q1', true, T0); // caja 2
    const c = reviewCard(prev, 'Q1', false, T0 + DAY);
    expect(c.box).toBe(1);
    expect(c.lapses).toBe(1); // cayó desde caja ≥2
    expect(c.due).toBeLessThan(T0 + DAY + DAY); // due a ~10 min, no días
  });

  it('fallo en primera exposición no cuenta lapso', () => {
    const c = reviewCard(undefined, 'Q1', false, T0);
    expect(c.box).toBe(1);
    expect(c.lapses).toBe(0);
  });

  it('aciertos sucesivos llegan a la caja máxima (mastered)', () => {
    let c = reviewCard(undefined, 'Q1', true, T0);
    for (let i = 0; i < 10; i++) c = reviewCard(c, 'Q1', true, c.due);
    expect(c.box).toBe(MAX_BOX);
    expect(categoryOf(c)).toBe('mastered');
    expect(c.due).toBe(c.lastSeen + intervalForBox(MAX_BOX));
  });

  it('no muta el estado previo', () => {
    const prev = reviewCard(undefined, 'Q1', true, T0);
    const snapshot = { ...prev };
    reviewCard(prev, 'Q1', true, T0 + DAY);
    expect(prev).toEqual(snapshot);
  });
});

describe('computeStats / dueCardIds / unseenCardIds', () => {
  const allIds = ['Q1', 'Q2', 'Q3', 'Q4'];
  const store: SrsStore = {
    Q1: reviewCard(undefined, 'Q1', true, T0 - 5 * DAY), // due hace tiempo
    Q2: reviewCard(undefined, 'Q2', false, T0 - 5 * DAY), // vencida (fallada)
    // Q3, Q4 no vistas
  };

  it('cuenta vistas, no vistas y vencidas', () => {
    const s = computeStats(store, allIds, T0);
    expect(s.total).toBe(4);
    expect(s.seen).toBe(2);
    expect(s.unseen).toBe(2);
    expect(s.due).toBe(2); // ambas vencidas en T0
  });

  it('accuracy = aciertos / repeticiones', () => {
    const s = computeStats(store, allIds, T0);
    expect(s.reps).toBe(2);
    expect(s.correct).toBe(1);
    expect(s.accuracy).toBe(50);
  });

  it('dueCardIds devuelve vencidas ordenadas por due ascendente', () => {
    const due = dueCardIds(store, allIds, T0);
    expect(due).toContain('Q1');
    expect(due).toContain('Q2');
    expect(due).not.toContain('Q3');
    // la más vencida primero
    expect(store[due[0]].due).toBeLessThanOrEqual(store[due[1]].due);
  });

  it('unseenCardIds lista las no vistas en orden', () => {
    expect(unseenCardIds(store, allIds)).toEqual(['Q3', 'Q4']);
  });
});

describe('statsByModule', () => {
  const questions: QuizQuestion[] = [
    mkQ('Q1', 1),
    mkQ('Q2', 1),
    mkQ('Q3', 2),
  ];
  it('agrupa por módulo y cuenta vistas/vencidas', () => {
    const store: SrsStore = { Q1: reviewCard(undefined, 'Q1', false, T0 - DAY) };
    const by = statsByModule(store, questions, T0);
    expect(by[1].total).toBe(2);
    expect(by[1].seen).toBe(1);
    expect(by[1].due).toBe(1);
    expect(by[2].total).toBe(1);
    expect(by[2].seen).toBe(0);
  });
});

function mkQ(id: string, module: number): QuizQuestion {
  return {
    id,
    doc: 'PBM-01',
    module,
    level: 'basico',
    q: 'q',
    options: ['a', 'b', 'c', 'd'],
    answer: 0,
    explanation: 'e',
    ref: 'PMID 1',
  };
}
