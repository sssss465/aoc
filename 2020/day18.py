import fileinput
import operator

lines = list(fileinput.input())
op_map = {'+': operator.add, '-': operator.sub,
          '/': operator.floordiv, '*': operator.mul}
pres = {'+': 1, '-': 1, '*': 1, '/': '1', '(': 0, ')': 0}


def solve():
    rs = 0
    for line in lines:
        ops = []
        vals = []
        for token in line:
            # print(line.strip(), token)
            if token == ' ':
                continue
            if ord('0') <= ord(token) <= ord('9'):
                vals.append(int(token))
            if token == '(':
                ops.append(token)
            if token == ')':
                while ops[-1] != '(':
                    op = ops.pop()
                    # print(vals, ops)
                    t2, t1 = vals.pop(), vals.pop()
                    vals.append(op_map[op](t1, t2))
                ops.pop()
            if token in op_map:
                # while token has greater presidence than operator on top of stack
                while len(ops) and pres[token] <= pres[ops[-1]]:
                    op = ops.pop()
                    # print(vals, ops, op)
                    t2, t1 = vals.pop(), vals.pop()
                    vals.append(op_map[op](t1, t2))
                ops.append(token)
            # print(vals, ops, token)
        while len(ops):  # finish remaining operations
            op = ops.pop()
            t2, t1 = vals.pop(), vals.pop()
            vals.append(op_map[op](t1, t2))
        # assert(len(vals) == 1 and len(ops) == 0)
        rs += vals[-1]
    return rs


print('silver', solve())
pres['+'] = 2
print('gold', solve())
