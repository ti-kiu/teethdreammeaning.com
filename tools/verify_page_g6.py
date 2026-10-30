import re
src = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
ibn = re.sub(r'\s+', ' ', open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
pmcn = re.sub(r'\s+', ' ', open('/root/.hermes/cache/web/pmc.ncbi.nlm.nih.gov-3f3efc6b2c.md', encoding='utf-8').read().replace('_',''))
page = open('/root/teethdreammeaning/site/dream/teeth-falling-out-good-or-bad-omen/index.html', encoding='utf-8').read()

def fuzz(text, corpus):
    # allow optional hyphen/space artifacts from PDF scans between words
    pat = r'\s*[-\u00ad]?\s*'.join(re.escape(w) for w in text.split(' '))
    return re.search(pat, corpus)

# Arabic fragments asserted as "checked verbatim" on the page
ar = [
 "فإن أهل بيته يموتون قبله وربما كان ذلك موت ذوي سنه أو مرض أهل بيته",
 "فإن تساقطت جميع الأسنان فإنه يهلك جميع من في ذلك المنزل والأصحاب والأحرار والمسافرون وتدل هذه الرؤيا منهم على مرض طويل من غير أن يموتوا وتدل في العبيد على العتق والتجار والمسافرين على خفة حملهم",
 "فإن أمسكها ولم يدفنها فإنه يستفيد بدلها",
 "فإن دفنها فإنه موت ذلك القريب",
 "فإن ذلك يدل على أنه يقضي دينه",
 "دراهم على عددها",
 "سقطت بكفه من غير ألم ولا معالجة",
 "أن أسنانه العليا سقطت في يده فهو مال يصير إليه",
 "وقيل",
 "عائق يعوقه",
 "دليل على قضاء الديون",
 "لزوم الصوم",
]
ok = True
for c in ar:
    hit = c in src
    ok &= hit
    print('AR', 'OK ' if hit else 'MISS', c[:60])

# English quotes as printed on the page (after restoring the two artifacts the page itself flags)
en = [
 "The entire family of my master will perish",
 "The dream of my master, the prince of the believers, is true, for he shall live the longest amongst his relatives",
 "In this case, both interpreters gave the same meaning, though the presentation is different",
 "If your dream is true, it means that all your relatives will die before you",
 "Falling teeth in a dream means longevity, or living past one's contemporaries",
 "If one cannot find his teeth in the dream, it means that his family will die before him, or that a member of his clan will emigrate to a new land",
 "If one finds a lost tooth in a dream, it means the return of an immigrant to his homeland",
 "If one saves his lost tooth and does not bury it in the dream, it means that someone will come forth and be to him as good as that relative",
 "If the upper teeth fall into one's hand in the dream, they represent profits",
 "Falling teeth in a dream also mean paying one's debts",
]
for c in en:
    hit = fuzz(c, ibn) is not None
    ok &= hit
    print('EN', 'OK ' if hit else 'MISS', c[:60])

l2 = [
 "one of the most common and universal typical dream themes, yet their source remains unknown",
 "incompatible with the",
 "the earliest documented interpretation was given in Ancient Greece by Artemidorus",
 "he related losing teeth in a dream to the payment of debts",
 "a prophecy for the impending death of a family member",
 "The connection between TD and death was a common belief for many years",
 "reacted to with irony",
 "the fear of growing older",
 "support the dental irritation hypothesis and do not support the symbolic hypothesis",
 "0.21 (0.07, 0.33)",
 "0.06 (-0.07, 0.20), ns",
 "0.02 (-0.11, 0.16), ns",
 "39.0% of respondents reported that they had experienced teeth dreams (TD) at least once, 16.2% reported that their TD were recurrent, and 8.2% reported that their TD were regular",
 "Conversely, TD were unrelated to psychological distress, whereas other dream types were (specifically, dreams of being smothered and dreams of falling)",
]
for c in l2:
    hit = fuzz(c, pmcn) is not None
    ok &= hit
    print('L2', 'OK ' if hit else 'MISS', c[:60])

# structure
import collections
for tag in ['div','blockquote','p','h2','h3','footer','ul','li','nav']:
    o = len(re.findall(r'<%s[ >]' % tag, page)); c = len(re.findall(r'</%s>' % tag, page))
    print('TAG', tag, o, c, 'OK' if o==c else 'MISMATCH'); ok &= (o==c)
# Chinese check
cjk = re.findall(r'[\u4e00-\u9fff]', page)
print('CJK chars:', len(cjk))
ok &= len(cjk)==0
# p<0.005 assertion vs paper: paper text says "p < 0.005" for TD-tension
m = fuzz('with a small-to-medium effect size', pmcn)
print('effect-size ctx:', bool(m))
print('ALL PAGE QUOTES VERIFIED' if ok else 'PAGE QUOTE FAILURE')
