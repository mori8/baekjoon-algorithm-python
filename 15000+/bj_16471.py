import sys

n = int(input())
juon = list(map(int, sys.stdin.readline().split()))
sajang = list(map(int, sys.stdin.readline().split()))

juon.sort()
sajang.sort()

cnt = 0

for i in range(n // 2 + 1):
    if juon[i] < sajang[n // 2 + i]:
        cnt += 1

if cnt > n // 2:
    print("YES")
else:
    print("NO")

