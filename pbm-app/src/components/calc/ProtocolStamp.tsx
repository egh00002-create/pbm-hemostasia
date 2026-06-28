/** Sello de trazabilidad para las calculadoras que reproducen el protocolo local. */
export function ProtocolStamp() {
  return (
    <p className="protocol-stamp" role="note">
      <span aria-hidden="true">📋</span>
      <span>
        Protocolo <strong>PTC-ANR-22-01-01</strong> · Anestesia CAUSA/SACYL · v. 18/12/2025 · revisión cada 4 años
      </span>
    </p>
  );
}
