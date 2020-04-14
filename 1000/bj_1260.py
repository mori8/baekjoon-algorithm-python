# 백준 1260번 DFS와 BFS
# set으로 만들어서 방문 노드 중복 제거하는 방법 좋은 것 같다. 이해도 잘 된다

from collections import deque


def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort()
                queue += tmp
    return " ".join(str(x) for x in visited)


def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort(reverse=True)
                stack += tmp
    return " ".join(str(x) for x in visited)


graph_dic = {}
n, m, v = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    if a not in graph_dic:
        graph_dic[a] = [b]
    elif b not in graph_dic[a]:
        graph_dic[a].append(b)
    if b not in graph_dic:
        graph_dic[b] = [a]
    elif a not in graph_dic[b]:
        graph_dic[b].append(a)


print(dfs(graph_dic, v))
print(bfs(graph_dic, v))

