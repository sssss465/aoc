import fileinput
from collections import defaultdict, deque

lines = [l.strip() for l in fileinput.input()]

line = lines[0]
d = defaultdict(int)
def solve(silver=True):
    taken = []
    free = deque()
    cur = 0
    for i in range(len(line)):
        c = int(line[i])
        if c == 0:
            continue
        if i%2 == 1:
            free.append([cur, cur+c-1])
        else:
            taken.append([cur, cur+c-1, i//2])
        cur += c
    #print(taken,free)
    taken2 = []
    if silver:
        while free and free[0][1] < taken[-1][1]:
            l,r = free[0]
            slots = r-l +1 
            tl, tr, iid = taken[-1]
            need = tr - tl +1
            delta = min(slots, need)
            taken2.append([l, l+delta-1, iid])
            l += delta
            tr -= delta
            if l > r:
                free.popleft()
            else:
                free[0] = [l,r]
            if tl > tr:
                taken.pop()
            else:
                taken[-1] = [tl, tr, iid]
    else:
        for i in range(len(taken)-1, -1, -1):
            for j in range(len(free)):
                l,r = free[j]
                slots = r-l +1 
                tl, tr, iid = taken[i]
                need = tr - tl +1
                if l > tl:
                    break
                if need > slots:
                    continue
                taken[i] = [l, l+need-1, iid]
                free[j] = [l+need, r] # if l+need > r it will be invalid

    silvers = sorted(taken + taken2)
    res = 0
    for l,r, iid in silvers:
        for j in range(l,r+1):
            res += iid*j
    if silver:
        print('silver', res) 
    else:
        print('gold', res)
solve()
solve(False)
# too big 15825847038794