import re, urllib.request
def get(u):
    req = urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8','ignore')
for slug in ("teeth-falling-out-with-blood","gold","dead-person-resurrected"):
    t = get(f"https://teethdreammeaning.com/dream/{slug}/")
    print(slug, "link-to-blood:", t.count('href="/dream/blood/"'))
t = get("https://teethdreammeaning.com/dream/blood/?v=" + "9")
seg = t.split('<h1>')[1].split('<h2>')[0]
print("blood online: h1 ok:", "Dreaming of Blood" in t, "| first-screen CJK:", bool(re.search(r'[\u4e00-\u9fff]', seg)), "| first-screen Arabic:", bool(re.search(r'[\u0600-\u06ff]', seg)))
