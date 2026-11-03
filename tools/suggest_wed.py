#!/usr/bin/env python3
import json, time, urllib.request, urllib.parse
qs = ["dreaming about a wedding", "dream of getting married", "wedding dream meaning",
      "dream about marriage islam", "dreaming of someone else's wedding", "dream of my own wedding",
      "dream about wedding preparation", "dream of bride"]
for q in qs:
    url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=" + urllib.parse.quote(q)
    try:
        raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=8).read().decode("utf-8", "ignore")
        d = json.loads(raw)
        print(f"Q: {q}\n   " + " | ".join(d[1]))
    except Exception as e:
        print(f"Q: {q}\n   ERR {e}")
    time.sleep(0.5)
