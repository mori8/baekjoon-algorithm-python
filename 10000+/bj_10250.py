num = int(input())
for i in range(num):
    height, width, n = map(int, input().split())
    if n % height == 0:
        print("%d%02d" % (height, n / height))
    else:
        print("%d%02d" % (n % height, (n / height) + 1))
