#!/usr/bin/env python3
"""Append research-attribution links to QA blocks that cite study data."""
import re, pathlib

ROOT = pathlib.Path("/root/teethdreammeaning/site/dream")
# slug -> research-section anchor id on that page
LINKS = {
    "teeth-dreams-and-stress": "what-the-one-head-on-study-found",
    "teeth-falling-out-good-or-bad-omen": "what-the-one-empirical-paper-says-about-",
}

ATTR = (' The design and full numbers behind these figures are laid out in the '
        '<a href="#{rid}">modern-research section</a> below.')

for slug, rid in LINKS.items():
    f = ROOT / slug / "index.html"
    s = f.read_text()
    anchor = f'id="{rid}"'
    assert anchor in s, f"{slug}: anchor {rid} missing"

    def qa_repl(m):
        block = m.group(0)
        if not re.search(r"r = \d|n=\d|n = \d", block):
            return block
        if "modern-research section" in block:
            return block
        return block.replace("</p>", ATTR.format(rid=rid) + "</p>", 1)

    ns = re.sub(r'<div class="qa">.*?</div>\n', qa_repl, s, flags=re.S)
    if ns != s:
        f.write_text(ns)
        print(slug, "attributed:", ns.count("modern-research section"))
    else:
        print(slug, "NO CHANGE — check QA content")

# teeth-three-traditions: has study data in QA but no research h2 on page.
# Check what it references and whether an anchor exists at all.
f3 = ROOT / "teeth-three-traditions/index.html"
s3 = f3.read_text()
qas = re.findall(r'<div class="qa">.*?</div>\n', s3, flags=re.S)
hits = [q for q in qas if re.search(r"r = \d|n=\d|n = \d", q)]
print("three-traditions QA with data:", len(hits))
print("h2 ids:", re.findall(r'<h2 id="([^"]+)"', s3))
