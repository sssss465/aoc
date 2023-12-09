import fileinput
import re

lines = [line.strip() for line in fileinput.input()]
print(len(lines))
silver = 0
gold = 0
for line in lines:
    nums = [int(i) for i in line.split()]
    rows = []
    rows2 = []
    cur = [int(i) for i in nums]
    while not all(i==0 for i in cur):
        rows.append(cur[:])
        rows2.append(cur[::-1])
        diffs = []
        for i in range(1,len(cur)):
            diffs.append(cur[i]-cur[i-1])
        cur = diffs
    rows.append(cur[:])
    rows2.append(cur[:])
    c = 0
    c2 = 0
    assert(len(rows) == len(rows2))
    for j in range(len(rows)-1,-1 ,-1):
       # print(rows[j])
        rows[j].append(rows[j][-1]+c)
        c = rows[j][-1]
        rows2[j].append(rows2[j][-1]-c2)
        c2 = rows2[j][-1]
    silver += (rows[0][-1])
    gold += (rows2[0][-1])
print(silver)
print(gold)
