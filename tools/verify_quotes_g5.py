import re
src = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
ibn = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()
norm = re.sub(r'\s+', ' ', ibn)

ar = [
 "أن أسنانه السفلى سقطت",
 "فإنه يصيب وجعاً وألماً وهماً وغماً",
 "وإن تساقطت أسنانه بلا وجع",
 "فإن ذلك يدل على أعمال تبطل",
 "وإن رأى أنها تسقط مع وجع",
 "فإنه يدل على ذهاب شيء مما في منزله",
 "فإن تحرك منها سن",
 "فمرض فإن سقطت أو ضاعت",
 "وقيل من سقطت أسنانه",
 "تسع وعشرون سنة أو ثلاثون سنة",
 "أسنانه سقطت وتعذر عليه الأكل",
 "فإنه يفتقر",
 "دالة على منتهى الأجل",
]
ok = True
for c in ar:
    hit = c in src
    ok &= hit
    print('AR', 'OK ' if hit else 'MISS', c)

en = [
 "Falling teeth in a dream means longevity, or living past one's contemporaries",
 "If the lower teeth fall in the dream, they mean pain, sufferings, sorrows and distress",
 "If one's teeth fall without pain or a cause in the dream, then they represent worthless deeds",
 "If they fall because of a gum disease or cause pain in the dream, then they mean being forced to part with something from one's house",
 "Falling teeth in a dream also denote a long illness that may not necessarily culminate in death",
 "If a tooth moves in its place in the dream, it means an illness",
 "Teeth in a dream represent one's identity, age, clan",
]
for c in en:
    hit = c in norm
    ok &= hit
    print('EN', 'OK ' if hit else 'MISS', c)

extra_en = [
 "If one loses his teeth and finds himself unable to eat properly in the dream, it also means poverty",
 "(Acrimony; Dice; Grasping; Longevity; Migration) Falling teeth in a dream",
 "Falling teeth in a dream also denote a long illness that may not necessarily culminate in death",
 "Grinding: (See Extracting oils from seeds; Hand mill; Mill; Miller)",
]
for c in extra_en:
    hit = c in norm
    ok &= hit
    print('EN+', 'OK ' if hit else 'MISS', c[:60])

print('ALL QUOTES VERIFIED' if ok else 'QUOTE FAILURE — FIX BEFORE WRITING PAGE')
