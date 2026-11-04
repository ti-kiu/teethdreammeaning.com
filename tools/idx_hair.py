import re
lines = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read().split('\n')
idx = "\n".join(lines[27600:])
for word in ["Hair", "Haircut", "Hairdresser", "Shaving", "Strand", "Braiding", "Barber", "Comb", "Lice", "Dye", "Henna", "Baldness"]:
    for m in re.finditer(rf"\b{word}[a-z]*\s+\d+", idx):
        print(word, '->', repr(m.group(0)))
    print('---')
