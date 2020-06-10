n = int(input())

fibo = [0, 1]

for i in range(2, 1000000000000000001):
    num = fibo[i-1] + fibo[i-2]
    fibo.append(num % 1000000)

print(fibo[n])