import sys
input = sys.stdin.readline
check = {}
cnt = 0
l = 0


def t(x):
    h, m = map(int, x.split(':'))
    return int(h * 60 + m)


while 1:
    r = input().rstrip()
    if not r:
        break
    if l == 0:
        s, e, q = r.split()
        start = t(s)
        end = t(e)
        qu = t(q)
        l += 1
        continue
    time, mem = r.split()
    time = t(time)
    if time <= start:
        check[mem] = 1
    elif qu >= time >= end:
        if check.get(mem) and check[mem] == 1:
            cnt += 1
            check[mem] = 2


print(cnt)
exit(0)
