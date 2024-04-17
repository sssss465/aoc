import fileinput
import re
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop

lines = [l.strip() for l in fileinput.input()]
map = defaultdict(list)
dist = defaultdict(lambda: float('inf'))
map2 = [[0 for j in range(len(lines[0]))] for i in range(len(lines))]
print(map2)
start= (0,0)
q = []
silver = 0
for i,line in enumerate(lines):
    for j in range(len(line)):
        if lines[i][j] == '.':
            continue
        if lines[i][j] == 'S':
            q.append((0, (i,j)))
            start = (i,j)
        if lines[i][j] == '|':
            map[(i+1,j)].append((i,j))
            map[(i-1,j)].append((i,j))
        elif lines[i][j] == '-':
            map[(i,j+1)].append((i,j))
            map[(i,j-1)].append((i,j))
        elif lines[i][j] == 'L':
            map[(i-1,j)].append((i,j))
            map[(i,j+1)].append((i,j))
        elif lines[i][j] == 'J':
            map[(i,j-1)].append((i,j))
            map[(i-1,j)].append((i,j))
        elif lines[i][j] == '7':
            map[(i,j-1)].append((i,j))
            map[(i+1,j)].append((i,j))
        elif lines[i][j] == 'F':
            map[(i+1,j)].append((i,j))
            map[(i,j+1)].append((i,j))
dist[q[0][1]] = 0
while q:
    d, cur = heappop(q)
    silver = max(silver, d)
    for n in map[cur]:
        if dist[n] > dist[cur]+1:
            dist[n] = dist[cur]+1
            heappush(q,(dist[n], n))

#gold 
def bfs(start, left=True):
    if start[0] < 0 or start[1] < 0 or start[0] >= len(map2) or start[1] >= len(map2[0]):
        return -float('inf')
    if map2[start[0]][start[1]] != 0:
        return 0
    
    cur = 0 
    q = deque([start])
    bad = False
    vis = set()
    while q:
        t = q.popleft()
        cur +=1
        map2[t[0]][t[1]] = 'l' if left else 'r'
        vis.add(t)
        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
            a,b = t[0]+x, t[1]+y
            if a < 0 or b < 0 or a >= len(map2) or b >= len(map2[0]):
                bad = True
                continue
            if (a,b) not in vis and map2[a][b] == 0:
                q.append((t[0]+x,t[1]+y))
    
    return cur if not bad else -float('inf')

# we need to take one long traversal going through the pipe while tagging all of the right side of the pipe with t if they are equal to . as inside the pipe

cur = start
visited = set()
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
lefts,rights = 0,0
leftres, rightres = 0,0
been = []
while cur not in visited:
    visited.add(cur)
    been.append(cur)
    for n in map[cur]:
        if n not in visited:
            ori = dirs.index((n[0]-cur[0], n[1]-cur[1]))
            left = (ori-1)%len(dirs)
            right = (ori+1)%len(dirs)
            # print((n[0]-cur[0], n[1]-cur[1]),dirs[left],dirs[right])
            left = (cur[0]+dirs[left][0], cur[1]+dirs[left][1])
            right = (cur[0]+dirs[right][0], cur[1]+dirs[right][1])
            cl, cr = bfs(left, left=True), bfs(right, left=False)
            print(n, cl,cr)
            if cl< 0:
                lefts += 1
            leftres += cl
            if cr < 0:
                rights += 1 
            rightres += cr
            cur = n
            break
assert(lefts==0 or rights==0)
print(lefts,rights,leftres,rightres, been)       

# gold = 0
# for i in range(len(map2)):
#     for j in range(len(map2[0])):
#         if map2[i][j] == 't':
#             c = bfs((i,j)) 
#             if c >=0:
#                 print(c)
#             gold +=  0 if c < 0 else c

for i in range(len(lines)):
    l = [map2[i][j] for j in range(len(lines[0]))]
    print(l)
print(silver)
#print(gold)
        