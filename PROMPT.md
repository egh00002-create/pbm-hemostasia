# PROMPT ÚNICO — App PBM (pegar en Claude/Continue dentro de VSCodium)

> Abre ESTA carpeta en VSCodium y pega todo el bloque de abajo en el chat de Continue (modo Agent).
> La carpeta ya contiene los datos en `app-data/`: `content.json` (23 documentos), `references.json` (30 refs con DOI/PMID),
> `questions.json` (200 preguntas) y `content.md` (texto plano para búsqueda). No necesitas nada más.

---

Eres un ingeniero frontend senior. Crea una **PWA offline** en **React 18 + Vite + TypeScript** llamada
**"PBM — Hemostasia y Medicina Transfusional Perioperatoria"**, en **español**, que combine un **lector** de la serie
(23 documentos: 3 pilares + eje de hemostasia), **calculadoras clínicas** y un **módulo de evaluación** (200 preguntas).
Es apoyo docente, **no un dispositivo médico**: muestra en el pie y en cada herramienta/calculadora/quiz el texto
"No sustituye al juicio clínico ni a los protocolos locales vigentes".

DATOS (consúmelos desde `app-data/`, cárgalos en runtime, NO inventes contenido ni cifras):
- `content.json`: array de documentos `{ code, title, module, pillar, anchor (GUIA/META/ECA/REV/ALG), level (BASICO/AVANZADO), core (bool), coverHtml, bodyHtml, refsHtml }`. El contenido viene en HTML con entidades; renderízalo (dangerouslySetInnerHTML) reutilizando la paleta; decodifica entidades cuando necesites texto plano (título, búsqueda).
- `references.json`: `{ citation, doi, pmid }`. Enlaza por `https://doi.org/<doi>` o `https://pubmed.ncbi.nlm.nih.gov/<pmid>/`.
- `questions.json`: 200 ítems `{ id, doc, module, level: "basico"|"avanzado", q, options:[4], answer:0-3, explanation, ref:"PMID ..." }`.
- `content.md`: texto plano de los 23 documentos (úsalo para el buscador full-text).

REQUISITOS TÉCNICOS:
- PWA instalable y 100% offline (`vite-plugin-pwa` + Workbox; cachear app shell y `app-data/`). Routing con hash router.
- Sin backend. Estado con hooks. CSS Modules o Tailwind (uno, consistente). Mobile-first, táctil, modo oscuro.
- Accesibilidad AA (teclado, ARIA, toques ≥44px). ESLint + Prettier. Cálculos y lógica del quiz en funciones puras con tests Vitest.
- `localStorage` SOLO para preferencias de UI e histórico de puntuaciones del quiz (clave "pbm_quiz_history"); nunca datos clínicos.
- Build estático para GitHub Pages/Netlify + README (instalar, dev, build, desplegar).

IDENTIDAD VISUAL (tokens exactos):
`--accent:#8E2433` (granate), `--accent-soft:#F4E3E6`, `--accent2:#4F6B7A` (acero), `--accent2-soft:#E7EDF1`,
`--warm:#B0682B` (alertas), `--ink:#211A1C`, `--muted:#6E6168`, `--line:#E0D6D8`, `--bg:#FAF6F7`. Serif en titulares, sans en texto.
Badges de ancla: GUÍA #8E2433, META #4F6B7A, ECA #7A3E6E, REV #6E6358, ALG #4E5A66. Tema claro por defecto + oscuro.

ESTRUCTURA DE CONTENIDO (espina = 3 pilares + eje):
- Módulo 1 Fundamentos: PBM-01, 02, 03 · Módulo 2 Pilar 1 (masa eritrocitaria): PBM-04, 05, 06 ·
  Módulo 3 Pilar 2 (minimizar pérdida): PBM-07..11 · Módulo 4 Pilar 3 (tolerancia/transfusión): PBM-12, 13, 14 ·
  Módulo 5 Eje hemostasia: PBM-15..18 · Quick-reference (tarjetas ALG): P-QR-01..05.

PANTALLAS:
1. Inicio: tarjetas de los 3 pilares + eje, buscador global, accesos a calculadoras y evaluación.
2. Índice maestro: lista por módulos con badge de ancla, nivel y ★ (core).
3. Lector: render del documento (estilos de la serie), índice lateral, anterior/siguiente, referencias enlazadas por DOI.
4. Calculadoras (ver abajo).
5. Evaluación/Quiz (ver abajo).
6. Buscador full-text (sobre title + content.md).
7. Acerca de / descargo.

