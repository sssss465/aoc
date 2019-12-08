import fileinput

paths = [line.split(',') for line in fileinput.input()]

patha, pathb = paths[0], paths[1]
beena = set()
dirs = {
    'L': [-1, 0],
    'R': [1, 0],
    'U': [0, 1],
    'D': [0, -1]
}
start = [0, 0]
for cmd in patha:
    dist = int(cmd[1:])
    d = dirs[cmd[0]]
    for i in range(dist):
        start = list(sum(x) for x in zip(start, d))
        beena.add(tuple(start))
start = [0, 0]
res = []
for cmd in pathb:
    dist = int(cmd[1:])
    d = dirs[cmd[0]]
    for i in range(dist):
        start = list(sum(x) for x in zip(start, d))
        if tuple(start) in beena:
            res.append(tuple(start))

res = sorted(res, key=lambda k: abs(k[0]) + abs(k[1]))
print(res)
print(abs(res[0][0]) + abs(res[0][1]))
