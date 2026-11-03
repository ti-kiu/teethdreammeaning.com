#!/usr/bin/env python3
"""Wedding page quote verification — every assertion must hit source verbatim.
EN: /root/dream_research/ibn_sirin_full.txt (compilation OCR)
AR: /root/dream_research/nabulsi_page_145.txt / _289.txt / p347_349.txt (shamela)
ZH: zhougong_yuanban.txt (ch.14 appended today, cross-checked) + Dunhuang recension sources
"""
import re

IBN = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8', errors='ignore').read()
NAB145 = open('/root/dream_research/nabulsi_page_145.txt', encoding='utf-8', errors='ignore').read()
NAB289 = open('/root/dream_research/nabulsi_page_289.txt', encoding='utf-8', errors='ignore').read()
NAB347 = open('/root/dream_research/nabulsi_p347_349.txt', encoding='utf-8', errors='ignore').read()

def norm_en(t):
    t = t.replace('\u00ad', '').replace('-\n', '').replace('\n', ' ')
    t = re.sub(r'DICTIONARY OF DREAMS \d+|\d+ IBN SEERIN[^\s]*|IBN SEERIN[^\s]*', ' ', t)
    return re.sub(r'\s+', ' ', t)

def norm_ar(t):
    t = re.sub(r'[\u064B-\u0652\u0670\u0653-\u0655\u0640]', '', t)
    for a in 'أإآٱ':
        t = t.replace(a, 'ا')
    t = t.replace('ى', 'ي').replace('ة', 'ه')
    return re.sub(r'\s+', ' ', t)

IBN_N, A_N = norm_en(IBN), None
N145, N289, N347 = norm_ar(NAB145), norm_ar(NAB289), norm_ar(NAB347)

EN = [
 "Marriage in a dream represents the providence of God Almighty and care for His servants",
 "Marriage in a dream also means imprisonment, indebtedness, sorrow, distress, depression, carrying a liability, or endeavoring to achieve a high ranking position",
 "If one marries a known woman in his dream, it means that he will endeavor to satisfy the normal responsibilities of a husband",
 "it denotes the nearing of his death, or it could mean moving from an old house into a new one",
 "If a sick woman sees herself getting married to a man she does not recognize or know his name in a dream, it means that she may die from her illness",
 "If the man who sees himself getting married in the dream qualifies, it means that he will attain a high ranking job or a suitable position",
 "If one's wedding ceremony is made with witnesses only in the dream, it means that he has made a covenant with God Almighty",
 "If he performs a traditional wedding ceremony with its celebrations and festivities in the dream, it means a new job, or it could mean acquiring fame, or becoming renowned for one's good reputation or character",
 "Marriage in a dream is also interpreted in association with a trade",
 "it means that he will perform a job that earns him nothing but hard labor, toiling and stress",
 "If one marries an adulteress in a dream, it means that he is an adulterer",
 "it means that his movements will be hampered with various restrictions",
 "If one marries a deceased woman in a dream, it means that he will revive a profitable project he had earlier abandoned",
 "If a man offers his mother in marriage to one of his friends in a dream, it means that he will sell his house",
 "If a pregnant woman sees herself getting married in a dream, it means that she will give birth to a girl",
 "If she sees herself in her wedding night in a dream, it means that she will beget a son",
 "If a mother who has a son sees herself getting married in a dream, it means that she will marry off her son",
 "In general, the marriage of a married woman, or of an unwed woman in a dream means benefits",
 "If a woman marries a deceased man in a dream, it means that she will become lost and impoverished",
 "If a married man sees himself getting married to a second woman in a dream, it means profits",
 "To marry the daughter of a known man of knowledge in a dream means prosperity",
 "it means that he will sever his ties with such a relative, or with her family",
 "To rescind one's bond of marriage in a dream means either death or dismissal from work",
 "To revoke the bond of marriage in a dream also may mean selling a product for a term, requiring its return, or it may mean apostasy",
 "If one sees himself as a bridegroom on his wedding night, accompanied with musicians and dancers in the dream, it means that he may die in that place",
 "If one sees himself having marital intercourse with his bride, but could not see her or recognize her, nor is she named to him in the dream, it also means his death",
 "If one sees and recognizes his bride, or if she is named as his bride in the dream, then it means acquiring wealth",
 "it means wealth in this world",
 "it means his death or that he may commit a murder",
 "it means that he will marry the same woman",
 "he will gain power equal to the position of that woman, her role, danger, her family's status, the meaning of her name, and her beauty",
 "Death in a dream also signifies marriage, for a deceased person is washed and perfumed, and a bridegroom also takes a bath and anoints himself with perfumes on his wedding day",
 "An officiant in a dream means a wedding, a divorce, or he could represent a pimp, depending on the mental condition, or the type of work one who is seeing the dream performs",
 "If one gives a dower for an undefined purpose in his dream, it means that he will fulfill his obligatory duties or comply with a religious injunction",
 "A wife in a dream represents a partner, an enemy, an unjust ruler, one's opponent, prosperity, a vehicle, earthly wealth, worldly pleasures",
]

