import { useData } from '../data/DataContext';
import { Disclaimer } from '../components/Disclaimer';

export function About() {
  const { docs, questions, references } = useData();
  return (
    <div>
      <section className="page-head">
        <p className="kicker-line">Acerca de</p>
        <h1>PBM — Hemostasia y Medicina Transfusional Perioperatoria</h1>
      </section>

      <div className="card">
        <p>
          Aplicación web docente (PWA, 100% offline) de la serie formativa sobre{' '}
          <strong>Patient Blood Management</strong> y hemostasia perioperatoria. Reúne{' '}
          <strong>{docs.length} documentos</strong> (3 pilares + eje de hemostasia),{' '}
          <strong>{references.length} referencias</strong> verificadas con DOI/PMID y{' '}
          <strong>{questions.length} preguntas</strong> de evaluación.
        </p>
        <p>
          Estructura: optimizar la masa eritrocitaria · minimizar la pérdida sanguínea ·
          tolerar la anemia y transfundir bien · eje transversal de hemostasia y riesgo
          hemorrágico.
        </p>
      </div>

      <div className="card" style={{ marginTop: 14 }}>
        <h3>Descargo</h3>
        <Disclaimer />
        <p className="source-note">
          Este material es <strong>apoyo docente y no un dispositivo médico</strong>. Las
          calculadoras son estimaciones de planificación: no son disparadores automáticos de
          transfusión ni de tratamiento. Los umbrales, dosis y tiempos definitivos se toman del
          protocolo local vigente y de la ficha técnica de cada fármaco. Ninguna decisión clínica
          debe basarse únicamente en esta aplicación.
        </p>
        <p className="source-note">
          No se recogen ni se envían datos clínicos. El navegador solo guarda, en local,
          preferencias de interfaz y el histórico de puntuaciones del quiz.
        </p>
      </div>

      <div className="card" style={{ marginTop: 14 }}>
        <h3>Honestidad de la evidencia</h3>
        <ul>
          <li>SCA: se favorece umbral transfusional liberal (≈10 g/dl), en contra del restrictivo.</li>
          <li>PREVENTT: hierro IV preoperatorio con resultado neutro en su objetivo principal.</li>
          <li>CRASH-3: beneficio del tranexámico limitado/ausente en TCE grave.</li>
          <li>No transfundir plasma por INR/TTPa levemente alterado sin sangrado.</li>
          <li>FA: en contra del puente sistemático con HBPM (BRIDGE).</li>
        </ul>
      </div>

      <div className="card" style={{ marginTop: 14 }}>
        <h3>Autoría</h3>
        <p className="source-note">
          Ideación y contenidos: <strong>Emilio García Hernández</strong> — FEA Anestesiología y
          Reanimación · CAUSA · SACYL (Salamanca).
        </p>
      </div>
    </div>
  );
}
