
import itertools
from functools import reduce
from enum import Enum
import fileinput
import operator
from collections import defaultdict


class CardinalDirection(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    @classmethod
    def offsets(cls):
        return list(member.value for member in cls)


def count_trees_in_direction(grid, row, column, direction: tuple):
    drow, dcolumn = direction
    end = False
    extra = 0

    def check(coord):
        nonlocal end, extra
        # hopped off edge
        if coord[0] < 0 or coord[0] >= len(grid) or coord[1] < 0 or coord[1] >= len(grid[0]):
            end = True
            return False
        if grid[coord[0]][coord[1]] >= grid[row][column]:  # hopped to any including edge
            extra = 1
            return False
        return True
    return sum(
        1
        for _ in itertools.takewhile(
            lambda coord: check(coord),
            itertools.chain(
                map(
                    lambda off: (row + drow*off, column + dcolumn*off),
                    itertools.count(1)
                ),
                [(row, column)]
            )
        )
    ) + extra, end


def count_good_trees(grid):
    res = defaultdict(int)
    for row, column, dir in itertools.product(list(range(len(grid))), list(range(len(grid[0]))), CardinalDirection.offsets()):
        if count_trees_in_direction(grid, row, column, dir)[1]:
            res[(row, column)] = 1
    return sum(res.values())


def find_largest_good_forest(grid):
    max_forest_size = 0
    for row, column in itertools.product(range(len(grid)), range(len(grid[0]))):
        trees_in_directions = [
            count_trees_in_direction(grid, row, column, direction)[0]
            for direction in CardinalDirection.offsets()
        ]
        max_forest_size = max(
            max_forest_size, int(reduce(operator.mul, trees_in_directions)))
    return max_forest_size


def main():
    grid = [
        [int(i) for i in list(line.strip())]
        for line in fileinput.input()
    ]
    num_good_trees = count_good_trees(grid)
    max_forest_size = find_largest_good_forest(grid)
    print(num_good_trees)
    print(max_forest_size)


if __name__ == '__main__':
    main()
