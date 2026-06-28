import { describe, it, expect } from 'vitest';
import {
  shuffleOptions,
  buildQuiz,
  selectByMode,
  scoreQuiz,
  mulberry32,
  type ShuffledQuestion,
} from './quiz';
import type { QuizQuestion } from '../types';

function q(partial: Partial<QuizQuestion> & { id: string }): QuizQuestion {
  return {
    id: partial.id,
    doc: partial.doc ?? 'PBM-01',
    module: partial.module ?? 1,
    level: partial.level ?? 'basico',
    q: partial.q ?? 'pregunta',
    options: partial.options ?? ['A', 'B', 'C', 'D'],
    answer: partial.answer ?? 0,
    explanation: partial.explanation ?? 'exp',
    ref: partial.ref ?? 'PMID 1',
  };
}

describe('shuffleOptions (INVARIANTE OBLIGATORIA)', () => {
  it('tras barajar, answer sigue apuntando a la opción correcta', () => {
    const base = q({ id: 'Q1', options: ['w', 'x', 'y', 'z'], answer: 2 }); // 'y' correcta
    const correctText = base.options[base.answer];
    // Probar con muchas semillas para cubrir todas las permutaciones posibles.
    for (let seed = 0; seed < 200; seed++) {
      const s = shuffleOptions(base, mulberry32(seed));
      expect(s.options).toHaveLength(4);
      expect(new Set(s.options)).toEqual(new Set(base.options)); // mismas opciones
      expect(s.options[s.answer]).toBe(correctText); // la respuesta sigue siendo correcta
    }
  });

  it('originalOrder traza el origen de cada opción', () => {
    const base = q({ id: 'Q1', options: ['w', 'x', 'y', 'z'], answer: 1 });
    const s = shuffleOptions(base, mulberry32(7));
    s.options.forEach((opt, i) => {
      expect(opt).toBe(base.options[s.originalOrder[i]]);
    });
  });
});

describe('selectByMode', () => {
  const bank = [
    q({ id: 'a', module: 1, doc: 'PBM-01', level: 'basico' }),
    q({ id: 'b', module: 2, doc: 'PBM-04', level: 'avanzado' }),
    q({ id: 'c', module: 0, doc: 'P-QR-01', level: 'basico' }),
  ];
  it('por módulo', () => {
    expect(selectByMode(bank, { kind: 'modulo', module: 2 }).map((x) => x.id)).toEqual(['b']);
  });
  it('por nivel', () => {
    expect(selectByMode(bank, { kind: 'nivel', level: 'basico' }).map((x) => x.id)).toEqual([
      'a',
      'c',
    ]);
  });
  it('por documento', () => {
    expect(selectByMode(bank, { kind: 'documento', doc: 'P-QR-01' }).map((x) => x.id)).toEqual([
      'c',
    ]);
  });
  it('por pilar (varios módulos)', () => {
    expect(
      selectByMode(bank, { kind: 'pilar', pillarKey: 'x', modules: [1, 2] }).map((x) => x.id),
    ).toEqual(['a', 'b']);
  });
});

describe('buildQuiz', () => {
  const bank = Array.from({ length: 50 }, (_, i) =>
    q({ id: `Q${i}`, module: (i % 5) + 1, answer: i % 4 }),
  );
  it('modo rápido recorta a 10 y mantiene la respuesta correcta', () => {
    const built = buildQuiz(bank, { kind: 'rapido' }, mulberry32(42));
    expect(built).toHaveLength(10);
    for (const item of built) {
      const original = bank.find((b) => b.id === item.id)!;
      expect(item.options[item.answer]).toBe(original.options[original.answer]);
    }
  });
  it('modo completo conserva todas', () => {
    expect(buildQuiz(bank, { kind: 'completo' }, mulberry32(1))).toHaveLength(50);
  });
});

describe('scoreQuiz', () => {
  it('puntúa total, %, por módulo y por nivel', () => {
    const questions: ShuffledQuestion[] = [
      { ...q({ id: '1', module: 1, level: 'basico', answer: 0 }), originalOrder: [0, 1, 2, 3] },
      {
        ...q({ id: '2', module: 1, level: 'avanzado', answer: 2 }),
        originalOrder: [0, 1, 2, 3],
      },
      { ...q({ id: '3', module: 2, level: 'basico', answer: 1 }), originalOrder: [0, 1, 2, 3] },
    ];
    const answers = [0, 0, 1]; // 1ª bien, 2ª mal, 3ª bien
    const s = scoreQuiz(questions, answers);
    expect(s.correct).toBe(2);
    expect(s.total).toBe(3);
    expect(s.percent).toBe(67);
    expect(s.byModule[1]).toEqual({ total: 2, correct: 1 });
    expect(s.byModule[2]).toEqual({ total: 1, correct: 1 });
    expect(s.byLevel.basico).toEqual({ total: 2, correct: 2 });
    expect(s.byLevel.avanzado).toEqual({ total: 1, correct: 0 });
  });
});
