"""Builds the release file index.html from src/avlynx-source.html.
Usage:  python3 build/build.py
It adds the Content Security Policy and inlines jsPDF 4.2.1 (identical to the npm package),
so the finished file needs no network access."""
import hashlib, pathlib
H=pathlib.Path(__file__).resolve().parent; ROOT=H.parent
src=(ROOT/'src'/'avlynx-source.html').read_text(encoding='utf-8')
def sub(s,a,b):
    assert s.count(a)==1, 'not found exactly once: '+a[:60]; return s.replace(a,b)
VP='<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
out=sub(src,VP,VP+(H/'csp.txt').read_text().strip()+'\n')
assert 'fonts.googleapis.com' not in out
out=sub(out,'<script src="https://cdn.jsdelivr.net/npm/jspdf@4.2.1/dist/jspdf.umd.min.js" integrity="sha384-qovJwSBbRDPP5cEjCp8S0UP66wrvnjaa60XMOGzTNanrThcrGfXfnZkvgY8N1KT3" crossorigin="anonymous" referrerpolicy="no-referrer"></script>',(H/'jspdf-inline.html').read_text(encoding='utf-8'))
(ROOT/'index.html').write_text(out,encoding='utf-8')
print('index.html', hashlib.sha256(out.encode('utf-8')).hexdigest())
