from dataclasses import dataclass
import fileinput
from collections import Counter, defaultdict
from typing import Union, List
import ast
import math

lines = [l.strip() for l in fileinput.input()]
# If any pair is nested inside four pairs, the leftmost such pair explodes.
# If any regular number is 10 or greater, the leftmost such regular number splits.


def build(pair: str) -> List[List[int]]:
    level = 0  # we start at one bc we are gooing to  put both in a list
    res = []
    for c in pair:
        if c == "[":
            level += 1
        elif c == "]":
            level -= 1
        elif c == ",":
            continue
        else:
            res.append([int(c), level])
    return res


# To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.
def explode(pair, level=0) -> bool:
    # print("in explode")
    for i in range(len(pair)):
        if pair[i][1] == 5:
            if i > 0:
                pair[i - 1][0] += pair[i][0]
            if i < len(pair) - 2:
                pair[i + 2][0] += pair[i + 1][0]
            pair[i] = [0, 4]
            pair.pop(i + 1)

            return True
    return False


# To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.
def split(pair) -> bool:
    for i in range(len(pair)):
        if pair[i][0] >= 10:
            ov, ol = pair[i][0], pair[i][1]
            # print(type(ov), type(ol))
            # insert right one first
            pair.pop(i)
            pair.insert(i, [math.ceil(ov / 2), ol + 1])
            pair.insert(i, [ov // 2, ol + 1])

            return True
    return False


def magnitude(pairs) -> List[int]:  # returns last pair
    # 3x left value, 2x right value summed up, do this recursively
    # build by level from increase to decreasing
    st = [pairs[0]]
    for i in range(1, len(pairs)):
        st.append([pairs[i][0], pairs[i][1]])
        while len(st) >= 2 and st[-1][1] == st[-2][1]:
            v, d = st.pop()  # right
            v1, d1 = st.pop()  # left
            st.append([3 * v1 + 2 * v, d - 1])
        # print(st)
    # print(st)
    return st[0]
    return -1  # bad value


def red(pair: List[List[int]]) -> List[List[int]]:
    # print("in red")
    """keep reducing until it is fully reduced"""
    i = 0
    while True:
        i += 1
        if explode(pair):
            # print(f"{'after explode:':15}", pair)
            continue
        elif split(pair):
            # print(f"{'after split:':<15}", pair)
            continue
        break
    return pair


def solve():
    p = build(lines[0])
    # print(p)
    for i in range(1, len(lines)):
        p += build(lines[i])
        # print("pp", p)
        for j in range(len(p)):
            p[j][1] += 1
        p = red(p)
    print(p)
    return magnitude(p)


def solve2():
    res = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                p = build(lines[i]) + build(lines[j])
                for j in range(len(p)):
                    p[j][1] += 1
                res = max(res, magnitude(red(p))[0])
    return res


if __name__ == "__main__":
    print("silver", solve()[0])
    print("gold", solve2())
