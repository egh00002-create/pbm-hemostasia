# -*- coding: utf-8 -*-
"""Exporta el contenido de la serie PBM a JSON limpio para la app (sin dependencia de los scripts en ejecucion).
Genera: app-data/content.json (23 documentos con cover/body/refs en HTML ya estilable) y app-data/references.json."""
import importlib, json, re, pathlib

BASE = pathlib.Path(__file__).resolve().parent
OUT = BASE / "app-data"; OUT.mkdir(exist_ok=True)

# code -> (modulo, pilar, ancla, nivel, nucleo)
META = {
 "PBM-01": ("Modulo 1 - Fundamentos", "Fundamentos", "GUIA", "BASICO", True),
 "PBM-02": ("Modulo 1 - Fundamentos", "Fundamentos", "GUIA", "BASICO", True),
 "PBM-03": ("Modulo 1 - Fundamentos", "Fundamentos", "GUIA", "BASICO", False),
 "PBM-04": ("Modulo 2 - Pilar 1: masa eritrocitaria", "Pilar 1", "GUIA", "BASICO", True),
 "PBM-05": ("Modulo 2 - Pilar 1: masa eritrocitaria", "Pilar 1", "META", "BASICO", True),
 "PBM-06": ("Modulo 2 - Pilar 1: masa eritrocitaria", "Pilar 1", "META", "AVANZADO", False),
 "PBM-07": ("Modulo 3 - Pilar 2: minimizar perdida", "Pilar 2", "REV", "BASICO", True),
 "PBM-08": ("Modulo 3 - Pilar 2: minimizar perdida", "Pilar 2", "ECA", "BASICO", True),
 "PBM-09": ("Modulo 3 - Pilar 2: minimizar perdida", "Pilar 2", "META", "AVANZADO", False),
 "PBM-10": ("Modulo 3 - Pilar 2: minimizar perdida", "Pilar 2", "META", "AVANZADO", False),
 "PBM-11": ("Modulo 3 - Pilar 2: minimizar perdida", "Pilar 2", "REV", "BASICO", False),
 "PBM-12": ("Modulo 4 - Pilar 3: tolerancia/transfusion", "Pilar 3", "ECA", "BASICO", True),
 "PBM-13": ("Modulo 4 - Pilar 3: tolerancia/transfusion", "Pilar 3", "GUIA", "BASICO", True),
 "PBM-14": ("Modulo 4 - Pilar 3: tolerancia/transfusion", "Pilar 3", "REV", "AVANZADO", False),
 "PBM-15": ("Modulo 5 - Eje hemostasia clinica", "Eje hemostasia", "REV", "BASICO", True),
 "PBM-16": ("Modulo 5 - Eje hemostasia clinica", "Eje hemostasia", "GUIA", "AVANZADO", True),
 "PBM-17": ("Modulo 5 - Eje hemostasia clinica", "Eje hemostasia", "REV", "AVANZADO", False),
 "PBM-18": ("Modulo 5 - Eje hemostasia clinica", "Eje hemostasia", "REV", "AVANZADO", False),
 "P-QR-01": ("Quick-reference", "Tarjetas", "ALG", "BASICO", True),
 "P-QR-02": ("Quick-reference", "Tarjetas", "ALG", "BASICO", True),
 "P-QR-03": ("Quick-reference", "Tarjetas", "ALG", "BASICO", True),
 "P-QR-04": ("Quick-reference", "Tarjetas", "ALG", "BASICO", True),
 "P-QR-05": ("Quick-reference", "Tarjetas", "ALG", "AVANZADO", False),
}
ORDER = [("PBM-%02d" % i, "_build_pbm%02d" % i) for i in range(1, 19)] + \
        [("P-QR-%02d" % i, "_build_pqr%02d" % i) for i in range(1, 6)]

TITLE_RE = re.compile(r'<h1 class="title">(.*?)</h1>', re.S)
DOI_RE = re.compile(r'doi:([^\s<]+)')
PMID_RE = re.compile(r'PMID\s*([0-9]+)')

def clean(s):
    return re.sub(r'\s+', ' ', s).strip()

docs = []
refs_seen = {}
for code, mod_name in ORDER:
    m = importlib.import_module(mod_name)
    title = clean(TITLE_RE.search(m.COVER).group(1)) if TITLE_RE.search(m.COVER) else code
    mod, pillar, anchor, level, core = META[code]
    docs.append({
        "code": code, "title": title, "module": mod, "pillar": pillar,
        "anchor": anchor, "level": level, "core": core,
        "coverHtml": m.COVER.strip(), "bodyHtml": m.BODY.strip(), "refsHtml": m.REFS.strip(),
    })
    # extraer referencias (doi + pmid) de cada <li> de REFS
    for li in re.findall(r'<li>(.*?)</li>', m.REFS, re.S):
        doi = DOI_RE.search(li); pmid = PMID_RE.search(li)
        key = (pmid.group(1) if pmid else (doi.group(1) if doi else li[:40]))
        if key not in refs_seen:
            refs_seen[key] = {
                "citation": clean(re.sub(r'<[^>]+>', '', li)),
                "doi": doi.group(1).rstrip('.') if doi else None,
                "pmid": pmid.group(1) if pmid else None,
            }

(OUT / "content.json").write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
(OUT / "references.json").write_text(json.dumps(list(refs_seen.values()), ensure_ascii=False, indent=2), encoding="utf-8")
print("Documentos exportados:", len(docs))
print("Referencias unicas:", len(refs_seen))
print("Salida:", OUT)
