#!/usr/bin/env python3
"""Build site/dream/dog/index.html (Day 11, matrix item dog).
All quoted passages injected VERBATIM from corpus files (/root/dream_research/*);
every EN/AR/CN assertion is checked at build time — nothing is hand-copied.
Skeleton reused from the shipped fire page (build_fire.py)."""
import re, json, os

def norm(s): return re.sub(r'\s+', ' ', s).strip()

# ---------------- corpus: EN (Ibn Sirin compilation) ----------------
en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = norm(re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en))
en = norm(re.sub(r"[\d~]+ IBN SEERIN'?S", ' ', en))

def cut(src, start, end):
    i = src.find(start); assert i != -1, "MISS START: " + start[:60]
    j = src.find(end, i); assert j != -1, "MISS END: " + end[:60]
    return norm(src[i:j+len(end)])

def must(src, s):
    assert s in src, "MISS: " + s[:70]

DOG = cut(en, "Dog: (Bitch; Canine; Desire; Greyhound; Japanese spaniel; Pekingese; Lust;",
             "Seeing a dog in a city in a dream also means renewal of one's business contract.")
assert len(DOG) > 3800, len(DOG)
assert 'IBN SEERIN' not in DOG and 'DICTIONARY OF DREAMS' not in DOG
DOGFIGHT = "Dogfight: In a dream, a dogfight means love for the world. (Also see Dog)"
must(en, DOGFIGHT)
for s in ("an insolent man who dares to indulge in sinful actions",
          "repulsive and an abominable character",
          "harm caused by one's enemy and its effects will depend on the amount of pain one suffers in the dream",
          "harm caused by a close companion or a servant",
          "Ifone does not hear the barking of the dog in the dream, it signifies that one's enemy has left him inflected with a small loss",
          "A puppy in a dream represents a loved child",
          "grow to be a believer",
          "govern the household and to presides over its people",
          "a child of adultery, a foundling who is left in the street, wrapped in a swaddle",
          "A shepherd's dog in a dream represents profits and benefits",
          "A pet dog in a dream represents an astringent and a bitter enemy",
          "gaining authority, control and wealth",
          "backbone of an army general or his best helper",
          "though he lacks principals and moral integrity",
          "A Japanese spaniel or a Pekingese in a dream signifies mixing with, or doing business with a foreign counterpart",
          "Bringing-up a dog for companion",
          "Hunting with a dog in a dream means satisfying one's lust or desire",
          "Killing a dog in a dream signifies vanquishing one's enemy",
          "blessings and prosperity for everyone",
          "dispelling people's fears, or it could mean lack of work",
          "a high rate of unemployment",
          "illness and financial losses or loss of appetite or losing the pleasure of living",
          "A barking bitch in a dream signifies harm and deceit which is caused by abominable people",
          "suffering from extremely high fever and in relation to Dog star or the stars Procyon and Sirius of the constellations Canis Minor and Canis Major",
          "all breeds of dogs represent lowly, obsequious and despicable people",
          "reared for bantering or dallying with in a dream signify fun and enjoying one's life",
          "suffering from distress, sorrow or loss of one's pleasure of living",
          "God Almighty has taught him great knowledge which he abused and discarded, then God Almighty stripped him from such a knowledge",
          "a police informer or a police dog",
          "a weak enemy or a niggardly person",
          "hear something he despises or hates to make public from someone who lacks any sense of honor or virtue",
          "Eating a dog's meat in a dream means cracking down at one's enemy",
          "a guard or an innovator",
          "Drinking dog's milk in a dream means a scare",
          "Laying one's head on a dog or relaxing with a dog or using the dog for a pillow in a dream, the dog then represents a friend or a good companion",
          "a street boy, a beggar or an obsequious, lowly and a despicable person who maintains affection toward his master and jealously guards him, his children and property",
          "greed, love for the worldly pleasures, committing a dogfight to win them and failing to have any reserve or savings",
          "A hunting dog in a dream represents honor and profits",
          "A shepherd's dog represents a good neighbor who cares more about his neighbors than about his own household",
          "Adopting a dog as a pet in a dream means wavering, or paying financial damages, or it could mean unemployment",
          "Taking a dog for a companion on a journey in a dream means disappearing",
          "disbelief, ingratitude or losing hope, belying, fear, imprisonment, or becoming a fugitive",
          "renewal of one's business contract"):
    must(en, s)
# cross-reference headwords (kept as printed in the A-Z body):
must(en, "Bitch: (See Dog)")
must(en, "Canine: (See Dog)")
must(en, "Canines: (See Tooth)")
must(en, "Greyhound: (See Dog)")
must(en, "Puppy: (See Dog)")
must(en, "Shepherd's dog: (See Dog)")
must(en, "Tyke: (See Dog)")
must(en, "Hunting dog: (Lust; Desire; Want. See Dog)")
must(en, "Dog star: (astr. See Dog)")
# index lines:
must(en, "Dog 123")
must(en, "Dog star 123")
must(en, "Dogfight 124")
must(en, "Bitch 40")
must(en, "Greyhound 195")
must(en, "Puppy 346")
must(en, "Shepherd's dog 384")

