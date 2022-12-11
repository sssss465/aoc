import fileinput
import re
from dataclasses import dataclass, field
from typing import Type, Callable
import typing

lines = [line.strip() for line in fileinput.input()]

lines = '\n'.join(lines)

lines = lines.split('\n\n')


# @dataclass
class Monkey:
    # items: list[int] = field(default_factory=list)
    # op: 'Callable[[int], int]' = lambda x:  x
    # test: 'Callable[[int], bool]' = lambda x: x % 2 == 0
    # iftrue: int = 0
    # iffalse: int = 0
    # actions: int = 0
    # id: int = 0
    def __init__(self):
        self.items = []
        self.op = lambda x: x
        self.test = lambda x: x % 2 == 0
        self.iftrue = 0
        self.iffalse = 0
        self.actions = 0
        self.id = 0
        self.old = []

    def perform(self, gold=False) -> list[tuple[int]]:
        res = []
        for _, i in enumerate(self.items):
            o = self.op(i) // 3 if not gold else self.op(i) % magic
            res.append((self.iftrue if self.test(o) else self.iffalse, o))
            self.actions += 1
        self.items = []
        return res

    def reset(self):
        self.items = self.old[:]
        self.actions = 0


monkeys = []
magic = 1


def make_lambda(operator, opend):  # need closure for lambda scopes
    if opend == 'old':
        return lambda x: x * x if operator == '*' else lambda x: x + x
    else:
        return lambda x: x * int(opend) if operator == '*' else lambda x: x + int(opend)


def make_mod(n):
    return lambda x: x % n == 0


for i, m in enumerate(lines):
    mm = Monkey()
    mm.id = i
    for i, l in enumerate(m.split('\n')):
        match i:
            case 1:
                mm.items = [int(i)
                            for i in re.search(r'items: (.*)', l).groups()[0].split(',')]
                mm.old = mm.items[:]
            case 2:
                operator, opend = re.search(
                    r'old (.*)', l).groups()[0].split(' ')
                mm.op = make_lambda(operator, opend)
            case 3:
                mm.test = make_mod(int(l.split(' ')[-1]))
                magic *= int(l.split(' ')[-1])
            case 4:
                mm.iftrue = int(l.split(' ')[-1])
            case 5:
                mm.iffalse = int(l.split(' ')[-1])
    monkeys.append(mm)

for r in [20, 10000]:
    for i in range(r):
        for m in monkeys:
            passes = m.perform(r == 10000)
            for k, v in passes:
                monkeys[k].items.append(v)
    ans = sorted(monkeys, key=lambda x: -x.actions)
    print('silver:' if r == 20 else "gold: ",
          ans[0].actions * ans[1].actions)
    for m in monkeys:
        m.reset()
