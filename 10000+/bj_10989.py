# 수 정렬하기 3
# Counting sort

import sys

arr = [0] * 10001  # index : 0 ~ 10000
n = int(input())

for line in sys.stdin:
    arr[int(line.rstrip())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)