#!/usr/bin/env python3
"""probe_rain.py — check every quote endpoint exists verbatim in corpus before build."""
import re
def norm(s): return re.sub(r'\s+', ' ', s).strip()

en = norm(open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read())
en = norm(re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en))
en = norm(re.sub(r"\d+ IBN SEERIN'?S", ' ', en))

EN = [
 ("RAIN-S", "Rain: (Clouds; Drizzling; Life; Vapor; Water) If no harm"),
 ("RAIN-E", "it means a sickness. (Also see Water)"),
 ("RB-S", "Rainbow: (Fantasy; Illusion; Pipe dream)"),
 ("RB-E", "then it means war."),
 ("WL-S", "Water level: (Artificial lake; Farm pond; Ombrometer; Ombrograh; Pluviometer;"),
 ("WL-E", "same interpretation. (Also see Water)"),
 ("CL-S", "Clouds: (Concealment; Gloom;"),
 ("CL-E", "harsh mandates."),
 ("CL2-S", "If people are expecting clouds to water their farms"),
 ("CL2-E", "the majority of whom will perish during a trip."),
 ("DEATH-RAIN", "The death of an unknown woman in a dream means absence of rain or dearth, and if she comes back to life in the dream, it means rain."),
 ("CARAVAN", "Rain in a dream also represents a caravan of camels, and a caravan of camels in a dream represents rain."),
]
for tag, s in EN:
    print("EN", tag, "OK" if s in en else "MISS")

ARS = {}
for pg in (315, 316, 317, 318):
    ARS[pg] = norm(open(f'/root/dream_research/nabulsi_page_{pg}.txt', encoding='utf-8').read())

AR = [
 (315, "A315-S", "- (مطر) هو في المنام إذا لم يحصل منه ضرر"),
 (315, "A315-E", "حياة من يخشى عليه من"),
 (316, "A316-S", "آدمي أو أرض وربما دل المطر على إنجاز ما يوعد به"),
 (316, "A316-E", "وتتفجر العيون."),
 (316, "AG-S", "- (ومن رأى) مطراً عاماً يحيا له أمر ميت"),
 (316, "AG-E", "فرج عنه."),
 (316, "AH-S", "- (ومن رأى) المطر قد عاجله"),
 (316, "AH-E", "في تلك السنة."),
 (316, "AD-S", "- (ومن رأى) المطر في داره خاصة"),
 (316, "AD-E", "تلك القرية."),
 (316, "AF-S", "- (ومن رأى) مطراً يسيح من كل جانب"),
 (316, "AF-E", "في حين ضرره."),
 (316, "AS-S", "- (ومن رأى) نفسه في المطر تحت سقف"),
 (316, "AS-E", "قضيت له."),
 (316, "AW-S", "- (ومن رأى) السماء قد أمطرت سيوفاً"),
 (316, "AW-E", "فإنهم يمرضون."),
 (316, "ADK-S", "- (ومن رأى) أنه يشرب من ماء المطر"),
 (316, "ADK-E", "شرب من الماء."),
 (317, "MZ-S", "- (ميزاب) هو في المنام رجل صاحب معروف في بعض الأحيان."),
 (317, "MZ-E", "ميازيب تجري في غير مطر فإنها"),
 (318, "MZC-S", "تدل على فتن وكل ميزاب منها يدل على ضرب رقبة"),
 (318, "MZC-E", "بما ينزل منه الماء."),
 (318, "MZU-S", "- (ومن رأى) أنه تحت ميزاب الرحمة"),
 (318, "MZU-E", "كان بعكس ذلك."),
 (316, "ZAMZAM", "ميزاب الرحمة في جامع"),
]
for pg, tag, s in AR:
    print("AR", pg, tag, "OK" if s in ARS[pg] else "MISS")

zg = open('/root/dream_research/zhougong_yuanban.txt', encoding='utf-8').read()
ZG = ["天晴雨散百忧去", "阴雨晦时主囚事", "行路逢雨有酒食", "狂风大雨人死亡"]
for L in ZG:
    print("ZG", L, "OK" if L in zg else "MISS")
print("ZG total 雨 count:", zg.count("雨"))

f = norm(open('/root/dream_research/frontiers_full.txt', encoding='utf-8').read())
import re as _re
hits = _re.findall(r'[A-Za-z]*[Rr]ain[A-Za-z]*', f)
print("FRONTIER rain-like tokens:", sorted(set(hits)))
print("FRONTIER has 'toilet':", 'toilet' in f.lower())
