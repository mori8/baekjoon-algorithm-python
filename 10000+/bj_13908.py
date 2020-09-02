n, m = map(int, input().split())
nums = map(int, input().split())

pw = 0
cnt = 0

if n == m:
    ans = 1
    for i in range(1, n+1):
        ans *= i
    print(ans)
    exit(0)

for i in range(0, int('9'*n)):
    if not set(nums) - set(list(str(pw))):
        cnt += 1
    pw += 1

print(cnt)