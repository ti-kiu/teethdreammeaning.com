import json, urllib.parse, urllib.request

queries = [
    "dreaming about the kaaba",
    "dream of kaaba",
    "kaaba dream",
    "dream about hajj pilgrimage",
    "dream of visiting mecca",
    "dream mecca",
    "dreaming of the holy house islam",
    "circumambulating the kaaba dream",
]
for q in queries:
    url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=" + urllib.parse.quote(q)
    try:
        d = json.load(urllib.request.urlopen(url, timeout=15))
        print("Q:", q)
        for s in d[1][:10]:
            print("   ", s)
    except Exception as e:
        print("Q:", q, "ERR", e)
