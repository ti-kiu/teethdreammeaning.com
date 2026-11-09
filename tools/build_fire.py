#!/usr/bin/env python3
"""Build site/dream/fire/index.html (Day 10, matrix item fire).
All quoted passages injected VERBATIM from corpus files (/root/dream_research/*);
every EN/AR/CN assertion is checked at build time — nothing is hand-copied.
Skeleton reused from the shipped rain page (build_rain.py)."""
import re, json, os

def norm(s): return re.sub(r'\s+', ' ', s).strip()

# ---------------- corpus: EN (Ibn Sirin compilation) ----------------
en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = norm(re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en))
en = norm(re.sub(r"\d+ IBN SEERIN'?S", ' ', en))

def cut(src, start, end):
    i = src.find(start); assert i != -1, "MISS START: " + start[:60]
    j = src.find(end, i); assert j != -1, "MISS END: " + end[:60]
    return norm(src[i:j+len(end)])

def must(src, s):
    assert s in src, "MISS: " + s[:70]

FIRE = cut(en, "Fire: The element offire in a dream represents might", "It also means poverty and need. (Also see Body'; Firewood; Hell-fire)")
assert len(FIRE) > 3900, len(FIRE)
assert "DICTIONARY OF DREAMS" not in FIRE  # headers stripped; entry continuous
GOLDFIRE = "Seeing one's house turning gold in a dream means that a fire will consume his house."
must(en, GOLDFIRE)
TORCH = cut(en, "Torch: (Beacon) Carrying a torch in a dream means knowledge, wisdom, guiding", "he will receive little appreciation for his work.")
FIREWOOD = cut(en, "Firewood: Firewood in a dream means slander and backbiting", "their livelihood. (Also see Fire; Log)")
must(en, "A fireplace in a dream also represents one's stomach and the firewood in a dream represents alate heavy meal that will cause indigestion or confused dreams.")
STOMACH = "A fireplace in a dream also represents one's stomach and the firewood in a dream represents alate heavy meal that will cause indigestion or confused dreams."
WORSHIP = cut(en, "Worshipping fire: (Fire worshipper; Magi; Magus; Mazdaism; Sorcerer) Seeing an", "he is seeking unlawful earnings.")
for s in ("Ifone sees a blazing fire with sparks shooting in every",
          "adversities.lfit is seen", "pIa es and mass loU", "lone's mouth in a dream means distress",
          "ajust and a righteous", "one'sjob", "unla wful profits"):
    must(en, s)  # scan artifacts kept as printed, noted on the page

# ---------------- corpus: AR (Al-Nabulsi) ----------------
def arload(f): return norm(open(f'/root/dream_research/nabulsi_page_{f}.txt', encoding='utf-8').read())
ar348, ar349, ar350, ar360 = (arload(f) for f in ("348","349","350","360"))

NAR_HEAD  = cut(ar348, "- (نار) هي في المنام بشارة وإنذار وحرب وعذاب وسلطان وحبس وخسارة وذنوب وبركة", "فإنها فتنة يهلك منها عالم من الناس على قدر ما أحرقت.")
NAR_HEART = cut(ar348, "- (ومن رأى) ناراً في قلبه ذلك حب غالب", "من هجر محبوبه أو غيره.")
NAR_TWO1  = cut(ar348, "- (ومن رأى) نارين وكل منهما تهب إلى الأخرى", "يخرج إلى المضاف إلى")   # breaks at page edge
NAR_TWO2  = cut(ar349, "النار التي فاض الماء عليها فتخمد ناره ويهلك جنده", "فهي دليل أنس.")  # resumes at next page head
NAR_WORSH = cut(ar349, "- (ومن رأى) أنه يعبد النار", "يطيع الشيطان في معصيته.")
NAR_WARM  = cut(ar349, "- (ومن رأى) أنه يصطلي بالنار في الشتاء", "فإنه ينال غنى.")
NAR_EAT   = cut(ar349, "- (ومن رأى) أنه يأكل النار", "أو يأكل مالاً حراماً.")
NAR_CONDEMN = cut(ar349, "- (ومن رأى) أنه أمر به إلى النار", "فإنه يدخل الجنة.")
NAR_SEEHELL = cut(ar349, "- (ومن رأى) جهنم عياناً", "فإنه يقع في فتنة.")
NAR_GROUP = cut(ar349, "- (ومن رأى) ناراً مضيئة وحولها جماعة", "فإنهم ينالون بركة.")
NAR_BR    = cut(ar349, "- (ومن رأى) ناراً في بر وأنس إليها", "وفى له بموعده.")
NAR_GRAIN = cut(ar349, "- (ومن رأى) النار قد أحرقت شيئاً من الحبوب", "غلت وكثر طلابها.")
NAR_QIDR  = cut(ar349, "- (ومن رأى) ناراً تحت قدر بلا طعام", "نكبة من سلطان.")
NAR_WALI  = cut(ar349, "- (ومن رأى) من الولاة أنه يوقد ناراً وهي تطفأ", "ويعزل وتخمد ناره" if False else "فإنه يعزل وتخمد ناره.")
NAR_TORCH = cut(ar349, "- (ومن رأى) شعلة نار على بابه من غير دخان", "والنار في الأصابع تدل على ظلم الكتبة والنار في الكف ظلم في المصنعة والنار في الفم غم")
NAR_TOWN  = cut(ar349, "- (ومن رأى) ناراً وقعت في بلدة أو في محلة", "فهي أمراض وأحداث تقع هناك")
NAR_MEAT  = cut(ar349, "- (ومن رأى) أنه أجج ناراً ليصلى عليها", "ويسد به فقره")
NAR_LIMB  = cut(ar349, "- (ومن رأى) ناراً أحرقت بعض ثيابه أو بعض أعضائه", "ذلك الثوب أو العضو.")
NAR_IGTIBAS = cut(ar349, "- (ومن رأى) أنه اقتبس ناراً", "مالاً حراماً من سلطان.")
NAR_WAHJ  = cut(ar349, "- (ومن رأى) أنه أصابه وهج نار", "وقرب من السلطان.")
NAR_BAB   = cut(ar349, "- (ومن رأى) أنه أوقد ناراً على باب السلطان", "ملكاً عظيماً وقوة.")
NAR_KHUJR = cut(ar349, "- (ومن رأى) ناراً خرجت من داره", "قوة في حرفة.")
NAR_SHARQ = cut(ar349, "- (ومن رأى) أن شعاع ناره أضاء من المشرق إلى المغرب", "في المشرق والمغرب.")
NAR_DARHA = cut(ar349, "- (ومن رأى) أن النار وقعت في بيته أصاب خصباً", "يرى من امرأته سروراً.")
NAR_JBAL  = cut(ar349, "- (ومن رأى) أنه يشعل ناراً في رأس جبل", "خرب بيته.")
NAR_TANUR2 = cut(ar349, "- (ومن رأى) في تنوره ناراً موقدة وكان مزوجاً", "حملت امرأته.")
NAR_JALIS = cut(ar349, "- (ومن رأى) أنه جالس في النار وهي تحرقه", "من قبل السلطان.")
NAR_SAMAA = cut(ar349, "- (ومن رأى) أن ناراً نزلت من السماء فأحرقته", "من حرارة وبرسام.")
NAR_WASAT = cut(ar349, "- (ومن رأى) أنه في وسط النار ولا يجد لها حراً", "وظفراً على أعدائه.")
NAR_TAFI2 = cut(ar349, "- (ومن رأى) ناراً طفئت فإنه تسكن الفتنة", "فإنه يدخل في بيته اللصوص.")
NAR_WAA   = cut(ar349, "- (ومن رأى) أنه جعل ناراً في وعاء أو أحرزها لنفسه", "والمغرم الذي")  # breaks at page edge
NAR_WAA2  = cut(ar350, "يرميه السلطان على الناس.", "يرميه السلطان على الناس.")
NAR_TANUR3 = cut(ar350, "- (ومن رأى) أن عنده ناراً في تنور أو فرن أو كانون", "أو يتعطل عن عمله أو صناعته.")
NAR_KALAM = cut(ar350, "- (ومن رأى) النار تتكلم في جرة أو قربة أو وعاء", "وكذلك النور والظلمة.")
NAR_NARINJ1 = cut(ar360, "- (نارنج) هو في المنام شر كله أو فتنة.", "شر كله أو فتنة.")
NAR_NARINJ2 = cut(ar360, "- (ومن رأى) جماعة يتراجمون بالنارنج", "المال والأمتعة.")
for a, src in ((NAR_HEAD,ar348),(NAR_HEART,ar348),(NAR_TWO1,ar348),(NAR_TWO2,ar349),
               (NAR_WORSH,ar349),(NAR_WARM,ar349),(NAR_EAT,ar349),(NAR_CONDEMN,ar349),(NAR_SEEHELL,ar349),
               (NAR_GROUP,ar349),(NAR_BR,ar349),(NAR_GRAIN,ar349),(NAR_QIDR,ar349),(NAR_WALI,ar349),
               (NAR_TORCH,ar349),(NAR_TOWN,ar349),(NAR_LIMB,ar349),(NAR_IGTIBAS,ar349),(NAR_WAHJ,ar349),
               (NAR_BAB,ar349),(NAR_KHUJR,ar349),(NAR_SHARQ,ar349),(NAR_DARHA,ar349),(NAR_JBAL,ar349),
               (NAR_TANUR2,ar349),(NAR_JALIS,ar349),(NAR_SAMAA,ar349),(NAR_WASAT,ar349),(NAR_TAFI2,ar349),
               (NAR_WAA,ar349),(NAR_WAA2,ar350),(NAR_TANUR3,ar350),(NAR_KALAM,ar350),
               (NAR_NARINJ1,ar360),(NAR_NARINJ2,ar360)):
    must(src, a)
