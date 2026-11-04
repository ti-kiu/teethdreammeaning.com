#!/usr/bin/env python3
"""Build site/dream/hair/index.html. All Arabic/English/Chinese quoted passages are
injected VERBATIM from source files already checked by tools/verify_hair.py (FAILS=0)."""
import re, os, json

def norm(s): return re.sub(r'\s+', ' ', s).strip()

en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en)
en = re.sub(r'\d+ IBN SEERIN\'?S', ' ', en)
en = norm(en)
# repair hyphen-split OCR words
en = re.sub(r'(\w)- (\w)', lambda m: (m.group(1)+m.group(2)) if (m.group(1).lower()+m.group(2).lower()) in (
 'distributing','participating') else m.group(0), en)
en = en.replace('distrib- uting','distributing').replace('Partici- pating','Participating')

ar192 = norm(open('/root/dream_research/nabulsi_page_192.txt', encoding='utf-8').read())
ar193 = norm(open('/root/dream_research/nabulsi_page_193.txt', encoding='utf-8').read())
zg = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()

def cut(src, start, end):
    i = src.find(start); assert i != -1, start[:50]
    j = src.find(end, i); assert j != -1, end[:50]
    return norm(src[i:j+len(end)])

HAIR   = cut(en, "Hair: In a dream, hair represents money and longevity.", "(See Black hair; Dye; Shaving; Strand of hair)")
HAIRCUT= cut(en, "Haircut: A short haircut", "(Also see Hair; Shaving)")
BRAID  = cut(en, "Braiding: (Hair; Intertwine; Plait)", "(Also see Hair)")
SHAVE  = cut(en, "Shaving: Shaving one's hair in a dream relates", "losing one's strength")
STAND  = cut(en, "Strand of hair: (Bun; Tuft; Wisp)", "something wrong she has committed")
AQI    = cut(en, "'Aqiqah rites: (Hair of a newborn;", "(Also see ~qiq canyons; Carnelian-red)")

k = ar192.find("(شعر الرأس)"); e192 = norm(ar192[k:].split("تحميل")[0].split("اذهب")[0])
assert e192.endswith("فليحذر أن يصير"), e192[-60:]
k2 = ar193.find("ومن رأى شعره صار كشعر الخنزير"); e193 = norm(ar193[k2:].split("اذهب")[0].split("تحميل")[0])
POEM = cut(ar192, "(شعر) من رأى أنه يقول الشعر", "الوسواس")

assert "If one's hair turns white in a dream" in HAIR
assert len(e192) > 800 and len(e193) > 800
for junk in ("اذهب","التشكيل","مسار الصفحة"):
    assert junk not in HAIR and junk not in e192 and junk not in e193

zg_lines = {
 "头白主长命大吉": "White hair on the head: long life, greatly auspicious.",
 "头秃发落皆凶事": "Baldness and hair falling out: all of it inauspicious.",
 "头须自落忧子孙": "Beard and moustache falling out on their own: worry about the descendants.",
 "头须再生主长命": "Beard and moustache growing back: long life.",
 "剪剃头发家内凶": "Cutting or shaving the hair: misfortune inside the household.",
 "露头披发阴人谋": "Head bared, hair loose: a secret plot against you.",
 "披头盖面官讼至": "Hair hanging over the face: a lawsuit arrives.",
 "眉与发齐禄位至": "Brows and hair level: salary and rank arrive.",
 "梳头洗面百忧去": "Combing the hair and washing the face: a hundred worries depart.",
 "妇人披头有私情": "A woman with loosened hair: a private affair.",
 "齿自落者父母凶 齿落更生子孙兴": "Teeth falling out on their own: misfortune to the parents; teeth falling and regrowing: the descendants thrive.",
}
for L in zg_lines: assert L in zg, L
ZGBLOCK = "  ·  ".join(f"{k} — \"{zg_lines[k]}\"" for k in zg_lines)

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

