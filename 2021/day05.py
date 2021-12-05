import fileinput

lines = [l.strip() for l in fileinput.input()]

grid = [[0] * 1000 for _ in range(1000)]
silver = 0
skipped = []
for line in lines:
    start, end = line.split("->")
    start = list(map(int, start.split(",")))
    end = list(map(int, end.split(",")))
    if start[1] == end[1]:
        for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            grid[i][start[1]] += 1
    elif start[0] == end[0]:
        for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            grid[start[0]][i] += 1
    else:
        skipped.append((start, end))
for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1:
            silver += 1
print("silver", silver)

gold = 0
for start, end in skipped:
    if start[0] > end[0]:
        start, end = end, start
    if start[1] < end[1]:
        # sloping up
        beg = start
        while beg != end:
            grid[beg[0]][beg[1]] += 1
            beg = [beg[0] + 1, beg[1] + 1]
        grid[beg[0]][beg[1]] += 1
    else:
        # sloping down
        beg = start
        while beg != end:
            grid[beg[0]][beg[1]] += 1
            beg = [beg[0] + 1, beg[1] - 1]
        grid[beg[0]][beg[1]] += 1
for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1:
            gold += 1
print("gold", gold)
