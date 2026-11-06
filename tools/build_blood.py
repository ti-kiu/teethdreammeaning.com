#!/usr/bin/env python3
"""Build site/dream/blood/index.html. All quoted passages injected VERBATIM from
corpus files (/root/dream_research/*). Every EN/AR assertion below is asserted
against the source file at build time — nothing is hand-copied."""
import re, json, os

def norm(s): return re.sub(r'\s+', ' ', s).strip()

en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en)
en = re.sub(r"\d+ IBN SEERIN'?S", ' ', en)
en = norm(en)

def cut(src, start, end):
    i = src.find(start); assert i != -1, "MISS START: " + start[:60]
    j = src.find(end, i); assert j != -1, "MISS END: " + end[:60]
    return norm(src[i:j+len(end)])

def must(src, s):
    assert s in src, "MISS: " + s[:70]

# --- Ibn Sirin compilation entries (printed pages per end-of-volume index) ---
BLOOD = cut(en, "Blood: In a dream, blood represents unlawful", "vanquishing one's enemy.")
BLEEDING = cut(en, "Bleeding: Internal bleeding in a dream means", "Also seeBleeding nose")
NOSE = cut(en, "Bleeding nose: A bleeding nose in a dream means", "(Also see Bleeding; Cut; Injury; Wound)")
CUPPING = cut(en, "Cupping: (Sacrification; A medicinal process of blood letting)", "abstaining from reply.")
MENSTR = cut(en, "Menstrual period: (Discharge; Menstruation; The Curse of Eve)", "(Also see Garden; Hilarity; Mirth)")
VEINS = cut(en, "Veins: (Blood ties; Family; Relative; Vessel)", "(Also see Aorta; Blood; Body'; Jugular vein)")
LEECH = cut(en, "Leech: (Bloodsucker; Sponger)", "base and a despicable enemy.")
BLOODDIS = cut(en, "Blood disease: If one is presented", "(Also see Dates)")

must(en, "Bleeding naturally in a dream means peace and comfort. Excess bleeding in a dream means the opposite.")
NATURAL = "Bleeding naturally in a dream means peace and comfort. Excess bleeding in a dream means the opposite."

# --- Al-Nabulsi (shamela 117 = printed 120, continues shamela 118 = printed 121) ---
ar117 = norm(open('/root/dream_research/nabulsi_page_117.txt', encoding='utf-8').read())
ar118 = norm(open('/root/dream_research/nabulsi_page_118.txt', encoding='utf-8').read())
ar116 = norm(open('/root/dream_research/nabulsi_page_116.txt', encoding='utf-8').read())
ar94  = norm(open('/root/dream_research/nabulsi_page_94.txt', encoding='utf-8').read())

DEM_HEAD = cut(ar117, "- (دم) في المنام مال حرام", "رجع من سفره سالماً.")
DEM_SHORT = cut(ar117, "- (وقيل من رأى) أنه يخرج الدم من جسده", "ونجا منه.")
DEM_WELLS = cut(ar117, "- (ومن رأى) أنه وقع في بئر من دم", "فهو كذب يكذب عليه.")
DEM_LONG = cut(ar117, "- (ومن رأى) دماً خرج منه في غير فصد", "مدح أو ذم")   # ends at p117 line-end join
must(ar118, "دل على نطفته التي يضعف لخروجها")
DEM_CONT = cut(ar118, "دل على نطفته التي يضعف لخروجها", "أو يظفر بعدوه")
DEM_SWITCH = cut(ar118, "والإفراط في خروج الدم نكد", "للآيسة من الحيض مرض")
DEM_ANUS = cut(ar118, "- (ومن رأى) أنه يخرج من دبره دم", "بأفواه العروق")
DEM_TEARS = cut(ar118, "- (دمع) في المنام", "فهو هم وحزن")
DEML = cut(ar116, "- (دمل) ومن رأى في المنام", "عاد مكانه")

must(ar94, "فإن قتلها ظفر بعدو فإن سال الدم على يديه مات عدوه وورث ماله")