FAQ = [
 ("What does it mean to dream of hair falling out?",
  "Both classical Arabic books open the same way: hair in a dream means money and longevity (Ibn Sirin compilation, printed p. 198) - scalp hair stands for your property and your years. So shedding clauses are priced as losses, not as death omens: forearm hair scattering means you may lose all your savings; hair falling from the back of the head means humiliation; and Al-Nabulsi, clause for clause, says if the forearm hair scatters, all you have acquired goes away, and if it sheds, whatever your effort and labor earned is lost (shamela 193, printed p. 196)."),
 ("Is dreaming about losing hair a bad omen?",
  "The books condition it, the way they condition everything. Shedding reads as loss of money, rank or protection; but shaving during the pilgrimage season means safety and protection, cutting or plucking means paying debts and dispelling distress, and having less hair simply means diminishing difficulties. The one dark clause without a hedge is braiding: if a sick woman braids her hair, the compilation says she dies of her illness - and Al-Nabulsi adds that a woman plaited in three plaits is divorced three times, and if she is sick, she dies. Health decides which side of the same image applies."),
 ("What does the Chinese Zhou Gong book say about hair dreams?",
  "Chapter 3 of the received text runs verdict lines: baldness and hair falling out are all inauspicious, and cutting or shaving the hair brings misfortune inside the household. But on two specific images it flatly reverses the Arabic books: white hair on the head means long life, and a beard growing back means long life - while in the Ibn Sirin compilation, hair turning white means loss of money, and hair growing anew means losing most of your wealth."),
 ("Why do the two traditions disagree?",
  "The Arabic books treat hair as an asset - money, years, dependents - so growth is profit and loss is debt; the Zhou Gong book treats the head as a family ledger, so white and regrown hair, the signs that reverse aging, come out on the side of long life. Same image, two different accounts being audited: one is your property, one is your lineage."),
 ("What does modern research say about hair falling out?",
  "Medicine has one firm link and it runs the other direction: telogen effluvium is real stress-triggered shedding, seen 3-4 months after a triggering event (Malkud, J Clin Diagn Res 2015, PMID 26500992), and hair loss itself provokes distress out of proportion to its severity (Hadshiew et al., J Invest Dermatol 2004, PMID 15304082). But no published study we could find reports a prevalence figure for dreaming of hair falling out - the 2018 teeth-dream study (PubMed 30319507) measured teeth, falling, smothered and toilet themes only. That gap is reported here, not papered over."),
]
FAQ_JSON = json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ], ensure_ascii=False)

T = {}
T['HAIR_ENTRY'] = esc(HAIR)
T['HAIRCUT'] = esc(HAIRCUT)
T['BRAID'] = esc(BRAID)
T['SHAVE'] = esc(SHAVE)
T['STAND'] = esc(STAND)
T['AQI'] = esc(AQI)
T['E192'] = esc(e192)
T['E193'] = esc(e193)
T['POEM'] = esc(POEM)
T['ZGBLOCK'] = ZGBLOCK
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
<link rel="canonical" href="https://teethdreammeaning.com/dream/hair/">
<meta property="og:title" content="Dreaming of Hair Falling Out: What the Two Arabic Books Say">
<meta property="og:description" content="Hair dreams in Ibn Sirin and Al-Nabulsi: hair = money and longevity, shedding = lost savings, shaving = paid debts. Zhou Gong reads white hair as long life.">
<meta property="og:url" content="https://teethdreammeaning.com/dream/hair/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
<title>Dreaming of Hair Falling Out: What the Dream Books Say</title>
<meta name="description" content="Hair dreams in Ibn Sirin and Al-Nabulsi: hair = money and longevity, shedding = lost savings, shaving = paid debts. Zhou Gong reads white hair as long life.">
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
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Article", "author": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"}, "datePublished": "2026-11-04", "dateModified": "2026-11-04", "publisher": {"@type": "Organization", "name": "Teeth Dream Meaning", "url": "https://teethdreammeaning.com/"}, "headline": "Dreaming of Hair Falling Out: What the Two Arabic Books Actually Say", "url": "https://teethdreammeaning.com/dream/hair/", "inLanguage": "en", "about": {"@type": "Thing", "name": "dream interpretation"}}</script>
<script type="application/ld+json">@@FAQ_JSON@@</script>
</head>
<body>
<div class="wrap">
<nav class="top"><a href="/">Teeth Dream Meaning</a> · classical sources, checked page by page</nav>

