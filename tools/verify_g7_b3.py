#!/usr/bin/env python3
# Third batch of verbatim checks for gap #7 page.
AR = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
EN = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()
a3 = [
 "والرباعية ابن عم الرجل أو صديقان يقومان مقامه",
 "والناب الأسفل سيد أهل بيته ومن يستند إليه",
 "والضواحك السفلى بنت خالته أو بنت خاله",
 "والأضراس السفلى والعليا الأبعدون من أهل بيت الرجل",
 "وكذلك سائر الأسنان كلها وكذلك الجوارح كلها فإن سبيلها كسبيل سائر الأسنان",
 "فإن أمسكها بعد عاهة تصيبها فإنه يستفيد مثلها من الأقارب أو الأجانب",
 "وإن لم يكن له أب أو عم فأخوات أو ولدان أو صديقان ناصحان مشفقان",
]
e3 = [
 "and the lower left",
 "incisor represents one's aunt from his father's side",
 "The bicuspids represent one's uncles from the mother's",
 "The lower canine tooth, or the eyetooth",
 "represents the sire of the house, or the landlord.",
 "then the\nteeth of the right side represent the boys, and those on the left side represent",
 "or it could possibly mean that he will be separated from him and",
 "can no longer see him.",
]
f = 0
for a in a3:
    hit = a in AR
    print(("HIT " if hit else "MISS"), "[AR]", a[:75])
    f += 0 if hit else 1
for a in e3:
    hit = a in EN
    print(("HIT " if hit else "MISS"), "[EN]", a[:75].replace("\n", " "))
    f += 0 if hit else 1
print("fail:", f)
