import fileinput
import re
import bisect
from collections import defaultdict

lines = [l.strip() for l in fileinput.input()]
digs = '0123456789.'

dirs = [(-1,0), (1,0), (0,-1), (0,1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
silver = []
gears = defaultdict(set)
for i in range(len(lines)):
    cur = 0
    good = False
    tags = []
    for j in range(len(lines[0])):
        if lines[i][j] == '.' or lines[i][j] not in digs:
            if good:
                silver.append(cur)
                for t in tags:
                    gears[t].add(cur)
            cur=0
            good = False
            tags = []
            continue
        cur = cur*10 + int(lines[i][j])
        for x,y in dirs:
            a = i+x
            b = j+y
            if a >=0 and a < len(lines) and b >=0 and b < len(lines[0]):
                if lines[a][b] not in digs:
                   # assert 1==3
                    if lines[a][b] == '*':
                        tags.append((a,b))
                    good = True
    if good:
        silver.append(cur)
        for t in tags:
            gears[t].add(cur)
#print(silver)
#print(gears)
gold=0
for k,v in gears.items():
    if len(v) == 2:
        gold += v.pop()*v.pop()
print(sum(silver))
print(gold)

                    
        
