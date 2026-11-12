import json, urllib.parse, urllib.request
qs = ["cat dream meaning", "dream of a cat", "cat dream meaning islam",
      "cat biting me dream", "cat attacking me in a dream", "black cat dream meaning",
      "cat in dream islamic interpretation", "dream of cat scratching me"]
for q in qs:
    url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=" + urllib.parse.quote(q)
    with urllib.request.urlopen(url, timeout=15) as r:
        d = json.loads(r.read().decode("utf-8", "replace"))
    print("q=" + q)
    print("  " + " | ".join(d[1][:12]))
