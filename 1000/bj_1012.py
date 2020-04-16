# 백준 1012 유기농 배추
# dfs

import sys
sys.setrecursionlimit(50000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = int(input())


def dfs(x, y):
    arr[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if arr[nx][ny] == 1:
            dfs(nx, ny)


for _ in range(t):
    count = 0
    m, n, k = map(int, sys.stdin.readline().split())
    arr = [[0 for x in range(n)] for y in range(m)]
    for x in range(k):
        a, b = map(int, sys.stdin.readline().split())
        arr[a][b] = 1
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
