#!/usr/bin/env python3
"""Probe corpus anchors for the baby page (Ibn Sirin EN side)."""
import re
def norm(s): return re.sub(r'\s+', ' ', s).strip()

en = norm(open('/root/dream_research/ibn_sirin_full.txt').read())
en2 = re.sub(r'DICTIONARY OF DREAMS \d+', ' ', en)
en2 = re.sub(r"\d+ IBN SEERIN'?S", ' ', en2)
en2 = norm(en2)

def seg(start, end, src=en2):
    i = src.find(start); assert i != -1, "MISS START " + start[:50]
    j = src.find(end, i); assert j != -1, "MISS END " + end[:50]
    return src[i:j+len(end)]

CHILD = seg("Child: (Little boy) In a dream, a child carried", "the little girl then represents his glad tidings.")
print("CHILD len", len(CHILD))
BIRTH = seg("Childbirth: (Giving birth) Seeing one's wife giving birth", "giving birth in a dream means loss of his investment. (Also see Dragon)")
print("BIRTH len", len(BIRTH))
BOY = seg("Boy: (Young boy) Seeing a young boy", "something good or bad may take place in wakefulness.")
print("BOY len", len(BOY))
SON = seg("Son: In a dream, a son may mean", "a daughter or a servant.")
print("SON:", repr(SON))
CHICKS = seg("Chicks: (Baby; Chicken; Fowl) A chick in a dream", "represents the voice of insolent people.")
print("CHICKS:", repr(CHICKS))

for a in [
  "If a sick person sees himself as a child in a dream, it means his death.",
  "he will become free from his sins, like the day his mother gave birth to him.",
  "it means that he plays a string instrument.",
  "Bereavement of a child in a dream means the opposite in real life.",
  "A child in a dream represents a weak enemy who sometime shows friendliness",
  "If they are one's own children in the dream, then they mean temptation with money.",
  "Giving birth to a girl means relief from distress, while giving birth to a boy in the dream means distress and worries.",
  "If a pregnant woman sees herself giving birth to a girl in a dream, it means a boy, and if she gives birth to a boy in the dream, it means a girl.",
  "it means that he will receive an inheritance from his mother.",
  "she will beget a son who will look like his father.",
  "Carrying a child in a dream means managing an inheritance or a financial investment.",
  "If a woman gives birth to a child from her mouth in a dream, it means her death.",
  "Carrying a young boy in a dream means carrying burdens.",
  "himself as a newborn child in a dream, it means that he will become wealthy",
  "a little child who disdains from coming near his father",
  "it means financial promotion and enjoyment of one's life.",
  "A little male child in a dream represents worries, responsibilities, hard work",
  "If a prisoner sees himself carrying a little girl in his dream, it means that he will be released from his prison.",
  "Children in a dream also could mean either sorrow and pain or happiness and joy.",
  "Seeing a mature child in a dream means power and superiority.",
  "it means that he will repent of a common sin he is used to commit.",
  "it means relief from distress and good health",
  "Begetting a boy in a dream means worries, burdens or sickness",
  "Seeing a young boy in a dream means receiving glad tidings.",
  "If one sees one of the renowned people of knowledge sitting in a kindergarten",
  "A chick in a dream represents a stolen or a missing child.",
]:
    print(("OK   " if a in en2 else "MISS "), a[:70])