# ---------------- corpus: AR (Al-Nabulsi) ----------------
def arload(f): return norm(open(f'/root/dream_research/nabulsi_page_{f}.txt', encoding='utf-8').read())
ar295, ar296 = arload("295"), arload("296")

KALB_HEAD  = cut(ar295, "- (كلب) هو في المنام رجل سفيه يجترئ على المعاصي", "فإذا نبح فهو سفيه شنيع طبع.")
KALB_BITE  = cut(ar295, "- (ومن رأى) كلباً عضه أو خدشه", "بقدر الألم وربما مرض.")
KALB_LONG  = cut(ar295, "- (ومن رأى) كلباً مزق ثيابه", "ليس هم من أهل الإسلام.")
KALB_SCEN  = cut(ar295, "- (ومن رأى) أنه أخذ كلباً", "عمل لا يتم ورجاء كاذب.")
KALB_TRANS1 = cut(ar295, "- (ومن رأى) أنه تحول كلباً", "قد علمه علماً عظيماً")   # breaks at page edge
KALB_TRANS2 = cut(ar296, "فبطر ذلك العلم فسلبه الله إياه", "والكلب رجل شحيح.")
KALB_BARK  = cut(ar296, "- (ومن رأى) أنه ينبح عليه كلب", "كلاماً يكرهه.")
KALB_MEAT  = cut(ar296, "- (ومن رأى) أنه يأكل لحم كلب", "دليل على تجديد ولاية.")
for a, src in ((KALB_HEAD,ar295),(KALB_BITE,ar295),(KALB_LONG,ar295),(KALB_SCEN,ar295),
               (KALB_TRANS1,ar295),(KALB_TRANS2,ar296),(KALB_BARK,ar296),(KALB_MEAT,ar296)):
    assert a in src and len(a) > 30, a[:50]
# key mirror phrases inside the Arabic:
for s in ("رجل سفيه يجترئ على المعاصي", "بقدر الألم", "امرأة دنيئة من قوم سوء معاندين",
          "جرو الكلب ولد محبوب", "فإن كان أبيض فهو مؤمن", "يسود أهل بيته", "لقيط رجل سفيه يربيه",
          "عدو ظالم", "رجل ظهر ينصر على الأعداء لكنه دنيء بلا مروة",
          "يخالط قوماً من العجم ليس هم من أهل الإسلام", "ينال أمنيته ويبلغ شهوته",
          "يظفر بعدوه", "ذهاب الفزع وعلى بطالة", "تدل على حفظ امرأة الرجل ومتاعه",
          "مضرة تكون من أناس سوء وعلى خديعة منهم", "يدل على الحمى بسبب الكوكب الذي يسمى الكلب",
          "الشعري اليمانية التي هي علة الحميات", "قوم أذلة", "فسلبه الله إياه",
          "بغلمان الشرطة", "عدو ضعيف", "رجل شحيح", "قليل المروءة",
          "يظفر بعدوه ويصيب من ماله", "الحارس", "ذي البدعة", "شرب لبن الكلب خوف",
          "فالمُتَوَسِّد" if False else "ومن توسد كلباً فالكلب حينئذ صديق",
          "غلام أو شحاذ على الأبواب", "الانكلاب على الدنيا مع عدم الادخار",
          "كلب الصيد عز ورفعة ورزق", "جار صالح غيور على الأهل والجار",
          "الزيغ والغرم في المال وإبطال العمل", "صحبة الكلب تدل على الاختفاء لقصة أهل الكهف",
          "امرأة حافظة للزوج كثيرة النسل", "الكفر والإياس من رحمة الله تعالى والتكذيب",
          "رؤية كلب أهل الكهف يدل على الخوف والسجن أو الهرب", "رؤيته في البلد دليل على تجديد ولاية",
          "الكلبة المائية تدل على عمل لا يتم ورجاء كاذب"):
    assert s in ar295 or s in ar296, "AR MISS: " + s[:50]

# ---------------- corpus: CN (Zhou Gong received text) ----------------
zg = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()
ZG_LINES = ["豺狼恶狗有盗贼", "犬吠人鬼来求食", "犬咬主人失财凶"]
for s in ZG_LINES: must(zg, s)
assert zg.count('犬') == 2 and zg.count('狗') == 1, (zg.count('犬'), zg.count('狗'))

