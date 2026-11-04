#!/usr/bin/env python3
"""Structural + content checks for /dream/hair/ before deploy."""
import re, sys
from html.parser import HTMLParser

P = '/root/teethdreammeaning/site/dream/hair/index.html'
h = open(P, encoding='utf-8').read()
fails = []

VOID = {'meta','link','br','img','hr','input'}
class Chk(HTMLParser):
    def __init__(self):
        super().__init__(); self.stack=[]; self.errs=[]
    def handle_starttag(self, tag, attrs):
        if tag not in VOID: self.stack.append(tag)
    def handle_endtag(self, tag):
        if not self.stack: self.errs.append('extra close '+tag); return
        if self.stack[-1] != tag: self.errs.append(f'mismatch: open {self.stack[-1]} closed {tag}')
        else: self.stack.pop()
c = Chk(); c.feed(h)
if c.stack: fails.append('unclosed: '+str(c.stack))
if c.errs: fails.append('err tags: '+str(c.errs[:5]))

# junk from shamela chrome must not leak
for junk in ['اذهب','البحث في','القرون','مسار الصفحة','نسخ الفقرة','لتخصيص','دخول']:
    if junk in h: fails.append('JUNK LEAK: '+junk)

# CJK only inside Sources section
src_i = h.find('Sources (all passages checked')
head = h[:src_i]
cjk_head = re.findall(r'[一-鿿]', head)
if cjk_head: fails.append(f'CJK in narrative ({len(cjk_head)}): ' + ''.join(cjk_head[:10]))
# Arabic must be zero before first h2 (first-screen rule)
first_h2 = h.find('<h2')
screen1 = h[:first_h2]
ar = re.findall(r'[؀-ۿ]', screen1)
if ar: fails.append(f'Arabic in first screen ({len(ar)})')
# Arabic must not appear outside src/quote/loc areas: check qa blocks
for m in re.finditer(r'<div class="qa">.*?</div>\s*</div>', h, re.S):
    if re.search(r'[؀-ۿ]', m.group(0)):
        fails.append('Arabic inside qa block')
# zh lines in narrative: check lede/note/p outside src
src_start = h.find('<h2>Sources')
narr = h[:src_start]
zh = re.findall(r'[一-鿿]', narr)
if zh: fails.append(f'CJK before Sources ({len(zh)}): '+''.join(zh[:20]))

# title/desc lengths
t = re.search(r'<title>(.*?)</title>', h).group(1)
d = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
print('title len', len(t), '| desc len', len(d))
if not (45 <= len(t) <= 62): fails.append('title len')
if not (120 <= len(d) <= 165): fails.append('desc len')
# canonical + h1 + faq json
assert 'canonical' in h
import json
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
    try: json.loads(m.group(1))
    except Exception as e: fails.append('bad ld+json: '+str(e))
# no 'http://' mixed content
if 'href="http://' in h: fails.append('http link')

# verbatim spot-check: key EN quotes must survive esc() intact
en_checks = ["Hair: In a dream, hair represents money and longevity.",
 "If one's hair turns white in a dream",
 "Braiding: (Hair; Intertwine; Plait)",
 "'Aqiqah rites: (Hair of a newborn;",
 "hair growing anew in a dream, it means that he may lose most of his wealth"]
for q in en_checks:
    if q not in h: fails.append('verbatim EN missing: '+q[:50])
ar_checks = ["(شعر الرأس) هو في المنام مال وطول عمر فمن رأى أن شعر رأسه طال فإنه يطول عمره",
 "وإذا ضفر شعر المرأة ثلاثة قرون طلقت من زوجها ثلاثاً وإن كانت مريضة ماتت"]
for q in ar_checks:
    if q not in h: fails.append('verbatim AR missing: '+q[:40])
zh_checks = ["头白主长命大吉","头秃发落皆凶事","剪剃头发家内凶"]
for q in zh_checks:
    if q not in h: fails.append('verbatim ZH missing: '+q)

print('FAILS =', len(fails))
for f in fails: print('  -', f)
sys.exit(1 if fails else 0)