AR = [
 # Nabulsi (زواج) headword paragraph, shamela 145 (printed 148)
 "(زواج) في المنام يدل على العناية من الله تعالى وربما دل الزواج على الأسر والدين والغم والهم والدخول في الضمان أو السعي في تولية المناصب الجليلة فإن تزوج امرأة معروفة سعى فيما يستطيع القيام به وإن تزوج امرأة مجهولة أو لم ير في المنام امرأة دل ذلك على قرب الأجل والرحلة من دار إلى دار وإن كان صالحاً للإمارة تأمر أو الولاية تولى أو نال منصباً يليق به وإن كان الزواج في المنام بمجرد شهوة كان عقداً مع الله صالحاً وإن كان بزفاف على جاري العادة فهو منصب أو صيت حسن يرتفع له والزواج يعبر بالحرفة فمن رأى أنه تزوج امرأة وماتت فإنه يعمل في حرفة لا ينال منها إلا العمل والعناء والهم ومن تزوج في المنام بأربعة نسوة فإنه ينال زيادة.",
 # trades clauses
 "أنه تزوج بامرأة يهودية فإنه يسعى في حرفة ينال منها إثماً واجتراء على المعاصي",
 "أنه تزوج بامرأة نصرانية فإنه يسعى في حرفة فيها باطل وافتتان وإن كانت مجوسية فهي حرفة بلا دين ومن تزوج بزانية فهو زان ومن تزوج بزوجة سليطة عليه فإنه يقيد بقيد ثقيل ومن تزوج بكلبة فإنه يملك أمراً دنيئاً",
 "أنه تزوج بنت سلطان بالمعازف والقيان فإنه يشرب بنت نفاق وهي الخمر أو ما يفعل فعله",
 "إنساناً تزوج بامرأة ونقلها إليه فإنه ينال مالاً من زوج المرأة",
 # sick/bathhouse/sultan's wife/dead woman/pregnant block
 "ومن تزوج بامرأة ميتة ظفر بأمر ميت قد أيس منه وإذا تزوجت المرأة المريضة ولم تعاين الزوج ولا عرفته ولا تسمى لها فإنها تموت وكذلك الرجل المريض إذا تزوج في منامه ولا عاين المرأة ولا سميت له فإنه يموت ومن زوج أمه بإنسان باع عقاره وإذا رأت الحبلى أنها تزوجت فإنها تضع جارية وإذا جليت كالعروس فإنها تضع غلاماً وإذا رأت المرأة التي لها ابن أنها تزوجت فإنها تزوج ابنها وإن تزوجت المرأة العزباء والمزوجة في المنام نالت خيراً وإذا تزوجت المرأة برجل ميت تشتت شملها وافتقرت",
 "أنه تزوج بامرأة ودخل بها فإنه يظفر بأمر ميت بحياله وهو في الأمور بقدر جمال تلك المرأة فإن لم يكن دخل بها فإن ظفره بذلك الأمر يكون دون ما لو دخل بها",
 "أنه تزوج امرأة وله زوجة أو زوجات أصاب خيراً وسلطاناً لقدر جمال المرأة وهيئتها إذا عاينها أو عرفها فإن هو لم يعرفها ولا سميت له وكانت تجهز له فإن ذلك دليل على موته أو موت إنسان على يديه",
 "أنه تزوج ابنة شيخ مجهول له فإنه يصيب خيراً كثيراً وإن رأت امرأة أنها تزوجت شيخاً مجهولاً فإنها تصيب خيراً كثيراً وإن كانت مريضة أفاقت من مرضها",
 "أنه تزوج امرأة ميتة من ذوات محارمه فإنه يصل رحمها وإن كانت حية قطع رحمها",
 "أنه تزوج ذات محرم فإنه يسود أهل بيته والزوجة في المنام شريك أو عدو أو سلطان جائر أو خصم ألد أو ملك أو مركب أو مركوب وكل ما دلت الأرض عليه من راحة أو تعب أو خير أو شر فانسب للزوجة مثله لدلالته عليها",
 "زوجته تزوجت برجل حمامي يعرض لها الحمى الملازمة لها ومن تزوج بزوجة السلطان نال ملكاً إن كان لذلك أهلاً وإلا تولى ولاية",
 # death=marriage mirror clause, shamela 344 (printed 347)
 "وقيل الموت على الإطلاق زواج لأن الميت يحتاج إلى الطيب والغسل كالمتزوج",
 # Kaaba headword cross-ref تزويج, shamela 289 (printed 292)
 "كعبة) هي في المنام خليفة أو وزير أو رئيس أو تزويج",
]

fails = 0
for i, s in enumerate(EN):
    if norm_en(s) not in IBN_N:
        fails += 1; print(f"EN[{i}] MISS: {s[:80]}")
for i, s in enumerate(AR):
    n = norm_ar(s)
    if not (n in N145 or n in N289 or n in N347):
        fails += 1; print(f"AR[{i}] MISS: {s[:70]}")
print(f"checked EN={len(EN)} AR={len(AR)} FAILS={fails}")
