n = int(input())
dp = [99999 for _ in range(n + 1)]

dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    for j in range(1, i + 1):
        if i < j**2:
            break
        if i == j**2:
            dp[i] = 1
        if i > j**2:
            dp[i] = min(dp[i], dp[i-j**2] + 1)

print(dp[n])
