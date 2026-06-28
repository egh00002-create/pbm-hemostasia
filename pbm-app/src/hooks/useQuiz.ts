import { useCallback, useMemo, useState } from 'react';
import type { QuizQuestion } from '../types';
import {
  buildQuiz,
  scoreQuiz,
  mulberry32,
  type QuizMode,
  type ShuffledQuestion,
  type QuizScore,
} from '../lib/quiz';

export type QuizPhase = 'setup' | 'running' | 'results';

export interface UseQuiz {
  phase: QuizPhase;
  questions: ShuffledQuestion[];
  index: number;
  current: ShuffledQuestion | null;
  answers: (number | null)[];
  selected: number | null; // respuesta de la pregunta actual (null si no contestada)
  answeredCount: number;
  score: QuizScore | null;
  start: (mode: QuizMode, modeLabel: string) => void;
  answer: (optionIndex: number) => void;
  next: () => void;
  prev: () => void;
  goTo: (i: number) => void;
  finish: () => QuizScore;
  reset: () => void;
  modeLabel: string;
}

/**
 * Orquesta una tanda de evaluación: barajado, navegación, respuestas y puntuación.
 * La lógica pura vive en lib/quiz.ts; aquí solo se gestiona el estado de UI.
 */
export function useQuiz(bank: QuizQuestion[]): UseQuiz {
  const [phase, setPhase] = useState<QuizPhase>('setup');
  const [questions, setQuestions] = useState<ShuffledQuestion[]>([]);
  const [answers, setAnswers] = useState<(number | null)[]>([]);
  const [index, setIndex] = useState(0);
  const [score, setScore] = useState<QuizScore | null>(null);
  const [modeLabel, setModeLabel] = useState('');

  const start = useCallback(
    (mode: QuizMode, label: string) => {
      const seed = (Date.now() & 0xffffffff) >>> 0;
      const rng = mulberry32(seed);
      const built = buildQuiz(bank, mode, rng);
      setQuestions(built);
      setAnswers(new Array(built.length).fill(null));
      setIndex(0);
      setScore(null);
      setModeLabel(label);
      setPhase('running');
    },
    [bank],
  );

  const answer = useCallback(
    (optionIndex: number) => {
      setAnswers((prev) => {
        if (prev[index] !== null) return prev; // bloquear una vez contestada
        const copy = prev.slice();
        copy[index] = optionIndex;
        return copy;
      });
    },
    [index],
  );

  const next = useCallback(
    () => setIndex((i) => Math.min(i + 1, questions.length - 1)),
    [questions.length],
  );
  const prev = useCallback(() => setIndex((i) => Math.max(i - 1, 0)), []);
  const goTo = useCallback(
    (i: number) => setIndex(Math.max(0, Math.min(i, questions.length - 1))),
    [questions.length],
  );

  const finish = useCallback(() => {
    const s = scoreQuiz(questions, answers);
    setScore(s);
    setPhase('results');
    return s;
  }, [questions, answers]);

  const reset = useCallback(() => {
    setPhase('setup');
    setQuestions([]);
    setAnswers([]);
    setIndex(0);
    setScore(null);
    setModeLabel('');
  }, []);

  const answeredCount = useMemo(() => answers.filter((a) => a !== null).length, [answers]);

  return {
    phase,
    questions,
    index,
    current: questions[index] ?? null,
    answers,
    selected: answers[index] ?? null,
    answeredCount,
    score,
    start,
    answer,
    next,
    prev,
    goTo,
    finish,
    reset,
    modeLabel,
  };
}
