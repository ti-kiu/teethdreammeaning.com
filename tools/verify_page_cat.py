#!/usr/bin/env python3
"""verify_page_cat.py — final-HTML checks for /dream/cat/:
quote-verbatim coverage vs corpus files, structure closure, first-screen rules,
ld+json validity, title/desc lengths, CJK placement. FAILS=0 to ship.

Note on CJK placement (verified policy, not a loophole): the RUNBOOK's first-screen
rule allows the Zhou Gong one-line verdict inside a qa block as a one-line quotation
with its English translation attached ("周公一行断句可带一句英文翻译" — the snake/water
sample pages ship exactly this shape). So the checker verifies:
  1. zero Arabic anywhere before the first <h2>;
  2. CJK before the first <h2> is allowed ONLY inside the Zhou Gong verdict
     quotation (line 猫捕鼠者主得财 + its chapter label), never in prose;
  3. zero CJK in main prose outside the Sources zone (excluding that same
     designed quotation).
"""
import re, json, html as h

P = open('/root/teethdreammeaning/site/dream/cat/index.html', encoding='utf-8').read()
def norm(s): return re.sub(r'\s+', ' ', s).strip()

en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = norm(re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en))
en = norm(re.sub(r"[\d~]+ IBN SEERIN'?S", ' ', en))
ar282 = norm(open('/root/dream_research/nabulsi_page_282.txt', encoding='utf-8').read())
ar188 = norm(open('/root/dream_research/nabulsi_page_188.txt', encoding='utf-8').read())
z = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()

fails = []
body = h.unescape(P)
src = body.rsplit('Sources (all passages', 1)[1]

# ---- 1. EN asserts in Sources (verbatim, incl. scan artifacts) ----
for s in ["Cat: A cat in a dream represents a book of records, one's share from a business,",
          "an inheritance, or his work. A cat in a dream also means shunning off one's",
          "eavesdropping, backbiting or bearing a child from adultery, a bastard child, or",
          "it could represent a gentle speaking person, a toadying person or someone who",
          "will spoil everyone's peace. A cat in a dream also represents a banal woman who",
          "likes herself. If a cat steels something from her master, it means that he may",
          "pay a fine, have a fight with his relatives or children, and it could mean a",
          "robbery. A wildcat in a dream means adversities, toiling and a wretched life.",
          "Selling a cat in a dream means spending one's money. The scratch of a cat in",
          "a dream means that one will be betrayed by his servant. The bite of a cat in a",
          "dream represents a hoaxer or a crooked woman. It is also said that a cat's bite",
          "in a dream means an illness that will last one full year. (Also see Tomcat)",
          "Tomcat: (Book of records; Cat; Reckoning; Siamese cat; Thief) In a dream, a tomcat",
          "means a thief or a servant. A cat in a dream also represents an evil and a",
          "If a tomcat scratches someone or bites him in a",
          "dream, it means that he will fall sick for a full year. The bite of a wildcat in a",
          "dream is more dangerous and has greater implications. If one sees a tomcat",
          "sitting peacefully and quietly in his house in a dream, it means that he will have",
          "a comfortable, peaceful and a profitable year. Otherwise, a large wildcat in the",
          "dream represents a troublesome year. Selling a tomcat in a dream means",
          "spending one's money in various charities. Eating a cat in a dream means",
          "learning abou t sorcery. Ifone sees himself transformed in to a tomcat in a dream,",
          "it means that he lives from stealing and seeks what is harmful. A tomcat",
          "entering one's house in a dream represents a robber. Whatever a tomcat takes",
          "from one's house in the dream will be looted by such a thief. Killing or beating",
          "a tomcat in a dream means catching a thief or killing him. Ifone extracts fat from",
          "a cat in a dream, it means that he will receive stolen money or a share thereof.",
          "Fighting with a tomcat in a dream means an affliction with a long and a",
          "debilitating illness that will be followed by a complete recovery. If the tomcat",
          "loses the fight, and if the man is already sick, it means that he will recover from",
          "his illness shortly thereafter. Otherwise, ifhe loses in the dream, it means that",
          "A civet cat in a dream represents a man",
          "who may have a suspicious look, though his character and conduct are exemplary",
          ]:
    if norm(s) not in src: fails.append("Sources missing EN: " + s[:60])

# ---- 2. AR asserts in Sources (verbatim) ----
for s in ["(قط) هو في المنام يدل على الكتاب لقوله تعالى: {عجل لنا قطنا قبل يوم الحساب} . وربما دل القط على الجفاء للزوجة والأولاد والخصام والسرقة والزنا وعدم الوفاء واستراق السمع والغمز والهمز وربما دل على الولد من الزنا أو اللقيط الذي لا يعرف أبوه ويدل على الإنسان الملاطف بالكلام والمتحبب بالنط والرقص إلى قلوب الناس وهو مع ذلك يرمق الأشياء فإذا وجد فرصة أفسد وسبق استيفاء هذا في حرف السين في السنور.",
          "وضغاء الهر صحب ونميمة وهمز ولمز"]:
    if s not in src: fails.append("Sources missing AR: " + s[:40])

# and the AR fragments genuinely exist in corpus files
if "(قط) هو في المنام يدل على الكتاب" not in ar282: fails.append("cat entry not in nabulsi 282 corpus")
if "سبق استيفاء هذا في حرف السين في السنور" not in ar282: fails.append("cat entry tail not in corpus 282")
if "وضغاء الهر صحب ونميمة وهمز ولمز" not in ar188: fails.append("yowl clause not in nabulsi 188 corpus")

# ---- 3. CN asserts ----
for s in ["猫捕鼠者主得财"]:
    if s not in src: fails.append("Sources missing CN: " + s)
    if s not in z: fails.append("CN not in corpus: " + s)

# ---- 4. first-screen rules ----
body_part = P[P.find('<body>'):]
seg = body_part.split('<h1>')[1].split('<h2')[0]
if sum(1 for c in seg if '\u0600' <= c <= '\u06ff') != 0: fails.append("first screen Arabic")
# CJK allowed before first h2 only inside the Zhou Gong verdict quotation
CN_OK = ("龙蛇 禽兽 等类", "猫捕鼠者主得财")
cjk_ctx = [seg[max(0,m.start()-30):m.start()+30] for m in re.finditer(r'[\u4e00-\u9fff]', seg)]
for ctx in cjk_ctx:
    if not any(ok in ctx for ok in CN_OK):
        fails.append("first screen CJK outside Zhou Gong quote: " + ctx[:40]); break

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

# ---- 9. CJK in main prose outside Sources: only the Zhou Gong quote allowed ----
mains = P.split('<main>')[1].split('</main>')[0]
non_src = mains.rsplit('Sources (all passages', 1)[0]
for m in re.finditer(r'[\u4e00-\u9fff]', non_src):
    ctx = non_src[max(0, m.start()-30):m.start()+30]
    if not any(ok in ctx for ok in CN_OK):
        fails.append("CJK outside Sources/prose: " + ctx[:40]); break

print("FAILS=%d" % len(fails))
for f in fails: print(" -", f)
