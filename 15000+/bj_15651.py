from itertools import product
n, m = map(int, input().split())
pool = [str(x) for x in range(1, n+1)]

rep_com = product(pool, repeat=m)
for item in rep_com:
    print(' '.join(item))