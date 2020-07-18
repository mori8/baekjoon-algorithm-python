n = int(input())
t = [0 for _ in range(n)]
p = [0 for _ in range(n)]
dp = [0 for _ in range(n)]
maximum = 0

for i in range(n):
    t[i], p[i] = map(int, input().split())


def solve():
    global maximum
    if t[n-1] == 1:
        dp[n-1] = p[n-1]
    for i in range(n-2, -1, -1):
        if (i + t[i]) == n:
            dp[i] = max([p[i], dp[i+1]])
        elif (i + t[i]) < n:
            dp[i] = max([p[i] + dp[i + t[i]], dp[i+1]])
        elif (i + t[i]) > n:
            dp[i] = dp[i+1]

    print(dp[0])

solve()
