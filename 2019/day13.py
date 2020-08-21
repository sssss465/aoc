import os
import time
import fileinput
from functools import reduce
import sys
import collections
symbols = [' ', '█', '░', '_', 'O']
codes = []
for line in fileinput.input():
    line = line.rstrip()
    codes = line.split(',')
codes = [int(a) for a in codes] + [0] * 10000
codes[0] = 2  # play for free
i = 0
base = 0
output = []
print(codes[:2000])
print(codes[1558:1600])

codes[1558+2:1600-2] = [1] * len(codes[1558+2:1600-2])  # cheat code lel


def parse(output):
    os.system('clear')
    print('output len: ', len(output))
    output = [output[i:i+3] for i in range(0, len(output), 3)]
    max_x, max_y = 0, 0
    for x, y, code in output:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    board = [[0]*(max_x+1) for i in range(max_y+1)]
    walls = set()
    bricks = set()
    score = 0
    ball, paddle = None, None
    for x, y, code in output:
        if x == -1 and y == 0:
            score = code
            continue
        board[y][x] = symbols[code]
        if code == 1:
            walls.add((y, x))
        if code == 2:
            bricks.add((y, x))
        if code == 3:
            paddle = (y, x)
        if code == 4:
            ball = (y, x)
    print('SCORE: ', score)
    for r in board:
        print(''.join(r), sep='')


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
        parse(output)
        codes[params[0]] = 0  # input
    elif op[0] == 4:
        assert(len(params) == 1)
        output.append(params[0])
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

parse(output)


class Board:
    def __init__(self, board, bricks, walls, ball, paddle):
        self.board = board
        self.bricks = bricks
        self.walls = walls
        self.ball = ball
        self.vel = (-1, -1)
        self.paddle = paddle
        self.commands = []

    def __repr__(self):
        # os.system('clear')
        self.clear()
        print('bricks left: ', len(self.bricks))
        print(self.ball, self.vel, self.paddle)
        out = ''
        for r in self.board:
            out += ''.join([*r]) + '\n'
        return out

    def clear(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                self.board[r][c] = ' '
                if (r, c) in self.bricks:
                    self.board[r][c] = '░'
                if (r, c) in self.walls:
                    self.board[r][c] = '█'
                if (r, c) == self.ball:
                    self.board[r][c] = 'O'
                if (r, c) == self.paddle:
                    self.board[r][c] = '_'

    def run(self):
        while True:
            print(self)
            future = (self.ball[0] + self.vel[0],
                      self.ball[1] + self.vel[1])
            futurex = (self.ball[0] + self.vel[0],
                       self.ball[1])
            futurey = (self.ball[0],
                       self.ball[1] + self.vel[1])
            if futurex in self.bricks:  # reflect and destroy
                self.bricks.remove(futurex)
                self.vel = (-self.vel[0], self.vel[1])
            elif futurey in self.bricks:
                self.bricks.remove(futurey)
                self.vel = (self.vel[0], -self.vel[1])
            elif future in self.bricks:
                self.bricks.remove(future)
                self.vel = (-self.vel[0], -self.vel[1])
            elif future[0] > len(board[0])-1 or future[0] < 1 or (future[0] > self.paddle[0]-1 and self.vel[0] > 0):
                self.vel = (-self.vel[0], self.vel[1])
            elif future[1] > len(board)-1 or future[1] < 1:
                self.vel = (self.vel[0], -self.vel[1])
            self.ball = (self.ball[0] + self.vel[0],
                         self.ball[1] + self.vel[1])
            self.paddle = (self.paddle[0], self.ball[1])
            # time.sleep(1)  # 15 fps
# b = Board(board, bricks, walls, ball, paddle)
# b.run()
