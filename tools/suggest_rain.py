#!/usr/bin/env python3
import urllib.request, urllib.parse, json
qs = ["rain dream", "dreaming about rain", "dream of rain", "rain dream meaning islam",
      "heavy rain dream", "dream about rain and flooding", "dream about raining inside house",
      "rain in dream islamic interpretation", "dream of rain on me", "standing in rain dream"]
for q in qs:
    url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=" + urllib.parse.quote(q)
    try:
        d = json.loads(urllib.request.urlopen(url, timeout=15).read().decode("utf-8", "ignore"))
        print("Q:", q, "->", json.dumps(d[1][:12], ensure_ascii=False))
    except Exception as e:
        print("Q:", q, "ERR", e)
