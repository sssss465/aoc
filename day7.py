from functools import reduce
import fileinput

out = []
for line in fileinput.input():
    line = line.rstrip()
    out = line.split(',')
out = [int(a) for a in out]
dup = out[:]


class Amplifier:
    def __init__(self, phase, input_sig, codes):
        self.phase = phase
        self.input = input_sig
        self.codes = codes
        self.times = 0
        self.output = None
        self.main()

    def main(self):
        codes = self.codes
        i = 0
        while i < len(codes):
            j = i+1
            op = [int(i) for i in list(reversed(str(codes[i])))]  # 2 0 0 1
            # 2 params, res stored in 3rd.
            if len(op) < 4 and op[0] not in (4, 3):
                op = op + [0] * (4-len(op))
            elif op[0] == 4 and len(op) < 3:
                op = op + [0] * (3 - len(op))
            params = []
            # print('Running operation: ', op, 'on line ', i, codes[i:i+4])
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
            elif op[0] == 2:
                codes[c] = reduce((lambda x, y: x * y), params)
            elif op[0] == 3:
                times = self.times
                if times == 0:
                    codes[c] = self.phase
                elif times == 1:
                    codes[c] = self.input
                else:
                    raise Exception('got more than two codes')
                self.times += 1
            elif op[0] == 4:
                assert(self.output is None and len(params) == 1)
                self.output = params[0]
                # print(params)
                # print(params[0])
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


if __name__ == '__main__':
    res = 0
    answers = {}
    for i in range(44445):
        # for i in range(10431, 10433):
        # for i in range():
        x = [int(j) for j in list(str(i))]
        if len(x) < 5:
            x = [0]*(5 - len(x)) + x
        flag = True
        for j in x:
            if j in [5, 6, 7, 8, 9]:
                flag = False
                break
        if not flag or len(set(x)) != len(x):
            continue
        amp1 = Amplifier(x[0], 0, dup[:])
        assert(amp1.output is not None)
        amp2 = Amplifier(x[1], amp1.output, dup[:])
        assert(amp2.output is not None)
        amp3 = Amplifier(x[2], amp2.output, dup[:])
        assert(amp3.output is not None)
        amp4 = Amplifier(x[3], amp3.output, dup[:])
        assert(amp4.output is not None)
        amp5 = Amplifier(x[4], amp4.output, dup[:])
        assert(amp5.output is not None)
        res = max(res, amp5.output)
        answers[amp5.output] = x[:]
        # print(amp5.output, 'tmp res is ')
    print('final answer is ', res, answers[res])
