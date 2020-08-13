# 그르다 김가놈
# 이분탐색?
import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
kimbab = []

for i in range(n):
    # 김밥 손질
    tmp = int(input())
    if tmp >= 2*k:
        kimbab.append(tmp - 2*k)
    elif tmp > k:
        kimbab.append(tmp - k)
    else:
        continue

def check(x):
    global m, kimbab
    cnt = 0
    for i in range(len(kimbab)):
        cnt += kimbab[i] // x
    if cnt >= m:
        return True
    return False

# main
left = 1
right = sum(kimbab)
ans = 0

while left <= right:
    mid = (left + right) // 2
    if mid == 0:
        print(-1)
        exit(0)
    elif check(mid):
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

if ans == 0:
    print(-1)
else:
    print(ans)