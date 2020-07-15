import sys
from itertools import combinations

while 1:
    nums = sys.stdin.readline().strip().split()
    if nums[0] == '0':
        break
    nums = nums[1:]
    answer = list(map(' '.join, combinations(nums, 6)))
    for x in answer:
        print(x)
    print()
