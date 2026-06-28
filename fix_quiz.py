# -*- coding: utf-8 -*-
"""fix_quiz.py - Revision psicometrica del banco: reequilibra la posicion de la respuesta correcta
(25% A/B/C/D) reordenando las opciones de cada pregunta de forma determinista. No cambia el contenido
clinico ni la opcion correcta; solo su posicion. Reescribe app-data/questions.json."""
import json, random, collections, pathlib

BASE = pathlib.Path(__file__).resolve().parent
P = BASE / "app-data" / "questions.json"
q = json.load(open(P, encoding="utf-8"))
n = len(q)

# lista balanceada de posiciones objetivo (50/50/50/50) barajada con semilla fija (reproducible)
targets = [i % 4 for i in range(n)]
random.seed(20260621)
random.shuffle(targets)

for x, tgt in zip(q, targets):
    opts = x["options"]; ans = x["answer"]
    correct = opts[ans]
    distract = [o for j, o in enumerate(opts) if j != ans]  # conserva orden relativo
    new = [None, None, None, None]
    new[tgt] = correct
    di = 0
    for slot in range(4):
        if slot == tgt: continue
        new[slot] = distract[di]; di += 1
    x["options"] = new
    x["answer"] = tgt

# validacion
assert all(len(x["options"]) == 4 and len(set(x["options"])) == 4 for x in q)
assert all(0 <= x["answer"] <= 3 for x in q)
json.dump(q, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Reequilibrado. Distribucion:", dict(sorted(collections.Counter(x["answer"] for x in q).items())))
print("Total:", n)
