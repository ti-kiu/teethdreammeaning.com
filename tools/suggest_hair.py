#!/usr/bin/env python3
import urllib.request, urllib.parse, json, time
qs = ["dream about hair falling out", "hair falling out dream", "dream hair falling out meaning",
      "dream about hair falling out in clumps islam", "dream of losing hair", "hair dream meaning islam",
      "dream about hair falling out reddit", "dreaming of hair loss spiritual"]
for q in qs:
    url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=" + urllib.parse.quote(q)
    try:
        raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=15).read().decode("utf-8", "ignore")
        data = json.loads(raw)
        print(q, "=>", data[1][:8])
    except Exception as e:
        print(q, "ERR", e)
    time.sleep(1)
