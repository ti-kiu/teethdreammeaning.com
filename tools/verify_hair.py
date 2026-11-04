#!/usr/bin/env python3
"""Verify every quote for the hair page verbatim against source files. FAILS=0 required before publishing."""
import re, sys

src_en = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()
src_ar_192 = open('/root/dream_research/nabulsi_page_192.txt', encoding='utf-8').read()
src_ar_193 = open('/root/dream_research/nabulsi_page_193.txt', encoding='utf-8').read()
src_ar = src_ar_192 + "\n" + src_ar_193
src_zg = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()

EN = [
 "Hair: In a dream, hair represents money and longevity.",
 "it means increase of his wealth and growth of his business based on a business loan or a mortgage",
 "If one sees his straight hair frizzed or curled in a dream, it means that he will be honored",
 "humiliation or lose his rank",
 "If one's hair looks curly in a dream, it means that power, honor and praises will be the lot of his superior",
 "If a sick woman sees herself braiding her hair in a dream, it means that she will die from her illness",
 "it means debts.",
 "Shaving one's moustache, or under one's armpit in a dream means paying",
 "one's debts, dispelling distress, or following good hygienes",
 "Shaving one's head during the pilgrimage season in a dream means safety and protection",
 "Shortening one's hair, or removing unwanted hair during makeup in a dream means dispelling",
 "stress, or being coerced to pay one's debts",
 "If one sees himself having hair like that of a hog in a dream,",
 "it connotes major calamities",
 "If an unhappy person sees himself hairy in a dream, it means aggravation of his depression and unhappiness",
 "The black hair of a woman in a dream represents her husband's love for her",
 "it means that she will suffer slander and defamation",
 "it means that he will molest male",
 "suffer harm from his evil actions",
 "If one sees his hair infested with lice in a dream, it means that he has a large family",
 "Having less hair in a dream means diminishing difficulties",
 "If one sees someone pulling out his hair in a dream, it means that he may have to face a financial disaster",
 "If a woman sees a strand of her hair being cut in a dream, it means a fight between",
 "her and her husband",
 "Nicely combing one's hair in a dream means loyalty and fulfilling a promise",
 "Combing the hair of one's wife in a dream means divorce",
 "Good looking hair in a dream represents a person of good character",
 "Hair in a dream also denotes farming, money, a wife, a husband or",
 "marriage",
 "If one sees his",
 "hair growing anew in a dream, it means that he may lose most of his wealth",
 "If one sees hair growing on his face where hair does not usually grow in a dream,",
 "it means debts",
 "If one sees hair growing in the palm of his hand in a dream, it",
 "means benefits from a business",
 "hair on his forearm scattering, or falling in a dream, it means that he may lose",
 "all his savings",
 "A hairy child in a dream means longevity",
 "If one's hair turns white in a dream, it means loss of money for a rich person, or paying",
 "the debts of a poor person",
 "Braiding: (Hair; Intertwine; Plait) Braiding women's hair in a dream is a sign of",
 "braiding one's hair in a dream represents complications in one's life,",
 "unbearable debts, or confusion",
 "Shaving: Shaving one's hair in a dream relates to one's personal customs",
 "he will pay a fine as an atonement",
 "recovering from a migraine headache",
 "If one sees his hair shaved during the",
 "winter in a dream, it means difficulties, adversities, penalties, or a sickness",
 "If one is suffering from depression and he sees his head", "shaved in a dream, it means an end to his trouble, or payment of his debts",
 "If a soldier sees his head shaved in a dream, it means that he will lose his strength and esteem",
 "If a woman sees her head shaved", "in a dream, it means divorce, or the death of her husband",
 "Trimming",
 "Cutting one's hair",
 "in a dream means losing one's strength",
 "If a pregnant WOman sees a strand of hair in her",
 "dream, it means that she will beget a blessed son",
 "A strand of hair hanging over", "one's head in a dream means money",
 "Haircut: A short haircut in a dream means failure to properly fulfill one's duties",
 "Hair in one's ears in a dream",
 "means knowledge, or admonition. Seeing hair in one's noses in a dream",
]
# some casing fixes: line-broken joins normalized
def norm(s): return re.sub(r'\s+', ' ', s)
en_n = norm(src_en)
fails = 0
for q in EN:
    if norm(q) not in en_n:
        print("EN MISS:", q[:90]); fails += 1

