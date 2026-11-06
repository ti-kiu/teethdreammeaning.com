#!/usr/bin/env python3
"""Rollout v3 zones template (validated on teeth-falling-out-and-death preview)
to the remaining 16 dream pages. Applies to each page:
  1. z-text / z-research / z-reading chips above h2s, and aside groups
  2. reading notes (paragraphs after each citation table) -> .reading boxes
  3. mobile order: title -> quick answer -> collapsed TOC -> lede -> body
  4. real links: shamela.ws/book/N/P, PubMed IDs, DOI 10.1037/a0026171
  5. colors: .z-reading #6b6357, small labels #999 -> #666
Text content unchanged. Idempotent-ish; run once."""
import re, pathlib

ROOT = pathlib.Path("/root/teethdreammeaning/site/dream")
SKIP = {"teeth-falling-out-and-death"}

ICONS = {
    "text": '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6.2C10.4 5 8 4.2 4.8 4.2v13.6c3.2 0 5.6.8 7.2 2 1.6-1.2 4-2 7.2-2V4.2C16 4.2 13.6 5 12 6.2zM12 6.2v13.6"/></svg>',
    "research": '<svg width="11" h="11" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 3h5M10.8 3v5.2L5.6 16.8A2.5 2.5 0 0 0 7.8 20.5h8.4a2.5 2.5 0 0 0 2.2-3.7L13.2 8.2V3M8.2 14.5h7.6"/></svg>'.replace('h="11"','height="11"'),
    "reading": '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7-4-4-7 7-1 5zM16 5l2 2M13 8l2 2"/></svg>',
}
CHIP = {
    "text": f'<span class="zone z-text">{ICONS["text"]}Classical text</span>',
    "research": f'<span class="zone z-research">{ICONS["research"]}Modern research</span>',
    "reading": f'<span class="zone z-reading">{ICONS["reading"]}This site\'s reading</span>',
}

# h2 classification per page: list of (h2_text_prefix -> zone)
ZONES = {
 "blood": [("The finding", "reading"), ("The entries", "text"), ("What modern research", "research"), ("Sources", None)],
 "dead-person-resurrected": [("The one dark reading", "reading"), ("The entries", "text"), ("What modern research", "research"), ("Sources", None)],
 "gold": [("The finding", "reading"), ("The entries", "text"), ("What modern research", "research"), ("Sources", None)],
 "hair": [("The finding", "reading"), ("The entries", "text"), ("What modern research", "research"), ("Sources", None)],
 "kaaba": [("The hinge", "reading"), ("The entries", "text"), ("What modern research", "research"), ("Sources", None)],
 "one-tooth-vs-all-teeth": [("The counting rule", "text"), ("The Ibn Sirin compilation", "text"), ("Blood only enters", "text"), ("The odd pair", "text"), ("What modern research", "research")],
 "snake": [("So which reading", "reading"), ("The entries", "text"), ("What modern research", "research"), ("Sources", None)],
 "spider": [("The finding", "reading"), ("The entries", "text"), ("What modern research", "research"), ("Sources", None)],
 "teeth-dreams-and-stress": [("The strange headline", "text"), ("Where the books", "text"), ("The physical chain", "text"), ("A dictionary quirk", "text"), ("What the one head-on study", "research"), ("Set the layers", "reading"), ("The honest gap", "reading")],
 "teeth-falling-into-hand-lap-ground": [("The three surfaces", "text"), ("For the lower teeth", "text"), ("Where the page rules", "text"), ("The pocket", "text"), ("The honest gap", "reading"), ("Why the dream feels", "research")],
 "teeth-falling-out": [("Why it feels so real", "research"), ("Where the classical readings", "text"), ("Where the readings clash", "reading"), ],
 "teeth-falling-out-good-or-bad-omen": [("The book's own lesson", "text"), ("The calamity reading", "text"), ("The exceptions clause", "text"), ("The switch", "text"), ("What the one empirical", "research"), ("Set the layers", "reading"), ("The honest gap", "reading")],
 "teeth-falling-out-with-blood": [("The front-teeth ruling", "text"), ("The same ruling", "text"), ("Blood on a caught tooth", "text"), ("The clause both books", "text"), ("What modern research", "research")],
 "teeth-three-traditions": [("The Zhou Gong lines", "text"), ("Where all three", "reading"), ("The age reading", "text"), ("Who actually gets", "text"), ("What a modern reader", "reading")],
 "water": [("One honest complication", "reading"), ("The entries", "text"), ("The thirst layer", "research"), ("Sources", None)],
 "wedding": None,  # auto: first h2 -> reading? inspect below
}

