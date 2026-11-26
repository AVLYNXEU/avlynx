"""Builds a company edition of AVLYNX from the release file.

Usage (all options are optional):
  python3 build/company-build.py \
      --input index.html \
      --output avlynx-company.html \
      --edition "Example Ltd edition" \
      --company "Example Ltd" \
      --library avlynx-library.json \
      --accent "#0e6e7a" \
      --hide libraryManager,example,customDevice

--input     The public release file: index.html from this repository or avlynx.html
            from a release. Default: index.html next to the build folder.
--output    The file to write. Default: avlynx-company.html in the current folder.
--edition   Text shown next to the version in the welcome message.
--company   Company name pre-filled in the title block of new projects.
--library   A library file exported from AVLYNX (Manage library, Export, Export as JSON).
            Its groups are built into the file, so the company devices are there even
            without a server.
--accent    Accent colour for new projects, the legend and the PDF, as #rrggbb.
--hide      Parts of the interface to hide, separated by commas:
            libraryManager, example, customDevice. Hidden is not protected.

The script changes only the five build switches described in docs/EXTENSIONS.md.
It uses no third-party packages.
"""
import argparse, hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FEATURES = ('libraryManager', 'example', 'customDevice')


def fail(msg):
    sys.exit('company-build: ' + msg)


def js(value):
    """JSON text that is safe inside an inline <script>."""
    t = json.dumps(value, ensure_ascii=False, separators=(',', ':'))
    return (t.replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
             .replace('\u2028', '\\u2028').replace('\u2029', '\\u2029'))


def put(src, placeholder, default, value):
    a = '/*@' + placeholder + '@*/' + default
    if src.count(a) != 1:
        fail('placeholder %s not found. Use an unchanged release file of version 1.2 or later as --input.' % placeholder)
    return src.replace(a, '/*@' + placeholder + '@*/' + value)


def text(value, name, limit):
    value = value.strip()
    if len(value) > limit:
        fail('%s is longer than %d characters.' % (name, limit))
    return value


def load_library(path):
    try:
        data = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    except (OSError, ValueError) as e:
        fail('cannot read the library file: %s' % e)
    groups = data.get('groups') if isinstance(data, dict) else None
    if not isinstance(groups, list) or not groups:
        fail('the library file has no groups. Export it in AVLYNX with Manage library, Export, Export as JSON.')
    n = 0
    for g in groups:
        if not isinstance(g, dict) or not isinstance(g.get('name'), str) or not isinstance(g.get('cats'), list):
            fail('the library file has a group without a name or categories.')
        for c in g['cats']:
            if not isinstance(c, dict) or not isinstance(c.get('devs'), list):
                fail('the group "%s" has a category without devices.' % g['name'])
            n += len(c['devs'])
    stamp = data.get('stamp')
    if not isinstance(stamp, (int, float)) or stamp <= 0:
        stamp = int(pathlib.Path(path).stat().st_mtime * 1000)
    out = {'stamp': int(stamp), 'groups': groups}
    if isinstance(data.get('retired'), list):
        out['retired'] = [r for r in data['retired'] if isinstance(r, str)]
    return out, len(groups), n


def main():
    p = argparse.ArgumentParser(description='Build a company edition of AVLYNX.')
    p.add_argument('--input', default=str(ROOT / 'index.html'))
    p.add_argument('--output', default='avlynx-company.html')
    p.add_argument('--edition', default='')
    p.add_argument('--company', default='')
    p.add_argument('--library')
    p.add_argument('--accent')
    p.add_argument('--hide', default='')
    a = p.parse_args()

    try:
        src = pathlib.Path(a.input).read_text(encoding='utf-8')
    except OSError as e:
        fail('cannot read %s: %s' % (a.input, e))
    if 'Content-Security-Policy' not in src:
        fail('%s is not a release file. Run build/build.py first, or use avlynx.html from a release.' % a.input)

    report = []
    if a.edition:
        src = put(src, 'EDITION', "''", js(text(a.edition, '--edition', 60)))
        report.append('edition: ' + a.edition.strip())
    if a.company:
        src = put(src, 'COMPANY', "''", js(text(a.company, '--company', 120)))
        report.append('company: ' + a.company.strip())
    if a.library:
        lib, ng, nd = load_library(a.library)
        src = put(src, 'BAKED_LIBRARY', 'null', js(lib))
        report.append('library: %d groups, %d devices' % (ng, nd))
    if a.accent:
        if not re.fullmatch(r'#[0-9a-fA-F]{6}', a.accent):
            fail('--accent must be a colour like #0e6e7a.')
        src = put(src, 'ACCENT', "'#0e6e7a'", js(a.accent.lower()))
        report.append('accent: ' + a.accent.lower())
    hide = [h.strip() for h in a.hide.split(',') if h.strip()]
    for h in hide:
        if h not in FEATURES:
            fail('unknown part "%s" in --hide. Use %s.' % (h, ', '.join(FEATURES)))
    if hide:
        src = put(src, 'FEATURES', '{}', js({h: False for h in hide}))
        report.append('hidden: ' + ', '.join(hide))

    out = pathlib.Path(a.output)
    out.write_text(src, encoding='utf-8')
    print(out.name, hashlib.sha256(src.encode('utf-8')).hexdigest())
    for r in report:
        print('  ' + r)


if __name__ == '__main__':
    main()
