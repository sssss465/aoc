import fileinput

lines = [l.strip() for l in fileinput.input()]
grid = []
ps = []
max_x, max_y = 0, 0 
st = 0
for l in lines:
    if len(l) == 0:
        break
    x,y = l.split(',')
    x,y = y,x
    ps.append((int(x), int(y)))
    max_x = max(max_x, int(x))
    max_y = max(max_y, int(y))
    st += 1
st += 1
grid = [[0]*(max_y+1) for i in range(max_x+1)]
for x,y in ps:
    grid[x][y] = 1
print(len(grid), len(grid[0]))
fst = 0
for i in range(st, len(lines)):
    d = lines[i].split(' ')[-1]
    d, pos = d.split('=')
    pos = int(pos)
    if d == 'y': # horizontal flip
        # for r in grid[:max_x+1]:
        #     print(r)
        for i in range(pos+1, max_x+1):
            for j in range(0, max_y+1):
                # print((i,j), pos, i, pos - (i - pos), max_x)
                grid[pos - (i-pos)][j] = min(grid[i][j] + grid[pos - (i-pos) ][j], 1)
        max_x = pos
    else:
        for i in range(0, max_x+1):
            for j in range(pos+1, max_y+1):
                grid[i][pos - (j-pos)] = min(grid[i][j] + grid[i][pos - (j-pos)], 1)
        max_y = pos
    if fst == 0:
        print('silver', sum([1 if grid[i][j] == 1 else 0 for j in range(max_y+1) for i in range(max_x+1) ]))
    fst += 1

print('gold')
for r in grid[:max_x+1]:
    print(''.join('x ' if i == 1 else '  'for i in r[:max_y+1]))
