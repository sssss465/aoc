import fileinput

paths = []
for line in fileinput.input():
    s = line.split(',')
    paths.append(s)

patha, pathb = paths[0], paths[1]
beena = {}

dirs = {
    'L': [-1, 0],
    'R': [1, 0],
    'U': [0, 1],
    'D': [0, -1]
}

start = [0, 0]

steps = 0
for cmd in patha:
    d = cmd[0]
    dist = int(cmd[1:])
    d = dirs[d]
    for i in range(dist):
        start = list(sum(x) for x in zip(start, d))
        steps += 1
        beena[tuple(start)] = beena.get(tuple(start), steps)

start = [0, 0]
res = []
steps = 0
for cmd in pathb:
    d = cmd[0]
    dist = int(cmd[1:])
    d = dirs[d]
    for i in range(dist):

        start = list(sum(x) for x in zip(start, d))
        steps += 1
        if tuple(start) in beena:
            print(tuple(start))
            res.append(beena[tuple(start)] + steps)

res = sorted(res)
print(res)
# print(abs(res[1][0]) + abs(res[1][1]))
