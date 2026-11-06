import re
p = open('/root/teethdreammeaning/site/dream/blood/index.html', encoding='utf-8').read()
t = re.search(r'<title>(.*?)</title>', p).group(1)
d = re.search(r'<meta name="description" content="(.*?)">', p).group(1)
print("title:", len(t), "|", t)
print("desc:", len(d))
print("syms cards:", open('/root/teethdreammeaning/site/index.html', encoding='utf-8').read().split('<h2>Other symbols</h2>')[1].split('The method')[0].count('class="card"'))
