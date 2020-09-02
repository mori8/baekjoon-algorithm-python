import sys, heapq
from collections import deque
r = sys.stdin.readline


def dijkstra(x):
    que = []
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
                path[next] = cur
                heapq.heappush(que, (cur_dist + next_dist, next))
    return dist


def go(s, e, arr):
    arr.appendleft(s)
    if e == -1:
        print(len(arr))
        print(' '.join(map(str, arr)))
        return
    go(e, path[e], arr)


INF = 9876543210
n = int(r())
e = int(r())

adj = [[] for _ in range(n + 1)]
dist = [INF for _ in range(n + 1)]
path = [-1 for _ in range(n + 1)]
for i in range(e):
    u, v, w = map(int, r().split())
    adj[u].append([v, w])

start, end = map(int, r().split())
d = dijkstra(start)
print(dist[end])

deq = deque()
go(end, path[end], deq)
