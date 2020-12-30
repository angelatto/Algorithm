import heapq
def reconstructQueue(people):
# 방법 1 시간복잡도 : 104초 공간복잡도 : 15.1
# 우선순위 큐를 이용하여 키가 큰 순서대로 pop하고 인덱스를 지정해서 배열에 삽입
    #heap = [] # 키 max heap
    # for person in people:
    #     heapq.heappush(heap, (-person[0], person[1]))
    #
    # result = []
    # while heap:
    #     person = heapq.heappop(heap)
    #     result.insert(person[1], [-person[0], person[1]])

# 방법2 시간복잡도: 88초 공간복잡도 : 14.9
# people을 다중 조건으로 재정렬 한 뒤에 인덱스를 지정해서 배열에 삽입

    result = []
    people = sorted(people, key=lambda person : (-person[0], person[1]))

    print(people)

    for person in people:
        result.insert(person[1], [person[0], person[1]])

    return result
print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
