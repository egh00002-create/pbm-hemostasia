import { useCallback, useMemo } from 'react';
import { useLocalStorage } from './useLocalStorage';
import {
  reviewCard,
  computeStats,
  dueCardIds,
  unseenCardIds,
  statsByModule,
  type SrsStore,
} from '../lib/srs';
import type { QuizQuestion } from '../types';

export const SRS_KEY = 'pbm_srs';

/**
 * Progreso del usuario y repetición espaciada (Leitner) sobre el banco de
 * preguntas. Persistido en localStorage (solo preferencias/aprendizaje, nunca
 * datos clínicos). El reloj es Date.now(); la lógica pura vive en lib/srs.ts.
 */
export function useProgress(questions: QuizQuestion[]) {
  const [store, setStore, resetStore] = useLocalStorage<SrsStore>(SRS_KEY, {});
  const allIds = useMemo(() => questions.map((q) => q.id), [questions]);

  const recordAnswer = useCallback(
    (id: string, correct: boolean) => {
      const now = Date.now();
      setStore((prev) => ({ ...prev, [id]: reviewCard(prev[id], id, correct, now) }));
    },
    [setStore],
  );

  // now en el momento del render; los derivados se recalculan en cada cambio del store.
  const now = Date.now();
  const stats = useMemo(() => computeStats(store, allIds, now), [store, allIds, now]);
  const due = useMemo(() => dueCardIds(store, allIds, now), [store, allIds, now]);
  const unseen = useMemo(() => unseenCardIds(store, allIds), [store, allIds]);
  const byModule = useMemo(() => statsByModule(store, questions, now), [store, questions, now]);

  return { store, stats, due, unseen, byModule, recordAnswer, resetStore };
}
