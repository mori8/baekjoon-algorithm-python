n = int(input())
dp = [0 for _ in range(n)] # i번째 수를 마지막으로 하는 IS 중 가장 긴 것의 길이. dp[]를 어떻게 채울 것인가?
arr = list(map(int, input().split()))

for i in range(n):
    maximum = 0
    for j in range(i):
        if maximum < dp[j] and arr[j] < arr[i]:
            maximum = dp[j]
    dp[i] = maximum + arr[i]

print(max(dp))