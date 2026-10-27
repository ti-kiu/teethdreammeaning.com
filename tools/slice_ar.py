import re, sys
t = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
a, b = int(sys.argv[1]), int(sys.argv[2])
print(t[a:b])
