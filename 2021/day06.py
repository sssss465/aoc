import fileinput
from os import X_OK

lines = [l.strip() for l in fileinput.input()]
fishes = list(map(int, lines[0].split(",")))
days = 11
res = 0

# for f in fishes:
#     off = days % (int(f) + 1)
#     print(f, off)
#     res += 2 ** (days // 7) + (1 if off == 0 else 0)


def naive(days, fishes):
    for d in range(days):
        new_fishes = []
        # print(fishes)
        for f in range(len(fishes)):
            if fishes[f] == 0:
                new_fishes.append(8)
            fishes[f] = (fishes[f] - 1) % 7 if fishes[f] < 7 else fishes[f] - 1
        fishes += new_fishes
    return len(fishes)


# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# 6 8
# 5 7
# 4 6
# 3 5
# 2 4
# 1 3
# 0 2 8
# 6 1 7
# 5 0 6
# 4 6 5 8

cache = {}


def dfs(days, n):
    print(days, n)
    if (days, n) in cache:
        return cache[(days, n)]
    if days - n <= 0:
        return 1
    cache[(days, n)] = dfs(days - n, 7) + dfs(days - n, 9)
    return cache[(days, n)]


def fast(days, fishes):
    res = sum(dfs(days, f) for f in fishes)
    return res


print("silver", naive(80, fishes[:]))
print("gold", fast(256, fishes[:]))
# print(cache)

# for i in range(days):
