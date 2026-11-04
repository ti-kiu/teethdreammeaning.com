#!/usr/bin/env python3
"""Extract clean text from frontiers_full.html; count hair mentions; print key passages."""
import re, html
raw = open('/root/dream_research/frontiers_full.html', encoding='utf-8', errors='ignore').read()
# strip script/style
raw = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', raw, flags=re.S|re.I)
body = re.sub(r'<[^>]+>', ' ', raw)
body = html.unescape(body)
body = re.sub(r'\s+', ' ', body)
open('/root/dream_research/frontiers_full.txt','w').write(body)
print('total chars:', len(body))
print('hair count:', len(re.findall(r'\bhair\w*', body, re.I)))
for m in list(re.finditer(r'.{240}[Hh]air.{240}', body))[:8]:
    print('---HAIR---'); print(m.group(0))
print('nightmare count:', len(re.findall(r'nightmare', body, re.I)))
for pat in [r'.{160}teeth tension.{240}', r'.{100}bruxism.{200}']:
    for m in list(re.finditer(pat, body, re.I))[:3]:
        print('==='); print(m.group(0))
