import sys
import collections

symbols = collections.defaultdict(empty=' ',
                                  brick='░',
                                  wall='█',
                                  ball='O',
                                  paddle='_')
print(symbols)

for line in sys.stdin:
    print(line)
