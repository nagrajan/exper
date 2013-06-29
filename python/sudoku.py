# sudoku solver
__author__ = 'nagarajan'

from copy import deepcopy
from time import time

def updateRow(possb, pos, val):
    rr = pos/9
    for ov in xrange(rr*9, (rr+1)*9):
        if val in possb[ov]:
            if len(possb[ov]) == 1:
                return False
            possb[ov].remove(val)

def updateCol(possb, pos, val):
    cc = pos%9
    for ov in xrange(cc, 81, 9):
        if val in possb[ov]:
            if len(possb[ov]) == 1:
                return False
            possb[ov].remove(val)

def updateCell(possb, pos, val):
    sc = (pos/27)*27 + ((pos%9)/3)*3
    for addv in (0, 1, 2, 9, 10, 11, 18, 19, 20):
        scv = sc + addv
        if val in possb[scv]:
            if len(possb[scv]) == 1:
                return False
            possb[scv].remove(val)

def updateAll(possb, pos, val):
    if updateRow(possb, pos, val) is False:
        return False
    if updateCol(possb, pos, val) is False:
        return False
    if updateCell(possb, pos, val) is False:
        return False

    return True


def initPossibilities(possb, ins):
    for rr in xrange(9):
        for cc in xrange(9):
            pos = rr*9 + cc
            val = ins[pos]
            if val != 0:
                # update row, col and cell
                possb[pos] = set()

                # update all
                if updateAll(possb, pos, val) is False:
                    print "Failed in initializing possibilities"
                    return False
    return possb

def solveSudoku(possb, ss):
    changed = True
    while changed:
        changed = False
        for pos in xrange(81):
            if len(possb[pos]) == 1:
                changed = True
                val = possb[pos].pop()
                ss[pos] = val
                if updateAll(possb, pos, val) is False:
                    return False

    guessPos = None
    for pos in xrange(81):
        if len(possb[pos]) > 1:
            guessPos = pos
            break

    if guessPos is None:
        return ss

    ss2 = deepcopy(ss)
    guessValues = possb[guessPos]
    for guess in guessValues:
        possb2 = deepcopy(possb)
        possb2[guessPos] = set()
        ss2[guessPos] = guess
        if updateAll(possb2, guessPos, guess) is False:
            return False
        retVal = solveSudoku(possb2, ss2)
        if retVal is not False:
            return retVal
    return False


def getCell(sdk, cell):
    cs = (cell/3)*27 + (cell%3)*3
    return [sdk[cs + x] for x in (0,1,2,9,10,11,18,19,20)]

def checkSolution(outs):
    # every row
    set9 = set(xrange(1,10))
    for rr in range(9):
        assert set9 == set([outs[rr*9 + x] for x in xrange(9)])

    for cc in xrange(9):
        assert set9 == set([outs[x*9 + cc] for x in xrange(9)])

    for cell in xrange(9):
        assert set9 == set(getCell(outs, cell))

    return "Solution checks out..."


def formatSudoku(outs):
    data = [str(x) for x in outs]
    data = [' '.join(data[x*3:(x+1)*3]) for x in range(27)]
    data = ['   '.join(data[x*3:(x+1)*3]) for x in range(9)]
    data = ['\n'.join(data[x*3:(x+1)*3]) for x in range(3)]
    data = '\n\n'.join(data)
    return '\n' + data + '\n'

if __name__ == '__main__':
    possibilities = [set(range(1,10)) for x in xrange(9) for y in xrange(9)]
    inSudoku = ([0,0,0,2,0,0,0,6,3] +
                [3,0,0,0,0,5,4,0,1] +
                [0,0,1,0,0,3,9,8,0] +
                [0,0,0,0,0,0,0,9,0] +
                [0,0,0,5,3,8,0,0,0] +
                [0,3,0,0,0,0,0,0,0] +
                [0,2,6,3,0,0,5,0,0] +
                [5,0,3,7,0,0,0,0,8] +
                [4,7,0,0,0,1,0,0,0] )

    inSudoku = ([8,0,0,0,0,0,0,0,0] +
                [0,0,3,6,0,0,0,0,0] +
                [0,7,0,0,9,0,2,0,0] +
                [0,5,0,0,0,7,0,0,0] +
                [0,0,0,0,4,5,7,0,0] +
                [0,0,0,1,0,0,0,3,0] +
                [0,0,1,0,0,0,0,6,8] +
                [0,0,8,5,0,0,0,1,0] +
                [0,9,0,0,0,0,4,0,0] )

    possb = initPossibilities(possibilities, inSudoku)
    if possb is False:
        print "Failed miserably"
        exit()

    st = time()
    result = solveSudoku(possb, inSudoku)
    et = time()

    if result is False:
        print "Failed to find solution"
    else:
        print formatSudoku(result)
        print checkSolution(result)
        print "Took %s seconds"%str(et-st)

