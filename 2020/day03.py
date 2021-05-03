import fileinput

grid = []
for line in fileinput.input():
    grid.append(list(line.strip()))

n, m = len(grid), len(grid[0])
x, y = 0, 0
silver = 0
for j in range(n):
    if grid[j][x] == '#':
        silver += 1
    x = (x+3) % (m)
    y += 1
print('silver', silver)
gold = 1
for px, py in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    rs = 0
    x = 0
    for j in range(0, n, px):
        if grid[j][x] == '#':
            rs += 1
        print(j, x)
        x = (x+py) % (m)
    gold *= rs
print('gold', gold)
