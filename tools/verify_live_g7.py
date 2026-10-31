#!/usr/bin/env python3
import urllib.request, re
def get(u):
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 Chrome/120"})
    r = urllib.request.urlopen(req, timeout=25)
    return r.status, r.read().decode('utf-8', 'replace')
s, home = get("https://teethdreammeaning.com/")
print("home", s, "interlink in home:", "teeth-falling-out-and-death" in home)
s, new = get("https://teethdreammeaning.com/dream/teeth-falling-out-and-death/")
print("new page", s, "len", len(new), "CJK", len(re.findall(r'[\u4e00-\u9fff]', new)))
s, om = get("https://teethdreammeaning.com/dream/teeth-falling-out-good-or-bad-omen/")
print("omen footer backlink:", s, "teeth-falling-out-and-death" in om)
s, sm = get("https://teethdreammeaning.com/sitemap.xml")
print("sitemap", s, "contains URL:", "teeth-falling-out-and-death" in sm, "urls:", sm.count("<loc>"))
