#!/usr/bin/env python3
"""verify_live_baby.py — post-deploy checks against the live site."""
import re, json, subprocess

def get(url):
    return subprocess.run(['curl','-s',url], capture_output=True, text=True).stdout

def code(url):
    return subprocess.run(['curl','-s','-o','/dev/null','-w','%{http_code}',url], capture_output=True, text=True).stdout.strip()

V = '?v=1107d'
fails = []
if code('https://teethdreammeaning.com/dream/baby/'+V) != '200': fails.append('baby not 200')
if code('https://teethdreammeaning.com/'+V) != '200': fails.append('home not 200')

sm = get('https://teethdreammeaning.com/sitemap.xml'+V)
if 'dream/baby/' not in sm: fails.append('sitemap missing baby')
print('sitemap urls:', sm.count('<loc>'))

home = get('https://teethdreammeaning.com/'+V)
if 'href="/dream/baby/"' not in home: fails.append('home missing baby link')

baby = get('https://teethdreammeaning.com/dream/baby/'+V)
if '<footer>' not in baby: fails.append('baby footer broken')
if '<h1>Dreaming of a Baby: What It Means</h1>' not in baby: fails.append('baby h1 missing')
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', baby, re.S):
    try: json.loads(m)
    except Exception as e: fails.append('baby ld+json: '+str(e)[:40])
if '\u4e00' <= min(baby.split('<h1>')[1].split('<h2')[0]) <= '\u9fff': pass
seg = baby.split('<h1>')[1].split('<h2')[0]
if re.search(r'[\u0600-\u06ff\u4e00-\u9fff]', seg): fails.append('first-screen non-latin on live')

death = get('https://teethdreammeaning.com/dream/teeth-falling-out-and-death/'+V)
if 'href="/dream/baby/"' not in death: fails.append('death page backlink missing')
wed = get('https://teethdreammeaning.com/dream/wedding/'+V)
if 'href="/dream/baby/"' not in wed: fails.append('wedding backlink missing')

# footer fix on legacy pages: no more literal backslash-1 line
blood = get('https://teethdreammeaning.com/dream/blood/'+V)
if '\\1>' in blood: fails.append('blood footer still broken')
if '<footer>' not in blood: fails.append('blood footer missing')

print('FAILS =', len(fails))
for f in fails: print(' -', f)