<h1>Dreaming of Hair Falling Out: What It Means</h1>
<p class="lede">Dreaming of your hair falling out is read by both classical Arabic books as a dream about <strong>your money and your years, coming loose</strong>. The <em>Ibn Sirin</em> compilation opens the entry with a one-line ledger: "In a dream, hair represents money and longevity" (printed p. 198). Al-Nabulsi opens his entry with the identical line in Arabic. So when hair falls, the books do not read death — they read loss: forearm hair scattering means you may lose all your savings, hair falling from the back of the head means humiliation, and whatever sheds from your arms, your earned work goes away. Then the same entries carve exceptions: shaving during the pilgrimage season means safety, cutting or plucking means <em>paying your debts</em>, and having less hair means diminishing difficulties.</p>

<p>So the honest first answer is: <strong>in these books, a hair-loss dream is an asset report, not an omen of death.</strong> Growth and loss are graded like money in and money out — and the Chinese Zhou Gong book, reading the same head, flips two of the ledger entries: white hair and regrown hair, which the Arabic books price as loss of money and loss of wealth, mean <em>long life</em> in the Chinese text. The scenarios people actually dream are below: plain answers first, no Arabic or Chinese on this screen, every quote checked to its printed page.</p>

<div class="qa">
<h3>Your hair fell or scattered — the loss clauses</h3>
<p>The compilation is specific about <em>where</em> the hair falls. Forearm hair scattering or falling: "he may lose all his savings." Hair on the back of the head disheveled: humiliation — and Al-Nabulsi prices it twice on the same page: if the hair of your forearms scatters, all you have acquired goes away; if it sheds, whatever your effort and labor earned is gone and lost (printed p. 196). Hair shed from the right side of the head points at harm from male relatives, from the left side at female relatives — and if you have no kin, "he will suffer harm from his evil actions": the loss turns inward. None of these clauses is a death sentence on a person. They are loss-of-property sentences.</p>
</div>

<div class="qa">
<h3>You were braiding or plaiting your hair</h3>
<p>This is the entry's sharpest fork. For women, and for men accustomed to braiding, both books read it as good: benefits, saving or investing money, and in the compilation "mastering one's craft." For everyone else it means "complications in one's life, unbearable debts, or confusion." And then the dark clause, carried almost word for word by both books, one book each: if a <em>sick</em> woman sees herself braiding her hair, the compilation says she will die of her illness (printed p. 198); Al-Nabulsi says if a woman's hair is plaited in three plaits "she is divorced from her husband three times — and if she is ill, she dies" (printed p. 196). Health decides which side of the same image applies.</p>
</div>

<div class="qa">
<h3>You cut, shaved or plucked it</h3>
<p>The books ask you a question first: is this your custom? The Shaving entry (printed p. 382) is customs-dependent — a man used to short hair who shaves "will pay a fine as an atonement," shaving in summer brings benefit, in winter difficulty, and for someone depressed it means "an end to his trouble, or payment of his debts." The main entry agrees from the other side: shaving your head during the pilgrimage season "means safety and protection," and shortening your hair "means dispelling stress, or being coerced to pay one's debts" — paying, but under duress. Plucking is the same trade with the same sting: Al-Nabulsi reports the opinion that plucking hair indicates "the dreamer's payment of his debt — grudgingly" (printed p. 195). The Chinese book drops the calculus: cutting or shaving the hair, misfortune inside the household. One tradition's debt-cleanser is the other's household alarm.</p>
</div>

