import functools
import sys
import numpy as np
import copy
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
    moons.append(Moon(*line))

steps = 0
i = 0
start = copy.deepcopy(moons)

moonflag = [False] * 3
res = [0] * 3


def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)


while True:
    # print('step: ', i, moonflag, res)
    # for m in moons:
    #     print(m)
    if i > 0:
        if all(moonflag):
            break
        for j in range(3):
            if res[j] == 0:
                flag = True
                for m in range(len(moons)):
                    if moons[m].pos[j] == start[m].pos[j] and moons[m].vel[j] == 0:
                        continue  # print(moons[m].pos[j], moons[m].vel[j])
                    else:
                        flag = False
                        break
                if flag:
                    moonflag[j] = True
                    res[j] = i
    for m in moons:
        for n in moons:
            if m is not n:
                m.gravity(n)
    for m in moons:
        m.velocity()
    i += 1
print(res)
r = res[0]
for i in range(1, len(res)):
    r = lcm(r, res[i])
print('answer is', r)
