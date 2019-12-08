#! /usr/bin/env python3

import fileinput
res = 0
for line in fileinput.input():
    res += int(line) // 3 - 2
print(res)
