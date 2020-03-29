# 에라토스테네스의 체

m, n = map(int, input().split())

primeList = [True] * 1000001

primeList[0] = primeList[1] = False

for i in range(2, 1000):
    if primeList[i]:
        j = 0
        for j in range(i*2, 1000000, i):
            primeList[j] = False

for i in range(m, n+1):
    if primeList[i]:
        print(i)