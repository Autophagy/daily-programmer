columnRange = [chr(c) for c in range(ord('a'), ord('g')+1)]
board = {x: ['.']*6 for x in columnRange }

def checkHorizontal(player, row):
    rowItems = ""
    for c in columnRange:
        rowItems += board.get(c)[row]
        if player*4 in rowItems:
            i = rowItems.index(player*4)
            return [columnRange[a] + str(row) for a in range(i,i+4)]
    return False

def checkVertical(player, column):
    return player*4 in  ''.join(board.get(column))

def checkDiagonal(player, column, row):