WEDDING_H2 = [("The finding", "reading"), ("The entries", "text"), ("What modern research", "research"), ("Sources", None)]
ZONES["wedding"] = WEDDING_H2

# "The finding" sections start with the site's own synthesis; keep them z-reading
# but their content stays as-is (only the chip is added).

CSS_ADD = """
/* ---- zones (v3 template) ---- */
.zone{display:inline-flex;align-items:center;gap:6px;font-family:Helvetica,Arial,sans-serif;
      font-size:11px;letter-spacing:.8px;text-transform:uppercase;color:#fff;
      border-radius:3px;padding:3px 9px;margin:0 0 10px}
.zone svg{flex-shrink:0}
.z-text{background:var(--accent)}
.z-reading{background:#6b6357}
.z-research{background:#4a6b6b}
h2{margin-top:38px}
h2 + .zone{margin-top:-6px}
.reading{background:#f5f1e6;border-left:3px solid #6b6357;padding:14px 18px;margin:14px 0 28px}
.reading .rlbl{display:block;font-family:Helvetica,Arial,sans-serif;font-size:11.5px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;color:#6b6357;margin-bottom:6px}
.reading p{font-size:15px;line-height:1.65;margin-bottom:10px}
.reading p:last-child{margin-bottom:0}
aside .g{font-family:Helvetica,Arial,sans-serif;font-size:10.5px;letter-spacing:.6px;text-transform:uppercase;color:#666;margin:14px 0 6px}
.cite-hd{color:#666}
/* mobile order: title -> quick answer -> toc -> lede -> body */
.mhead{display:contents}
aside details summary{font-weight:700;cursor:pointer;list-style:none}
aside details summary::-webkit-details-marker{display:none}
aside details summary::after{content:"▾";color:#666;margin-left:6px;font-size:12px}
aside details[open] summary::after{content:"▴"}
@media(min-width:861px){
  aside{grid-column:1;grid-row:1}
  .mhead{grid-column:2;grid-row:1}
  main{grid-column:2;grid-row:2}
}
@media(max-width:860px){
  .mhead{order:0}
  aside{order:1;position:static;border:1px solid var(--line);border-radius:6px;background:var(--card);padding:12px 20px;margin:0 0 28px}
  main{order:2}
  .top .brand em{display:none}
}
"""

JS_ADD = """<script>
if(window.matchMedia("(max-width:860px)").matches){
  var d=document.querySelector(".tocd"); if(d) d.removeAttribute("open");
}
</script>"""

def linkify(s):
    s = re.sub(r'(?<!href=")(?<!">)\b(shamela\.ws/book/\d+/\d+)\b',
               r'<a href="https://\1">\1</a>', s)
    s = re.sub(r'(?<!href=")(?<!">)\bPubMed (\d{5,8})\b',
               r'<a href="https://pubmed.ncbi.nlm.nih.gov/\1/">PubMed \1</a>', s)
    s = re.sub(r'(?<!href=")DOI 10\.1037/a0026171\b',
               r'<a href="https://doi.org/10.1037/a0026171">DOI 10.1037/a0026171</a>', s)
    return s

