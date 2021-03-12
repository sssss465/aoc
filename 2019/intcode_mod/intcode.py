from dataclasses import dataclass
from functools import reduce
import fileinput
from typing import List, Generator
import copy


@dataclass
class Intcode:
    """intcode machine"""
    codes: List[int]
    inputs: List[int]
    i: int = 0
    completed: bool = False
    base: int = 0
    debug: bool = False

    def __init__(self, inputs=[], codes=[], debug=False):
        self.codes = codes
        self.debug = debug
        self.inputs = iter(inputs)

    def copy(self):
        return copy.deepcopy(self)

    def read(self):
        codes = []
        for line in fileinput.input():
            line = line.rstrip()
            codes = line.split(',')
        self.codes = [int(a) for a in codes] + [0] * 10000

    def __repr__(self):
        return f'Intcode: {inputs} , i: {i}'

    def run(self):
        """ Runs the machine via generators

        Args:
            None

        Returns:
            Generator[List]
        """
        i = 0
        codes = self.codes
        base = 0
        while i < len(self.codes):
            j = i+1
            op = [int(i) for i in list(reversed(str(codes[i])))]  # 2 0 0 1
            # 2 params, res stored in 3rd.
            if len(op) < 4 and op[0] not in (9, 4, 3):
                op = op + [0] * (4-len(op))
            elif op[0] == 9 or op[0] in (4, 3) and len(op) < 3:
                op = op + [0] * (3 - len(op))
            params = []
            if op[0] == 9 and op[1] == 9:  # 99 case
                return self.codes  # stop iteration
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
            if self.debug:
                print('Running op: ', op, 'on line ',
                      i, params, codes[i:i+5], f"base: {base}")
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
                try:
                    codes[params[0]] = next(self.inputs)  # input
                except:
                    raise Exception('ran out of inputs to read')
            elif op[0] == 4:
                assert(len(params) == 1)
                # output.append(params[0])
                print('----INTCODE OUTPUT----:', params[0])
            elif op[0] == 5:
                assert(len(params) == 2)
                if params[0] != 0:
                    i = params[1]
                    yield self.codes
                    continue
            elif op[0] == 6:
                assert(len(params) == 2)
                if params[0] == 0:
                    i = params[1]
                    yield self.codes
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
            yield self.codes


# test on day5
if __name__ == '__main__':
    machine = Intcode([2]*100, debug=False)
    res = []
    its = 0
    for res in machine.run():
        # print(its := its+1)
        pass
    # it = machine.run()
    # print(next(it))
    # print(next(it))
