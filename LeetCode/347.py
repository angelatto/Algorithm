import collections
import heapq
def topKFrequent(nums, k: int):
    # 리스트에서 가장 많이 등장하는 k개를 추출
    freqs = collections.Counter(nums)

    # sol1) value 기준으로 딕셔너리 정렬해서 상위 k개의 key를 리스트에 추출
    # newlist = []
    # freqs = sorted(freqs.items(), key=lambda x : x[1], reverse=True)
    #
    # count = 0
    # while count < k:
    #     newlist.append(freqs[count][0])
    #     count += 1
    # return newlist

    # sol2) 우선순위 큐를 이용 - 카운터의 value가 큰 값 기준으로 최대 힙 만들기
    heap = []
    for f in freqs:
        heapq.heappush(heap, (-freqs[f], f))

    newlist = []
    for _ in range(k):
        newlist.append(heapq.heappop(heap)[1])

    # sol3 - 파이썬다운방식
    #return list(zip(*collections.Counter(nums).most_common(k)))[0]

    return newlist
print(topKFrequent([1,1,1,2,2,3], 2))
