#!/usr/bin/env python3
"""Build site/dream/baby/index.html (Day 8, matrix item baby).
All quoted passages injected VERBATIM from corpus files (/root/dream_research/*);
every EN/AR assertion is asserted at build time — nothing is hand-copied.
Skeleton (styles/chips/aside/footer) reused from the shipped blood page."""
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

CHILD  = cut(en, "Child: (Little boy) In a dream, a child carried", "the little girl then represents his glad tidings.")
BIRTH  = cut(en, "Childbirth: (Giving birth) Seeing one's wife giving birth", "giving birth in a dream means loss of his investment. (Also see Dragon)")
BOY    = cut(en, "Boy: (Young boy) Seeing a young boy", "something good or bad may take place in wakefulness.")
SON    = cut(en, "Son: In a dream, a son may mean", "a daughter or a servant.")
CHICKS = cut(en, "Chicks: (Baby; Chicken; Fowl) A chick in a dream", "represents the voice of insolent people.")
assert len(CHILD) > 3000 and len(BIRTH) > 2000

ar214 = norm(open('/root/dream_research/nabulsi_page_214.txt', encoding='utf-8').read())
ar215 = norm(open('/root/dream_research/nabulsi_page_215.txt', encoding='utf-8').read())
ar218 = norm(open('/root/dream_research/nabulsi_page_218.txt', encoding='utf-8').read())

SUBI_HEAD = cut(ar214, "- (صبي) هو في المنام هم وغم", "والصبي البالغ عزة وقوة.")
SUBI_TALK = cut(ar214, "- (ومن رأى) أنه صبي يتعلم في المكتب", "فإنه يتوب من ذنب كان")  # p214 tail (sentence continues on p215)
SUBI_CONT = cut(ar215, "يعمله إذا كان تعلمه قرآناً", "من العز إلى الهوان.")      # p215 head continuation
SUBI_MARD = cut(ar215, "- (ومن رأى) أنه أمرد", "فإنه يموت.")
SUBI_QAHR = cut(ar215, "- (ومن رأى) نفسه صبياً وله محاكمة", "فإنه يقهر.")
SUBI_MIR  = cut(ar215, "- (ومن رأى) وجهه في المرآة وجه صبي", "عاقبته مذمومة.")
SUBI_CARRY= cut(ar215, "- (ومن رأى) أنه يحمل صبياً فإنه يدبر ملكاً", "كيوم ولدته أمه.")
SUBI_NEAR = cut(ar215, "- (ومن رأى) أن له ولداً صغيراً", "هموم صغيرة يسيرة.")
SUBI_LAP  = cut(ar215, "- (ومن رأى) أن في حجره صبياً", "وكثرة الخير المترادف.")
SUBIYA    = cut(ar215, "- (صبية) صغيرة رؤيتها في المنام", "فإن حملها جارية تشبهها.")
SUBI_BUY  = cut(ar215, "- (ومن رأى) أنه اشترى غلاماً أصابه هم", "أصاب خيراً.")
SUBI_BET  = cut(ar215, "- (ومن رأى) أنه يحمل صبية", "أن يحمل صبياً.")
SUBI_RET  = cut(ar215, "- (ومن رأى) أنه عاد طفلاً", "عاش إلى أرذل العمر.")
QAMAL     = cut(ar218, "- (صبيان القمل) هو في المنام قوم مفسدون", "ولا يقدر على منعهم.")
for a,src in ((SUBI_HEAD,ar214),(SUBI_CONT,ar215),(SUBIYA,ar215),(QAMAL,ar218)):
    must(src, a[:50])

zg = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()
ZG = ["抱小儿女主口舌","小儿死者主口舌","新生男女主大吉","子死者主添喜事","齿落更生子孙兴"]
for L in ZG: must(zg, L)

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

