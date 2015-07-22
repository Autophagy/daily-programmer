#An implementation of the Fisher-Yates shuffle
from random import randint

def fisherYatesShuffle(a):
    for i in range(len(a)-1,0,-1):
        j = randint(0,i)
        a[j], a[i] = a[i], a[j]
    return a

a = [1,2,3,4,5,6,7,8]
b = ['apple', 'blackberry', 'cherry', 'dragonfruit', 'grapefruit', 'kumquat', 'mango', 'nectarine', 'persimmon', 'raspberry', 'raspberry']
c = ['a', 'e', 'i', 'o', 'u']

a = fisherYatesShuffle(a)
b = fisherYatesShuffle(b)
c = fisherYatesShuffle(c)

print(a)
print(b)
print(c)
