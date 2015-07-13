def garland(word):
    for i in range(1,len(word)):
        a = word[i:]
        b = word[:(len(word)-i)]
        if a == b:
            return len(a)
    return 0

print(garland("programmer"))
print(garland("ceramic"))
print(garland("onion"))
print(garland("alfalfa"))
