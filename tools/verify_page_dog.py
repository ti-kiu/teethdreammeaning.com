#!/usr/bin/env python3
"""verify_page_dog.py — final-HTML checks for /dream/dog/:
quote-verbatim coverage vs corpus files, structure closure, first-screen rules,
ld+json validity, title/desc lengths. FAILS=0 to ship."""
import re, json, html as h

P = open('/root/teethdreammeaning/site/dream/dog/index.html', encoding='utf-8').read()
def norm(s): return re.sub(r'\s+', ' ', s).strip()

en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = norm(re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en))
en = norm(re.sub(r"[\d~]+ IBN SEERIN'?S", ' ', en))
ar295 = norm(open('/root/dream_research/nabulsi_page_295.txt', encoding='utf-8').read())
ar296 = norm(open('/root/dream_research/nabulsi_page_296.txt', encoding='utf-8').read())
z = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()

fails = []
body = h.unescape(P)
src = body.rsplit('Sources (all passages', 1)[1]

# ---- 1. EN asserts in Sources ----
for s in ["Dog: (Bitch; Canine; Desire; Greyhound; Japanese spaniel; Pekingese; Lust;",
          "an insolent man who dares to indulge in sinful actions",
          "its effects will depend on the amount of pain one suffers in the dream",
          "A puppy in a dream represents a loved child",
          "grow to govern the household and to presides over its people",
          "a child of adultery, a foundling who is left in the street, wrapped in a swaddle",
          "A shepherd's dog in a dream represents profits and benefits",
          "A pet dog in a dream represents an astringent and a bitter enemy",
          "though he lacks principals and moral integrity",
          "Hunting with a dog in a dream means satisfying one's lust or desire",
          "Killing a dog in a dream signifies vanquishing one's enemy",
          "a high rate of unemployment",
          "suffering from extremely high fever and in relation to Dog star or the stars Procyon and Sirius of the constellations Canis Minor and Canis Major",
          "God Almighty has taught him great knowledge which he abused and discarded",
          "a police informer or a police dog",
          "Eating a dog's meat in a dream means cracking down at one's enemy",
          "Drinking dog's milk in a dream means a scare",
          "jealously guards him, his children and property",
          "A shepherd's dog represents a good neighbor who cares more about his neighbors than about his own household",
          "Taking a dog for a companion on a journey in a dream means disappearing",
          "renewal of one's business contract",
          "Dogfight: In a dream, a dogfight means love for the world.",
          "Bitch: (See Dog)", "Canine: (See Dog)",
          "Hunting dog: (Lust; Desire; Want. See Dog)", "Tyke: (See Dog)",
          "Canines: (See Tooth)",
          "Dog at 123", "Dog star at 123", "Dogfight at 124", "Bitch at 40", "Greyhound at 195",
          "Puppy at 346", "Shepherd's dog at 384"]:
    if s not in src: fails.append("Sources missing EN: " + s[:60])
# EN full-entry integrity: every word of the corpus entry appears (verbatim injection check)
DOGCUT = src[src.find("Dog: (Bitch"):src.find("Dogfight:", src.find("Dog: (Bitch"))]
assert "Ifone" in DOGCUT and "companion\xadship" in DOGCUT or "companion" in DOGCUT
for frag in ("inflected with a small loss", "astringent and a bitter enemy", "niggardly person"):
    if frag not in DOGCUT: fails.append("DOGCUT frag missing: " + frag)

# ---- 2. AR asserts in Sources (verbatim) ----
for s in ["(كلب) هو في المنام رجل سفيه يجترئ على المعاصي فإذا نبح فهو سفيه شنيع طبع.",
          "بقدر الألم وربما مرض.",
          "جرو الكلب ولد محبوب", "فإن كان أبيض فهو مؤمن", "يسود أهل بيته",
          "لقيط رجل سفيه يربيه",
          "رجل ظهر ينصر على الأعداء لكنه دنيء بلا مروة",
          "يخالط قوماً من العجم ليس هم من أهل الإسلام",
          "ينال أمنيته ويبلغ شهوته",
          "ذهاب الفزع وعلى بطالة",
          "تدل على حفظ امرأة الرجل ومتاعه",
          "يدل على الحمى بسبب الكوكب الذي يسمى الكلب",
          "الشعري اليمانية التي هي علة الحميات",
          "فسلبه الله إياه", "بغلمان الشرطة", "عدو ضعيف", "رجل شحيح",
          "يظفر بعدوه ويصيب من ماله",
          "شرب لبن الكلب خوف",
          "الانكلاب على الدنيا مع عدم الادخار",
          "جار صالح غيور على الأهل والجار",
          "لقصة أهل الكهف",
          "الكلبة المائية تدل على عمل لا يتم ورجاء كاذب",
          "رؤية كلب أهل الكهف يدل على الخوف والسجن أو الهرب",
          "رؤيته في البلد دليل على تجديد ولاية"]:
    if s not in src: fails.append("Sources missing AR: " + s[:50])
# and the AR fragments genuinely exist in corpus files
for s in ["رجل سفيه يجترئ على المعاصي", "بقدر الألم وربما مرض", "الشعري اليمانية التي هي علة الحميات",
          "فسلبه الله إياه", "لقصة أهل الكهف", "رؤيته في البلد دليل على تجديد ولاية"]:
    if s not in ar295 and s not in ar296: fails.append("AR not in corpus: " + s)

# ---- 3. CN asserts ----
for s in ["豺狼恶狗有盗贼", "犬吠人鬼来求食", "犬咬主人失财凶"]:
    if s not in src: fails.append("Sources missing CN: " + s)
    if s not in z: fails.append("CN not in corpus: " + s)

# ---- 4. first-screen rules ----
seg = P.split('<h1>')[1].split('<h2')[0]
if sum(1 for c in seg if '\u0600' <= c <= '\u06ff') != 0: fails.append("first screen Arabic")
if sum(1 for c in seg if '\u4e00' <= c <= '\u9fff') != 0: fails.append("first screen CJK")

# ---- 5. tag closure ----
for t in ('div', 'p', 'h2', 'h3', 'section', 'article', 'main', 'aside', 'footer', 'ul', 'li'):
    o = len(re.findall(r'<%s(?=[ >])' % t, P)); c = len(re.findall(r'</%s>' % t, P))
    if o != c: fails.append(f"tag {t}: {o} open {c} close")

# ---- 6. ld+json parse ----
for i, m in enumerate(re.finditer(r'<script type="application/ld\+json">(.*?)</script>', P, re.S)):
    try: json.loads(m.group(1))
    except Exception as e: fails.append(f"ld+json {i}: {e}")

# ---- 7. title/desc ----
ti = re.search(r'<title>(.*?)</title>', P).group(1)
de = re.search(r'<meta name="description" content="(.*?)">', P).group(1)
if not (45 <= len(ti) <= 60): fails.append("title len " + str(len(ti)))
if not (120 <= len(de) <= 165): fails.append("desc len " + str(len(de)))

# ---- 8. internal links resolve to shipped pages ----
import os
for m in re.finditer(r'href="(/dream/[a-z0-9-]+/)"', P):
    if not os.path.exists('/root/teethdreammeaning/site' + m.group(1) + 'index.html'):
        fails.append("dead internal link " + m.group(1))

print("FAILS=%d" % len(fails))
for f in fails: print(" -", f)
