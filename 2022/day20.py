import fileinput
from collections import Counter

lines = [l.strip() for l in fileinput.input()]
decrypt = 811589153
moves = []
orig = []
start = ()
for ind, l in enumerate(lines):
    if int(l) == 0:
        start = (0, ind)
    moves.append((int(l), ind))


def mix(moves, arr):
    for ind, m in enumerate(moves):
        i = m[0]
        cur = arr.index(m)
        while i:
            if i > 0:
                nxt = (cur+1) % len(arr)
                arr[cur], arr[nxt] = arr[nxt], arr[cur]
                cur = nxt
                i -= 1
            elif i < 0:
                nxt = (cur-1) % len(arr)
                arr[cur], arr[nxt] = arr[nxt], arr[cur]
                cur = nxt
                i += 1
    return arr


arr = mix(moves, moves[:])
# print(arr)
off = [1000, 2000, 3000]
# not 5548
zero = arr.index(start)
coord = [arr[(zero+o) % len(arr)][0] for o in off]
print('silver', sum(coord))
# gold
start = ()
for i in range(len(moves)):
    if moves[i][0] == 0:
        start = (0, i)
    orig.append(moves[i][0] * decrypt)
    moves[i] = (((moves[i][0])*decrypt) %
                (len(moves) - 1), i)  # important !!! mod n - 1
arr = moves[:]
for _ in range(10):
    mix(moves, arr)
zero = arr.index(start)
coord = [orig[arr[(zero+o) % len(arr)][1]] for o in off]
print('gold', sum(coord))
