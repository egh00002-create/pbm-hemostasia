# Revisión por pares — Serie PBM (Hemostasia y Medicina Transfusional Perioperatoria)

Gracias por revisar este material **docente**. El objetivo es validar la **exactitud clínica** del contenido y del
cuestionario antes de difundirlo. No es una guía oficial; no sustituye al juicio clínico ni a los protocolos locales.

## Qué revisar
- **Libro completo:** `PBM-libro.pdf` (capítulos PBM-01…18, tarjetas P-QR, cuestionario, glosario, bibliografía, algoritmos, índice).
- **Foco:** cifras y umbrales (Hb, plaquetas, fibrinógeno, dosis de TXA, MABL), indicaciones, y los **matices de evidencia**
  (SCA liberal, PREVENTT neutro, CRASH-3 en TCE grave, BRIDGE contra el puente, baja certeza de la viscoelástica).

## Cómo anotar
1. **Capítulos** → `rejilla-capitulos.csv` (una fila por documento). Marca *Sí / No / Parcial*, y describe errores, matices
   o cifras a revisar. Abre con Excel/LibreOffice (separador `;`, UTF-8).
2. **Preguntas** → `rejilla-preguntas.csv` (una fila por pregunta, 200). Indica si la respuesta marcada es correcta,
   si algún distractor es ambiguo/también válido, y un comentario.
3. Pon tu **nombre y fecha** en las columnas correspondientes.

## Criterios sugeridos
- ¿La cifra/umbral coincide con la guía citada (AABB, ESAIC, EACTS, BSH) o el ensayo (TRICC, CRASH-2, etc.)?
- ¿La “mejor respuesta” es inequívoca? ¿Hay un distractor defendible?
- ¿Falta algún matiz de seguridad relevante (contraindicación, excepción)?
- ¿Algo está desactualizado respecto a una guía más reciente?

## Devolución
Devuelve los dos CSV cumplimentados. Las correcciones se aplicarán al banco (`app-data/questions.json`) y a los scripts
de cada capítulo, y se registrarán en `CHANGELOG.md` con una nueva versión.

> Bibliografía verificada contra PubMed (DOI/PMID) en el Apéndice B del libro. Fuentes aún no indexadas (WHO 2025,
> NICE TXA, *Blood Transfusion* hierro 2025) están marcadas como **pendientes** y no se citan como ancla.
