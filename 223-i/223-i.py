def canBeOffensive(word, insult):
    wordResult = list(word)
    for c in word:
        if c not in insult:
            wordResult.remove(c)
    return insult == ''.join(wordResult)

def problemCount(file, insult):
    count = 0
    with open(file) as file:
        for line in file:
            count+= int(canBeOffensive(line.strip(), insult))
    print('Problem count for ' + insult + ' is ' + str(count))

print(canBeOffensive("synchronized", "snond"))
print(canBeOffensive("misfunctioned", "snond"))
print(canBeOffensive("mispronounced", "snond"))
print(canBeOffensive("shotgunned", "snond"))
print(canBeOffensive("snond", "snond"))

problemCount('enable1.txt', 'snond')
problemCount('enable1.txt', 'rrizi')
