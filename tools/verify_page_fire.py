#!/usr/bin/env python3
"""verify_page_fire.py — final-HTML checks for /dream/fire/:
quote-verbatim coverage vs corpus files, structure closure, first-screen rules,
ld+json validity, title/desc lengths. FAILS=0 to ship."""
import re, json, html as h

P = open('/root/teethdreammeaning/site/dream/fire/index.html', encoding='utf-8').read()
def norm(s): return re.sub(r'\s+', ' ', s).strip()

en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = norm(re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en))
en = norm(re.sub(r"\d+ IBN SEERIN'?S", ' ', en))
ars = {}
for f in ('348','349','350','360'):
    ars[f] = norm(open(f'/root/dream_research/nabulsi_page_{f}.txt', encoding='utf-8').read())
z = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()
m = open('/root/dream_research/mathes_schredl_2014.txt', encoding='utf-8', errors='ignore').read()

fails = []
body = h.unescape(P)
src = body.rsplit('Sources (all passages', 1)[1]

# ---- 1. EN asserts ----
en_assert = [
 "Fire: The element offire in a dream represents might",
 "It also means poverty and need. (Also see Body'; Firewood; Hell-fire)",
 "Seeing one's house turning gold in a dream means that a fire will consume his house.",
 "Torch: (Beacon) Carrying a torch in a dream means knowledge, wisdom, guiding",
 "he will receive little appreciation for his work.",
 "Firewood: Firewood in a dream means slander and backbiting",
 "their livelihood. (Also see Fire; Log)",
 "A fireplace in a dream also represents one's stomach and the firewood in a dream represents alate heavy meal that will cause indigestion or confused dreams.",
 "Worshipping fire: (Fire worshipper; Magi; Magus; Mazdaism; Sorcerer) Seeing an",
 "he is seeking unlawful earnings",
 "adversities.lfit is seen",
 "pIa es and mass loU",
 "one'sjob",
]
for s in en_assert:
    if s not in src: fails.append("Sources missing EN: "+s[:50])
    if s not in en: fails.append("EN assert not verbatim in corpus: "+s[:50])

# ---- 2. AR asserts (head + tail anchors per clause) ----
ar_assert = [
 ('348', "- (نار) هي في المنام بشارة وإنذار وحرب وعذاب وسلطان وحبس وخسارة وذنوب وبركة"),
 ('348', "فإنها فتنة يهلك منها عالم من الناس على قدر ما أحرقت."),
 ('348', "- (ومن رأى) ناراً في قلبه ذلك حب غالب"),
 ('348', "- (ومن رأى) نارين وكل منهما تهب إلى الأخرى"),
 ('348', "يخرج إلى المضاف إلى"),
 ('349', "النار التي فاض الماء عليها فتخمد ناره ويهلك جنده"),
 ('349', "وقيل إن النار إذا رؤيت نهاراً فهي دليل حرب وفتنة وإذا رؤيت ليلاً فهي دليل أنس"),
 ('349', "- (ومن رأى) أنه يعبد النار"),
 ('349', "- (ومن رأى) أنه يصطلي بالنار في الشتاء"),
 ('349', "- (ومن رأى) أنه يأكل النار"),
 ('349', "- (ومن رأى) أنه أمر به إلى النار"),
 ('349', "- (ومن رأى) جهنم عياناً"),
 ('349', "- (ومن رأى) ناراً مضيئة وحولها جماعة"),
 ('349', "- (ومن رأى) ناراً في بر وأنس إليها"),
 ('349', "- (ومن رأى) النار قد أحرقت شيئاً من الحبوب"),
 ('349', "- (ومن رأى) ناراً تحت قدر بلا طعام"),
 ('349', "- (ومن رأى) من الولاة أنه يوقد ناراً وهي تطفأ"),
 ('349', "- (ومن رأى) شعلة نار على بابه من غير دخان"),
 ('349', "- (ومن رأى) ناراً وقعت في بلدة أو في محلة"),
 ('349', "- (ومن رأى) أنه أجج ناراً ليصلى عليها"),
 ('349', "- (ومن رأى) ناراً أحرقت بعض ثيابه أو بعض أعضائه"),
 ('349', "- (ومن رأى) أنه اقتبس ناراً"),
 ('349', "- (ومن رأى) أنه أصابه وهج نار"),
 ('349', "- (ومن رأى) أنه أوقد ناراً على باب السلطان"),
 ('349', "- (ومن رأى) ناراً خرجت من داره"),
 ('349', "- (ومن رأى) أن شعاع ناره أضاء من المشرق إلى المغرب"),
 ('349', "- (ومن رأى) أن النار وقعت في بيته أصاب خصباً"),
 ('349', "- (ومن رأى) أنه يشعل ناراً في رأس جبل"),
 ('349', "- (ومن رأى) في تنوره ناراً موقدة وكان مزوجاً"),
 ('349', "- (ومن رأى) أنه جالس في النار وهي تحرقه"),
 ('349', "- (ومن رأى) أن ناراً نزلت من السماء فأحرقته"),
 ('349', "- (ومن رأى) أنه في وسط النار ولا يجد لها حراً"),
 ('349', "- (ومن رأى) ناراً طفئت فإنه تسكن الفتنة"),
 ('349', "- (ومن رأى) أنه جعل ناراً في وعاء أو أحرزها لنفسه"),
 ('349', "والمغرم الذي"),
 ('350', "يرميه السلطان على الناس."),
 ('350', "- (ومن رأى) أن عنده ناراً في تنور أو فرن أو كانون"),
 ('350', "- (ومن رأى) النار تتكلم في جرة أو قربة أو وعاء"),
 ('350', "وتدل النار في الشتاء على الفاكهة لقولهم النار فاكهة الشتاء"),
 ('360', "- (نارنج) هو في المنام شر كله أو فتنة."),
 ('360', "- (ومن رأى) جماعة يتراجمون بالنارنج"),
 ('360', "كثرة النارنج في البيت تدل على اشتعال النار فيه"),
]
for pg, s in ar_assert:
    if s not in src: fails.append(f"Sources missing AR({pg}): "+s[:40])
    if s not in ars[pg]: fails.append(f"AR({pg}) assert not verbatim in corpus: "+s[:40])

