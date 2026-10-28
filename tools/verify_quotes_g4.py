import re
src = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
ibn = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()
norm = re.sub(r'\s+', ' ', ibn)
ar_checks = [
    "أن أسنانه العليا سقطت في يده فهو مال يصير إليه وإن سقطت في حجره فهو ولد ذكر وإن سقطت إلى الأرض فهي مصيبة الموت",
    "أن أسنانه السفلى سقطت فإنه يصيب وجعاً وألماً وهماً وغماً",
    "أن أسنانه تسقط وهو يأخذها بيده أو بلحيته أو في حجره فإن ذلك يدل على أن أولاده تنقطع ولا يولد له",
    "ومن رآها سقطت بكفه من غير ألم ولا معالجة فإنها دراهم على عددها",
    "وإن رأى أن ثنية سقطت في يده أو صرها في ثوبه فإنه يستفيد ولداً أو أخاً أو أختاً",
    "وتدل الأسنان على الودائع والأسرار",
]
en_checks = [
    "If the upper\nteeth fall into one's hand in the dream, they represent profits",
    "Ifthey fall in his\nlap in the dream, they mean a son",
    "if they fall on the floor in the dream, they\nmeans death",
    "If the lower teeth fall in the dream, they mean pain, sufferings,\nsorrows and distress",
    "Collecting one's lost teeth\nin a dream means longevity, or it could mean having a large progeny",
    "Ifone collects\nhis fallen teeth in a dream, it also means that he can no longer conceive children",
]
ok = True
for c in ar_checks:
    hit = c in src
    ok &= hit
    print('AR', 'OK ' if hit else 'MISS', c[:60])
def norm_src(t):
    return re.sub(r'\s+', ' ', t)
for c in en_checks:
    hit = norm_src(c) in norm
    ok &= hit
    print('EN', 'OK ' if hit else 'MISS', c[:60].replace('\n',' '))
h = open('/root/teethdreammeaning/site/dream/teeth-falling-into-hand-lap-ground/index.html', encoding='utf-8').read()
print('DIV', h.count('<div'), h.count('</div>'), 'BQ', h.count('<blockquote>'), h.count('</blockquote>'), 'P', h.count('<p'), h.count('</p>'))
print('CJK:', bool(re.search(r'[\u4e00-\u9fff]', h)))
print('ALL QUOTES VERIFIED' if ok else 'QUOTE FAILURE — DO NOT SHIP')
