from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
index_arr = [x for x in range(n)]
perms = list(permutations(index_arr, n))
nums = [0 for _ in range(n)]
max = 0

for i in perms:
    idx = 0
    sum = 0
    for x in i:
        nums[x] = arr[idx]
        idx += 1
    for j in range(n-1):
        sum += abs(nums[j] - nums[j+1])
    if sum > max:
        max = sum

print(max)
