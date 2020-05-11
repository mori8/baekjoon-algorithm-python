# 1로 만들기

dp = [0, 0, 1, 1]


def makeOne(n):
    for i in range(4, n+1):
        if i % 3 == 0 and i % 2 == 0:
            dp.append(min(dp[i//3]+1, dp[i//2]+1, dp[i-1]+1))
        elif i % 3 == 0 and i % 2 != 0:
            dp.append(min(dp[i//3]+1, dp[i-1]+1))
        elif i % 3 != 0 and i % 2 == 0:
            dp.append(min(dp[i//2]+1, dp[i-1]+1))
        else:
            dp.append(dp[i-1]+1)


num = int(input())
makeOne(num)
print(dp[num])

