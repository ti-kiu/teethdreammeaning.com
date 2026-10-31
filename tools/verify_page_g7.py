#!/usr/bin/env python3
# FINAL page-gate for gap #7: every quoted fragment on the live page must
# appear verbatim in its source file. Also structural checks.
import re, sys

PAGE = open('/root/teethdreammeaning/site/dream/teeth-falling-out-and-death/index.html', encoding='utf-8').read()
AR = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
EN = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()
PM = open('/root/.hermes/cache/web/pubmed.ncbi.nlm.nih.gov-7450fdf5d0.md', encoding='utf-8').read()
FM = open('/root/.hermes/cache/web/www.frontiersin.org-fc4707a4dd.md', encoding='utf-8').read()

ARQ = [
 "فإنه يغترب عن عشيرته واحد فإن أصابه بعدما فقده رجع وإلا فلا يرجع",
 "فإن تحرك منها سن واحدة من هؤلاء فمرض فإن سقطت أو ضاعت فإنه موت من ينسب إليه هؤلاء أو غيبته عنه غيبة لا يرونه بعد ذلك فإن أمسكها ولم يدفنها فإنه يستفيد بدلها من يكون له مثل ذلك القريب الذي ينسب إليه تلك السن في التأويل فإن دفنها فإنه موت ذلك القريب",
 "فإن أهل بيته يموتون قبله وربما كان ذلك موت ذوي سنه أو مرض أهل بيته",
 "وربما كان المغرم على قدر دية السن في الشرع",
 "يموت إلى ثلاثين يوماً أو يغرم ثلاثين ديناراً",
 "وتدل هذه الرؤيا منهم على مرض طويل من غير أن يموتوا",
 "وإن سقطت إلى الأرض فهي مصيبة الموت",
 "والأسنان أهل بيت الإنسان فالعليا هم الرجال من جهة أبيه",
]
ENQ = [
 "Falling teeth in a dream\nmeans longevity, or living past one's contemporaries.",
 "cannot find his teeth in the dream, it means that his family will die before him,\nor that a member of his clan will emigrate to a new land.",
 "in a dream, it means the return of an immigrant to his homeland.",
 "Teeth in a dream represent one's identity, age, clan, a boy, a girl, his\nfamily, money, servants, domestic animals, employees, weapons, life, death,\nunity, separation, trusts, or savings.",
 "The closer the teeth are to the incisor, the closer is the relative.",
 "If a tooth moves in its place in the dream, it means\nan illness. If it falls, or if it is lost, then it means death of the person to whom",
 "dream, it means that someone will come forth and be to him as good as that\nrelative.",
 "If one loses a\nmolar tooth in a dream, it means the death of an elderly person in his household.",
 "If extra incisors grow in one's mouth in a dream,\nit means that one's family will grow by either a new born brother or a new son.",
 "Falling teeth in a dream also\ndenote a long illness that may not necessarily culminate in death.",
 "and if they fall on the floor in the dream, they\nmeans death.",
 "teeth of the right side represent the boys, and those on the left side",
]
PMQ = [  # PubMed full text (Freud name present there)
 "The connection between TD and death was a common belief for many years, which Freud (1900) reacted to with irony",
 ", in the Jewish Talmud, TD were construed as a prophecy for the impending death of a family member",
 "39.0% of respondents reported that they had experienced teeth dreams (TD) at least once, 16.2% reported that their TD were recurrent, and 8.2% reported that their TD were regular (Yu, 2012)",
 "may perhaps serve as indicators of undiagnosed bruxism",
]
FMQ = [
 "r* = 0.21 (0.07, 0.33), *p* < 0.005",
 "r* = 0.06 (-0.07, 0.20), ns",
 "r* = 0.02 (-0.11, 0.16), ns",
 "r* = 0.14 (-0.01, 0.28",
 "tension sensations in the teeth, gums, or jaws upon awakening",
 "= 210 with full data (76.7% females, Mage = 23.4",
]

f = 0
def check(tag, needle, hay):
    global f
    hit = needle in hay
    print(("HIT " if hit else "MISS"), tag, needle[:68].replace("\n", "⏎"))
    if not hit: f += 1

for q in ARQ: check("[AR]", q, AR)
for q in ENQ: check("[EN]", q, EN)
for q in PMQ: check("[PM]", q, PM)
for q in FMQ: check("[FM]", q, FM)

# structure
for t in ["div", "blockquote", "p", "footer"]:
    o = len(re.findall(rf"<{t}[ >]", PAGE)); c = len(re.findall(rf"</{t}>", PAGE))
    print(f"tag {t}: open={o} close={c}", "OK" if o == c else "MISMATCH")
    if o != c: f += 1
# no CJK
cjk = re.findall(r"[\u4e00-\u9fff]", PAGE)
print("CJK chars:", len(cjk), "OK" if not cjk else "FAIL")
if cjk: f += 1
print("fail:", f)
sys.exit(1 if f else 0)