<div class="qa">
<h3>It turned white — or grew back</h3>
<p>Two images, and the traditions answer them in opposite directions. The compilation: "If one's hair turns white in a dream, it means loss of money for a rich person, or paying the debts of a poor person"; Al-Nabulsi reads short and white hair as the ugly state of whoever the hair stands for; and regrowth is worse than loss — "if one sees his hair growing anew in a dream, it means that he may lose most of his wealth" (Al-Nabulsi, identically: his money has gone or will go, all but a little). Zhou Gong chapter 3 reads the same two images as <em>years added</em>: white hair on the head means long life, greatly auspicious; a beard growing back means long life. The Arabic books audit your wallet; the Chinese book audits your lineage — and each marks the same sign to the opposite column.</p>
</div>

<div class="qa">
<h3>Your hair grew long or thick</h3>
<p>Growth is not simply good; the books grade it against custom and mood. Long hair worn with pleasure "is praiseworthy, especially for women" (Al-Nabulsi, printed p. 195). Straight hair turning curly means honor; curly turning straight means humiliation. But length beyond custom, walked in the street unashamed, means "debts, distress and inability to take care of one's family" — and Al-Nabulsi stacks three hedged opinions on the same image: long hair is long misery; or many children; or the fear and watchfulness of God, with worldly worry on top. Lice are double-edged too: hair infested with lice "means that he has a large family" — while delousing yourself "means discovering some of your own faults," and Al-Nabulsi carries the same clause: whoever delouses his head is shown some of his own defects.</p>
</div>

<div class="qa">
<h3>A pregnant woman, a newborn, a strand of hair</h3>
<p>The smallest hair images get the most specific readings. The Strand of hair entry (printed p. 415): a pregnant woman seeing a strand of hair "will beget a blessed son"; a strand hanging over one's head means money; several tufts carried represent one's neighbors; a woman's long strand means her son becomes a leader. A hairy child "means longevity," and a beardless man growing hair means his wife will soon be pregnant. And the compilation keeps a whole ritual entry, 'Aqiqah rites (printed p. 15) — the newborn's hair shaved on the seventh day and weighed, gold or silver given in charity against its weight: the ceremony in a dream "represents glad tidings, the arrival of a long awaited person, recovering from an illness, or the release of a prisoner." Hair as money, weighed out: the entry is the ledger, one last time.</p>
</div>

<h2>The finding: the same ledger, three reversals</h2>
<p>Set the compilation's English and Al-Nabulsi's Arabic side by side and the Hair entry mirrors itself clause by clause, a thousand years apart: hair = money and longevity; the rich man's bun means more wealth, the poor man's bun means debts; straight turning curly is honor and curly turning straight is humiliation; the curly head crowns your superior; a sick woman braiding dies; hair long enough to plait with the beard means debts; shave the moustache or the armpit and you pay debts and end distress; cut during the pilgrimage and you are safe; pluck and you pay, grudgingly; hair like a horse's means a thief is caught; like a hog's, major calamities; the unhappy man made hairy is unhappier, the happy man made hairier is happier; black hair is the husband's love; a woman's loosened hair is a husband's absence — uncovered and staying uncovered, he never returns, or she never marries; people staring at her hair is slander; horns of hair are might; the right side shed is harm from his male kin, the left from the female; less hair is less difficulty; someone pulling your hair is a financial disaster; a woman's cut strand is a fight with her husband or a rival urging him to other women; combing her hair may be divorce, nice combing is loyalty; regrowth is lost wealth; face-hair is debt; palm-hair is business profit; forearm shed is lost savings; leg-hair twisted is money earned against the grain; white hair is loss for the rich and debt paid for the poor; a hairy child is long life. Both books carry all of it, in the same order — this is the same machine the teeth pages run on the same head.</p>

<p>The reversals are the three things no summary quotes. <strong>One:</strong> Al-Nabulsi keeps the headword (شعر) for <em>poetry</em> on the same page as the hair entry — "poetry in a dream is vain speech," and the poet is a man "who says what he does not do" — hair and verse share the Arabic word and none of the verdict. <strong>Two:</strong> regrowth is <em>worse</em> than loss in the Arabic books — losing most of your wealth is read from hair growing anew — while the Chinese book reads regrowth as long life. <strong>Three:</strong> the death clauses are locked to the dreamer's health, not to the image: braiding is benefit, full stop — unless you are sick, and then both books, in their own languages, say you die. The books are not predicting; they are taking a medical history in the language of property. That is exactly the move the teeth pages make — death readings only under conditions (teeth lost and not found), health clauses excepted — which is why this site keeps linking the two families.</p>

