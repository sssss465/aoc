import fileinput
from collections import defaultdict, deque

dirs = [(0,1), (0, -1), (1,0), (-1,0)]
lines = [[int(i) for i in l.strip()] for l in fileinput.input()]
def bfs(start):
    q = deque([start])
    ends = set()
    golds = 0
    while q:
        x,y = q.popleft()
        if lines[x][y] == 9:
            ends.add((x,y))
            golds += 1
            continue
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if nx >=0 and nx < len(lines) and ny >=0 and ny < len(lines[0]):
                if lines[nx][ny] == lines[x][y] + 1:
                    q.append((nx,ny))
    return len(ends), golds

silver = 0
gold = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 0:
            s,g = bfs((i,j)) # bad variable name 
            silver+= s
            gold += g 

print('silver', silver)
print('gold', gold)



