import fileinput

lines = []
for l in fileinput.input():
    lines.append(list(l.strip()))


def update(board):
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0],
            [-1, -1], [-1, 1], [1, -1], [1, 1]]
    empty = []
    fill = []
    occupied = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'L':
                good = True
                for x, y in dirs:
                    if i+x >= 0 and i+x < len(board) and j+y >= 0 and j+y < len(board[0]):
                        if board[i+x][j+y] == '#':
                            good = False
                            break
                if good:
                    fill.append([i, j])
            elif board[i][j] == '#':
                occupied += 1
                cnt = 0
                for x, y in dirs:
                    if i+x >= 0 and i+x < len(board) and j+y >= 0 and j+y < len(board[0]):
                        if board[i+x][j+y] == '#':
                            cnt += 1
                if cnt >= 4:
                    empty.append([i, j])
    for k, v in empty:
        board[k][v] = 'L'
    for k, v in fill:
        board[k][v] = '#'
    return board, len(empty)+len(fill), occupied


def update_gold(board):
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0],
            [-1, -1], [-1, 1], [1, -1], [1, 1]]
    empty = []
    fill = []
    occupied = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'L':
                good = True
                for x, y in dirs:
                    curi = i+x
                    curj = j+y
                    while curi >= 0 and curi < len(board) and curj >= 0 and curj < len(board[0]):
                        if board[curi][curj] == '#':
                            good = False
                            break
                        if board[curi][curj] == 'L':
                            break
                        curi += x
                        curj += y
                if good:
                    fill.append([i, j])
            elif board[i][j] == '#':
                occupied += 1
                cnt = 0
                for x, y in dirs:
                    curi = i+x
                    curj = j+y
                    while curi >= 0 and curi < len(board) and curj >= 0 and curj < len(board[0]):
                        if board[curi][curj] == '#':
                            cnt += 1
                            break
                        if board[curi][curj] == 'L':
                            break
                        curi += x
                        curj += y
                if cnt >= 5:
                    empty.append([i, j])
    for k, v in empty:
        board[k][v] = 'L'
    for k, v in fill:
        board[k][v] = '#'
    return board, len(empty)+len(fill), occupied


board, changes, occupied = update([l[:] for l in lines])
while changes:
    board, changes, occupied = update(board)
print('silver', occupied)
board, changes, occupied = update_gold([l[:] for l in lines])
while changes:
    board, changes, occupied = update_gold(board)
print('gold', occupied)
