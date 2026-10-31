#!/bin/bash
# google suggest for gap #7 (death reading) queries
for q in "teeth falling out dream meaning death" "dream about teeth falling out death" "teeth falling out dream buried" "dream of losing teeth someone dying" "teeth falling out dream grandmother"; do
  echo "Q: $q"
  python3 -c "
import urllib.request, urllib.parse, json, sys
u='https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q='+urllib.parse.quote('$q')
print(urllib.request.urlopen(u, timeout=15).read().decode('utf-8', 'replace'))
"
  sleep 1
done