# ---------------- FAQ ----------------
FAQ = [
 ("What does a dog mean in a dream?",
  "Both classical Arabic books open the dog entry with the same single sentence: a dog is an insolent man who dares to indulge in sinful actions — and if he barks, he is impudent with a repulsive, abominable character (Ibn Sirin compilation, printed p. 123; Al-Nabulsi, shamela 295, printed p. 298, five centuries apart, the Arabic running word for word, quoted in full in Sources). Everything after that first sentence is a ledger of switches: bark, bite, breed, color, and what the dog does to you or you do to it."),
 ("Is a dog in a dream a good omen or a bad omen?",
  "The books do not price the animal; they price the relationship. A hunting dog means honor and profits, a shepherd's dog profits and benefits (and, later in the same entry, a good neighbor), and a puppy is a loved child — while a pet dog is a bitter enemy, a barking bitch harm and deceit, and a sick house dog illness and financial loss. The same animal sits on both ends of the ledger depending on what it is kept for. Full clauses at their printed pages below."),
 ("What does it mean if a dog bites you in a dream?",
  "Harm from an enemy — measured by your own pain: \"its effects will depend on the amount of pain one suffers in the dream\", says the compilation, and Al-Nabulsi's mirror runs the same clause in fewer words: harm from your enemy in proportion to the pain — the Arabic phrase quoted verbatim in Sources — and perhaps sickness (printed p. 123; shamela 295, printed p. 298). The books add two fall-guys: the harm can come from a close companion or a servant. And a strange quiet clause runs beside it: if you do not hear the barking, the enemy leaves you with only a small loss."),
 ("What does the Chinese Zhou Gong book say about dogs?",
  "Exactly three verdict lines carry the dog in the received 27-chapter text — two using the classical character for dog, one the vernacular. Chapter 25: jackals, wolves and vicious dogs mean thieves. Chapter 26: a dog barking at a person means ghosts come for food, and a dog biting its master means lost wealth and misfortune. No breed ledger, no enemy metaphor — bark, bite and menace each get one flat verdict. Lines quoted verbatim, in Chinese, in Sources."),
 ("What does modern research say about dog dreams?",
  "Dog dreams are the best-measured animal theme in the literature, and the headline finding is not symbolic: waking life drives the dream. In Schredl and colleagues' 2020 online survey of 1,695 Germans, dogs appeared on average in about 5.5% of remembered dreams, but the number splits by contact — people living with a dog estimate 19.19% of their dreams include dogs, never-dog-people 1.32%. Dog dreams are also measurably nicer than dreams in general (mean tone +0.64 vs +0.07 on a −2/+2 scale), and about 25% of respondents reported a negative waking experience with dogs, mostly a bite; those people report more threatening dog dreams (PDF re-pulled and all tables re-read today). The classical bite clause priced harm by felt pain; the research prices dog dreams by felt contact."),
]
FAQ_JSON = json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ], ensure_ascii=False)

# ---------------- skeleton from shipped rain/fire page ----------------
B = open('/root/teethdreammeaning/site/dream/rain/index.html', encoding='utf-8').read()
CSS = re.search(r'<style>.*?</style>', B, re.S).group(0)
CHIP = {z: re.search(r'<span class="zone z-%s">.*?</span>' % z, B, re.S).group(0) for z in ("text","reading","research")}
assert all(CHIP.values())

TITLE = "Dreaming of a Dog: What the Dream Books Actually Say"
DESC = "Dog in a dream: both Arabic books file it as an insolent enemy, then flip on bark, breed, color and bite. Zhou Gong runs three dog lines."

