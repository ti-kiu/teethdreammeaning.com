import re
lines = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read().split('\n')
heads = [(i+1, l.strip()) for i, l in enumerate(lines[:4000])
         if re.match(r'^\s*(DICTIONARY OF DREAMS \d+|\d+ IBN)', l)]
for target, name in [(2617, "Aqiqah rites"), (2621, "Aqiqah mid")]:
    prev = None
    for i, h in heads:
        if i > target: break
        prev = (i, h)
    nxt = next((h for i, h in heads if i > target), None)
    print(name, target, '-> prev header', prev, '| next', nxt)
# print raw header line to inspect OCR
for i, l in enumerate(lines[2630:2680], start=2631):
    if re.search(r'IBN|DICTIONARY', l):
        print('RAW', i, repr(l))
