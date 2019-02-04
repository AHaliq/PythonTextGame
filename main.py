from functools import partial
from random import randint

class Tile:
    wall = '█'
    empty = ' '

def emptyBoard(w,h):
    return [[Tile.empty] * h for col in range(w)]

def cloneBoard(b):
    return [[b[x][y] for y in range(len(b[x]))] for x in range(len(b))]

def insertWallBorder(b):
    w = len(b) - 1
    h = len(b[0]) - 1
    for i in range(w + 1):
        b[i][0] = Tile.wall
        b[i][h] = Tile.wall
    for i in range(h + 1):
        b[0][i] = Tile.wall
        b[w][i] = Tile.wall
    return b

"""
@param b    a board that MUST have at least one empty tile
"""
def insertWallTile(b, n=1):
    opts = []
    w = len(b) - 1
    h = len(b[0]) - 1
    for x in range(w):
        for y in range(h):
            if b[x][y] == Tile.empty:
                opts.append((x,y))
    while n > 0 and len(opts) > 0:
        e = randint(0, len(opts)-1)
        (x,y) = opts[e]
        b[x][y] = Tile.wall
        opts.pop(e)
        n -= 1
        
    return b


def printBoard(bori):
    class C:
        cb = [['┌','┐'],['└','┘']]
        hb = '─'
        vb = '│'

    b = cloneBoard(bori)
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
    c = insertWallTile(insertWallBorder(cloneBoard(b)),2)
    printBoard(b)
    printBoard(c)
    alive = False