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
