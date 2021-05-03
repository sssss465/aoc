import fileinput
from collections import Counter

pairs = []
for line in fileinput.input():
    line = line.rstrip().split(':')
    line[1] = line[1].strip()
    pairs.append(line)
part1 = 0
part2 = 0
for line in pairs:
    cnt, letter = line[0].split(' ')
    lo, hi = [int(i) for i in cnt.split('-')]
    c = Counter(line[1])
    if c[letter] >= lo and c[letter] <= hi:
        part1 += 1
    if line[1][lo-1] != line[1][hi-1] and (line[1][lo-1] == letter or line[1][hi-1] == letter):
        part2 += 1
print('part1:', part1)
print('part2:', part2)
