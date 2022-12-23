import fileinput
import re

lines = [line for line in fileinput.input()]
lines, letters = ''.join(lines).split('\n\n')
grid = [list(l) for l in lines.splitlines()]
cmds = [int(l) if l not in 'LRUD' else l for l in re.findall(
    r'(\d+|[LRUD])', letters)]
width = 0
for l in grid:
    if len(l) > width:
        width = len(l)
for i in range(len(grid)):
    if len(grid[i]) < width:
        grid[i] += [' ']*(width-len(grid[i]))
M = len(grid)
N = len(grid[0])
beg = [0, 0]
dim = 0  # dimensions of the cube
seam = {}  # map each "seam" of the cube to the right coordinate and new direction

for i in range(len(grid)):
    if grid[i][-1] != ' ':
        dim += 1


def face_coord_to_real(i, j, face):
    if face == 1:
        return tuple([i, j + 2*dim])
    elif face == 2:
        return tuple([i + dim, j])
    elif face == 3:
        return tuple([i+dim, j + dim])
    elif face == 4:
        return tuple([i + dim, j + 2*dim])
    elif face == 5:
        return tuple([i + 2*dim, j + 2*dim])
    elif face == 6:
        return tuple([i + 2*dim, j + 3*dim])
    raise Exception('invalid face')


def make_seam_transitions():  # tricky logic
    # map seam to the right coordinate and new direction
    for i in range(dim):
        seam[face_coord_to_real(
            i, -1, 1)] = face_coord_to_real(0, i, 3), [1, 0]  # 1 to 3
        # 3 to 1
        seam[face_coord_to_real(-1, i, 3)
             ] = face_coord_to_real(i, 0, 1), [0, 1]
        # 1 to 6
        seam[face_coord_to_real(i, dim, 1)] = face_coord_to_real(
            dim-1-i, dim-1, 6), [0, -1]
        # 6 to 1
        seam[face_coord_to_real(i, dim, 6)] = face_coord_to_real(
            dim-1-i, dim-1, 1), [0, -1]
        # 2 to 1
        seam[face_coord_to_real(-1, i, 2)] = face_coord_to_real(
            0, dim-1-i, 1), [1, 0]
        # 1 to 2
        seam[face_coord_to_real(-1, i, 1)] = face_coord_to_real(
            0, dim-1-i, 2), [1, 0]
        # 2 to 5
        seam[face_coord_to_real(dim, i, 2)] = face_coord_to_real(
            dim-1, dim-1-i, 5), [-1, 0]
        # 5 to 2
        seam[face_coord_to_real(dim, i, 5)] = face_coord_to_real(
            dim-1, dim-1-i, 2), [-1, 0]
        # 3 to 5
        seam[face_coord_to_real(dim, i, 3)] = face_coord_to_real(
            dim-1-i, 0, 5), [0, 1]
        # 5 to 3
        seam[face_coord_to_real(i, -1, 5)] = face_coord_to_real(
            dim-1, dim-1-i, 3), [-1, 0]
        # 4 to 6
        seam[face_coord_to_real(i, dim, 4)] = face_coord_to_real(
            0, dim-1-i, 6), [1, 0]
        # 6 to 4
        seam[face_coord_to_real(-1, i, 6)] = face_coord_to_real(
            dim-1-i, dim-1, 4), [0, -1]
        # 2 to 6
        seam[face_coord_to_real(i, -1, 2)] = face_coord_to_real(
            dim-1, dim-1-i, 6), [-1, 0]
        # 6 to 2
        seam[face_coord_to_real(dim, i, 6)] = face_coord_to_real(
            dim-1-i, 0, 2), [0, 1]


make_seam_transitions()


def real_to_face_coord(i, j):
    if i < dim and j >= 2*dim:
        return [i, j - 2*dim, 1]
    elif dim <= i < 2*dim and j < dim:
        return [i - dim, j, 2]
    elif dim <= i < 2*dim and j >= dim and j < 2*dim:
        return [i - dim, j - dim, 3]
    elif dim <= i < 2*dim and j >= 2*dim:
        return [i - dim, j - 2*dim, 4]
    elif i >= 2*dim and 3*dim > j >= 2*dim:
        return [i - 2*dim, j - 2*dim, 5]
    elif i >= 2*dim and j >= 3*dim:
        return [i - 2*dim, j - 3*dim, 6]


