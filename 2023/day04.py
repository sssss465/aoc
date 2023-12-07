import fileinput
import re
import bisect
from collections import defaultdict

lines = [l.strip() for l in fileinput.input()]
silver=0
gold =0
copies = [1]*len(lines)
for j,l in enumerate(lines):
    digs = [int(i) for i in re.findall(r'(\d+)', l)]
    digs.pop(0)
    last = int(re.findall(r'(\d+) \|', l)[0])
    good = False
    mine = set()
    cur = -1
    for i in range(len(digs)):
        if good:
            if digs[i] in mine:
                cur+=1
        else:
            if digs[i] == last:
                good = True
            mine.add(digs[i])
    if cur > -1:
        silver += pow(2,cur)
    matches = cur+1
    for k in range(j+1,j+1+matches):
        copies[k]+=copies[j]
print(copies)
    


print(silver)
print(sum(copies))
