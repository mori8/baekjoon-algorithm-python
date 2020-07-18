# 최소 신장 트리
# 프림 알고리즘(힙 사용)

from collections import defaultdict
from heapq import *

v, e = map(int, input().split())
edges = []

for i in range(e):
    a, b, w = input().split()
    w = int(w)
    edges.append((w, a, b))


def prim(start_node, edges):
    dis = 0
    adj_edges =defaultdict(list)
    for w, a, b in edges:
        adj_edges[a].append((w, a, b))
        adj_edges[b].append((w, b, a))

    connected_nodes = set(start_node)  # 연결된 노드의 집합
    candidate_edge_list = adj_edges[start_node]  # 연결된 노드와 인접한 노드의 집합
    heapify(candidate_edge_list)   # 우선순위 큐 이용 - adj_edges가 (w, a, b)로 구성되어 있으니 자동으로 가중치 순서대로 정렬됨

    while candidate_edge_list:
        w, a, b = heappop(candidate_edge_list)  # 선택된 간선은 간선 리스트에서 제거
        if b not in connected_nodes:
            connected_nodes.add(b)
            dis += w
        for e in adj_edges[b]:
            if e[2] not in connected_nodes:
                heappush(candidate_edge_list, e)
    return dis


print(prim('1', edges))