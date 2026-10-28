# Serie PBM — Hemostasia y Medicina Transfusional Perioperatoria

Manual docente sobre *Patient Blood Management* (PBM) y hemostasia perioperatoria, en español, para anestesiólogos
adjuntos y residentes (CAUSA / SACYL). **Versión 1.1.1** (ver `VERSION` y `CHANGELOG.md`).

> Material **docente**. No es un dispositivo médico ni una guía oficial. **No sustituye al juicio clínico ni a los
> protocolos locales vigentes.** Cifras verificadas contra PubMed; los tiempos y dosis se confirman con la ficha técnica
> y el protocolo del centro.

## Qué entregable usar
- **`PBM-libro.pdf`** — el libro completo (lo recomendado): 23 capítulos + cuestionario + glosario + bibliografía +
  algoritmos + índice analítico, con índice paginado y cabeceras.
- **`PBM-cuestionario-200.pdf`** — examen de 200 preguntas + soluciones (para imprimir/evaluar).
- **`PBM-NN-*.pdf` / `P-QR-NN-*.pdf`** — cada documento/tarjeta por separado.
- **`PBM-dosier-completo.pdf`** y **`PBM-dosier-completo-cuestionario.pdf`** — versiones previas del dosier sin formato
  de libro (se conservan; el libro las sustituye).
- **`indice-maestro-pbm.html`** — índice/estado vivo de la serie.

## Datos para la app
`app-data/`: `content.json` (23 documentos), `content.md` (texto plano), `references.json` (30 refs con DOI/PMID),
`questions.json` (200 preguntas). Para construir la app: abrir la carpeta en VS Code/VSCodium y usar `PROMPT.md`
(reglas en `.continue/rules/`).

## Reconstruir
- Todo: `python build_all.py`
- Solo el libro: `python build_all.py --solo-libro`  (o `python build_libro5.py`)
- Requiere: `pip install weasyprint`. Datos de la app: `python export_content.py` y `python export_markdown.py`.
- Cuestionario PDF: `python make_quiz_pdf.py`. Reequilibrar posiciones del test: `python fix_quiz.py`.

## Revisión por pares
`revision/`: `instrucciones-revisores.md` + `rejilla-capitulos.csv` + `rejilla-preguntas.csv`. Devolver los CSV
cumplimentados; las correcciones se registran en `CHANGELOG.md` con nueva versión.

## Pendiente
- Verificar por web oficial (no PubMed): hierro *Blood Transfusion* 2025 (sin confirmar). *(WHO PBM 2025 y NICE NG24
  TXA 2026 ya verificadas e incorporadas en v1.1.0.)*
- Revisión clínica externa.

*Ideación: Emilio García Hernández — Licenciado Especialista en Anestesiología y Reanimación · CAUSA · SACYL.*
