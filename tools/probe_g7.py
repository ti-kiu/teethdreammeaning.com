#!/usr/bin/env python3
import urllib.request, urllib.error
urls = [
 "https://ba634d36.teethdreammeaning.pages.dev/dream/teeth-falling-out-and-death/",
 "https://ba634d36.teethdreammeaning.pages.dev/",
 "https://ba634d36.teethdreammeaning.pages.dev/sitemap.xml",
 "https://teethdreammeaning.com/dream/teeth-falling-out-and-death/",
 "https://teethdreammeaning.com/",
 "https://teethdreammeaning.com/sitemap.xml",
 "https://teethdreammeaning.com/dream/teeth-falling-out/",
 "https://teethdreammeaning.com/robots.txt",
]
for u in urls:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/120 Safari/537.36"})
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read()
            print(r.status, len(body), u)
    except urllib.error.HTTPError as e:
        print(e.code, "-", u)
    except Exception as e:
        print("ERR", type(e).__name__, str(e)[:60], u)
