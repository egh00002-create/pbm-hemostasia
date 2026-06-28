# PBM — Hemostasia y Medicina Transfusional Perioperatoria (PWA)

Aplicación web **docente** y **100% offline** (PWA instalable) de la serie formativa sobre
*Patient Blood Management* y hemostasia perioperatoria. Reúne un **lector** de los 23 documentos
(3 pilares + eje de hemostasia), **16 calculadoras clínicas** (organizadas por momento
asistencial) y un **módulo de evaluación** con 200 preguntas, **progreso por usuario** y
**repaso espaciado (Leitner)**.

> ⚠️ **Apoyo docente, no dispositivo médico.** No sustituye al juicio clínico ni a los
> protocolos locales vigentes. Las calculadoras son estimaciones de planificación.

React 18 · Vite · TypeScript · `vite-plugin-pwa` (Workbox) · React Router (hash) · Vitest.

---

## Datos

La app consume los datos desde `app-data/` (en la **carpeta raíz del proyecto**, un nivel por
encima de `pbm-app/`):

- `content.json` — 23 documentos `{ code, title, module, pillar, anchor, level, core, coverHtml, bodyHtml, refsHtml }`
- `references.json` — 30 referencias `{ citation, doi, pmid }`
- `questions.json` — 200 preguntas `{ id, doc, module, level, q, options, answer, explanation, ref }`
- `content.md` — texto plano de los 23 documentos (buscador full-text)

`npm run sync-data` copia esos cuatro archivos a `public/app-data/` para que Vite los sirva y
Workbox los precachee (offline). Se ejecuta **automáticamente** antes de `dev` y `build`.
La fuente de verdad sigue siendo la carpeta raíz `app-data/`; nunca se editan los datos aquí.

## Requisitos

- Node 18+ y npm.

## Instalar

```bash
cd pbm-app
npm install
```

## Desarrollo

```bash
npm run dev
```

Abre la URL que indica Vite (por defecto `http://localhost:5173`). El service worker está
desactivado en modo dev; el resto de la app funciona con normalidad.

## Tests (Vitest)

```bash
npm test          # una pasada
npm run test:watch
```

Incluye, entre otros:

- **MABL**: varón 80 kg, 1,75 m, Hto 42→28 % ⇒ VSE ≈ 5,15 L y MABL ≈ 2060 ml.
- **Barajado del quiz**: tras barajar las opciones, `answer` sigue apuntando a la opción correcta
  (probado con 200 semillas).
- **Repaso espaciado (Leitner)**: acierto sube de caja y reprograma el repaso; fallo reinicia la
  caja; cálculo de tarjetas vencidas, no vistas y estadística de progreso.

## Lint y formato

```bash
npm run lint
npm run format
```

## Build de producción

```bash
npm run build      # genera dist/ (estático)
npm run preview    # sirve dist/ localmente para probar la PWA
```

`base` está configurado como `./` (rutas relativas), por lo que `dist/` funciona tanto en la
raíz de un dominio como en una **subruta** de GitHub Pages.

## Desplegar

### Netlify / cualquier hosting estático

Sube el contenido de `dist/`. No hace falta backend. Para que el *deep-linking* funcione con
hash-router no se necesita configuración especial (las rutas viven tras `#/`).

### GitHub Pages

1. `npm run build`
2. Publica el contenido de `dist/` en la rama/zona de Pages (p.ej. con la acción
   `actions/deploy-pages` o subiendo `dist/` a `gh-pages`).
3. Al usar `base: './'` y hash-router, la app carga correctamente en
   `https://<usuario>.github.io/<repo>/`.

## Instalación como app (PWA)

Con la app servida por HTTPS (o `localhost`), el navegador ofrece **Instalar**. Una vez
instalada, abre y funciona sin conexión: el app-shell y `app-data/` quedan precacheados.

---

## Estructura

```
pbm-app/
├─ public/
│  ├─ app-data/            # copiado por sync-data (no versionado)
│  ├─ icons/               # iconos PWA
│  └─ favicon.svg
├─ scripts/sync-data.mjs   # copia ../app-data → public/app-data
├─ src/
│  ├─ data/DataContext.tsx # carga JSON/MD en runtime
│  ├─ hooks/               # useQuiz, useTheme, useLocalStorage
│  ├─ lib/                 # calculators, quiz, search, html, references, structure (+ tests)
│  ├─ components/          # Layout, Badges, Disclaimer, calc/*
│  ├─ pages/               # Home, IndexPage, Reader, Calculators, Quiz, Search, About
│  ├─ styles/              # tokens.css (paleta granate/acero) + global.css
│  ├─ App.tsx              # rutas (hash router)
│  └─ main.tsx
├─ vite.config.ts          # plugin React + PWA (Workbox) + Vitest
└─ package.json
```

## Identidad visual

Granate `#8E2433` + acero `#4F6B7A`, alerta cálida `#B0682B`. Serif en titulares, sans en
texto. Tema **claro por defecto** y tema **oscuro** (toggle claro/oscuro/automático). Badges de
ancla de evidencia: GUÍA, META, ECA, REV, ALG.

## Privacidad

Sin backend ni telemetría. `localStorage` guarda **solo** preferencias de interfaz (tema, clave
`pbm_theme`), el histórico de puntuaciones del quiz (`pbm_quiz_history`) y el progreso del
repaso espaciado (`pbm_srs`: caja Leitner y fecha de próximo repaso por pregunta). **Nunca**
datos clínicos. El progreso es **local a este navegador** (sin perfiles ni cuentas); el botón
«Reiniciar progreso» en Evaluación lo borra.

## Funcionalidades destacadas

- **Lector** con estilos de la serie, índice lateral por secciones y referencias enlazadas (DOI/PMID).
- **16 calculadoras** organizadas por momento asistencial (preoperatorio, intraoperatorio,
  urgencia/hemorragia, postoperatorio): diagnóstico de anemia/ferropenia, Fe+EPO electiva y
  urgente, hierro carboximaltosa (Ganzoni) y sacarosa, indicación de EPO, MABL, TXA, umbral de
  hematíes, plaquetas (AABB/ICTMG 2025), plasma/fibrinógeno, HEMSTOP, antitrombóticos + BRIDGE,
  fármacos hemostáticos, antídotos anticoagulantes y anemia postoperatoria. Cada una muestra su
  fuente verificada y el descargo de juicio clínico.
- **Evaluación** con 6 modos + **repaso espaciado**: cada respuesta del quiz alimenta el sistema
  Leitner; «Repasar vencidas» y «Preguntas nuevas» programan sesiones; panel de progreso con
  vistas/dominadas/acierto y desglose por módulo. Aviso de «para repasar hoy» en Inicio.

---

Ideación y contenidos: **Emilio García Hernández** — FEA Anestesiología y Reanimación · CAUSA ·
SACYL (Salamanca).
