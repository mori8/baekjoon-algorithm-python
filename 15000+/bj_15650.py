from itertools import combinations

n, m = map(int, input().split())
pool = [str(x) for x in range(1, n+1)]

comb = list(combinations(pool, m))
for item in comb:
    print(' '.join(item))

