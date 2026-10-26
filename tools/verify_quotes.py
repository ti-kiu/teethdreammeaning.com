import re
src=open('/root/dream_research/shamela_177.txt',encoding='utf-8').read()
ibn=open('/root/dream_research/ibn_sirin_full.txt',encoding='utf-8').read()
ar_checks=[
"وإن كان عليه دين إذا سقطت أسنانه في المنام فإن ذلك يدل على أنه يقضي دينه",
"وإن رأى أن سناً واحدة من أسنانه سقطت فإنه يقضي رجلاً واحداً دينه أو يقضي الكل في دفعة واحدة",
"وإن سقطت أسنانه فإنه يقضي عدة من غرمائه أو يقضي أحداً منهم أشياء كثيرة",
"وإن تساقطت أسنانه بلا وجع فإن ذلك يدل على أعمال تبطل",
"فإن تساقطت جميع الأسنان فإنه يهلك جميع من في ذلك المنزل والأصحاب والأحرار والمسافرون",
"وتدل في العبيد على العتق والتجار والمسافرين على خفة حملهم",
"أن أسنانه تسقط وهو يأخذها بيده أو بلحيته أو في حجره فإن ذلك يدل على أن أولاده تنقطع ولا يولد له",
"وإن رأى جميع أسنانه سقطت وصارت في يده أو عنده فإنه يكثر نسل أهل ذلك البيت وعددهم",
"فإن كان مع وجع أو خروج دم أو لحم فإنه يبطل أو يفسد الأمر الذي يريده",
"وإن رأى أن ثنية سقطت في يده أو صرها في ثوبه فإنه يستفيد ولداً أو أخاً أو أختاً",
"وإن كان هناك دم فإن ذلك إثم القطيعة للرحم إلا أن يكون عليه دين",
"وقيل من سقطت أسنانه فقد بقي من عمره تسع وعشرون سنة أو ثلاثون سنة",
"وقيل يموت إلى ثلاثين يوماً أو يغرم ثلاثين ديناراً",
"على قدر دية السن في الشرع",
"ومقاديم الأسنان إذا سقطت",
]
for c in ar_checks:
    print('AR', 'OK ' if c in src else 'MISS', c[:45])
en_checks=[
"Falling teeth in a dream also mean paying one's debts",
"the number of fallen teeth represent the number of debts to be satisfied",
"teeth fall without pain or a cause in the dream, then they represent worthless deeds",
"If one collects his fallen teeth in a dream, it also means that he can no longer conceive children",
"incompetence or inability to complete a project",
]
norm=re.sub(r'\s+',' ',ibn)
for c in en_checks:
    print('EN', 'OK ' if c in norm else 'MISS', c[:55])
h=open('/root/teethdreammeaning/site/dream/one-tooth-vs-all-teeth/index.html',encoding='utf-8').read()
print('DIV', h.count('<div'), h.count('</div>'), 'BQ', h.count('<blockquote>'), h.count('</blockquote>'), 'P', h.count('<p'), h.count('</p>'))
print('CJK:', bool(re.search(r'[\u4e00-\u9fff]', h)))
print('AR-lines:', [l[:70] for l in h.split('\n') if re.search(r'[\u0600-\u06ff]', l)])
