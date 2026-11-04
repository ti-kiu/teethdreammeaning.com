import re
s = open('/root/teethdreammeaning/tools/build_hair.py', encoding='utf-8').read()
lines = s.split('\n')
for n, l in enumerate(lines, 1):
    # find lines inside f-string with unbalanced braces (single { or } not doubled)
    t = l.replace('{{','').replace('}}','')
    odd_c = t.count('{') - t.count('}')
    if odd_c != 0 and (n > 60):
        print(n, repr(t[:150]))
