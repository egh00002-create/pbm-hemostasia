# -*- coding: utf-8 -*-
"""Exporta los 23 documentos a Markdown plano (sin HTML) para busqueda de texto: app-data/content.md
y app-data/md/<code>.md por documento."""
import importlib, re, pathlib, html

BASE = pathlib.Path(__file__).resolve().parent
OUT = BASE / "app-data"; (OUT / "md").mkdir(parents=True, exist_ok=True)
ORDER = [("PBM-%02d" % i, "_build_pbm%02d" % i) for i in range(1, 19)] + \
        [("P-QR-%02d" % i, "_build_pqr%02d" % i) for i in range(1, 6)]

def to_md(htmltext):
    s = htmltext
    s = re.sub(r'(?is)<h1[^>]*>(.*?)</h1>', lambda m: "\n# " + strip(m.group(1)) + "\n", s)
    s = re.sub(r'(?is)<h2[^>]*>(.*?)</h2>', lambda m: "\n## " + strip(m.group(1)) + "\n", s)
    s = re.sub(r'(?is)<h3[^>]*>(.*?)</h3>', lambda m: "\n### " + strip(m.group(1)) + "\n", s)
    s = re.sub(r'(?is)<h4[^>]*>(.*?)</h4>', lambda m: "\n**" + strip(m.group(1)) + "**\n", s)
    s = re.sub(r'(?is)<span class="box-h">(.*?)</span>', lambda m: "\n**" + strip(m.group(1)) + "**\n", s)
    s = re.sub(r'(?is)<caption>(.*?)</caption>', lambda m: "\n_" + strip(m.group(1)) + "_\n", s)
    s = re.sub(r'(?is)<li>(.*?)</li>', lambda m: "- " + strip(m.group(1)) + "\n", s)
    s = re.sub(r'(?is)<(p|div|tr|table|ul|ol|section|nav|figure)[^>]*>', "\n", s)
    s = re.sub(r'(?is)</(p|div|tr|table|ul|ol|section|nav|figure|h1|h2|h3|h4)>', "\n", s)
    s = re.sub(r'(?is)<th[^>]*>(.*?)</th>', lambda m: strip(m.group(1)) + " | ", s)
    s = re.sub(r'(?is)<td[^>]*>(.*?)</td>', lambda m: strip(m.group(1)) + " | ", s)
    s = strip(s)
    s = re.sub(r'\n{3,}', "\n\n", s)
    return s.strip()

def strip(x):
    x = re.sub(r'(?is)<[^>]+>', '', x)
    x = html.unescape(x)
    return re.sub(r'[ \t]+', ' ', x).strip()

parts = []
for code, mod in ORDER:
    m = importlib.import_module(mod)
    body = "\n\n".join([to_md(m.COVER), to_md(m.BODY), to_md(m.REFS)])
    (OUT / "md" / f"{code}.md").write_text(body, encoding="utf-8")
    parts.append(f"\n\n---\n\n<!-- {code} -->\n\n{body}")

(OUT / "content.md").write_text("# Serie PBM - Hemostasia y Medicina Transfusional Perioperatoria\n" + "".join(parts), encoding="utf-8")
print("Markdown generado:", OUT / "content.md", "y", len(ORDER), "archivos en app-data/md/")
