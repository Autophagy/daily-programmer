#This is a very messy and gross solution, which i'll optimise ++ make neater
#... promise. I'm actually a little ashamed of this

#directions correspond to moving rightward, moving downward, moving leftward,
#moving upward respectively
directions = [(1,0),(0,1),(-1,0),(0,-1)]
direction = directions[0]
x, y = 0, 0
maxX = 0

outputString = []

#The next move is valid if it is not out of x/y bounds, and there is a letter
def isValidMove(newX, newY):
    return (0 <= newX < maxX) and (0 <= newY < len(inputFile[newX])) and (inputFile[newX][newY] != " ")

def getRightAngleTurns(direction):
    turns = [[0,0],[0,0]]

    for index, coordinate in enumerate(direction):
        if (coordinate != 0):
            turns[0][index] = 0
            turns[1][index] = 0
        else:
            turns[0][index] = -1
            turns[1][index] = 1
    return turns

with open("input1.txt") as f:
    inputFile = f.readlines()

#Remove the first line (number of lines) and strip the newlines
inputFile = [line.rstrip('\n') for line in inputFile]
maxX = int(inputFile.pop(0))

if (isValidMove(0,1)):
    direction = directions[1]

while True:
    outputString.append(inputFile[x][y])
    turns = getRightAngleTurns(direction)

    #if the next position following the current direction is valid, move to it
    if (isValidMove(x + direction[0], y + direction[1])):
        x += direction[0]
        y += direction[1]
    #if one of the right angles is valid, move to it
    elif(isValidMove(x + turns[0][0], y + turns[0][1])):
        #If the angle turn is valid, append a space + the current character again
        outputString.append(' ')
        direction = turns[0]
    #if the other right angle turn is valid, move to it
    elif(isValidMove(x + turns [1][0], y + turns[1][1])):
        outputString.append(' ')
        direction = turns[1]
    #if none of this is true, we've reached the end
    else:
        break

print ''.join(outputString)
