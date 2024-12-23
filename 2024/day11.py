import fileinput
from collections import defaultdict, deque
from functools import cache
import sys
lines = [l.strip() for l in fileinput.input()]

maxdepth = 25
@cache
def dfs(ele, depth=0):
    if depth == maxdepth:
        return 1
    if ele == 0:
        return dfs(1, depth+1)
    elif len(str(ele))%2 == 0:
        s = str(ele)
        l,r = s[:len(s)//2], s[len(s)//2:]
        return dfs(int(l), depth+1) + dfs(int(r), depth+1)
    else:
        return dfs(ele*2024, depth+1)
    
row = [int(i) for i in lines[0].split()]
silver = 0
gold = 0
for ele in row:
    maxdepth = 25
    silver += dfs(ele, 0)
    maxdepth = 75
    dfs.cache_clear()
    gold += dfs(ele, 0)
    dfs.cache_clear()
print('silver', silver)
print('gold', gold)