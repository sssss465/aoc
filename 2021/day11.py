import fileinput

lines = [l.strip() for l in fileinput.input()]

steps = 100
silver = 0
grid = [list(map(int, list(l))) for l in lines]
grid2 = [l[:] for l in grid]
dirs = [[-1, -1], [1, 1], [-1, 1], [1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
def proc(grid):
    flashed = set()
    def dfs(i,j):
        if grid[i][j] < 10 or (i,j) in flashed:
            return
        flashed.add((i,j))
        for x,y in dirs:
            a = i+x
            b = j+y
            if a >= 0 and a < len(grid) and b >= 0 and b < len(grid[0]):
                grid[a][b] += 1
                dfs(a,b)
    flashes= 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] +=1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] >= 10:
                dfs(i,j)
    for i,j in flashed:
        grid[i][j] = 0
    flashes = len(flashed)
    return flashes


for _ in range(steps):
    silver += proc(grid)
print('silver:' , silver)
gold = 1
while proc(grid2) != len(grid2) * len(grid2[0]):
    gold += 1
print('gold: ', gold)
