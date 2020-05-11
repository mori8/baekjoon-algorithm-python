# 동전 0

c, k = map(int, input().split())
money = [int(input()) for x in range(c)]
cnt = 0

for i in money[::-1]:
    if k >= i:
        cnt += (k // i)
        k %= i

print(cnt)