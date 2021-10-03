import fileinput

lines = [l.strip() for l in fileinput.input()]
grid = [[0]*1000 for _ in range(1000)]
grid_gold = [[0]*1000 for _ in range(1000)]

for l in lines:
    l = l.split()
    if l[0] == 'turn':
        is_off = l[1] == 'off'
        for x in range(int(l[2].split(',')[0]), int(l[4].split(',')[0])+1):
            for y in range(int(l[2].split(',')[1]), int(l[4].split(',')[1])+1):
                grid[x][y] = 0 if is_off else 1
                grid_gold[x][y] = max(
                    0, grid_gold[x][y]-1) if is_off else grid_gold[x][y] + 1
    elif l[0] == 'toggle':
        for x in range(int(l[1].split(',')[0]), int(l[3].split(',')[0])+1):
            for y in range(int(l[1].split(',')[1]), int(l[3].split(',')[1])+1):
                grid[x][y] = 1 if grid[x][y] == 0 else 0
                grid_gold[x][y] += 2

print(f"Silver: {sum(sum(i) for i in grid)}")
print(f"Gold: {sum(sum(i) for i in grid_gold)}")
