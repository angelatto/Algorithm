# 우선순위 큐를 이용
import heapq
def mergeKLists(lists):
    heap = []
    for list in lists:
        for i in list:
            heapq.heappush(heap, i)

    result = []
    while heap:
        result.append(heapq.heappop(heap))
    return result


print(mergeKLists([[1,4,5],[1,3,4],[2,6]]))
