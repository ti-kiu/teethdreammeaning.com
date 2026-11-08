#!/usr/bin/env python3
import re
def norm(s): return re.sub(r'\s+',' ',s).strip()
en = norm(open('/root/dream_research/ibn_sirin_full.txt',encoding='utf-8').read())
en = norm(re.sub(r'DICTIONARY OF DREAMS \d+',' ',en))
en = norm(re.sub(r"\d+ IBN SEERIN'?S",' ',en))
i = en.find('expecting clouds'); print("EN1:", repr(en[i-40:i+80]))
j = en.find('perish during a trip'); print("EN2:", repr(en[j-80:j+40]))
a316 = norm(open('/root/dream_research/nabulsi_page_316.txt',encoding='utf-8').read())
k = a316.find('المحلة'); print("AR-D:", repr(a316[k-60:k+80]) if k!=-1 else "no محلّة")
z = a316.find('زمزم'); print("AR-Z316:", repr(a316[z-100:z+60]) if z!=-1 else "no zamzam on 316")
a318 = norm(open('/root/dream_research/nabulsi_page_318.txt',encoding='utf-8').read())
w = a318.find('زمزم'); print("AR-Z318:", repr(a318[w-120:w+60]) if w!=-1 else "no zamzam on 318")
