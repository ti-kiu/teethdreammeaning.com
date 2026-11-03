#!/usr/bin/env python3
"""Source-side verbatim verification for /dream/gold/.

Checks (2026-11-03):
- Ibn Sirin compile (Pearl 1992) "Gold" entry assertions, line-start 11883 (index: Gold 189)
- Nabulsi shamela 124 (ص127) (ذهب) entry + shamela 125 (ص128) gold/silver transformation passage
- Zhougong 原版 chapter 9 gold lines
Every assertion is a verbatim substring of the source file. FAILS must be 0 before page build.
"""
import re

SRC_IBN = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8', errors='ignore').read()
SRC_N124 = open('/root/dream_research/nabulsi_page_124.txt', encoding='utf-8').read()
SRC_N125 = open('/root/dream_research/nabulsi_page_125.txt', encoding='utf-8').read()
SRC_ZG = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()

def norm_ar(t):
    t = re.sub(r'[\u064B-\u0652\u0670\u0653-\u0655\u0640]', '', t)
    for a in 'أإآٱ':
        t = t.replace(a, 'ا')
    t = t.replace('ى', 'ي').replace('ة', 'ه')
    return re.sub(r'\s+', ' ', t)

N124 = norm_ar(SRC_N124)
N125 = norm_ar(SRC_N125)
IBN = re.sub(r'\s+', ' ', SRC_IBN)

fails = []

def chk(label, hay, needle):
    ok = needle in hay
    if not ok:
        fails.append(label)
    print(('PASS' if ok else 'FAIL'), label)

# --- Ibn Sirin "Gold" entry (English compile) ---
chk('IBN: disliked element damages anxiety losses', IBN, 'gold is a disliked element which cause damages, anxiety and losses')
chk('IBN: golden bracelet = inheritance', IBN, 'Wearing a golden bracelet in a dream means receiving an inheritance')
chk('IBN: golden ornament = marriage incompatible person', IBN, 'marriage to an incompatible person')
chk('IBN: golden bar = losing money or business', IBN, 'Receiving a golden bar in a dream means losing money or business')
chk('IBN: melting bar = persecuted loathsome act talk of town', IBN, 'persecuted for committing a loathsome act and he will become the talk of the town')
chk('IBN: broken chips/whole coin = meeting ruler', IBN, 'means meeting with the ruler of the country or with the governor of town')
chk('IBN: minting gold = evil death destruction', IBN, 'Minting gold in a dream represents evil, death or destruction')
chk('IBN: house turning gold = fire consume', IBN, 'means that a fire will consume his house')
chk('IBN: hand turns gold = paralyzed', IBN, 'it means that it may be paralyzed')
chk('IBN: eyes turn gold = blind', IBN, 'means that he may become blind')
chk('IBN: necklace = leader or something in trust', IBN, 'become a leader, or that he could receive something in trust')
chk('IBN: gold = festivities joy profits good deeds stress marriage children knowledge guidance', IBN, 'festivities, joy, profits, good deeds, dispelling stress, marriage, children, knowledge, spiritual guidance')
chk('IBN: gold turning silver = decrease women children properties', IBN, 'means decrease in value, or changing conditions in relation to women, children or properties')
chk('IBN: silver turning gold = increase rising moon', IBN, 'means increase in value, the rising moon of one')
chk('IBN: gold embroidered garment = religious offerings', IBN, 'means religious offerings')
chk('IBN: gold plated = emulating mundane people', IBN, 'means emulating mundane people')
chk('IBN: pure gold/silver = purity sincerity covenant peace treaty', IBN, 'means purity and sincerity of one')
chk('IBN: plated/leaf = short life changing circumstances sleepless nights forgetfulness', IBN, 'represent a short life, changing circumstances')
chk('IBN: handmade jewelry = perpetual earnings', IBN, 'means perpetual earnings')
chk('IBN: Goldsmith entry exists (see Goldsmith cross-ref)', IBN, 'Goldsmith: (Jeweler) In a dream, a goldsmith represents celebrations, joy')

