def fac(n):
    ret = 1
    while n > 1:
        ret *= n
        ret %= p
        n -= 1
    return ret


p = 1000000007
n, k = map(int, input().split())

a = fac(n)
b = fac(k) * fac(n - k) % p
ans = a * pow(b, p-2, p) % p

print(ans)