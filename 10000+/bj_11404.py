import sys
r = sys.stdin.readline
INF = 9876543210

n = int(r())
m = int(r())
adj = [[INF for _ in range(101)] for _ in range(101)]

for i in range(m):
    a, b, c = map(int, r().split())
    adj[a][b] = min(adj[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if adj[i][j] == INF:
            print("0", end=" ")
        else:
            print(adj[i][j], end=" ")
    print()
