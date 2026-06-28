import { HashRouter, Routes, Route, Navigate, useRouteError } from 'react-router-dom';
import { DataProvider, useDataState } from './data/DataContext';
import { Layout } from './components/Layout';
import { Home } from './pages/Home';
import { IndexPage } from './pages/IndexPage';
import { Reader } from './pages/Reader';
import { Calculators } from './pages/Calculators';
import { Quiz } from './pages/Quiz';
import { Search } from './pages/Search';
import { About } from './pages/About';

function Gate({ children }: { children: React.ReactNode }) {
  const { loading, error } = useDataState();
  if (loading) {
    return (
      <div className="loading" role="status" aria-live="polite">
        <div className="spinner" aria-hidden="true" />
        Cargando contenido de la serie…
      </div>
    );
  }
  if (error) {
    return (
      <div className="empty" role="alert">
        <h2>No se pudieron cargar los datos</h2>
        <p>{error}</p>
        <p className="source-note">
          Asegúrate de haber ejecutado <code>npm run sync-data</code> para copiar{' '}
          <code>app-data/</code>.
        </p>
      </div>
    );
  }
  return <>{children}</>;
}

function RouteError() {
  const err = useRouteError();
  return (
    <div className="empty" role="alert">
      <h2>Algo salió mal</h2>
      <p>{err instanceof Error ? err.message : 'Error de navegación.'}</p>
    </div>
  );
}

export default function App() {
  return (
    <DataProvider>
      <HashRouter>
        <Layout>
          <Gate>
            <Routes>
              <Route path="/" element={<Home />} errorElement={<RouteError />} />
              <Route path="/indice" element={<IndexPage />} />
              <Route path="/doc/:code" element={<Reader />} />
              <Route path="/calculadoras" element={<Calculators />} />
              <Route path="/calculadoras/:tool" element={<Calculators />} />
              <Route path="/evaluacion" element={<Quiz />} />
              <Route path="/buscar" element={<Search />} />
              <Route path="/acerca" element={<About />} />
              <Route path="*" element={<Navigate to="/" replace />} />
            </Routes>
          </Gate>
        </Layout>
      </HashRouter>
    </DataProvider>
  );
}
