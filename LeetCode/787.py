import collections
import heapq

def findCheapestPrice(n: int, flights, src: int, dst: int, K: int) -> int:

    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    queue = [(0, 0, src)] # 맨 앞에 0은 price, 가운데는 경유지 개수, 마지막은 출발점 노드
    # 주의 !!!!! - 애초에 우선순위 큐에 경유지 조건을 만족하는 경우만 큐에 푸시한다.

    while queue:
        price, mid, node = heapq.heappop(queue)

        if node == dst: # 도착지에 도착하면 - 리턴!!!! 여기서는 최소가격보다 경유지가 선조건이다.
            print(price, mid, node)
            return price
        for v, w in graph[node]:
            if mid <= K:
                heapq.heappush(queue, (price + w, mid+1, v))

    return -1

print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))
