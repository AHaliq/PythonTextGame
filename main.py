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
    return getRandomEmptyTiles(b,1,r)[0]

def getRobots(b):
    (w,h) = getDims(b)
    bots = []
    for x in range(w):
        for y in range(h):
            if b[x][y] == Tile.robot:
                bots.append((x,y))
    return bots

def alignWallCollision(b, p, moveX, moveY):
    (x,y) = p
    destBlocked = b[x + moveX][y + moveY] == Tile.wall
    if(b[x + moveX][y] == Tile.wall or destBlocked):
        moveX = 0
    if(b[x][y + moveY] == Tile.wall or destBlocked):
        moveY = 0
    return (x + moveX, y + moveY)

# map utils -------------------------------------

def moveRobots(b,r,p):
    (px, py) = p
    nr = []
    for (x,y) in r:
        moveX = 1 if px > x else (-1 if px < x else 0)
        moveY = 1 if py > y else (-1 if py < y else 0)
        nr.append(alignWallCollision(b, (x,y), moveX, moveY))
    return nr

def checkRRCollision(r):
    d = {}
    nr = []
    for x in r:
        if x in d.keys():
            d[x] += 1
        else:
            d[x] = 1
    for x in d.keys():
        if d[x] == 1:
            nr.append(x)
    return nr

# robot utils -----------------------------------

def getUserMove(b,p):
    (x,y) = p
    (w,h) = getDims(b,True)
    moveX = 0
    moveY = 0
    while True:
        m = input('make your move : ')
        if m in ['q','w','e','a','s','d','z','x','c']:
            if m in ['q','a','z']:
                moveX = -1
            elif m in ['e','d','c']:
                moveX = 1
            else:
                moveX = 0
            if m in ['q','w','e']:
                moveY = -1
            elif m in ['z','x','c']:
                moveY = 1
            else:
                moveY = 0
            # get moveXY
            if ((moveX == -1 and x == 0) or
            (moveX == 1 and x == w) or
            (moveY == -1 and y == 0) or
            (moveY == 1 and y == h)):
                print('move out of bounds, pick another')
                # detect out of bounds
            else:
                p = alignWallCollision(b, p, moveX, moveY)
                # valid move
                break
        else:
            print('invalid move, choose: q,w,e,a,s,d,z,x,c')
    return p

# player ----------------------------------------

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

b = insertWallTile(insertWallBorder(emptyBoard(20,10)),20)
p = getAnEmptyTile(b)
r = getRandomEmptyTiles(b, 4, [], p)
printBoard(b, r, p)
while True:
    p = getUserMove(b,p)
    r = moveRobots(b,r,p)
    # check player robot collision
    r = checkRRCollision(r)
    printBoard(b,r,p)
    if len(r) == 0:
        print("you win")
        break

# TODO fix wall collision
# player robot collision
# win/loose state