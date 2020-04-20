import sys
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = []
n = int(input())


for line in sys.stdin:
    arr.append(list(line.rstrip()))


def dfs(a, b, color):
    visited[a][b] = 1
    for k in range(4):
        na = a + dx[k]
        nb = b + dy[k]
        if na < 0 or na >= n or nb < 0 or nb >= n:
            continue
        if arr[na][nb] == color and visited[na][nb] == 0:
            dfs(na, nb, color)


# 적록색약이 아닌 경우
count = 0
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, arr[i][j])
            count += 1

print(count)

# 적록색약인 경우
count = 0
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, arr[i][j])
            count += 1

print(count)
