from functools import reduce
import fileinput

codes = []
for line in fileinput.input():
    line = line.rstrip()
    codes = line.split(',')
codes = [int(a) for a in codes]

i = 0
while i < len(codes):
    j = i+1
    op = [int(i) for i in list(reversed(str(codes[i])))]  # 2 0 0 1
    if len(op) < 4 and op[0] not in (3, 4):
        op = op + [0] * (4-len(op))
    elif op[0] == 4 and len(op) < 3:
        op = op + [0] * (3 - len(op))
    params = []
    # print('Running operation: ', op, 'on line ', i, codes[i:i+3])
    if op[0] == 9:  # 99 case
        break
    for k in range(2, len(op)):
        act = op[k]
        if act == 0:  # position mode
            params.append(codes[codes[j]])
        else:
            params.append(codes[j])
        j += 1
    # now we have to be in position mode after finding results
    c = codes[j]  # we write to the last pointed position
    if op[0] == 1:
        # print('params are', params, 'putting in ', c)
        codes[c] = sum(params)
    if op[0] == 2:
        codes[c] = reduce((lambda x, y: x * y), params)
    if op[0] == 3:
        codes[c] = 1  # input
    if op[0] == 4:
        assert(len(params) == 1)
        print(params[0])
    i = j + 1 if op[0] != 4 else j
    # print(codes)
# print(codes[0])
