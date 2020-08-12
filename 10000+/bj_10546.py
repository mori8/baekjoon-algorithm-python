import sys
input = sys.stdin.readline
marathon = {}

n = int(input())

for i in range(n):
    tmp = input().strip()
    if not marathon.get(tmp):
        marathon[tmp] = 1
    else:
        marathon[tmp] += 1

for i in range(n-1):
    tmp = input().strip()
    if marathon[tmp] == 1:
        del marathon[tmp]
    else:
        marathon[tmp] -= 1

for k in marathon:
    print(k)
    break
