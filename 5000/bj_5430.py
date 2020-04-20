# 백준 5430 AC
# deque

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    cmd = sys.stdin.readline()
    size = int(sys.stdin.readline())
    if size == 0:
        dq = deque(list(sys.stdin.readline().lstrip('[').rstrip(']\n')))
    else:
        dq = deque(list(map(int, sys.stdin.readline().lstrip('[').rstrip(']\n').split(','))))

    r_flag = False  # reverse?
    d_flag = False  # D에서 발생한 에러는 []을 출력할 필요가 없다

    for c in cmd:
        if c == 'R':
            if r_flag:
                r_flag = False
            else:
                r_flag = True
        if c == 'D':
            if not dq:
                print("error")
                d_flag = True
                break
            if r_flag:
                dq.pop()
            else:
                dq.popleft()

    if dq and r_flag and not d_flag:
        dq.reverse()
        print('[' + ','.join(str(x) for x in dq) + ']')
    elif dq and not r_flag and not d_flag:
        print('[' + ','.join(str(x) for x in dq) + ']')
    elif not dq and not d_flag:
        print("[]")