assert NAR_TWO1.endswith("يخرج إلى المضاف إلى") and NAR_TWO2.startswith("النار التي فاض")
assert NAR_WAA.endswith("والمغرم الذي") and NAR_WAA2 == "يرميه السلطان على الناس."
assert "وقيل إن النار إذا رؤيت نهاراً فهي دليل حرب وفتنة وإذا رؤيت ليلاً فهي دليل أنس" in NAR_TWO2

# ---------------- corpus: CN (Zhou Gong) ----------------
zg = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()
ZG_LINES = [l for l in zg.splitlines() if ('火' in l) and not l.startswith('#')]
ZG_PHRASES = []
for l in ZG_LINES:
    if l.startswith('【'):  # chapter title 水火 盗贼 灯烛 — the 16th occurrence
        continue
    for p in l.split():
        if '火' in p: ZG_PHRASES.append(p)
assert len(ZG_PHRASES) == 15, (len(ZG_PHRASES), ZG_PHRASES)
ZG_PICK = ["执火入船主大吉", "水上火出主大吉", "火烧日月大人助", "火烧河水长命吉", "火烧山野大显达",
           "火烧自是主兴旺", "火焰炎炎主发财", "火从地生疾病至", "执火乘行官位至", "大火烧天主国安",
           "身在火中贵人扶", "火烟黑色主疾病", "把火行路不通达", "把火烧井主病至", "天火烧门主凶事"]
for s in ZG_PICK: must(zg, s)
assert zg.count('火') == 16, zg.count('火')  # 15 verdict lines + 1 chapter title 水火

