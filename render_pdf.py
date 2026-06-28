#!/usr/bin/env python3
"""render_pdf.py - Render alternativo HTML->PDF con Playwright. En el sandbox usar WeasyPrint (build_doc.py)."""
import sys, pathlib
def render(html_file):
    src = pathlib.Path(html_file).resolve(); out = src.with_suffix(".pdf")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto(src.as_uri())
        pg.pdf(path=str(out), format="A4", margin={"top":"16mm","right":"15mm","bottom":"18mm","left":"15mm"}, print_background=True)
        b.close()
    print("PDF:", out)
if __name__ == "__main__":
    render(sys.argv[1])
