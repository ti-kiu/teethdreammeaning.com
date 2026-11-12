import re, html
body = html.unescape(open('site/dream/cat/index.html', encoding='utf-8').read())
first_h2 = body.find('<h2')
src = body.rfind('Sources')
mid = body[first_h2:src]
for m in re.finditer(r'[\u4e00-\u9fff]+', mid):
    s = max(0, m.start()-100); e = min(len(mid), m.end()+50)
    print('...', mid[s:e].replace('\n', ' '), '...')
    print('---')