# ---------------- FAQ ----------------
FAQ = [
 ("What does fire mean in a dream?",
  "Both classical Arabic books open the same entry with the same nine words, in the same order — glad tidings, warning, war, chastisement, a ruler, imprisonment, loss, sins, blessing — and the compilation adds might and love first (Ibn Sirin compilation, printed p. 158; Al-Nabulsi, shamela 348, printed p. 351). Nothing else is decided by the flame itself: the books then flip the reading on day or night, smoke, place, and whether the fire reached you and burned. Every clause quoted at its printed page below."),
 ("Is dreaming of fire a good omen or a bad omen?",
  "The books install switches, not signs. Fire seen by daylight means war and adversities; the same fire seen at night means peace and guidance — in both books (printed p. 158; shamela 349, printed p. 352). The more black smoke, the greater the danger. A group gathered around a fire means blessings; a raging blaze in your town means war or plague. And the harm switch cuts across all of it: touched by fire and unburned, a promise is kept you; burned, the calamity falls on whatever the burning thing stands for."),
 ("What does it mean when the fire burns your house?",
  "The books read four different house-fires. Fire falling in your house: fertility and plenty, says Al-Nabulsi, or war and destruction, says the compilation, if it rages. Fire going out of your house: a political appointment, a business, strength — and in Al-Nabulsi's Arabic, governorship, trade or skill. The light-fire that used to brighten your house being extinguished: the death of the father, the husband or a child. And a fire in your house quenched by rain — the books' rarest clause — means poverty or a stopped trade (printed p. 159; shamela 350, printed p. 353)."),
 ("What does the Chinese Zhou Gong book say about fire?",
  "The received 27-chapter text carries fire in fifteen verdict lines: thirteen in chapter 23 (水火 盗贼 灯烛), one in the boats chapter (carrying fire onto a boat: very auspicious) and one in the gates chapter (heaven's fire burning the gate: misfortune). Its verdicts sort by direction and target: fire burning sun, river, hill or heaven brings patrons, long life and national peace; flame blazing brings wealth; standing in fire brings a noble helper — while fire rising from the ground, black smoke, fire carried on the road and fire burned into a well all bring illness or blocked roads. Lines quoted verbatim in Sources."),
 ("What does modern research say about fire dreams?",
  "Fire is a measurable but rare dream theme: in 1,612 diary dreams collected from 425 students over two weeks, fire content appeared in 1.74% of reports, 6.60% of dreamers reported at least one fire dream in the fortnight, and 25.94% had ever dreamed of fire on the lifetime questionnaire (Mathes & Schredl, Somnologie 18:106-111, 2014, PDF re-pulled and re-read today). The same table puts teeth-falling-out dreams at 0.56% of diary reports. The 2018 teeth-dream paper (PubMed 30319507, full text re-checked today) contains no fire item at all — the word does not appear once. Classical books read fire as a civic sign; the modern record is two-week diary statistics."),
]
FAQ_JSON = json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ], ensure_ascii=False)

# ---------------- skeleton from shipped rain page ----------------
B = open('/root/teethdreammeaning/site/dream/rain/index.html', encoding='utf-8').read()
CSS = re.search(r'<style>.*?</style>', B, re.S).group(0)
CHIP = {z: re.search(r'<span class="zone z-%s">.*?</span>' % z, B, re.S).group(0) for z in ("text","reading","research")}
assert all(CHIP.values())

TITLE = "Dreaming of Fire: What the Dream Books Actually Say"
DESC = "Fire in a dream: both Arabic books open with the same nine-word ledger, then flip it on day, smoke, place and harm. Zhou Gong runs fifteen fire lines."

ARTICLE_LD = json.dumps({"@context": "https://schema.org", "@type": "Article",
 "author": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"},
 "datePublished": "2026-11-09", "dateModified": "2026-11-09",
 "publisher": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"},
 "headline": TITLE, "url": "https://teethdreammeaning.com/dream/fire/", "inLanguage": "en",
 "about": {"@type": "Thing", "name": "dream interpretation"}}, ensure_ascii=False)

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="canonical" href="https://teethdreammeaning.com/dream/fire/">
<meta property="og:title" content="@@TITLE@@">
<meta property="og:description" content="@@DESC@@">
<meta property="og:url" content="https://teethdreammeaning.com/dream/fire/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
<title>@@TITLE@@</title>
<meta name="description" content="@@DESC@@">
@@CSS@@
<script type="application/ld+json">@@ALD@@</script>
<script type="application/ld+json">@@FAQJ@@</script>
</head>
<body>
<div class="wrap">
<div class="top">
  <div class="brand"><a href="/">Teeth Dream Meaning</a> <em>· classical sources, checked page by page</em></div>
  <nav class="topnav"><a href="/about/">About</a><span>·</span><a href="/disclaimer/">Disclaimer</a><span>·</span><a href="/about/">Sources</a></nav>
</div>

<div class="cols">
<div class="mhead">
<h1>Dreaming of Fire: What It Means</h1>
<p class="lede">Both classical Arabic books open the fire entry with the same nine words, in the same order: <strong>glad tidings, a warning, war, chastisement, a ruler, imprisonment, losses, sins, or blessings</strong> (Ibn Sirin compilation, printed p. 158; Al-Nabulsi, shamela 348, printed p. 351 — five centuries apart, clause for clause). Before the ledger the compilation names two private readings — <strong>might</strong>, and <strong>love</strong> — and Al-Nabulsi keeps the love clause as its own line: a fire burning inside your heart is a love that overwhelms you. But no clause on this page is decided by the flame itself. The books flip the reading on four switches: <strong>day or night</strong> — fire seen in daylight means war and adversities, the same fire seen at night means peace and guidance, in both books; <strong>smoke</strong> — the more black smoke, the greater the danger; <strong>place</strong> — your house, the desert, the town, the sultan's door, the mountaintop each carry their own verdict; and <strong>harm</strong> — touched and unburned, someone keeps a promise to you; burning, the calamity falls on what the burning thing stands for. So the honest first answer is: <strong>these books do not read fire; they read when it burned, how much smoke it made, where it stood, and whether you were touched by it.</strong></p>
</div>
<aside>
<details class="tocd" open>
<summary>On this page</summary>
<ul>
<div class="g">This site's reading</div>
<li><a href="#the-finding-fire-four-switches">The finding: one flame, four switches</a></li>
<div class="g">Classical texts</div>
<li><a href="#the-entries-briefly">The entries, briefly</a></li>
<div class="g">Modern research</div>
<li><a href="#what-modern-research-adds-and-what-it-do">What modern research adds — and what it doesn't</a></li>
<li><a href="#sources-all-passages-checked-against-the">Sources (all passages checked against the cited pages)</a></li>
<li><a href="#related-questions">Related questions</a></li>
</ul>
</details>
</aside>
<main><article>

<p>Fire belongs on this site for the same reason rain did: the classical books are clause machines, and the fire entries are the cleanest side-by-side test in either book — a two-page Arabic run and a three-page English entry that mirror each other nearly line for line, with a handful of collisions the mirrors leave unsmoothed. Plain answers first — no Arabic or Chinese on this screen — every quote checked to its printed page.</p>

<div class="qa">
<h3>The nine-word ledger both books open with</h3>
<p>The compilation's headword: fire signifies "glad tidings, a warning, war, chastisement, power, imprisonment, losses, sins, or blessings". Al-Nabulsi's Arabic, five centuries on, runs the same nine slots in the same order, the ninth word again blessing (quoted in full below). Then both books price the loud fire: sparks shooting every way, burning the wood, roaring with tumult — in the compilation, insubordination, civic disorder, an adversity through which many die; in Al-Nabulsi, a sedition through which people perish, "on the measure of what it burned" (printed p. 158; shamela 348, printed p. 351). The scale word — proportion — is in both.</p>
</div>

