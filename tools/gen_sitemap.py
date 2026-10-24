#!/usr/bin/env python3
"""Generate sitemap.xml from the site tree. Every <page>.html -> URL with lastmod.
Run on every deploy (build step). Future pages picked up automatically."""
import os, datetime, xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(BASE, "..", "site")
DOMAIN = "https://teethdreammeaning.com"
SKIP = {"404.html"}

def page_url(rel):
    # index.html -> / ; dream/foo.html -> /dream/foo/
    if rel == "index.html":
        return DOMAIN + "/"
    u = DOMAIN + "/" + rel
    if u.endswith(".html"):
        u = u[:-5] + "/"
    return u

items = []
for root, dirs, files in os.walk(SITE):
    for f in files:
        if not f.endswith(".html") or f in SKIP:
            continue
        full = os.path.join(root, f)
        rel = os.path.relpath(full, SITE).replace(os.sep, "/")
        mtime = datetime.datetime.utcfromtimestamp(os.path.getmtime(full))
        items.append((page_url(rel), mtime.strftime("%Y-%m-%d")))

items.sort()
sm = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
for loc, lastmod in items:
    url = ET.SubElement(sm, "url")
    ET.SubElement(url, "loc").text = loc
    ET.SubElement(url, "lastmod").text = lastmod

ET.indent(sm, space="  ")
out = os.path.join(SITE, "sitemap.xml")
ET.ElementTree(sm).write(out, encoding="unicode", xml_declaration=True)
print(f"sitemap.xml: {len(items)} urls")
for loc, lm in items:
    print(" ", loc, lm)
