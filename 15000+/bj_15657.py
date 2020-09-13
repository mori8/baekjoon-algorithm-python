from itertools import combinations_with_replacement
n, m = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
arr.sort()
c = combinations_with_replacement(arr, m)
for x in c:
    for i in x:
        print(i, end=' ')
    print()
