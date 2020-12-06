import collections
import heapq
# bfs로 풀면 테케1번이 런타임에러가 난다. -> 이문제는 dfs로 푸는게 훨씬 쉬움.

def solution(tickets):
    answer = []

    flights = collections.defaultdict(list)
    for t in tickets:
        heapq.heappush(flights[t[0]], t[1])

    now = 'ICN'
    answer.append(now)

    count = 0
    while count != len(tickets):
        print(flights)
        print(now, flights[now])
        candidate = flights[now][0]
        if candidate not in flights and len(tickets)-count != 1: # alt를 sfo 뒤로 보낸다 / 마지막 순서가 아니어야함
            heapq.heappop(flights[now])
            tmp = now
            now = heapq.heappop(flights[now])
            answer.append(now)
            count += 1

            heapq.heappush(flights[tmp], candidate)
            # flights[now].append(candidate)
        else:
            now = heapq.heappop(flights[now])
            answer.append(now)
            count += 1
    return answer

# print(solution([['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]))

# print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'],
#  ['ATL', 'ICN'], ['ATL','SFO']]))
# print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]))
# print(solution([['ICN','B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']]))
# print(solution( [['ICN','A'],['ICN','A'],['A','ICN']]))
print(solution([['ICN', 'A'], ['ICN', 'B'], ['A', 'D'], ['D', 'C'], ['C', 'ICN']]))
