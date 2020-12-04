import collections
import heapq

def networkDelayTime(times, N: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    print(graph)

    queue = [(0, K)] # 0은 가중치 & K는 시작점, 출발 노드 의미 (우선순위 큐 - minheap이용)
    dist = collections.defaultdict(int)

    while queue:
        time, node = heapq.heappop(queue)

        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                heapq.heappush(queue, (time + w, v))

    print(dist)
    # 출발정점으로부터 나머지 모든 정점으로 도달할 수 있는지 여부를 판단
    if len(dist) == N:
        return max(dist.values()) # dist는 최단경로값이 저장됨
    return -1

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
