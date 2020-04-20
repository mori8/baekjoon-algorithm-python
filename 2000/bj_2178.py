import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
miro = []

for line in sys.stdin:
    miro.append(line.rstrip())
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
q = deque([[0, 0]])

# bfs
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if miro[nx][ny] == '1' and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])

print(visited[n-1][m-1])

