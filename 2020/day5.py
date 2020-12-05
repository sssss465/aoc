import fileinput

lines = []
for line in fileinput.input():
    l = line.strip()
    lines.append(l)

silver = 0
seats = [[0]*8 for i in range(127)]
for l in lines:
    lo = 0
    hi = 127
    left = 0
    right = 7
    for c in l[:7]:
        mid = (lo+hi)//2
        if c == 'F':
            hi = mid
        else:
            lo = mid+1
    for c in l[7:]:
        mid = (left+right)//2
        if c == 'L':
            right = mid
        else:
            left = mid+1
    # print(lo, hi)
    # print(left, right, l)
    # assert(lo == hi)
    # assert(left == right)
    seats[lo][left] = 1
    silver = max(silver, lo*8+left)
print('silver', silver)
for i in range(len(seats)):
    for j in range(len(seats[0])):
        left = seats[i][j-1] if j > 0 else 1
        right = seats[i][j+1] if j < len(seats[0])-1 else 1
        if left == 1 and right == 1 and seats[i][j] == 0:
            print('gold', i*8+j)
            break
