# Proyecto — Hemostasia y Medicina Transfusional Perioperatoria (PBM) (serie formativa)

> **Cómo usar este archivo:** esta carpeta vive en `Documents/Claude/Projects/PBM`, junto a las series hermanas (BIS, neuroanestesia, traumatología, urología, CMA, prehabilitación, vía aérea difícil). Selecciónala en Cowork y di: *"Lee CLAUDE.md y arranca por PBM-01"*. Incluye el pipeline `build_doc.py`, `template.html`, `render_pdf.py` y `build_dossier.py` con la paleta de esta serie. Instrucciones de carpeta para Cowork; léelas al inicio de cada sesión antes de tocar archivos o renderizar.

---

## 1. Qué es este proyecto

Serie formativa de PDFs en español sobre **gestión de la sangre y del sangrado perioperatorio** —el *Patient Blood Management* (PBM) y la hemostasia/medicina transfusional perioperatoria—, paralela a las series ya existentes (BIS, CMA, neuroanestesia, traumatología, urología, prehabilitación). Mismo pipeline: **HTML templado + WeasyPrint**.

- Autor / destinatario: Emilio García Hernández (FEA Anestesiología y Reanimación, CAUSA / SACYL, Salamanca).
- Idioma: **español**. Audiencia: anestesiólogos adjuntos y residentes; útil para hematología, cirugía y enfermería perioperatoria.
- **Espina conceptual = los 3 pilares del PBM + el eje transversal de la hemostasia y el sangrado**: (1) optimizar la masa eritrocitaria; (2) minimizar la pérdida sanguínea; (3) optimizar y tolerar la anemia; (4) eje transversal: evaluación y manejo del sangrado/coagulopatías. Todo documento debe poder situarse en un pilar o en el eje.
- Acento visual: **granate `#8E2433` + gris acero `#4F6B7A`** (distinto de BIS —petróleo/verde—, CMA —índigo/turquesa— y trauma/uro —terracota/ámbar—). Tono cálido `#B0682B` solo para alertas.
- Índice maestro y estado vivo: `indice-maestro-pbm.html` (actualízalo al cerrar cada documento: `.dot.pend` → `.prog` → `.done`).
- **Antecedente:** existieron intentos de *app* (en `Desktop/pbm/pbm-perioperative` y `Desktop/Hemostatic care/app`) y abundante material fuente (guías BSH, HEMSTOP, TEG/ROTEM, EPO, MABL). Se decide formato de **serie de texto**, igual que con BIS. El material útil se referencia desde `material-fuente/`.

---

## 2. Estructura de la serie

18 documentos en 5 módulos (`PBM-01 … PBM-18`) + 5 quick-reference (`P-QR-01 … P-QR-05`). Los ★ son núcleo. La fuente de verdad del estado, ancla y nivel es `indice-maestro-pbm.html`.

**Módulo 1 — Fundamentos: PBM y medicina transfusional**
- PBM-01 ★ Qué es el PBM: los 3 pilares y el marco perioperatorio — *cabeza de serie*
- PBM-02 ★ Componentes sanguíneos y sus indicaciones (hematíes, plasma, plaquetas)
- PBM-03 Seguridad transfusional: identificación, trazabilidad y reacciones adversas

**Módulo 2 — Pilar 1: optimizar la masa eritrocitaria**
- PBM-04 ★ Diagnóstico y manejo de la anemia preoperatoria
- PBM-05 ★ Ferropenia y hierro intravenoso
- PBM-06 Eritropoyetina (EPO) en PBM: evidencia y uso

**Módulo 3 — Pilar 2: minimizar la pérdida sanguínea**
- PBM-07 ★ Hemostasia perioperatoria: fisiología y estrategia de minimización
- PBM-08 ★ Antifibrinolíticos: ácido tranexámico (CRASH-2/3, WOMAN, ATACAS)
- PBM-09 Pruebas viscoelásticas (ROTEM/TEG) y algoritmos guiados
- PBM-10 Recuperación celular intraoperatoria y técnicas de ahorro
- PBM-11 Pérdida sanguínea admisible (MABL): cálculo y planificación

**Módulo 4 — Pilar 3: tolerancia a la anemia y transfusión**
- PBM-12 ★ Umbrales restrictivos de transfusión (TRICC, TRISS, REALITY)
- PBM-13 ★ Hemorragia crítica y protocolo de transfusión masiva
- PBM-14 Optimización de la tolerancia a la anemia: fisiología y límites

**Módulo 5 — Hemostasia clínica y paciente con riesgo hemorrágico**
- PBM-15 ★ Cribado del riesgo hemorrágico preoperatorio (HEMSTOP)
- PBM-16 ★ Manejo perioperatorio de antiagregantes y anticoagulantes
- PBM-17 Coagulopatías congénitas y adquiridas en cirugía
- PBM-18 Fármacos hemostáticos (CCP, fibrinógeno, rFVIIa, desmopresina)

