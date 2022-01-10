"""
01.09.22
실버2

# 정점, 간선, 시작점
5 5 3
5 4
5 2
1 2
3 4
3 1

"""
import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 정점, 간선, 시작점
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# 작은 수를 가진 정점부터 탐색하기 위함
for g in graph:
    g.sort()

visited = [False] * (n+1)
dfs(graph.copy(), v, visited)
print()
visited = [False] * (n+1)
bfs(graph.copy(), v, visited)
