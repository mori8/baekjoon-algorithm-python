from itertools import combinations_with_replacement
n, m = map(int, input().split())
pool = [str(x) for x in range(1, n+1)]

c = combinations_with_replacement(pool, m)
for item in c:
    print(' '.join(item))