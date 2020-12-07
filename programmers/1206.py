import collections
# bfs로 풀면 테케1번이 런타임에러가 난다. -> 이 문제는 dfs로 푸는게 훨씬 쉬움.
def solution(tickets):
    #그래프 만들기
    graph = collections.defaultdict(list)
    for t in tickets:
        graph[t[0]].append(t[1])
    print(graph)

    # 그래프 알파벳 순으로 정렬
    for g in graph:
        graph[g].sort()
    print(graph)

    #--main--시작정점: ICN
    N = len(tickets)
    answer = dfs(graph, N, 'ICN', ['ICN'])
    return answer

def dfs(graph, N, v, footprint):
    print(footprint)

    if len(footprint) == N+1: # 종료조건
        return footprint

    for index, country in enumerate(graph[v]):
        graph[v].pop(index)

        tmp = footprint[:]
        tmp.append(country)
        ret = dfs(graph, N, country, tmp)

        if ret:
            return ret
        else:
            print(graph)
            graph[v].insert(index, country) # 다시 반복문 돌아야함. 원상복귀해줌
            print(graph)


print(solution([['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]))
# print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'],
#  ['ATL', 'ICN'], ['ATL','SFO']]))
# print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]))
# print(solution([['ICN','B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']]))
# print(solution( [['ICN','A'],['ICN','A'],['A','ICN']]))
# print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'D'], ['D', 'C'], ['C', 'ICN']]))
