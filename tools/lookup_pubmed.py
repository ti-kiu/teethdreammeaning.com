#!/usr/bin/env python3
"""Fetch PubMed records by search term or id, print compact summaries. No pipes to interpreters."""
import json, sys, time, urllib.request, urllib.parse

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "tdm-research/1.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")

def esearch(term):
    u = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&term=" + urllib.parse.quote(term)
    return json.loads(get(u))["esearchresult"].get("idlist", [])

def esummary(ids):
    if not ids: return {}
    u = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids)
    return json.loads(get(u))["result"]

def efetch_text(ids):
    u = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=text&rettype=abstract&id=" + ",".join(ids)
    return get(u)

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "search":
        term = sys.argv[2]
        ids = esearch(term)[:5]
        print("IDS:", ids)
        r = esummary(ids)
        for i in ids:
            x = r.get(i, {})
            print(i, "|", x.get("title"), "|", x.get("source"), x.get("volume"), "(" + str(x.get("issue")) + "):", x.get("pages"), x.get("pubdate"))
        time.sleep(0.4)
    elif mode == "abstract":
        ids = [sys.argv[2]]
        print(efetch_text(ids)[:6000])
