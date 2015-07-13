def garlandDegree(word):
    for i in range(1,len(word)):
        if word[i:] == word[:len(word)-i]:
            return len(word[i:])
    return 0

def garland(word):
    degree = garlandDegree(word)
    print (word + " // " + str(degree) + " // " + word+word[degree:]*4)

garland("programmer")
garland("ceramic")
garland("onion")
garland("alfalfa")
