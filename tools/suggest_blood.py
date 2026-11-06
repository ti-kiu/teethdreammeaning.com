#!/usr/bin/env python3
"""Google suggest pulls for the blood queue page — record only real dropdowns."""
import json, urllib.request, urllib.parse, time

QUERIES = [
    "dream about blood",
    "blood dream meaning",
    "dream of bleeding",
    "blood in dream islam",
    "dreaming about blood",
    "period dream islam",
    "dream of blood everywhere",
    "drinking blood dream",
]

for q in QUERIES:
    url = ("https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q="
           + urllib.parse.quote(q))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        data = json.loads(urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "ignore"))
        print(f"q={q!r}")
        for s in data[1]:
            print("   ", s)
    except Exception as e:
        print(f"q={q!r} ERR {e}")
    time.sleep(1.0)
