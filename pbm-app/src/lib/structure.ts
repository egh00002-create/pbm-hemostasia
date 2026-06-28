// Metadatos de la espina de la serie: 3 pilares + eje de hemostasia.
import type { Anchor } from '../types';

export interface ModuleInfo {
  n: number; // número de módulo (0 = quick-reference)
  key: string; // valor de PbmDoc.pillar correspondiente
  label: string; // etiqueta visible
  pillarTag: string; // texto del pilar/eje
  axis?: boolean; // true para el eje (acero) en lugar de pilar (granate)
}

export const MODULES: ModuleInfo[] = [
  { n: 1, key: 'Fundamentos', label: 'Módulo 1 · Fundamentos', pillarTag: 'Fundamentos' },
  {
    n: 2,
    key: 'Pilar 1',
    label: 'Módulo 2 · Pilar 1: optimizar la masa eritrocitaria',
    pillarTag: 'Pilar 1',
  },
  {
    n: 3,
    key: 'Pilar 2',
    label: 'Módulo 3 · Pilar 2: minimizar la pérdida sanguínea',
    pillarTag: 'Pilar 2',
  },
  {
    n: 4,
    key: 'Pilar 3',
    label: 'Módulo 4 · Pilar 3: tolerancia a la anemia y transfusión',
    pillarTag: 'Pilar 3',
  },
  {
    n: 5,
    key: 'Eje hemostasia',
    label: 'Módulo 5 · Eje de hemostasia clínica',
    pillarTag: 'Eje hemostasia',
    axis: true,
  },
  {
    n: 0,
    key: 'Tarjetas',
    label: 'Quick-reference · Tarjetas (ALG)',
    pillarTag: 'Quick-reference',
    axis: true,
  },
];

/** Tarjetas de los 3 pilares + eje para la pantalla de inicio. */
export interface PillarCard {
  pillarKey: string;
  tag: string;
  title: string;
  desc: string;
  axis?: boolean;
}

export const PILLAR_CARDS: PillarCard[] = [
  {
    pillarKey: 'Pilar 1',
    tag: 'Pilar 1',
    title: 'Optimizar la masa eritrocitaria',
    desc: 'Anemia preoperatoria, ferropenia y hierro IV, eritropoyetina.',
  },
  {
    pillarKey: 'Pilar 2',
    tag: 'Pilar 2',
    title: 'Minimizar la pérdida sanguínea',
    desc: 'Hemostasia, antifibrinolíticos, viscoelástica, recuperación celular, MABL.',
  },
  {
    pillarKey: 'Pilar 3',
    tag: 'Pilar 3',
    title: 'Tolerar la anemia y transfundir bien',
    desc: 'Umbrales restrictivos, hemorragia crítica, fisiología de la tolerancia.',
  },
  {
    pillarKey: 'Eje hemostasia',
    tag: 'Eje transversal',
    title: 'Hemostasia y riesgo hemorrágico',
    desc: 'Cribado HEMSTOP, antitrombóticos, coagulopatías, fármacos hemostáticos.',
    axis: true,
  },
];

export const ANCHOR_LABELS: Record<Anchor, string> = {
  GUIA: 'GUÍA',
  META: 'META',
  ECA: 'ECA',
  REV: 'REV',
  ALG: 'ALG',
};

export const ANCHOR_CLASS: Record<Anchor, string> = {
  GUIA: 'guia',
  META: 'meta',
  ECA: 'eca',
  REV: 'rev',
  ALG: 'alg',
};

export function moduleByNumber(n: number): ModuleInfo | undefined {
  return MODULES.find((m) => m.n === n);
}

export function moduleByKey(key: string): ModuleInfo | undefined {
  return MODULES.find((m) => m.key === key);
}
