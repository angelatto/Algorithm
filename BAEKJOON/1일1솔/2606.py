"""
01.16.22
실버3

1번 노드의 (단지개수 -1) 을 출력하라. 자신 미포함

"""
import sys
from collections import deque


def bfs(graph, start):
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        visited[node] = 1
        # print(node)
        result.append(node)

        for i in graph[node]:
            if not visited[i] and i not in queue:
                queue.append(i)

    return len(result)-1


# main
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
#
# print(graph)
# print(visited)
print(bfs(graph, 1))





