# 캐시 - LRU(Least Recently Used) 캐시 교체 알고리즘을 구현하는 문제
# 난이도 - 하
# 주의 - 대소문자를 구분하지 않는다 !!!!!
# 적게 사용된게 아니라 -> 가장 오래전에 사용한걸 지우는 거임

#rerererere

import collections
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    # 대소문자 처리
    def f(city):
        return city.lower()
    cities = list(map(f, cities))

    answer = 0
    cache = collections.OrderedDict()
    for city in cities:
        if city in cache: # 캐시에 이미 있다면
            answer += 1
            cache[city] += 1
        else:
            answer += 5
            # 버퍼의 공간이 없을 때 - 캐시 교체 작업 여기서부터 !!
            if len(cache) == cacheSize:
                # 가장 적게 사용된 도시를 찾아서 삭제 -> 캐시에 도시와 함꼐 사용횟수를 저장해야함
                li = sorted(cache.items(), key=lambda x: x[1]) # value로 오름차순 정렬
                last = cache.pop(li[0][0])
            cache[city] = 1

    return answer

print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']))
print(solution(2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(solution(5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(solution(2, ['Jeju', 'Pangyo', 'NewYork', 'newyork']))
print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
