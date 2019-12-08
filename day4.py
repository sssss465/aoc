import fileinput
zz = 156218-652527
res = 0
# 4b
for i in range(156218, 652527+1):
    kk = str(i)
    if (kk == ''.join(sorted(kk))):
        flag = False  # group of 2
        flag2 = True  # no bigger group than 2
        i = 0
        while (i < len(kk)):
            j = i
            while (j < len(kk) and kk[i] == kk[j]):
                j += 1
            temp = j - i
            if (temp == 2):
                flag = True
            if temp > 2:
                flag2 = False
            i = j
        if (flag):
            res += 1

print(res)
