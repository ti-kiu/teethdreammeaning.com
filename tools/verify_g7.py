#!/usr/bin/env python3
# Verify gap #7 (death-reading) L1 assertions verbatim against source files.
# Exit 0 only if all HIT.
import sys

SRC_AR = open('/root/dream_research/shamela_177.txt', encoding='utf-8').read()
SRC_EN = open('/root/dream_research/ibn_sirin_full.txt', encoding='utf-8').read()

AR = [
    # burial switch: held-not-buried = replacement relative
    "أمسكها ولم يدفنها فإنه يستفيد بدلها من يكون له مثل ذلك القريب",
    # buried = that relative dies
    "فإن دفنها فإنه موت ذلك القريب",
    # tooth moves -> illness -> falls/lost = death or absence of the relative
    "فإن تحرك منها سن واحدة من هؤلاء فمرض فإن سقطت أو ضاعت فإنه موت من ينسب إليه هؤلاء أو غيبته عنه غيبة لا يرونه بعد ذلك",
    # vanished tooth = relative absent by death or separation
    "وإذا غابت عنه فإنه يغيب ذلك القريب بموت أو فراق",
    # lost teeth -> goes abroad from one clansman; finds it -> returns; else no return
    "فإنه يغترب عن عشيرته واحد فإن أصابه بعدما فقده رجع وإلا فلا يرجع",
    # gone vision (about the eyes/sight line at top of page): family die before him
    "فإن أهل بيته يموتون قبله وربما كان ذلك موت ذوي سنه أو مرض أهل بيته",
    # one tooth without treatment, held in hand/tied in garment -> child; if pregnant woman -> a child, else reconciled kin
    "وسقوط السن الواحدة إن كان من غير معالجة وأخذها بيده أو صرها في ثوبه فإن كان عنده حامل جاءه ولد وإلا صالح أخاً أو قريباً كان قد قاطعه",
    # blood clause = sin of severing kinship, unless debt
    "وإن كان هناك دم فإن ذلك إثم القطيعة للرحم إلا أن يكون عليه دين فإنه يطالب به",
    # all teeth into hand -> progeny multiplies (the counter-reading)
    "وإن رأى جميع أسنانه سقطت وصارت في يده أو عنده فإنه يكثر نسل أهل ذلك البيت وعددهم",
    # catching them in hand/beard/lap -> offspring cut off
    "فإن ذلك يدل على أن أولاده تنقطع ولا يولد له",
    # upper fell to ground = death calamity
    "وإن سقطت إلى الأرض فهي مصيبة الموت",
    # long illness without dying (household clause)
    "وتدل هذه الرؤيا منهم على مرض طويل من غير أن يموتوا",
    # teeth = term of appointed age/death
    "هي في المنام دالة على منتهى الأجل",
    # teeth also indicate... death and life...
    "والذخائر والموت والحياة",
    # worn/eroded tooth = that man struck by affliction, no benefit
    "فإن رأى بعض أسنانه تآكلت أو درست فإن الرجل الذي هو تأويلها يصيبه بلاء فلا ينتفع به",
]

EN = [
    # cannot find teeth = family die before him OR clan member emigrates
    "cannot find his teeth in the dream, it means that his family will die before him,\nor that a member of his clan will emigrate to a new land.",
    # found lost tooth = return of immigrant
    "Ifone finds a lost tooth\nin a dream, it means the return of an immigrant to his homeland.",
    # fallen teeth also denote long illness not necessarily death
    "Falling teeth in a dream also\ndenote a long illness that may not necessarily culminate in death.",
    # upper teeth to floor = "they means death" (original grammar flaw kept)
    "and if they fall on the floor in the dream, they\nmeans death.",
    # collecting lost teeth = longevity OR large progeny (counter-reading)
    "Collecting one's lost teeth\nin a dream means longevity, or it could mean having a large progeny.",
    # falling teeth = longevity, living past contemporaries (first line)
    "Falling teeth in a dream\nmeans longevity, or living past one's contemporaries.",
    # collecting fallen teeth also = can no longer conceive (self-contradiction pair)
    "Ifone collects\nhis fallen teeth in a dream, it also means that he can no longer conceive children.",
    # lost teeth + unable to eat = poverty
    "If\none loses his teeth and finds himself unable to eat properly in the dream, it also\nmeans poverty.",
    # religious person loses teeth -> devotion/fasting
    "If a religious person loses his teeth in a dream, it means that he should be more\nassiduous in his devotion",
    # teeth entry headword line w/ Migration
    "Teeth 1: (Acrimony; Dice; Grasping; Longevity; Migration) Falling teeth in a dream",
]

fail = 0
for a in AR:
    hit = a in SRC_AR
    print(("HIT " if hit else "MISS"), "[AR]", a[:80].replace("\n", " "))
    if not hit: fail += 1
for a in EN:
    hit = a in SRC_EN
    print(("HIT " if hit else "MISS"), "[EN]", a[:80].replace("\n", " "))
    if not hit: fail += 1
print(f"\n{len(AR)+len(EN)-fail}/{len(AR)+len(EN)} assertions verified verbatim")
sys.exit(1 if fail else 0)
