---
name: PBM App — reglas del proyecto
description: Reglas permanentes para construir la PWA PBM (Continue / Claude en VSCodium)
alwaysApply: true
---

# Reglas para la app PBM (Hemostasia y Medicina Transfusional Perioperatoria)

Construyes una **PWA offline en React + Vite + TypeScript**: lector de 23 documentos (3 pilares + eje de hemostasia) +
16 calculadoras clínicas organizadas por momento asistencial. Interfaz en **español**. Es apoyo docente, **no un dispositivo médico**.

## Fuente de datos (úsala, no la reinventes)
- El contenido de los 23 documentos está en `app-data/content.json` (campos: code, title, module, pillar, anchor,
  level, core, coverHtml, bodyHtml, refsHtml). Renderiza el HTML reutilizando la paleta del proyecto.
- Las referencias están en `app-data/references.json` (citation, doi, pmid). Enlaza por `https://doi.org/<doi>`.
- El banco de evaluación está en `app-data/questions.json` (200 ítems tipo test): campos
  `id, doc, module, level, q, options[4], answer (0-3), explanation, ref (PMID)`. Inclúyelo como pantalla "Evaluación"
  (modos: rápido 10, por módulo/pilar, por documento, por nivel, completo). Tras responder muestra explicación + enlace
  a la fuente; al final, puntuación y repaso de fallos enlazando al documento.
- Para regenerar estos JSON: `python export_content.py` (contenido), `python export_markdown.py` (Markdown plano).

## Innegociables (seguridad clínica)
1. **No inventes ni alteres cifras clínicas** (umbrales, dosis, fórmulas) ni referencias. Si un dato no está en
   `app-data/` o en el PROMPT, no lo pongas.
2. Cada calculadora muestra su(s) fuente(s) con enlace al DOI y el texto: *"No sustituye al juicio clínico ni a los
   protocolos locales vigentes."*
3. Conserva siempre los **matices de honestidad**: SCA → umbral liberal (≈10 g/dl); PREVENTT neutro; CRASH-3 limitado en
   TCE grave; no transfundir plasma por analítica alterada sin sangrado; BRIDGE en contra del puente sistemático en FA.
4. Los cálculos van en **funciones puras** con **tests Vitest**. Caso de control MABL: varón 80 kg, 1,75 m, Hto 42→28 %
   ⇒ VSE ≈ 5,15 L, MABL ≈ 2060 ml.

## Datos de las calculadoras (valores verificados)
- **MABL:** Nadler varón `0.3669*talla^3+0.03219*peso+0.6041`; mujer `0.3561*talla^3+0.03308*peso+0.1833` (L).
  Gross: `MABL = VSE_ml*(Hto_ini-Hto_diana)/((Hto_ini+Hto_diana)/2)`.
- **Umbrales hematíes:** <7 (estable/crítico/séptico); <7,5 (cardíaca); <8 (ortopedia/ECV crónica); **SCA → ≈10 liberal**.
- **Plaquetas (AABB/ICTMG 2025):** <10 (profilaxis/CVC compresible); <20 (PL/RI bajo riesgo); <50 (cirugía mayor no
  neuroaxial/RI alto riesgo); **no** en cirugía cardiovascular sin sangrado ni HIC no quirúrgica con plaquetas >100.
- **Plasma:** sangrado/procedimiento con coagulopatía, 10–15 ml/kg; no por INR/TTPa leve sin sangrado.
- **Fibrinógeno/crio:** <1,5 g/l o déficit funcional en sangrado.
- **TXA:** trauma 1 g/10 min + 1 g/8 h (<3 h); HPP 1 g repetible; TCE leve-moderado 1 g+1 g/8 h (<3 h); cirugía bolo+infusión.
- **HEMSTOP:** 7 ítems sí/no; **≥2 → estudio dirigido + hematología**.
- **Antitrombóticos:** decisión por fármaco × riesgo trombótico × riesgo hemorrágico; tiempos exactos del protocolo local.

## Estilo
- Paleta: `--accent:#8E2433` (granate), `--accent2:#4F6B7A` (acero), `--warm:#B0682B` (alertas), `--bg:#FAF6F7`.
- Badges de ancla: GUÍA #8E2433, META #4F6B7A, ECA #7A3E6E, REV #6E6358, ALG #4E5A66.
- Mobile-first, accesibilidad AA, modo oscuro. Sin `localStorage` para datos clínicos (sí para preferencias de UI).
