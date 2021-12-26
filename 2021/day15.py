import fileinput
import heapq
import collections
grid = [list(map(int, list(l.strip()))) for l in fileinput.input()]

def solve(grid):
    print(len(grid[0]), len(grid))
    for i in range(1, len(grid)):
        grid[i][0] += grid[i-1][0]
    for j in range(1, len(grid[0])):
        grid[0][j] += grid[0][j-1]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]

def solve2(grid):
    #dijkstras
    heap = [[0, (0, 0)]]
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0 ]]
    visited = collections.defaultdict(int)
    parent = {}
    while heap:
        v, loc = heapq.heappop(heap)
        for x,y in dirs:
            a = loc[0] + x
            b = loc[1] + y
            if a >= 0 and a < len(grid) and b >= 0 and b < len(grid[0]):
                if (a,b) not in visited:
                    visited[(a,b)] = v + grid[a][b]
                    heapq.heappush(heap, [v+grid[a][b], (a,b)])
                    # parent[(a,b)] = loc
                else:
                    visited[(a,b)] = min(visited[(a,b)], v + grid[a][b])
                    # if v + grid[a][b] < visited[(a,b)]:
                    #     parent[(a,b)] = loc
    # def printpath(i,j):
    #     path = []
    #     while (i,j) != (0,0):
    #         path.append([i,j])
    #         i,j = parent[(i,j)]
    #     path.append([0,0])
    #     print(path[::-1])
    # printpath(len(grid)-1, len(grid[0])-1)
    return visited[(len(grid)-1, len(grid[0])-1)]   


grid2 = [[0]*(5*len(grid[0])) for i in range(5*len(grid))]

for i in range(len(grid2)):
    for j in range(len(grid2[0])):
        tx, ty = i//len(grid), j // len(grid[0])
        # print(i,j, tx, ty)
        grid2[i][j] = (grid[i%len(grid)][j%len(grid[0])] + tx + ty)
        if grid2[i][j] >= 10:
            # print(grid2[i][j])
            grid2[i][j] -= 9
print('silver', solve(grid))
print('gold', solve2(grid2))

# for r in grid2:
#     print(r)
