import re, json, html

IS = open('/root/dream_research/ibn_sirin_full.txt').read()
PAGE = html.unescape(open('/root/teethdreammeaning/site/dream/kaaba/index.html').read())

def squash(s):
    s = re.sub(r"\d{3} (?:IBN [A-Za-z:·'()!1]+[A-Za-z:·'()!1]*|DICTIONARY OF DREAMS \d+)", ' ', s)
    s = s.replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', '', s)

ISN = squash(IS)
m = re.search(r'entry, printed pp\. 237–238.*?: "(Ka\'aba: .*?students and disciples\.)"</p>', PAGE, re.S)
big = squash(m.group(1))

# binary-search divergence point
lo, hi = 0, len(big)
while lo < hi:
    mid = (lo + hi + 1) // 2
    if big[:mid] in ISN:
        lo = mid
    else:
        hi = mid - 1
print('matches first', lo, 'chars')
print('PAGE continues:', repr(big[lo:lo+120]))
i = ISN.find(big[max(0,lo-40):lo])
print('IS   continues:', repr(ISN[i+40:i+160]) if i >= 0 else 'anchor not found')
