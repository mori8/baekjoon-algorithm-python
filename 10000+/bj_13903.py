from collections import deque
import sys
input = sys.stdin.readline

dx = []
dy = []
cnt = []

n, m = map(int, input().split())
arr = [input().split() for _ in range(n)]
way = int(input())

for i in range(way):
    r, c = map(int, input().split())
    dx.append(r)
    dy.append(c)

visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
for i in range(m):
    if arr[0][i] == '1':
        this_cnt = 0
        q.append([0, i])
        visited[0][i] = 1

while q:
    x, y = q.popleft()
    for i in range(way):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if arr[nx][ny] == '1' and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            if nx == n - 1:
                cnt.append(visited[nx][ny] - 1)
            q.append([nx, ny])

if not cnt:
    print('-1')
else:
    print(min(cnt))
