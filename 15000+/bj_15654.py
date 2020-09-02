import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
arr.sort()
comb = list(permutations(arr, m))
for x in comb:
    for i in x:
        print(i, end=' ')
    print()