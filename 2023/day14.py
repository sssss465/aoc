import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict,deque
from functools import cache
import math
import bisect

lines = [l.strip() for l in fileinput.input()]
grid = [[lines[i][j] for j in range(len(lines[0]))] for i in range(len(lines))]
oldgrid = [[lines[i][j] for j in range(len(lines[0]))] for i in range(len(lines))]
def tilt(grid, dir='N'):
    dirs = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    d= dirs[dir]
    # for j in grid:
    #     print(j)
    dx = {'N': (0,len(grid)), 'S': (len(grid)-1, -1, -1), 'E': (0,len(grid)),'W': (0,len(grid)) }
    dy = {'E': (0, len(grid[0])), 'W': (len(grid[0])-1, -1, -1), 'N': (0, len(grid[0])), 'S': (0, len(grid[0])) }
    st = set()
    while True:
        good = False
        st = set()
        for i in range(*(dx[dir])):
            for j in range(*(dy[dir])):
                if grid[i][j] == 'O':
                    st.add((i,j))
                    nx, ny = i + d[0], j + d[1]
                    if nx >=0 and nx < len(grid) and ny >=0 and ny < len(grid[0]):
                        if grid[nx][ny] == '.':
                            good = True
                            grid[nx][ny] = 'O'
                            grid[i][j] = '.'
        # for j in grid:
        #     print(j)
        # print('\n')
        if not good:
            break
    return frozenset(st)

def gold(grid):
    seen = defaultdict(int)
    seen2 = defaultdict(list)
    cycle = 0
    cdir = ['N','W','S','E']
    fs = frozenset()
    cc = {}
    target = 1000000000
    for i in range(0, 1000000):
        if i%4 == 0:
            state = fs
            
            if state in seen:
                # for t in state:
                #     print(t)
                # print('\n')
                print('prev cycle', seen[state], cycle)
                cc[cdir[i%4]] = (seen[state], cycle, fs)
                rem = (target-cycle)%(cycle - seen[state])
                gd = 0
                for x,y in seen2[seen[state]+rem]:
                    gd += len(grid) - x
                print('gold is', gd)
                break
                
            seen[state] = cycle
            seen2[cycle] = state
            cycle+=1
        d = cdir[i%4]
        fs = tilt(grid, d)
        # for g in grid:
        #     print(g)
        # print(fs)
        print(i)
        
        
            
def load(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                res += len(grid)-i
    return res

tilt(grid)
print(load(grid))
grid = oldgrid
print(gold(grid))
