n, m = map(int, input().split())
lst = [[] * m] * n

for x in range(n):
    lst[x] = list(map(int, input().split()))

k = int(input())

for r in range(k):
    i, j, x, y = map(int, input().split())
    sum = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            sum += lst[a][b]
    print(sum)
