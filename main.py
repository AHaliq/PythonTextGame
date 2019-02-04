from functools import partial

def emptyBoard(w,h):
    return [[False] * h for col in range(w)]

def cloneBoard(b):
    return [[b[x][y] for y in range(len(b[x]))] for x in range(len(b))]

def decorateBorder(b):
    w = len(b) - 1
    h = len(b[0]) - 1
    for i in range(w + 1):
        b[i][0] = True
        b[i][h] = True
    for i in range(h + 1):
        b[0][i] = True
        b[w][i] = True
    return b

def printBoard(bori):
    class C:
        cb = [['┌','┐'],['└','┘']]
        hb = '─'
        vb = '│'
        wall = '█'
        empty = ' '
    # characters

    b = [[C.wall if bori[x][y] else C.empty
        for y in range(len(bori[x]))]
        for x in range(len(bori))]
    w = len(b)
    # local variables

    def ph(top = True):
        i = 0 if top else 1
        return f"{C.cb[i][0]}{C.hb * w}{C.cb[i][1]}"
    # top bottom border subroutine

    print(ph())
    # top border
    for y in range(len(b[0])):
        print(f"{C.vb}{''.join([b[x][y] for x in range(len(b))])}{C.vb}")
    # mid content
    print(ph(False))
    # bottom border
        
alive = True
while alive:
    b = emptyBoard(5,5)
    c = decorateBorder(cloneBoard(b))
    printBoard(b)
    printBoard(c)
    alive = False