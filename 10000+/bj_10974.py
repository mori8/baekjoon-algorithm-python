from itertools import permutations

n = int(input())
arr = [str(x) for x in range(1, n+1)]

perms = list(permutations(arr, n))

for x in perms:
    print(' '.join(x))
