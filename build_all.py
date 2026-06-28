# -*- coding: utf-8 -*-
"""build_all.py - Punto de entrada unico del build de la serie PBM.
Reconstruye: PDFs de cada documento -> dosier -> libro (con figuras) -> cuestionario PDF
-> datos de la app (content/markdown/preguntas) -> paquete de revision.
Uso: python build_all.py [--solo-libro]"""
import subprocess, sys, glob, pathlib, time

BASE = pathlib.Path(__file__).resolve().parent
def run(script):
    t = time.time()
    print("==>", script, flush=True)
    r = subprocess.run([sys.executable, str(BASE / script)], cwd=str(BASE))
    print(("   OK " if r.returncode == 0 else "   ERROR ") + "(%.1fs)" % (time.time() - t), flush=True)
    return r.returncode

def main():
    solo = "--solo-libro" in sys.argv
    steps = []
    if not solo:
        steps += sorted(glob.glob("_build_pbm*.py"), key=lambda s: s)
        steps += sorted(glob.glob("_build_pqr*.py"), key=lambda s: s)
        steps += ["build_dossier.py", "make_quiz_pdf.py",
                  "export_content.py", "export_markdown.py", "build_reviewpack.py"]
    steps += ["build_libro5.py"]   # libro final con figuras
    rc = 0
    for s in steps:
        rc |= run(pathlib.Path(s).name)
    print("\nLIBRO:", BASE / "PBM-libro.pdf")
    print("Resultado:", "OK" if rc == 0 else "con errores (revisar arriba)")

if __name__ == "__main__":
    main()
