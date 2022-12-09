import fileinput

lines = [line for line in fileinput.input()]


class Rope:
    def __init__(self, l=2):
        self.chain = []
        for _ in range(l):
            self.chain.append([0, 0])
        self.visited = set((0, 0))

    def dist(self, head, tail):
        for dx, dy in [[-1, -1], [1, 1], [-1, 1], [1, -1]]:
            if head[0] + dx == tail[0] and head[1] + dy == tail[1]:
                return 1
        return abs(head[0] - tail[0]) + abs(head[1] - tail[1])

    def move(self, index=0, last=[0, 0]):
        if index == 0:
            self.chain[index][0] += last[0]
            self.chain[index][1] += last[1]
        else:
            if self.chain[index][0] == self.chain[index-1][0] or self.chain[index][1] == self.chain[index-1][1]:
                search = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            else:
                search = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
            for dx, dy in search:
                nx = self.chain[index][0] + dx
                ny = self.chain[index][1] + dy
                if self.dist([nx, ny], self.chain[index-1]) == 1:
                    self.chain[index][0] = nx
                    self.chain[index][1] = ny
                    break
        if index == len(self.chain) - 1:
            self.visited.add(tuple(self.chain[index]))
            return
        if self.dist(self.chain[index], self.chain[index+1]) > 1:
            self.move(index+1, last)

    def __repr__(self):
        return str(self.chain)


for ln in [2, 10]:
    rope = Rope(ln)
    for l in lines:
        dir, amt = l.split(' ')
        amt = int(amt)
        for _ in range(amt):
            match dir:
                case 'U':
                    rope.move(0, [0, 1])
                case 'D':
                    rope.move(0, [0, -1])
                case 'R':
                    rope.move(0, [1, 0])
                case 'L':
                    rope.move(0, [-1, 0])
    print("silver:" if ln == 2 else "gold: ", len(rope.visited))
