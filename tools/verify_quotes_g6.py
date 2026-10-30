import re
src = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
ibn = re.sub(r'\s+', ' ', open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
pmc = open('/root/.hermes/cache/web/pmc.ncbi.nlm.nih.gov-3f3efc6b2c.md', encoding='utf-8').read()
pmcn = re.sub(r'\s+', ' ', pmc.replace('_', ''))

ar = [
 "فإن تساقطت جميع الأسنان فإنه يهلك جميع من في ذلك المنزل والأصحاب والأحرار والمسافرون",
 "وتدل هذه الرؤيا منهم على مرض طويل من غير أن يموتوا",
 "وتدل في العبيد على العتق والتجار والمسافرين على خفة حملهم",
 "سقوط أسنانه دل على مضرة لبعض أصدقائه",
 "وقيل إن سقوط الأسنان يدل على عائق يعوقه عما يريده",
 "وقيل هو دليل على قضاء الديون",
 "لأرباب المجاهدات على لزوم الصوم",
 "فإنها دراهم على عددها",
 "فإن أمسكها ولم يدفنها فإنه يستفيد بدلها",
 "فإن دفنها فإنه موت ذلك القريب",
 "فإن أهل بيته يموتون قبله",
 "وربما كان ذلك موت ذوي سنه أو مرض أهل بيته",
 "فإن ذلك يدل على أنه يقضي دينه",
]
ok = True
for c in ar:
    hit = c in src
    ok &= hit
    print('AR', 'OK ' if hit else 'MISS', c)

en = [
 "Falling teeth in a dream means longevity, or living past one's contemporaries",
 "Collecting one's lost teeth in a dream means longevity, or it could mean having a large progeny",
 "cannot find his teeth in the dream, it means that his family will die before him, or that a member of his clan will emigrate to a new land",
 "If the upper teeth fall into one's hand in the dream, they represent profits",
 "If one saves his lost tooth and does not bury it in the dream, it means that someone will come forth and be to him as good as that relative",
 "ifhe does bury it, then it means the death of his relative",
 "The entire family of my master will perish",
 "for he shall live the longest amongst his relatives",
 "both interpreters gave the same meaning, though the presentation is different",
 "If your dream is true, it means that all your relatives will die before you",
 "Falling teeth in a dream also mean paying one's debts",
 "denote a long illness that may not necessarily culminate in death",
 "assiduous in his devotion, and votive fasting will surely help him as a start",
]
for c in en:
    hit = c in ibn
    ok &= hit
    print('EN', 'OK ' if hit else 'MISS', c[:70])

# English fragments spanning hyphenated line breaks in the PDF scan: allow single-space split-hyphen join
for c in en:
    if c not in ibn:
        words = c.split(' ')
        # try reconstructing with optional hyphen+newline pattern
        pat = r'\s*[-]?\s*'.join(re.escape(w) for w in words)
        m = re.search(pat, ibn)
        print('EN-FUZZY', 'HIT' if m else 'MISS', c[:50])

l2 = [
 "one of the most common and universal typical dream themes, yet their source remains unknown",
 "the earliest documented interpretation was given in Ancient Greece by Artemidorus",
 "he related losing teeth in a dream to the payment of debts",
 "in the Jewish Talmud, TD were construed as a prophecy for the impending death of a family member",
 "Freud (1900)",
 "reacted to with irony",
 "a more recent interpretation of TD as the fear of growing older",
 "the present findings support the dental irritation hypothesis and do not support the symbolic hypothesis regarding the origins of TD",
 "r = 0.21 (0.07, 0.33)",
 "r = 0.06 (-0.07, 0.20), ns",
 "r = 0.02 (-0.11, 0.16), ns",
 "39.0% of respondents reported that they had experienced teeth dreams (TD) at least once, 16.2% reported that their TD were recurrent, and 8.2% reported that their TD were regular",
 "depicted as a manifestation of distress",
]
for c in l2:
    hit = c in pmc or c in pmcn
    ok &= hit
    print('L2', 'OK ' if hit else 'MISS', c[:70])

# find the sentence stating distress correlated with falling/smothered dreams
m = re.search(r'[^.]*dreams of being smothered and dreams of falling[^.]*\.', pmcn)
print('L2-CTX:', m.group(0) if m else 'NOT FOUND')

print('ALL QUOTES VERIFIED' if ok else 'QUOTE FAILURE — FIX BEFORE WRITING PAGE')