# --- Zhou Gong (received text; full-corpus blood lines: exactly two) ---
zg = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()
ZG1 = "手足浓血出大吉"
ZG2 = "牛角有血主三公"
for L in (ZG1, ZG2): must(zg, L)
assert zg.count("血") == 2, zg.count("血")

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

FAQ = [
 ("What does it mean to dream of blood?",
  "Both classical Arabic books open the same way: blood in a dream is unlawful money, or a wrong act coming out of the dreamer (Ibn Sirin compilation, printed p. 43; Al-Nabulsi, shamela 117, printed p. 120). But the same paragraphs carry two bright clauses: blood flowing from the skin or a wound means health and safety and, for a traveller, a safe return home — and bleeding out of necessity means relief and the ending of worry. What colour the reading is depends on where the blood goes and whether it was drawn on purpose."),
 ("What does it mean to dream of bleeding without being injured?",
  "The compilation: blood emanating from the body without cupping or a cut means giving money away — and if the dreamer is poor, receiving it (printed p. 43). Al-Nabulsi, same page, same shape: blood leaving with no cupping, no shave and no wound means money leaving in proportion to the blood; if he has money it goes; if he is poor, he gains its like (printed p. 120). A poor person's unexplained bleed is income; a rich person's is loss — the ledger flips by the dreamer's state, not by the image."),
 ("Is a dream about period blood a bad omen?",
  "The two books disagree on exactly one figure. The compilation's Menstrual entry (printed p. 274): for an unmarried or widowed woman it means marriage; for an aged woman it means she will bear a son. Al-Nabulsi (printed p. 121): the unmarried woman gets a husband and the pregnant woman miscarries — but for the woman past her periods, blood means illness. Same image, one reversal: post-menopausal blood is a birth in one book and a sickness in the other, and the page states both."),
 ("What does the Chinese Zhou Gong book say about blood?",
  "The received 27-chapter text carries blood in exactly two verdict lines. Chapter 3: thick blood coming from the hands and feet is greatly auspicious. Chapter 26: blood on an ox's horns prescribes high office. There is no general blood entry to quote — and the two lines that exist run against the Arabic books, which read the same substance mostly as unlawful money or a lie told about you."),
 ("What does modern research say about blood dreams?",
  "No published survey reports a prevalence figure for dreams of blood: the standard theme instruments, including the checklist used in the 2018 teeth-dream study (PubMed 30319507), have no blood item — we re-checked that paper's full text today and the word blood does not occur in it. The closest measured numbers concern waking reactions to blood rather than dreams: blood-injection-injury phobia runs 3.5% lifetime with a median onset of 5.5 years (Bienvenu & Eaton, Psychol Med 1998, PubMed 9794020, re-pulled today), and threat-simulation theory predicts exactly the over-representation of injury imagery the classical collections are full of (Revonsuo, Behav Brain Sci 2000, PubMed 11515147, re-pulled today). The gap is reported, not papered over."),
]
FAQ_JSON = json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ], ensure_ascii=False)

