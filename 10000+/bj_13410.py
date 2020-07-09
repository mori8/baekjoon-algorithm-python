n, k = map(int, input().split())
maximum = 0

for i in range(1, k+1):
    tmp = int(''.join(reversed(str(n * i))))
    if maximum < tmp:
        maximum = tmp

print(maximum)
