from functools import reduce
import fileinput
import collections

codes = []
for line in fileinput.input():
    line = line.rstrip()
    codes = line.split(',')
codes = [int(a) for a in codes] + [0]*1000
i = 0
cdir = (0, 1)
where = (0, 0)
been = collections.defaultdict(int)
printed = 0

# print(len(codes))


def right(cdir):
    # (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
    cdir = (cdir[1], -cdir[0])
    return cdir


def left(cdir):
    # (0,1) -> (-1, 0 ) -> (0, -1) -> (1, 0 )
    cdir = (-cdir[1], cdir[0])
    return cdir


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
        if act not in (0, 1):
            raise ValueError('Relative mode not supported')
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
    elif op[0] == 2:
        codes[c] = reduce((lambda x, y: x * y), params)
    elif op[0] == 3:
        codes[c] = been[where]
    elif op[0] == 4:
        assert(len(params) == 1)
        if printed % 2 == 0:
            if params[0] in (0, 1):
                been[where] = params[0]
            else:
                raise ValueError('bad painting value')
        else:
            if params[0] == 0:
                cdir = left(cdir)
            elif params[0] == 1:
                cdir = right(cdir)
            else:
                raise ValueError('bad turn value')
            where = (where[0] + cdir[0], where[1] + cdir[1])
        # print(params[0])
        printed += 1
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
    else:
        raise ValueError('opcode ', op[0], ' is not supported ')
    i = j + 1 if op[0] not in (4, 5, 6) else j

print('part1', len(been))
