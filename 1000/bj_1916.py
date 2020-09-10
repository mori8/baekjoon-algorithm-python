import sys, heapq
r = sys.stdin.readline
INF = 9876543210


def dijkstra(x):
    que = []
    dist = [INF for _ in range(1001)]
    dist[x] = 0
    heapq.heappush(que, (0, x))
    while que:
        cur_dist, cur = heapq.heappop(que)
        if dist[cur] < cur_dist:
            continue
        for i in adj[cur]:
            next, next_dist = i
            if cur_dist + next_dist < dist[next]:
                dist[next] = cur_dist + next_dist
                heapq.heappush(que, (cur_dist + next_dist, next))
    return dist


n = int(r())
m = int(r())
adj = [[] for _ in range(1001)]

for i in range(m):
    a, b, w = map(int, r().split())
    adj[a].append([b, w])

start, end = map(int, r().split())

d = dijkstra(start)
print(d[end])
