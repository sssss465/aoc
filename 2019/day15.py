from functools import reduce
import fileinput

codes = []
for line in fileinput.input():
    line = line.rstrip()
    codes = line.split(',')
codes = [int(a) for a in codes] + [0] * 10000

i = 0
base = 0
output = []
dirs = [1, 2, 3, 4]
opposite = {1: 2, 2: 1, 3: 4, 4: 3}

while i < len(codes):
    j = i+1
    op = [int(i) for i in list(reversed(str(codes[i])))]  # 2 0 0 1
    if len(op) < 4 and op[0] not in (9, 4, 3):  # 2 params, res stored in 3rd.
        op = op + [0] * (4-len(op))
    elif op[0] == 9 or op[0] in (4, 3) and len(op) < 3:
        op = op + [0] * (3 - len(op))
    params = []
    if op[0] == 9 and op[1] == 9:  # 99 case
        break
    for k in range(2, len(op)):
        act = op[k]
        if act == 2:  # relative mode
            if op[0] == 3 or (op[0] in (1, 2, 7, 8) and len(params) >= 2):
                params.append(base + codes[j])  # special write case
            else:
                params.append(codes[base + codes[j]])
        elif act == 0:  # position mode
            if op[0] == 3:
                params.append(codes[j])
            else:
                params.append(codes[codes[j]])
        elif act == 1:  # immediate mode
            params.append(codes[j])
        j += 1
    # print('Running op: ', op, 'on line ', i, codes[i:i+5], params, base)
    # now we have to be in position mode after finding results
    c = codes[j]  # we write to the last pointed position
    # update written position to relative mode if it ends with 2
    if op[-1] == 2 and op[0] not in (3, 4, 5, 6, 9) and len(op) == 5:
        c = params.pop()
        j -= 1

    if op[0] == 1:
        # print('params are', params, 'putting in ', c)
        codes[c] = sum(params)
    elif op[0] == 2:
        codes[c] = reduce((lambda x, y: x * y), params)
    elif op[0] == 3:
        assert(len(params) == 1)
        print('input', params)
        codes[params[0]] = 2  # input
    elif op[0] == 4:
        assert(len(params) == 1)
        # output.append(params[0])
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
        assert(len(params) == 1)
        base += params[0]
    else:
        raise ValueError('opcode ', op[0], ' is not supported ')
    i = j + 1 if op[0] not in (3, 4, 5, 6, 9) else j
print('output: ', output)
