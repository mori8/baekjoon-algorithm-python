# 백트래킹
# 1. 방문 배열을 재귀 호출이 종료된 뒤에 초기화해주어야 함
# 2. 조건에 맞는 숫자를 재귀호출하는지 확인해주어야 함
import sys


def check(x, y, op):
    if op == '>' and x <= y:
        return False
    if op == '<' and x >= y:
        return False
    return True


def solve(index, seq):
    global min_value, max_value
    if index == k+1:
        if int(seq) < int(min_value):
            min_value = seq
        if int(seq) > int(max_value):
            max_value = seq
        return
    for i in range(10):
        if not visited[i]:
            if index == 0 or check(int(seq[index-1]), i, arr[index-1]):
                visited[i] = True
                solve(index+1, seq + str(i))
                visited[i] = False  # 방문한 곳은 초기화해주어야 모든 경우를 탐색할 수 있다


visited = [False] * 10
k = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split())

min_value = '99999999999'
max_value = '0'

solve(0, '')
print(max_value)
print(min_value)