<h2>The entries, briefly</h2>
<p class="src">The Arabic side comes from two books: the compiled English dictionary attributed to Ibn Sirin (Pearl Publishing House, 1992 — "Hair" entry printed p. 198 per the book's own end-of-volume index, which also locates Braiding at 54, Haircut and Hairdresser at 200, Shaving at 382 and Strand of hair at 415; the 'Aqiqah rites entry sits under the running head of printed p. 15 and is not carried in the index) and the Arabic original of Al-Nabulsi's <em>Ta'tir al-Anam</em>, whose (شعر الرأس) headword sits at shamela.ws/book/1217/192 (printed p. 195, باب الشين) and runs across to shamela.ws/book/1217/193 (printed p. 196). The Chinese side is one chapter of verdict lines: the received Zhou Gong book, ch. 3 (body, face, teeth and hair). One sample of each book, translated, then the full checked passages are in the sources section at the bottom.</p>

<blockquote>
<p>"Hair: In a dream, hair represents money and longevity... If one sees his hair growing anew in a dream, it means that he may lose most of his wealth... If one's hair turns white in a dream, it means loss of money for a rich person, or paying the debts of a poor person."</p>
</blockquote>
<p class="loc">Ibn Seerin's Dictionary of Dreams (Al-Akili compilation, Pearl 1992) — "Hair," printed p. 198. Translated/compiled English.</p>

<blockquote dir="rtl" lang="ar">
<p>(شعر الرأس) هو في المنام مال وطول عمر فمن رأى أن شعر رأسه طال فإنه يطول عمره</p>
</blockquote>
<p class="loc">Al-Nabulsi, Ta'tir al-Anam — shamela.ws/book/1217/192 (printed p. 195), the headword line, verbatim: scalp hair in a dream is money and length of life — whoever sees his head-hair grown long, his life is lengthened.</p>

<blockquote dir="rtl" lang="ar">
<p>وإذا ضفر شعر المرأة ثلاثة قرون طلقت من زوجها ثلاثاً وإن كانت مريضة ماتت</p>
</blockquote>
<p class="loc">Same book — shamela.ws/book/1217/193 (printed p. 196), the three-plaits clause, verbatim: if a woman's hair is plaited in three plaits she is divorced from her husband three times — and if she is sick, she dies.</p>

<div class="note"><p>Zhou Gong, stated plainly: the received Chinese dream book has no clause machine for hair — chapter 3 is a run of four-character verdicts (baldness and hair falling out: all inauspicious; beard falling out: worry for the descendants; beard regrown: long life; white head-hair: long life; hair cut or shaved: misfortune in the household; brows and hair level: rank arrives; combing the hair and washing the face: a hundred worries depart). All are quoted at chapter location in the sources section; nothing else is claimed for the Chinese side.</p></div>