def nxt2(pos, dir):
    # wrap around the cube
    nxt = [(pos[0]+dir[0]), (pos[1]+dir[1])]
    ndir = dir[:]
    if (nxt[0], nxt[1]) in seam:
        nxt, ndir = seam[(nxt[0], nxt[1])]
    else:
        assert (0 <= nxt[0] < M and 0 <= nxt[1] <
                N and grid[nxt[0]][nxt[1]] != ' ')
    if grid[nxt[0]][nxt[1]] == '#':
        return False, pos, dir
    return True, nxt, ndir


def valid(pos, dir):
    nxt = [(pos[0]+dir[0]) % M, (pos[1]+dir[1]) % N]
    while grid[nxt[0]][nxt[1]] == ' ':
        nxt = [(nxt[0]+dir[0]) % M, (nxt[1]+dir[1]) % N]
    return grid[nxt[0]][nxt[1]] != '#', nxt, dir


def rotate(dir: list[int], c):
    if c == 'L':
        return [-dir[1], dir[0]]
    else:
        return [dir[1], -dir[0]]


def gold_setup():
    # wtf input lol
    # rotate 6 180 degrees right, move down one unit
    # rotate 2 and 3 90 degrees left, move down up one unit
    global grid, M, N
    old_pos = {}  # map new position to old position
    fi = 0
    grid2 = [[' ' for _ in range(dim*4)] for _ in range(dim*3)]
    for i in range(dim-1, -1, -1):
        fj = 0
        for j in range(3*dim-1, 2*dim-1, -1):
            x, y = face_coord_to_real(fi, fj, 6)
            grid2[x][y] = grid[i][j]
            old_pos[(x, y)] = (i, j)
            fj += 1
        fi += 1
    fi = 0
    for j in range(dim):
        fj = 0
        for i in range(4*dim-1, 3*dim-1, -1):
            x, y = face_coord_to_real(fi, fj, 2)
            grid2[x][y] = grid[i][j]
            old_pos[(x, y)] = (i, j)
            fj += 1
        fi += 1
    fi = 0
    for j in range(dim):
        fj = 0
        for i in range(3*dim-1, 2*dim-1, -1):
            x, y = face_coord_to_real(fi, fj, 3)
            grid2[x][y] = grid[i][j]
            old_pos[(x, y)] = (i, j)
            fj += 1
        fi += 1
    fi = 0
    for i in range(dim):
        fj = 0
        for j in range(dim, 2*dim):
            x, y = face_coord_to_real(fi, fj, 1)
            grid2[x][y] = grid[i][j]
            old_pos[(x, y)] = (i, j)
            fj += 1
        fi += 1
    fi = 0
    for i in range(dim, 2*dim):
        fj = 0
        for j in range(dim, 2*dim):
            x, y = face_coord_to_real(fi, fj, 4)
            grid2[x][y] = grid[i][j]
            old_pos[(x, y)] = (i, j)
            fj += 1
        fi += 1
    fi = 0
    for i in range(2*dim, 3*dim):
        fj = 0
        for j in range(dim, 2*dim):
            x, y = face_coord_to_real(fi, fj, 5)
            grid2[x][y] = grid[i][j]
            old_pos[(x, y)] = (i, j)
            fj += 1
        fi += 1
    grid = grid2
    M = len(grid)
    N = len(grid[0])
    return old_pos


for lvl in ['silver', 'gold']:
    check = valid if lvl == 'silver' else nxt2
    if lvl == 'gold':
        old_pos = gold_setup()
    for j in range(len(grid[0])):
        if grid[0][j] == '.':
            beg[1] = j
            break
    pos = beg[:]
    dir = [0, 1]
    for c in cmds:
        if c == 'L' or c == 'R':
            dir = rotate(dir, c)
        else:
            for _ in range(c):
                good, nxt, dir = check(pos, dir)
                if not good:
                    break
                pos = nxt

    if lvl == 'gold':
        _, _, face = real_to_face_coord(pos[0], pos[1])
        pos = old_pos[(pos[0], pos[1])]
        if face in [2, 3]:
            dir = rotate(dir, 'L')
        if face == 6:
            dir = rotate(rotate(dir, 'R'), 'R')
    facing = [[0, 1], [1, 0], [0, -1], [-1, 0]].index(dir)
    # print(pos[0]+1, pos[1]+1, facing)
    print(lvl, (pos[0]+1)*1000 + (pos[1]+1)*4 + facing)
