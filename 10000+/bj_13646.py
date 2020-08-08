import sys

def solve(x):
    answer = x
    idx = 2
    while idx**2 <= x:
        if x % idx == 0:
            while x % idx == 0:
                x //= idx
            answer *= (1 - 1/idx)
        idx += 1
    if x != 1:  # 마지막에 남는 소인수
        answer *= (1 - 1/x)
    return int(answer)


for line in sys.stdin:
    x = int(line)
    print(solve(x) // 2)