<h2>What modern research adds — and what it doesn't</h2>
<p>Start with the honest absence: we found no published study reporting how common hair-falling dreams are. The nearest thing the empirical dream literature has to a checklist is the 2018 teeth-dream study (Rozen & Soffer-Dudek, <em>Frontiers in Psychology</em> 9:1812, PubMed 30319507), and its battery — re-extracted today — measured a fixed list only: teeth dreams, falling dreams, dreams of being smothered, toilet dreams, psychological distress, teeth grinding, teeth tension, sleep quality, general sleep disturbances. Hair was never one of them. What medicine does say is one firm causal chain, and it runs the opposite way from every folk reading: real stress-triggered shedding exists, called telogen effluvium, described by Kligman in 1961 and the most common cause of diffuse hair loss; shedding is seen 3-4 months <em>after</em> the triggering event, and "the observation of increased telogen hair shedding does not infer a cause" (Malkud, <em>J Clin Diagn Res</em> 9(9):WE01-3, 2015, PMID 26500992). The 2021 review is blunter still: the mechanisms by which physiological stress influences the human hair cycle "is unknown," and there are no targeted treatments (Chien Yin, Lee & Wang, <em>J Dermatol Sci</em> 101(3):156-163, 2021, PMID 33541773). And the distress loop is measured: hair loss "provokes anxieties and distress more profound than its objective severity would appear to justify" (Hadshiew, Foitzik, Arck & Paus, <em>J Invest Dermatol</em> 123(3):455-457, 2004, PMID 15304082) — the clinical shape of the worry this page's folklore feeds. One animal result now backs the oldest version of the belief, that stress grays hair: in mice, acute stress empties the follicle's pigment stem cells through sympathetic-nerve release of noradrenaline, and the depletion is permanent (Zhang et al., <em>Nature</em> 577(7792):676-681, 2020, PMID 31969699; mouse melanocyte stem cells, not human dreams — the page says so on purpose). So: medicine confirms stress moves hair, with a months-long lag and an unsettled mechanism; the classical books confirm hair moves assets, with verdicts that depend on your health. Neither layer, as published, has anything to say about what tomorrow brings.</p>

