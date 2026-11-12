#!/usr/bin/env python3
import re
P = open('/root/teethdreammeaning/site/dream/cat/index.html', encoding='utf-8').read()
body_part = P[P.find('<body>'):]
seg = body_part.split('<h1>')[1].split('<h2')[0]
ar = [(m.start(), seg[max(0,m.start()-50):m.start()+25]) for m in re.finditer(r'[\u0600-\u06ff]', seg)]
print('AR in first screen:', len(ar))
for a in ar[:5]: print(repr(a))
cjk = [(m.start(), seg[max(0,m.start()-50):m.start()+25]) for m in re.finditer(r'[\u4e00-\u9fff]', seg)]
print('CJK in first screen:', len(cjk))
for c in cjk[:6]: print(repr(c))
