#!/usr/bin/env python3
"""Pull shamela.ws/book/1217/<pg> pages and save clean Arabic text to /root/dream_research/nabulsi_page_<pg>.txt"""
import re, html, sys, time, urllib.request

def pull(pg):
    url = f"https://shamela.ws/book/1217/{pg}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"})
    raw = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    # shamela page text is inside div id=book_text (older) or article; try several
    m = re.search(r'id="book_text".*?>(.*?)</div>', raw, re.S)
    if not m:
        m = re.search(r'<article[^>]*>(.*?)</article>', raw, re.S)
    body = m.group(1) if m else raw
    # strip tags
    body = re.sub(r'<script.*?</script>', ' ', body, flags=re.S)
    body = re.sub(r'<style.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<br[^>]*>', '\n', body)
    body = re.sub(r'</p>', '\n', body)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(body)
    # normalize whitespace per line
    lines = [re.sub(r'[ \t\u200f\u200e\u061c]+', ' ', l).strip() for l in body.splitlines()]
    lines = [l for l in lines if l]
    return url, "\n".join(lines)

if __name__ == "__main__":
    pages = [int(x) for x in sys.argv[1:]]
    for pg in pages:
        try:
            url, txt = pull(pg)
            out = f"/root/dream_research/nabulsi_page_{pg}.txt"
            with open(out, "w", encoding="utf-8") as f:
                f.write(txt)
            print(pg, len(txt), out)
        except Exception as e:
            print(pg, "ERR", e)
        time.sleep(1.2)
