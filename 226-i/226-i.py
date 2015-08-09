columnRange = [chr(c) for c in range(ord('a'), ord('g')+1)]
board = {x: ['.']*6 for x in columnRange }

def checkHorizontal(player, row):
    rowItems = ""
    for c in columnRange:
        rowItems += board.get(c)[row]
        if player*4 in rowItems:
            i = rowItems.index(player*4)
            return ' '.join([columnRange[a].upper() + str(row+1) for a in range(i,i+4)])
    return ''

def checkVertical(player, column):
    col = ''.join(board.get(column))
    if player*4 in col:
        i = col.index(player*4)
        return ' '.join([column.upper() + str(a+1) for a in range(i,i+4)])
    return ''

def checkDiagonal(player, column, row):
    return ''

def playMove(player,column):
    col = board.get(column)
    row = col.index('.')

    col[row] = player
    return checkWinState(player, column, row)

def checkWinState(player, column, row):
    h = checkHorizontal(player, row)
    if h is not '': return h

    v = checkVertical(player, column)
    if v is not '': return v

    return checkDiagonal(player,column,row)

def playMoves(filename):
    with open(filename) as file:
        lines = file.read().splitlines()

    xMoveList = []
    oMoveList = []

    for line in lines:
        a, b = line.split('  ')
        xMoveList.append(a.lower())
        oMoveList.append(b)

    #Play moves
    for i in range(0,len(lines)-1):
        a = playMove('X',xMoveList[i])

        if (a is not ''):
            return 'X won at move ' + str(i+1) + ' (with ' + a + ')'

        a = playMove('O',oMoveList[i])

        if (a is not ''):
            return 'O won at move ' + str(i+1) + ' (with ' + a + ')'

    return 'No winner from list of moves: ' + filename

x = playMoves('example.txt')
print(x)
