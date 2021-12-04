import fileinput
from typing import List

lines = [*map(lambda l: l.strip(), fileinput.input())]


class Board:
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.dup = [b[:] for b in board]
        self.mp = {}
        self.marked = []
        self.last = None
        self.fill_map()

    def fill_map(self):
        for r, row in enumerate(self.board):
            for c, v in enumerate(row):
                self.mp[v] = (r, c)

    def __bool__(self):
        return self.bingo()

    def __repr__(self):
        if self.last is not None:
            # print(self.marked)
            return f"{self.last*sum(self.mp.keys()), self.last , self.mp.keys()}"

    def set(self, v: int):
        if v in self.mp:
            loc = self.mp[v]
            self.board[loc[0]][loc[1]] = "x"
            del self.mp[v]
            self.last = v
            self.marked.append(v)

    def bingo(self):
        for r in self.board:
            if r == ["x"] * len(r):
                return True
        for c in zip(*self.board):
            if list(c) == ["x"] * len(c):
                return True
        return False

    def reset(self):
        self.board = [b[:] for b in self.dup]
        self.mp = {}
        self.marked = []
        self.last = None
        self.fill_map()


balls = [int(l) for l in lines[0].split(",")]
balls2 = balls[:]
boards = []
i = 1
while i < len(lines):
    if lines[i] == "":
        i += 1
        continue
    board = []
    while i < len(lines) and lines[i] != "":
        board.append(list(map(int, lines[i].split())))
        i += 1
    boards.append(Board(board))

while not any(boards):
    ball = balls.pop(0)
    for b in boards:
        b.set(ball)
        if b:
            print("silver:", b)
for b in boards:
    b.reset()
solves = 0
last = None
done = set()
while not all(boards):
    ball = balls2.pop(0)
    for b in boards:
        b.set(ball)
        if b and b not in done:
            last = b
            done.add(b)
print("gold", last)
