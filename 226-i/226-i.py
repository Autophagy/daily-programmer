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
    rows = len(board.get(column))
    cols = len(columnRange)

    #Top left to bottom right diagonals
    b = [(columnRange.index(column),row)]
    rowIndex,colIndex = row, columnRange.index(column)
    a = getDiagonal(rowIndex, colIndex, rows, -1, 1, -1)
    c = getDiagonal(rowIndex, colIndex, -1, cols, -1, 1)
    a.reverse()

    rowItems = ''.join(expandList([(columnRange[x],y) for x,y in a+b+c]))
    if player*4 in rowItems:
        return ' '.join([columnRange[x].upper() + str(y+1) for x,y in a+b+c])

    #top right to bottom left
    a = getDiagonal(rowIndex, colIndex, rows, cols, 1, 1)
    c = getDiagonal(rowIndex, colIndex, -1, -1, -1, -1)
    a.reverse()

    rowItems = ''.join(expandList([(columnRange[x],y) for x,y in a+b+c]))
    if player*4 in rowItems:
        return ' '.join([columnRange[x].upper() + str(y+1) for x,y in a+b+c])

    return ''

def expandList(coordinates):
    return [board.get(a)[b] for a,b in coordinates]

def getDiagonal(rowIndex, colIndex, rowBoundary, colBoundary, rowInc, colInc):
    a = []
    rowIndex += rowInc
    colIndex += colInc

    while(rowIndex is not rowBoundary and colIndex is not colBoundary):
        a.append((colIndex,rowIndex))
        rowIndex += rowInc
        colIndex += colInc

    return a

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

    for move, line in enumerate(lines):
        x, o = line.split('  ')

        a = playMove('X',x.lower())

        if (a is not ''):
            return 'X won at move ' + str(move+1) + ' (with ' + a + ')'

        a = playMove('O',o)

        if (a is not ''):
            return 'O won at move ' + str(move+1) + ' (with ' + a + ')'

    return 'No winner from list of moves: ' + filename

x = playMoves('example.txt')
print(x)
