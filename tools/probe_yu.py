import re
t = open('/root/dream_research/frontiers_full.txt', encoding='utf-8').read()
for m in re.finditer(r'.{150}(39\.0|16\.2|8\.2).{150}', t):
    print('---'); print(m.group(0))
print('has Yu 2012:', 'Yu, T.-P.' in t or 'Yu (2012)' in t or '2012' in t and 'Yu' in t)
m = re.search(r'.{200}Yu.{160}2012.{160}', t)
if m: print('YUCITE:'); print(m.group(0))
