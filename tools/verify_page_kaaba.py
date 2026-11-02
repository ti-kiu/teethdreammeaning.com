import re, json, html

IS = open('/root/dream_research/ibn_sirin_full.txt').read()
NAB = json.load(open('/root/.hermes/nabulsi_p2_120.json'))['289']['txt']
PAGE = html.unescape(open('/root/teethdreammeaning/site/dream/kaaba/index.html').read())

def squash(s):
    s = re.sub(r"\d{3} (?:IBN [A-Za-z:·'()ÙÜÍÉ!1]+['::)·]*|DICTIONARY OF DREAMS \d+|DICTIONARY OF DREAMS \d+)", ' ', s)
    s = s.replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', '', s)

ISN, NABN = squash(IS), squash(NAB)

# 1. verbatim English blobs quoted in the page's Sources (attributed to compilation)
m = re.search(r'entry, printed pp\. 237–238.*?: "(Ka\'aba: .*?students and disciples\.)"</p>', PAGE, re.S)
big = m.group(1)
print('Ka\'aba full entry verbatim:', squash(big) in ISN)
m2 = re.search(r'entry, printed p\. 41.*?: "(Black Stone: .*?to be wrong\.)"', PAGE, re.S)
print('Black Stone verbatim:', squash(m2.group(1)) in ISN)
m3 = re.search(r'"(In a dream, the Holy Mecca represents .*?manifest in his life\.)"', PAGE)
print('Mecca clause verbatim:', squash(m3.group(1)) in ISN)
m4 = re.search(r'And its marriage clause: "(If one sees himself living in Mecca in a dream, it also may mean that he will give his daughter in marriage to a noble person\.)"', PAGE)
print('Mecca marriage verbatim:', squash(m4.group(1)) in ISN)

# 2. every Arabic run inside quotes on the page must be verbatim in shamela p289 text
ar_segs = re.findall(r'"([^"]*[؀-ۿ][^"]*)"', PAGE)
fails = 0
for a in ar_segs:
    ok = squash(a) in NABN
    if not ok:
        print('AR MISS |', a[:80]); fails += 1
print('AR segments checked:', len(ar_segs), 'fails:', fails)

# 3. body verbatim English quotes (straight-quoted fragments attributed to the compilation)
body = [
 "or it could mean receiving glad tidings and dispelling evil",
 "safety and protection against fear",
 "enjoying the guardianship and protection of someone in authority, and safety from one's enemy",
 "entering before a ruler",
 "means walking the path of righteousness, or correcting one's religious life as much as one does in his dream",
 "is equal to changing the direction (arb. Qiblah) of one's prayers",
 "becoming an apostate",
 "though with a questionable conduct",
 "the death of the Calif or the local governor",
 "will reflect upon the Imam, or the guide of all Muslims",
 "still in power and living with grace",
 "he will be endowed with wisdom, gain knowledge and act upon it, and that people will learn at his hand and follow his example",
 "perhaps an indication of going to perform one's pilgrimage",
 "for it is the focal point of all praying Muslims",
 "correcting one's religious standing",
 "waking-life activities are reflected in corresponding differences in dream content",
 "remains vague",
]
bfails = 0
for q in body:
    ok = squash(q) in ISN
    if not ok:
        print('BODY MISS |', q); bfails += 1
print('body EN quotes:', len(body), 'fails:', bfails)

# 4. L2 numbers cross-check against cached study pages
sch = open('/root/.hermes/cache/web/pubmed.ncbi.nlm.nih.gov-44e86fc936.md', errors='ignore').read()
bai = open('/root/.hermes/cache/web/journals.lww.com-52b83b8e9d.md', errors='ignore').read()
for tok, src, name in [
    ("Continuity between waking activities and dream activities", sch, 'Schredl title'),
    ("correlational design", sch, 'correlational design'),
    ("remains vague", sch, 'remains vague'),
    ("Bamagoos, Ahmad A", bai, 'authors'),
    ("13(2):p 70-74", bai, 'journal pages'),
    ("228 adult pilgrims", bai, 'n=228'),
    ("21%", bai, 'OSA risk 21%'),
    ("dissatisfaction from their daily sleep quality", bai, '38% dissatisfied'),
    ("58%", bai, '58% symptoms'),
    ("47%", bai, '47% morning tiredness'),
    ("25%", bai, '25% snoring'),
    ("Mina", bai, 'Mina'),
]:
    print(('OK  ' if tok in src else 'MISS'), name)

# 5. page structure
div_o, div_c = PAGE.count('<div'), PAGE.count('</div>')
bq_o, bq_c = PAGE.count('<blockquote'), PAGE.count('</blockquote>')
p_o, p_c = len(re.findall(r'<p[ >]', PAGE)), PAGE.count('</p>')
print('div', div_o, div_c, '| blockquote', bq_o, bq_c, '| p', p_o, p_c)
cjk = re.findall(r'[一-鿿]', PAGE)
print('CJK chars on page:', len(cjk), ''.join(sorted(set(cjk))))
# first screen rule: no Arabic between h1 and first h2
seg = PAGE.split('<h1>')[1].split('<h2>')[0]
print('Arabic in first screen:', bool(re.search(r'[؀-ۿ]', seg)))
print('DONE')
