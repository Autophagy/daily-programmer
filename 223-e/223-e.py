def garlandDegree(word):
    for i in range(1,len(word)):
        if word[i:] == word[:len(word)-i]:
            return len(word[i:])
    return 0

def garland(word):
    degree = garlandDegree(word)
    print (word + " // " + str(degree) + " // " + word+word[degree:]*4)

def garlandFile(file, description):
    result = ""
    garland = 0
    with open(file) as file:
        for line in file:
            a = line.strip().lower()
            g = garlandDegree(a)
            if(g >garland):
                result, garland = a, g
    if(garland>0):
        print ("Largest garland word in '" + description + "' is " + result)
    else:
        print ("No garland words found in '" + description + "'")

garland("programmer")
garland("ceramic")
garland("onion")
garland("alfalfa")

#Both dictionaries sourced from Leipzig Uni's Wortschatz
#http://wortschatz.uni-leipzig.de/
garlandFile('english.txt', 'Top 10,000 English Words')
garlandFile('german.txt', 'Top 10,000 German Words')
