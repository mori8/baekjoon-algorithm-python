# gcd - 유클리드 호제법
# 1. 최대공약수를 구하는 함수 gcd(x, y)
# 2. x % y == 0이라면 gcd(x, y) = y
# 3. x % y != 0이라면 gcd(x, x % y)
# 4. x % y == 0이 될 때까지 2~3번을 반복

# lcm
# 최소공배수는 주어진 수인 x, y의 곱에서 x, y의 최대공약수를 나누어 준 것과 같음

import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


x, y = map(int, input().split())

print(math.gcd(x, y))
print(lcm(x, y))
