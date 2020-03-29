# 백준 2193번 이친
# 아이디어 : 조건 2개. 이진수를 string으로 변한한 뒤
# 1. 1로 시작하는가?
# 2. '11'을 포함하지 않는 문자열인가?


# 첫번째 시도 : 큰 수 입력받으면 시간초과됨

# n = input().rstrip('\n')
# ansList = []
#
# for i in range(2 ** (int(n) - 1), 2 ** int(n)):
#     num = format(i, 'b')
#     if str(num)[0] == '0':
#         continue
#     if '11' in str(num):
#         continue
#     ansList.append(num)
#
# print(len(ansList))

# 두번째 시도 : 아이디어 수정
# 1로 시작하고 0의 개수가 n-1개인 string 생성
# 이 string을 2진수 int로 형변환 -> 1을 더함 -> 2진수로 변환 후 다시 str로 형변환 -> 조건 판단(자리수가 n보다 커질 때까지 반복)


# n = int(input())
# ansList = []
# num = '1' + ('0' * (n - 1))
#
# while len(num) == n:
#     print(num)
#     if '11' in num:
#         num = format(int('0b' + num, 2) + 1, 'b')
#         continue
#     ansList.append(num)
#     num = format(int('0b' + num, 2) + 1, 'b')
#
#
# print(len(ansList))
# print(ansList)

# 1
# 10
# 101 100
# 1001 1000 1010
# 10101 10100 10001 10000 10010

# ㅅㅂ 피보나치였네 으아악 ㅜㅜ

n = int(input())

fibo = [0, 1]

for i in range(2, 91):
    num = fibo[i-1] + fibo[i-2]
    fibo.append(num)

print(fibo[n])