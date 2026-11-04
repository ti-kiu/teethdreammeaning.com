#!/usr/bin/env python3
"""Probe Frontiers 2018 full text for hair mentions + verify quote snippets for hair page."""
import re, html, sys, pathlib

p = pathlib.Path('/root/dream_research/frontiers_2018.html')
if p.exists():
    raw = p.read_text(encoding='utf-8', errors='ignore')
    body = re.sub(r'<[^>]+>', ' ', raw)
    body = html.unescape(body)
    body = re.sub(r'\s+', ' ', body)
    print('Hair-word count in Frontiers 2018:', len(re.findall(r'\bhair\b', body, re.I)))
    for m in list(re.finditer(r'.{250}[Hh]air.{250}', body))[:6]:
        print('---'); print(m.group(0))
    print('Nightmare word count:', len(re.findall(r'nightmare', body, re.I)))
    # pull key r-values verbatim
    for pat in [r'.{200}teeth tension.{200}', r'.{200}r = 0\.21.{200}']:
        for m in list(re.finditer(pat, body))[:2]:
            print('===R==='); print(m.group(0))
