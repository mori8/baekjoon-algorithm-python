import sys

while 1:
    nums = sys.stdin.readline().split()
    l = int(nums[0])
    if l == 0:
        exit(0)
    nums = nums[1:]
    nums.sort()
    if l % 2 == 0:
        tmp1 = tmp2 = ''
        for i in range(l // 2 + 1):
            tmp1 += nums[i]
            tmp2 += nums[l // 2 + i - 1]
        print(int(tmp1) + int(tmp2))
    else:
        tmp1 = tmp2 = ''
        for i in range(1, l // 2 + 1):
            tmp1 += nums[i]
            tmp2 += nums[l // 2 + i - 1]
        print(int(tmp1) + int(tmp2))