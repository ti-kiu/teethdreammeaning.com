#!/usr/bin/env python3
"""IndexNow submit (Bing/Yandex/Naver). Usage: python3 submit_indexnow.py [urls...]
Default: homepage + teeth page."""
import sys, json, urllib.request, urllib.error

BASE = "/root/teethdreammeaning"
KEY = open(BASE + "/.indexnow_key").read().strip()
HOST = "teethdreammeaning.com"
urls = sys.argv[1:] or [
    "https://teethdreammeaning.com/",
    "https://teethdreammeaning.com/dream/teeth-falling-out/",
]
payload = {"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json; charset=utf-8"},
)
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("indexnow api:", r.status)
except urllib.error.HTTPError as e:
    print("indexnow api:", e.code)
