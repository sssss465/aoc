import sys
import numpy as np
pic = []
for line in sys.stdin:
    pic = [int(i) for i in list(line.rstrip())]
width = 25
length = 6

assert(len(pic) % (width // length) == 0)

res = [[[0] * width for i in range(length)]
       for j in range(len(pic) // (width*length))]
p = 0
layer = None
min_zero = float('inf')
for l in range(len(pic) // (width*length)):
    zeros = 0
    for i in range(length):
        for j in range(width):
            if pic[p] == 0:
                zeros += 1
            res[l][i][j] = pic[p]
            p += 1
    if zeros < min_zero:
        min_zero = zeros
        print(min_zero)
        layer = l
l = layer
# print(sum([r.count(1) for r in res[l]]) * sum([r.count(2) for r in res[l]]))

res = np.array(res)  # tofix
# x = np.argmax(res != 2, axis=0).flatten()
# print(np.shape(x))

# x = res[x, np.repeat(range(length), len(x) // length),
#         np.repeat(range(width), len(x) // width)]
# print(np.shape(x))
# print(x.reshape((6, 25)))
o = [[0] * width for i in range(length)]

for i in range(length):
    for j in range(width):
        r = 2
        for x in res[:, i, j]:
            if x == 0 or x == 1:
                r = x
                break
        o[i][j] = r
print(np.array(o))
