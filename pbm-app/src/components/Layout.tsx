import { type ReactNode } from 'react';
import { NavLink, Link } from 'react-router-dom';
import { useTheme } from '../hooks/useTheme';
import { DISCLAIMER_TEXT } from './Disclaimer';

const NAV = [
  { to: '/', label: 'Inicio', icon: '🏠', end: true },
  { to: '/indice', label: 'Índice', icon: '📚' },
  { to: '/calculadoras', label: 'Calculadoras', icon: '🧮' },
  { to: '/evaluacion', label: 'Evaluación', icon: '✔️' },
  { to: '/buscar', label: 'Buscar', icon: '🔍' },
];

function ThemeToggle() {
  const { pref, cycle } = useTheme();
  const label =
    pref === 'light' ? 'Tema claro' : pref === 'dark' ? 'Tema oscuro' : 'Tema automático';
  const icon = pref === 'light' ? '☀️' : pref === 'dark' ? '🌙' : '🌗';
  return (
    <button
      type="button"
      className="iconbtn"
      onClick={cycle}
      aria-label={`Cambiar tema (actual: ${label})`}
      title={label}
    >
      <span aria-hidden="true">{icon}</span>
    </button>
  );
}

export function Layout({ children }: { children: ReactNode }) {
  return (
    <div className="app">
      <a className="skip-link" href="#contenido">
        Saltar al contenido
      </a>
      <header className="appbar">
        <div className="container appbar__inner">
          <Link to="/" className="brand">
            <img src={`${import.meta.env.BASE_URL}favicon.svg`} alt="" className="brand__mark" />
            <span>
              PBM
              <span className="brand__sub"> · Hemostasia perioperatoria</span>
            </span>
          </Link>
          <nav className="nav" aria-label="Principal">
            {NAV.map((n) => (
              <NavLink key={n.to} to={n.to} end={n.end}>
                {n.label}
              </NavLink>
            ))}
          </nav>
          <span className="appbar__spacer" />
          <ThemeToggle />
        </div>
      </header>

      <main id="contenido" className="main" tabIndex={-1}>
        <div className="container">
          {/* Aviso temporal mientras se revisan las calculadoras de hierro/EPO (auditoría 2026-10). */}
          <p className="disclaimer" role="note">
            <span className="ic" aria-hidden="true">⚠</span>
            <span>
              <strong>Herramienta en revisión.</strong> Las calculadoras de hierro y EPO pueden dar
              recomendaciones no concordantes entre pantallas. No usar para prescribir sin verificar con el
              protocolo del servicio.
            </span>
          </p>
          {children}
        </div>
      </main>

      <nav className="tabbar" aria-label="Navegación inferior">
        <div className="tabbar__inner">
          {NAV.map((n) => (
            <NavLink key={n.to} to={n.to} end={n.end}>
              <span className="ic" aria-hidden="true">
                {n.icon}
              </span>
              {n.label}
            </NavLink>
          ))}
        </div>
      </nav>

      <footer className="footer">
        <div className="container">
          <p>
            <strong>PBM — Hemostasia y Medicina Transfusional Perioperatoria.</strong> Apoyo
            docente, no dispositivo médico. {DISCLAIMER_TEXT}
          </p>
          <p>
            Ideación: Emilio García Hernández — FEA Anestesiología y Reanimación · CAUSA ·
            SACYL. · <Link to="/acerca">Acerca de</Link>
          </p>
        </div>
      </footer>
    </div>
  );
}