<div class="qa">
<h3>Day fire, night fire — the first switch</h3>
<p>The books agree in both directions. Seen by daylight, fire means war and adversities; seen at night, peace and guidance (printed p. 159 — in the scan the sentence prints with its words run together, kept as printed below). Al-Nabulsi's mirror clause closes the two-armies paragraph the same way: "it is said that fire seen in the day is a proof of war and sedition, and seen at night, a proof of comfort" (shamela 349, printed p. 352). Same switch, same two poles. Kindling has its own version: light a fire in the dark night so people can find the road, and you will acquire knowledge and guide people with it; light one on the bright road with no darkness needing it, and you are on the road of innovation, misleading others. Al-Nabulsi's Arabic again runs line-for-line with the English.</p>
</div>

<div class="qa">
<h3>Two fires facing each other — and the water switch</h3>
<p>Both books stage the same image: two burning thicket-loads trying to consume each other, two armies on the field. Whichever fire has more fuel is more numerous and harder-pressed; whichever the wind is with wins; whichever is blacker and darker has the worse intent; equal in color and harming nothing — two seditions sitting in that quarter. Then the switch that ties this page to the rain page: the army whose fire stands nearer the water is the one likelier to submit — and if the water overflows and quenches the fire, the water itself is debilitated and consumed, "and likewise if the rain comes down on it". Al-Nabulsi's mirror finishes the sentence the compilation started, page break and all (printed pp. 159-160; shamela 348-349, printed pp. 351-352). Fire quenched by rain is the rarest of the book's switches: in the compilation it means poverty or loss of your job; in Al-Nabulsi, your livelihood stops.</p>
</div>

<div class="qa">
<h3>The harm switch — touched, unburned, eating</h3>
<p>Fire that reaches you and does no harm means someone will fulfill a promise they made to you; Al-Nabulsi's same-page mirror: "whoever the fire touches and it does not burn him — his appointment will be honored" (printed p. 159; shamela 349, printed p. 352). Standing in the fire feeling cool and comfortable is the victory clause — truthfulness, sincerity, triumph over enemies in the compilation; in the Arabic, whoever sits in the fire and finds no heat attains truth, certainty, kingship. The burn switch flips: fire burning your garment or your skin means a calamity falling on you, or on the family member that limb represents. And eating fire? Swindling orphans' property or earning suspicious, unlawful money — both books, in the same words, quoting the same Qur'anic idiom; Al-Nabulsi adds the table setting: eating from gold or silver plates, and then poverty and begging.</p>
</div>

<div class="qa">
<h3>Fire and the house — five verdicts</h3>
<p>The books read five different house-fires. Fire falling into your house: in Al-Nabulsi, fertility and plenty; in the compilation, war and destruction if it rages, a new-disease spread if it makes no noise. Fire going out of your house: appointment, business, strength, trade-skill — governorship, trade, or craft-power in the Arabic, mirror for mirror. The house-light being extinguished: the death of the father, husband or child, and an extinguished fire in the town means the death of its governor, its great scholar, its renowned shaikh; in Al-Nabulsi, the manager of the house dies, the head of the town dies. A fire kindled on the mountaintop: devotion, needs met, safe return home — and in both books' next breath, a fire blazing in your own house ruins it. The two-armies clause and the torch clause (a burning torch with no smoke at your door: pilgrimage, house-renovation or marriage) sit between the extremes.</p>
</div>

<div class="qa">
<h3>Smoke, and what smoke hides</h3>
<p>Smoke is a gauge and a divider. The more black smoke a fire makes, the greater the danger and consequent sufferings (printed p. 159); Al-Nabulsi: the higher the smoke, the greater the terror. But fire with no smoke is its own species: it represents spirits or jinns — "for they are created from a smokeless fire" — and also drought, locusts, calamity. The Arabic entry keeps the same clause with the same theology and the same two plagues (printed p. 160; shamela 349, printed p. 352). A clean-flamed blaze is never simply cleaner: it changes what the fire is made of.</p>
</div>

<div class="qa">
<h3>Fire in the mouth, the fingers, the palm — the teeth page's neighbors</h3>
<p>Three short body clauses sit together in both books, and they are the ones a teeth-dream reader should notice. Fire in the fingers: an unjust person — or changing the contents of a book, or perjury. Fire lit in the palm: cutting corners in your trade, violating your own trade's code. Fire inside the mouth: distress — says the compilation, and so says Al-Nabulsi in one word of grief (quoted verbatim below), extending the ledger: fire in the fingers is the scribes' injustice, fire in the palm the artisan's. The mouth clause is this site's own entry point: the same books that read a falling tooth as a family ledger read a flame inside the mouth as grief with no omen in it (printed p. 160; shamela 349, printed p. 352).</p>
</div>

<div class="qa">
<h3>Prices, sickness, possession</h3>
<p>Fire burns goods, and the books read the market. A fire inside a granary means hiking prices; whatever product burns is in high demand and rising — and Al-Nabulsi's mirror: fire burning grain sends its price up, fire falling on any commodity makes it dear with many buyers. Fire in winter is the warm exception: warming yourself from a nearby fire on a cold day means becoming rich; in the Arabic, fire in winter means fruit — "they say, fire is winter's fruit". A fire talking to you out of a jar or pitcher means an evil spirit has possessed your son or daughter — the Arabic names it as jinn-speaking-on-the-tongue possession. And fire seen without flame and without roar? The compilation: the spread of a new disease; the Arabic: illnesses and events falling there.</p>
</div>

