# 백준 2667 단지번호붙이기
# dfs

import sys

dx = [-1, 0, 1, 0]  # 좌 하 우 상
dy = [0, 1, 0, -1]

n = int(input())
arr = [list(sys.stdin.readline()) for x in range(n)]

count = 0
apart = []


def dfs(x, y):
    global count
    arr[x][y] = '0'  # 재방문 방지용으로 방문한 곳은 0으로 바꿔주기
    count += 1
    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]
        if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:
            continue
        if arr[new_x][new_y] == '1':
            dfs(new_x, new_y)


for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            count = 0
            dfs(i, j)
            apart.append(count)

print(len(apart))
for i in sorted(apart):
    print(i)

