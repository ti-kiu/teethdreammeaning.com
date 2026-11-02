import re, subprocess

def fetch(url):
    return subprocess.run(['curl', '-s', url], capture_output=True, text=True, timeout=30).stdout

def code(url):
    return subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', url], capture_output=True, text=True, timeout=30).stdout

print('kaaba status:', code('https://teethdreammeaning.com/dream/kaaba/'))
print('home status:', code('https://teethdreammeaning.com/'))
print('disclaimer:', code('https://teethdreammeaning.com/disclaimer/'))
sm = fetch('https://teethdreammeaning.com/sitemap.xml')
print('sitemap has kaaba:', '/dream/kaaba/' in sm, '| urls:', sm.count('<loc>'))
home = fetch('https://teethdreammeaning.com/')
print('home links kaaba:', home.count('/dream/kaaba/'))
h = fetch('https://teethdreammeaning.com/dream/kaaba/')
print('h1:', re.search(r'<h1>(.*?)</h1>', h).group(1))
print('div', h.count('<div'), h.count('</div>'), '| bq', h.count('<blockquote'), h.count('</blockquote>'),
      '| p', len(re.findall(r'<p[ >]', h)), h.count('</p>'), '| footer', h.count('<footer'), h.count('</footer>'))
cjk = re.findall(r'[一-鿿]', h)
print('CJK count (must all be inside Sources/note/FAQ absence-statement):', len(cjk), ''.join(cjk))
seg = h.split('<h1>')[1].split('<h2>')[0]
print('CJK in first screen:', len(re.findall(r'[一-鿿]', seg)), '| Arabic in first screen:', bool(re.search(r'[؀-ۿ]', seg)))
print('canonical:', 'href="https://teethdreammeaning.com/dream/kaaba/"' in h)
print('word count:', len(re.sub(r'<[^>]+>', ' ', h).split()))
