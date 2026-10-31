#!/usr/bin/env python3
# Second batch of verbatim checks for gap #7 page: relative map + cross-refs.
import sys
SRC_AR = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
SRC_EN = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()

AR = [
    # upper = men from father's side, lower = women from mother's side
    "والأسنان أهل بيت الإنسان فالعليا هم الرجال من جهة أبيه والسفلى هن النساء من جهة أمه",
    # nearest to the central incisors = nearest in kinship
    "فأدناها من الثنايا أقربهم في النسب",
    # two upper centrals = father and paternal uncle (right=father, left=uncle)
    "والثنيتان العليا هم الأب والعم فاليمنى الأب واليسرى العم",
    # lower centrals = mother and maternal aunt
    "والثنيتان السلفيان الأم والعمة",
    # canine = master/lord of the household
    "والناب سيد أهل بيته الذي يستند إليه ولا يكون فوقه أحد",
    # premolars = maternal uncles
    "الضواحك الأخوال",  # upper premolars = maternal uncles (no واو in scan)
    # molars = grandparents and small children
    "والأضراس أجداد وبنون صغار",
    # four incisors sentence (used in earlier pages too? here just ثنية=أب/عم covered)
]
EN = [
    # Tooth entry: teeth represent ... life, death, unity, separation...
    "his\nfamily, money, servants, domestic animals, employees, weapons, life, death,\nunity, separation, trusts, or savings.",
    # upper=father-side males, lower=mother-side females
    "male's or female's upper teeth\nrepresent the male members of one's family from the father's side, and the teeth\nof the lower jaw represent the female members of one's family from the mother's\nside.",
    # closer to incisor = closer relative
    "The closer the teeth are to the incisor, the closer is the relative.",
    # upper right incisor = father; upper left = paternal uncle
    "the upper right incisor represents the father, and the upper left",
    # lower right incisor = mother
    "The lower right incisor represents the mother",
    # tooth moves = illness; falls or lost = death of attributed person OR separation
    "If a tooth moves in its place in the dream, it means\nan illness. If it falls, or if it is lost, then it means death of the person to whom\nit is attributed, or it could possibly mean that he will be separated from him and\ncan no longer see him.",
    # save-not-bury = replacement; bury = death
    "If one saves his lost tooth and does not bury it in the\ndream, it means that someone will come forth and be to him as good as that\nrelative. Otherwise, ifhe does bury it, then it means the death of his relative.",
    # molar lost = death of elderly person in household
    "If one loses a\nmolar tooth in a dream, it means the death of an elderly person in his household.",
    # extra incisors grow = family grows
    "If extra incisors grow in one's mouth in a dream,\nit means that one's family will grow by either a new born brother or a new son.",
    # limbs also represent family (parallel rule)
    "Human teeth in a dream also represent one's business and management of his\nlife.",
]
fail = 0
for a in AR:
    hit = a in SRC_AR
    print(("HIT " if hit else "MISS"), "[AR]", a[:80])
    if not hit: fail += 1
for a in EN:
    hit = a in SRC_EN
    print(("HIT " if hit else "MISS"), "[EN]", a[:80])
    if not hit: fail += 1
print("fail:", fail)