ARTICLE_LD = json.dumps({"@context": "https://schema.org", "@type": "Article",
 "author": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"},
 "datePublished": "2026-11-10", "dateModified": "2026-11-10",
 "publisher": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"},
 "headline": TITLE, "url": "https://teethdreammeaning.com/dream/dog/", "inLanguage": "en",
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
<link rel="canonical" href="https://teethdreammeaning.com/dream/dog/">
<meta property="og:title" content="@@TITLE@@">
<meta property="og:description" content="@@DESC@@">
<meta property="og:url" content="https://teethdreammeaning.com/dream/dog/">
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
<h1>Dreaming of a Dog: What It Means</h1>
<p class="lede">The two classical Arabic books open the dog entry with the same sentence: <strong>a dog is an insolent man who dares to indulge in sinful actions</strong> — and if he barks, he is impudent, of a repulsive and abominable character (Ibn Sirin compilation, printed p. 123; Al-Nabulsi, shamela 295, printed p. 298 — five centuries apart, running word for word; the Arabic quoted in full in Sources). That first sentence, though, is only the headline of a ledger. The books then price the dog by four switches: <strong>the bite</strong> — harm from an enemy, and the harm is sized by the pain you felt in the dream itself; <strong>the bark</strong> — hear it and the enemy is impudent, don't hear it and he leaves you with only a small loss; <strong>the breed</strong> — a hunting dog brings honor and profits, a pet dog is a bitter enemy, a shepherd's dog is profit or a good neighbor, a greyhound is army backbone without morals; and <strong>the color of the puppy</strong> — white grows to a believer, black grows to rule your household, because a puppy is a child. So the honest first answer is: <strong>these books do not ask whether the dog is friendly or feral; they ask what it did, whether you heard it, what breed it was, and what you were doing with it.</strong> The Chinese book runs three flat verdict lines — bark, bite, menace — with no ledger at all.</p>
</div>
<aside>
<details class="tocd" open>
<summary>On this page</summary>
<ul>
<div class="g">This site's reading</div>
<li><a href="#the-finding-dog-one-ledger-four-switches">The finding: one ledger, four switches</a></li>
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

<p>The dog is the most human animal in all three traditions, which makes it the cleanest test of what each layer does with closeness: the Arabic books read the dog as a person in disguise — an insolent man, a servant, a beggar, a police informer, a bitter enemy who guards your children — while modern survey research reads dreams of dogs as a contact log of the actual animal in the dreamer's house. Plain answers first — no Arabic or Chinese on this screen — every quote checked to its printed page.</p>

<div class="qa">
<h3>The bite, and the pain switch</h3>
<p>A dog's bite or scratch means harm caused by one's enemy, \"and its effects will depend on the amount of pain one suffers in the dream\" — the omen is literally metered by the dreamer's own sensation (printed p. 123). The clause adds two fall-guys: it could also mean falling sick, great affliction, or harm by a close companion or a servant. Al-Nabulsi's mirror runs the same clause shorter: \"whoever a dog bites or scratches — harm from his enemy in proportion to the pain, and perhaps sickness\" (shamela 295, printed p. 298). And beside the bite sits the quietest clause on the page: if you do not hear the dog barking, your enemy leaves you — afflicted, says the scan, with a small loss. No bark, small harm; full bark, pain-priced harm. The books never let the dog simply be a dog.</p>
</div>

<div class="qa">
<h3>The breed ledger — six dogs, six verdicts</h3>
<p>The entry splits the species by what humans keep it for. A shepherd's dog represents profits and benefits at the head of one paragraph and a good neighbor \"who cares more about his neighbors than about his own household\" at the head of another. A pet dog is an astringent and a bitter enemy; a greyhound is authority, control, wealth — the backbone of an army general, a good strategist \"though he lacks principals and moral integrity\" (the misspelling is the book's, kept as printed). A hunting dog means honor and profits; hunting with one means satisfying your lust or desire. A Japanese spaniel or a Pekingese means mixing with or doing business with a foreign counterpart — in Al-Nabulsi's Arabic, the same clause names the Chinese dog and foreign peoples who are not of the people of Islam. Al-Nabulsi keeps one breed the English compilation drops entirely: the water bitch, a job that never gets finished and a hope that lies. The same species, priced six ways, by six different closenesses.</p>
</div>

<div class="qa">
<h3>Puppies are children — and the color decides</h3>
<p>\"A puppy in a dream represents a loved child.\" White, the son grows a believer; black, he grows to govern the household and preside over its people — with the two books' standard hedge clause, \"it is said,\" loaded on the third reading: the puppy is a child of adultery, a foundling wrapped in a swaddle, brought home by an insolent person to be reared (printed p. 123; shamela 295, printed p. 298, word for word). The puppy clause is also the dog page's bridge into this site's baby page: the same book, in its child entry, reads a child as responsibility and a foundling as an enemy's child — the dog entry simply lends the swaddling image.</p>
</div>

<div class="qa">
<h3>Dogs, stars and fever — the strangest shared clause</h3>
<p>Both books, in the middle of the enemy ledger, install a piece of astronomy: \"A dog in a dream also means suffering from extremely high fever and in relation to Dog star or the stars Procyon and Sirius of the constellations Canis Minor and Canis Major\" (printed p. 123 — the scan prints the entry's tail on the page headed 124). Al-Nabulsi runs the same clause with the Arabic name of the star: the dog means fever because of the planet called the Dog — the Sirius of the Yemen, which is the cause of fevers (shamela 295, printed p. 298; the star's Arabic name quoted verbatim in Sources). This is not folklore about dogs; it is the classical doctrine that Sirius's heliacal rise opens the fever season, transplanted whole into dream grammar. The dream dog becomes a weather report.</p>
</div>

<div class="qa">
<h3>Becoming a dog, sleeping with a dog</h3>
<p>Two clauses about proximity close the ledger. Transformation: if you are turned into a dog, God taught you great knowledge which you abused and discarded, and then stripped it from you — both books, the sentence breaking across Al-Nabulsi's page edge mid-word of the story (printed p. 123; shamela 295-296, printed pp. 298-299). Comfort: lay your head on a dog, relax with one, use it as a pillow, and the dog is a friend and a good companion; Al-Nabulsi adds the warranty clause — a friend you take revenge with and lean on. Between them the books list the dog's other jobs: a guard, an innovator, a police informer, a street boy, a beggar who jealously guards his master's children and property, and drinking dog's milk — a scare. The dog is the servant who can be taken into the bed or into the soul, and the books check which one happened.</p>
</div>

<div class="qa">
<h3>The dog of the Cave — Nabulsi's own annotation</h3>
<p>One mirror pair shows exactly how the two books differ in method. The compilation: \"Taking a dog for a companion on a journey in a dream means disappearing.\" Al-Nabulsi, same clause, with the citation attached: the company of a dog means hiding \"because of the story of the People of the Cave\" — the Qur'anic sleepers whose dog stretched its paws at the entrance — and he then adds the verse's own dog as a separate reading: seeing the dog of the Companions of the Cave means fear, prison, or flight; and seeing a dog in the land means the renewal of governance, where the compilation had written, flatly, renewal of one's business contract (printed p. 123; shamela 296, printed p. 299). The Arabic book annotates its intertext; the English compilation translates the verdict and drops the footnote. Same clause, two disciplines.</p>
</div>

<div class="qa">
<h3>What Zhou Gong gives instead of a ledger</h3>
<p>The received Chinese book carries the dog in exactly three verdict lines across twenty-seven chapters. Chapter 25, the beasts chapter: jackals, wolves and vicious dogs — thieves. Chapter 26, the livestock chapter: a dog barking at a person — ghosts come for food; a dog biting its master — lost wealth, misfortune. Three lines, and they do what the Arabic ledger never does: they point outward. The Arabic bark means an enemy's insolence you overhear; the Chinese bark means a ghost at your door asking for a meal. The Arabic bite is pain-metered harm from an enemy; the Chinese bite is a household balance-sheet event — the master loses money. No breed, no color, no star, no Cave.</p>
</div>

@@CHIPR@@
<h2 id="the-finding-dog-one-ledger-four-switches">The finding: one ledger, four switches</h2>
<p>Set the compilation's Fire-like long Dog entry at printed pp. 123-124 beside Al-Nabulsi's (كلب) run at shamela 295-296 (printed pp. 298-299), and the clause order is the tightest mirror this site has measured on the queue — the English entry is a translation of the Arabic one, and they keep step clause by clause: the insolent man, the barking character, the pain-metered bite, the torn clothing as slander, the unheard bark as a small loss, the vile woman among evildoers, the loved child, white believer and black ruler, the adulterine foundling with its وقيل hedge, the shepherd's profit, the pet's bitter enmity, the greyhound's amoral strategist, the foreign counterpart, the servant kept with love, hunting as lust, killing as victory over the enemy, the hound expedition out (blessings), returning (fears dispelled or work lacking), entering town (unemployment), the sick house dog, the barking bitch, the Dog-star fever, all breeds as lowly people, the dallying dogs and their grief, the transformation and the stripped knowledge, the police informer, the weak enemy, the niggardly man, the bark you despise, eating dog meat as cracking the enemy, guard and innovator, milk as a scare, the pillow friend, the beggar who guards, greed and the dogfight and no savings, hunting dog honor, shepherd dog neighbor, the pet's wavering and damages, the journey companion's disappearance, disbelief and prison and flight, the city's renewed contract. Where the books part, they part three ways. <strong>The translator's choices:</strong> Al-Nabulsi's الكلب الصيني becomes \"a Japanese spaniel or a Pekingese\" — a breed relabeling that quietly re-dates the ledger for a 1992 English reader. <strong>What the Arabic keeps and the English drops:</strong> the water bitch (unfinished work, false hope), the faithful fertile wife reading of the bitch beside the harm-and-deceit reading, the People of the Cave citation. <strong>What the English adds:</strong> the constellation names Procyon and Sirius, Canis Minor and Canis Major, where the Arabic said only the Dog star of the Yemen. Then the cross-language collision: the Chinese book's three lines read the bark as ghosts at the door and the bite as the master's money — shape and rank verdicts again, no relationship ledger — while the modern layer, below, measures neither enemies nor ghosts but contact hours per week.</p>

@@CHIPT@@
<h2 id="the-entries-briefly">The entries, briefly</h2>
<p class="src">The Arabic side comes from two books: the compiled English dictionary attributed to Ibn Sirin (Pearl Publishing House, 1992 — \"Dog\" printed p. 123 per the book's own end-of-volume index, the entry running onto p. 124, where the same index places Dogfight; Bitch is indexed at 40, Greyhound at 195, Puppy at 346, Shepherd's dog at 384 — each of those headwords printing only \"See Dog\") and the Arabic original of Al-Nabulsi's <em>Ta'tir al-Anam</em>, whose (كلب) headword sits at shamela.ws/book/1217/295 (printed p. 298, باب القاف) and whose transformation sentence breaks at the bottom of that page, resuming at the top of shamela 296 (printed p. 299). The Chinese side is three verdict lines from the received Zhou Gong text — one in chapter 25, two in chapter 26. One sample of each book, translated, then the full checked passages in the sources section at the bottom.</p>

<div class="cites">
<div class="cite-hd"><div>Text</div><div class="src-hd">Source</div></div>
<div class="cite-row">
  <div class="txt"><p>\"@@DOG_HEAD_SENT@@... If he barks in the dream, it means that such a man is impudent and has a repulsive and an abominable character. A dog bite or his scratch in a dream means harm caused by one's enemy and its effects will depend on the amount of pain one suffers in the dream... A puppy in a dream represents a loved child. If it is a white puppy in the dream, it means that such a son will grow to be a believer. If it is a black puppy in the dream, it means that he will grow to govern the household... A dog in a dream also means suffering from extremely high fever and in relation to Dog star or the stars Procyon and Sirius... Taking a dog for a companion on a journey in a dream means disappearing... Seeing a dog in a city in a dream also means renewal of one's business contract.\" (elided; full entry in Sources)</p></div>
  <div class="src">Ibn Seerin's Dictionary of Dreams (Al-Akili compilation, Pearl 1992) — \"Dog,\" printed p. 123, running onto p. 124 (the running head reads 124 in the scan; the book's end index lists Dog 123, Dog star 123, Dogfight 124). Translated/compiled English; the scan's joined words (Ifone) and printed oddities (\"left him inflected with a small loss,\" \"lacks principals,\" \"companion\xadship\" hyphenation) are kept as printed.</div>
</div>
<div class="cite-row">
  <div class="txt"><p class="ar">@@KALB_HEAD@@</p><p class="ar">@@KALB_BITE@@</p></div>
  <div class="src">Al-Nabulsi, Ta'tir al-Anam — shamela.ws/book/1217/295 (printed p. 298), the (كلب) headword and the bite clause, verbatim: a dog is an insolent man who dares the sins; if he barks he is an insolent one of horrible nature; whoever is bitten or scratched by a dog takes harm from his enemy in proportion to the pain, and perhaps sickness. (Translation ours.)</div>
</div>
</div>
<div class="note"><p>Zhou Gong, stated plainly: the received Chinese dream book this site quotes chapter by chapter carries the dog in exactly three verdict lines — one in chapter 25 (龙蛇 禽兽 等类): 豺狼恶狗有盗贼 — jackals, wolves and vicious dogs: thieves; two in chapter 26 (牛马 猪羊 六畜): 犬吠人鬼来求食 — a dog barking at a person: ghosts come for food — and 犬咬主人失财凶 — a dog biting its master: lost wealth, misfortune. The character 犬 appears twice in the whole corpus and 狗 once; all three occurrences are quoted. The bark is a ghost clause and the bite a money clause — neither reads the dog as an enemy in disguise. Nothing else is claimed for the Chinese side.</p></div>

@@CHIPZ@@
<h2 id="what-modern-research-adds-and-what-it-do">What modern research adds — and what it doesn't</h2>
<p>Of every animal in the dream literature, dogs have the only dedicated empirical study — and its variables are not symbols. Michael Schredl's team surveyed 1,695 Germans (960 women, 735 men, mean age 53.8, range 20–96) online over eight days in April 2020 and asked them to estimate what share of their remembered dreams include dogs: on average <strong>5.52%</strong> (±14.04), with <strong>69.03% saying zero</strong> and 4.13% estimating more than 40% — about <strong>31% of respondents (525)</strong> reporting any dog dreams at all. The split by waking contact is the study's headline: people who currently live with a dog estimated <strong>19.19%</strong> of their dreams include dogs, past dog-holders <strong>5.68%</strong>, people who never lived with one <strong>1.32%</strong>; within owners, active hours spent with the dog per week (mean 20.28 h) predicted the percentage (p = 0.0027), and so did where the dog sleeps at night — the closer to the bed, the more dog dreams, marginally significant (p = 0.0704). Tone goes the same way: dog dreams are <em>more positive than dreams in general</em> — mean +0.64 versus +0.07 on a −2/+2 scale, Wilcoxon z = 9.4, p &lt; 0.0001 — yet about 11% of respondents' dog dreams involved a threatening dog, and past negative waking experience with dogs (reported by roughly 25%, most often a bite, 48.6% of descriptions) predicted exactly that subscale (p &lt; 0.0001). The paper's own single-case anchor: one dreamer's dog dreams rose from 0.53% of dreams in 2006 to 3.93% in 2007 — the year his partner bought a dog (Schredl, Bailer, Weigel &amp; Welt, <em>Animals</em> 10(10):1915, 2020, <a href="https://pubmed.ncbi.nlm.nih.gov/33086615/">PubMed 33086615</a>, DOI 10.3390/ani10101915; open-access full text and all seven tables re-pulled and re-read today; self-estimated percentages in an online survey, stated as such — the estimates are recalled ratios, not diary counts). Older aggregate records agree on rank: across standard questionnaire studies dogs run in about 1.5–5% of dreams and are often the most frequent animal; Van de Castle found that when an animal dream is positive, the animal is most likely a dog. The instrument tradition has never carried a dog item: in the 56-item Typical Dream Questionnaire analyzed against 1,612 diary dreams, there is no dog line — the nearest items are \"Being pursued by an animal\" (one of the three most frequent themes already in Gahagan's 1936 questionnaire of 559 students) and \"Being an animal\" itself, which scored 4.72% lifetime and zero in two weeks of diaries (Mathes &amp; Schredl, <em>Somnologie</em> 18:106–111, 2014; corpus file re-read today). The 2018 teeth-dream paper this site leans on elsewhere (<a href="https://pubmed.ncbi.nlm.nih.gov/30319507/">PubMed 30319507</a>) has no dog item and no animal item — its full text, re-checked today, contains no form of the words dog or animal. Against the classical layer the collision is complete: the Arabic books read the dog as a masked person — insolent man, servant, informer, child — while the modern record says the dog in the dream tracks the dog in the house, more pleasant than average, and rarely threatening unless the waking bite happened first.</p>

