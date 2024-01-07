import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict,deque
from functools import cache
import math
import bisect

lines = [l.strip() for l in fileinput.input()]

def solve(step):
    cur = 0
    for c in step:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur
silver=0
gold=0
mp = defaultdict(list)
label = {}

for line in lines:
    l = line.split(',')
    for s in l:
        silver+= solve(s)
        if '=' in s:
            lab,v = s.split('=')
            good = False
            for lens in mp[solve(lab)]:
                if lens[0] == lab:
                    lens[1] = v
                    good = True
                    break
            if not good:
                mp[solve(lab)].append([lab,v])
        else:
            box = solve(s[:-1])
            for i in range(len(mp[box])):
                if mp[box][i][0] == s[:-1]:
                    del mp[box][i]
                    break
for k,v in mp.items():
    for i,lens in enumerate(v):
        lb,lp = lens
        gold += (k+1) * (i+1) * int(lp)
print(silver)
print(gold)
