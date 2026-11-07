#!/usr/bin/env python3
"""Fix broken ld+json FAQ blocks on 5 pages: the zones rollout (92109f6) linkified
PubMed/shamela URLs INSIDE the JSON string values with raw href="..." quotes,
breaking JSON parse. This script re-escapes the inner quotes so the JSON parses,
keeping the <a> tags (Google tolerates them in acceptedAnswer text)."""
import re, json, glob

def fix_block(inner):
    # only touch unescaped quotes that belong to injected href attributes
    s = inner
    if _parses(s):
        return s, False
    s2 = s.replace('<a href="', '<a href=\\"').replace('">PubMed', '\\">PubMed').replace('">shamela', '\\">shamela').replace('">DOI', '\\">DOI')
    if _parses(s2):
        return s2, True
    return s, None  # signal failure

def _parses(s):
    try:
        json.loads(s); return True
    except Exception:
        return False

changed = []
for f in sorted(glob.glob('site/dream/*/index.html')) + ['site/index.html']:
    t = open(f).read()
    out = []
    pos = 0
    ok = True
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        inner = m.group(1)
        if _parses(inner):
            continue
        fixed, did = fix_block(inner)
        if did is None:
            print("STILL BROKEN:", f); ok = False; continue
        out.append((m.start(1), m.end(1), fixed))
    if not out:
        continue
    for s, e, rep in reversed(out):
        t = t[:s] + rep + t[e:]
    open(f, 'w').write(t)
    changed.append(f)

print("changed:", changed)
# re-verify all ld+json parses
bad = 0
for f in sorted(glob.glob('site/dream/*/index.html')) + glob.glob('site/*/index.html') + ['site/index.html']:
    t = open(f).read()
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        if not _parses(m.group(1)):
            print("BAD REMAINS", f); bad += 1
print("bad remaining:", bad)