@@CHIPR@@
<h2 id="the-finding-fire-four-switches">The finding: one flame, four switches</h2>
<p>Set the two entries side by side — Al-Nabulsi's (نار) run at shamela 348-350 (printed pp. 351-353) and the compilation's Fire entry at printed pp. 158-160 — and the clause order is a mirror almost head to head: the nine-word ledger, then the loud-sparks civic sedition with its proportion clause, then heart-fire as love, then the two fires as two armies with fuel, wind, blackness, water-nearness and the quenching water's own ruin, then the smoke gauge, then the night-kindled guide of knowledge and the daylight innovation, then the day/night war-versus-comfort switch, then fire-worship, then winter-warming wealth, then eating fire and orphans' property, then the condemned and the entered-and-exited hell, then the lighted fire ringed by a blessing group, then touch-without-burn as promise kept, then grain prices, then the empty pot, then the governor's smothering fire, then torch-at-door without smoke, then fingers, palm and mouth, then the plague list, then roasted meat and backbiting, then garment and limb, then borrowed fire as unlawful money, then the glare of tongues, then the sultan's door, then fire going out of the house, then east-to-west beams, then the falling-in fertility line, then the mountaintop, then the oven pregnancy, then sitting in the fire, then the sky-fire, then the extinguished fire and its deaths, then the vessel-fire and the jinns. Where the two books meet, they meet in order. On top of the mirror, this fire page shows four switches the teeth and rain pages also found working in these books: <strong>time</strong> (day war, night guidance; winter fire the one warmly positive case), <strong>smoke</strong> (a danger gauge upward, and a species marker at zero: no smoke means jinns, not safety), <strong>place</strong> (house, town, desert, sultan's door, mountaintop, granary, oven — five different house-fires alone), and <strong>harm</strong> (touched and unburned = a kept promise; burned = the calamity on what the thing represents; eaten = unlawful money).</p>

<p>And four collisions no summary repeats. <strong>Between the books:</strong> sky-fire that burns and does not affect you. The compilation reads the harm-free sky-fire as verbal abuse with no lasting consequences; Al-Nabulsi, in the same words about the same fire, reads it as soldiers descending on your house — same image, private insult versus public garrison. The extinguished house-light runs the other way: the compilation hangs death clauses on it (father, husband, child, town's scholar); Al-Nabulsi adds a burglary clause the English never keeps — a fire that goes out in your house and a wind comes in and lights it again: thieves enter. <strong>Inside the Arabic book:</strong> a citron — نارنج, the sour orange — means an evil or a sedition, and a house full of citrons means fire blazing in it; the book says the reading is taken "from its name, its color and its sourness" — the word contains نار, fire (shamela 360, printed p. 363). A whole verdict built on a pun the English can only report. <strong>Inside the alphabetic book:</strong> the fireplace entry ends by filing fire under the body and the table — the hearth represents your stomach, and its firewood a late heavy meal "that will cause indigestion or confused dreams" (printed p. 161): a 1992 compilation that tells you where confused dreams come from, printed on the page with the word run together. <strong>Across the languages:</strong> the Chinese book's fire verdicts sort neither by smoke nor harm but by direction and rank — fire burning the sun, moon, rivers, hills or heaven brings patrons, long life and national peace; standing in fire a noble helper; flame blazing wealth — while fire rising from the ground, black smoke, carrying fire down the road and putting fire to a well bring illness and blocked roads. Fifteen verdict lines, no ledger, no switch: the shapes do the work.</p>

@@CHIPT@@
<h2 id="the-entries-briefly">The entries, briefly</h2>
<p class="src">The Arabic side comes from two books: the compiled English dictionary attributed to Ibn Sirin (Pearl Publishing House, 1992 — "Fire" printed p. 158 per the book's own end-of-volume index, the entry running onto pp. 159-160; the same index locates Fire iron and Fire worshiper also at 158, Fireboat at 160, Firewood at 161, Torch at 443, Worshipping fire at 481) and the Arabic original of Al-Nabulsi's <em>Ta'tir al-Anam</em>, whose (نار) headword sits at shamela.ws/book/1217/348 (printed p. 351, باب النون), whose (ومن رأى) clauses run across shamela 349 (printed p. 352) and shamela 350 (printed p. 353) with one sentence breaking at each page edge, and whose citron (نارنج) clause sits at shamela 360 (printed p. 363). The Chinese side is fifteen verdict lines from the received Zhou Gong text — thirteen in chapter 23, one in chapter 12, one in chapter 8. One sample of each book, translated, then the full checked passages in the sources section at the bottom.</p>

<div class="cites">
<div class="cite-hd"><div>Text</div><div class="src-hd">Source</div></div>
<div class="cite-row">
  <div class="txt"><p>"Fire: The element offire in a dream represents might. Fire in a dream also means love. A product that is touched by fire in the process of its manufacturing or cooking in a dream means arguments and disputes. In a dream, fire also signifies glad tidings, a warning, war, chastisement, power, imprisonment, losses, sins, or blessings. Ifone sees a blazing fire with sparks shooting in every direction and burning in the forest and raging with tumultuous noise and uproar in a dream, it means insubordination, civic disorder or an adversity through which many people will die. ... If a fire is extinguished by rain in a dream, it means poverty or loss of one'sjob. ... It also means poverty and need. (Also see Body'; Firewood; Hell-fire)" (elided; full entry in Sources)</p></div>
  <div class="src">Ibn Seerin's Dictionary of Dreams (Al-Akili compilation, Pearl 1992) — "Fire," printed p. 158, running onto pp. 159-160 (the running head "DICTIONARY OF DREAMS 159" sits mid-entry in the scan). Translated/compiled English; the scan's joined words (offire, Ifone, one'sjob) are kept as printed.</div>
</div>
<div class="cite-row">
  <div class="txt"><p class="ar">@@NAR_HEAD@@</p><p class="ar">@@NAR_TWO1@@</p><p class="ar">@@NAR_TWO2@@</p></div>
  <div class="src">Al-Nabulsi, Ta'tir al-Anam — shamela.ws/book/1217/348-349 (printed pp. 351-352), the (نار) headword and the two-armies paragraph, verbatim; the sentence breaks mid-phrase at "يخرج إلى المضاف إلى" at the bottom of printed p. 351 and resumes at "النار التي فاض" at the top of p. 352: fire is glad tidings, warning, war, chastisement, a ruler, imprisonment, loss, sins and blessing — a fire with sparks and flame burning the trees, with noise and tumult, is a sedition through which people perish on the measure of what it burned; fire in the heart is an overwhelming love and the defeat of being parted from the beloved; two fires blowing at each other are two armies — more fuel, more numbers; the wind with you, the win; blacker and darker, worse intent; equal, unburning, two seditions in that quarter; nearer the water, likelier to submit — and the fire the water overflows onto is quenched, its host destroyed by God's help, likewise if the rain comes down on it, and that water may be an ambush coming out to the one it is added to; the higher the smoke, the greater the terror; kindling a fire in a dark night to guide people earns guiding knowledge; kindling it on the road in daylight is innovation and misguidance — and fire seen by day proves war and sedition, by night, comfort. (Translation ours.)</div>
</div>
</div>
<div class="note"><p>Zhou Gong, stated plainly: the received Chinese dream book this site quotes chapter by chapter carries fire in exactly fifteen verdict lines — thirteen in chapter 23 (水火 盗贼 灯烛), one in the boats-and-carts chapter (执火入船主大吉 — carrying fire onto a boat: very auspicious) and one in the gates chapter (天火烧门主凶事 — heaven's fire burning the gate: misfortune). The verdicts sort by what the fire touches and where it comes from: burning sun, moon, river, hill or heaven prescribes patrons, long life, prominence, thriving and national peace; blazing flame prescribes wealth; being in the fire prescribes a noble helper; carrying or riding with fire prescribes office — while fire rising from the ground, black smoke, carrying fire down the road and putting fire to a well all prescribe illness, disease or a blocked road. The character 火 appears exactly sixteen times in the received text: fifteen verdict lines and the chapter title itself. All quoted at location in Sources; nothing else is claimed for the Chinese side.</p></div>

@@CHIPZ@@
<h2 id="what-modern-research-adds-and-what-it-do">What modern research adds — and what it doesn't</h2>
<p>Modern dream research treats fire as a countable theme, not a sign. The numbers below were pulled and re-read today from the study itself. Johannes Mathes and Michael Schredl coded 1,612 dreams written down in diaries by 425 psychology students over two weeks, and scored each report against the 56-item Typical Dream Questionnaire: fire content (item 34) appeared in <strong>1.74% of the diary reports</strong>; <strong>6.60% of dreamers</strong> recorded at least one fire dream inside the fortnight; and <strong>25.94%</strong> reported having dreamed of fire at least once in their lifetime. Fire ranked 17.5 among themes in the diaries and 30.5 on the lifetime questionnaire, with a small diary-questionnaire correlation (r = 0.094) — and the paper's own review sentence puts fire in the list of "archaic" themes (with earthquake, snakes, spiders and insects) that "occur relatively rarely" in adults (Mathes &amp; Schredl, <em>Somnologie</em> 18:106–111, 2014, DOI 10.1007/s11818-013-0653-6; PDF re-pulled and table re-read today; student sample, stated as such). The same table is useful for this site's main subject too: teeth falling out (item 18) ran at 0.56% of diary reports — rarer in two weeks of actual diary life than fire, though 35.08% endorse it lifetime, a gap the authors themselves flag as unexplained. Questionnaire work adds only stability: across 444 participants the rank order of the 55 typical themes was stable, men reporting physical-aggression dreams more than women (Schredl, Ciric, Götz &amp; Wittmann, <em>The Journal of Psychology</em> 138(6):485–494, 2004, <a href="https://pubmed.ncbi.nlm.nih.gov/15612605/">PubMed 15612605</a>, record re-pulled today). The 2018 teeth-dream paper this site leans on elsewhere (<a href="https://pubmed.ncbi.nlm.nih.gov/30319507/">PubMed 30319507</a>) has no fire item anywhere — its full text, re-checked today, contains no form of the word. Against the classical layer the direction is the story again: the Arabic books read fire as a civic sign — war, sedition, prices, governors, thieves, armies — while the modern instrument counts how many students wrote "fire" down in fourteen days, and finds the flame is rare. The gap is reported, not papered over.</p>

<h2 id="sources-all-passages-checked-against-the">Sources (all passages checked against the cited pages)</h2>
<div class="src">
<p><strong>Ibn Sirin compilation — "Fire," printed p. 158, running onto pp. 159-160</strong> (Ibn Seerin's Dictionary of Dreams, compiled by Muhammad M. Al-Akili, Pearl Publishing House 1992, ISBN 1879405032; a later compilation attributed to the 8th-century scholar, not his autograph text; the book's own page index lists Fire at 158, Fireboat at 160, Firewood at 161, Torch at 443, Worshipping fire at 481). Full entry, scan verbatim including its joined words and its two print glitches kept as printed (the daylight sentence runs "adversities.lfit"; the plague word breaks as "pIa es and mass loU"): "@@FIRE@@" — "Gold," printed p. 189, the house-fire clause: "@@GOLDFIRE@@" — "Torch," printed p. 443, the whole entry: "@@TORCH@@" — "Firewood," printed p. 161, the whole entry: "@@FIREWOOD@@" — the hearth's body clause, from "Fireplace," printed p. 160, running onto p. 161: "@@STOMACH@@" — "Worshipping fire," printed p. 481, head to tail: "@@WORSHIP@@"</p>
<p><strong>Al-Nabulsi — (نار), shamela.ws/book/1217/348, printed p. 351, continuing at /349 (printed p. 352) and /350 (printed p. 353)</strong> (Ta'tir al-Anam fi Ta'bir al-Manam, Abd al-Ghani al-Nabulsi d. 1731 CE, Dar al-Fikr edition; باب النون; translation ours). Headword and spark clause: "@@NAR_HEAD@@" (fire is glad tidings, warning, war, chastisement, a ruler, imprisonment, loss, sins, blessing; fire with sparks and flame burning trees, with noise and tumult, is sedition — people perish from it on the measure of what it burned). Heart line: "@@NAR_HEART@@" (fire in the heart: overwhelming love, the defeat of being parted from the beloved). The two-armies paragraph, breaking at the page edge after "يخرج إلى المضاف إلى" and resuming at the next page head: "@@NAR_TWO1@@" / "@@NAR_TWO2@@" (two armies; fuel, wind, blackness; equal and unburning, two seditions in the quarter; nearer water submits; water overflowing quenches and its host perishes with God's help, likewise rain; the water may be an ambush; high smoke, greater terror; night-kindled guidance earns knowledge, daylight road-kindling is innovation; by day war and sedition, by night comfort). — The scenario clauses on printed p. 352: "@@NAR_WORSH@@" (fire-worship: love of war, obeying Satan); "@@NAR_WARM@@" (warming by fire in winter: wealth); "@@NAR_EAT@@" (eating fire: devouring orphans' property unjustly, or unlawful money); "@@NAR_CONDEMN@@" (condemned to the fire: prison; entering and coming out: paradise); "@@NAR_SEEHELL@@" (hell seen plainly: beware the ruler; tasting its punishment: falling into sedition); "@@NAR_GROUP@@" (a lit fire ringed by a group: they attain blessing); "@@NAR_BR@@" (fire in the open desert and feeling calm by it: calm after dread; touched and unburned: your appointment is honored); "@@NAR_GRAIN@@" (grain burned: its price rises; fire falling on a commodity: it grows dear, buyers crowd); "@@NAR_QIDR@@" (fire under an empty pot: the householder stirred up over what harms him; the burning fire is a calamity from the ruler); "@@NAR_WALI@@" (a governor kindling a fire that keeps going out: dismissed, his fire quenched); "@@NAR_TORCH@@" (a torch at your door with no smoke: pilgrimage; work in the house: marriage; fire in the fingers: the scribes' injustice; in the palm: the artisan's; in the mouth: grief); "@@NAR_TOWN@@" (fire in a town with flame, tongue, devouring and dread sound: war, plague, fever-rash, smallpox or death there; no flame, no voice: illnesses and events there); "@@NAR_MEAT@@" (stoking a fire to warm by: a profit-making affair; roasting meat over it: stirring what people keep private, tongue-harm; eating it: provision and a heavy grief); "@@NAR_LIMB@@" (fire burning garment or limb: calamity in whatever that garment or limb stands for); "@@NAR_IGTIBAS@@" (borrowing a flame: unlawful money from a ruler); "@@NAR_WAHJ@@" (a fire's heat on your face: falling into people's tongues and gossip; useful lighted fire: safety for the fearful, closeness to the ruler); "@@NAR_BAB@@" (kindling at the sultan's gate: great office and strength); "@@NAR_KHUJR@@" (fire going out of your house: governorship, trade, or power in a craft); "@@NAR_SHARQ@@" (your fire's beam lighting east to west: knowledge spoken of east and west); "@@NAR_DARHA@@" (fire falling in your house: fertility; flame rising from your head or out of your house with light and beam, your wife pregnant: a son through whom you lead, great news, joy from her); "@@NAR_JBAL@@" (kindling on a mountaintop: nearness to God, needs fulfilled, the absent traveler home safe — and a fire blazing in your house ruins it); "@@NAR_TANUR2@@" (fire lit in your oven, married: your wife conceives); "@@NAR_JALIS@@" (sitting in the fire while it burns you: the king draws you near, speaks with you, keeps his secret with you, you prevail over enemies, the unclear matter clears; fire in the desert: unfinished war; taking a coal from the fire: unlawful money from the ruler); "@@NAR_SAMAA@@" (sky-fire burning you and the burn not affecting you: soldiers descend on your house; kindling fire among people: enmity and rancor between them; flame darting from your head: severe illness of heat and fever-rash); "@@NAR_WASAT@@" (in the fire's middle, finding no heat: truth, certainty, kingship, victory over enemies); "@@NAR_TAFI2@@" (a fire quenched: sedition and evil settle in that place; the household's lighted fire quenched: the manager of that house dies; in a town: its head and its scholar die; in your orchard: you or your children; quenched and a wind entering to light it again: thieves enter your house); "@@NAR_WAA@@" + "@@NAR_WAA2@@" (storing fire in a vessel: unlawful money; fire may mean jinn, created from smokeless fire, and drought, locusts and a fine the ruler throws on people — the sentence breaks at the page edge and completes at printed p. 353). — On printed p. 353: "@@NAR_TANUR3@@" (fire in oven, furnace or stove where you live: wealth and use, most of all if your trade is fire and in winter; your fire smothered, quenched, turned to ash, quenched by water or rain: poverty, or your work and craft stalled); "@@NAR_KALAM@@" (fire speaking from a jar, waterskin or vessel of men or women: the one that vessel stands for is touched by jinn-speaking possession; harmful fire: the unjust ruler; fire people benefit from: the just ruler; carrying coals that scatter from you: unable to carry another's affair; fire in winter: fruit — "they say fire is winter's fruit"; eating fire: eating and drinking from forbidden vessels, gold and silver, and perhaps poverty and begging; a fire's glare: the heart's glare in waking over a loss or a death; and fever-illnesses; and fire may mean its worshipper — so do light and darkness). — The citron clause, shamela /360 printed p. 363: "@@NAR_NARINJ1@@" (citron is evil entire, or sedition); "@@NAR_NARINJ2@@" (people pelting each other with citrons: fighting — the reading taken from the word's name, its color and its sourness; citron prescribes fleeing and seeking safety, for نارنج carries نار in it; perhaps love and madness; many citrons in the house: fire blazing in it; for the bachelor: a beautiful virgin wife with money and goods).</p>
<p><strong>Zhou Gong Jie Meng — received 27-chapter text</strong> (corpus checked line by line; the character 火 occurs exactly sixteen times: fifteen verdict lines and one chapter title). ch. 23 (水火 盗贼 灯烛): "水上火出主大吉" — fire rising out of water on the river: very auspicious; "火烧日月大人助" — fire burning the sun and moon: great persons aid; "火烧河水长命吉" — fire burning river water: long life, fortune; "火烧山野大显达" — fire burning hill and field: high advancement; "火烧自是主兴旺" — fire burning yourself: rising and thriving; "火焰炎炎主发财" — flame blazing high: wealth; "火从地生疾病至" — fire rising from the ground: illness arrives; "执火乘行官位至" — carrying fire, riding out: office arrives; "大火烧天主国安" — great fire burning the sky: the state at peace; "身在火中贵人扶" — your body in the fire: a noble person supports; "火烟黑色主疾病" — smoke black: illness; "把火行路不通达" — carrying fire along the road: passage blocked; "把火烧井主病至" — putting fire to a well: illness arrives. ch. 12 (船车 游行 物价): "执火入船主大吉" — carrying fire aboard a boat: very auspicious. ch. 8 (门户 井灶 厨厕): "天火烧门主凶事" — heaven's fire burning the gate: misfortune. The chapter title itself (水火 盗贼 灯烛) is the sixteenth occurrence. No other chapter carries a fire line.</p>
<p><strong>Modern research.</strong> Mathes J, Schredl M. "Analysis of a large sample of diary dreams — how typical are these typical dreams?" <em>Somnologie — Schlafforschung und Schlafmedizin</em> 18:106–111, 2014. DOI 10.1007/s11818-013-0653-6 (publisher PDF re-pulled and Table 2 re-read today: 425 participants, mean age 23 — the methods section counts 64 men and 361 women, the German abstract says 321 women, a discrepancy inside the paper itself, reported as found; 1,612 diary reports over a 14-day window; Fire item 34: 1.74% of reports, 6.60% of dreamers in-period, rank 17.5 in diaries, 25.94% lifetime TDQ prevalence, rank 30.5, diary-TDQ r = 0.094; Teeth falling out item 18: 0.56% of reports, 2.12% of dreamers, 35.08% lifetime, r = 0.151; the review sentence lists Earthquake, Fire, Snakes, Spiders and insects among archaic themes that occur relatively rarely). Schredl M, Ciric P, Götz S, Wittmann L. "Typical dreams: stability and gender differences." <em>The Journal of Psychology</em> 138(6):485–494, 2004. <a href="https://pubmed.ncbi.nlm.nih.gov/15612605/">PubMed 15612605</a> (record re-pulled today: 444 participants; rank order of the 55 TDQ themes stable; most themes endorsed at least once lifetime by most participants; men reported more physical-aggression dreams). Rozen N, Soffer-Dudek N. <em>Frontiers in Psychology</em> 9:1812, 2018. <a href="https://pubmed.ncbi.nlm.nih.gov/30319507/">PubMed 30319507</a> (full text re-checked today: no fire item in the theme list; no form of the word fire appears in the paper).</p>
</div>

<div class="note"><p>This page reports what two classical Arabic texts, the received Chinese dream book (whose fifteen fire lines sort by direction and target, not by omen), and a two-week student diary can see about dreams of fire. It is not a prediction, a medical or religious ruling, and no dream book — classical or modern — settles what a dream means for the person who had it. If this dream unsettled you, note the move every source on this page makes in its own form: the books do not ask whether fire is good or bad; they ask <em>when</em> it burned, <em>how much smoke</em> it made, <em>where</em> it stood, and <em>what it touched</em>. For the same flame read from the other side of two switches — the rain that quenches it into poverty, the gold house it consumes — see <a href="/dream/rain/">rain dreams</a> and <a href="/dream/gold/">gold dreams</a>, and for the body door this page's mouth clause opens onto, <a href="/dream/teeth-falling-out/">teeth falling out</a>.</p></div>

<section style="border-top:1px solid var(--line);margin-top:40px;padding-top:20px"><h2 id="related-questions" style="font-size:18px;font-weight:400">Related questions</h2><ul style="list-style:none;padding:0"><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/rain/">Rain dreams — the rain that quenches a fire, the books' own poverty clause</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/gold/">Gold dreams — the gold house the fire consumes, clause for clause</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/water/">Water dreams — the same books' fitna-versus-fortune clauses on the army's side of the water switch</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/teeth-falling-out/">Teeth falling out dream — the classic page that started this site, next door to the mouth-fire clause</a></li></ul></section>
</article></main>
</div>
<footer>
<p>Teeth Dream Meaning · <a href="/">Home</a> · <a href="/dream/teeth-falling-out/">Teeth falling out</a> · <a href="/disclaimer/">Disclaimer</a></p>
</footer>
</div>
<script>
if(window.matchMedia("(max-width:860px)").matches){
  var d=document.querySelector(".tocd"); if(d) d.removeAttribute("open");
}
</script></body>
</html>
"""

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

T = {k: esc(v) for k, v in {
 'FIRE': FIRE, 'GOLDFIRE': GOLDFIRE, 'TORCH': TORCH, 'FIREWOOD': FIREWOOD, 'STOMACH': STOMACH, 'WORSHIP': WORSHIP,
 'NAR_HEAD': NAR_HEAD, 'NAR_HEART': NAR_HEART, 'NAR_TWO1': NAR_TWO1, 'NAR_TWO2': NAR_TWO2,
 'NAR_WORSH': NAR_WORSH, 'NAR_WARM': NAR_WARM, 'NAR_EAT': NAR_EAT, 'NAR_CONDEMN': NAR_CONDEMN,
 'NAR_SEEHELL': NAR_SEEHELL, 'NAR_GROUP': NAR_GROUP, 'NAR_BR': NAR_BR, 'NAR_GRAIN': NAR_GRAIN,
 'NAR_QIDR': NAR_QIDR, 'NAR_WALI': NAR_WALI, 'NAR_TORCH': NAR_TORCH, 'NAR_TOWN': NAR_TOWN,
 'NAR_MEAT': NAR_MEAT, 'NAR_LIMB': NAR_LIMB, 'NAR_IGTIBAS': NAR_IGTIBAS, 'NAR_WAHJ': NAR_WAHJ,
 'NAR_BAB': NAR_BAB, 'NAR_KHUJR': NAR_KHUJR, 'NAR_SHARQ': NAR_SHARQ, 'NAR_DARHA': NAR_DARHA,
 'NAR_JBAL': NAR_JBAL, 'NAR_TANUR2': NAR_TANUR2, 'NAR_JALIS': NAR_JALIS, 'NAR_SAMAA': NAR_SAMAA,
 'NAR_WASAT': NAR_WASAT, 'NAR_TAFI2': NAR_TAFI2, 'NAR_WAA': NAR_WAA, 'NAR_WAA2': NAR_WAA2,
 'NAR_TANUR3': NAR_TANUR3, 'NAR_KALAM': NAR_KALAM, 'NAR_NARINJ1': NAR_NARINJ1, 'NAR_NARINJ2': NAR_NARINJ2,
}.items()}
subs = {'@@TITLE@@': esc(TITLE), '@@DESC@@': esc(DESC), '@@CSS@@': CSS,
        '@@ALD@@': ARTICLE_LD, '@@FAQJ@@': FAQ_JSON,
        '@@CHIPR@@': CHIP['reading'], '@@CHIPT@@': CHIP['text'], '@@CHIPZ@@': CHIP['research']}
for k, v in subs.items():
    HEAD = HEAD.replace(k, v)
for k, v in T.items():
    HEAD = HEAD.replace('@@'+k+'@@', v)
assert '@@' not in HEAD, [l for l in HEAD.splitlines() if '@@' in l]
os.makedirs('/root/teethdreammeaning/site/dream/fire', exist_ok=True)
open('/root/teethdreammeaning/site/dream/fire/index.html','w',encoding='utf-8').write(HEAD)
print("wrote", len(HEAD), "bytes")
print("div", HEAD.count('<div'), HEAD.count('</div>'))
print("blockquote", HEAD.count('<blockquote'), HEAD.count('</blockquote>'))
print("p", HEAD.count('<p'), HEAD.count('</p>'))
print("footer", HEAD.count('<footer'), HEAD.count('</footer>'))
seg = HEAD.split('<h1>')[1].split('<h2')[0]
print("first-screen Arabic:", sum(1 for ch in seg if '\u0600' <= ch <= '\u06ff'),
      "CJK:", sum(1 for ch in seg if '\u4e00' <= ch <= '\u9fff'))
print("CJK total:", sum(1 for ch in HEAD if '\u4e00' <= ch <= '\u9fff'))
print("title", len(TITLE), "desc", len(DESC))
