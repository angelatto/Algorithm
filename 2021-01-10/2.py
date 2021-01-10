import collections
# 모든 경우의 수
def solution(links):
    answer = 0

    graph = collections.defaultdict(list)
    for link in links:
        graph[link[0]].append(link[1])

    # 먼저, 팀장이면서 팀원이 노드 구하기
    both = []
    li_value = []
    for value in list(graph.values()):
        for v in value:
            li_value.append(v)

    for k in list(graph.keys()):
        if k in li_value:
            both.append(k)

    # 1. 팀원들끼리 경우의 수
    temp = collections.defaultdict(list)
    for g in graph:
        for v in graph[g]:
            if v not in both:
                temp[g].append(v)

    n = 1
    for t in temp:
        n *= len(temp[t])
    answer += n

    # 팀장이 낄 때 - 팀장이 없는 팀의 팀원 개수를 모조리 합하기
    for boss in both:
        n = 0
        for g in graph:
            if boss != g and boss not in graph[g]:
                n += len(graph[g])
        answer += n

    return answer % 1000000007

# print(solution([[4, 5], [4, 3], [4, 2], [1, 6], [7, 4], [7, 1]])) # 7
# print(solution([[3,5], [3,2], [6,3], [6,1], [4,6]])) # 5
