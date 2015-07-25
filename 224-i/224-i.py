def buildMap(data):
    dict = { }
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            dict[x,y] = c
            if ()
    return dict

def areHorizontalConnected(a,b,y):
    for i in range(a+1,b):
        if data[i,y] == " ":
            return false
    return true

def findHorizontalPairs():
    pairs = []
    for i in range(0,height):
        crosses

data = open('example.txt').readlines()
width = len(max(data, key=len))
height = len(data)
data = buildMap(data)
