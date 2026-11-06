#!/usr/bin/env python3
"""verify_page_blood.py — final-HTML checks for /dream/blood/:
quote-verbatim coverage vs corpus files, structure closure, first-screen rules,
ld+json validity, title/desc lengths. FAILS=0 to ship."""
import re, json, html as h

P = open('/root/teethdreammeaning/site/dream/blood/index.html', encoding='utf-8').read()
def norm(s): return re.sub(r'\s+', ' ', s).strip()

en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en)
en = re.sub(r"\d+ IBN SEERIN'?S", ' ', en); en = norm(en)
ars = []
for f in ('117','118','116','94'):
    ars.append(norm(open(f'/root/dream_research/nabulsi_page_{f}.txt', encoding='utf-8').read()))
z = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()

fails = []

# 1. every quoted EN passage (inside blockquote / src <p> "…") must be verbatim in corpus
body = h.unescape(P)
quotes = re.findall(r'<p>"(.*?)"(?: \(elided.*?\))?</p>', body, re.S)
for q in quotes:
    qq = norm(q).rstrip('.').replace('...','')  # elided sample lines
    head = norm(q)[:80]
    if head not in en: fails.append("EN quote head missing: "+head[:60])

# injected corpus passages: pull from sources div
src = body.split('Sources (all passages')[1]
en_assert = [
  "Blood: In a dream, blood represents unlawful or illegal money",
  "vanquishing one's enemy.",
  "Bleeding: Internal bleeding in a dream means financial losses",
  "Bleeding nose: A bleeding nose in a dream means unlawful money",
  "Cupping: (Sacrification; A medicinal process of blood letting)",
  "Menstrual period: (Discharge; Menstruation; The Curse of Eve)",
  "Veins: (Blood ties; Family; Relative; Vessel)",
  "Leech: (Bloodsucker; Sponger)",
  "Blood disease: If one is presented in his dream with red unripened dates",
  "Bleeding naturally in a dream means peace and comfort.",
]
for s in en_assert:
    if s not in src: fails.append("Sources missing EN: "+s[:50])
    if s not in en: fails.append("EN assert not verbatim in corpus: "+s[:50])

ar_assert = [
  "(دم) في المنام مال حرام أو إثم يخرج منه أو فعل يأثم به",
  "رجع من سفره سالماً",
  "وقيل من رأى) أنه يخرج الدم من جسده",
  "ارعوى عن إثم ونجا منه",
  "ومن رأى) أنه وقع في بئر من دم",
  "فهو كذب يكذب عليه",
  "دماً خرج منه في غير فصد ولا حجامة",
  "مدح أو ذم",
  "دل على نطفته التي يضعف لخروجها",
  "أو يظفر بعدوه",
  "والإفراط في خروج الدم نكد",
  "للآيسة من الحيض مرض",
  "يخرج من دبره دم",
  "بأفواه العروق",
  "(دمع) في المنام",
  "فهو هم وحزن",
  "(دمل) ومن رأى في المنام",
  "عاد مكانه",
  "فإن سال الدم على يديه مات عدوه وورث ماله",
]
for s in ar_assert:
    if s not in src: fails.append("Sources missing AR: "+s[:40])
    if not any(s in a for a in ars): fails.append("AR assert not verbatim in corpus: "+s[:40])

for s in ("手足浓血出大吉","牛角有血主三公"):
    if s not in body: fails.append("ZG missing: "+s)
    if s not in z: fails.append("ZG not verbatim: "+s)

# 2. structure closure
for tag in ("div","blockquote","p","section","footer"):
    o, c = len(re.findall(rf'<{tag}[ >]', P)), P.count(f'</{tag}>')
    if o != c: fails.append(f"{tag} {o}/{c}")

# 3. first-screen rules: between h1 and first h2 — 0 Arabic, 0 CJK
seg = body.split('<h1>')[1].split('<h2>')[0]
if re.search(r'[\u0600-\u06ff]', seg): fails.append("Arabic before first h2")
if re.search(r'[\u4e00-\u9fff]', seg): fails.append("CJK before first h2")

# 4. ld+json valid
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', P, re.S):
    json.loads(m)

# 5. title / desc lengths
t = re.search(r'<title>(.*?)</title>', P).group(1)
d = re.search(r'<meta name="description" content="(.*?)">', P).group(1)
if not (45 <= len(t) <= 62): fails.append(f"title {len(t)}")
if not (120 <= len(d) <= 168): fails.append(f"desc {len(d)}")
ogt = re.search(r'og:title" content="(.*?)"', P).group(1)
ogd = re.search(r'og:description" content="(.*?)"', P).group(1)
if ogt != t and len(ogt) > 62: fails.append("og mismatch")

# 6. no placeholders, canonical
if '@@' in P: fails.append("placeholder left")
if 'dream/blood/' not in P: fails.append("canonical missing")

# 7. related links exist as files
for slug in re.findall(r'href="/dream/([a-z0-9-]+)/"', body):
    import os
    if not os.path.exists(f'/root/teethdreammeaning/site/dream/{slug}/index.html'):
        fails.append("dead internal link: "+slug)

print("FAILS =", len(fails))
for f in fails: print(" -", f)