# --- Nabulsi shamela 124 (ص127) (ذهب) entry ---
chk('N124: headword (ذهب) disliked burdensome loss of property', N124, norm_ar('(ذهب) هو في المنام أمر مكروه وغرم مال'))
chk('N124: bracelet worn = inheritance falls in hand', N124, norm_ar('والسوار منه إذا لبسه ميراث يقع في يده'))
chk('N124: wearing gold = marries unfit people (يصاهر قوماً غير أكفاء)', N124, norm_ar('فإنه يصاهر قوماً غير أكفاء له'))
chk('N124: ingot = money loss or sorrow proportionate', N124, norm_ar('فإن أصاب سبيكة ذهب منه مال أو أصابه هم بقدر ما أصاب من الذهب'))
chk('N124: ruler anger + fine', N124, norm_ar('أو غضب عليه السلطان وغرمه'))
chk('N124: melting gold = dispute in detestable matter + tongues of people', N124, norm_ar('فإن رأى أنه يذيب الذهب خوصم في أمر مكروه ووقع في ألسنة الناس'))
chk('N124: given large piece = sultan + leadership', N124, norm_ar('فإنه ينال سلطاناً ورياسة'))
chk('N124: found broken gold/sound dinars = sees ruler face returns safe', N124, norm_ar('فإنه يرى وجه الملك ويرجع منه سالماً'))
chk('N124: minting (سبك) = evil and perdition', N124, norm_ar('فإن رأى أنه سبك ذهباً نال شراً وهلاكاً'))
chk('N124: house of gold = fire', N124, norm_ar('ومن رأى أن بيته من ذهب أصابه حريق'))
chk('N124: hands of gold = paralyzed no movement', N124, norm_ar('أن يديه من ذهب بطلتا وصارتا بلا حركة'))
chk('N124: eyes of gold = blind', N124, norm_ar('أن عينيه من ذهب عمي بصره'))
chk('N124: necklace gold/silver/gems = wilayah + trust', N124, norm_ar('أن عليه قلادة من ذهب أو فضة أو خرز أو جوهر ولى ولاية وتقلد أمانة'))
chk('N124: gold vision = joys provisions good deeds worries depart wives children knowledge guidance', N124, norm_ar('والذهب تدل رؤيته على الأفراح والأرزاق والأعمال الصالحة وذهاب الهموم'))

# --- Nabulsi shamela 125 (ص128) transformation passage ---
chk('N125: gold→silver = state change increase→decrease (women wealth children servants)', N125, norm_ar('والذهب إذا صار في المنام فضة دل على تغير حال من دل عليه من النساء والأموال والأولاد والخدم من الزيادة إلى النقص'))
chk('N125: silver→gold = good state (wives family folk)', N125, norm_ar('كما أن الفضة إذا صارت في المنام ذهباً دل على حسن حال من دل عليه من الأزواج أو الأهل أو العشيرة'))
chk('N125: gold-woven/embroidered high garments = nearness to God or tribulation', N125, norm_ar('قربات إلى الله سبحانه لمن لبس ذلك من نساء أو أزواج أو أولاد أو إماء أو بلاء لأربابها'))
chk('N125: plated = resembling people of dunya', N125, norm_ar('فإنه يدل على التشبه بأبناء الدنيا'))
chk('N125: pure (خالص) gold/silver = sincerity + sound covenant', N125, norm_ar('والخالص من الذهب والفضة يدل على الإخلاص وصفاء النية والمعاقدة والعهد الصحيح'))
chk('N125: leaf/plating removal = short deeds fluctuation forgetting', N125, norm_ar('فإنه يدل على الأعمال القصيرة وتقلبات الأمور والسهو والنسيان'))
chk('N125: spun/drawn (المغزول) gold/silver = continuous provision', N125, norm_ar('والمغزول من الذهب والفضة رزق مستمر'))
chk('N125: (ذهبي) goldsmith-seller vision = joys; mixing truth with falsehood', N125, norm_ar('هو بائع الذهب المغزول تدل رؤية كل منهما على الأفراح والمسرات وربما دل على من يمزج الحق بالباطل'))

# --- Zhougong chapter 9 (金银珠玉绢帛) ---
chk('ZG: 金银宝者主富贵', SRC_ZG, '金银宝者主富贵')
chk('ZG: 金银珠玉大吉利', SRC_ZG, '金银珠玉大吉利')
chk('ZG: 金银杯皿有贵孕', SRC_ZG, '金银杯皿有贵孕')
chk('ZG: 金银作铛器大吉', SRC_ZG, '金银作铛器大吉')
chk('ZG: 得金玉环生贵子', SRC_ZG, '得金玉环生贵子')
chk('ZG: 玉积如山大富贵', SRC_ZG, '玉积如山大富贵')

print()
print('FAILS =', len(fails), fails)
