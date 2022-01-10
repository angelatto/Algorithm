"""
실버2
01.09.22


4 5 1
1 2
1 3
1 4
2 4
3 4

"""
import sys
from collections import deque

# dfs
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True

    # 이제 여기서 방문하는 노드마다 해야할 비지니스로직 처리하면됨
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# bfs
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()

        # 여기서 이제 각 노드 마다 해야할 비지니스 로직 처리
        print(v, end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# main
# 정점 , 간선 개수 , 시작점
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


# print(graph)
for g in graph:
    g.sort()
# print(graph)


# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * (n+1)
dfs(graph.copy(), v, visited)
print()
visited = [False] * (n+1)
bfs(graph.copy(), v, visited)
