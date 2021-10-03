import hashlib
solve = 'iwrupvqb'

answer = 1
while True:
    hash = hashlib.md5((solve + str(answer)).encode('utf-8')).hexdigest()
    if hash[:5] == '00000':
        print(answer)
    if hash[:6] == '000000':
        print(answer)
        break
    answer += 1
