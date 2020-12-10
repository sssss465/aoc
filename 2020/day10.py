import fileinput

lines = []
for line in fileinput.input():
    lines.append(line.strip())
lines = list(map(int, lines))

device = max(lines) + 3
st = sorted(lines + [0] + [device])
one, three = 0, 0
for i in range(1, len(st)):
    if st[i] - st[i-1] == 1:
        one += 1
    elif st[i] - st[i-1] == 3:
        three += 1
    else:
        assert(False)
print('silver', one*three)
s = set(st)
d = {}


def dp(cur):
    if cur == 0:
        return 1
    if cur in d:
        return d[cur]
    res = 0
    for i in range(cur-1, cur-4, -1):
        if i in s:
            res += dp(i)
    d[cur] = res
    return res


print('gold', dp(device))
