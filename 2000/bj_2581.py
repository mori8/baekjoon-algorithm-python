# 백준 2581번 소수
# 아이디어 : 자연수 M부터 N까지의 수를 그것보다 작은 모든 수로 나눔 -> 하나라도 나누어떨어지는 수가 있으면 break
# 놓친 점 : 2는 예외처리를 해줘야 함

m = int(input())
n = int(input())

primes = []

for i in range(m, n+1):
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

if not primes:
    print(-1)
else :
    print(sum(primes))
    print(primes[0])