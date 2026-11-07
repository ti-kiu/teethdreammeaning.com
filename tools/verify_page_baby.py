#!/usr/bin/env python3
"""verify_page_baby.py — final-HTML checks for /dream/baby/:
quote-verbatim coverage vs corpus files, structure closure, first-screen rules,
ld+json validity, title/desc lengths. FAILS=0 to ship."""
import re, json, html as h, os

P = open('/root/teethdreammeaning/site/dream/baby/index.html', encoding='utf-8').read()
def norm(s): return re.sub(r'\s+', ' ', s).strip()

en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = norm(re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en))
en = norm(re.sub(r"\d+ IBN SEERIN'?S", ' ', en))
ars = []
for f in ('214','215','218'):
    ars.append(norm(open(f'/root/dream_research/nabulsi_page_{f}.txt', encoding='utf-8').read()))
z = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()

fails = []

# 1. injected corpus passages must be verbatim in corpus
body = h.unescape(P)
src = body.rsplit('Sources (all passages', 1)[1]
def devowel(s): return re.sub(r'[\u064B-\u0652\u0670\u0640]', '', s)
en_assert = [
  "Child: (Little boy) In a dream, a child carried in one's arms means responsibility",
  "the little girl then represents his glad tidings.",
  "Childbirth: (Giving birth) Seeing one's wife giving birth to a son in a dream",
  "giving birth in a dream means loss of his investment. (Also see Dragon)",
  "Boy: (Young boy) Seeing a young boy in a dream means receiving glad tidings.",
  "something good or bad may take place in wakefulness.",
  "Son: In a dream, a son may mean a daughter or a servant.",
  "Chicks: (Baby; Chicken; Fowl) A chick in a dream represents a stolen or a missing child.",
]
for s in en_assert:
    if s not in src: fails.append("Sources missing EN: "+s[:50])
    if s not in en: fails.append("EN assert not verbatim in corpus: "+s[:50])

ar_assert = [
  "(صبي) هو في المنام هم وغم إذا كان طفلا يحمل",
  "والصبي البالغ عزة وقوة.",
  "(ومن رأى) أنه صبي يتعلم في المكتب فإنه يتوب من ذنب كان",
  "يعمله إذا كان تعلمه قرآناً",
  "من العز إلى الهوان.",
  "(ومن رأى) أنه أمرد فإنه يرث ميراثاً من أمه",
  "وإذا رأى المريض أنه صبي فإنه يموت.",
  "(ومن رأى) نفسه صبياً وله محاكمة فإنه يقهر.",
  "(ومن رأى) وجهه في المرآة وجه صبي",
  "عاقبته مذمومة.",
  "(ومن رأى) أنه يحمل صبياً فإنه يدبر ملكاً",
  "كيوم ولدته أمه.",
  "(ومن رأى) أن له ولداً صغيراً",
  "هموم صغيرة يسيرة.",
  "(ومن رأى) أن في حجره صبياً فإنه يضرب بالعود",
  "وكثرة الخير المترادف.",
  "(صبية) صغيرة رؤيتها في المنام تدل على خصب وعز",
  "فإن حملها جارية تشبهها.",
  "(ومن رأى) أنه اشترى غلاماً أصابه هم ومن اشترى جارية أصاب خيراً.",
  "(ومن رأى) أنه يحمل صبية",
  "أن يحمل صبياً.",
  "(ومن رأى) أنه عاد طفلاً فإن كان في قماط سجن أو مرض",
  "عاش إلى أرذل العمر.",
  "(صبيان القمل) هو في المنام قوم مفسدون",
  "ولا يقدر على منعهم.",
]
for s in ar_assert:
    sd = devowel(s)
    if s not in src and sd not in devowel(src): fails.append("Sources missing AR: "+s[:40])
    if not any(sd in devowel(a) for a in ars): fails.append("AR assert not verbatim in corpus: "+s[:40])

for s in ("抱小儿女主口舌","小儿死者主口舌","新生男女主大吉","子死者主添喜事","齿落更生子孙兴"):
    if s not in body: fails.append("ZG missing: "+s)
    if s not in z: fails.append("ZG not verbatim: "+s)

# 2. structure closure (word-boundary tags; no self-closing p/path confusion)
for tag in ("div","section","footer","aside","main","article","details","ul","li","h1","h2","h3"):
    o, c = len(re.findall(rf'<{tag}[ >]', P)), P.count(f'</{tag}>')
    if o != c: fails.append(f"{tag} {o}/{c}")
po = len(re.findall(r'<p[ >]', P)); pc = P.count('</p>')
if po != pc: fails.append(f"p {po}/{pc}")

# 3. first-screen rules: between h1 and first h2 — 0 Arabic, 0 CJK
seg = body.split('<h1>')[1].split('<h2')[0]
if re.search(r'[\u0600-\u06ff]', seg): fails.append("Arabic before first h2")
if re.search(r'[\u4e00-\u9fff]', seg): fails.append("CJK before first h2")

# 4. ld+json valid
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', P, re.S):
    json.loads(m)

# 5. title / desc lengths
t = re.search(r'<title>(.*?)</title>', P).group(1)
d = re.search(r'<meta name="description" content="(.*?)">', P).group(1)
if not (45 <= len(t) <= 62): fails.append(f"title {len(t)}: {t}")
if not (120 <= len(d) <= 168): fails.append(f"desc {len(d)}")

# 6. no placeholders, canonical
if '@@' in P: fails.append("placeholder left")
if 'dream/baby/' not in P: fails.append("canonical missing")

# 7. related links exist as files
for slug in re.findall(r'href="/dream/([a-z0-9-]+)/"', body):
    if not os.path.exists(f'/root/teethdreammeaning/site/dream/{slug}/index.html'):
        fails.append("dead internal link: "+slug)

# 8. all CJK sits inside Sources/note zones (no CJK in prose qa blocks)
qa_zone = body.split('<div class="qa">')
for i, q in enumerate(qa_zone[1:]):
    q = q.split('</div>')[0]
    if re.search(r'[\u4e00-\u9fff\u0600-\u06ff]', q):
        fails.append(f"non-Latin text inside qa block {i}")

print("FAILS =", len(fails))
for f in fails: print(" -", f)
