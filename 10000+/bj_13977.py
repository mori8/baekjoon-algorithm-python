import sys

fac = [0, ] * 4000001
fac[0] = fac[1] = 1

t = int(input())
p = 1000000007

for i in range(2, 4000001):
    fac[i] = fac[i-1] * i
    fac[i] %= p

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    a = fac[n]
    b = fac[k] * fac[n-k] % p
    print(a * pow(b, p-2, p) % p)
