# 원점에서 가까운 포인트 K개를 리턴하라.
# 우선순위 큐를 이용하여 heap에서 K개 추출한다.
import heapq
def kClosest(points, K: int):
    heap = []
    for (x,y) in points:
        dist = x**2 + y**2
        heapq.heappush(heap, (dist, x, y))

    result = []
    for _ in range(K):
        (dist, x, y) = heapq.heappop(heap)
        result += [x,y],
    return result

print(kClosest([[3,3],[5,-1],[-2,4]], 2))
