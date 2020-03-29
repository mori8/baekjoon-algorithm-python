# 백준 2292번 벌집
# 아이디어 : 이것은 계차수열이다

n = int(input())
i = 1

while n > 1 + 3 * i * (i - 1):
    i += 1

print(i)