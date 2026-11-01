import re, sys
h = open('/root/teethdreammeaning/site/dream/dead-person-resurrected/index.html').read()

def count(t): return len(re.findall(t, h))
for tag in ['div','blockquote','p','footer','section','h2','h3','ul','li','a']:
    o = count(r'<%s[ >]' % tag); c = count(r'</%s>' % tag)
    print(tag, o, c, 'OK' if o==c else 'MISMATCH')

# first screen: h1 to first h2 must have no Arabic
body = h.split('<body>')[1]
m = re.search(r'<h1>.*?(?=<h2>)', body, re.S)
first = m.group(0)
ar = re.findall(r'[\u0600-\u06FF]+', first)
print('FIRST SCREEN Arabic runs:', ar if ar else 'NONE', '(OK)')

# CJK on whole page outside quote zones: permitted inside blockquote/src/note? count all CJK
cjk = re.findall(r'[\u4E00-\u9FFF]+', body)
print('CJK total:', sum(len(x) for x in cjk))
# locate CJK outside Sources div + blockquote = violation
pre = body.split('<h2>Sources')[0]
outside_src = re.sub(r'<blockquote>.*?</blockquote>', '', pre, flags=re.S)
outside_src = re.sub(r'<div class="note">.*?</div>', '', outside_src, flags=re.S)
stray = re.findall(r'[\u4E00-\u9FFF]+', outside_src)
print('CJK outside quotes/Sources (lede断句 allowed once):', stray)
# Arabic outside Sources + loc lines
ar_all = re.findall(r'[\u0600-\u06FF]', body)
print('Arabic chars on page:', len(ar_all))

# title/desc lengths
t = re.search(r'<title>(.*?)</title>', h).group(1)
d = re.search(r'name="description" content="(.*?)">', h).group(1)
print('title len', len(t), '| desc len', len(d))
print('canonical ok:', 'teethdreammeaning.com/dream/dead-person-resurrected/' in h)
print('FAQ ld count:', count('application/ld\+json'))
