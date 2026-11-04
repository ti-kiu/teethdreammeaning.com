import re
t193 = open('/root/dream_research/nabulsi_page_193.txt', encoding='utf-8').read()
t192 = open('/root/dream_research/nabulsi_page_192.txt', encoding='utf-8').read()
comb = re.sub(r'\s+',' ', t192+' '+t193)
for q in ["كشعر الفرس", "مؤخر رأسه قد انتثر", "ينبت في وجهه", "شعر بطنه كثر", "ذراعيه يتناثر"]:
    m = re.search(r'.{50}'+re.escape(q)+r'.{100}', comb)
    print('---', q)
    print(m.group(0) if m else 'NOT FOUND')
en = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()
en_n = re.sub(r'\s+',' ', en)
for q in ["hair growing anew", "Seeing hair in one's noses", "hair in one's noses"]:
    m = re.search(r'.{60}'+re.escape(q)+r'.{120}', en_n)
    print('===', q)
    print(m.group(0) if m else 'NOT FOUND')
