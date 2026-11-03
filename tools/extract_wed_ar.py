#!/usr/bin/env python3
"""Extract verbatim Arabic passages from shamela page 145 (زواج entry) + p347 death=marriage clause
+ kaaba headword, and print them ready to paste into the page. Anchors chosen to be unique."""
import re, unicodedata

t145 = open('/root/dream_research/nabulsi_page_145.txt', encoding='utf-8').read()
t347 = open('/root/dream_research/nabulsi_p347_349.txt', encoding='utf-8').read()
t289 = open('/root/dream_research/nabulsi_page_289.txt', encoding='utf-8').read()

def span(text, start_anchor, end_anchor, name):
    i = text.find(start_anchor)
    if i < 0:
        print(f"!! {name}: START NOT FOUND: {start_anchor}"); return None
    j = text.find(end_anchor, i)
    if j < 0:
        print(f"!! {name}: END NOT FOUND: {end_anchor}"); return None
    s = text[i:j+len(end_anchor)]
    print(f"### {name} [{len(s)}ch]")
    print(s)
    print()
    return s

# The whole زواج headword paragraph = from (زواج) to "فإنه ينال زيادة."
span(t145, "(زواج) في المنام", "فإنه ينال زيادة.", "headword_full")
# jewish/christian/majusi/prostitute/sorceress/dog clauses
span(t145, "- (ومن رأى) أنه تزوج بامرأة يهودية", "فإنه يملك أمراً دنيئاً.", "trades_clauses")
# daughtress-of-ruler clause
span(t145, "- (ومن رأى) أنه تزوج بنت سلطان", "أو ما يفعل فعله.", "sultan_daughter")
# transfer-marriage money clause
span(t145, "- (ومن رأى) إنساناً تزوج بامرأة ونقلها", "مالاً وخيراً.", "transferred")
# the big multi-clause paragraph starting with زوجته تزوجت برجل حمامي
span(t145, "- (ومن رأى) زوجته تزوجت برجل حمامي", "فإنها تموت.", "big_para_a")
# marriage with deceased woman = revive abandoned affair
span(t145, "- (ومن رأى) أنه تزوج بامرأة ودخل بها", "دون ما لو دخل بها.", "entered")
# second wife clause
span(t145, "- (ومن رأى) أنه تزوج امرأة وله زوجة", "على يديه.", "second_wife")
# unknown sheikh clauses
span(t145, "- (ومن رأى) أنه تزوج ابنة شيخ مجهول", "أفاقت من مرضها.", "sheikh")
# mahram clauses
span(t145, "- (ومن رأى) أنه تزوج امرأة ميتة من ذوات محارمه", "فانسب للزوجة مثله لدلالته عليها.", "mahram_wife")
# death = marriage in Nabulsi (p347)
span(t347, "وقيل الموت على الإطلاق زواج", "كالمتزوج", "nabulsi_death_marriage")
# kaaba = marriage cross-ref (p289)
span(t289, "(كعبة) هي في المنام", "ومن رآها", "kaaba_headword")