AR = [
 "(شعر الرأس) هو في المنام مال وطول عمر فمن رأى أن شعر رأسه طال فإنه يطول عمره",
 "وإن رأى أن على رأسه جمة شعر فوصلها بشعر آخر فإن كان غنياً ازداد ماله",
 "وإن كان فقيراً فإنه قد اجتمع عليه دين ويستدين لغيره",
 "وإن رأى أن شعره السبط جعد فإنه يتضع ويصير دون ما كان عليه",
 "جمة الشعر لحملة الصلاح وقاية",
 "ومن رأى أن له شعراً طويلاً وهو مسرور به فإن ذلك محمود خصوصاً في النساء",
 "حلق شعر رأسه وقصه في زمن الحج يدل على الأمن",
 "وقيل نتف الشعر يدل على وفاء دين الرائي على كره منه",
 "وإذا رأى الهاشمي طول شعره ملك الرقاب",
 "ومن رأى شعره كشعر الفرس فإنه يمسك ويقبض عليه إن كان لصاً أو آبقاً وإن رأى ذلك حر فليحذر أن يصير",
 "ومن رأى شعره صار كشعر الخنزير أصابته شدائد",
 "وكثرة الشعر للمهموم زيادة في همه",
 "وسواد شعر المرأة يدل على محبة زوجها لها",
 "فإن رأت امرأة أنها كشفت شعرها فإن زوجها يغيب عنها",
 "وإن رأت أنها لم تزل مكشوفة الرأس فإن زوجها لا يرجع إليها",
 "وإن رأت شعرها كثيفاً وأبصر الناس ذلك منها فإنها تفتضح في أمرها",
 "فإن رأى الرجل أن على رأسه قروناً من شعر فإنه رجل منيع",
 "وإن رأى أن شعر مؤخر رأسه قد انتثر أصابه ذل في الوقت",
 "دل على أنه يصاب بالذكور من أقربائه",
 "فإن كان شعر الجانب الأيسر فإنه يصاب بالإناث منهم",
 "إن رأت إنساناً يجز شعرها من ورائها",
 "ومن رأى أنه دهن شعره بدهن فهو زينة له",
 "إن سال عليه الدهن أصابه هم وغم",
 "فإن وجد رائحة فذلك ثناء حسن",
 "ومن رأى أنه يفلي رأسه فإنه يطلع على بعض عيوبه",
 "فإن ماله قد ذهب أو يذهب إلا أقله",
 "(ومن رأى) الشعر ينبت في وجهه أو حيث لا ينبت الشعر فإنه يكثر عليه الدين",
 "والشعر في الصدر واللسان حكمة وبيان وشعر وفطنة إلا أن يخرج عن الحد فيعود إلى الهموم والكمد والحزن",
 "(ومن رأى) شعر بطنه كثر فإنه كثير الدين مهموم",
 "(ومن رأى) أن شعر ذراعيه يتناثر فإن جميع ما اكتسبه يذهب عنه",
 "وإن رأى أنه تساقط فإن جميع ما سعى به وكده ذاهب",
 "رؤية المرأة شعر رأسها دال على من يسترها",
 "قصره وبياضه ونتن رائحته دليل على قبح حالهم",
 "وحلقه أو تقصيره لمن لا يؤثر ذلك مقاطعة أو تبذير للمال",
 "تقصيره دليل على العلم والهدى",
 "وإذا ضفر شعر المرأة ثلاثة قرون طلقت من زوجها ثلاثاً وإن كانت مريضة ماتت",
 "وإن صار شعر الآدمي كشعر غيره من الحيوان دل على الجهد والتعب",
 "شعر الأذن علم أو كلام يسمعه",
 "وشعر الأنف خبر يتنسمه فيه نكد أو مال مخفي",
 "والشعر للطفل دليل على طول عمره",
 "طول الشعر لمن لا يليق به دليل على الهموم والأنكاد والديون",
 "وضفر الشعر يدل على إتقان الأمور",
 "وضفر شعر النساء دليل خير",
 "وإزالة شعر الشارب والإبط دليل على قضاء الديون وذهاب الهم",
]
ar_n = re.sub(r'\s+', ' ', src_ar)
for q in AR:
    if norm(q) not in ar_n:
        print("AR MISS:", q[:80]); fails += 1

ZG = [
 "头白主长命大吉",
 "头生两角有争竞",
 "头秃发落皆凶事",
 "头须自落忧子孙",
 "头须再生主长命",
 "剪剃头发家内凶",
 "妇人披头有私情",
 "露头披发阴人谋",
 "披头盖面官讼至",
 "眉与发齐禄位至",
 "梳头洗面百忧去",
 "齿自落者父母凶 齿落更生子孙兴",
]
for q in ZG:
    if q not in src_zg:
        # corpus may be simplified chars
        import unicodedata
        print("ZG MISS:", q); fails += 1

print("FAILS =", fails)
sys.exit(1 if fails else 0)
