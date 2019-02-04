alive = True

def emptyBoard(w,h):
    return list(map(lambda x: [False] * h, [False] * w))

def decorateBoardWalls(b):
    w = len(b)
    h = len(b[0])
    for i in range(w):
        b[i][0] = True
        b[i][h-1] = True
    for i in range(h):
        b[0][i] = True
        b[w-1][i] = True
    return b

def printBoard(b):
    str = '┌'
    for x in range(len(b)):
        str += '─'
    str += '┐'
    print(str)
    # print top border

    for y in range(len(b[0])):
        str = '│'
        for x in range(len(b)):
            str += '#' if b[x][y] else ' '
        str += '│'
        print(str)
    # print side border and content

    str = '└'
    for x in range(len(b)):
        str += '─'
    str += '┘'
    print(str)
    # print top border
        

while alive:
    b = emptyBoard(5,5)
    c = decorateBoardWalls(b)
    printBoard(b)
    printBoard(c)
    alive = False