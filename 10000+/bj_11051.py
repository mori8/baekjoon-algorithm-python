cache = [[0 for i in range(1001)] for j in range(1001)]

n, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(n+1):
        if j == 0 or i == j:
            cache[i][j] = 1
        else:
            cache[i][j] = (cache[i-1][j-1] + cache[i-1][j]) % 10007

print(cache[n][k])
