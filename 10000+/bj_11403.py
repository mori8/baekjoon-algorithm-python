import sys
r = sys.stdin.readline

adj = []
n = int(r())
for i in range(n):
    adj.append(list(map(int, r().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj[i][k] + adj[k][j] == 2:
                adj[i][j] = 1

for i in range(n):
    for j in range(n):
        print(adj[i][j], end=" ")
    print()
