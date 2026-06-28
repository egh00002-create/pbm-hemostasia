# -*- coding: utf-8 -*-
"""build_reviewpack.py - Genera el paquete para revisores: rejillas CSV (capitulos y preguntas)
y las instrucciones. Salida en revision/."""
import json, csv, pathlib, html, re

BASE = pathlib.Path(__file__).resolve().parent
OUT = BASE / "revision"; OUT.mkdir(exist_ok=True)
def plain(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()

docs = json.load(open(BASE / "app-data" / "content.json", encoding="utf-8"))
qs = json.load(open(BASE / "app-data" / "questions.json", encoding="utf-8"))
L = ["A", "B", "C", "D"]

# Rejilla de capitulos
with open(OUT / "rejilla-capitulos.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["Codigo", "Titulo", "Modulo/Pilar", "Ancla", "Contenido correcto (Si/No/Parcial)",
                "Errores o matices a corregir", "Cifras/umbrales a revisar", "Revisor", "Fecha"])
    for d in docs:
        w.writerow([d["code"], plain(d["title"]), d["pillar"], d["anchor"], "", "", "", "", ""])

# Rejilla de preguntas
with open(OUT / "rejilla-preguntas.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["ID", "Cap", "Nivel", "Pregunta", "Respuesta marcada como correcta",
                "Correcta (Si/No)", "Distractor problematico", "Comentario", "Revisor"])
    for q in qs:
        w.writerow([q["id"], q["doc"], q["level"], plain(q["q"]),
                    L[q["answer"]] + ": " + plain(q["options"][q["answer"]]), "", "", "", ""])

print("CSV capitulos:", len(docs), "| CSV preguntas:", len(qs), "| en", OUT)
