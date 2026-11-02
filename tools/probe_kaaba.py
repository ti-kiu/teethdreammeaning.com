import json, re
d = json.load(open('/root/.hermes/nabulsi_p2_120.json'))
txt = re.sub(r'\s+', ' ', d['289']['txt'])
for pat in ["الكعبة قد خربت", "يطوف حولها", "نقص من المناسك", "والكعبة تدل على الصلاة",
            "وقد تدل على الموسم", "من يقتدي به", "صيت في الناس", "الأمر بالمعروف",
            "فإن الكعبة إمام المسلمين"]:
    i = txt.find(pat)
    print(pat, '->', repr(txt[max(0, i-70):i+len(pat)+50]) if i >= 0 else 'NOT FOUND')
