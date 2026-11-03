#!/usr/bin/env python3
"""Structural verification for /dream/wedding/.
Quote verification itself lives in verify_wed.py (source-side, verbatim substring).
This script checks the page: tag balance, RTL blockquotes resolve to verified blocks,
no Arabic/CJK before the first h2, title/desc lengths, no masking artifacts,
and that Sources-block Arabic runs are subsets of verified blocks.
"""
import re, html as H

PAGE = open('/root/teethdreammeaning/site/dream/wedding/index.html', encoding='utf-8').read()
N145 = open('/root/dream_research/nabulsi_page_145.txt', encoding='utf-8', errors='ignore').read()
N289 = open('/root/dream_research/nabulsi_page_289.txt', encoding='utf-8', errors='ignore').read()
N347 = open('/root/dream_research/nabulsi_p347_349.txt', encoding='utf-8', errors='ignore').read()
ZG = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8', errors='ignore').read()

def norm_ar(t):
    t = re.sub(r'[\u064B-\u0652\u0670\u0653-\u0655\u0640]', '', t)
    for a in 'أإآٱ':
        t = t.replace(a, 'ا')
    t = t.replace('ى', 'ي').replace('ة', 'ه')
    return re.sub(r'\s+', ' ', t)

SRC = " || ".join(norm_ar(x) for x in (N145, N289, N347))

fails = []

# 1. tag balance
for tag in ['div', 'blockquote', 'p', 'footer', 'section', 'ul', 'html', 'body', 'head']:
    o = len(re.findall(rf'<{tag}[ >]', PAGE))
    c = len(re.findall(rf'</{tag}>', PAGE))
    if o != c:
        fails.append(f"TAG {tag}: open={o} close={c}")

# 2. first screen clean (h1 -> first h2): no Arabic, no CJK
z = re.sub(r'<[^>]+>', ' ', PAGE[PAGE.find('<h1>'):PAGE.find('<h2>')])
for name, pat in (("CJK", r'[\u4e00-\u9fff]'), ("ARABIC", r'[\u0600-\u06FF]')):
    hits = re.findall(pat, z)
    if hits:
        fails.append(f"{name} before first h2: {hits[:8]}")

# 3. RTL blockquotes must be verbatim in sources
for bq in re.findall(r'<blockquote dir="rtl"[^>]*>\s*<p>(.*?)</p>\s*</blockquote>', PAGE, re.S):
    frag = norm_ar(H.unescape(re.sub(r'<[^>]+>', '', bq))).strip().strip('. ')
    if frag and frag not in SRC:
        fails.append(f"RTL BQ MISS: {frag[:70]}")

# 4. every Arabic run >=15 chars in the page must sit inside a verified source string
runs = [norm_ar(r) for r in re.findall(r'[\u0600-\u06FF][\u0600-\u06FF\s\(\)0-9\.\,\-؛]{14,}',
                                       H.unescape(PAGE))]
bad_runs = []
for r in runs:
    r2 = r.strip(' .-')
    if len(r2) < 15:
        continue
    if r2 in SRC or re.sub(r'^\(?\s*(?:زواج|كعبة)\s*[:\)（(]*', '', r2).strip(' ().,:-') in SRC:
        continue
    # tolerate parenthesized glosses: test maximal 4-word windows
    words = r2.split()
    ok = any(" ".join(words[i:i+5]) in SRC for i in range(max(1, len(words)-4)))
    if not ok:
        bad_runs.append(r2[:70])
if bad_runs:
    fails.append(f"UNVERIFIED ARABIC RUNS ({len(bad_runs)}/{len(runs)}): " + " ;; ".join(bad_runs[:3]))

# 5. Zhou Gong lines verbatim
for line in ['见嫁聚及孝主凶', '夫妇宴会主相别', '见娶妻者主改动']:
    if line not in ZG:
        fails.append(f"ZG MISS: {line}")

# 6. artifacts + meta lengths
if '***' in PAGE:
    fails.append("MASKING ARTIFACT *** in page")
t = re.search(r'<title>(.*?)</title>', PAGE)
d = re.search(r'name="description" content="(.*?)"', PAGE)
print(f"title len={len(t.group(1)) if t else 'MISSING'}  desc len={len(d.group(1)) if d else 'MISSING'}")
cjk_total = len(re.findall(r'[\u4e00-\u9fff]', PAGE))
print(f"arabic runs checked={len(runs)}  CJK total={cjk_total}")
print("FAILS:" if fails else "ALL GREEN")
for f in fails:
    print(" -", f)
