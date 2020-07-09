import sys

n = int(sys.stdin.readline())

for i in range(1, n):
    const = i
    tmp = i
    while tmp:
        const += tmp % 10
        tmp //= 10
    if const == n:
        print(i)
        exit(0)

print(0)