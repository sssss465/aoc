import fileinput
from collections import defaultdict

lines = [line for line in fileinput.input()]
grid = [list(line.strip()) for line in lines]
order = [[(-1, -1), (-1, 0), (-1, 1)], [(1, -1), (1, 0), (1, 1)],
         [(-1, -1), (0, -1), (1, -1)], [(-1, 1), (0, 1), (1, 1)]]
order_s = 0
elves = set()  # elf position (x,y)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            elves.add((i, j))


def movable(elf):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y = elf[0] + dx, elf[1] + dy
        if (x, y) in elves:
            return True
    return False


def propose(elf, props):

    for i in range(order_s, order_s+4):
        left, mid, right = order[i % 4]
        l, m, r = (elf[0]+left[0], elf[1]+left[1]), (elf[0]+mid[0],
                                                     elf[1]+mid[1]), (elf[0]+right[0], elf[1]+right[1])
        if l not in elves and m not in elves and r not in elves:
            props[m].append(elf)
            return True
    return False


def print_elves():
    sx, sy = float('inf'), float('inf')
    bx, by = float('-inf'), float('-inf')
    for k, v in elves:
        sx = min(sx, k)
        sy = min(sy, v)
        bx = max(bx, k)
        by = max(by, v)

    for i in range(sx, bx+1):
        for j in range(sy, by+1):
            if (i, j) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print()


# print_elves()
for round in range(1, 4000):
    props = defaultdict(list)  # proposed new positions -> list of elves
    elves_new = set()
    good = True
    for x, y in elves:
        if not (movable((x, y)) and propose((x, y), props)):
            elves_new.add((x, y))
    for k, v in props.items():
        if len(v) == 1:
            elves_new.add(k)
        else:
            elves_new = elves_new.union(v)

    if elves == elves_new:
        print('gold', round)
        break

    elves = elves_new
    order_s = (order_s+1) % 4
    # print_elves()

    if round == 10:
        sx, sy = float('inf'), float('inf')
        bx, by = float('-inf'), float('-inf')
        for k, v in elves:
            sx = min(sx, k)
            sy = min(sy, v)
            bx = max(bx, k)
            by = max(by, v)

        print('silver', (bx-sx+1)*(by-sy+1) - len(elves))
