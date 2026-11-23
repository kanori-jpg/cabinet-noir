"""Construit la version GitHub Pages (docs/index.html) à partir de index.html.

index.html est la source publiée sur claude.ai : claude.ai l'entoure lui-même
de <!doctype html><html><head>…<body>. Pour GitHub Pages, on ajoute ce cadre ici.
Lancer après chaque modification :  python construire.py
"""
from pathlib import Path

ici = Path(__file__).resolve().parent
source = (ici / "index.html").read_text(encoding="utf-8")

page = (
    "<!doctype html>\n<html lang=\"fr\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
    "<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);"
    "padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}"
    "[hidden]{display:none!important}</style>\n"
    "</head>\n<body>\n" + source.strip() + "\n</body>\n</html>\n"
)

(ici / "docs").mkdir(exist_ok=True)
(ici / "docs" / "index.html").write_text(page, encoding="utf-8", newline="\n")
(ici / "docs" / ".nojekyll").write_text("", encoding="utf-8")
print("docs/index.html construit")
