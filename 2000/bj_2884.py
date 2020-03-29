# 백준 2884번 알람 시계
# 아이디어 : 보면 알어...

h, m = map(int, input().split())

if m - 45 > 0:
    print(h, (m - 45))
elif m == 45:
    print(h, 0)
else:
    h -= 1
    if h < 0:
        h = 23
    m += 15
    print(h, m)