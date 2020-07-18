n, m, k = map(int, input().split())
maximum = 0

for i in range(k + 1):
    girls = n - k + i
    boys = m - i
    if girls > 0 and boys > 0 and girls >= 2 * boys and maximum < boys:
        maximum = boys
    elif maximum < girls // 2 < boys:
        maximum = girls // 2


print(maximum)
