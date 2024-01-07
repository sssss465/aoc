import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict,deque
from functools import cache
import math
import bisect
from dataclasses import dataclass

lines = [line.strip() for line in fileinput.input()]

def reflect(grid):
    res = Counter()
    for r in grid:
        for i in range(1,len(r)):
            if i <= len(r)//2:
                #print(r[:i], r[i:i+i][::-1])
                if r[:i][::-1] == r[i:i+i]:
                    res[i]+=1
            else:
                #print('second half', r)
                #print(r[i - (len(r) - i):i][::-1] , '  ',  r[i:],'  ', )
                if r[i:][::-1] == r[i - (len(r) - i):i]:
                    res[i]+=1
        #print(r, res)
    out = [0,0]
    for k,v in res.items():
        if v == len(grid):
            out[0] = k
        if v == len(grid)-1:
            out[1] = k
    return out
i=0
vertical = 0
horizontal = 0
vertgold = 0
horigold=0
checks = 0
while i < len(lines):
    cur = []
    while i < len(lines) and len(lines[i]) > 0 :
        cur.append(lines[i])
        i+=1
    v, vg = reflect(cur)
    h, hg = reflect(list(zip(*cur)))
    vertical += v
    horizontal += h
    vertgold += vg
    horigold += hg
    i+=1
    #print(vertical, horizontal)
    checks += 1
    # if checks == 2:
    #     break
print(vertical + 100*horizontal)
print(vertgold + 100*horigold)
wrong = 38139
