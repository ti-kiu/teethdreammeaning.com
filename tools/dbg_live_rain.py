#!/usr/bin/env python3
import re
t=open('/tmp/live_rain.html').read()
seg=t.split('<h1>')[1].split('<h2')[0]
print('bytes',len(t))
print('first-screen Arabic', sum(1 for c in seg if '\u0600'<=c<='\u06ff'), 'CJK', sum(1 for c in seg if '\u4e00'<=c<='\u9fff'))
print('h1:', re.search(r'<h1>([^<]*)',t).group(1))
print('AR blocks on live page:', t.count('class="ar"'))
