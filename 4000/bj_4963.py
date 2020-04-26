# 백준 4963번 섬의 개수
# dfs

import sys
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]


def dfs(m, n):
    arr[m][n] = '0'
    for i in range(8):
        nm = m + dx[i]
        nn = n + dy[i]
        if nm < 0 or nm >= h or nn < 0 or nn >= w:
            continue
        if arr[nm][nn] == '1':
            dfs(nm, nn)


while 1:
    count = 0
    arr = []
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    for _ in range(h):
        arr.append(input().split())
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '1':
                dfs(i, j)
                count += 1
    print(count)
