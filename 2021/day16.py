import fileinput
from typing import List

lines = [l.strip() for l in fileinput.input()]  # type: List[str]

for l in lines:
    pass


def test(a: 'int') -> int | None:
    return 4


def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
    print(b, a, b//a, x, y)
    return gcd, x, y


# https://cp-algorithms.com/algebra/extended-euclid-algorithm.html
# extended finds as + bt = gcd(a,b) and returns gcd(a,b), a, b
print(gcdExtended(11, 26))


class Node:
    def __init__(self, a: int):
        self.v: int = a
        self.left: Node | None = None
        self.right: Node | None = None


n = Node(5)
n.left = Node(10)
# print(gcd(3000, 47))  # type: int
