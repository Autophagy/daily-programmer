def getIntersectionPairs(data, y):
    intersections = []
    for x,c in enumerate(data[y]):
        if(c == "+"):
            intersections.append((x,y))

    connectedPairs = []
    for index, intersection in enumerate(intersections):
        #See if it is paired with the other intersections
        for i in intersections:
            if intersection[0] < i[0]:
                if pairHorizontallyConnects(data, intersection, i):
                    connectedPairs.append((intersection, i))

    return connectedPairs

def pairHorizontallyConnects(data, a,b):
    for i in range(a[0]+1, b[0]):
        if data[a[1]][i] not in ["+","-"]:
            return False
    return True

def isInvalidVerticalMove(data, x,y):
    if(y+1 >= len(data) or len(data[y+1]) <= x):
        return True
    elif(data[y+1][x] not in ["+","|"]):
        return True
    return False

def findQuads(data, a,b):
    isValid = True
    quads = 0
    while(isValid):
            if isInvalidVerticalMove(data, a[0],a[1]) or isInvalidVerticalMove(data, b[0],b[1]):
                isValid = False
            else:
                a, b = (a[0],a[1]+1), (b[0],b[1]+1)
                if data[a[1]][a[0]] == "+" and data[b[1]][b[0]] == "+":
                    if pairHorizontallyConnects(data, a,b):
                        quads += 1
    return quads

def analyse(fileName):
    data = open(fileName).readlines()
    for line in data:
        line = line.rstrip()

    quadCount = 0

    for y, line in enumerate(data):
        pairs = getIntersectionPairs(data, y)
        for pair in pairs:
            quadCount += findQuads(data, pair[0],pair[1])

    print('Number of quads in file ' + fileName +': ' + str(quadCount))

analyse('example.txt')
analyse('challenge.txt')
