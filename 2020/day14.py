import fileinput
import collections
import re
# mask
# 0 0 - 0
# 0 1 - 1
# 1 1 - 1
# 1 0 - 0
# 0 X - 0
# 1 X - 1

# - 0 1
# 0 0 1
# 1 0 1
# ^AB + AB = B

lines = [x for x in fileinput.input()]
memory = collections.defaultdict(int)
mask = ''


def msk(m, n):  # mask, number
    r = 0
    i = len(m)-1
    base = 1
    while i >= 0:
        bit = n % 2
        if m[i] != 'X':
            bit = int(m[i])
        r += base * bit
        base *= 2
        n = n//2
        i -= 1
    return r


for l in lines:
    left, right = l.split('=')
    left = left.strip()
    right = right.strip()
    if left != 'mask':
        index = re.findall("(?<=\[).+?(?=\])", left)[0]
        num = int(right)
        memory[int(index)] = msk(mask, num)
    else:
        mask = right
# print(memory)
print('silver', sum(memory.values()))
