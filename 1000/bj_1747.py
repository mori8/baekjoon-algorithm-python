# 백준 1747번 소수&팰린드롬
# 아이디어 : 1차로 팰린드롬만 뽑고 2차로 소수 판별

import sys

num = int(sys.stdin.readline())

while True:
    if str(num) == str(num)[::-1]:
        if num == 1:
            num += 1
        elif num == 2:
            print(num)
            break
        else:
            for i in range(2, num):
                flag = num % i
                if not flag:
                    break
            if not flag:
                num += 1
            else:
                print(num)
                break
    else:
        num += 1