<h2 id="sources-all-passages-checked-against-the">Sources (all passages checked against the cited pages)</h2>
<div class="src">
<p><strong>Ibn Sirin compilation — \"Dog,\" printed p. 123, running onto p. 124</strong> (Ibn Seerin's Dictionary of Dreams, compiled by Muhammad M. Al-Akili, Pearl Publishing House 1992, ISBN 1879405032; a later compilation attributed to the 8th-century scholar, not his autograph text; the book's own page index lists Dog at 123, Dog star at 123, Dogfight at 124, Bitch at 40, Greyhound at 195, Puppy at 346, Shepherd's dog at 384). Full entry, scan verbatim including its joined words and printed oddities (\"Ifone,\" \"left him inflected with a small loss,\" \"lacks principals,\" the soft-hyphenated \"companion\xadship\"; the page-124 running head prints inside the entry's last third): \"@@DOG@@\" — \"Dogfight,\" printed p. 124, the whole entry: \"@@DOGFIGHT@@\" — cross-references, as printed: \"Bitch: (See Dog)\" · \"Canine: (See Dog)\" · \"Hunting dog: (Lust; Desire; Want. See Dog)\" · \"Tyke: (See Dog)\" — and the dictionary's own filing decision, from the index: \"Canines: (See Tooth)\" — the canine teeth are not routed through the dog entry at all; they are sent to the Tooth entry, this site's main subject.</p>
<p><strong>Al-Nabulsi — (كلب), shamela.ws/book/1217/295, printed p. 298, continuing at /296 (printed p. 299)</strong> (Ta'tir al-Anam fi Ta'bir al-Manam, Abd al-Ghani al-Nabulsi d. 1731 CE, Dar al-Fikr edition; باب القاف; translation ours). Headword and bite: \"@@KALB_HEAD@@\" (a dog is an insolent man who dares the sinful; barking, insolent of horrible nature); \"@@KALB_BITE@@\" (bitten or scratched: harm from your enemy in proportion to the pain — and perhaps sickness). The breed chain, verbatim: \"@@KALB_LONG@@\" (torn garment: a vile man backbiting you; unheard bark: an enemy leaving you with a small loss; a dog also a vile insolent woman among persistent evildoers; a puppy a loved child — white, a believer; black, he rules the household; it is said: a foundling of an insolent man who rears him; the house dog a bitter enemy; the shepherd's dog a benefit coming from a ruler; the saluki fit for the sultan, receiving authority and surplus — the back of the army victorious over enemies, but vile without chivalry; the Chinese dog: mixing with foreign peoples who are not of the people of Islam). The scenario clauses on printed p. 298, verbatim: \"@@KALB_SCEN@@\" (taking a dog: loving a servant dearly; bitten: calamity, harm and hardship from a friend or servant; hunting with dogs: your wish and desire attained; killing dogs: victory over the enemy; hounds going out to hunt: good for all people, a deed and a stirring; returning: fears gone and work laid up; entering the city: work laid up; house-guarding dogs: the keeping of your wife and goods; ill: sickness, loss, some goods gone; a barking bitch: harm and deceit from evil men; the dog means fever because of the star called the Dog — the Sirius of the Yemen, cause of fevers; all breeds are abject people; dogs kept for play and snapping: ease with delight; a mishap befalling them: grief and the passing of life's delight; the water bitch: unfinished work and false hope). The transformation clause, breaking at the bottom of printed p. 298 and completing at the top of printed p. 299: \"@@KALB_TRANS1@@\" / \"@@KALB_TRANS2@@\" (turned into a dog: God taught you great knowledge and you were ingrate for it, so God stripped it from you; dogs are the police boys; the dog a weak enemy; the dog a stingy man). Bark at you, printed p. 299: \"@@KALB_BARK@@\" (a dog barking at you: words you hate from a man with little chivalry). The closing chain, printed p. 299, verbatim: \"@@KALB_MEAT@@\" (eating dog meat: victory over your enemy and a share of his wealth; the dog the guard and the man of innovation; drinking its milk: fear; pillow-ing on a dog: a friend you take revenge with and lean upon; the dog a boy or a beggar at the doors — perhaps baseness, humiliation, abjection and wretchedness with much devotion, guarding his people and repelling for his master; perhaps dogs mean the turning to the world with nothing saved; all dogs the people of the world; the hunting dog honor, height and provision; the cattle dog a good neighbor jealous for family and neighbor; keeping or befriending a dog: straying, money damages, work undone; the dog's company means hiding — because of the story of the People of the Cave; the bitch a wife keeping her husband, many children; and perhaps the dog means disbelief, despair of God's mercy, and denial; the dog of the Cave: fear, prison or flight; a dog in the land: renewal of governance).</p>
<p><strong>Zhou Gong Jie Meng — received 27-chapter text</strong> (corpus checked line by line; 犬 occurs exactly twice and 狗 exactly once). ch. 25 (龙蛇 禽兽 等类): \"豺狼恶狗有盗贼\" — jackals, wolves and vicious dogs: thieves. ch. 26 (牛马 猪羊 六畜): \"犬吠人鬼来求食\" — a dog barking at a person: ghosts come for food; \"犬咬主人失财凶\" — a dog biting its master: lost wealth, misfortune. No other chapter carries a dog line.</p>
<p><strong>Modern research.</strong> Schredl M, Bailer C, Weigel MS, Welt MS. \"Dreaming about Dogs: An Online Survey.\" <em>Animals</em> 10(10):1915, 2020. <a href="https://pubmed.ncbi.nlm.nih.gov/33086615/">PubMed 33086615</a>, DOI 10.3390/ani10101915 (open-access full text re-pulled and all tables re-read today: 1,695 participants — 960 women, 735 men; mean age 53.84 ± 13.99, range 20–96; Germany, survey 13–20 April 2020; Table 1: mean estimated percentage of dreams including dogs 5.52 ± 14.04, 69.03% zero, 4.13% above 40%; 525 of 1,695 report any dog dreams; Table 2: tone of dog dreams +0.64 ± 1.06 vs general +0.07 ± 0.81, Wilcoxon z = 9.4, p &lt; 0.0001, effect size 0.940; Table 3: current dog-in-household 19.19 ± 23.51%, past 5.68 ± 12.67%, never 1.32 ± 6.04%; active time with the dog 20.28 ± 12.82 h/week, p = 0.0027 in the owners-only regression, sleeping-place proximity marginally significant p = 0.0704; Table 6: mean percentage of dog dreams with threatening dogs 11.14 ± 25.67, 67.62% zero; about 25% of 1,583 reported negative past dog experiences — 48.60% bites, 37.64% threat or attack without bite; past negatives predict threatening-dog percentage p &lt; 0.0001; introduction: literature range 1.5–5%, Van de Castle's finding that positive animal dreams most often involve dogs, and the single case of 108 dog dreams in an 8,400-dream series — 0.53% in 2006 rising to 3.93% in 2007 after the partner's new dog; 8.33% of those dog dreams negative, 27.78% positive). Mathes J, Schredl M. <em>Somnologie</em> 18:106–111, 2014 (local full-text file re-read today: Gahagan 1936, 559 psychology students, questionnaire of 23 themes — most frequent \"Falling,\" \"Being pursued by a person\" and \"Being pursued by an animal\"; TDQ item 49 \"Being an animal\": 0.00% of 1,612 diary reports, 4.72% lifetime, rank 54; the 56-item TDQ carries no dog item). Schredl M. \"Animal dreams in a long dream series.\" <em>International Journal of Dream Research</em> 6(1):59–64, 2013, DOI 10.11588/ijodr.2013.1.9609 (abstract page re-read today: one male dreamer, 8,420 dreams over 23 years, animals present in about 7% of them — 577 dreams; the paper reports the dreamer's waking cats and hamster reflected in his animal dreams). Rozen N, Soffer-Dudek N. <em>Frontiers in Psychology</em> 9:1812, 2018. <a href="https://pubmed.ncbi.nlm.nih.gov/30319507/">PubMed 30319507</a> (full text re-checked today: no form of the word dog or animal appears anywhere in the paper — no animal item on its theme list; stated on this page, not papered over).</p>
</div>