**Quick-reference (P-QR)**
- P-QR-01 ★ Los 3 pilares del PBM de un vistazo
- P-QR-02 ★ Umbrales de transfusión por componente
- P-QR-03 ★ Ácido tranexámico: dosis por escenario
- P-QR-04 ★ MABL rápido (volumen sanguíneo de Nadler + Gross)
- P-QR-05 Manejo de antitrombóticos según fármaco y riesgo

---

## 3. Sistema de anclas de evidencia (CRÍTICO)

- `GUÍA` — NBA *Patient Blood Management Guidelines* (Módulos 1–6); guías **BSH**; recomendaciones **SEDAR**/ESAIC; AABB.
- `META` — revisión sistemática / metaanálisis (hierro IV, EPO, viscoelástica, transfusión restrictiva).
- `ECA` — ensayo pivotal (TRICC, TRISS, REALITY; CRASH-2/3, WOMAN, ATACAS).
- `REV` — revisión narrativa / síntesis.
- `ALG` — algoritmo / tarjeta.

### Reglas de verificación (heredadas de BIS)
- **NO inventar fuentes.** Verificar cada cita contra PubMed (autoría + título + revista + año + DOI/PMID juntos) antes de darla por buena.
- **Presentar la evidencia con honestidad.** Beneficios sólidos (ácido tranexámico reduce sangrado/transfusión; umbrales restrictivos no inferiores y a menudo mejores; hierro IV en ferropenia) frente a áreas más discutidas (EPO sin señal en mortalidad; viscoelástica con heterogeneidad; umbral exacto por contexto).
- Material de fabricante o de plataformas (BloodSafe, BloodSafe es **solo referencia de arquitectura**, no contenido) se cita como tal, no como evidencia.
- Cada documento incluye una **sección de verificación bibliográfica** al final.

---

## 4. Pipeline y archivos

- `build_doc.py` — CSS maestra (granate/acero) + `build()`; un `.html`+`.pdf` por documento.
- `template.html` — esqueleto de referencia. `render_pdf.py` — alternativa Playwright (en sandbox usar WeasyPrint).
- `indice-maestro-pbm.html` — índice/estado vivo. `_build_pbmNN.py` / `_build_pqrNN.py` — un script por documento (META/COVER/BODY/REFS + `build()`).
- `build_dossier.py` — dosier único `PBM-dosier-completo.pdf` (omite los no construidos).
- `build_all.py` — punto de entrada único: reconstruye PDFs → dosier → cuestionario → `app-data/` → revisión → `PBM-libro.pdf` (`--solo-libro` para solo el libro).
- Salida: `PBM-NN-slug.pdf` / `P-QR-NN-slug.pdf`. Render: `pip install weasyprint --break-system-packages`.
- **Entorno de render (Windows).** WeasyPrint necesita las librerías nativas **GTK/Pango** además del paquete Python. Si faltan
  (`OSError: cannot load library 'libgobject-2.0-0'`), `build()` degrada con elegancia: **escribe el HTML pero el PDF da
  `PDF-ERROR`**. En esta máquina están instaladas vía **MSYS2** (`C:\msys64`, `pacman -S mingw-w64-x86_64-pango`). El
  intérprete con `weasyprint` es **Python 3.14** (`py -3.14`). Para renderizar, añade la carpeta de DLLs al PATH antes del
  build (PowerShell):

  ```powershell
  $env:PATH = "C:\msys64\mingw64\bin;$env:PATH"; py -3.14 build_all.py
  ```

  En sandbox/Linux basta `pip install weasyprint` (las libs suelen estar presentes).

---

## 5. Material fuente ya disponible (Escritorio)

- `Desktop/pbm/`: guía BSH 2024 (Lester); algoritmo MABL (Nadler/Gross) → PBM-11, P-QR-04; EPO metaanálisis 2026 → PBM-06; artículos Rev Esp Anestesiol.
- `Desktop/Hemostatic care/`: HEMSTOP → PBM-15, P-QR-05; díptico TEG/ROTEM → PBM-09; BSH 2014 trastornos raros → PBM-17; componentes sanguíneos → PBM-02; nota AEMPS antitrombóticos → PBM-16/18.
- BloodSafe eLearning Australia: referencia de **arquitectura** y puente a las guías **NBA** (anclas GUÍA). No reutilizar su contenido (copyright).

---

## 6. Convenciones

- Numeración estable; cabecera con código + badge + módulo; mensaje nuclear equilibrado; índice; secciones numeradas; perlas; bibliografía verificada; nota de verificación.
- Conectar con series hermanas: **CMA/prehabilitación** (optimización preoperatoria), **traumatología** (hemorragia crítica, tranexámico), **BIS** (mismo método y tono honesto).
- Pie estándar + línea de Ideación de Emilio García Hernández (ya la añade `build_doc.py`).
- Antes de marcar `done`, pasar la verificación bibliográfica de la §3.

---

*Kit de continuidad para reproducir el método de las series de anestesia aplicado a PBM y hemostasia perioperatoria. Autor/destinatario: Emilio García Hernández — Licenciado Especialista en Anestesiología y Reanimación · CAUSA · SACYL.*
