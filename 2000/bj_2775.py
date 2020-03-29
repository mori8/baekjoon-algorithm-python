# 백준 2775번 부녀회장이 될테야
# 아이디어 : 이건 조합이다


def combination(n, k):
    numerator = 1
    denominator = 1
    k = min(n-k, k)
    for i in range(1, k+1):
        denominator *= i
        numerator *= n+1-i
    return numerator/denominator


count = int(input())

for i in range(count):
    a = int(input())
    b = int(input())
    if b == 1:
        print(1)
    else:
        print(int(combination(a + b, a + 1)))