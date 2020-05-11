# 날짜 계산

e, s, m = map(int, input().split())
num = 0

while 1:
    if num % 15 == e-1 and num % 28 == s-1 and num % 19 == m-1:
        # 1 <= e <= 0 15보다 0 <= e <= 14로 생각하는게 더 쉬운듯
        print(num+1)
        break
    num += 1