CALCULADORAS (usa EXACTAMENTE estos valores verificados; no los modifiques; cada una muestra su fuente y el descargo):
1) MABL: Nadler varón `VSE(L)=0.3669*talla^3+0.03219*peso+0.6041`; mujer `0.3561*talla^3+0.03308*peso+0.1833`.
   Gross `MABL=VSE_ml*(Hto_ini-Hto_diana)/((Hto_ini+Hto_diana)/2)`. Aviso: "estimación de planificación, no disparador de transfusión".
   Caso de test: varón 80 kg, 1,75 m, Hto 42→28% ⇒ VSE≈5,15 L, MABL≈2060 ml.
2) Umbrales hematíes: <7 (estable/crítico/séptico); <7,5 (cardíaca); <8 (ortopedia/ECV crónica); **SCA → liberal ≈10** (en contra de restrictivo). 1 U≈+1 g/dl.
3) Plaquetas (AABB/ICTMG 2025): <10 (profilaxis/CVC compresible); <20 (PL/RI bajo riesgo); <50 (cirugía mayor no neuroaxial/RI alto riesgo);
   **no** transfundir en cirugía cardiovascular sin sangrado ni en HIC no quirúrgica con plaquetas >100 (incl. antiagregantes).
4) Plasma: sangrado/procedimiento con coagulopatía, 10–15 ml/kg; no por INR/TTPa leve sin sangrado. Fibrinógeno/crio: <1,5 g/l o déficit funcional.
5) TXA por escenario: trauma 1 g/10 min + 1 g/8 h (<3 h); HPP 1 g repetible; TCE leve-moderado 1 g+1 g/8 h (<3 h, limitado en TCE grave);
   cirugía bolo+infusión (vigilar convulsiones a dosis altas). Mensaje fijo: "cuanto antes, mejor".
6) HEMSTOP: 7 ítems sí/no (Hematoma, hEmorragia, Menorragia, Surgery, Tooth, Obstetrics, Parents); **≥2 → estudio dirigido + hematología**.
7) Antitrombóticos: decisión por fármaco × riesgo trombótico × riesgo hemorrágico; incluir BRIDGE (no puente en FA: no inferior y menos hemorragia);
   "los tiempos exactos de suspensión se toman del protocolo local y la ficha técnica".

EVALUACIÓN (QUIZ) con `app-data/questions.json`:
- Tipo TS `QuizQuestion { id:string; doc:string; module:number; level:'basico'|'avanzado'; q:string; options:string[]; answer:number; explanation:string; ref:string }`.
- Selector de MODO: Rápido (10 al azar), Por módulo, Por pilar, Por documento, Por nivel, Completo (200).
- Barajar preguntas y también las opciones (recalculando el índice correcto). Vista pregunta a pregunta con progreso.
- Al responder: marcar acierto/error, mostrar `explanation` y enlace a la fuente (PMID→PubMed, o DOI desde references.json).
- Resultados: puntuación y %, desglose por módulo/pilar y nivel, lista de fallos con enlace al documento (`doc`) para repasar.
- Histórico en localStorage ("pbm_quiz_history"). No modifiques questions.json.
- Test Vitest obligatorio: tras barajar las opciones, `answer` sigue apuntando a la opción correcta.

REGLAS INNEGOCIABLES:
1. No inventes ni alteres cifras clínicas (umbrales, dosis, fórmulas) ni referencias: usa solo `app-data/` y este prompt.
2. Cada calculadora y cada corrección del quiz muestran fuente (DOI/PMID) y el descargo de juicio clínico.
3. Conserva los matices de honestidad: SCA→umbral liberal; PREVENTT neutro; CRASH-3 limitado en TCE grave;
   no plasma por analítica sin sangrado; BRIDGE en contra del puente sistemático.
4. Funciones puras + tests Vitest (incluye el caso MABL y el de barajado del quiz).

ENTREGABLES: genera el proyecto completo (estructura, package.json, config PWA, componentes, hook useQuiz, utils, tests, README).
Empieza proponiendo el árbol de archivos y luego impleméntalo.
