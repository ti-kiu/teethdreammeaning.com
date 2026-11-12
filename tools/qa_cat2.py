import re, json, html
P = open('site/dream/cat/index.html', encoding='utf-8').read()
for t in ['div','blockquote','p','section','ul','li','h2','footer']:
    o = len(re.findall(r'<'+t+r'[ >]', P)); c = len(re.findall(r'</'+t+'>', P))
    if o != c: print('CLOSE FAIL', t, o, c)
print('closure checked')
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', P, re.S):
    try: json.loads(m)
    except Exception as e: print('LD FAIL', e)
print('ld ok')
body = html.unescape(P)
first_h2 = body.find('<h2')
pre = body[:first_h2]
ar = re.findall(r'[\u0600-\u06FF]', pre)
cjk = re.findall(r'[\u4e00-\u9fff]', pre)
print('first-screen arabic:', len(ar), 'cjk:', len(cjk), repr(''.join(sorted(set(cjk)))))
src = body.rfind('Sources')
mid = body[first_h2:src]
print('CJK in mid:', len(re.findall(r'[\u4e00-\u9fff]', mid)))
print('title len:', len(re.search(r'<title>(.*?)</title>', P).group(1)))
print('desc len:', len(re.search(r'name="description" content="([^"]*)"', P).group(1)))
print('canonical:', 'rel="canonical"' in P, '| og:', 'og:title' in P, '| h1 count:', len(re.findall(r'<h1', P)))
