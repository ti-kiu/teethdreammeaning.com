#!/usr/bin/env python3
import re, json
PAGE = open('/root/teethdreammeaning/site/dream/spider/index.html', encoding='utf-8').read()
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', PAGE, re.S)
for i, b in enumerate(blocks):
    try:
        json.loads(b)
        print(i, 'OK')
    except Exception as e:
        print(i, 'ERR', e)
        pos = 3382
        print(repr(b[pos-60:pos+60]))
