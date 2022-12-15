import fileinput
from functools import cmp_to_key
lines = [line.strip() for line in fileinput.input()]
lines = '\n'.join(lines).split('\n\n')
res = 0


def parse(s) -> list[int | list]:
    return eval(s)


def comp(l1, l2) -> bool | str:
    for i in range(min(len(l1), len(l2))):
        if isinstance(l1[i], list) or isinstance(l2[i], list):
            l, r = l1[i] if not isinstance(l1[i], int) else [l1[i]], l2[i] if not isinstance(
                l2[i], int) else [l2[i]]
            r = comp(l, r)
            if r != 'c':
                return r
        elif l1[i] != l2[i]:
            return l1[i] < l2[i]
    if len(l1) == len(l2):
        return 'c'
    return len(l1) < len(l2)


def make_comparator(less_than):
    def compare(a, b):
        if less_than(a, b):
            return -1
        elif less_than(b, a):
            return 1
        else:
            return 0
    return compare


parsed = []
for i, l in enumerate(lines, 1):
    t, d = l.split('\n')
    l1, l2 = parse(t), parse(d)
    parsed.extend([l1, l2])
    r = comp(l1, l2)
    if r:
        res += i
print('silver', res)
diva, divb = [[2]], [[6]]
parsed.extend([diva, divb])
parsed.sort(key=cmp_to_key(make_comparator(comp)))
print('gold', (parsed.index(diva) + 1) * (parsed.index(divb) + 1))
