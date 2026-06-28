import type { Anchor, DocLevel } from '../types';
import { ANCHOR_CLASS, ANCHOR_LABELS } from '../lib/structure';

export function AnchorBadge({ anchor }: { anchor: Anchor }) {
  return (
    <span className={`badge ${ANCHOR_CLASS[anchor]}`} title={`Ancla de evidencia: ${anchor}`}>
      {ANCHOR_LABELS[anchor]}
    </span>
  );
}

export function LevelBadge({ level }: { level: DocLevel }) {
  return (
    <span className="badge level">{level === 'BASICO' ? 'Básico' : 'Avanzado'}</span>
  );
}

export function CoreBadge() {
  return (
    <span className="badge core" title="Documento núcleo de la serie">
      ★ Núcleo
    </span>
  );
}
