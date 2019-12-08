import sys
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
print(sum([r.count(1) for r in res[l]]) * sum([r.count(2) for r in res[l]]))
