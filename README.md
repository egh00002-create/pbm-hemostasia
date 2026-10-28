# PBM — Hemostasia y Medicina Transfusional Perioperatoria

Serie formativa en español sobre **Patient Blood Management (PBM)** y hemostasia perioperatoria
para anestesiólogos adjuntos y residentes (CAUSA / SACYL). Incluye los textos, un cuestionario,
el libro completo y una **PWA docente offline**.

### 🔗 App en vivo: **https://egh00002-create.github.io/pbm-hemostasia/**

> ⚠️ **Material docente. No es un dispositivo médico ni una guía oficial.** No sustituye al juicio
> clínico ni a los protocolos locales vigentes. Las cifras están verificadas contra PubMed (o la
> web oficial del organismo emisor en el caso de las guías); las dosis y tiempos se confirman con
> la ficha técnica y el protocolo del centro.

## Contenido

- **23 documentos** — 18 capítulos (PBM-01…18) + 5 tarjetas de consulta rápida (P-QR-01…05),
  estructurados en los **3 pilares del PBM** + el eje transversal de la hemostasia.
- **Cuestionario de 200 preguntas** con soluciones razonadas (`PBM-cuestionario-200.pdf`).
- **Libro completo** `PBM-libro.pdf` (≈123 pp): portada, índice paginado, glosario, bibliografía
  maestra (**32 referencias verificadas**), algoritmos en figura e índice analítico.
- **PWA** (`pbm-app/`): lector de la serie + **16 calculadoras clínicas** + evaluación con repaso
  espaciado. Instalable y **100 % offline**, sin backend ni telemetría.

Versión **1.1.1** — ver [`CHANGELOG.md`](CHANGELOG.md). Guía de uso de los entregables en
[`LEEME.md`](LEEME.md); detalles de la app en [`pbm-app/README.md`](pbm-app/README.md).

## Reconstruir

```bash
# Documentos, dosier, cuestionario, datos de la app y libro (requiere WeasyPrint + GTK):
python build_all.py            # en Windows, ver nota de entorno en CLAUDE.md §4

# La PWA:
cd pbm-app && npm install && npm run build
```

El despliegue de la PWA es **automático**: cada push que toque `pbm-app/**` o `app-data/**`
dispara el workflow [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml), que recompila
y republica en GitHub Pages.

## Privacidad

La app no tiene backend ni telemetría. `localStorage` guarda **solo** preferencias de interfaz y
el progreso del cuestionario/repaso; **nunca** datos clínicos.

---

*Ideación y contenidos: **Emilio García Hernández** — Licenciado Especialista en Anestesiología y
Reanimación · CAUSA · SACYL (Salamanca).*
