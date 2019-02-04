from functools import partial
from random import randint

class Tile:
    wall = '█'
    empty = ' '
    robot = 'r'
    player = 'P'

def emptyBoard(w,h):
    return [[Tile.empty] * h for col in range(w)]

def cloneBoard(b):
    return [[b[x][y] for y in range(len(b[x]))] for x in range(len(b))]

def insertWallBorder(b):
    (w,h) = getDims(b, True)
    for i in range(w + 1):
        b[i][0] = Tile.wall
        b[i][h] = Tile.wall
    for i in range(h + 1):
        b[0][i] = Tile.wall
        b[w][i] = Tile.wall
    return b

def insertWallTile(b, n = 1, r = [], p = None):
    opts = getRandomEmptyTiles(b, n, r, p)
    for (x,y) in opts:
        b[x][y] = Tile.wall
    return b

def insertRobots(b, r):
    for (x,y) in r:
        b[x][y] = Tile.robot
    return b

# map generator ---------------------------------

def getDims(b,tail = False):
    a = 1 if tail else 0
    return (len(b) - a,len(b[0]) - a)

def getRandomEmptyTiles(b, n = 1, r = [], p = None):
    tiles = []
    opts = getAllEmptyTiles(b,r,p)
    while n > 0 and len(opts) > 0:
        e = randint(0, len(opts)-1)
        tiles.append(opts[e])
        opts.pop(e)
        n -= 1
    return tiles

def getAllEmptyTiles(b, r = [], p = None):
    opts = []
    (w,h) = getDims(b, True)
    for x in range(w):
        for y in range(h):
            if (b[x][y] == Tile.empty and
            not (x,y) in r and
            (p is None or (x,y) != p)):
                opts.append((x,y))
    return opts

"""
@param  b   must have an empty tile otherwise infinite loop
"""
def getAnEmptyTile(b, r = []):
    while True:
        x = randint(0,len(b) - 1)
        y = randint(0,len(b[0]) - 1)
        if(b[x][y] == Tile.empty and not (x,y) in r):
            return (x,y)

def getRobots(b):
    (w,h) = getDims(b)
    bots = []
    for x in range(w):
        for y in range(h):
            if b[x][y] == Tile.robot:
                bots.append((x,y))
    return bots

# map utils -------------------------------------

def moveRobots(b,r,p):
    (px, py) = p
    nr = []
    for (x,y) in r:
        moveX = 1 if px > x else (-1 if px < x else 0)
        moveY = 1 if py > y else (-1 if py < y else 0)
        if(b[x + moveX][y] == Tile.wall):
            moveX = 0
        if(b[x][y + moveY] == Tile.wall):
            moveY = 0
        nr.append((x + moveX, y + moveY))
    return nr

# robot utils -----------------------------------

def printBoard(bori, r = [], p = None):
    class C:
        cb = [['┌','┐'],['└','┘']]
        hb = '─'
        vb = '│'

    b = insertRobots(cloneBoard(bori), r)
    if not p is None:
        b[p[0]][p[1]] = Tile.player
    (w,h) = getDims(b)
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

# rendering -------------------------------------

alive = True
b = insertWallTile(insertWallBorder(emptyBoard(20,10)),20)
p = getAnEmptyTile(b)
r = getRandomEmptyTiles(b, 4, [], p)
while alive:
    printBoard(b, r, p)
    r = moveRobots(b,r,p)
    printBoard(b,r,p)
    alive = False

# robot collision
# player motion
# player robot collision
# win state