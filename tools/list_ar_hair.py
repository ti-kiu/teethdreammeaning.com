import re
for pg in (192, 193):
    t = open(f'/root/dream_research/nabulsi_page_{pg}.txt', encoding='utf-8').read()
    # keep only the book text region: lines starting with ( or - ( ...
    lines = [l for l in t.splitlines() if l and not l.startswith('اذهب') and 'البحث في' not in l and 'مسار الصفحة' not in l and 'القرون' not in l and 'لتخصيص' not in l and 'بحث تحديد' not in l and 'موقع افتراضي' not in l and 'الغراء' not in l and l not in ('×',)]
    txt = "\n".join(lines)
    # split into sentences
    sents = [s.strip() for s in re.split(r'(?<=\.)\s+', txt) if s.strip()]
    print(f'===== PAGE {pg} : {len(sents)} sentences =====')
    for i, s in enumerate(sents):
        print(f'[{pg}.{i}] {s[:200]}')
