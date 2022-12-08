import fileinput

lines = [line.strip() for line in fileinput.input()]
grid = []
for line in lines:
    grid.append(list(int(i) for i in list(line)))
silver = 0
gold = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        n = [i, j]
        cur = n[:]
        good = False
        score = []
        for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            trees = 0
            if cur[0] == 0 or cur[0] == len(grid) - 1 or cur[1] == 0 or cur[1] == len(grid[0]) - 1:
                good = True
            cur[0] += dir[0]
            cur[1] += dir[1]
            while cur[0] >= 0 and cur[0] < len(grid) and cur[1] >= 0 and cur[1] < len(grid[0]):
                trees += 1
                if grid[cur[0]][cur[1]] >= grid[n[0]][n[1]]:
                    break
                if cur[0] == 0 or cur[0] == len(grid) - 1 or cur[1] == 0 or cur[1] == len(grid[0]) - 1:
                    good = True
                    break
                cur[0] += dir[0]
                cur[1] += dir[1]
            score.append(trees)
            cur = n[:]
        gold = max(gold, score[0] * score[1] * score[2] * score[3])
        if good:
            silver += 1
print(silver)
print(gold)
