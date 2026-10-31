#!/usr/bin/env python3
# Batch 4 checks for gap #7.
AR = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
EN = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()
PMC = open('/root/.hermes/cache/web/www.frontiersin.org-fc4707a4dd.md', encoding='utf-8').read()
a4 = [
 "وقيل من سقطت أسنانه فقد بقي من عمره تسع وعشرون سنة أو ثلاثون سنة وقيل يموت إلى ثلاثين يوما أو يغرم ثلاثين دينارا",
 "فإن تساقطت جميع الأسنان فإنه يهلك جميع من في ذلك المنزل",
 "وقيل من رأى سقوط أسنانه دل على مضرة لبعض أصدقائه",
 "ربما كان المغرم على قدر دية السن في الشرع",
]
e4 = [
 "Falling teeth in a dream\nmeans longevity, or living past one's contemporaries.",
]
p4 = [
 "In the Jewish Talmud, TD were construed as a prophecy for the impending death of a family member",
 "The connection between TD and death was a common belief for many years",
 "TD may perhaps serve as indicators of undiagnosed bruxism",
 "utilized by dentists as an aid for screening of dental problems",
]
f = 0
for a in a4:
    hit = a in AR
    print(("HIT " if hit else "MISS"), "[AR]", a[:70]); f += 0 if hit else 1
for a in e4:
    hit = a in EN
    print(("HIT " if hit else "MISS"), "[EN]", a[:70].replace("\n"," ")); f += 0 if hit else 1
for a in p4:
    hit = a in PMC
    print(("HIT " if hit else "MISS"), "[PMC]", a[:70]); f += 0 if hit else 1
print("fail:", f)
