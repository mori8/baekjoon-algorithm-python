# 백트래킹
# 가능한 모든 경우의 수의 최대값이 16조 이상이므로 완전 탐색으로는 제한 시간(2초)안에 구현 불가
# 필요한 정보, Base Case, Recursive Case 생각하기


def check(index):  # 현재 index 번째 수를 채울 때 sign[i][index]의 부호조건을 만족하는지 아닌지 검사하는 함수(역순)
    s = 0
    for i in range(index, -1, -1):
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] < 0:
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            if s <= 0:
                return False
    return True


def solve(index):   # 현재 index 번째 수를 채우는 함수
    if index == n:  # check(index)를 만족해야 solve(index + 1)의 재귀호출이 가능하므로 index = n이면 sign 배열의 모든 부호 조건을 만족한 경우이므로 True 리턴
        return True
    if sign[index][index] == 0:  # recursive case 1: 현재 index 수가 n 미만이고 0이면 바로 조건 검사 후 재귀 호출
        ans[index] = 0           # index ~ index 번째의 수의 합이 0이 되려면 ans[index]가 0이 되어야 함!
        return check(index) and solve(index + 1)

    for i in range(1, 11):       # recursive case 2: 현재 index 수가 n 미만이고 0이 아니면 index 번째 부호를 붙인 후 조건 검사 후 재귀 호출
        ans[index] = i * sign[index][index]
        if check(index) and solve(index + 1):
            return True
    return False


n = int(input())
ans = [0] * n
signs = list(input())
sign = [[0 for _ in range(n)] for _ in range(n)]

idx = 0

for i in range(0, n):
    for j in range(i, n):
        if signs[idx] == '+':
            sign[i][j] = 1
        elif signs[idx] == '-':
            sign[i][j] = -1
        idx += 1

solve(0)
print(' '.join(map(str, ans)))
