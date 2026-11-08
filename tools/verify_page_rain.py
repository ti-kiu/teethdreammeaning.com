#!/usr/bin/env python3
"""verify_page_rain.py — final-HTML checks for /dream/rain/:
quote-verbatim coverage vs corpus files, structure closure, first-screen rules,
ld+json validity, title/desc lengths. FAILS=0 to ship."""
import re, json, html as h

P = open('/root/teethdreammeaning/site/dream/rain/index.html', encoding='utf-8').read()
def norm(s): return re.sub(r'\s+', ' ', s).strip()

en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = norm(re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en))
en = norm(re.sub(r"\d+ IBN SEERIN'?S", ' ', en))
ars = {}
for f in ('315','316','317','318','328','338'):
    ars[f] = norm(open(f'/root/dream_research/nabulsi_page_{f}.txt', encoding='utf-8').read())
ars['347'] = norm(open('/root/dream_research/nabulsi_p347_349.txt', encoding='utf-8').read())
z = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()

fails = []
body = h.unescape(P)
src = body.rsplit('Sources (all passages', 1)[1]

# ---- 1. EN asserts: present in Sources AND verbatim in corpus ----
en_assert = [
  "Rain: (Clouds; Drizzling; Life; Vapor; Water) If no harm or destruction is caused",
  "it means a sickness. (Also see Water)",
  "Rainbow: (Fantasy; Illusion; Pipe dream) In a dream, a rainbow means peace and",
  "then it means war.",
  "Water level: (Artificial lake; Farm pond; Ombrometer; Ombrograh; Pluviometer;",
  "same interpretation. (Also see Water)",
  "Clouds: (Concealment; Gloom;",
  "harsh mandates.",
  "Ifpeople are expecting clouds to water their farms",
  "whom will perish during a trip.",
  "The death of an unknown woman in a dream means absence of rain or dearth, and if she comes back to life in the dream, it means rain.",
  "caravan of camels, and a caravan of camels\n".replace("\n"," ") if False else "Rain in a dream also represents a caravan of camels, and a caravan of camels in a dream represents rain.",
]
for s in en_assert:
    if s not in src: fails.append("Sources missing EN: "+s[:50])
    if s not in en: fails.append("EN assert not verbatim in corpus: "+s[:50])

# ---- 2. AR asserts: present in Sources AND verbatim in one corpus page ----
ar_assert = [
  ('315', "- (مطر) هو في المنام إذا لم يحصل منه ضرر"),
  ('315', "حياة من يخشى عليه من"),
  ('316', "آدمي أو أرض"),
  ('316', "وتتفجر العيون."),
  ('316', "- (ومن رأى) مطراً عاماً يحيا له أمر ميت"),
  ('316', "- (ومن رأى) المطر قد عاجله"),
  ('316', "- (ومن رأى) المطر في داره خاصة"),
  ('316', "والمحلة والموضع والقرية."),
  ('316', "- (ومن رأى) مطراً يسيح من كل جانب"),
  ('316', "في حين ضرره."),
  ('316', "- (ومن رأى) نفسه في المطر تحت سقف"),
  ('316', "قضيت له."),
  ('316', "- (ومن رأى) السماء قد أمطرت سيوفاً"),
  ('316', "فإنهم يمرضون."),
  ('316', "- (ومن رأى) أنه يشرب من ماء المطر"),
  ('316', "شرب من الماء."),
  ('317', "- (ميزاب) هو في المنام رجل صاحب معروف في بعض الأحيان."),
  ('317', "ميازيب تجري في غير مطر فإنها"),
  ('318', "تدل على فتن وكل ميزاب منها يدل على ضرب رقبة"),
  ('318', "بما ينزل منه الماء."),
  ('318', "- (ومن رأى) أنه تحت ميزاب الرحمة"),
  ('318', "كان بعكس ذلك."),
  ('328', "- (مطرقة) هي في المنام صاحب الشرط."),
  ('328', "اللغط في الكلام."),
  ('338', "- (مطران) من رأى في المنام أنه مطران يخضع له"),
  ('347', "وموت المرأة المجهولة يدل على إمساك القطر عن الأرض"),
  ('347', "أحيا الله تعالى الأرض بالغيث"),
]
for pg, s in ar_assert:
    if s not in src: fails.append(f"Sources missing AR({pg}): "+s[:40])
    if s not in ars[pg]: fails.append(f"AR({pg}) assert not verbatim in corpus: "+s[:40])

# ---- 3. CN asserts ----
cn_assert = ["天晴雨散百忧去","阴雨晦时主囚事","行路逢雨有酒食","狂风大雨人死亡"]
for s in cn_assert:
    if s not in src: fails.append("Sources missing CN: "+s)
    if s not in z: fails.append("CN not in zhougong corpus: "+s)
if z.count("雨") != 4: fails.append("zhougong rain count != 4")

# ---- 4. RTL blocks inside cite-rows + sources are Arabic; strip tags then check each injected AR block is a corpus substring ----
def devowel(s): return re.sub(r'[\u064B-\u0652\u0670\u0640]', '', s)
allar = " ".join(ars.values())
mtr_blocks = re.findall(r'<p class="ar">(.*?)</p>', body, re.S)
for b in mtr_blocks:
    bt = norm(re.sub(r'<[^>]+>', '', b))
    if not bt: continue
    ok = any(bt in ars[f] for f in ars) or bt in norm(en)
    if not ok:
        ok = devowel(bt) in devowel(allar)
    if not ok: fails.append("AR block not verbatim: "+bt[:60])

# ---- 5. structure closure ----
for tag in ('div','p','section','aside','main','article','footer','details','summary','ul','li','h1','h2','h3','title','style','script'):
    o = len(re.findall(r'<%s[\s>]' % tag, P)); c = P.count('</%s>' % tag)
    if o != c: fails.append(f"tag {tag} open {o} close {c}")

# ---- 6. first-screen rules: between h1 and first h2, no Arabic, no CJK ----
seg = P.split('<h1>')[1].split('<h2')[0]
if any('\u0600' <= ch <= '\u06ff' for ch in seg): fails.append("Arabic in first screen")
if any('\u4e00' <= ch <= '\u9fff' for ch in seg): fails.append("CJK in first screen")
# h1..firsth2 done; also no CJK/AR between top of body and first h2 (covers lede+aside)
seg2 = P.split('<div class="cols">')[1].split('<h2')[0]
if any('\u4e00' <= ch <= '\u9fff' for ch in seg2): fails.append("CJK in pre-first-h2 region")

# ---- 7. ld+json both groups parse ----
lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', P, re.S)
if len(lds) != 2: fails.append("ld+json count "+str(len(lds)))
for i, l in enumerate(lds):
    try: json.loads(h.unescape(l))
    except Exception as e: fails.append(f"ld+json {i} parse: {e}")

# ---- 8. title/desc lengths ----
t = re.search(r'<title>(.*?)</title>', P, re.S).group(1)
d = re.search(r'<meta name="description" content="(.*?)">', P).group(1)
if not (45 <= len(t) <= 60): fails.append("title len "+str(len(t)))
if not (120 <= len(d) <= 170): fails.append("desc len "+str(len(d)))

# ---- 9. internal links resolve to files on disk ----
for href in re.findall(r'href="(/dream/[a-z0-9-]+/)"', P):
    if not __import__('os').path.exists('/root/teethdreammeaning/site'+href+'index.html'):
        fails.append("dead internal link "+href)

print("FAILS =", len(fails))
for f in fails: print(" -", f)