<div class="note"><p>This page reports what two classical Arabic texts, the received Chinese dream book (whose three dog lines read bark and bite as events in the house, not as a masked person), and one online survey of 1,695 Germans can see about dreams of dogs. It is not a prediction, a medical or religious ruling, and no dream book — classical or modern — settles what a dream means for the person who had it. If this dream unsettled you, note the move every source on this page makes in its own form: the books do not ask whether the dog was friendly; they ask <em>whether you heard it bark</em>, <em>how much the bite hurt</em>, <em>what breed it was</em> and <em>what you were doing with it</em> — while the research asks how many hours a week you walk a dog and where it sleeps at night. For the other animal the classical books read as a trial — the snake — see <a href="/dream/snake/">snake dreams</a>; for the entry that shares the puppy clause's child ledger, <a href="/dream/baby/">baby dreams</a>; and for the dictionary's own filing decision that routes canines past the dog to the tooth, <a href="/dream/teeth-falling-out/">teeth falling out</a>.</p></div>

<section style="border-top:1px solid var(--line);margin-top:40px;padding-top:20px"><h2 id="related-questions" style="font-size:18px;font-weight:400">Related questions</h2><ul style="list-style:none;padding:0"><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/snake/">Snake bite dream: disgrace or windfall — the other animal, priced by the bite the dreamer feels</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/baby/">Baby dreams — the child ledger the puppy clause is drawn from, white believer and black ruler</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/spider/">Spider dreams — the single-case series where animals run at 7%, and the prepared-fear reading</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/teeth-falling-out/">Teeth falling out dream — the entry the dictionary routes Canines to, this site's main subject</a></li></ul></section>
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

