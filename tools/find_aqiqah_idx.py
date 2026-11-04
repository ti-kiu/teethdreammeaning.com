import re
lines = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read().split('\n')
# index region: find 'Aqiqah' entries after line 27600
for i, l in enumerate(lines):
    if i > 27600 and re.search(r"Aqiqah|'Aqiq", l):
        print('IDX?', i+1, repr(l[:120]))
# first index lines
for i in range(27680, 27700):
    if lines[i].strip():
        print('IDX-START', i+1, repr(lines[i][:120]))
