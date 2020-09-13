import sys
r = sys.stdin.readline


def bubble_sort(num):
    for i in range(len(num) - 1):
        for j in range(len(num) - i - 1):
            if int(num[j + 1] + num[j]) > int(num[j] + num[j + 1]):
                num[j], num[j + 1] = num[j + 1], num[j]


n = int(r())
arr = r().rstrip().split()
bubble_sort(arr)

print(int(''.join(arr)))
