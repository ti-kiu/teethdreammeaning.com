#!/usr/bin/env python3
# Probe Pages preview + production URLs for TDM health check.
import urllib.request, urllib.error
urls = [
 "https://97a0f6b8.teethdreammeaning.pages.dev/",
 "https://97a0f6b8.teethdreammeaning.pages.dev/dream/teeth-falling-out-good-or-bad-omen/",
 "https://cc82a567.teethdreammeaning.pages.dev/",
 "https://3e05082b.teethdreammeaning.pages.dev/",
 "https://teethdreammeaning.com/",
 "https://teethdreammeaning.com/dream/teeth-falling-out/",
 "https://teethdreammeaning.com/sitemap.xml",
]
for u in urls:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "curl/8.5"})
        with urllib.request.urlopen(req, timeout=20) as r:
            print(r.status, len(r.read()), u)
    except urllib.error.HTTPError as e:
        print(e.code, "-", u)
    except Exception as e:
        print("ERR", type(e).__name__, str(e)[:80], u)
