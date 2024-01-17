import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict,deque
from functools import cache
import math
import bisect

lines = [l.strip() for l in fileinput.input()]

graph = defaultdict(list)
graph2 = defaultdict(list)
pieces = []

def factorygt(rss, amt):
    return lambda x: rss if x > int(amt) else False

def factorylt(rss, amt):
    return lambda x: rss if x < int(amt) else False

def factorynx(r):
    return lambda x: r

rules = True
for l in lines:
    if not l:
        rules = False
        continue
    if rules:
        #print(l)
        wd, rul = re.findall(r'(\w+){(.*?)}', l)[0]
        mp = []
        mp2 = []
        for r in rul.split(','):
            bounds = [1, 4000]
            if ':' in r:
                func, rss = r.split(':')
                targ, sign, amt = re.findall(r'(\w+)(<|>|<=|>=)(\d+)', func)[0]
                if sign == '>':
                    mp.append((targ, factorygt(rss, amt)))
                    bounds = [int(amt)+1, 4000]
                elif sign == '<':
                    mp.append((targ, factorylt(rss, amt)))
                    bounds = [1, int(amt)-1]
                mp2.append((targ, bounds, rss))
            else: # last rule
                mp.append((r[:], factorynx(r)))
                mp2.append((r[:], bounds, r[:]))
        graph[wd] = mp
        graph2[wd]= mp2
    else:
        mp = defaultdict(int)
        rul = re.findall(r'{(.*?)}', l)[0]
        for rr in rul.split(','):
            ll,rr = rr.split('=')
            mp[ll] = int(rr)
        pieces.append(mp)

# print(graph)
# print(pieces)
#print(graph2)

def dfs(cur='in', state={'x':[1,4000], 'm':[1,4000],'a':[1,4000],'s':[1,4000],}):
    print(cur)
    if cur == 'R':
        return 0
    if cur == 'A':
        sx, bx = state['x']
        sm, bm = state['m']
        sa, ba = state['a']
        ss, bs = state['s']
        #print('done', state)
        return max(0, (bx - sx + 1) * (bm - sm + 1) * (ba - sa + 1) * (bs - ss+1))
    res = 0
    cur_state = {k:v[:] for k,v in state.items()}
    for nei, (l,r), dest in graph2[cur]:
        cc = {k:v[:] for k,v in cur_state.items()}
        if nei in cur_state: #handle last case
            cc[nei] = [max(cur_state[nei][0], l), min(cur_state[nei][1], r)]
            if cc[nei][0] > cur_state[nei][0]: # remove matching interval 
                cur_state[nei] = [cur_state[nei][0], cc[nei][0]-1]
            else:
                cur_state[nei] = [cc[nei][1]+1, cur_state[nei][1]]
        res += dfs(dest, cc)
    return res

res = 0 
for p in pieces:
    cur = 'in'
    ii = 0
    while cur not in ('A', 'R'):
        m = graph[cur]
        #print(cur,p)
        for i,(name, rule) in enumerate(m):
            nxt = rule(p[name])
            #print(nxt, name, rule)
            if nxt:
                cur = nxt
                break
        
    if cur == 'A':
        res += sum(p.values())
    #print()

print(res)
    
print(dfs())