<h2>Sources (all passages checked against the cited pages)</h2>
<div class="src">
<p><strong>Ibn Sirin compilation — "Hair" entry, printed p. 198</strong> (Ibn Seerin's Dictionary of Dreams, compiled by Muhammad M. Al-Akili, Pearl Publishing House 1992, ISBN 1879405032; a later compilation attributed to the 8th-century scholar, not his autograph text; the book's own page index lists Hair at 198; OCR running-heads and mid-word line breaks removed, wording otherwise as printed): "@@HAIR_ENTRY@@"</p>
<p><strong>Same compilation, related hair entries</strong> (headwords and pages per the volume's own index): "@@BRAID@@" (Braiding, printed p. 54) — "@@SHAVE@@" (Shaving, printed p. 382) — "@@STAND@@" (Strand of hair, printed p. 415) — "@@HAIRCUT@@" (Haircut, printed p. 200) — "@@AQI@@" ('Aqiqah rites, printed p. 15 per the running head; the headword is not carried in the volume's page index).</p>
<p><strong>Al-Nabulsi — (شعر الرأس), shamela.ws/book/1217/192, printed p. 195</strong> (Ta'tir al-Anam fi Ta'bir al-Manam, Abd al-Ghani al-Nabulsi d. 1731 CE, Dar al-Fikr edition; باب الشين; text verbatim from the shamela page): @@E192@@</p>
<p><strong>Al-Nabulsi — (شعر الرأس) continued, shamela.ws/book/1217/193, printed p. 196</strong>: @@E193@@</p>
<p><strong>Al-Nabulsi — (شعر) as poetry, shamela.ws/book/1217/192, printed p. 195</strong>: @@POEM@@ — poetry in a dream is vain speech; whoever composes it to earn a living testifies to falsehood; memorizing verse may mean the passing of office and the shortening of religion; obscene lampooning is accusation, praise-poverty for the rich; broken meter marks a man who babbles, or into whom whispering enters. The hair entry and the poetry entry sit on the same page under different headwords — the shared word is the coinage of this book, not of this reading.</p>
<p><strong>Zhou Gong Jie Meng — ch. 3 身体 面目 齿发</strong> (received recension, our corpus file, verbatim): @@ZGBLOCK@@. The chapter's teeth pair is quoted too because the same chapter governs both symbol families on this site: fallen teeth mean misfortune to the parents, regrown teeth the thriving of the descendants — the Chinese ledger runs on the head's two hard tissues at once.</p>
<p><strong>Modern research.</strong> Malkud S. "Telogen Effluvium: A Review." <em>J Clin Diagn Res</em> 9(9):WE01-3, 2015. PMID 26500992 (PubMed abstract re-extracted today: "Telogen effluvium was first described by Kligman in 1961. It is the most common cause of diffuse hair loss... Diffuse shedding of telogen hair are seen after 3-4 months of triggering event. The observation of increased telogen hair shedding does not infer a cause."). Chien Yin G, Lee JSS, Wang ECE. "Telogen Effluvium — a review of the science and current obstacles." <em>J Dermatol Sci</em> 101(3):156-163, 2021. PMID 33541773, DOI 10.1016/j.jdermsci.2021.01.007 (abstract: "usually precipitated by physiological stress such as childbirth or sudden weight loss... the mechanisms through which physiological stress influences the human hair cycle is unknown, and there are no targeted treatments"). Hadshiew IM, Foitzik K, Arck PC, Paus R. "Burden of hair loss: stress and the underestimated psychosocial impact of telogen effluvium and androgenetic alopecia." <em>J Invest Dermatol</em> 123(3):455-457, 2004. PMID 15304082, DOI 10.1111/j.0022-202X.2004.23237.x (abstract: "provokes anxieties and distress more profound than its objective severity would appear to justify... in vivo studies in mice have substantiated the long-held popular belief that stress can exert profound hair growth-inhibitory catagen-inducing and hair-damaging pro-inflammatory effects"). Zhang B, Ma S, Rachmin I, et al. "Hyperactivation of sympathetic nerves drives depletion of melanocyte stem cells." <em>Nature</em> 577(7792):676-681, 2020. PMID 31969699, DOI 10.1038/s41586-020-1935-3 (abstract, mice: stress-induced greying via sympathetic-nerve noradrenaline burst; melanocyte stem cells "proliferate rapidly, and is followed by their differentiation, migration and permanent depletion from the niche"). Rozen & Soffer-Dudek. "Teeth Dreams, Wake-Time Dental Irritation, and Psychological Distress." <em>Frontiers in Psychology</em> 9:1812, 2018. PubMed 30319507 (full text re-extracted today: the measured-variable list above is Table 1's own caption; the word "hair" does not occur in the article). No study we could locate reports a prevalence figure for hair-falling dreams — the absence is stated here on purpose.</p>
</div>

<div class="note"><p>This page reports what two classical texts and one Chinese tradition record say about dreams of hair, and what published research can see. It is not a prediction, a medical, financial or religious ruling, and no dream book — classical or modern — settles what a dream means for the person who had it. If this dream unsettled you, note the one move every tradition here makes in its own form: the hair is judged by the state of the head it is on — health, custom, season — not by the strands themselves. Sudden real-world shedding that lasts is a dermatology visit, not an interpretation.</p></div>

<section style="border-top:1px solid var(--line);margin-top:40px;padding-top:20px"><h2 style="font-size:18px;font-weight:400">Related questions</h2><ul style="list-style:none;padding:0"><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/teeth-falling-out/">Teeth falling out dream — the same head, the same money-and-years ledger</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/teeth-dreams-and-stress/">Teeth dreams and stress — what the 2018 study actually measured</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/gold/">Dreaming of gold — the newborn's hair weighed against it, in the compilation's own entry</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/dead-person-resurrected/">A dead person coming back to life — the health-conditioned reads, same mechanism</a></li><li style="padding:8px 0;border-bottom:1px solid var(--line)"><a href="/dream/teeth-three-traditions/">How three traditions read the same dream — the comparison hub</a></li></ul></section>
<footer>
<p>Teeth Dream Meaning · <a href="/">Home</a> · <a href="/dream/gold/">Gold dream</a> · <a href="/disclaimer/">Disclaimer</a></p>
</footer>
</div>
</body>
</html>
"""

for key, val in T.items():
    PAGE = PAGE.replace('@@%s@@' % key, val)
assert '@@' not in PAGE

out = '/root/teethdreammeaning/site/dream/hair/index.html'
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(PAGE)
print('written', out, len(PAGE), 'bytes')
print('div', PAGE.count('<div'), PAGE.count('</div>'))
print('blockquote', PAGE.count('<blockquote'), PAGE.count('</blockquote>'))
print('p', PAGE.count('<p>'), PAGE.count('</p>'))
print('section', PAGE.count('<section'), PAGE.count('</section>'))
print('h2', PAGE.count('<h2'), )
