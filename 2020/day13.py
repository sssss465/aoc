from functools import reduce
import fileinput

lines = [x for x in fileinput.input()]

value = int(lines[0])
buses = list(map(int, filter(lambda v: v != 'x', lines[1].split(','))))

waits = [(b, b - (value % b)) for b in buses]
part1 = min(waits, key=lambda k: k[1])
print(value, waits, part1)
print("silver:", part1[0]*part1[1])

# Part2: Chinese Remainder theorum
# a mod 13 = 0
# a mod 41 = 0
# a mod 37 = 0
# and find min a

offsets = [int(n)-i for i, n in enumerate(
    lines[1].split(',')) if n != 'x']  # (offset, bus)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


print("gold:", chinese_remainder(buses, offsets))
