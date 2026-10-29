import re
h = open('/root/teethdreammeaning/site/dream/teeth-dreams-and-stress/index.html', encoding='utf-8').read()
# structural closure
print('DIV', h.count('<div'), h.count('</div>'))
print('BQ', h.count('<blockquote>'), h.count('</blockquote>'))
print('P', h.count('<p'), h.count('</p>'))
print('H2', h.count('<h2>'), h.count('</h2>'))
print('H3', h.count('<h3>'), h.count('</h3>'))
print('BLOCKQUOTE_OPEN', h.count('<blockquote>'))
print('EM', h.count('<em>'), h.count('</em>'))
print('CJK:', bool(re.search(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', h)))
# Arabic runs embedded on the page must exist verbatim in shamela source
src = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
ar_on_page = re.findall(r'[؀-ۿ][؀-ۿ \n,؛"\u201c\u201d()]{8,}', h)
ok = True
seen = set()
for a in ar_on_page:
    core = re.sub(r'\s+', ' ', a).strip().strip('"\u201c\u201d(),; ')
    if len(core) < 15 or core in seen:
        continue
    seen.add(core)
    src_n = re.sub(r'\s+', ' ', src)
    hit = core in src_n
    ok &= hit
    print('ARQ', 'OK ' if hit else 'MISS', core[:60])
print('PAGE CHECK', 'PASS' if ok and len(seen) >= 3 else 'FAIL')
