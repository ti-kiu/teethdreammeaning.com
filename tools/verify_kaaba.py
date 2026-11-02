import re, json

IS = open('/root/dream_research/ibn_sirin_full.txt').read()
NAB = json.load(open('/root/.hermes/nabulsi_p2_120.json'))
P292 = NAB['289']['txt']
ZG = open('/root/dream_research/zhougong_yuanban.txt').read()

def norm(s):
    s = re.sub(r'\s+', ' ', s)
    # strip OCR running heads so sentences split across page boundaries join up
    s = re.sub(r'\d{3} (?:IBN [A-Z:·\'()ÙÜÍÉ!1]+[\'::)·]*|DICTIONARY OF DREAMS \d+)', ' ', s)
    return s

ISN, P292N, ZGN = map(norm, (IS, P292, ZG))

EN = [
 "the holy Ka'aba represents the calif of all Muslims, his chief minister, a leader of a country, or it may represent a wedding",
 "Seeing the holy Ka'aba in a dream also means that one may enter it, or it could mean receiving glad tidings and dispelling evil",
 "Praying inside the holy Ka'aba in a dream means enjoying the guardianship and protection of someone in authority, and safety from one's enemy",
 "Entering inside the holy Ka'aba in a dream means entering before a ruler",
 "Taking something from inside the holy Ka'aba in a dream means receiving something from the ruler",
 "Ifone of the walls of the holy Ka'aba crumbles in a dream, it means the death of the Calif or the local governor",
 "Entering the holy Ka'aba and failing to perform any of the prescribed rites in a dream means standing before God Almighty on the Day of Judgment having performed one's obligations, or it could mean repenting from one's sins",
 "To look at the holy Ka'aba in a dream means safety and protection against fear",
 "If one is given a job in Mecca in a dream, it means that he may become an Imam",
 "Stealing anything from the holy Ka'aba in a dream means committing a sin",
 "Walking toward the holy Ka'aba, or seeking it in a dream means correcting one's religious standing",
 "Seeing oneself in Mecca mixing with departed souls who are inquiring from him about the world in a dream means to die testifying to the Oneness of God Almighty and to the prophethood of His Messenger",
 "Seeing the Ka'aba inside one's own house in a dream means that one is still in power and living with grace",
 "If the holy Ka'aba does not look right in one's eyes in the dream, then it means adversities",
 "it means that one truly follows the Imam",
 "Praying on top of the holy Ka'aba in a dream means becoming an apostate",
 "Entering the holy Mosque in Mecca and praying on the roof of the holy Ka'aba in a dream represents peace, tranquility, presiding over others",
 "though with a questionable conduct, he also may follow innovation and depart from the traditions and teachings of God's Messenger",
 "If one sees angels descending from the heavens to lift away the pillar of God's House from Mecca and place it in a different town in the dream, it means that people have gone astray and the time of destruction has come",
 "If one sees the holy Ka'aba burning in a dream, it means that one has neglected or abandoned his prescribed prayers",
 "Any changes, decrease or increase in the shape of the holy Ka'aba, moving of it away from its place, or changing its look in a dream will reflect upon the Imam, or the guide of all Muslims",
 "Circumambulating the holy Ka'aba or performing any of the prescribed rites in a dream means walking the path of righteousness, or correcting one's religious life as much as one does in his dream",
 "such innovation is equal to changing the direction (arb. Qiblah) of one's prayers",
 "The holy Ka'aba in a dream also represents one's prayers, for it is the focal point of all praying Muslims",
 "it represents a teacher, a guide, Islam, the holy Qur'an, the prophetic traditions, one's son, a religious scholar, a shaikh, a master, a husband, one's mother, and the heavenly paradise",
 "If one sees that his own house has become the Ka'aba and people are seeking it and crowds are gathering at his door in a dream, it means that he will be endowed with wisdom, gain knowledge and act upon it",
 "one may work for someone in authority, or serve a man of knowledge, a shaikh, a renunciate, one's father, one's mother",
]

