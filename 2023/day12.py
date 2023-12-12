import fileinput
from collections import Counter
import functools
import re
from collections import defaultdict,deque
from functools import cache
import math
import bisect

lines = [l.strip() for l in fileinput.input()]

old_arrange = []

#slow code below
def valid(mp, arrange, last=True):
    gps = []
    cur = []
    #assert '?' not in mp
    for c in mp:
        if c == '#':
            cur.append('#')
        else:
            if cur:
                gps.append(''.join(cur))
            cur = []
    if cur:
        gps.append(''.join(cur))
    #print(gps, old_arrange)
    if len(old_arrange) < len(gps):
        return False
    for i in range(len(old_arrange)):
        if i >= len(gps):
            return not last
        if old_arrange[i] != len(gps[i]):
            return False
    return True

def mid_valid(mp, arrange, last=True):
    gps = []
    cur = []
    #assert '?' not in mp
    for c in mp:
        if c == '#':
            cur.append('#')
        else:
            if cur:
                gps.append(''.join(cur))
            cur = []
    if cur:
        gps.append(''.join(cur))
    #print(gps, old_arrange)
    if len(old_arrange) < len(gps):
        print('bad1')
        return False
    for i in range(len(old_arrange)):
        if i >= len(gps):
            return not last
        if old_arrange[i] < len(gps[i]):
            print('bad2')
            return False
    return True
    
def dfs(mp, arrange,cur=0,i=0):
    if i >= len(mp) or cur >= len(arrange):
        return 1 if valid(mp, arrange) else 0
    # if not mid_valid(mp, arrange, last=False):
    #     print(mp,arrange,False)
    #     return 0
    if mp[i] == '#':
        arrange[cur]-=1
        skip = dfs(mp, arrange,cur if arrange[cur] else cur+1,i+1)
        arrange[cur]+=1
        return skip
    if mp[i] != '?':
        return dfs(mp, arrange,cur,i+1)
    res = 0
    mp[i] = '.'
    res += dfs(mp, arrange,cur,i+1)
    mp[i] = '#'
    arrange[cur] -=1 
    res += dfs(mp, arrange,cur if arrange[cur] else cur+1,i+1)
    arrange[cur] +=1
    mp[i] = '?'
    return res

# def solve(mp, arrange):
# Dynamic programming. f (pos, groups, len) = number of ways to:

# parse the first pos positions
# have groups groups of #
# with the last group of # having length len
# The transitions are:

# if the character is # or ?, we can continue the previous group or start a new group:
# f (pos + 1, groups, len + 1) += f (pos, groups, len)
# if the character is . or ?, and the length of the current group is zero or exactly what we need, we can proceed without a group:
# f (pos + 1, groups + (len==arrange[groups], 0) += f (pos, groups, len)
# In the end, the answer is f (lastPos, numberOfGgroups, 0). (Add a trailing . to the string for convenience to avoid cases.)
def solve(mp, arrange):

    mp.append('.') # catches edge case with sequence ending on last char
    @cache
    def dp(pos, groups, ln):
        #print(pos,groups,ln)
        if pos >= len(mp):
            if groups == len(arrange) and ln == 0:
                return 1
            return 0
        
        res = 0
        #print(pos,groups,ln, pos >= len(mp))
        # if mp[pos] == '#' or mp[pos] == '?':
        #     res += dp(pos + 1, groups , ln + 1)
        # if mp[pos] == '.' or mp[pos] == '?':
        #     res += dp(pos + 1, groups + (ln == arrange[groups] if groups<len(arrange) else 0), 0)

        if mp[pos] in '.?' and ln==0:
            res += dp(pos + 1, groups, 0)
        if mp[pos] in '.?' and ln and groups < len(arrange) and arrange[groups] == ln:
            res += dp(pos + 1, groups+1, 0)
        if mp[pos] in '#?':
            res += dp(pos+1, groups, ln+1)
        return res

    s= dp(0, 0, 0)
    dp.cache_clear()
    return s
    
    
silver=0
for ii, line in enumerate(lines):
    mp, arrange = line.split()
    arrange = [int(x) for x in arrange.split(',')]
    mp = list(mp)
   # print(mp, arrange)
    old_arrange = arrange[:]
    #c = dfs(mp,arrange,cur=0,i=0)
    c = solve(mp, arrange)
    # c = count_arrangements(mp, arrange)
    #print(c)
    silver+=c
    # if ii == 1:
    #     break
gold = 0
for ii, line in enumerate(lines):
    mp, arrange = line.split()
    arrange = [int(x) for x in arrange.split(',')]
    mp = list(mp)
    mp, arrange = (mp + ['?'])*5 , arrange*5
    mp.pop()
    ##print(mp, arrange)
    old_arrange = arrange[:]
    c = solve(mp,arrange)
    #print(c)
    gold+=c

print(silver)
print(gold)

wrong = 7570 #toohigh
