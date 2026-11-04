import re
raw = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()
lines = raw.split('\n')
# Hair entry: starts at line 12341 (index 12340), ends before line 'Haircut: ...' (12445 index 12444)
hair = '\n'.join(lines[12340:12444])
hair = re.sub(r'DICTIONARY OF DREAMS \d+', ' ', hair)
hair = re.sub(r'\s+', ' ', hair).strip()
print('HAIR len', len(hair))
print('start:', hair[:80])
print('end:', hair[-120:])
# A: forearm sentence
a = hair[hair.find('If one sees the'):hair.find('Braiding the hair')].strip()
print('A:', a)
# B: lice/delouse chunk
b = hair[hair.find('If one sees his hair infested'):hair.find('If one sees his hair growing anew')].strip()
print('B:', b[:200])
# C: white hair end
c = hair[hair.find('If one\'s hair turns white'):].strip()
print('C:', c)
