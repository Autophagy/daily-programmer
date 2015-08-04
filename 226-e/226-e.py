#Greatest common divisor between 2 numbers
def GCD(a,b):
	if (b == 0):
		return a
	else:
		return GCD(b, a % b)

#Lowest common multiple between 2 numbers
def LCM(a,b):
	return ((a*b) / GCD(a,b));

#Find the LCM of more than 2 numbers via recursion
#Eg. LCM(x,y,z) = LCM(x,LCM(y,z)))
def multiLCM(numbers):
	while (len(numbers) > 1):
		x = numbers.pop()
		i = len(numbers)
		numbers[i - 1] = LCM(numbers[i - 1], x)

	return numbers[0]

def fractionAdd(numbers):
    denominators = [int(d[1]) for d in numbers]
    LCD = multiLCM(denominators)
    sumOfFractions = sum([(int(a[0])*(LCD/int(a[1]))) for a in numbers])
    x = GCD(sumOfFractions, LCD)
    print str(sumOfFractions/x) + '/' + str(LCD/x)


def parseFile(filename):
    with open(filename) as file:
        lines = file.read().splitlines()

    #Remove the first line - unneeded
    del lines[0]
    fractionAdd([ l.split('/') for l in lines ])


parseFile('input1.txt')
parseFile('input2.txt')