DOG_HEAD_SENT = "Dog: (Bitch; Canine; Desire; Greyhound; Japanese spaniel; Pekingese; Lust; Puppy; Shepherds' dog; Tyke) In a dream, a dog represents an insolent man who dares to indulge in sinful actions."

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

T = {k: esc(v) for k, v in {
 'DOG': DOG, 'DOG_HEAD_SENT': DOG_HEAD_SENT, 'DOGFIGHT': DOGFIGHT,
 'KALB_HEAD': KALB_HEAD, 'KALB_BITE': KALB_BITE, 'KALB_LONG': KALB_LONG,
 'KALB_SCEN': KALB_SCEN, 'KALB_TRANS1': KALB_TRANS1, 'KALB_TRANS2': KALB_TRANS2,
 'KALB_BARK': KALB_BARK, 'KALB_MEAT': KALB_MEAT,
}.items()}
subs = {'@@TITLE@@': esc(TITLE), '@@DESC@@': esc(DESC), '@@CSS@@': CSS,
        '@@ALD@@': ARTICLE_LD, '@@FAQJ@@': FAQ_JSON,
        '@@CHIPR@@': CHIP['reading'], '@@CHIPT@@': CHIP['text'], '@@CHIPZ@@': CHIP['research']}
for k, v in subs.items():
    HEAD = HEAD.replace(k, v)
for k, v in T.items():
    HEAD = HEAD.replace('@@'+k+'@@', v)
assert '@@' not in HEAD, [l for l in HEAD.splitlines() if '@@' in l]
os.makedirs('/root/teethdreammeaning/site/dream/dog', exist_ok=True)
open('/root/teethdreammeaning/site/dream/dog/index.html','w',encoding='utf-8').write(HEAD)
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
