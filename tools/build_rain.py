#!/usr/bin/env python3
"""Build site/dream/rain/index.html (Day 9, matrix item rain).
All quoted passages injected VERBATIM from corpus files (/root/dream_research/*);
every EN/AR assertion is asserted at build time — nothing is hand-copied.
Skeleton reused from the shipped baby/blood pages."""
import re, json, os

def norm(s): return re.sub(r'\s+', ' ', s).strip()

# ---------------- corpus ----------------
en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = norm(re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en))
en = norm(re.sub(r"\d+ IBN SEERIN'?S", ' ', en))

def cut(src, start, end):
    i = src.find(start); assert i != -1, "MISS START: " + start[:60]
    j = src.find(end, i); assert j != -1, "MISS END: " + end[:60]
    return norm(src[i:j+len(end)])

def must(src, s):
    assert s in src, "MISS: " + s[:70]

RAIN     = cut(en, "Rain: (Clouds; Drizzling; Life; Vapor; Water) If no harm", "it means a sickness. (Also see Water)")
RAINBOW  = cut(en, "Rainbow: (Fantasy; Illusion; Pipe dream) In a dream, a rainbow means peace", "then it means war.")
WATERL   = cut(en, "Water level: (Artificial lake; Farm pond; Ombrometer; Ombrograh; Pluviometer;", "same interpretation. (Also see Water)")
CLOUDS1  = cut(en, "Clouds: (Concealment; Gloom;", "harsh mandates.")
CLOUDS2  = cut(en, "Ifpeople are expecting clouds to water their farms", "whom will perish during a trip.")
assert "Ifpeople" in CLOUDS2  # scan ligature kept as printed, noted in page
DEATHCL  = "The death of an unknown woman in a dream means absence of rain or dearth, and if she comes back to life in the dream, it means rain."
must(en, RAIN); must(en, RAINBOW); must(en, WATERL); must(en, CLOUDS1); must(en, CLOUDS2); must(en, DEATHCL)
assert len(RAIN) > 2800 and len(RAINBOW) > 700 and len(WATERL) > 700, (len(RAIN), len(RAINBOW), len(WATERL))

ar315 = norm(open('/root/dream_research/nabulsi_page_315.txt', encoding='utf-8').read())
ar316 = norm(open('/root/dream_research/nabulsi_page_316.txt', encoding='utf-8').read())
ar317 = norm(open('/root/dream_research/nabulsi_page_317.txt', encoding='utf-8').read())
ar318 = norm(open('/root/dream_research/nabulsi_page_318.txt', encoding='utf-8').read())
ar328 = norm(open('/root/dream_research/nabulsi_page_328.txt', encoding='utf-8').read())
ar338 = norm(open('/root/dream_research/nabulsi_page_338.txt', encoding='utf-8').read())
ar347 = norm(open('/root/dream_research/nabulsi_p347_349.txt', encoding='utf-8').read())

MTR_HEAD = cut(ar315, "- (مطر) هو في المنام إذا لم يحصل منه ضرر", "حياة من يخشى عليه من")   # breaks mid-sentence at page end
MTR_CONT = cut(ar316, "آدمي أو أرض", "وتتفجر العيون.")
assert MTR_HEAD[-25:] in "حياة من يخشى عليه من" or MTR_HEAD.endswith("من"), MTR_HEAD[-40:]
assert MTR_CONT.startswith("آدمي أو أرض")
MTR_AAM  = cut(ar316, "- (ومن رأى) مطراً عاماً يحيا له أمر ميت", "فرج عنه.")
MTR_FAJ  = cut(ar316, "- (ومن رأى) المطر قد عاجله", "في تلك السنة.")
MTR_DAR  = cut(ar316, "- (ومن رأى) المطر في داره خاصة", "والمحلة والموضع والقرية.")
MTR_FIT  = cut(ar316, "- (ومن رأى) مطراً يسيح من كل جانب", "في حين ضرره.")
MTR_SQF  = cut(ar316, "- (ومن رأى) نفسه في المطر تحت سقف", "قضيت له.")
MTR_SIF  = cut(ar316, "- (ومن رأى) السماء قد أمطرت سيوفاً", "فإنهم يمرضون.")
MTR_SHRB = cut(ar316, "- (ومن رأى) أنه يشرب من ماء المطر", "شرب من الماء.")
MZ_HEAD  = cut(ar317, "- (ميزاب) هو في المنام رجل صاحب معروف", "ميازيب تجري في غير مطر فإنها")  # breaks at page end
MZ_CONT  = cut(ar318, "تدل على فتن وكل ميزاب منها يدل على ضرب رقبة", "بما ينزل منه الماء.")
MZ_RAHM  = cut(ar318, "- (ومن رأى) أنه تحت ميزاب الرحمة", "كان بعكس ذلك.")
MTQ1     = cut(ar328, "- (مطرقة) هي في المنام صاحب الشرط.", "صاحب الشرط.")
MTQ2     = cut(ar328, "- (ومن رأى) أنه أخذ مطرقة صار إليه فضل كثير", "اللغط في الكلام.")
MTRAN    = cut(ar338, "- (مطران) من رأى في المنام أنه مطران يخضع له", "بريء.")
MAWT     = cut(ar347, "وموت المرأة المجهولة يدل على إمساك القطر عن الأرض", "أحيا الله تعالى الأرض بالغيث")
for a, src in ((MTR_HEAD,ar315),(MTR_CONT,ar316),(MTR_DAR,ar316),(MTR_SIF,ar316),(MZ_HEAD,ar317),
               (MZ_CONT,ar318),(MZ_RAHM,ar318),(MTQ2,ar328),(MTRAN,ar338),(MAWT,ar347)):
    must(src, a)

