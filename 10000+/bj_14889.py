from itertools import combinations
import sys

n = int(input())
nums = tuple(x for x in range(1, n+1))
stat = []
min_gap = 999999
for i in range(n):
    stat.append(list(map(int, sys.stdin.readline().split())))

my_comb = list(combinations(nums, n//2))

for i in range(len(my_comb)):
    my_total = 0
    op_total = 0
    op_comb = list(set(nums) - set(my_comb[i]))
    for a, b in combinations(my_comb[i], 2):
        my_total += stat[a - 1][b - 1] + stat[b - 1][a - 1]
    for c, d in combinations(op_comb, 2):
        op_total += stat[c - 1][d - 1] + stat[d - 1][c - 1]
    gap = abs(my_total - op_total)
    if min_gap > gap:
        min_gap = gap

print(min_gap)
