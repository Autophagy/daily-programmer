def balanceWord(word):
    for index in range(1, len(word)-2):
        left, right = list(word[:index]), list(word[index+1:])
        leftVal, rightVal = 0, 0
        for a, aLetter in enumerate(left):
            leftVal += (len(left) - a) * (ord(aLetter) - 64)
        for b, bLetter in enumerate(right):
            rightVal += (b + 1) * (ord(bLetter) - 64)
        if (leftVal == rightVal):
            print ''.join((''.join(left), word[index], ''.join(right), ' - ', str(leftVal)))
            return
    print(word + ' DOES NOT BALANCE')

balanceWord("CONSUBSTANTIATION")
balanceWord("WRONGHEADED")
balanceWord("UNINTELLIGIBILITY")
balanceWord("SUPERGLUE")
