#!/usr/bin/env python3
"""Page-level verification for /dream/wedding/ — v2.
Core method: every Arabic and English quoted fragment ON THE PAGE must appear in a
whitelist of source-verified passages (verify_wed.py checked those verbatim against
ibn_sirin_full.txt / shamela files), matched by longest-common-substring coverage.
Simpler and stricter than regex-splitting page runs.
"""
import re, html as H

PAGE = open('/root/teethdreammeaning/site/dream/wedding/index.html', encoding='utf-8').read()
N145 = open('/root/dream_research/nabulsi_page_145.txt', encoding='utf-8', errors='ignore').read()
N289 = open('/root/dream_research/nabulsi_page_289.txt', encoding='utf-8', errors='ignore').read()
N347 = open('/root/dream_research/nabulsi_p347_349.txt', encoding='utf-8', errors='ignore').read()
IBN = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8', errors='ignore').read()
ZG = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8', errors='ignore').read()

def norm_ar(t):
    t = re.sub(r'[\u064B-\u0652\u0670\u0653-\u0655\u0640]', '', t)
    for a in 'أإآٱ':
        t = t.replace(a, 'ا')
    t = t.replace('ى', 'ي').replace('ة', 'ه')
    t = t.replace(' علي ', ' على ')  # page-safe: source uses على
    return re.sub(r'\s+', ' ', t)

def norm_en(t):
    t = t.replace('\u00ad', '').replace('-\n', '').replace('\n', ' ')
    t = re.sub(r'DICTIONARY OF DREAMS \d+|\d+ IBN SEERIN[^\s]*|IBN SEERIN[^\s]*', ' ', t)
    t = re.sub(r'\s+', ' ', t)
    return t

AR corpus = None
