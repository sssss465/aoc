import fileinput

lines = [line.strip() for line in fileinput.input()]
dirs = list(lines[0])
grid = {(0, 0): 1}
grid2 = {(0, 0): 1}
x, y = 0, 0
santx, santy = 0, 0
robx, roby = 0, 0
cur = 0
for d in dirs:
    if d == '^':
        y -= 1
        santy -= 1 if cur % 2 == 0 else 0
        roby -= 1 if cur % 2 == 1 else 0
    elif d == 'v':
        y += 1
        santy += 1 if cur % 2 == 0 else 0
        roby += 1 if cur % 2 == 1 else 0
    elif d == '<':
        x -= 1
        santx -= 1 if cur % 2 == 0 else 0
        robx -= 1 if cur % 2 == 1 else 0
    elif d == '>':
        x += 1
        santx += 1 if cur % 2 == 0 else 0
        robx += 1 if cur % 2 == 1 else 0
    grid[(x, y)] = 1
    grid2[(santx, santy)] = 1
    grid2[(robx, roby)] = 1
    cur += 1
print(f"silver: {sum(grid.values())}")
print(f"gold: {sum(grid2.values())}")
