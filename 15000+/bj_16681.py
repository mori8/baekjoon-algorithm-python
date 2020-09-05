import sys
import heapq

r = sys.stdin.readline


def dijkstra(x):
    que = []
    dist = [INF for _ in range(n + 1)]
    dist[x] = 0
    heapq.heappush(que, (0, x))
    while que:
        cur_dist, cur = heapq.heappop(que)
        if dist[cur] < cur_dist:
            continue
        for i in adj[cur]:
            next, next_dist = i
            if cur_dist + next_dist < dist[next] and high[cur-1] < high[next-1]:
                dist[next] = cur_dist + next_dist
                heapq.heappush(que, (cur_dist + next_dist, next))
    return dist


INF = sys.maxsize
n, m, d, e = map(int, r().split())
high = list(map(int, r().split()))
adj = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, w = map(int, r().split())
    adj[a].append([b, w])
    adj[b].append([a, w])

f = dijkstra(1)
s = dijkstra(n)
ans = []

for i in range(1, n) :
    if f[i] != INF and s[i] != INF:
        ans.append(high[i-1] * e - d * (f[i] + s[i]))

if ans:
    print(max(ans))
else:
    print("Impossible")


# 1. 다익 한문제 더
# 2. 내일 발표준비
# 3. DSC(10일까지)
