k = int(input())

cache = [[] * 2] * 41
cache[0] = [1, 0]
cache[1] = [0, 1]

for i in range(2, 41):
    cache[i] = [cache[i-1][0] + cache[i-2][0], cache[i-1][1] + cache[i-2][1] ]

for x in range(k):
    n = int(input())
    print(cache[n][0], cache[n][1])
