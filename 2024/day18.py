import fileinput
from collections import deque, defaultdict
from functools import cache
from heapq import heappop, heappush

lines = [l.strip() for l in fileinput.input()]

start = (0,0)
end = (70,70)
obstacles = set()
def bfs(start, end, obstacles=obstacles):
    q = deque([(start, 0)])
    visited = set()
    while q:
        pos, dist = q.popleft()
        if pos == end:
            return dist
        visited.add(pos)
        x, y = pos
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            new_pos = (x+dx, y+dy)
            if new_pos[0] < 0 or new_pos[0] > end[0] or new_pos[1] < 0 or new_pos[1] > end[1]:
                continue
            if new_pos in obstacles or new_pos in visited:
                continue
            visited.add(new_pos)
            q.append((new_pos, dist+1))
    return -1
limit = 1024
obstacles_all = []
for i, pair in enumerate(lines):
    y,x = pair.split(',')
    x,y = int(x),int(y)
    if i < limit:
        obstacles.add((x,y))
    obstacles_all.append((x,y))
print('silver', bfs(start, end, obstacles))

# binary first search path where its not possible
low = 0
hi = len(obstacles_all)
#end = (6,6)
while low < hi:
    mid = (low + hi) // 2
    obstacles = set(obstacles_all[:mid])
    if bfs(start, end, obstacles) == -1:
        hi = mid
    else:
        low = mid + 1
    print(low,hi)
print('gold', low-1, obstacles_all[low-1][::-1])
