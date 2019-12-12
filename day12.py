import sys
import numpy as np

moons = []


class Moon:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.vel = [0, 0, 0]

    def __str__(self):
        return f'position: {self.pos}, velocity: {self.vel}'

    def gravity(self, other):
        for i in range(len(other.pos)):
            if other.pos[i] > self.pos[i]:
                self.vel[i] += 1
            elif other.pos[i] < self.pos[i]:
                self.vel[i] -= 1

    def velocity(self):
        self.pos = [a+b for a, b in zip(self.pos, self.vel)]

    def energy(self):
        return sum((abs(a) for a in self.pos)) * sum((abs(a) for a in self.vel))


for line in sys.stdin:
    line = line.rstrip('>\n').lstrip('<').split(',')
    line = [int(l.split('=')[1]) for l in line]
    print(line)
    moons.append(Moon(*line))

steps = 1
for i in range(0, steps+1):
    print('step: ', i)
    for m in moons:
        print(m)
    if i == steps:
        print(sum([m.energy() for m in moons]))

    for m in moons:
        for n in moons:
            m.gravity(n)
    for m in moons:
        m.velocity()
