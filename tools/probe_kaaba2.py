import json, re
d = json.load(open('/root/.hermes/nabulsi_p2_120.json'))
txt = re.sub(r'\s+', ' ', d['289']['txt'])
i = txt.find("والكعبة تدل على الصلاة")
seg = txt[i:i+320]
print(repr(seg))
