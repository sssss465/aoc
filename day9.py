from functools import reduce
import fileinput

codes = []
for line in fileinput.input():
    line = line.rstrip()
    codes = line.split(',')
codes = [int(a) for a in codes] + [0] * 10000

# Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
# Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
# Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
# Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.

i = 0
while i < len(codes):
    j = i+1
    op = [int(i) for i in list(reversed(str(codes[i])))]  # 2 0 0 1
    if len(op) < 4 and op[0] not in (4, 3):  # 2 params, res stored in 3rd.
        op = op + [0] * (4-len(op))
    elif op[0] == 4 and len(op) < 3:
        op = op + [0] * (3 - len(op))
    params = []
    # print('Running operation: ', op, 'on line ', i, codes[i:i+4])
    if op[0] == 9 and op[1] == 9:  # 99 case
        break
    for k in range(2, len(op)):
        act = op[k]
        if act == 2:  # relative mode
            pass
        elif act == 0:  # position mode
            params.append(codes[codes[j]])
        else:
            params.append(codes[j])
        j += 1
    # now we have to be in position mode after finding results
    c = codes[j]  # we write to the last pointed position
    if op[0] == 1:
        # print('params are', params, 'putting in ', c)
        codes[c] = sum(params)
    elif op[0] == 2:
        codes[c] = reduce((lambda x, y: x * y), params)
    elif op[0] == 3:
        codes[c] = 5  # input
    elif op[0] == 4:
        assert(len(params) == 1)
        print(params[0])
    elif op[0] == 5:
        assert(len(params) == 2)
        if params[0] != 0:
            i = params[1]
            continue
    elif op[0] == 6:
        assert(len(params) == 2)
        if params[0] == 0:
            i = params[1]
            continue
    elif op[0] == 7:
        assert(len(params) == 2)
        if params[0] < params[1]:
            codes[c] = 1
        else:
            codes[c] = 0
    elif op[0] == 8:
        assert(len(params) == 2)
        if params[0] == params[1]:
            codes[c] = 1
        else:
            codes[c] = 0
    elif op[0] == 9:
        pass
    else:
        raise ValueError('opcode ', op[0], ' is not supported ')
    i = j + 1 if op[0] not in (4, 5, 6) else j
