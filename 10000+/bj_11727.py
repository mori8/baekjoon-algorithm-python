# 백준 11727번 2xN 타일링 2

import sys
sys.setrecursionlimit(10000)

cache = [0] * 1001


def dp(x):
    if x == 1:
        return 1
    if x == 2:
        return 3
    if cache[x] != 0:
        return cache[x]
    cache[x] = dp(x-1) + 2*dp(x-2)
    return cache[x] % 10007


n = int(input())
print(dp(n))
