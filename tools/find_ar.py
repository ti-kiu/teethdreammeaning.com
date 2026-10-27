import re, sys
t = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
print("LEN", len(t))
for kw in sys.argv[1:]:
    for m in re.finditer(re.escape(kw), t):
        s = max(0, m.start()-160); e = min(len(t), m.end()+300)
        print(f"--- {kw} @{m.start()} ---")
        print(t[s:e].replace('\n', ' '))
        print()
