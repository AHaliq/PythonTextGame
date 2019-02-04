from functools import reduce, partial

alive = True

class C:
    
    cb = [['┌','┐'],['└','┘']]
    hb = '─'
    vb = '│'
    wall = '█'
    empty = ' '

def emptyBoard(w,h):
    return [[False] * h for col in range(w)]

def cloneBoard(b):
    return [[b[x][y] for y in range(len(b[x]))] for x in range(len(b))]

def decorateBoardWalls(b):
    w = len(b) - 1
    h = len(b[0]) - 1
    for i in range(w + 1):
        b[i][0] = True
        b[i][h] = True
    for i in range(h + 1):
        b[0][i] = True
        b[w][i] = True
    return b

def printHoriBorder(w, top = True):
    i = 0 if top else 1
    str = reduce(lambda a, c: a + C.hb, range(w), C.cb[i][0])
    str += C.cb[i][1]
    return str

def printBoard(b):
    ph = partial(printHoriBorder, len(b))
    print(ph())
    for y in range(len(b[0])):
        str = C.vb
        for x in range(len(b)):
            str += C.wall if b[x][y] else C.empty
        str += C.vb
        print(str)
    print(ph(False))
        

while alive:
    b = emptyBoard(5,5)
    c = decorateBoardWalls(cloneBoard(b))
    printBoard(b)
    printBoard(c)
    alive = False