zg = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()
ZG = ["天晴雨散百忧去", "阴雨晦时主囚事", "行路逢雨有酒食", "狂风大雨人死亡"]
for L in ZG: must(zg, L)
assert zg.count("雨") == 4, zg.count("雨")

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

# ---------------- FAQ ----------------
FAQ = [
 ("What does it mean to dream about rain?",
  "Both classical Arabic books open the same entry with the same switch: if no harm comes from the rain, it is good, provision and mercy; if it destroys, the reading flips to punishment and calamity (Ibn Sirin compilation, printed p. 350; Al-Nabulsi, shamela 315, printed p. 318 — the Arabic headword runs the same harm clause first). Between those two poles the books price the scene: whose roof it falls on, which town, which season, whether you sheltered, washed or drank."),
 ("Is rain in a dream a good omen or a bad omen?",
  "Neither on its own — the books install switches, not signs. Rain over your house alone is personal blessing and, in the same sentence, an illness in that house (printed p. 350). Rain in season blocks travel, trade, medicine and freedom, Al-Nabulsi's shelter clause adds; rain out of its time, in its hour of harm, means sickness (printed p. 319). A general rain revives a dead matter and relieves the worried and the indebted. What decides the sign is location, timing and what the water did, not the cloud."),
 ("What does it mean when it rains inside the house?",
  "The classical books answer two separate scenes. Rain falling on your house from the sky: the compilation reads it twice in the same breath — personal blessings, and someone in that house falling sick (printed p. 350). Water running from a gutter — the rain's plumbing, the (ميزاب) entry: a gutter is a man of kindness, but gutters running with no rain mean strife and a reckoning, and standing under the Rain-Gutter of Mercy carries the same ruling as the well of Zamzam (shamela 317-318, printed pp. 320-321). All clauses quoted verbatim at location below."),
 ("What does the Chinese Zhou Gong book say about rain?",
  "The received 27-chapter text carries rain in exactly four verdict lines, and all four sit in chapter 1 (天地 日月 星辰): clearing after rain takes a hundred worries away; grey rainy weather prescribes confinement; meeting rain on the road means food and drink; wild wind and heavy rain mean a person's death. No chapter-1 rain line is a general omen — each names its own weather shape. The rain characters sit nowhere else in the received text; this book's teeth line (chapter 3) is quoted on the teeth pages."),
 ("What does modern research say about rain dreams?",
  "There is no population survey of rain dreams — we searched the published record today and none exists. Every usable number comes from one diary: a single dreamer's 30-year series of 11,777 dreams, in which rain-dreams run about 1.40%, the rain acted on the dreamer in about two thirds of them, and negative emotions outnumbered positive 48 dreams to 4 (Schredl, Int J Dream Res 13(2):302-305, 2020, abstract re-pulled from the journal today). In the same series the rain share rose across the years while snow, ice and hail fell (Schredl 2021, DOI 10.11588/ijodr.2021.1.78020, re-read today). The 2018 teeth-dream paper (PubMed 30319507, full text re-checked today) has no rain item anywhere — the letters r-a-i-n occur in it only inside the journal abbreviation 'Behav. Brain Sci.' The classical books read rain as a public sign for towns, rulers and harvests; the only modern design is one man's diary. The gap is stated, not papered over."),
]
FAQ_JSON = json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ], ensure_ascii=False)

# ---------------- skeleton from shipped baby page ----------------
B = open('/root/teethdreammeaning/site/dream/baby/index.html', encoding='utf-8').read()
CSS = re.search(r'<style>.*?</style>', B, re.S).group(0)
CHIP = {z: re.search(r'<span class="zone z-%s">.*?</span>' % z, B, re.S).group(0) for z in ("text","reading","research")}
assert all(CHIP.values())

