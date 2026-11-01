import re, json, sys

IS = open('/root/dream_research/ibn_sirin_full.txt').read()
NAB = json.load(open('/root/.hermes/nabulsi_p2_120.json'))
P347 = NAB['344']['txt']; P348 = NAB['345']['txt']
ZG = open('/root/dream_research/zhougong_yuanban.txt').read()
CACHE = open('/root/.hermes/cache/web/tools.10huan.com-5f4c4cc57a.md', errors='ignore').read()

def norm(s):
    # collapse whitespace; keep words as-is (scan artifacts like 'ifhe' handled by exact strings below)
    return re.sub(r'\s+', ' ', s)

ISN, P347N, P348N, ZGN, CN = map(norm, (IS, P347, P348, ZG, CACHE))

EN = [
 "Death: In a dream, death signifies religious failure, corruption and rising in status in the world.",
 "Ifone witnesses his own burial in the dream, then it means that his case is hopeless and that he will be seized by the world.",
 "buried in the dream. Ifone witnesses",
 "a deceased person has returned to life in a dream, it means that one will recuperate something he considered it dead",
 "happens to be going through difficulties, it means that his adversities will dissipate",
 "If a deceased person comes back to life in a dream, it also means that his progeny will benefit from something he left",
 "If he looks beautiful, happy and well dressed in the dream, it means that such happiness will become the inheritance of his descendants",
 "If one sees a deceased person busy, worried and ill dressed in a dream, it means that he is engaged in a struggle that can only subside by the will of God",
 "If the deceased person's face looks dark or opaque in the dream, it means that he died as an unbeliever",
 "deceased person sprightly, pleasant and casual in a dream, it means that one's dream is mere hallucination",
 "dead people do not joke and have their own duties to respond to",
 "Ifone's deceased\nfather or mother come back to life in a dream, it means relieffrom distress and\nabolishing of his fears",
 "particularly stronger when one's deceased mother is seen in the dream",
 "Resurrecting a deceased person in a dream means giving guidance to an unbeliever or admonishing an innovator",
 "If one sees a deceased person die again in a dream, it means that someone by the same name will shortly die",
 "If a deceased person complains about a migraine headache in a dream, it means that he is being questioned about his religious negligence",
 "dead people coming out of their graves and going to their homes in a dream, it means a mass release of prisoners during a general amnesty",
 "give life to a barren land",
 "death of a prophet in a dream means weakness in people's religious life, while their coming back to life in a dream means a flourishing spiritual life",
 "To come back to\nlife after dying in a dream means that one will become rich and dispense with\npoverty",
 "What a deceased person\nsays about himself in a dream is true, for he has reached the abode of truth",
 "If a deceased person tells something\nin a dream, and ifit does not take place, then it means that one is experiencing\nconfused dreams",
]
AR347 = [
 "(ومن رأى) أنه عاش بعد موته فإنه يستغني بعد فقره أو يتوب من ذنبه وإن كان الرائي مسافراً رجع سالماً إلى وطنه",
 "موت المرأة المجهولة يدل على إمساك القطر عن الأرض فإن عاشت أحيا الله تعالى الأرض بالغيث",
 "ومن أخبره ميت أنه لم يمت فإنه في مقام الشهداء منعم في الآخرة",
 "وقيل الموت على الإطلاق زواج لأن الميت يحتاج إلى الطيب والغسل كالمتزوج",
 "من مات ودفن فإنه يموت بلا توبة وإن خرج من قبره فإنه يتوب",
 "وإن رأى شيئاً من هيئة الأموات كالغسل والكفن فذلك زيادة في نقص دينه",
 "وإذا وقع الموت في النساء فهو في الصبيان وبالعكس",
]
AR348 = [
 "ميتاً أنه حي فإنه يحيا له أمر ميت وإن كان في عسر فإنه يأتيه اليسر من حيث لا يشعر",
 "أمواتاً معروفين قاموا في موضع أو بلدة أو محلة فإنه يحيا له أو لعقب هؤلاء الأموات أمر",
 "وإن كانوا مكتسين أثواباً جدداً وكانوا فرحين فإنه يحيا لهم أو لعقبهم أمور فيها سرور وفرح ويتجدد إقبالهم ويحسن حالهم",
 "وإن كانت الأموات محزونين أو كانت ثيابهم وسخة فإن أحوالهم تتحول إلى الفقر والهم وكسب الذنوب",
 "وإن رأى أن الميت يمازح فليس ذلك برؤيا لأن الميت مشغول بنفسه عن المزاح",
 "أن أباه وأمه قد حييا وكان خائفاً أمن وانفرج وزال همه خصوصاً أمه",
 "أنه أحيا ميتاً فإنه يسلم على يديه يهودي أو نصراني أو صاحب بدعة",
 "وإن رأى أنه يحيي الموتى فإنه يهدي قوماً ضالين أو مبتدعين أو يتوب على يديه من هو مصر على الذنوب",
 "وإن كان مريضاً فإنه مسؤول عن دينه فيما بينه وبين الله تعالى خاصة دون الناس",
]
ZH = [
 "死人复活主有信","见人死自死皆吉","子死者主添喜事","见死亡尊长大吉","死人立者主大凶","死人哭泣有口舌","干鱼下水命复通",
]

fails=0
for t in EN:
    ok = norm(t) in ISN; print(('OK  ' if ok else 'MISS'), 'EN |', t[:90]); fails += not ok
for t in AR347:
    ok = norm(t) in P347N; print(('OK  ' if ok else 'MISS'), 'AR347 |', t[:60]); fails += not ok
for t in AR348:
    ok = norm(t) in P348N; print(('OK  ' if ok else 'MISS'), 'AR348 |', t[:60]); fails += not ok
for t in ZH:
    o1 = t in ZGN; o2 = t in CN
    print(('OK  ' if (o1 and o2) else 'MISS'), 'ZH |', t, '| corpus:',o1,'| 10huan:',o2); fails += not (o1 and o2)
print('TOTAL FAILS', fails)
