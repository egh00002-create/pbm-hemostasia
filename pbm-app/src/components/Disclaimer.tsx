export const DISCLAIMER_TEXT =
  'No sustituye al juicio clínico ni a los protocolos locales vigentes.';

/** Descargo reutilizable. Obligatorio en pie, calculadoras y quiz. */
export function Disclaimer({ compact = false }: { compact?: boolean }) {
  return (
    <p className="disclaimer" role="note">
      <span className="ic" aria-hidden="true">
        ⚠
      </span>
      <span>
        {compact ? null : <strong>Apoyo docente, no dispositivo médico. </strong>}
        {DISCLAIMER_TEXT}
      </span>
    </p>
  );
}
