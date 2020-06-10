from itertools import permutations

n, m = map(int, input().split())
pool = [str(x) for x in range(1, n+1)]

perm = list(permutations(pool, m))
for item in perm:
    print(' '.join(item))
