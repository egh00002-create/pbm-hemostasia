import {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from 'react';
import type { PbmDoc, PbmReference, QuizQuestion } from '../types';
import { indexByPmid } from '../lib/references';
import { decodeEntities, stripHtml } from '../lib/html';

// Base relativa para que funcione en subrutas (GitHub Pages) y offline.
const BASE = import.meta.env.BASE_URL;

export interface PbmData {
  docs: PbmDoc[];
  references: PbmReference[];
  questions: QuizQuestion[];
  contentMd: string;
  byCode: Map<string, PbmDoc>;
  refByPmid: Map<string, PbmReference>;
  docTitle: (code: string) => string; // título en texto plano
}

interface DataState {
  data: PbmData | null;
  loading: boolean;
  error: string | null;
}

const DataCtx = createContext<DataState>({ data: null, loading: true, error: null });

async function fetchJson<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE}app-data/${path}`);
  if (!res.ok) throw new Error(`No se pudo cargar ${path} (${res.status})`);
  return (await res.json()) as T;
}

export function DataProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<DataState>({
    data: null,
    loading: true,
    error: null,
  });

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const [docs, references, questions, contentMd] = await Promise.all([
          fetchJson<PbmDoc[]>('content.json'),
          fetchJson<PbmReference[]>('references.json'),
          fetchJson<QuizQuestion[]>('questions.json'),
          fetch(`${BASE}app-data/content.md`).then((r) => {
            if (!r.ok) throw new Error('No se pudo cargar content.md');
            return r.text();
          }),
        ]);
        if (cancelled) return;

        const byCode = new Map(docs.map((d) => [d.code, d]));
        const refByPmid = indexByPmid(references);
        const titleCache = new Map<string, string>();
        const docTitle = (code: string) => {
          if (titleCache.has(code)) return titleCache.get(code)!;
          const d = byCode.get(code);
          const t = d ? stripHtml(d.title) : code;
          titleCache.set(code, t);
          return t;
        };

        setState({
          data: {
            docs,
            references,
            questions,
            contentMd: decodeEntities(contentMd),
            byCode,
            refByPmid,
            docTitle,
          },
          loading: false,
          error: null,
        });
      } catch (e) {
        if (cancelled) return;
        setState({
          data: null,
          loading: false,
          error: e instanceof Error ? e.message : 'Error desconocido al cargar los datos',
        });
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  return <DataCtx.Provider value={state}>{children}</DataCtx.Provider>;
}

/** Acceso al estado de carga (loading/error). */
export function useDataState(): DataState {
  return useContext(DataCtx);
}

/** Acceso a los datos ya cargados. Debe usarse dentro de un árbol con datos listos. */
export function useData(): PbmData {
  const { data } = useContext(DataCtx);
  if (!data) {
    throw new Error('useData() llamado antes de que los datos estuvieran disponibles');
  }
  return useMemo(() => data, [data]);
}
