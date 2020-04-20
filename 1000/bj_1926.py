import sys
sys.setrecursionlimit(300000)  # ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(a, b):
    global count
    arr[a][b] = '0'
    for k in range(4):
        na = a + dx[k]
        nb = b + dy[k]
        if na < 0 or na >= n or nb < 0 or nb >= m:
            continue
        if arr[na][nb] == '1':
            count += 1
            dfs(na, nb)


n, m = map(int, input().split())
arr = []

c_list = []
area = draw = 0
for line in sys.stdin:
    arr.append(line.split())

for i in range(n):
    for j in range(m):
        if arr[i][j] == '1':
            count = 1
            draw += 1
            dfs(i, j)
            area = max(area, count)

print(draw)
print(area)