AR = [
 "(كعبة)  هي في المنام خليفة أو وزير أو رئيس أو تزويج وربما يدخلها من رآها.",
 "الكعبة هو بشير له بخير يقدمه أو يدبر عنه شر ينويه أو يهم به",
 "فإنه يتمكن من رئيس أو إمام شريف ويأمن من الأعداء وينال خيراً",
 "فإنه يدخل على الخليفة وإن أخذ منه شيئاً فإنه ينال من الخليفة شيئاً",
 "وإن رأى حائطاً من حيطانها سقط فإنه يدل على موت الخليفة",
 "وإذا أتى الكعبة ولم يعمل فيها من المناسك شيئاً فإنه يأتي الله تعالى بالقيام بما أمره من الفرائض أو كفارة يمين",
 "والنظر إليها أمن مما يخافه",
 "وإن ولي أمراً بمكة فإنه يلي أمراً من أمور الإمام",
 "وإن رأى أنه سرق من الكعبة رماناً فإنه يأتي ذات محرم",
 "وإن رأى أنه توجه نحوها وأقبل عليها فإنه يصلح دينه",
 "وإن رأى أنه بمكة بين الأموات يسألونه فإنه يموت على الشهادة",
 "وإن رأى أنه أحدث في الكعبة فإنها مصيبة يصاب بها الإمام الأعظم",
 "وإن رأى أن الكعبة في داره فإنه لا يزال ذا سلطان وخدم وصيت في الناس",
 "إلا أن يرى الكعبة هيئة في سوء حال فذلك لا خير فيه لصاحب المنزل",
 "وإن رأى أن داره الكعبة فإن الكعبة إمام المسلمين فهو لا يزال مع الإمام",
 "أنه يصلي فوق الكعبة فإنه يرتد عن دين الإسلام",
 "أنه دخل الحرم وصلى على سطح الكعبة فإنه ينال أمناً وولاية ويجبي جباية من ملك مكان مع سوء المذهب ومخالفة السنة",
 "أنه يخطى الكعبة فإنه يخالف سنة رسول الله صلى الله عليه وسلم ويدخل في مذهب أهل الأهواء",
 "أن الملائكة عليهم السلام نزلوا من السماء ورفعوا عمود البيت فوضعوه في بلدة فإن الفتنة إذا وقعت في الأرض كان الإمام في تلك البلدة",
 "أن الكعبة قد خربت فإنه تارك الصلاة",
 "(ومن رأى)  أنه طاف بالكعبة أو عمل في شيء من المناسك فإنه صلاح في دينه بقدر ما عمل من المناسك",
 "أنه متوجه نحو الكعبة فإنه مقبل على ما يصلح دينه ودنياه أو متوجه إلى السلطان ليخالطه في بعض سلطانه",
 "الكعبة قد خربت فإنه تارك الصلاة",
 "أنه يطوف حولها أو يعمل عملاً من مناسكها خدم سلطاناً أو عالماً أو عابداً أو والداً أو والدة أو زوجة أو سيداً بنصح وبر وتعب",
 "وتدل على من",
 "الوالدة وقد تدل على الجنة لأنها بيت الله والجنة داره بها يوصل إليه",
 "أنه نقص من المناسك شيئاً على خلاف السنة فإن ذلك تحريف في دينه على نحو تحريف القبلة في صلاته",
 "والكعبة تدل على الصلاة لأنها قبلة المصلين",
 "وقد تدل على الموسم والجماعات والأسواق والرحاب",
 "فإنه ينكح امرأة شريفة من أهل الخير والصلاح",
 "وإن كان عبداً أعتقه سيده",
 "خدم سلطاناً أو عالماً أو عابداً أو والداً أو والدة أو زوجة أو سيداً بنصح وبر وتعب",
]

ZH_ABSENT = ["克白", "克尔白", "天房", "麦加", "朝觐"]
ZH_NEAREST = ["拜星月烧香大吉", "礼拜日月大吉昌"]

fails = 0
for t in EN:
    ok = norm(t) in ISN; print(('OK  ' if ok else 'MISS'), 'EN |', t[:80]); fails += not ok
for t in AR:
    ok = norm(t) in P292N; print(('OK  ' if ok else 'MISS'), 'AR |', t[:60]); fails += not ok
for t in ZH_ABSENT:
    print(('OK-absent  ' if t not in ZGN else 'PRESENT!'), 'ZH |', t)
for t in ZH_NEAREST:
    print(('OK  ' if t in ZGN else 'MISS'), 'ZH-nearest |', t)
print('TOTAL FAILS', fails)
