import math

n = input()
d = {'1': 1, '2': 2, '6': 3, '24': 4, '120': 5, '720': 6}

if n in d:
    print(d[n])
    exit()

n = len(n)-1
i = s = 0

while 1:
    i += 1
    s += math.log10(i)
    if int(s) == n:
        print(i)
        break
