# 백준 1914번 하노이 탑


def hanoi(n, start, to, via):
    if n == 1:
        print(start, to)
    else:
        hanoi(n-1, start, via, to)
        print(start, to)
        hanoi(n-1, via, to, start)


num = int(input())

print(2**num - 1)

if num <= 20:
    hanoi(num, 1, 3, 2)