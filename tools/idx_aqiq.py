import re
lines = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read().split('\n')
idx = "\n".join(lines[27600:])
# lines that end with a number (index entries), show ones containing key substrings
for key in ["riites", "rites", "Aqiq", "Qiq", "Strand"]:
    print('KEY', key)
    for l in idx.splitlines():
        if key in l and re.search(r"\d+\s*$", l):
            print(' ', repr(l[:120]))
