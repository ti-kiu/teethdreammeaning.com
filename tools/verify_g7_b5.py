#!/usr/bin/env python3
# Batch 5: exact extraction of the وقيل chains + Talmud line.
import re
AR = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
PMC = open('/root/.hermes/cache/web/www.frontiersin.org-fc4707a4dd.md', encoding='utf-8').read()

i = AR.find("وقيل من سقطت أسنانه")
print("AR30:", repr(AR[i:i+200]) if i >= 0 else "NOT FOUND")
j = AR.find("وقيل من رأى")
print("ARMUD:", repr(AR[j:j+220]) if j >= 0 else "NOT FOUND")
k = AR.find("Talmud", 0)  # in PMC
m = PMC.find("In the Jewish Talmud")
print("PMC TAL:", repr(PMC[m:m+160]) if m >= 0 else "NOT FOUND")
