import fileinput
from collections import Counter
import functools
from functools import cmp_to_key
import re
from collections import defaultdict, deque
from functools import cache
import math
import bisect
from dataclasses import dataclass

lines = [l.strip() for l in fileinput.input()]

graph = defaultdict(set)
parents = defaultdict(set)
updates = []
for l in lines:
    if "|" in l:
        l, r = l.split("|")
        graph[l].add(r)
    elif l:
        updates.append(l.split(","))


def mycmp(a, b):
    if b in graph[a]:
        return -1
    if a in graph[b]:
        return 1
    return 0


silver = 0
gold = 0

for u in updates:
    curmax = 0
    good = True
    vis = set()
    for i in u:
        for nei in graph[i]:
            if nei in vis:
                good = False
                break
        if not good:
            break
        vis.add(i)
    if good:
        silver += int(u[len(u) // 2])
    else:
        u.sort(key=cmp_to_key(mycmp))
        gold += int(u[len(u) // 2])

print("silver", silver)
print("gold", gold)
