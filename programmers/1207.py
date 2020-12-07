import collections
import heapq

def solution(n, edge):
    # 그래프 만들기
    graph = collections.defaultdict(list)
    for e in edge: #양방향 그래프이다.
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # 각 정점별로 최단경로 기록, 동시에 방문체크까지 가능
    dist = collections.defaultdict(int)

    # Dijkstra
    queue = [(0, 1)] # 시작 정점이 1
    while queue:
        count, node = heapq.heappop(queue)
        # 방문 체크와 동시에 최단경로의 간선 수 초기화
        if node not in dist:
            dist[node] = count
            # 큐에 넣기
            for w in graph[node]:
                heapq.heappush(queue, (count+1, w))

    li = list(dist.values())
    return li.count(max(li))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
