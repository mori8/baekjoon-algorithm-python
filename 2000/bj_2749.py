# 피보나치 수 2 -> 피사노 주기
n = int(input())

fibo = [0, 1]

for i in range(2, 1500001):
    num = fibo[i-1] + fibo[i-2]
    fibo.append(num % 1000000)

print(fibo[n % 1500000])