# ---- 3. CN asserts ----
cn_assert = ["水上火出主大吉","火烧日月大人助","火烧河水长命吉","火烧山野大显达","火烧自是主兴旺",
 "火焰炎炎主发财","火从地生疾病至","执火乘行官位至","大火烧天主国安","身在火中贵人扶",
 "火烟黑色主疾病","把火行路不通达","把火烧井主病至","执火入船主大吉","天火烧门主凶事"]
for s in cn_assert:
    if s not in src: fails.append("Sources missing CN: "+s)
    if s not in z: fails.append("CN not in zhougong corpus: "+s)
assert z.count('火') == 16, z.count('火')

# ---- 4. research numbers must match the PDF text ----
for s in ["Fire (34) 1.74 6.60 17.5 25.94 30.5 0.094*", "Teeth falling out (18) 0.56 2.12"]:
    if s.replace(' ',' ') not in norm(m): fails.append("PDF row not found: "+s[:40])
if "1.74%" not in body or "25.94%" not in body or "0.56%" not in body: fails.append("research numbers missing on page")

# ---- 5. structure ----
for tag in ('div','section','aside','main','article','footer','ul','li','h1','h2','h3','p','strong','em','a'):
    o = len(re.findall(r'<%s[ >]' % tag, P)); c = P.count('</%s>' % tag)
    if tag == 'p':  # <path false positives counted separately
        o = len(re.findall(r'<p[ >]', P))
    if o != c and tag not in ('li',):  # li pairs are inline-styled, checked anyway
        fails.append(f"tag {tag}: open {o} close {c}")
li_o = len(re.findall(r'<li[ >]', P)); li_c = P.count('</li>')
if li_o != li_c: fails.append(f"li: {li_o}/{li_c}")

# ---- 6. ld+json ----
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', P, re.S)
if len(blocks) != 2: fails.append("ld+json blocks != 2")
for b in blocks:
    try: json.loads(b)
    except Exception as e: fails.append("ld+json parse: "+str(e)[:80])

# ---- 7. first-screen rules ----
head_seg = P.split('<h1>')[1].split('<h2')[0]
ar_n = sum(1 for ch in head_seg if '\u0600' <= ch <= '\u06ff')
cn_n = sum(1 for ch in head_seg if '\u4e00' <= ch <= '\u9fff')
if ar_n: fails.append(f"first-screen Arabic {ar_n}")
if cn_n: fails.append(f"first-screen CJK {cn_n}")

# ---- 8. title/desc ----
t = re.search(r'<title>(.*?)</title>', P).group(1); d = re.search(r'<meta name="description" content="(.*?)"', P).group(1)
if not (45 <= len(t) <= 62): fails.append(f"title len {len(t)}")
if not (120 <= len(d) <= 170): fails.append(f"desc len {len(d)}")

print("FAILS =", len(fails))
for f in fails: print(" -", f)
print("div", P.count('<div'), P.count('</div>'), "| cite-rows AR clauses:", src.count('نار'), "| bytes:", len(P))
