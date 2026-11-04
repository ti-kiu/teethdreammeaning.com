import re
lines = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read().split('\n')
heads = [(i+1, l.strip()) for i, l in enumerate(lines)
         if re.match(r'^\s*(DICTIONARY OF DREAMS \d+|\d+ IBN)', l)]
def where(lineno):
    prev = None
    for i, h in heads:
        if i > lineno: break
        prev = (i, h)
    nxt = next((h for i, h in heads if i > lineno), None)
    return prev, nxt
for name, target in [("Hair", 12341), ("Hair cont p199", 12356), ("Hair end/Haircut", 12445),
                     ("Shaving", 21974), ("Strand", 23722), ("Braiding", 4697), ("Aqiqah", 2617)]:
    p, n = where(target)
    print(name, target, '->', p, '|next:', n)
# also show lines 12440-12448 raw and index lines for exact index entries
print('---Hair end raw---')
print('\n'.join(lines[12440:12448]))
# print index lines for Hair/Shaving/Braiding/'Aqiqah
for i, l in enumerate(lines):
    if re.match(r'^\s*(Hair|Shaving|Braiding|Strand of hair)', l) and i > 28900:
        print('IDX:', i+1, l)
