# 병든 나이트
# 그리디
n, m = map(int, input().split())
# 잘 생각해보면 한 열 당 나이트 하나밖에 못 들어감
if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m + 1) // 2))
elif m < 7:
    print(min(4, m))
else:
    print(m - 2)