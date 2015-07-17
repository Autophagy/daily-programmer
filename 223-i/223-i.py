def canBeOffensive(word, insult):
    wordResult = list(word)
    for c in word:
        if c not in insult:
            wordResult.remove(c)
    return insult == ''.join(wordResult)

print(canBeOffensive("synchronized", "snond"))
print(canBeOffensive("misfunctioned", "snond"))
print(canBeOffensive("mispronounced", "snond"))
print(canBeOffensive("shotgunned", "snond"))
print(canBeOffensive("snond", "snond"))
