import fileinput
from collections import defaultdict, deque
from functools import cache
import sys
lines = [l.strip() for l in fileinput.input()]

grid = []
dirs = ''
done = False
n,m = 0, len(lines[0])
for r in lines:
    if not r:
        done = True
        continue
    if done:
        dirs += r
    else:
        grid.append(list(r))
        n+=1

cur = []
cur2 = []
walls = set()
boxes = set()
walls2 = set()
boxes2 = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'O':
            boxes.add((i,j))
            boxes2.add((i,j*2))
        if grid[i][j] == '#':
            walls.add((i,j))
            walls2.add((i,j*2))
        if grid[i][j] == '@':
            cur = (i,j)
            cur2 = (i,j*2)

def scanpush2(d):
    #wrong 1493666
    global cur2
    dmap = {'^': [(-1, -1),(-1, 0)], 'v': [(1,0), (1, -1)], '<': [(0, -2)], '>': [(0, 1)]} # collisions against person
    box_map = {'^': [(-1, 1), (-1, -1),(-1, 0)], 'v': [(1,0), (1, -1), (1, 1)], '<': [(0, -2)], '>': [(0, 2)]}
    dmap_orig = {'^': (-1, 0), 'v': (1,0), '<': (0, -1), '>': (0, 1)}
    ddirs = box_map[d]
    dir_orig = dmap_orig[d]
    moving = set()
    q = deque()
    for m in dmap[d]:
        nx, ny = cur2[0] + m[0], cur2[1] + m[1]
        if (nx,ny) in boxes2:
            q.append((nx,ny))
        if (nx, ny) in walls2:
            return
    while q:
        t = q.popleft()
        if t in walls2:
            return
        moving.add(t)
        for dx, dy in ddirs:
            nx, ny = t[0] + dx, t[1] + dy
            if (nx,ny) in boxes2:
                q.append((nx,ny))
            if (nx, ny) in walls2:
                return
    for m in moving:
        boxes2.remove(m)
    cur2 = (cur2[0] + dir_orig[0], cur2[1] + dir_orig[1])
    for m in moving:
        boxes2.add((m[0] + dir_orig[0], m[1] + dir_orig[1]))


def scanpush(d):
    global cur
    dmap = {'^': (-1, 0), 'v': (1,0), '<': (0, -1), '>': (0, 1)}
    dx, dy = dmap[d]
    sofar = set([cur])
    px, py = cur
    px += dx
    py += dy
    while (px,py) in boxes:
        sofar.add((px,py))
        px += dx
        py += dy
    # either we hit a wall after or not
    if (px,py) in walls:
        return
    cur = (cur[0] + dx, cur[1] + dy)
    if cur in boxes: # we only need to move two boxes
        boxes.remove(cur)
        boxes.add((px,py))

def print_gold():
    for i in range(n):
        j = 0
        while j < m*2:
            if (i,j) in boxes2:
                print('[]', end="")
                j+=2
            elif (i,j) in walls2:
                print('##', end="")
                j+=2
            elif (i,j) == cur2:
                print('@', end="")
                j+=1
            else:
                print('.', end="")
                j+=1
        print('\n', end="")

for d in dirs:
    scanpush(d)
    scanpush2(d)
    i+=1
silver = 0
gold=0
for bx, by in boxes:
    silver += 100*bx + by

for bx, by in boxes2:
    gold += 100*bx + by
        

print(silver)
print(gold)