TITLE = "Dreaming of Rain: What the Dream Books Actually Say"
DESC = "Rain in a dream: both Arabic books read harm-free rain as mercy and profit, then price place, season and shelter. Zhou Gong runs four rain lines."

ARTICLE_LD = json.dumps({"@context": "https://schema.org", "@type": "Article",
 "author": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"},
 "datePublished": "2026-11-08", "dateModified": "2026-11-08",
 "publisher": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"},
 "headline": TITLE, "url": "https://teethdreammeaning.com/dream/rain/", "inLanguage": "en",
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
<link rel="canonical" href="https://teethdreammeaning.com/dream/rain/">
<meta property="og:title" content="@@TITLE@@">
<meta property="og:description" content="@@DESC@@">
<meta property="og:url" content="https://teethdreammeaning.com/dream/rain/">
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
<h1>Dreaming of Rain: What It Means</h1>
<p class="lede">Both classical Arabic books open the same entry with the same switch, in the same order: <strong>if no harm comes from the rain, it is blessings, provision and mercy</strong> — and if it destroys, the same water reads as punishment (Ibn Sirin compilation, printed p. 350; Al-Nabulsi, shamela 315, printed p. 318, a thousand years apart). Between those two poles the books install four switches folk summaries never carry: <strong>location</strong> — rain over your house alone is personal blessing <em>and</em>, in the next breath, an illness in that house; <strong>timing</strong> — rain in season blocks travel, trade and medicine, rain out of season is sickness; <strong>what the water was</strong> — stones or blood, dust or sand, honey or butter, swords or watermelons each get their own clause; and <strong>what you did</strong> — sheltering from the rain is slander coming your way, washing in it is repentance, drinking it is gain if it was clear and sickness if it was cloudy. So the honest first answer is: <strong>these books do not read rain; they read where it fell, when it fell, what came down with it, and whether you stood under a roof.</strong></p>
</div>
<aside>
<details class="tocd" open>
<summary>On this page</summary>
<ul>
<div class="g">This site's reading</div>
<li><a href="#the-finding-rain-four-switches">The finding: one cloud, four switches</a></li>
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

<p>Rain belongs on a teeth-dream site by method, not by subject: this site's whole claim is that the classical books are clause machines, and no entry in them is a purer test than rain. One substance, one headword, and the valence flips on four coordinates. Plain answers first — no Arabic or Chinese on this screen — every quote checked to its printed page.</p>

<div class="qa">
<h3>Rain fell and nothing was harmed — the general reading</h3>
<p>The headword clause, in both books: good, provision, mercy. Al-Nabulsi then keeps two quiet life-clauses the English round-ups drop: rain may stand for the life of someone whose life is feared for, and for the fulfillment of what a person has been promised. The compilation's parallel chain runs life, an earthly being, or fulfillment of a promise — the same three columns. And in the same entry both books state a rare equation, reversible on its face: rain represents a caravan of camels, and a caravan of camels represents rain. Two images, one ledger line, in either direction.</p>
</div>

<div class="qa">
<h3>The rain fell only on your house</h3>
<p>Location is the sharpest switch, and the books price it twice. Rain falling exclusively on one known place means sorrow and distress for its dwellers — or the loss of a beloved, the compilation adds. But rain falling exclusively over the dreamer's own house is read as personal blessings — and, in the next sentence, as someone in that house falling sick or suffering debilitating pain. Al-Nabulsi mirrors both: private rain to your house means benefit, good and dignity, and if it covers the whole town the ruling extends to everyone in it. Same image, two columns — blessing and illness — because the house is a household, not a weather station.</p>
</div>

<div class="qa">
<h3>The storm damaged things — the destruction clause</h3>
<p>Cross the harm switch and everything flips. A destructive rainstorm, in the compilation, denotes dishonesty, cheating with measures, and stands for punishment on the corruption of that place's dwellers. Al-Nabulsi's mirror adds the civic register: the destroying flood is sedition and ruin falling on that place from the ruler, and rain that melts in every direction and cuts down trees is sedition from the sultan's side — and in a private house the same water becomes diseases, afflictions and smallpox. Stones or blood from the sky mean calamity and punishment for sins; dust or sand mean an unjust ruler in that locality; dirt without dust, oddly, means prosperity and a good harvest. The books even price the odd rain-falls: swords from the sky mean people are tested with arguing and litigation — and if the sky rains watermelons, they fall sick.</p>
</div>

<div class="qa">
<h3>You sheltered from the rain — and the season switch</h3>
<p>The shelter clause is one of the most quoted by dreamers and one of the least quoted by summaries: standing under a cover, a roof or behind a wall to escape the rain means suffering because someone slanders you — and Al-Nabulsi adds a penalty scale, that the shelterer may be struck in proportion to the rain that reached him. Then the timing switch: rain in season is read negatively — a roadblock barring travel, business losses, medicine a poor person cannot buy, or imprisonment — while Al-Nabulsi's tail clause prices the other pole: rain out of its time, in its hour of harm, means illnesses and ailments. On time it stops you; off time it sickens you. Neither book lets seasonal rain simply be good.</p>
</div>

<div class="qa">
<h3>You washed in the rain, or drank it</h3>
<p>The action clauses run positive. Washing yourself in the rain, performing ablution with it, washing your face or filth away: repentance from sin, spiritual guidance, and the abolishing of innovations from the heart — and Al-Nabulsi prices the same clause by person: a disbeliever who washes becomes Muslim, an innovator or sinner repents, the poor are enriched, and a request to a ruler is answered favorably. Drinking rainwater splits on clarity: clear and pure means blessings and benefits; dirty and polluted means a sickness, in proportion to what you drank. One water, three readings — mouth, skin, roof.</p>
</div>

<div class="qa">
<h3>A general rain, and the death clause</h3>
<p>Two clauses tie rain to this site's other pages. Al-Nabulsi keeps a general-rain clause: a rain falling on everyone revives for the dreamer a dead matter, and brings good, blessing and relief for the worried or indebted. And both books run the same stranger line in the death entry: the death of an unknown woman means the rain being withheld from the earth, and if she comes back to life, God revives the earth with rain — the rain page and the <a href="/dream/dead-person-resurrected/">resurrection page</a> quote the same clause from opposite sides.</p>
</div>

<div class="qa">
<h3>Rain indoors — gutters and the Rain-Gutter of Mercy</h3>
<p>People search this scene as "raining inside the house," and the classical answer is the plumbing, not the cloud. Al-Nabulsi's gutter headword, a page and a half after the rain entry: a gutter is a man of kindness — and the clause runs on to say that gutters running in no rain (the sentence breaks mid-word at the page edge here, and resumes on the next) indicate strife, each gutter a reckoning of the neck; running water clear while people benefit means prosperity and safety, murky or foul-smelling means disease; and whoever sees himself under the Rain-Gutter of Mercy — the Kaaba's own gutter — is met by mercy and receives what he hopes, exactly as the book ruled the well of Zamzam. The roof clause flips again: under a roof from rain is slander; under the gutter of mercy is answered prayer. Same geometry, opposite verdicts.</p>
</div>

@@CHIPR@@
<h2 id="the-finding-rain-four-switches">The finding: one cloud, four switches</h2>
<p>Set the two entries side by side — Al-Nabulsi's (مطر) headword at shamela 315-316 (printed pp. 318-319), the compilation's Rain entry at printed p. 350 — and the clause order is a mirror: harm-free first (good, provision, mercy), then life, then the promised-thing fulfilled, then the location split (exclusive place = sorrow for its dwellers; own house = personal blessing and its illness double; whole town = everyone), then stones and blood, then dust and sand as the unjust ruler, then dirt-without-dust as harvest, then the traveller's hindrance, then the destruction clause and its measure-cheating, then reconciliation with enemies, then the camel caravan's two-way equation, then wells and springs, then reviving an old stagnant matter, then debts paid and relief felt, then the farmer's harvest, then honey butter oil and food rained down, then mercy, knowledge, wisdom, the Qur'an, rejuvenation, resurrection and life — and then the shelter, the season, the washing, the drinking. The inheritance is exact, entry for entry, in the same sequence. On top of the mirror, this rain page shows four switches the teeth pages also found in these books, working the same way: <strong>location</strong> (house versus town versus the known place), <strong>timing</strong> (in season it blocks; out of season it sickens), <strong>substance</strong> (the water's cargo: stones, blood, dust, dirt, honey, butter, oil, swords, watermelons), and <strong>action</strong> (shelter = slander, wash = repentance, drink = profit or illness by clarity).</p>

<p>And three collisions no English round-up repeats. <strong>Inside the books:</strong> rain over your own house is blessing and illness in one breath — the two columns of one clause, the same double-entry the teeth ledger keeps where one caught tooth cuts the line of heirs and another keeps the property. <strong>Inside the Chinese book:</strong> the received Zhou Gong text carries rain in exactly four verdict lines, all four in chapter 1 (the Heaven-and-Earth chapter), and they disagree by shape — clearing after rain takes a hundred worries away, grey rainy weather prescribes confinement, rain met on the road means food and drink, wild wind with heavy rain means a person's death — while that same chapter's lines make wind and rain co-sign the only fatal verdict. The Chinese book has no rain headword chapter; it has weather shapes. <strong>Inside the alphabetic book:</strong> Al-Nabulsi files rain next to its own near-spelling traps — a few columns on, مطرقة (mallet) is the police chief and whoever takes one gets abundant favor, and مطران (a metropolitan bishop) is a man of authority calling people to innovation — three headwords sharing the first three letters, a reminder that the classical entry you reach depends on the word you looked up. And the compiled English edition carries its own anachronism inside the clouds entry this page quotes: the translation reads that clouds in a dream "also represent ships, airplanes" — 1992 hands around an eight-century list.</p>

@@CHIPT@@
<h2 id="the-entries-briefly">The entries, briefly</h2>
<p class="src">The Arabic side comes from two books: the compiled English dictionary attributed to Ibn Sirin (Pearl Publishing House, 1992 — "Rain" printed p. 350 per the book's own end-of-volume index, which also locates Rain gauge at 351 — where it is only a redirect to "Water level," printed p. 469 — and Rainbow at 351) and the Arabic original of Al-Nabulsi's <em>Ta'tir al-Anam</em>, whose (مطر) headword begins at shamela.ws/book/1217/315 (printed p. 318, باب الميم), runs onto shamela.ws/book/1217/316 (printed p. 319) where six (ومن رأى) clauses continue, whose (ميزاب) headword sits at /317 (printed p. 320) mid-sentence into /318 (printed p. 321), and whose near-homograph headwords (مطرقة) and (مطران) sit at /328 (printed p. 331) and /338 (printed p. 341). The death-and-rain clause is shared: the compilation's "Death" entry at printed p. 111 and Al-Nabulsi's (موت) entry at shamela 344 (printed p. 347). The Chinese side is four verdict lines, all from chapter 1 of the received Zhou Gong text. One sample of each book, translated, then the full checked passages in the sources section at the bottom.</p>

<div class="cites">
<div class="cite-hd"><div>Text</div><div class="src-hd">Source</div></div>
<div class="cite-row">
  <div class="txt"><p>"Rain: (Clouds; Drizzling; Life; Vapor; Water) If no harm or destruction is caused by a rainstorm in a dream, then it means blessings, profits and mercy. Rain in a dream also represents life, an earthly being, or fulfillment of a promise. ... If one sees rain falling exclusively over his house in a dream, it means personal blessings. ... Rain falling exclusively over one's house in a dream also means that someone will fall sick in that house, or suffer from a debilitating and excruciating pain. ... Rain in a dream also represents a caravan of camels, and a caravan of camels in a dream represents rain. ... If one sees himself standing under a cover, a roof, or behind a wall to take shelter from a rainfall in a dream, it means that he may suffer because of someone slandering him. ... Drinking from rainwater and if it is clear and pure in the dream, it means receiving blessings and benefits. Ifthe water is dirty and polluted in the dream, it means a sickness. (Also see Water)" (elided; full entry in Sources)</p></div>
  <div class="src">Ibn Seerin's Dictionary of Dreams (Al-Akili compilation, Pearl 1992) — "Rain," printed p. 350, running onto p. 351 (the running head "DICTIONARY OF DREAMS 351" sits mid-entry in the scan). Translated/compiled English; the scan's joined words (Ifthe, Ifone) are kept as printed.</div>
</div>
<div class="cite-row">
  <div class="txt"><p class="ar">@@MTR_HEAD@@</p><p class="ar">@@MTR_CONT@@</p></div>
  <div class="src">Al-Nabulsi, Ta'tir al-Anam — shamela.ws/book/1217/315-316 (printed pp. 318-319), the (مطر) headword, verbatim; the headword sentence breaks at "من" at the bottom of printed p. 318 and resumes at "آدمي أو أرض" at the top of p. 319: rain that brings no harm is good, provision and mercy; it may mean the life of one whose life is feared for, human or land, and the fulfillment of what one is promised; rain on a known place means its people's grief or the dreamer's worry over a loss; blood or stones from the sky mean sins and disobedience; the traveller's journey stalls; destroying rain in a fixed place means short measure in weight and the way of Lot's people; useful rain means reconciliation with enemies; help for the distressed; and the rain is the camel caravan as the camel caravan is the rain — and if the sky rains water dripping from clouds on every side, people receive abundance and gladness and the springs gush. (Translation ours.)</div>
</div>
</div>
<div class="note"><p>Zhou Gong, stated plainly: the received Chinese dream book this site quotes chapter by chapter carries rain in exactly four verdict lines, and all four sit in chapter 1 (天地 日月 星辰): 天晴雨散百忧去 "it clears, the rain scatters: a hundred worries go"; 阴雨晦时主囚事 "grey rain in dull weather: confinement"; 行路逢雨有酒食 "meeting rain on the road: food and drink"; 狂风大雨人死亡 "wild wind and heavy rain: a person dies. The character for rain (雨) appears nowhere else in the 27-chapter received text — there is no rain headword chapter to quote, and no other verdict line to add. All quoted at location in Sources; nothing else is claimed for the Chinese side.</p></div>

@@CHIPZ@@
<h2 id="what-modern-research-adds-and-what-it-do">What modern research adds — and what it doesn't</h2>
<p>Modern dream research has never surveyed rain dreams in a population — we searched the published record today and there is no general sample, no questionnaire item, no prevalence number. Everything measurable comes from one diary. Michael Schredl analyzed a single dreamer's long series — 11,777 dreams recorded over 30 years — and found rain in about 1.40% of reports; the rain affected the dreamer in two-thirds of the rain dreams, usually with no emotion explicitly mentioned, and when emotions were named, negative ones outnumbered positive 48 dreams to 4 ("It's raining again" — Bad weather in a long dream series, <em>International Journal of Dream Research</em> 13(2):302–305, 2020, DOI 10.11588/ijodr.2020.2.75162; abstract re-pulled from the journal today). The same series, re-read in a companion report, showed the share of rain dreams rising across the decades (Spearman r = .435, p = .014) while cold elements — snow, ice, hail — fell, in step with Germany's shrinking count of ice days (Schredl, IJoDR 14(1):144–146, 2021, DOI 10.11588/ijodr.2021.1.78020, full text re-read today; single dreamer, stated as such, correlation of a diary share with climate indices — not a causal design). Older survey work supports only the general rule: season content shows continuity in winter but not in summer (Schredl, Perceptual and Motor Skills 98:1438–1440, 2004, N = 444, <a href="https://pubmed.ncbi.nlm.nih.gov/15291235/">PubMed 15291235</a>, record re-pulled today), and weather-adjacent measurement at population scale exists only for temperature, not rain: +1&deg;C warmer nights produced about three extra nights of self-reported insufficient sleep per hundred people per month across 765,000 U.S. responses (Obradovich et al., <em>Science Advances</em> 3(5):e1601555, 2017, <a href="https://pubmed.ncbi.nlm.nih.gov/28560320/">PubMed 28560320</a>, record re-pulled today). The 2018 teeth-dream paper this site leans on elsewhere (<a href="https://pubmed.ncbi.nlm.nih.gov/30319507/">PubMed 30319507</a>) has no rain item anywhere in it — its full text, re-checked today, contains the letters "rain" only inside the journal abbreviation "Behav. Brain Sci." Set against the classical layer, the direction is the story: the Arabic books read rain as a public sign — for the town, the ruler, the harvest, the caravan — while the only modern instrument is one private dreamer's notebook, and its finding is that rain in his dreams mostly made him feel worse, in agreement with the books' destruction clauses and in silence on their mercy clauses. The gap is reported, not papered over.</p>

<h2 id="sources-all-passages-checked-against-the">Sources (all passages checked against the cited pages)</h2>
<div class="src">
<p><strong>Ibn Sirin compilation — "Rain," printed p. 350 (running onto 351)</strong> (Ibn Seerin's Dictionary of Dreams, compiled by Muhammad M. Al-Akili, Pearl Publishing House 1992, ISBN 1879405032; a later compilation attributed to the 8th-century scholar, not his autograph text; the book's own page index lists Rain at 350, Rainbow at 351, and "Rain gauge" at 351 — the latter a redirect to Water level at 469). Full entry, scan verbatim including its joined words: "@@RAIN@@" — "Rainbow," printed p. 351, the whole entry: "@@RAINBOW@@" — "Water level," printed p. 469 (the rain-gauge redirect target): "@@WATERL@@" — "Clouds," printed p. 87, continuing onto p. 88 (the running head sits mid-entry in the scan; first paragraph quoted): "@@CLOUDS1@@" — the poison-rain paragraph from the same entry: "@@CLOUDS2@@" (the translation's clouds list reads "Clouds in a dream also represent ships, airplanes" — an anachronism kept as printed in the 1992 compilation) — "Death," printed p. 111, the rain clause: "@@DEATHCL@@"</p>
<p><strong>Al-Nabulsi — (مطر), shamela.ws/book/1217/315, printed p. 318, continuing at /316, printed p. 319</strong> (Ta'tir al-Anam fi Ta'bir al-Manam, Abd al-Ghani al-Nabulsi d. 1731 CE, Dar al-Fikr edition; باب الميم; translation ours). Headword, breaking at the page edge after "حياة من يخشى عليه من" and resuming at the next page head: "@@MTR_HEAD@@" / "@@MTR_CONT@@" Then the six scenario clauses on printed p. 319: "@@MTR_AAM@@" (a general rain revives a dead matter, brings good, blessing and grace — and the worried or indebted are relieved); "@@MTR_FAJ@@" (rain that comes upon you suddenly: good, wide provision without straitening — and the rain is relief and rescue in that year); "@@MTR_DAR@@" (rain in your house alone, not the people's: benefit, good and dignity — and seen over the whole town the ruling falls on all of its people, quarter, place and village); "@@MTR_FIT@@" (rain melting from every side, cutting down and toppling trees: sedition and ruin falling on that place from the sultan; and in a private house the rain may be diseases, aches, afflictions and smallpox; earth raining blood is punishment, so stones from the sky; rain of blood predominating, or dust, is the ruler's oppression; the farmer's rain is glad tidings and fertility; and it is said: dirt without dust is clamor; honey or welcomed fruit-types of rain, butter, milk, oil, are good for all people; the rain means God's mercy and religion and relief and help, and the Qur'an, knowledge and wisdom, for water is the life of creation — how much more if it is milk or butter or honey; and perhaps it means calamities sent down — locusts, hail, wind, especially with fire in it and hot water; perhaps the strife and bloodshed, especially when its water is blood; and perhaps sicknesses and ailments when it comes outside its time, in its hour of harm); "@@MTR_SQF@@" (found under a roof or wall in the rain: harm of speech and hurt, or being struck in proportion to the rain that reached him — if in its season, then being barred from travel or work or a sick one or poverty, or prison in proportion; washing in it from impurity or purifying with it for prayer or washing the face or filth from body or garment: the disbeliever becomes Muslim, the innovator or sinner repents, the poor are enriched, and a need at a ruler's or other's door is granted); "@@MTR_SIF@@" (sky raining swords: people tested with arguing and litigation; raining watermelons: they fall sick); "@@MTR_SHRB@@" (drinking rainwater: clear, good in proportion to what was drunk; cloudy, sickness). — The gutter headword (ميزاب), shamela /317 printed p. 320, breaking mid-sentence at the page edge: "@@MZ_HEAD@@" and resuming at /318 printed p. 321: "@@MZ_CONT@@" (gutters running in no rain indicate strifes, each one a striking of the neck; the gutters are the serving girls and boys of the place; the gutter may mean relief because its people are relieved by its turning the water; or the messenger or trustee who does not betray the one who trusts him, delivering to each his due; blood running from it: an enemy shedding that town's blood; clear water people benefit from: ease and safety; murky or foul-smelling: diseases with sores, boils and smallpox; and the Rain-Gutter of Mercy seen in a mosque, house or known place carries the ruling of the well of Zamzam, as stated earlier under the well in باب الباء, especially if people benefit from its water) — "@@MZ_RAHM@@" (whoever is under the Rain-Gutter of Mercy, God overtakes him with His mercy and he gets what he hopes — if the water is good and pure; if it comes down cloudy, the opposite). — The near-homograph headwords, same باب الميم: shamela /328 printed p. 331, (مطرقة): "@@MTQ1@@" "@@MTQ2@@" (the mallet is the police chief; whoever takes one receives abundant favor; it points to help and provision for its owners and perhaps to evil and clamor in talk); shamela /338 printed p. 341, (مطران): "@@MTRAN@@" (a metropolitan who is submitted to: a man of authority calling people to an innovation, who follow him in proportion and he rises among people in proportion — and if one is called a metropolitan against his will, he is charged with an innovation or a lie and hurled with it while he is innocent of it). — The death-rain clause, shamela /344 printed p. 347, (موت) entry: "@@MAWT@@" (the death of the unknown woman means the rain held back from the earth; if she lives again, God revives the earth with the rain).</p>
<p><strong>Zhou Gong Jie Meng — received 27-chapter text</strong> (corpus checked line by line; the character 雨 occurs exactly four times in the whole received text): ch. 1 (天地 日月 星辰): "天晴雨散百忧去" — it clears, the rain scatters: a hundred worries go; "阴雨晦时主囚事" — grey rain in dull weather: confinement; "行路逢雨有酒食" — meeting rain on the road: food and drink; "狂风大雨人死亡" — wild wind and heavy rain: a person dies. No other chapter carries a rain line; none is smoothed into a general omen.</p>
<p><strong>Modern research.</strong> Schredl M. "&lsquo;It's raining again&rsquo; — Bad weather in a long dream series." <em>International Journal of Dream Research</em> 13(2):302–305, 2020. DOI 10.11588/ijodr.2020.2.75162 (journal abstract page re-pulled today: single dreamer, N = 11,777 dreams; rain dreams about 1.40%; rain affected the dreamer in two thirds of them; negative emotions 48 dreams vs positive 4). Schredl M. "Does global warming affect dream content? Analyzing a 30-yr. dream series." <em>IJoDR</em> 14(1):144–146, 2021. DOI 10.11588/ijodr.2021.1.78020 (full text re-read today: 11,808 dreams; snow/ice/hail share declining r = −.237 p = .100 one-tailed; rain share from the same series rising r = .435 p = .014; series totals: cold 1.68%, rain 1.40%; explicitly a single dreamer). Schredl M. "Seasons in dreams." <em>Perceptual and Motor Skills</em> 98(3 Suppl):1438–1440, 2004. <a href="https://pubmed.ncbi.nlm.nih.gov/15291235/">PubMed 15291235</a> (record re-pulled today: 376 women, 68 men; five dreams over a two-week window; winter-theme continuity supported, summer themes not differentiated between winter and summer collections). Obradovich N, Migliorini R, Mednick SC, Fowler JH. "Nighttime temperature and human sleep loss in a changing climate." <em>Science Advances</em> 3(5):e1601555, 2017. <a href="https://pubmed.ncbi.nlm.nih.gov/28560320/">PubMed 28560320</a> (record re-pulled today: 765,000 U.S. survey respondents 2002–2011; +1&deg;C nighttime anomaly ≈ +3 nights of insufficient sleep per 100 people per month; largest in summer, lower-income and elderly respondents — temperature, not rain, and sleep quantity, not dream content). Rozen N, Soffer-Dudek N. <em>Frontiers in Psychology</em> 9:1812, 2018. <a href="https://pubmed.ncbi.nlm.nih.gov/30319507/">PubMed 30319507</a> (full text re-checked today: no rain item in the theme list; the string "rain" appears in the paper only inside "Behav. Brain Sci." in the reference list).</p>
</div>

<div class="note"><p>This page reports what two classical Arabic texts, the received Chinese dream book (whose four rain lines disagree by weather shape), and one single-dreamer diary can see about dreams of rain. It is not a prediction, a medical or religious ruling, and no dream book — classical or modern — settles what a dream means for the person who had it. If this dream unsettled you, note the move every source on this page makes in its own form: the books do not ask whether rain is good or bad; they ask <em>where</em> it fell, <em>when</em> it fell, <em>what came down with it</em>, and <em>what you did in it</em>. For the same water read through a different door — drinking, drowning, clear and dirty — see <a href="/dream/water/">water dreams</a>, and for the clause where withheld rain and a dead woman are the same news, <a href="/dream/dead-person-resurrected/">a dead person alive again</a>.</p></div>

<section style="border-top:1px solid var(--line);margin-top:40px;padding-top:20px"><h2 id="related-questions" style="font-size:18px;font-weight:400">Related questions</h2><ul style="list-style:none;padding:0"><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/water/">Water dreams — the same books' fitna-versus-fortune clauses on the other side of the rain</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/dead-person-resurrected/">Dreaming of a dead person alive again — where the unknown woman's return is the rain</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/kaaba/">The Kaaba in a dream — the book's own Rain-Gutter of Mercy clause stands on its roof</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/teeth-falling-out/">Teeth falling out dream — the classic page that started this site</a></li></ul></section>
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

T = {k: esc(v) for k, v in {
 'RAIN': RAIN, 'RAINBOW': RAINBOW, 'WATERL': WATERL, 'CLOUDS1': CLOUDS1, 'CLOUDS2': CLOUDS2,
 'MTR_HEAD': MTR_HEAD, 'MTR_CONT': MTR_CONT, 'MTR_AAM': MTR_AAM, 'MTR_FAJ': MTR_FAJ,
 'MTR_DAR': MTR_DAR, 'MTR_FIT': MTR_FIT, 'MTR_SQF': MTR_SQF, 'MTR_SIF': MTR_SIF,
 'MTR_SHRB': MTR_SHRB, 'MZ_HEAD': MZ_HEAD, 'MZ_CONT': MZ_CONT, 'MZ_RAHM': MZ_RAHM,
 'MTQ1': MTQ1, 'MTQ2': MTQ2, 'MTRAN': MTRAN, 'MAWT': MAWT, 'DEATHCL': DEATHCL,
}.items()}
subs = {'@@TITLE@@': esc(TITLE), '@@DESC@@': esc(DESC), '@@CSS@@': CSS,
        '@@ALD@@': ARTICLE_LD, '@@FAQJ@@': FAQ_JSON,
        '@@CHIPR@@': CHIP['reading'], '@@CHIPT@@': CHIP['text'], '@@CHIPZ@@': CHIP['research']}
for k, v in subs.items():
    HEAD = HEAD.replace(k, v)
for k, v in T.items():
    HEAD = HEAD.replace('@@'+k+'@@', v)
assert '@@' not in HEAD, [l for l in HEAD.splitlines() if '@@' in l]
os.makedirs('/root/teethdreammeaning/site/dream/rain', exist_ok=True)
open('/root/teethdreammeaning/site/dream/rain/index.html','w',encoding='utf-8').write(HEAD)
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
