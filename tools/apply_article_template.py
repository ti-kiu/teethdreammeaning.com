#!/usr/bin/env python3
"""Apply the v3 article template (sidebar TOC + citation rows) to all dream pages.
Text content is preserved; only structure/CSS changes. Lone blockquotes or locs
(no pairing) are kept as-is and styled by fallback CSS."""
import re, html as H, sys, pathlib

ROOT = pathlib.Path("/root/teethdreammeaning/site/dream")
SKIP = {"teeth-falling-out-and-death"}  # already converted

NEW_CSS = """<style>
:root{--ink:#1a1a1a;--paper:#fdfcf9;--accent:#7a5c2e;--line:#e4ddcf;--soft:#6b6357;--card:#f9f5f0}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Georgia,'Times New Roman',serif;background:var(--paper);color:var(--ink);line-height:1.75}
.wrap{max-width:1000px;margin:0 auto;padding:40px 24px 56px}
.cols{display:grid;grid-template-columns:190px minmax(0,1fr);gap:48px}
@media(max-width:860px){.cols{grid-template-columns:1fr;gap:0}}
.top{display:flex;justify-content:space-between;align-items:baseline;gap:20px;
     border-bottom:2px solid var(--ink);padding-bottom:20px;margin-bottom:36px}
.top .brand{font-size:16.5px}
.top .brand a{color:var(--ink);text-decoration:none;font-weight:700}
.top .brand em{color:#555;font-weight:400}
.topnav{font-family:Helvetica,Arial,sans-serif;font-size:13.5px;flex-shrink:0}
.topnav a{color:#555;text-decoration:none}
.topnav a:hover{color:var(--accent);text-decoration:underline}
.topnav span{color:#bbb;margin:0 5px}
aside{position:sticky;top:24px;align-self:start;font-size:15px}
aside .lbl{font-weight:700;margin-bottom:12px}
aside ul{list-style:none}
aside li{margin-bottom:11px}
aside a{color:#555;text-decoration:none;line-height:1.4;display:block}
aside a:hover{color:var(--accent);text-decoration:underline}
@media(max-width:860px){
  aside{position:static;border:1px solid var(--line);border-radius:6px;background:var(--card);padding:16px 20px;margin-bottom:34px}
}
article{max-width:680px}
h1{font-size:clamp(28px,4.5vw,38px);font-weight:400;line-height:1.25;margin-bottom:12px}
.lede{font-size:18px;color:#333;margin-bottom:24px}
.tldr{background:#faf5ed;border:1px solid #e0d9d0;border-radius:4px;padding:18px 22px;margin:0 0 28px}
.tldr strong{display:block;font-size:13.5px;letter-spacing:.4px;text-transform:uppercase;color:var(--accent);margin-bottom:8px;font-family:Helvetica,Arial,sans-serif}
.tldr p{font-size:15.5px;line-height:1.65;margin-bottom:10px}
.tldr p:last-child{margin-bottom:0}
h2{font-size:22px;font-weight:400;margin:44px 0 16px}
h3{font-size:17px;font-weight:700;margin:28px 0 8px}
p{margin-bottom:16px}
.qa{border-bottom:1px solid var(--line);padding:18px 0}
.qa h3{margin:0 0 8px}
.qa p:last-child{margin-bottom:0}
.cites{margin:24px 0 0;border-top:2px solid var(--ink)}
.cite-hd{display:grid;grid-template-columns:minmax(0,1fr) 160px;gap:20px;padding:8px 0;
         font-family:Helvetica,Arial,sans-serif;font-size:11px;letter-spacing:.8px;text-transform:uppercase;color:#999}
.cite-row{display:grid;grid-template-columns:minmax(0,1fr) 160px;gap:20px;
          padding:16px 0;border-bottom:1px solid var(--line)}
.cite-row .txt{font-size:16px;font-style:italic;color:#2e2a24;line-height:1.7}
.cite-row .txt p{margin-bottom:0}
.cite-row .src{font-size:13px;color:#777;align-self:start;line-height:1.5}
.cite-note{font-size:14.5px;color:#555;margin:14px 0 28px}
@media(max-width:560px){.cite-row{grid-template-columns:1fr;gap:6px}.cite-hd{grid-template-columns:1fr}.cite-hd .src-hd{display:none}}
.ar{font-size:16.5px;color:#3a362f;direction:rtl;text-align:right;line-height:2;margin:10px 0 0;font-style:normal}
/* fallbacks for unpaired legacy elements */
blockquote{border-left:3px solid var(--accent);padding:12px 20px;margin:16px 0 20px;background:#f7f3ea;font-style:italic}
blockquote p:last-child{margin-bottom:0}
.loc{font-family:Menlo,Consolas,monospace;font-size:12.5px;color:var(--soft);margin:-8px 0 24px}
.note{background:#faf5ed;border:1px solid #e0d9d0;border-radius:4px;padding:16px 20px;font-size:14.5px;color:#555;margin:30px 0}
.note p:last-child{margin-bottom:0}
footer{border-top:1px solid var(--line);margin-top:48px;padding-top:20px;
       font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#777;grid-column:1 / -1}
footer a{color:#777;text-decoration:none}
footer a:hover{color:var(--accent)}
footer span{color:#bbb;margin:0 5px}
a{color:var(--accent)}
.rel ul{list-style:none;padding:0}
.rel li{padding:8px 0;border-bottom:1px solid var(--line)}
</style>"""

