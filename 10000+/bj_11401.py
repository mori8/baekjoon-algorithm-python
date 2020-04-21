# 페르마의 소정리
# 임의의 소수 p와 서로소인 한 수의 p−1승을 p로 나눈 나머지는 무조건 1
# p가 소수면 (1/n)%p = a^(p-2)%p
# 분할정복으로 제곱 계산해야 하는데 pow로 같은 성능 연산 가능하길래 pow 씀
# 분할정복으로 푸는 방법도 공부해야 함


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