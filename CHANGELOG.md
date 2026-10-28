# Changelog — Serie PBM (Hemostasia y Medicina Transfusional Perioperatoria)

Formato: versión · fecha · cambios. Próxima revisión de evidencia prevista: **2027**.

## v1.1.1 — 2026-10
Correcciones técnicas del motor de ferropenia de la app (Fase 2a de la auditoría). **Sin cambios de criterio
clínico**: umbrales y matrices del PTC-ANR-22-01-01 intactos.
- **Motor único.** Diagnóstico, derivación y Fe + EPO salen de un solo motor (`ironDiagnosisCausa` +
  `causaDerivar` + `causaPreopPlan`). La regla «anemia + IST ≥ 20 % → derivar» ya no está duplicada entre la
  pantalla de diagnóstico y la matriz electiva.
- **Motor antiguo retirado.** `ironStatusOf` / `assessPreopAnemia` no los usaba ninguna pantalla y su lógica
  divergía del protocolo; se eliminan junto con sus tests.
- **Validación de entradas.** Si Hb, ferritina, IST, Ret-Hb o peso no son numéricos, son negativos o la IST
  supera el 100 %, el resultado queda bloqueado y se indica qué campo falla. Antes, una IST no numérica daba
  «normal» y, en electiva, se saltaba la derivación y se pautaba hierro.
- **PCR no aportada.** El resultado «normal» de la pantalla de diagnóstico se rotula ahora «Patrón férrico
  normal — inflamación no evaluada (PCR no aportada)». La clasificación no cambia.
- **Cirugía urgente (Fig. 13).** Nuevo campo IST. Con IST < 20 % la pauta no cambia. Con IST ≥ 20 % o sin IST,
  la app ya no calcula pauta («Fuera del algoritmo de la Figura 13; valorar individualmente»), porque la tabla
  del protocolo solo cubre IST < 20 %. Caso afectado: ferritina 70 + IST 24 % daba antes hierro IV 500 mg + EPO.
- **Comentario de Ret-Hb unificado.** El criterio diagnóstico es el de la Figura 7 (25–28 pg, 28 incluido =
  DFH); el «< 28» de la Fig. 15 se documenta como rótulo de otro contexto. La lógica no cambia.
- **Tests de regresión** (+11): límites de ferritina 30/100, IST 20 %, PCR 5 mg/L y Ret-Hb 25/28 pg;
  entradas inválidas; el caso de la auditoría en las tres pantallas.

## v1.1.0 — 2026-06
Revisión de las fuentes que quedaban pendientes de confirmar; dos resultaron ya publicadas y verificables y se
**incorporan** al contenido.
- ✅ **WHO — *Guidance on implementing patient blood management to improve global blood health status*** (OMS, marzo
  2025): ISBN 978-92-4-010466-2 · `https://iris.who.int/handle/10665/380784`. Verificada en **WHO IRIS** (no indexada
  en PubMed). **Incorporada** a PBM-01 §4 (marco de guías) y a la bibliografía maestra como ancla `GUÍA`.
- ✅ **NICE NG24 — actualización de ácido tranexámico** (NICE, publicada **26-feb-2026**, ya no borrador):
  `https://www.nice.org.uk/guidance/ng24`. Verificada en la web oficial de NICE. Cambio clave: se **elimina la
  estimación de pérdida sanguínea** y se ofrece TXA en *cualquier procedimiento con riesgo hemorrágico*; fuera de
  quirófano, si pérdida prevista >500 ml (adultos) o >10 % del volumen sanguíneo (niños 1–15 años). **Incorporada** a
  PBM-08 (§6) y P-QR-03, y a la bibliografía maestra como ancla `GUÍA`.
- ⚠️ **Revisión de hierro IV en *Blood Transfusion* (ene-2025)**: **no confirmada** — no se ha podido identificar con
  certeza el artículo concreto. Sigue **sin citar como ancla** hasta disponer de la cita exacta.
- Documentación de la app sincronizada: **16 calculadoras** (antes se indicaban 7) en `pbm-app/README.md` y
  `.continue/rules/pbm-app.md`.
- Bibliografía maestra: 30 → **32 referencias**. PDFs, dosieres, libro y `app-data/` regenerados.

## v1.0.0 — 2026-06
Primera edición completa.
- 18 documentos (PBM-01…18) + 5 quick-reference (P-QR-01…05), por 3 pilares + eje de hemostasia.
- Bibliografía: 30 referencias verificadas contra PubMed (autoría, título, revista, año, DOI/PMID).
- Actualización de evidencia 2024–2025 incorporada y verificada (AABB plaquetas 2025, CHEST 2024, EACTS 2024,
  metaanálisis SCA NEJM Evidence, Cochrane umbrales 2025, BSH anemia 2024, etc.).
- Cuestionario de **200 preguntas** con soluciones razonadas; revisión psicométrica: posición de la respuesta
  correcta reequilibrada a 50/50/50/50 (A/B/C/D).
- **Libro** `PBM-libro.pdf` (≈122 pp): portada, créditos, prólogo, índice temático con números de página,
  cabeceras de página, numeración romana (preliminares) + arábiga (cuerpo), glosario, bibliografía maestra,
  **5 algoritmos en figura** y **índice analítico**.
- Capa de datos para la app en `app-data/` (content.json, content.md, references.json, questions.json) + prompt único.
- Paquete de revisión por pares en `revision/`.

### Pendiente / en revisión
- Fuentes no indexadas en PubMed pendientes de confirmar (no citadas como ancla hasta confirmarse): revisión de hierro
  en *Blood Transfusion* (ene-2025). *(WHO PBM 2025 y NICE NG24 TXA 2026 confirmadas e incorporadas en v1.1.0.)*
- Revisión clínica externa por pares (rejillas en `revision/`).
