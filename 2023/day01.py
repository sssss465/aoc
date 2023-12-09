import fileinput
from dataclasses import dataclass, field
import re

lines = [line.strip() for line in fileinput.input()]

arr = []
res = 0
res2 = 0 
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in lines:
    matches = re.findall(r'(\d+)', line)
   # print(matches,line)
    s = ''.join(matches)
    if s:
        res += int(s[0] + s[-1])

    matches2 = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line) # thanks for mentioning overlapping cases xD
    for i in range(len(matches2)):
        if not matches2[i].isdigit():
            matches2[i] = str(words.index(matches2[i])+1)
    s2 = ''.join(matches2)
    res2 += int(s2[0] + s2[-1])

print(f'🤍 {res}')
print(f'💛 {res2}')
# print(f'💛 {sum(sorted(arr)[-3:]):>6}')
