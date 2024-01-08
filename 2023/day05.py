import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict, deque
from functools import cache
import math
import bisect
from dataclasses import dataclass

lines = [l.strip() for l in fileinput.input()]
mps = []

seeds = [int(i) for i in re.findall(r"(\d+)", lines[0])]

seeds2 = [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
mp = []
for l in lines[2:]:
    if not l:
        mps.append(mp)
        mp = []
        continue
    if l[0].isalpha():
        continue
    mp.append([int(x) for x in l.split()])
if mp:
    mps.append(mp)


def solve(seeds, gold=False):
    res = float("inf")
    for i in range(len(seeds)):
        good = False
        cur = seeds[i]
        for j in range(len(mps)):
            for m in mps[j]:
                if m[1] <= cur < m[1] + m[2]:
                    good = True
                    cur = m[0] + (cur - m[1])
                    break
        res = min(res, cur)
    print(res)


def solve2(seeds, gold=False):
    res = float("inf")
    for i in range(len(seeds)):
        good = False
        for k in seeds[i]:
            cur = k
            for j in range(len(mps)):
                for m in mps[j]:
                    if m[1] <= cur < m[1] + m[2]:
                        good = True
                        cur = m[0] + (cur - m[1])
                        break
            res = min(res, cur)
    print(res)


solve(seeds)
solve2(seeds2)
