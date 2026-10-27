import re
src = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
ibn = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()
norm = re.sub(r'\s+', ' ', ibn)
ar_checks = [
    "ومقاديم الأسنان إذا سقطت فإن كان مع وجع أو خروج دم أو لحم فإنه يبطل أو يفسد الأمر الذي يريده",
    "فإن سقط من غير وجع فإنه يذهب ما يملكه",
    "وإن رأى أنها تسقط مع وجع فإنه يدل على ذهاب شيء مما في منزله",
    "وإن كان هناك دم فإن ذلك إثم القطيعة للرحم إلا أن يكون عليه دين فإنه يطالب به ويعالج على قضائه",
    "وسقوط السن الواحدة إن كان من غير معالجة وأخذها بيده أو صرها في ثوبه فإن كان عنده حامل جاءه ولد وإلا صالح أخاً أو قريباً كان قد قاطعه",
    "أن أسنانه السفلى سقطت فإنه يصيب وجعاً وألماً وهماً وغماً",
]
en_checks = [
    "If the front teeth fall and cause pain and bleeding in the dream, they represent one's incompetence or inability to complete a project",
    "If the front teeth fall without pain or bleeding in the dream, then they mean losing one's property",
    "If his gums bleed, it means that he will forsake his family, except ifhe owed someone money, then it means that he will be asked to pay",
    "the lower teeth fall in the dream, they mean pain, sufferings, sorrows and distress",
    "if his gums bleed in the dream, it means that he will become free from his sins",
]
ok = True
for c in ar_checks:
    hit = c in src
    ok &= hit
    print('AR', 'OK ' if hit else 'MISS', c[:60])
for c in en_checks:
    hit = c in norm
    ok &= hit
    print('EN', 'OK ' if hit else 'MISS', c[:60])
h = open('/root/teethdreammeaning/site/dream/teeth-falling-out-with-blood/index.html', encoding='utf-8').read()
print('DIV', h.count('<div'), h.count('</div>'), 'BQ', h.count('<blockquote>'), h.count('</blockquote>'), 'P', h.count('<p'), h.count('</p>'))
print('CJK:', bool(re.search(r'[\u4e00-\u9fff]', h)))
print('ALL QUOTES VERIFIED' if ok else 'QUOTE FAILURE — DO NOT SHIP')
