# 백준 1978번 소수 찾기
# 아이디어 : 2581번 응용

m = int(input())
n = input().split()

primes = []

for i in range(2, 1001):
    flag = 0
    if i == 2:
        primes.append(2)
    else:
        for j in range(2, i):
            flag = i % j
            if flag == 0:
                break
    if flag != 0:
        primes.append(i)

count = 0

for i in n:
    if int(i) in primes:
        count += 1

print(count)