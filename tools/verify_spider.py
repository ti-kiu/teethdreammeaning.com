#!/usr/bin/env python3
"""Verify every L1 quote assertion for /dream/spider/ verbatim against corpora. FAILS must be 0."""
import re

def joined(path):
    return re.sub(r"\s+", " ", open(path, encoding="utf-8").read())

ibn = joined("/root/dream_research/ibn_sirin_full.txt")
p247 = joined("/root/dream_research/nabulsi_page_247.txt")
p248 = joined("/root/dream_research/nabulsi_page_248.txt")
zg = joined("/root/dream_research/zhougong_yuanban.txt")

EN = [
 "Spider: In a dream, a spider represents a malicious woman, or a weak, perfidious and a distant man.",
 "A spider in a dream also represents a weaver, an ascetic or a monk.",
 "If one sees a spider in his dream, it may mean that he will meet a pious and a religious man.",
 "Weaving a web in a dream means becoming weak.",
 "A spider in a dream also could represent a pleasing wife.",
 "If one sees a spider hanging down from the ceiling in a dream, it indicates a severe winter in that area.",
 "(Also see Tarantula)",
 "Tarantula: (Hairy spider; Spider) A tarantula in a dream represents a loathsome and an evil woman who interferes with people's business and damages their interests, or who destroys what they repair and denies having anything to do with their sufferings.",
 "In a dream, this interpretation is based on the legendary nervous disease, formerly believed to be caused by a poisonous bite of a tarantula.",
 "Thus, when this harmless hairy spider is seen in a dream, it also could represent a lethal enemy of a fierce sting, scowling, or a despising look.",
 "Weaver: (Knitting) In a dream, a weaver represents a problem solver, garments, travels, or hesitation.",
 "Seeing a weaver in a dream also may indicate the death of sick person, or lowering his corps into his grave.",
]
AR247 = [
 "(عنكبوت) هو في المنام امرأة ملعونة تهجر فراش زوجها.",
 "(ومن رأى) عنكبوتاً فإنه يرى رجلاً مكايداً",
]
AR248 = [
 "ضعيفاً متوانياً وقيل العنكبوت رجل نساج وقيل هو رجل عابد زاهد فمن أصاب عنكبوتاً صاحب رجلاً عابداً زاهداً.",
 "(ومن رأى) بيت العنكبوت ونسجها ضعف ووهن لقوله تعالى: {وإن أوهن البيوت لبيت العنكبوت}",
 "والعنكبوت يدل على المرأة السحارة وربما دل على معرفة النسج والحياكة.",
 "(ومن رأى) العنكبوت ساقطاً من السقوف فذلك دليل على شدة الشتاء.",
]
ZG_ABSENT = ["蜘蛛", "蛛"]  # expect zero hits — page must state absence honestly

fails = 0
for a in EN:
    ok = a in ibn; fails += (not ok)
    print(("OK   EN " if ok else "MISS EN "), a[:72])
for a in AR247:
    ok = a in p247; fails += (not ok)
    print(("OK   A247" if ok else "MISS A247"), a[:60])
for a in AR248:
    ok = a in p248; fails += (not ok)
    print(("OK   A248" if ok else "MISS A248"), a[:60])
for w in ZG_ABSENT:
    ok = w not in zg; fails += (not ok)
    print(("OK   ZG-absent" if ok else "MISS ZG-present"), w)
print("FAILS =", fails)
