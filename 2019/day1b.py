#! /usr/bin/env python3

import fileinput
res = 0
for line in fileinput.input():
    temp = 0
    fuel = int(line) // 3 - 2
    while fuel > 0:
        temp += fuel
        fuel = fuel // 3 - 2
    res += temp
print(res)