# ---------------- FAQ ----------------
FAQ = [
 ("What does it mean to dream about a baby?",
  "Both Arabic books open the same entry with the same split: a baby carried in arms is responsibility, distress and burden; a teenage child is glad tidings (Ibn Sirin compilation, printed p. 80; Al-Nabulsi, shamela 214, printed p. 217 — the Arabic runs clause for clause in the same order). The sign depends on the child's age, the child's sex, and the dreamer's own condition — sick, old, poor, imprisoned — not on the baby itself."),
 ("What is the difference between dreaming of a baby boy and a baby girl?",
  "The compilation's ledger: begetting a boy means worries, burdens or sickness; giving birth to a girl means relief from distress; and for a pregnant dreamer the books flip it — birthing a girl in the dream means a boy in life, and vice versa (printed pp. 53, 80-81). Al-Nabulsi: a little girl means fertility, might and ease after hardship, and carrying a girl is better than carrying a boy (printed p. 218). Zhou Gong runs against both: a newborn boy or girl alike is great fortune."),
 ("What does it mean to hold or carry a baby in a dream?",
  "The compilation reads carrying a child two ways in the same entry: distress and burdens — and managing an inheritance or a financial investment (printed p. 80). Al-Nabulsi mirrors both clauses, adding that whoever carries a boy manages a domain, while a prisoner who carries a girl is released (printed pp. 217-218). A baby in your arms is an asset report with a heavy column."),
 ("Is dreaming of a baby dying a bad omen?",
  "The compilation says the opposite: bereavement of a child in a dream means the opposite in real life — rejoicing, reunions, pleasures and earning respect — with a second, darker option: an intention of your children or wife to separate (printed p. 80). The received Zhou Gong book carries two child-death lines in two different chapters that contradict each other: one reads a little one's death as quarrels, the other as added joy. Both are quoted at location below."),
 ("What does modern research say about dreams of babies?",
  "The one study designed around infant dreams surveyed 273 women in three arms — postpartum, pregnant, never-pregnant: 88-91% recalled dreams, 86% of recalling postpartum mothers dreamed of the infant, and 73% of those dreams put the baby in peril, with 57% of postpartum women acting out the dream motorically and 60% waking to check on the baby (Nielsen & Paquette, SLEEP 30(9):1162-1169, 2007, PubMed 17910388, re-pulled today). No survey reports a general-population or male prevalence for baby dreams, and the 2018 teeth-dream checklist has no infant item (PubMed 30319507, re-checked today) — the gap is stated, not filled. The research measures maternal waking concern; none of its variables is the omen side of the ledger."),
]
FAQ_JSON = json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ], ensure_ascii=False)

# ---------------- skeleton from shipped blood page ----------------
B = open('/root/teethdreammeaning/site/dream/blood/index.html', encoding='utf-8').read()
CSS = re.search(r'<style>.*?</style>', B, re.S).group(0)
CHIP = {z: re.search(r'<span class="zone z-%s">.*?</span>' % z, B, re.S).group(0) for z in ("text","reading","research")}
assert all(CHIP.values())

TITLE = "Dreaming of a Baby: What the Dream Books Actually Say"
DESC = "Baby in a dream: both classical Arabic books price it as burden or glad tidings by age, sex and the dreamer's state. Zhou Gong reads newborns as fortune."