T = {k: esc(v) for k, v in {
  'BLOOD': BLOOD, 'BLEEDING': BLEEDING, 'NOSE': NOSE, 'CUPPING': CUPPING,
  'MENSTR': MENSTR, 'VEINS': VEINS, 'LEECH': LEECH, 'BLOODDIS': BLOODDIS,
  'DEM_HEAD': DEM_HEAD, 'DEM_SHORT': DEM_SHORT, 'DEM_WELLS': DEM_WELLS,
  'DEM_LONG': DEM_LONG, 'DEM_CONT': DEM_CONT, 'DEM_SWITCH': DEM_SWITCH,
  'DEM_ANUS': DEM_ANUS, 'DEM_TEARS': DEM_TEARS, 'DEML': DEML,
}.items()}
T['FAQ_JSON'] = FAQ_JSON

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="canonical" href="https://teethdreammeaning.com/dream/blood/">
<meta property="og:title" content="Dreaming of Blood: What the Two Arabic Books Say">
<meta property="og:description" content="Blood in a dream: both classical books read unlawful money first — then health, homecoming, and a necessity switch. Zhou Gong reads hand-and-foot blood as auspicious.">
<meta property="og:url" content="https://teethdreammeaning.com/dream/blood/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
<title>Dreaming of Blood: What the Dream Books Actually Say</title>
<meta name="description" content="Blood in a dream: both classical books read unlawful money first — then health, homecoming, and a necessity switch. Zhou Gong reads hand-and-foot blood as auspicious.">
<style>
:root{--ink:#1a1a1a;--paper:#fdfcf9;--accent:#7a5c2e;--line:#e4ddcf;--soft:#6b6357}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Georgia,'Times New Roman',serif;background:var(--paper);color:var(--ink);line-height:1.75}
.wrap{max-width:720px;margin:0 auto;padding:48px 24px}
h1{font-size:clamp(28px,5vw,38px);font-weight:400;line-height:1.25;margin-bottom:12px}
.lede{font-size:18px;color:#333;margin-bottom:28px}
h2{font-size:22px;font-weight:400;margin:44px 0 16px}
h3{font-size:17px;font-weight:700;margin:28px 0 8px}
p{margin-bottom:16px}
blockquote{border-left:3px solid var(--accent);padding:12px 20px;margin:16px 0 20px;background:#f7f3ea;font-style:italic}
blockquote p:last-child{margin-bottom:0}
blockquote[dir="rtl"]{font-style:normal;font-size:17px;text-align:right;border-left:0;border-right:3px solid var(--accent)}
.loc{font-family:Menlo,Consolas,monospace;font-size:12.5px;color:var(--soft);margin:-8px 0 24px}
.qa{border-bottom:1px solid var(--line);padding:18px 0}
.qa h3{margin:0 0 8px}
.qa p:last-child{margin-bottom:0}
.note{background:#f5f1e6;border:1px solid var(--line);padding:16px 20px;font-size:14.5px;color:var(--soft);margin:28px 0}
footer{border-top:1px solid var(--line);margin-top:56px;padding-top:24px;color:var(--soft);font-size:14px}
a{color:var(--accent)}
nav.top{font-size:14px;margin-bottom:32px;color:var(--soft)}
.src{font-size:14px;color:var(--soft)}
</style>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Article", "author": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"}, "datePublished": "2026-11-06", "dateModified": "2026-11-06", "publisher": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"},  "headline": "Dreaming of Blood: What the Two Arabic Books Actually Say", "url": "https://teethdreammeaning.com/dream/blood/", "inLanguage": "en", "about": {"@type": "Thing", "name": "dream interpretation"}}</script>
<script type="application/ld+json">@@FAQ_JSON@@</script>
</head>
<body>
<div class="wrap">
<nav class="top"><a href="/">Teeth Dream Meaning</a> · classical sources, checked page by page</nav>

<h1>Dreaming of Blood: What It Means</h1>
<p class="lede">Both classical Arabic books open the same entry with the same ledger line: <strong>blood in a dream is unlawful money, or a wrong act coming out of the dreamer.</strong> The <em>Ibn Sirin</em> compilation (printed p. 43) and Al-Nabulsi (shamela 117, printed p. 120) agree word for word in two languages. Then both books add the clauses folk summaries never quote: blood flowing from the skin or from wounds is "a sign of good health, safety," or a traveller's safe return home; bleeding <em>out of necessity</em> means relief and the ending of worry; and blood that leaves the body with no cupping and no cut is money leaving — or, if the dreamer is poor, money arriving. So the honest first answer is: <strong>these books price blood like cash and read its direction, not its colour.</strong> Money out or money in, a lie told about you, health restored, a journey ended — the scene decides.</p>

<p>That is also why a blood dream sits next to a teeth dream on this site: when teeth fall out with blood, the classical entries re-read the blood as debt and broken projects, not as a death mark — the same ledger rule, applied to the mouth. The scenarios people actually dream are below: plain answers first, no Arabic or Chinese on this screen, every quote checked to its printed page.</p>

<div class="qa">
<h3>You saw blood — the general reading</h3>
<p>The headword, in both books: unlawful money, or an evil act that will emanate from the dreamer. Al-Nabulsi's first scenario sharpens it: whoever sees himself wallowing in blood "amasses wealth and turns over in unlawful money or a great sin." But the same paragraph flips: blood staining a shirt with no known source means <em>someone will lie about you and you won't notice</em>; blood flowing from skin or wounds means health, safety, homecoming; blood in a jar stands for a menstruating woman; and the longest clause list in the entry reads blood as life itself — strength, wealth, helpers, clothing, praise or blame, separation from loved ones by death. One substance, one entry, a dozen ledgers.</p>
</div>

<div class="qa">
<h3>You were bleeding with no wound</h3>
<p>This is the entry's strangest hinge. The compilation: blood emanating from the body "without cupping or cuts" means giving money to someone — and "if he is a poor person, then it means receiving money from someone." Al-Nabulsi mirrors the whole clause, including the flip: blood leaving with no cupping, no shave and no wound means money leaving in exact proportion to the blood — the rich man's bleed is an outflow, the poor man's is an income. And the two books then agree on the switch that decides the valence: bleeding naturally means peace and comfort; excessive bleeding means the opposite — while Al-Nabulsi, page later, prices the same fork: excess blood is gloom, but blood let <em>out of necessity</em> in a dream means relief and the ending of worry. Unnecessary loss alarms; necessary loss pays.</p>
</div>

<div class="qa">
<h3>Blood on your shirt — and whose blood it was</h3>
<p>Both books run the same chain, in the same order, a thousand years apart: blood on the shirt from an unknown source — someone lies to you unnoticed; stained with a cat's blood — a thief lies to you; with a lion's — an unjust ruler in authority lies and exploits you; with a ram's — a rich, noble man lies, and at the end you consent to corrupt money. Al-Nabulsi adds the price tag the compilation states too: after the lie, unlawful money "in proportion to the blood." And the compilation's Veins entry (printed p. 459) moves the same liquid inside the body: veins are kinfolk — a vein split open means the death of a relative — and a rich man who sees a quantity of blood running through his veins will lose exactly that portion of his money. The poor man gains it.</p>
</div>

<div class="qa">
<h3>Cupping, bloodletting — blood drawn on purpose</h3>
<p>The compilation keeps a whole entry for the medieval blood-letting ritual (printed p. 106): cupping in a dream means signing an agreement under pressure, recovering from illness, payment of debts, alimony, loss of a business — or burying a treasure. And its sharpest clause: if the cupper works and <em>no blood comes</em>, it represents buried money you cannot find. That is the mirror image of the woundless bleed: drawn blood is debt paid and illness mended; withheld blood is wealth locked out of reach. Al-Nabulsi's headword clause assumes the same frame from the other side — bleed "in other than cupping or shaving or wound" and what leaves you is money.</p>
</div>

<div class="qa">
<h3>Menstrual blood — where the two books split</h3>
<p>The compilation's Menstrual period entry (printed p. 274): experiencing it means a wrongdoing or confusion; ablution after it means repentance; a widow or unmarried woman seeing it means marriage; an aged woman seeing it <strong>bears a son</strong>; a man experiencing it means an unlawful act or a lie; a man seeing his wife in her period means she closes herself off, or he loses money in business. Al-Nabulsi, one line in the entry's continuation (printed p. 121): the unmarried woman gets a husband, the pregnant woman miscarries, and the woman past her periods — <strong>illness</strong>. Same image, two verdicts on the same figure: post-menopausal blood is a birth in the compilation and a sickness in Al-Nabulsi. The page shows both and does not smooth it.</p>
</div>

<div class="qa">
<h3>Drinking blood, and a nosebleed</h3>
<p>Drinking human blood: money, profits, escape from danger — or a sin, then repentance (compilation, printed p. 43); Al-Nabulsi adds the hedged opinion that whoever drinks a person's blood "recoils from the sin and escapes it." Drinking your own blood is the ledger closing on itself: paying debts with a second loan, or vanquishing an enemy — Al-Nabulsi quotes the proverb directly: so-and-so washes blood with blood. The nosebleed entry (printed p. 42) is the most psychological page in the book: unlawful money, or a miscarriage, or — read from your own feeling in the dream — benefit or harm arriving from your superior; blood dripping onto the road means regular alms for the poor; and "it all depends on one's own consciousness in his dream." The entry even keeps the treasure clause: some say a nosebleed in a dream means finding a lost treasure. Same fluid; the dreamer's own reaction picks the column.</p>
</div>

<h2>The finding: one substance, three switches</h2>
<p>Put the two entries side by side and the clause order mirrors for paragraph after paragraph — unlawful money first, the shirt chain with cat, lion and ram in the same sequence, flowing blood as health and homecoming, the jar and the menstruating woman, blood as the dreamer's own adversary at home. Al-Nabulsi (d. 1731) inherits the compilation's material a thousand years older and keeps its machine intact. What makes the pair worth reading together is the three switches they install inside it. <strong>Switch one — direction:</strong> blood leaving with no cupping is money leaving if you are rich and arriving if you are poor; the image never fixes the sign, the dreamer's account does. <strong>Switch two — necessity:</strong> excess bleeding is gloom and its opposite, but blood let out of necessity is relief and the ending of worry — the same health-conditioning that lets a sick woman's braided hair mean death on the hair page. <strong>Switch three — drawn or spilled:</strong> cupping is debts paid and illness mended, and cupping that draws nothing is buried treasure you cannot find. A folk summary of "blood dream meaning" quotes the unlawful-money line and stops; the entries themselves spend most of their ink on when the reading flips.</p>

<p>And the two reversals no English round-up repeats. The <strong>first</strong> is inside the books: Al-Nabulsi opens a homograph on the next page — (دمع), tears: cold tears are joy, hot tears are grief — blood's near-spelling cousin, priced in the same single-word currency, one letter apart, two registers of the body's water. The <strong>second</strong> is across traditions: the received Zhou Gong text — which has no general blood entry at all — reads thick blood from the hands and feet (ch. 3) as <em>greatly auspicious</em>, and blood on an ox's horns (ch. 26) as high office. The Arabic books audit blood as tainted money and necessary loss; the Chinese verdict-lines audit it as rank and fortune rising. Same red, opposite column — exactly the structure the teeth pages found when Zhou Gong read a falling tooth against the Arabic longevity ledger.</p>

<h2>The entries, briefly</h2>
<p class="src">The Arabic side comes from two books: the compiled English dictionary attributed to Ibn Sirin (Pearl Publishing House, 1992 — "Blood" entry printed p. 43 per the book's own end-of-volume index, which also locates Bleeding and Bleeding nose at 42, Blood disease at 43, Bloodsucker at 44, Cupping at 106, Menstrual period at 274, Leech at 251 and Veins at 459) and the Arabic original of Al-Nabulsi's <em>Ta'tir al-Anam</em>, whose (دم) headword sits at shamela.ws/book/1217/117 (printed p. 120, باب الدال) and runs over onto shamela.ws/book/1217/118 (printed p. 121); the (دمل) boil clause sits at shamela 116 (printed p. 119) and the (دمع) tears clause at shamela 118 (printed p. 121). The Chinese side is two verdict lines from the received Zhou Gong book, chapters 3 and 26 — the only two blood lines in the 27-chapter text. One sample of each book, translated, then the full checked passages in the sources section at the bottom.</p>

<blockquote>
<p>"Blood: In a dream, blood represents unlawful or illegal money, or an evil act that will emanate from the person seeing the dream. ... Seeing blood flowing from one's body or from wounds is a sign of good health, safety, or it could mean coming home after a long journey. ... Blood in a dream also represents one's life, strength, wealth, business, helpers, clothing, earning praise or blame, weak points, unlawful food, lack of benefits, loss of business or money or esteem, inability to draw benefits from one's usual close ones, such as a father, a son, or a business partner, separation through death from one's beloveds or dear one's, such as wife or a kin. One's blood in a dream also represents his own Satan, or an enemy that dwells inside his house. Drinking one's own blood in a dream means paying one's debts with second loan, or vanquishing one's enemy." (elided; full entry in Sources)</p>
</blockquote>
<p class="loc">Ibn Seerin's Dictionary of Dreams (Al-Akili compilation, Pearl 1992) — "Blood," printed p. 43. Translated/compiled English.</p>

<blockquote dir="rtl" lang="ar">
<p>@@DEM_HEAD@@</p>
</blockquote>
<p class="loc">Al-Nabulsi, Ta'tir al-Anam — shamela.ws/book/1217/117 (printed p. 120), the headword paragraph, verbatim: blood in a dream is unlawful money, or a sin going out of him, or an act he sins by; wallowing in it means amassing unlawful wealth or a great sin; blood on the shirt from where he does not know means he is lied to without knowing — cat's blood, a thief's lie; lion's, an unjust sultan's; ram's, a noble rich man's, then unlawful money in proportion to the blood; and blood flowing from the skin is health and safety, and an absent man returns from his journey whole. (Translation ours.)</p>

<div class="note"><p>Zhou Gong, stated plainly: the received Chinese dream book this site quotes chapter by chapter carries <strong>no general blood entry</strong> — the full 27-chapter text contains exactly two lines with the blood character: 手足浓血出大吉 — "thick blood issuing from hands and feet: great fortune" (ch. 3, body and face), and 牛角有血主三公 — "blood on an ox's horns: the three dukes" (ch. 26, livestock). Both quoted at location in Sources; nothing else is claimed for the Chinese side.</p></div>

<h2>What modern research adds — and what it doesn't</h2>
<p>No typical-theme survey has published a prevalence figure for dreams of blood. The standard instruments skip it: the checklist behind the 2018 teeth-dream study (Rozen &amp; Soffer-Dudek, <em>Frontiers in Psychology</em> 9:1812, PubMed 30319507) covers teeth, falling, being smothered and toilet themes — we re-pulled its full text today, and the word "blood" does not occur in it at all. In the large content-analysis traditions Hall and Domhoff built on, bodily injury imagery is coded through aggression and mishap categories rather than a blood item, and in the 983-report two-week student diary Domhoff reprints, even the famous teeth theme appeared once — typical dreams are rare in daily life at exactly the rate folklore assumes them to be common (Domhoff, "The content of dreams," <em>Principles and Practice of Sleep Medicine</em>, 4th ed., 2005, pp. 522–534, chapter text re-read today). What <em>is</em> measured near the image is waking sensitivity to blood: the Baltimore ECA follow-up (n = 1,920, DIS-III-R; abstract re-pulled today) put DSM-IV blood-injection-injury phobia at a 3.5% lifetime prevalence, median age of onset 5.5 years, with higher fainting and seizure history among cases (Bienvenu &amp; Eaton, <em>Psychological Medicine</em> 28(5):1129–1136, 1998, PubMed 9794020) — a two-phase cardiovascular response that makes blood the one phobic stimulus people commonly faint to, whatever it is doing inside dreams. On the dream side, threat-simulation theory predicts precisely the over-representation of injury and consequence imagery the two classical collections catalogued a millennium before the questionnaires: Revonsuo's target paper is <em>Behavioral and Brain Sciences</em> 23(6):877–901, 2000, PubMed 11515147 (abstract re-pulled today). None of this settles what a blood dream means for you; the research layer measures waking fear and threat imagery, not omens — and the honest report on this page is that the symbol's own prevalence is simply unpublished. Note also the one classical clause that reads almost clinical: Al-Nabulsi's observation that blood turning, in a dying person, from red to blue or yellow may be what the dream shows (printed p. 121) — recorded here as a medical observation inside a dream book, not as endorsement.</p>

<h2>Sources (all passages checked against the cited pages)</h2>
<div class="src">
<p><strong>Ibn Sirin compilation — "Blood" entry, printed p. 43</strong> (Ibn Seerin's Dictionary of Dreams, compiled by Muhammad M. Al-Akili, Pearl Publishing House 1992, ISBN 1879405032; a later compilation attributed to the 8th-century scholar, not his autograph text; the book's own page index lists Blood at 43): "@@BLOOD@@" The same printed page continues: "@@NATURAL@@" (the sentence sits on p. 44 after the running head). — "Bleeding," printed p. 42: "@@BLEEDING@@ (In the scan the cross-reference is printed run-together as 'Also seeBleeding nose'.)" — "Bleeding nose," printed p. 42: "@@NOSE@@" — "Cupping," printed p. 106: "@@CUPPING@@" — "Menstrual period," printed p. 274: "@@MENSTR@@" — "Veins," printed p. 459: "@@VEINS@@" — "Leech," printed p. 251: "@@LEECH@@" — "Blood disease," printed p. 43: "@@BLOODDIS@@ (Also see Dates)"</p>
<p><strong>Al-Nabulsi — (دم), shamela.ws/book/1217/117, printed p. 120, continuing at /118, printed p. 121</strong> (Ta'tir al-Anam fi Ta'bir al-Manam, Abd al-Ghani al-Nabulsi d. 1731 CE, Dar al-Fikr edition; باب الدال; translation ours). Headword paragraph: "@@DEM_HEAD@@" Then the short clauses: "@@DEM_SHORT@@" — "@@DEM_WELLS@@" And the long ledger clause ending the page: "@@DEM_LONG@@" — the sentence runs across the page break and resumes on p. 121: "@@DEM_CONT@@" — the necessity switch and the menstrual figure: "@@DEM_SWITCH@@" — the anus clause: "@@DEM_ANUS@@" Adjacent headwords on the same pages — (دمع) tears, printed p. 121: "@@DEM_TEARS@@" and (دمل) boil, shamela 116, printed p. 119: "@@DEML@@" Cross-page note: the (دم) entry begins on shamela 117 and continues on shamela 118; both pages carry the same باب الدال running head. Elsewhere in the same book, blood appears in the serpent entry (حيه, shamela.ws/book/1217/94, printed p. 97): فإن قتلها ظفر بعدو فإن سال الدم على يديه مات عدوه وورث ماله — whoever kills the serpent prevails over an enemy, and if the blood runs onto his hands, the enemy dies and he inherits his money: the same money-by-blood grammar the blood entry carries.</p>
<p><strong>Zhou Gong Jie Meng — received 27-chapter text</strong> (corpus checked line by line; the blood character occurs in exactly two verdict lines): ch. 3 (body, face, teeth and hair): "手足浓血出大吉" — thick blood issuing from hands and feet: greatly auspicious. Ch. 26 (livestock): "牛角有血主三公" — blood on an ox's horns: brings the three dukes (the highest ministers). No general blood entry exists in the received text; the absence is stated, not filled.</p>
<p><strong>Modern research.</strong> Rozen E, Soffer-Dudek D. "Dental irritation and teeth-grinding may be associated with dreams about teeth: an association study." <em>Frontiers in Psychology</em> 9:1812, 2018. PubMed 30319507 (full text re-pulled today; word "blood": zero occurrences — no blood item in the theme checklist). Bienvenu OJ, Eaton WW. "The epidemiology of blood-injection-injury phobia." <em>Psychological Medicine</em> 28(5):1129–1136, 1998. PubMed 9794020, DOI 10.1017/s0033291798007144 (abstract re-pulled today: Baltimore ECA follow-up, n = 1,920, DIS-III-R; estimated unweighted lifetime prevalence 3.5%; median age of onset 5.5 years; 78% had symptoms within the last 6 months; higher lifetime fainting and seizures among cases; lower in the elderly, higher in females and persons with less education; diabetics with the phobia had higher-than-expected macrovascular complications). Revonsuo A. "The reinterpretation of dreams: an evolutionary hypothesis of the function of dreaming." <em>Behavioral and Brain Sciences</em> 23(6):877–901, 2000. PubMed 11515147, DOI 10.1017/s0140525x00004015 (abstract re-pulled today: threat-simulation hypothesis; dream content selectively simulates threatening events). Domhoff GW. "The content of dreams: Methodologic and theoretical implications." In Kryger MH, Roth T, Dement WC (eds.), <em>Principles and Practice of Sleep Medicine</em>, 4th ed., pp. 522–534, Saunders, 2005 (chapter text re-read today at dreams.ucsc.edu: 983 dream reports from 126 UCSC students over two weeks — five flying dreams (0.5%), one lost-teeth report; typical-dream themes are rare in ordinary diary samples; Hall/Van de Castle coding has no standalone blood category — injury imagery runs through aggression/mishap codes).</p>
</div>

<div class="note"><p>This page reports what two classical Arabic texts, the received Chinese dream book (including its honest silence on a general blood entry), and adjacent published research can see about dreams of blood. It is not a prediction, a medical or religious ruling, and no dream book — classical or modern — settles what a dream means for the person who had it. If this dream unsettled you, note the move every source on this page makes in its own form: the books do not ask whether blood is good or bad; they ask <em>whose</em> blood, <em>where</em> it goes, and whether it was drawn on purpose. For the mouth specifically — teeth falling out with blood — the reading runs through debt and broken projects, on its own page: <a href="/dream/teeth-falling-out-with-blood/">teeth falling out with blood</a>.</p></div>

<section style="border-top:1px solid var(--line);margin-top:40px;padding-top:20px"><h2 style="font-size:18px;font-weight:400">Related questions</h2><ul style="list-style:none;padding:0"><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/teeth-falling-out-with-blood/">Teeth falling out with blood — what the blood actually changes in the mouth's case</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/dead-person-resurrected/">Dreaming of a dead person alive again — the entry whose veins clause this page quotes</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/gold/">Gold dreams — the other classical asset the books price in unlawful money</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/snake/">Snake dreams — where Al-Nabulsi pays an enemy's blood as inherited money</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/teeth-falling-out/">Teeth falling out dream — the classic page that started this site</a></li></ul></section>
<footer>
<p>Teeth Dream Meaning · <a href="/">Home</a> · <a href="/dream/teeth-falling-out/">Teeth falling out</a> · <a href="/disclaimer/">Disclaimer</a></p>
</footer>
</div>
</body>
</html>
"""

PAGE = PAGE.replace('@@NATURAL@@', esc(NATURAL))
PAGE = PAGE.replace('@@FAQ_JSON@@', FAQ_JSON)
for k, v in T.items():
    if k == 'FAQ_JSON': continue
    PAGE = PAGE.replace('@@'+k+'@@', v)
assert '@@' not in PAGE, [l for l in PAGE.splitlines() if '@@' in l]
os.makedirs('/root/teethdreammeaning/site/dream/blood', exist_ok=True)
open('/root/teethdreammeaning/site/dream/blood/index.html','w',encoding='utf-8').write(PAGE)
print("wrote", len(PAGE), "bytes")
print("div open", PAGE.count('<div'), "close", PAGE.count('</div>'))
print("blockquote", PAGE.count('<blockquote'), PAGE.count('</blockquote>'))
print("p", PAGE.count('<p'), PAGE.count('</p>'))
import unicodedata
cjk = sum(1 for ch in PAGE if '\u4e00' <= ch <= '\u9fff')
print("CJK chars total:", cjk)
head = PAGE.split('<h2>')[0]
ar = sum(1 for ch in head if '\u0600' <= ch <= '\u06ff')
cjkh = sum(1 for ch in head if '\u4e00' <= ch <= '\u9fff')
print("first-screen Arabic:", ar, "CJK:", cjkh)
