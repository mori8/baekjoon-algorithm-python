# 백준 2747, 2748번 피보나치 수 1, 2
# 아이디어 : 재귀함수
# 놓친 점 : 시간제한있음
# 새로운 아이디어 : 리스트를 이용하자

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# n = int(input())
#
# print(fibonacci(n))


n = int(input())

fibo = [0, 1]

for i in range(2, 10001):
    num = fibo[i-1] + fibo[i-2]
    fibo.append(num)

print(fibo[n])