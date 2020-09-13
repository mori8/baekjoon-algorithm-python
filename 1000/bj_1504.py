# 시간초과나서 똑같은 로직으로 C++로 제출함
import sys
r = sys.stdin.readline
INF = 9876543210

n, m = map(int, r().split())
adj = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, r().split())
    adj[a][b] = min(c, adj[a][b])
    adj[b][a] = min(c, adj[b][a])

p1, p2 = map(int, r().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                adj[a][b] = 0
                continue
            adj[a][b] = min(adj[a][k] + adj[k][b], adj[a][b])

answer = min(adj[1][p1] + adj[p1][p2] + adj[p2][n], adj[1][p2] + adj[p2][p1] + adj[p1][n])
print(answer)
