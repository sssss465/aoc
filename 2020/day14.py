import fileinput
import collections
import re
from functools import reduce

lines = [x for x in fileinput.input()]
memory = collections.defaultdict(int)
mask = ''
memory2 = collections.defaultdict()


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


def msk2(memory2, m, index, num, location2s):  # part 2
    #n is index
    bld = f'{index:036b}'
    # print(m, bld)
    location = ''.join(
        (c2 if c1 == '0' else c1 for c1, c2 in zip(m, bld)))

    def find(location):
        try:
            first = location.index('X')
            find(location[0:first] + '1' + location[first+1:])
            find(location[0:first] + '0' + location[first+1:])
        except:
            memory2[int(location, 2)] = num
    find(location)


location2s = []
for l in lines:
    left, right = l.split('=')
    left = left.strip()
    right = right.strip()
    if left != 'mask':
        index = re.findall("(?<=\[).+?(?=\])", left)[0]
        num = int(right)
        memory[int(index)] = msk(mask, num)
        msk2(memory2, mask, int(index), num, location2s)
    else:
        mask = right
print(len(memory2))
print('silver', sum(memory.values()))
print('gold', reduce(lambda x, y: x + y, memory2.values(), 0))