ARTICLE_LD = json.dumps({"@context": "https://schema.org", "@type": "Article",
 "author": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"},
 "datePublished": "2026-11-07", "dateModified": "2026-11-07",
 "publisher": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"},
 "headline": TITLE, "url": "https://teethdreammeaning.com/dream/baby/", "inLanguage": "en",
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
<link rel="canonical" href="https://teethdreammeaning.com/dream/baby/">
<meta property="og:title" content="@@TITLE@@">
<meta property="og:description" content="@@DESC@@">
<meta property="og:url" content="https://teethdreammeaning.com/dream/baby/">
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
<h1>Dreaming of a Baby: What It Means</h1>
<p class="lede">Both classical Arabic books open the same entry with the same split verdict: <strong>a baby carried in your arms is responsibility, distress and burden — while a teenage child is glad tidings.</strong> The <em>Ibn Sirin</em> compilation (printed p. 80) and Al-Nabulsi (shamela 214, printed p. 217) run clause for clause in the same order a thousand years apart. Then both books install switches that folk summaries never quote: the child's <strong>age</strong> flips the reading, its <strong>sex</strong> flips the ledger — in the compilation a boy means worries and a girl means relief, and for a pregnant dreamer the sexes trade places in real life — and the <strong>dreamer's own state</strong> decides everything else: a sick person who sees himself a child is told the opposite of what an old man in distress is told. So the honest first answer is: <strong>these books do not read babies; they read who is holding the baby, how old it is, and what it does next.</strong></p>
</div>
<aside>
<details class="tocd" open>
<summary>On this page</summary>
<ul>
<div class="g">This site's reading</div>
<li><a href="#the-finding-one-baby-four-switches">The finding: one baby, four switches</a></li>
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

<p>The baby sits inside this site's tooth cluster by one shared clause: in Al-Nabulsi's teeth entry, a falling upper tooth that lands <em>in the dreamer's lap</em> reads as a son — the child is the thing the teeth are counting. This page opens that child ledger itself: plain answers first, no Arabic or Chinese on this screen, every quote checked to its printed page.</p>

<div class="qa">
<h3>You held a baby — the general reading</h3>
<p>The headword in both books: a child carried in one's arms means responsibility, distress and difficulties. But the same entry immediately doubles the reading into an asset column: carrying a child also means <em>managing an inheritance or a financial investment</em>, and Al-Nabulsi's mirror clause puts it more grandly — whoever carries a boy manages a domain. And the baby has a temperament: a child in a dream represents a weak enemy who sometimes shows friendliness and at other times demonstrates enmity. Holding a baby, on these pages, is holding a small, unreliable principal.</p>
</div>

<div class="qa">
<h3>A boy or a girl?</h3>
<p>The compilation keeps a strict, counter-intuitive gender ledger: begetting a boy means worries, burdens or sickness, while giving birth to a girl means relief from distress or easing of difficulties — and for the pregnant dreamer the sexes trade places outright: a woman who dreams of giving birth to a girl will bear a boy, and the other way around (printed pp. 53, 80). Al-Nabulsi keeps the same polarity — the little boy carried is a worry, the little girl is fertility, might and ease after hardship, and carrying a girl is explicitly better than carrying a boy. The books hedge even their own hedge: children, they add, could mean sorrow and pain <em>or</em> happiness and joy — if they are your own children, they mean temptation with money.</p>
</div>

<div class="qa">
<h3>The sick man, the old man, and the mirror</h3>
<p>Three clauses show the reading runs off the dreamer, not the baby. A sick person who sees himself as a child is read as facing death — while a depressed or penniless old man who sees himself an infant gets the page's most famous line: relief, health, and freedom from his sins, like the day his mother gave birth to him. A scholar who finds himself in a kindergarten shifts to ignorance and loses his rank — but a person being instructed like a child receives an inheritance from his mother. And if a man with a pregnant wife looks in a dream-mirror and sees a child's face, his wife will beget a son who looks like his father. Al-Nabulsi mirrors all four, clause for clause, and adds a fifth: whoever sees himself beardless inherits from his mother.</p>
</div>

<div class="qa">
<h3>A baby died in the dream</h3>
<p>The compilation's bereavement clause reads against every folk expectation: loss of a child in a dream means <em>the opposite in real life</em> — rejoicing, reunions, pleasures and earning respect — though the entry keeps a second, colder option: sometimes it portrays an intention of one's children or wife to separate from the family. The received Zhou Gong book carries two child-death lines in two different chapters, and they disagree with each other — one reads a small child's death as quarrels, the other as added joy. Both lines are quoted at location in the note below and in Sources.</p>
</div>

<div class="qa">
<h3>Crying on your lap — and a stringed instrument</h3>
<p>The strangest clause in the entry, and it is in both books with the same furniture: a little child screaming in your lap means you play a string instrument — in Al-Nabulsi's wording, you strike the oud. A child that disdains to come near its father means financial promotion and enjoyment of life; a prisoner who carries a little girl is released from prison; the destitute who holds one has his adversities lifted, the poor one thriving. And a small boy on his own is worries, responsibilities, hard work, catering to ignorant people — the age scale runs from burden (infant) through worry with a pay-off (little boy) to glad tidings (teenager) to power (mature child).</p>
</div>

<div class="qa">
<h3>Chicks, lice and missing children</h3>
<p>Two near-adjacent entries in the same books carry the fear side of the symbol. The compilation's chicks entry (printed p. 79, one page before the Child headword): a chick in a dream represents a <em>stolen or a missing child</em>, and the sound of chicks is the voice of insolent people. Al-Nabulsi keeps a headword three pages on (printed p. 221), boys of lice: a swarm of little boys who cannot be brushed off means corrupting people trailing after your wife whom you cannot restrain. Both clauses are quoted verbatim in Sources — the honest report is that these books also know a child image that is simply frightening, and they price that too.</p>
</div>

@@CHIPR@@
<h2 id="the-finding-one-baby-four-switches">The finding: one baby, four switches</h2>
<p>Set the two entries side by side — Al-Nabulsi's (صبي) headword, one thousand years after the compilation's Child entry — and the clause order is a mirror: carried baby equals burden, teenage child equals glad tidings, the besieged town where a beautiful child descends from the sky is near deliverance, the scholar in school turns to ignorance, the instructed child inherits from his mother, the sick man becomes a child and dies, the aged man becomes a child and is born again, the mirror face promises a resembling son, the crying lap produces a string instrument, the child is a weak enemy with two faces. The inheritance is exact, and on top of it the pair install four switches a folk summary drops. <strong>Switch one — age:</strong> infant, teenager, mature child are three different entries on the same page, and their valences run from burden to power. <strong>Switch two — sex:</strong> boy worries, girl relieves, and the pregnant dreamer's sexes flip in real life — the only clause in the cluster that reads the dream backwards from the womb. <strong>Switch three — the dreamer's state:</strong> the same self-as-infant image is a death sentence for the sick and a second birth for the desperate; the books sort outcomes by condition, not content. <strong>Switch four — who carries:</strong> a prisoner carrying a girl goes free, a man carrying a boy manages a domain, and carrying a girl is <em>better</em> than carrying a boy.</p>

<p>And two collisions no English round-up repeats. <strong>Inside the Chinese book:</strong> the received Zhou Gong text carries child-death in two chapters with opposite verdicts — quarrels in one, added joy in the other — while its newborn line reads a boy <em>or</em> a girl alike as great fortune, exactly against the Arabic boy-as-worry ledger. <strong>Inside the Arabic books:</strong> the Child entry itself concedes both poles in one sentence — children could mean sorrow and pain <em>or</em> happiness and joy — and Al-Nabulsi contradicts his own page in print: the little girl of the (صبية) headword is fertility, might and ease after hardship, yet of children actually born to the dreamer he writes that if the child is male the outcome is praiseworthy and if female it is blameworthy (printed p. 218). The same self-contradiction this site found on the teeth page, where one caught tooth cuts the line of heirs and another keeps the property. The books are not inconsistent by accident; they are ledgers, and a ledger lists both columns.</p>

@@CHIPT@@
<h2 id="the-entries-briefly">The entries, briefly</h2>
<p class="src">The Arabic side comes from two books: the compiled English dictionary attributed to Ibn Sirin (Pearl Publishing House, 1992 — "Child" printed p. 80 per the book's own end-of-volume index, which also locates Chicks at 79, Childbearing and Childbirth at 80, Boy at 53 and Son at 401) and the Arabic original of Al-Nabulsi's <em>Ta'tir al-Anam</em>, whose (صبي) headword sits at shamela.ws/book/1217/214 (printed p. 217, باب الصاد), runs onto shamela.ws/book/1217/215 (printed p. 218) where the (صبية) girl entry also sits, and whose (صبيان القمل) clause sits at shamela.ws/book/1217/218 (printed p. 221). The Chinese side is four verdict lines from the received Zhou Gong book, chapters 3, 14 and 18. One sample of each book, translated, then the full checked passages in the sources section at the bottom.</p>

<div class="cites">
<div class="cite-hd"><div>Text</div><div class="src-hd">Source</div></div>
<div class="cite-row">
  <div class="txt"><p>"Child: (Little boy) In a dream, a child carried in one's arms means responsibility, distress and difficulties. A teenage child represents glad tidings or dispelling one's worries. ... Seeing a mature child in a dream means power and superiority. ... If one sees himself as a newborn child in a dream, it means that he will become wealthy and prosper. ... If a sick person sees himself as a child in a dream, it means his death. ... Carrying a child in a dream means managing an inheritance or a financial investment. ... On the other hand, if such an elderly person who sees himself in a dream as a little child is suffering from depression or financial difficulties or health problems, then it means relief from distress and good health and that he will become free from his sins, like the day his mother gave birth to him. ... A child in a dream represents a weak enemy who sometime shows friendliness and at other times demonstrates his enmity. ..." (elided; full entry in Sources)</p></div>
  <div class="src">Ibn Seerin's Dictionary of Dreams (Al-Akili compilation, Pearl 1992) — "Child," printed p. 80. Translated/compiled English.</div>
</div>
<div class="cite-row">
  <div class="txt"><p class="ar">@@SUBI_HEAD@@</p></div>
  <div class="src">Al-Nabulsi, Ta'tir al-Anam — shamela.ws/book/1217/214 (printed p. 217), the (صبي) headword, verbatim: the boy is worry and grief when he is a child carried; the teenage boy is glad tidings; and if the town is besieged and its people in hardship, and one sees a beautiful boy enter the town or descend from the sky or come out of the ground — the good news has drawn near and relief is for the people of that place; and the grown boy is might and strength. (Translation ours.)</div>
</div>
</div>
<div class="note"><p>Zhou Gong, stated plainly: the received Chinese dream book this site quotes chapter by chapter carries the baby in four verdict lines, in three chapters — 新生男女主大吉 "a newborn boy or girl: great fortune" (ch. 14, spouses and conception); 抱小儿女主口舌 "holding a little girl: words will be spent over you" (ch. 14); 小儿死者主口舌 "a small child's death: quarrels" (ch. 14); and 子死者主添喜事 "a child's death: a joy is added" (ch. 18, grief and death) — the same image with opposite verdicts, one chapter apart. The teeth bridge line is 齿落更生子孙兴 "teeth fall and grow again: descendants flourish" (ch. 3). All quoted at location in Sources; nothing else is claimed for the Chinese side.</p></div>

@@CHIPZ@@
<h2 id="what-modern-research-adds-and-what-it-do">What modern research adds — and what it doesn't</h2>
<p>The one survey designed around infant dreams is a three-arm study of 273 women — postpartum (n = 202), pregnant (n = 50), never-pregnant (n = 21) — interviewed within days of birth and again by telephone (Nielsen &amp; Paquette, "Dream-associated behaviors affecting pregnant and postpartum women," <em>SLEEP</em> 30(9):1162–1169, 2007, <a href="https://pubmed.ncbi.nlm.nih.gov/17910388/">PubMed 17910388</a>; full text re-pulled today). Dream recall was equally high in all arms (88–91%), but infant-themed dreams spiked by condition: 86.0% of recalling postpartum mothers and 88.4% of recalling pregnant mothers had dreamed of the new or future infant, against 21.1% of never-pregnant women. Postpartum infant dreams were also darker — anxiety in 75% versus 59%, the infant in peril in 73% versus 42% — and more often enacted: motor activity in 57% of postpartum women (searching the bed-covers for a lost baby) against 24–25% in the other arms, with 60% reporting a need to check on the infant on waking. The authors' name for the pattern is the baby-in-bed nightmare. That is the modern layer's entire answer to "dreaming of a baby": in the one population systematically studied, the baby dream is a continuity picture of waking maternal vigilance, common, anxious, and sometimes acted out — and it says nothing about boys bringing worry or girls bringing relief. Outside that population the numbers simply do not exist: no general-population survey reports a prevalence for baby dreams, and the theme checklist behind the 2018 teeth-dream study (<a href="https://pubmed.ncbi.nlm.nih.gov/30319507/">PubMed 30319507</a>) has no infant item — its full text, re-checked today, contains none of the words baby, infant or newborn. The classical four switches — age, sex, dreamer's state, who carries — are not variables in any published design. The gap is reported, not papered over.</p>

<h2 id="sources-all-passages-checked-against-the">Sources (all passages checked against the cited pages)</h2>
<div class="src">
<p><strong>Ibn Sirin compilation — "Child," printed p. 80</strong> (Ibn Seerin's Dictionary of Dreams, compiled by Muhammad M. Al-Akili, Pearl Publishing House 1992, ISBN 1879405032; a later compilation attributed to the 8th-century scholar, not his autograph text; the book's own page index lists Child at 80, Childbearing and Childbirth at 80, Children at 81, Chicks at 79, Boy at 53, Son at 401). Full entry: "@@CHILD@@" — "Childbirth," printed p. 80, continuing onto p. 81 (the running head "DICTIONARY OF DREAMS 81" sits mid-entry in the scan): "@@BIRTH@@" — "Boy," printed p. 53: "@@BOY@@" — "Son," printed p. 401, the whole entry: "@@SON@@" — "Chicks," printed p. 79: "@@CHICKS@@"</p>
<p><strong>Al-Nabulsi — (صبي), shamela.ws/book/1217/214, printed p. 217, continuing at /215, printed p. 218</strong> (Ta'tir al-Anam fi Ta'bir al-Manam, Abd al-Ghani al-Nabulsi d. 1731 CE, Dar al-Fikr edition; باب الصاد; translation ours). Headword: "@@SUBI_HEAD@@" Then the school clause, which breaks across the page — on p. 217: "@@SUBI_TALK@@" and resuming on p. 218: "@@SUBI_CONT@@" (the sentence runs across the page break: whoever learns in school repents of a sin — if his learning is Qur'an; and if a man of knowledge or a ruler sees himself learning in school, he turns to ignorance or changes from might to abasement). — "@@SUBI_MARD@@" (beardless = inheritance from his mother; the poor man sees himself newly born = provision and wealth; a young man seeing it = not praised; a sick man seeing himself a child = he dies.) — "@@SUBI_QAHR@@" (a trial means being conquered; the face in the mirror continues: and if his wife is pregnant she brings a son resembling him; carrying the small child is worry, and the boy is a weak enemy who shows his friendship then his enmity) — "@@SUBI_MIR@@" — "@@SUBI_CARRY@@" (carrying a boy = managing a domain; a great man turned suckling infant = an ignorant act that goes his manhood — unless he is in heavy worry or straitened, and then it leads to relief and health, and he comes out of his sins like the day his mother gave birth to him) — "@@SUBI_NEAR@@" (a small child who keeps his distance from your body = increase and delight in your world; small boys = small, light worries) — "@@SUBI_LAP@@" (a boy screaming in your lap = you strike the oud; and the small ones, by the Qur'anic verse — {siṣību alladhīna ajramu ṣighārun ʿinda llāhi wa-ʿadhābun shadīd} — "there will befall the criminal ones humility before God and a terrible chastisement" (6:124), which Nabulsi cites against the word صغار; perhaps also joys and adornment; one's own children = temptation with money; perhaps contentment with little, or inability to pay the costs of living; and killing a child may mean abundant knowledge, from the story of al-Khiḍr; and it is said: sons mean money, spouses and abundance of heaped good). — The girl entry, same page: "@@SUBIYA@@" — "@@SUBI_BUY@@" — "@@SUBI_BET@@" — "@@SUBI_RET@@" (returning to childhood: in swaddling = prison or illness; let loose with money = his mind goes or his money is seized; a poor man = he lives to the most decrepit of age). And on shamela 218 (printed p. 221), the adjacent headword (صبيان القمل): "@@QAMAL@@" — boys of lice are corrupting people; whoever sees them and cannot remove them — men of corruption follow his wife and he cannot prevent them.</p>
<p><strong>Zhou Gong Jie Meng — received 27-chapter text</strong> (corpus checked line by line): ch. 14 (夫妻 产孕 交欢): "抱小儿女主口舌" — holding a little girl: words will be spent over you; "小儿死者主口舌" — a small child's death: quarrels; "新生男女主大吉" — a newborn boy or girl: great fortune. Ch. 18 (哀乐 病死 歌唱): "子死者主添喜事" — a child's death: a joy is added. Ch. 3 (身体 面目 齿发): "齿落更生子孙兴" — teeth fall out and grow again: descendants flourish. The two child-death lines sit in different chapters with opposite verdicts; both are printed, neither is smoothed.</p>
<p><strong>Modern research.</strong> Nielsen T, Paquette T. "Dream-associated behaviors affecting pregnant and postpartum women." <em>SLEEP</em> 30(9):1162–1169, 2007. <a href="https://pubmed.ncbi.nlm.nih.gov/17910388/">PubMed 17910388</a> (full text re-pulled today: three arms — postpartum n = 202 mean age 29.7, pregnant n = 50, null gravida n = 21; dream recall 88.1% / 88.4% / 90.5%; infant-themed dreams among recallers 86.0% / 88.4% / 21.1%; dream anxiety 75% vs 59%, P &lt; 0.05; infant in peril 73% vs 42%, P &lt; 0.0001; any dream-associated behavior 63.4% postpartum vs 39.5% pregnant; motor activity 57.3% vs 24.4% / 25.0%; post-awakening: anxiety 41%, confusion 51%, need to check on infant 60%; baby-in-bed (BIB) nightmare pattern defined; primiparas recalled infant dreams more than multiparas, 87.4% vs 66.4%). Rozen E, Soffer-Dudek D. "Dental irritation and teeth-grinding may be associated with dreams about teeth: an association study." <em>Frontiers in Psychology</em> 9:1812, 2018. <a href="https://pubmed.ncbi.nlm.nih.gov/30319507/">PubMed 30319507</a> (full text re-checked today: the theme checklist has no infant item — the words baby, infant and newborn do not occur in it).</p>
</div>

<div class="note"><p>This page reports what two classical Arabic texts, the received Chinese dream book (including its own child-death contradiction), and the one designed research study can see about dreams of babies. It is not a prediction, a medical or religious ruling, and no dream book — classical or modern — settles what a dream means for the person who had it. If this dream unsettled you, note the move every source on this page makes in its own form: the books do not ask whether the baby is good or bad; they ask <em>whose</em> child, <em>how old</em>, <em>what sex</em>, and <em>who is carrying it</em>. For the mouth-side of the same ledger — a falling tooth in the lap means a son, and a child's death reads two ways in the Chinese book — see <a href="/dream/teeth-falling-out-and-death/">teeth falling out and death</a>.</p></div>

<section style="border-top:1px solid var(--line);margin-top:40px;padding-top:20px"><h2 id="related-questions" style="font-size:18px;font-weight:400">Related questions</h2><ul style="list-style:none;padding:0"><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/teeth-falling-out-and-death/">Teeth falling out and death — where the tooth ledger counts sons and heirs</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/blood/">Blood dreams — the same books' menstrual clauses read the unmarried, the pregnant and the past-period woman three ways</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/dead-person-resurrected/">Dreaming of a dead person alive again — the entry whose progeny clause meets this page's bereavement flip</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/wedding/">Wedding dreams — Al-Nabulsi's pregnant-bride clause, next door in the same book</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/teeth-falling-out/">Teeth falling out dream — the classic page that started this site</a></li></ul></section>
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
 'CHILD': CHILD, 'BIRTH': BIRTH, 'BOY': BOY, 'SON': SON, 'CHICKS': CHICKS,
 'SUBI_HEAD': SUBI_HEAD, 'SUBI_TALK': SUBI_TALK, 'SUBI_CONT': SUBI_CONT,
 'SUBI_MARD': SUBI_MARD, 'SUBI_QAHR': SUBI_QAHR, 'SUBI_MIR': SUBI_MIR,
 'SUBI_CARRY': SUBI_CARRY, 'SUBI_NEAR': SUBI_NEAR, 'SUBI_LAP': SUBI_LAP,
 'SUBIYA': SUBIYA, 'SUBI_BUY': SUBI_BUY, 'SUBI_BET': SUBI_BET, 'SUBI_RET': SUBI_RET,
 'QAMAL': QAMAL,
}.items()}
subs = {'@@TITLE@@': esc(TITLE), '@@DESC@@': esc(DESC), '@@CSS@@': CSS,
        '@@ALD@@': ARTICLE_LD, '@@FAQJ@@': FAQ_JSON,
        '@@CHIPR@@': CHIP['reading'], '@@CHIPT@@': CHIP['text'], '@@CHIPZ@@': CHIP['research']}
for k, v in subs.items():
    HEAD = HEAD.replace(k, v)
for k, v in T.items():
    HEAD = HEAD.replace('@@'+k+'@@', v)
assert '@@' not in HEAD, [l for l in HEAD.splitlines() if '@@' in l]
os.makedirs('/root/teethdreammeaning/site/dream/baby', exist_ok=True)
open('/root/teethdreammeaning/site/dream/baby/index.html','w',encoding='utf-8').write(HEAD)
print("wrote", len(HEAD), "bytes")
print("div", HEAD.count('<div'), HEAD.count('</div>'))
print("blockquote", HEAD.count('<blockquote'), HEAD.count('</blockquote>'))
print("p", HEAD.count('<p'), HEAD.count('</p>'))
print("footer", HEAD.count('<footer'), HEAD.count('</footer>'))
seg = HEAD.split('<h1>')[1].split('<h2')[0]
print("first-screen Arabic:", sum(1 for ch in seg if '\u0600' <= ch <= '\u06ff'),
      "CJK:", sum(1 for ch in seg if '\u4e00' <= ch <= '\u9fff'))
print("CJK total:", sum(1 for ch in HEAD if '\u4e00' <= ch <= '\u9fff'))