def process(page, spec):
    src = page.read_text()

    # 1. CSS additions before </style>
    if ".zone{" not in src:
        src = src.replace("</style>", CSS_ADD + "</style>", 1)

    # 2. chips above h2s + aside groups
    chips, groups = [], {}
    def h2repl(m):
        attrs, body = m.group(1) or "", m.group(2)
        plain = re.sub(r"<[^>]+>", "", body)
        zone = None
        for prefix, z in spec:
            if plain.strip().startswith(prefix):
                zone = z
                break
        chips.append(zone)
        if zone:
            return CHIP[zone] + "\n<h2" + attrs + ">" + body + "</h2>"
        return m.group(0)
    src = re.sub(r"<h2([^>]*)>(.*?)</h2>", h2repl, src, flags=re.S)

    # aside: keep original <ul>, wrap in details, prepend group labels
    GROUP_LABELS = {"text": "Classical texts", "research": "Modern research", "reading": "This site's reading"}
    m = re.search(r"<aside>\s*<div class=\"lbl\">On this page</div>\s*<ul>(.*?)</ul>\s*</aside>", src, flags=re.S)
    assert m, "aside not found"
    items_html = m.group(1)
    lis = re.findall(r"<li>(.*?)</li>", items_html, flags=re.S)
    out = []
    for n, li in enumerate(lis):
        z = chips[n] if n < len(chips) else None
        prev = chips[n-1] if n else None
        if z and z != prev:
            out.append('<div class="g">' + GROUP_LABELS[z] + "</div>")
        out.append("<li>" + li + "</li>")
    new_aside = '<aside>\n<details class="tocd" open>\n<summary>On this page</summary>\n<ul>\n' + "\n".join(out) + "\n</ul>\n</details>\n</aside>"
    src = src.replace(m.group(0), new_aside, 1)

    # 3. wrap paragraphs after each .cites table into .reading box
    #    pattern: </div>(cites end) followed by one or more <p class="cite-note">...</p>
    src = re.sub(
        r'(</div>\s*)(<p class="cite-note">.*?</p>(?:\s*<p class="cite-note">.*?</p>)*)',
        lambda m: m.group(1) + '\n<div class="reading"><span class="rlbl">This site\'s reading</span>' + m.group(2).replace('class="cite-note"', "").replace("<p>", '<p style="margin-bottom:10px">').replace("</p>", "</p>") + "</div>",
        src, flags=re.S)

    # 4. linkify
    src = linkify(src)

    # 5. mhead wrapper: move aside before main? DOM is aside, main already (template).
    #    Wrap h1+lede region? Keep simple: insert .mhead wrapper around h1+lede + keep aside before main:
    # DOM order currently: top, cols> (aside, main(article)). For mobile order we need mhead first.
    # Move h1+lede out of article into .mhead before aside:
    m = re.search(r"<article>\s*(<h1>.*?</h1>)\s*(<p class=\"lede\">.*?</p>)", src, flags=re.S)
    if m:
        h1, lede = m.group(1), m.group(2)
        src = src.replace(m.group(0), "<article>\n", 1)
        src = src.replace('<div class="cols">\n<aside>',
                          '<div class="cols">\n<div class="mhead">\n' + h1 + "\n" + lede + '\n</div>\n<aside>', 1)
        # but desktop: mhead uses display:contents so h1/lede flow into col2 row1; article body row2.
        # article top needs the quick-answer too? Death page moved tldr into mhead; other pages lack tldr, fine.

    # 6. collapse script before </body>
    if "tocd" in src and "matchMedia" not in src:
        src = src.replace("</body>", JS_ADD + "</body>", 1)

    page.write_text(src)
    return chips

for d in sorted(ROOT.iterdir()):
    if d.name in SKIP or not (d / "index.html").exists():
        continue
    spec = ZONES.get(d.name)
    if not spec:
        print(f"{d.name}: no spec, skipped")
        continue
    try:
        chips = process(d / "index.html", spec)
        print(f"{d.name:36s} " + " ".join((c or "-")[0] for c in chips))
    except Exception as e:
        print(f"{d.name:36s} FAIL {e}")
