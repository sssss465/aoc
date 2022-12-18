import fileinput
from math import gcd
from collections import defaultdict
from memory_profiler import profile
lines = [l.strip() for l in fileinput.input()]
WIDTH = 7  # width of chamber

shapes = []
maxy = -1
i = 0
board = {}
moves = lines[0]
cycled = {}


class Shape():
    def __init__(self, miny=0):
        self.tiles = []
        self.miny = miny

    def fall(self):
        sim = [(x, y - 1) for x, y in self.tiles]
        if any(board.get(t) for t in sim) or any(t[1] < 0 for t in sim):
            return []
        return sim

    def move(self, dx):
        sim = [(x + dx, y) for x, y in self.tiles]
        if any(board.get(t) for t in sim) or any(t[0] < 0 or t[0] >= WIDTH for t in sim):
            return []
        return sim

    def sim(self, round):
        global i
        while True:
            if row := self.move(-1 if moves[i] == '<' else 1):
                self.tiles = row
            i = (i + 1) % len(moves)
            if row := self.fall():
                self.tiles = row
            else:
                break
        self.freeze(round)
        return self.tiles

    def freeze(self, round):
        for tile in self.tiles:
            board[tuple(tile)] = round+1


class Hori(Shape):
    def __init__(self, miny, kind):
        super().__init__(miny)
        miny += 3
        self.kind = [[(2, miny), (3, miny), (4, miny), (5, miny)],
                     [(3, miny), (2, miny+1), (3, miny+1),
                      (4, miny+1), (3, miny+2)],
                     [(2, miny), (3, miny), (4, miny),
                      (4, miny+1), (4, miny+2)],
                     [(2, miny), (2, miny+1), (2, miny+2), (2, miny+3)],
                     [(2, miny), (3, miny), (2, miny+1), (3, miny+1)]]
        self.tiles = self.kind[kind]


def main():
    global shapes, maxy
    cycled = defaultdict(list)
    gold = 1000000000000
    for round in range(3000):
        r = round % 5
        s = Hori(maxy+1, r)
        if round == 2022:
            print('silver', maxy+1)
        cycled[(r, i)].append((round, maxy+1))
        placed = s.sim(round)
        for t in s.tiles:
            maxy = max(maxy, t[1])
        # if round % 1000:
        #     for x, y in list(board):
        #         if board[(x, y)] < round - 100:
        #             del board[(x, y)]

    l = {}  # cycle increase
    l2 = {}  # cycle duration
    kk = None
    for k, v in cycled.items():
        if len(v) > 1:
            l[k] = (v[-1][1] - v[-2][1])
            l2[k] = (v[-1][0] - v[-2][0])
            # check key exists in cycle
            # basically if x - x0 is divisible by cycle length
            if (gold - v[0][0]) % l2[k] == 0:
                kk = k
        else:
            l[k] = v[-1][1]
    if not kk:
        print('no cycle')
        exit()
    k = kk
    # rise over run
    m = l[k] / l2[k]
    b = cycled[k][0][1] - m * cycled[k][0][0]
    print('gold', m*gold+b)


if __name__ == '__main__':
    main()
