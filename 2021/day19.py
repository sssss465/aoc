<<<<<<< HEAD
import fileinput
from dataclasses import dataclass, field

lines = [line.strip() for line in fileinput.input()]


@dataclass
class Beacons:
    x: int
    y: int
    z: int


@dataclass
class Scanner():
    beacs: list[Beacons] = field(default_factory=list)


def parse_rules(lines) -> list[Scanner]:
    scanners = []
    sc = Scanner()
    for line in lines:
        if not line or line[:2] == '--':
            if len(sc.beacs) > 0:
                scanners.append(sc)
            sc = Scanner()
            continue
        sc.beacs.append(Beacons(*[int(x) for x in line.split(',')]))
    return scanners


if __name__ == '__main__':
    scanners = parse_rules(lines)
    print(scanners)
||||||| parent of 091da18 (progress)
=======
import fileinput
import dataclasses
from dataclasses import dataclass
from collections import defaultdict

lines = [l.strip() for l in fileinput.input()]

# idea: O(n^2 m^2) where n is the number of scanners m is the number of detected beacons
# slowly add values to the grid bfs style such that each scanner is added if there are 12 or more common beacons

# check all 24 directions
# (1,1,1) (-1,1,1) (1,-1,1) (-1,-1,1)
# (1,1,-1) (1,-1,1) (-1,1,1)

@dataclass
class Big:
    x: float
    y: float
    z: float = 5

    def __add__(self, other):
        return Big(self.x + other.x, self.y + other.y, self.z + other.z)

def test(x: int | float) -> Big:
    """Doc strings are now working!"""
    x += 1
    d = defaultdict(int)
    d[5] = 3
    return Big(x, x, x)
months = {
        10: "october",
        11: "november",
        }
j = test(5) # type: Big
print(j)
print([p for p in zip([1,2,3], [4,5,6,7], strict=True)])


match j.x:
    case 5:
        print(5)
    case 6:
        print(6)
    case _:
        print('none')


beacons = []
cur = []
>>>>>>> 091da18 (progress)
