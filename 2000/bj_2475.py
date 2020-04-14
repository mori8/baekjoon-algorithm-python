# 백준 2475번 검증수
# 클래스 1 올클

num = list(map(int, input().split()))
sum = 0

for i in num:
    sum += i**2

print(sum%10)