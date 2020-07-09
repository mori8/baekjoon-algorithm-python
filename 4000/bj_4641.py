import sys

while 1:
    arr = list(map(int, sys.stdin.readline().strip().split()))
    if arr[0] == -1:
        break
    count = 0
    for x in arr:
        if x != 0 and x * 2 in arr:
            count += 1
    print(count)