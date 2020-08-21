import fileinput

codes = []
for line in fileinput.input():
    line = line.rstrip()
    codes = line.split(',')
codes = [int(a) for a in codes]

dup = codes[:]

for noun in range(0, 100):
    for verb in range(0, 100):
        codes[1] = noun
        codes[2] = verb

        for i in range(0, len(codes), 4):
            op, a, b, c = codes[i], codes[i+1], codes[i+2], codes[i+3]
            if op == 99:
                break
            if op == 1:
                codes[c] = codes[a]+codes[b]
            if op == 2:
                codes[c] = codes[a]*codes[b]
        if codes[0] == 19690720:
            print("answer is ", 100 * noun + verb)
        codes = dup[:]
