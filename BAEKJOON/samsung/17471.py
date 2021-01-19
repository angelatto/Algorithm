"""
- 게리멘더링 (lev.gold-5) : 게리멘더링은 특정 후보자나 정당에 유리하게 선거구를 획정하는 것을 의미한다.

- 연결 그래프로 나타내고, 두 그룹으로 나눌건데, 각각 그룹은 연결되어있는 그래프

-> 여기서 포인트는 하나의 그래프를 두 개의 연결 뽀그래프로 쪼개서 푸는 것 -> 뽑기 문제

- 구하는 것 : 두 선거구에 포함된 인구의 차이를 최소화 -> 최솟값 리턴하기
- 두 선거구로 나눌 수 없는 경우 -1 리턴
"""
import collections
import itertools
import sys

n = int(input())  # 구역의 개수
people = list(map(int, input().split()))

graph = collections.defaultdict(list)
for i in range(n):
    li_t = input().split()  # 2 2 4
    for node in li_t[1:]:
        graph[i + 1].append(int(node))


# 그래프 정점은 1-n 까지

def bfs(sub_graph):  # 연결그래프인지
    visited = []
    queue = collections.deque()
    queue.appendleft(sub_graph[0]) # 시작점 임의로 넣기

    while queue:
        v = queue.pop()
        if v not in visited:
            visited.append(v)

        for w in graph[v]:
            if w in sub_graph and w not in visited:
                queue.appendleft(w)

    if sum(visited) == sum(sub_graph):
        return True
    return False


def cal(g1, g2):
    sum1 = 0
    for i in g1:
        sum1 += people[i - 1]

    sum2 = 0
    for i in g2:
        sum2 += people[i - 1]

    if sum1 >= sum2:
        return sum1 - sum2
    return sum2 - sum1


# 1개 ~ n//2개 뽑기
min_ans = sys.maxsize
for k in range(1, n // 2 + 1):  # 뽑는 개수
    bucket = list(itertools.combinations(range(1, n + 1), k))
    for one in bucket:
        other = [n for n in range(1, n + 1) if n not in one]
        # one과 other이 각각 연결리스트이면 인구차이 계산하기
        if bfs(one) and bfs(other):
            cur_ans = cal(one, other)
            min_ans = min(min_ans, cur_ans)

# 답 리턴
if min_ans == sys.maxsize:
    print(-1)
else:
    print(min_ans)
