import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == b == 0:
        break
    print(a + b)