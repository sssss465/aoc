import fileinput
from collections import deque, defaultdict
from functools import cache
from heapq import heappop, heappush

lines = [l.strip() for l in fileinput.input()]
start = []
end = []
walls = set()
n,m = len(lines), len(lines[0])
for i in range(n):
    for j in range(m):
        if lines[i][j] == 'S':
            start = (i,j)
        if lines[i][j] == 'E':
            end = (i,j)
        if lines[i][j] == '#':
            walls.add((i,j))


q = []
q.append((0, start, (0,1))) # score, start, direction
path = defaultdict(list)
visited = defaultdict(lambda: float('inf'))
visited[(start, (0,1))] = 0
end_state = None
while q:
    score, (i,j), (di,dj) = heappop(q)
    if score > visited[(i,j), (di,dj)]:
        continue
    visited[(i,j), (di,dj)] = min(score, visited[(i,j), (di,dj)])
    if (i,j) == end:
        print(score)
        end_state = ((i,j), (di,dj))
        break
    ni, nj = i+di, j+dj
    if ni >=0 and ni < n and nj >= 0 and nj < m and (ni,nj) not in walls:
        if visited[(i,j), (di,dj)] + 1 < visited[((ni,nj), (di,dj))] :
            heappush(q, (score+1, (ni,nj), (di,dj)))
            visited[((ni,nj), (di,dj))] = visited[(i,j), (di,dj)] + 1
            path[((ni,nj), (di,dj))] = [((i,j), (di,dj))]
        elif visited[(i,j), (di,dj)] + 1 == visited[((ni,nj), (di,dj))]:
            path[((ni,nj), (di,dj))].append(((i,j), (di,dj)))
    for off_di, off_dj in [(dj, -di), (-dj, di)]:
        left_di, left_dj = off_di, off_dj
        if visited[(i,j), (di,dj)] + 1000 < visited[((i,j), (left_di,left_dj))] :
            visited[((i,j), (left_di,left_dj))] = visited[(i,j), (di,dj)] + 1000
            path[((i,j), (left_di,left_dj))] = [((i,j), (di,dj))]
            heappush(q, (score+1000, (i,j), (left_di,left_dj)))
        elif visited[(i,j), (di,dj)] + 1000 == visited[((i,j), (left_di,left_dj))]:
            path[((i,j), (left_di,left_dj))].append(((i,j), (di,dj)))
q = deque([end_state])
vss = set()
visited = set()
dirs = [(0,1), (0,-1), (1,0), (-1,0)]
while q:
    pos, direction = q.popleft()
    vss.add(pos)
    visited.add((pos, direction))
    for i, nei_state in enumerate(path[(pos,direction)]):
        visited.add(nei_state)
        q.append(nei_state)

    #break
# 682 too high 598 too high 519 too low
print(len(vss))

for i in range(n):
    for j in range(m):
        if (i,j) in vss:
            print('O', end='')
        else:
            print(lines[i][j], end='')
    print()