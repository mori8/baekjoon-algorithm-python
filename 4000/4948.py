import sys

primeList = [True] * 246913
primeList[0] = primeList[1] = False

for i in range(2, 497):
    if primeList[i]:
        j = 0
        for j in range(i*2, 246913, i):
            primeList[j] = False

for line in sys.stdin:
    n = int(line.rstrip())
    count = 0
    if n == 0:
        break
    for x in range(n+1, 2*n+1):
        if primeList[x]:
            count += 1
    print(count)
