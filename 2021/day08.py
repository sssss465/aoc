import fileinput

lines = [l.strip() for l in fileinput.input()]

segmap = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
segdisp = {
    0: (0, 1, 2, 4, 5, 6),
    1: (2, 5),
    2: (0, 2, 3, 4, 6),
    3: (0, 2, 3, 5, 6),
    4: (1, 2, 3, 5),
    5: (0, 1, 3, 5, 6),
    6: (0, 1, 3, 4, 5, 6),
    7: (0, 2, 5),
    8: (0, 1, 2, 3, 4, 5, 6),
    9: (0, 1, 2, 3, 5, 6),
}
dispseg = {v: k for k, v in segdisp.items()}

silver = 0
gold = 0


def permutations(arr, i=0):
    if i == len(arr):
        yield arr[:]
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            yield from permutations(arr, i + 1)
            arr[i], arr[j] = arr[j], arr[i]


checks = [p for p in permutations([i for i in range(7)])]
# print(checks)


def decode(signals, out):
    def codetonumber(code, dec):
        return tuple(sorted(dec[ord(l) - ord("a")] for l in code))

    # print(codetonumber("cdfbe", [3, 4, 0, 5, 6, 1, 2]), dispseg)
    r = []
    for c in checks:
        if all(codetonumber(s, c) in dispseg for s in signals):
            r = c
            break
    assert len(r) == 7
    res = []
    for o in out:
        res.append(dispseg[codetonumber(o, r)])
    # print(res)

    return int("".join(str(i) for i in res))


for l in lines:
    signals, out = l.split("|")
    signals = signals.strip().split()
    out = out.strip().split()
    easys = list(map(lambda i: segmap[i], [1, 4, 7, 8]))
    for o in out:
        if len(o) in easys:
            silver += 1
    gold += decode(signals, out)


print("silver: ", silver)
print("gold", gold)
