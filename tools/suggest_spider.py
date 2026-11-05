#!/usr/bin/env python3
import json, time, urllib.parse, urllib.request
queries = ["spider dream", "dreaming about spiders", "dream about a spider", "spider dream meaning",
           "dream of spider killing it", "spider crawling on me dream", "dream about spider islam",
           "black spider dream"]
for q in queries:
    url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=" + urllib.parse.quote(q)
    try:
        d = json.loads(urllib.request.urlopen(url, timeout=15).read().decode())
        print("Q:", q)
        for s in d[1]:
            print("  ", s)
    except Exception as e:
        print("Q:", q, "ERR", e)
    time.sleep(0.5)
