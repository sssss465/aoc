import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict,deque
from functools import cache
import math
import bisect

lines = [l.strip() for l in fileinput.input()]

cur = (0,0)
curbig = (0,0)
dirs = {'D': (1,0), 'U': (-1,0), 'R': (0,1), 'L': (0,-1)}
#0 means R, 1 means D, 2 means L, and 3 means U.
dirs2 = {'0':'R' ,'1':'D', '2':'L', '3':'U'}
map = defaultdict(lambda: '.')

lastr = {}

startx, starty = 0,0
endx, endy = 0,0
area =0
fs = 0

def corner(x,y):
    if map[(x,y)] != '#':
        return -1
    if map[(x+1,y)] == '#' and map[(x,y+1)] == '#':
        return 1 # top left
    if map[(x+1,y)] == '#' and map[(x,y-1)] == '#':
        return 2 # top right
    if map[(x-1,y)] == '#' and map[(x,y+1)] == '#':
        return 3 # bottom left
    if map[(x-1,y)] == '#' and map[(x,y-1)] == '#':
        return 4 # bottom right
    if map[(x,y-1)] == '#' and map[(x,y+1)] == '#':
        return 5 # top
    return 0


#find area of polygon given list of points using shoelace formula
def shoelace(list,border):
    area = 0
    for i in range(len(list)):
        area += list[i][0]*list[(i+1)%len(list)][1]
        area -= list[(i+1)%len(list)][0]*list[i][1]
        #print(abs(list[i][0] - list[(i+1)%len(list)][0]) + abs(list[i][1] - list[(i+1)%len(list)][1]))
    return abs(area)//2 + border
    
points2 = []
points1 = []
border=0
border2 = 0
for line in lines:
    print(re.findall(r'(\w) (\d+) \((.*)\)', line))
    d, c, color = re.findall(r'(\w) (\d+) \((.*)\)', line)[0]
    cx,cy = dirs[d]
    border+=int(c)
    print(c)
    points1.append(cur)
    for i in range(int(c)):
        map[cur] = '#'
        area+=1
        lastr[cur[0]] = cur[1]
        startx = min(startx, cur[0])
        starty = min(starty, cur[1])
        endx = max(endx, cur[0])
        endy = max(endy, cur[1])
        cur = (cur[0]+cx, cur[1]+cy)

    bigc = int(color[1:6],16)
    bigd = dirs2[color[-1]]
    cx,cy = dirs[bigd]
    points2.append(curbig)
    cx *= bigc
    cy *= bigc
    border2+=bigc
    curbig = (curbig[0]+cx, curbig[1]+cy)
print(points1)
print(points2)
#points2.append((0,0))
    
#map[(0,0)] = 'S'

for i in range(startx,endx+1):
    parity = 0
    j = starty
    while j <= endy:
        if map[(i,j)] == '#':
            if corner(i,j) in (1,2,0):
                parity = parity^1
            j+=1
            continue
        if parity:
            map[(i,j)] = 'F'
            fs+=1
        j+=1
# for i in range(startx, endx+1):
#     for j in range(starty, endy+1):
#         print(map[(i,j)], end='')
#     print()

print(area+fs)
print(border, border2)
print(shoelace(points1,0) + (border//2) + 1) # picks theorum and shoelace formula... way too niche knowledge lol
print(shoelace(points2,0) + (border2//2) + 1)

wrong = 55748 # too high
