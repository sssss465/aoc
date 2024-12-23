import fileinput
from functools import cache
from collections import defaultdict

lines = [l.strip() for l in fileinput.input()]

n = len(lines)
m = len(lines[0])
sigs = defaultdict(list)
silver = set()
gold = set()
for i in range(n):
    for j in range(m):
        if lines[i][j] != '.':
            sigs[lines[i][j]].append((i,j))

for sig in sigs:
    locations = sigs[sig]
    for l in locations:
        gold.add(l)
        for other in locations:
            if l != other:
                dx, dy = other[0] - l[0], other[1] - l[1]
                nx, ny = l[0] - dx, l[1] - dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    silver.add((nx,ny))
                while nx >= 0 and nx < n and ny >= 0 and ny < m:
                    gold.add((nx,ny))
                    nx, ny = nx - dx, ny - dy
print('silver', len(silver))
print('gold', len(gold))