TOP_BAR = """<div class="top">
  <div class="brand"><a href="/">Teeth Dream Meaning</a> <em>· classical sources, checked page by page</em></div>
  <nav class="topnav"><a href="/about/">About</a><span>·</span><a href="/disclaimer/">Disclaimer</a><span>·</span><a href="/about/">Sources</a></nav>
</div>"""

def slugify(text, n):
    t = re.sub(r"<[^>]+>", "", text)
    t = H.unescape(t)
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()[:40]
    return f"s{n}" if not t else t

def convert(page: pathlib.Path):
    src = page.read_text()
    orig = src

    # 1. swap CSS
    src, n = re.subn(r"<style>.*?</style>", lambda m: NEW_CSS, src, count=1, flags=re.S)
    assert n == 1, f"{page}: style block not found"

    # 2. swap top nav
    src, n = re.subn(r'<nav class="top">.*?</nav>', lambda m: TOP_BAR, src, count=1, flags=re.S)
    assert n == 1, f"{page}: nav.top not found"

    # 3. ids on h2 + collect TOC
    toc, counter = [], [0]
    def h2repl(m):
        attrs, body = m.group(1), m.group(2)
        if "id=" in attrs:
            m2 = re.search(r'id="([^"]+)"', attrs)
            hid = m2.group(1) if m2 else ""
        else:
            counter[0] += 1
            hid = slugify(body, counter[0])
            attrs = f' id="{hid}"' + attrs
        label = H.unescape(re.sub(r"<[^>]+>", "", body)).strip()
        toc.append((hid, label))
        return f"<h2{attrs}>{body}</h2>"
    src = re.sub(r"<h2([^>]*)>(.*?)</h2>", h2repl, src, flags=re.S)

    aside = '<aside>\n<div class="lbl">On this page</div>\n<ul>\n' + \
            "".join(f'<li><a href="#{h}">{H.escape(l)}</a></li>\n' for h, l in toc) + \
            "</ul>\n</aside>"

    # 4. blockquote+loc runs -> grouped citation tables (attrs allowed; rtl -> Arabic row)
    pair = re.compile(r"<blockquote([^>]*)>(.*?)</blockquote>\s*<p class=\"loc\">(.*?)</p>", re.S)
    runs = list(re.finditer(r"(?:<blockquote[^>]*>.*?</blockquote>\s*<p class=\"loc\">.*?</p>\s*)+", src, flags=re.S))
    for run in reversed(runs):
        block = run.group(0)
        pairs = pair.findall(block)
        rows = ""
        for attrs, t, s in pairs:
            t = t.strip()
            if 'dir="rtl"' in attrs:
                inner = re.sub(r"^<p[^>]*>|</p>$", "", t)
                rows += (f'<div class="cite-row">\n  <div class="txt"><p class="ar">{inner}</p></div>\n'
                         f'  <div class="src">{re.sub(r"<p[^>]*>|</p>", "", s).strip()}</div>\n</div>\n')
            else:
                rows += (f'<div class="cite-row">\n  <div class="txt">{t}</div>\n'
                         f'  <div class="src">{re.sub(r"<p[^>]*>|</p>", "", s).strip()}</div>\n</div>\n')
        table = ('<div class="cites">\n<div class="cite-hd"><div>Text</div><div class="src-hd">Source</div></div>\n'
                 + rows + "</div>\n")
        src = src[:run.start()] + table + src[run.end():]

    # 5. open cols/aside/main before h1, close before footer
    src, n = re.subn(r"(<h1)", f'</div>\n<div class="cols">\n{aside}\n<main><article>\n\\1', src, count=1)
    assert n == 1, f"{page}: h1 not found"
    # remove the stray </div> we used as placeholder anchor start? No: TOP_BAR already closed its div.
    # Fix: the inserted '</div>' is wrong if TOP_BAR is not wrapped. TOP_BAR has no wrapper div.
    src = src.replace('</div>\n<div class="cols">\n<aside>', '<div class="cols">\n<aside>', 1)
    src, n = re.subn(r"(<footer)", r"</article></main>\n</div>\n\\1", src, count=1)
    assert n == 1, f"{page}: footer not found"

    # 6. bump dateModified
    src = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"', '"dateModified": "2026-11-06"', src)

    page.write_text(src)
    body = re.sub(r"<style>.*?</style>", "", src, flags=re.S)
    lone_bq = len(re.findall(r"<blockquote", body))
    lone_loc = len(re.findall(r'class="loc"', body))
    rows = len(re.findall(r'class="cite-row"', body))
    ar = len(re.findall(r'class="ar"', body))
    return len(toc), rows, lone_bq, lone_loc, ar, len(src) - len(orig)

for d in sorted(ROOT.iterdir()):
    if d.name in SKIP or not (d / "index.html").exists():
        continue
    try:
        r = convert(d / "index.html")
        print(f"{d.name:36s} toc={r[0]:2d} rows={r[1]:2d} loneBQ={r[2]} loneLoc={r[3]} ar={r[4]} delta={r[5]:+6d}")
    except AssertionError as e:
        print(f"{d.name:36s} FAIL: {e}")
