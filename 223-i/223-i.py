def canBeOffensive(word, insult):
    for c in word:
        if c == insult[0]:
            insult = insult[1:]
        if len(insult) == 0:
            return True
    return False

print(canBeOffensive("synchronized", "snond"))
print(canBeOffensive("misfunctioned", "snond"))
print(canBeOffensive("mispronounced", "snond"))
print(canBeOffensive("shotgunned", "snond"))
print(canBeOffensive("snond", "snond"))
