import fileinput
from dataclasses import dataclass, field

lines = [line.strip() for line in fileinput.input()]

arr = []
cur = 0
for line in lines:
    if not line:
        arr.append(cur)
        cur = 0
    else:
        cur += int(line)
arr.append(cur)

print(f'🤍 {max(arr):>6}')
print(f'💛 {sum(sorted(arr)[-3:]):>6}')
