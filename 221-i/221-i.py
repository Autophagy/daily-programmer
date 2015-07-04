#directions correspond to moving rightward, moving downward, moving leftward,
#movinig upward respectively
directions = [(1,0),(0,1),(-1,0),(0,-1)]
direction = directions[0]
x, y = 0, 0
maxY = 0

outputString = []

with open("input1.txt") as f:
    inputFile = f.readlines()

#Remove the first line (number of lines) and strip the newlines
inputFile = [line.rstrip('\n') for line in inputFile]
maxY = int(inputFile.pop(0))

finished = False

while(!finished):
    #take the character of our current position, add it to outputString
    #check that the next position in our current direction is valid (it is not
    #past max x or max y, and there is a character)
    #if true, move
    #if false, check 90 degrees. if no valid path, then finished
    #if a valid, however, move there, repeat
    outputString.append(inputFile[x][y])

    nextX = x + direction[0]
    nextY = y + direction[y]

    #if the next position is valid, move to it
    if (0 <= nextX < len(inputFile[x])) && (0 <= nextY < maxY) && (inputFile[nextX][nextY] != ""):
        x = nextX
        y = nextY
