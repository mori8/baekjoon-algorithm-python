# 백준 11021 A + B - 7
# 후딱

t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print("Case #" + str(i) + ": " + str(a+b))
