# 좀 특이한 에라토스테네스의 체

n, k = map(int, input().split())
count = 0

primeList = [True] * (n + 1)
primeList[0] = primeList[1] = False

for i in range(2, n+1):
    if primeList[i]:
        j = 0
        for j in range(i, n+1, i):
            if primeList[j]:
                primeList[j] = False
                count += 1
            if count == k:
                print(j)
                break
