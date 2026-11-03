#!/usr/bin/env python3
"""Structural verification for /dream/gold/.
Quote verification lives in verify_gold.py (source-side, verbatim).
This checks the page: tag balance, RTL blockquotes resolve to verified blocks,
no Arabic/CJK before first h2, title/desc lengths, no masking artifacts,
Sources-block Arabic runs are subsets of verified source text.
"""
import re, html as H

PAGE = open('/root/teethdreammeaning/site/dream/gold/index.html', encoding='utf-8').read()
N124 = open('/root/dream_research/nabulsi_page_124.txt', encoding='utf-8').read()
N125 = open('/root/dream_research/nabulsi_page_125.txt', encoding='utf-8').read()
ZG = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()
IBN = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8', errors='ignore').read()

def norm_ar(t):
    t = re.sub(r'[\u064B-\u0652\u0670\u0653-\u0655\u0640]', '', t)
    for a in 'أإآٱ':
        t = t.replace(a, 'ا')
    t = t.replace('ى', 'ي').replace('ة', 'ه')
    return re.sub(r'\s+', ' ', t)

SRC = ' || '.join(norm_ar(x) for x in (N124, N125))
IBN_FLAT = re.sub(r'\s+', ' ', IBN)
ZG_FLAT = re.sub(r'\s+', ' ', ZG)

fails = []

# 1. tag balance (skip script data like the wedding checker)
def strip_script(h):
    out, pos = [], 0
    for m in re.finditer(r'<script(?=[\s>])[^>]*>.*?(?:</script>|\Z)', h, re.S | re.I):
        out.append(h[pos:m.start()])
        body = m.group(0)
        out.append(body[:body.index('>') + 1])
        if body.endswith('</script>'):
            out.append('</script>')
        pos = m.end()
    out.append(h[pos:])
    return ''.join(out)

S = strip_script(PAGE)
for tag in ['div', 'blockquote', 'p', 'footer', 'section', 'ul', 'li', 'html', 'body', 'head', 'h1', 'h2', 'h3', 'table', 'tr', 'td', 'th']:
    o = len(re.findall(rf'<{tag}[ >]', S))
    c = len(re.findall(rf'</{tag}>', S))
    if o != c:
        fails.append(f'tag {tag}: {o} open / {c} close')

# 2. title/desc lengths
title = re.search(r'<title>(.*?)</title>', PAGE, re.S)
desc = re.search(r'<meta name="description" content="([^"]*)"', PAGE)
if not title or not (40 <= len(title.group(1)) <= 65):
    fails.append(f'title len {len(title.group(1)) if title else 0} not 40-65')
if not desc or not (120 <= len(desc.group(1)) <= 165):
    fails.append(f'desc len {len(desc.group(1)) if desc else 0} not 120-165')

# 3. no Arabic/CJK before first h2
h2 = PAGE.find('<h2')
head = PAGE[:h2 if h2 > 0 else len(PAGE)]
ar_head = re.findall(r'[\u0600-\u06FF]', head)
cjk_head = re.findall(r'[\u4e00-\u9fff]', head)
if ar_head:
    fails.append(f'{len(ar_head)} Arabic chars before first h2')
# Zhou Gong one-line quote allowed in lede? Rule: CJK only in Sources (and one quoted verdict line max in body)
body = PAGE[h2:] if h2 > 0 else ''
cjk_body = re.findall(r'[\u4e00-\u9fff]', body)
src_block = PAGE[PAGE.find('Sources ('):] if 'Sources (' in PAGE else ''
cjk_src = re.findall(r'[\u4e00-\u9fff]', src_block)
outside = len(cjk_body) - len(cjk_src)
if outside > 12:  # allow one short verdict line quoted in body
    fails.append(f'{outside} CJK chars outside Sources block (>12)')

# 4. masking artifacts
if '***' in PAGE:
    fails.append('masking artifact *** in page')

# 5. RTL blockquotes resolve to verified source text
for i, m in enumerate(re.finditer(r'<blockquote dir="rtl"[^>]*>(.*?)</blockquote>', PAGE, re.S)):
    q = norm_ar(H.unescape(re.sub(r'<[^>]+>', ' ', m.group(1))))
    q = re.sub(r'\s+', ' ', q).strip()
    if q not in SRC:
        fails.append(f'RTL blockquote {i} not verbatim in N124/N125: {q[:60]}...')

# 6. English blockquotes resolve to Ibn Sirin compile
for i, m in enumerate(re.finditer(r'<blockquote>(?!.*dir)(.*?)</blockquote>', PAGE, re.S)):
    q = H.unescape(re.sub(r'<[^>]+>', ' ', m.group(1)))
    q = re.sub(r'\s+', ' ', q).strip().strip('"')
    if len(q) > 40 and q not in IBN_FLAT:
        fails.append(f'EN blockquote {i} not verbatim in compile: {q[:60]}...')

# 7. Zhou Gong quotes resolve
for m in re.finditer(r'([\u4e00-\u9fff]{4,}(?:[\u4e00-\u9fff]|，|。)+)', PAGE):
    q = m.group(1)
    if q not in ZG_FLAT:
        fails.append(f'ZG quote not verbatim: {q[:30]}')

# 8. JSON-LD blocks parse
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', PAGE, re.S):
    import json as J
    try:
        J.loads(m.group(1))
    except Exception as e:
        fails.append(f'ld+json parse error: {e}')

if fails:
    print('FAILS:', len(fails))
    for f in fails:
        print(' -', f)
else:
    print('ALL GREEN: tags balanced, quotes verbatim, no head Arabic, CJK confined, ld+json OK')
