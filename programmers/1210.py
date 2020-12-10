import collections

def solution(arrows):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    # 1. 그래프 만들기 - 좌표를 인접리스트로 표현함.
    graph = collections.defaultdict(list)

    curX = curY = 0
    before = (curX, curY)
    for arrow in arrows:
        curX += dx[arrow]
        curY += dy[arrow]
        after = (curX, curY)
        # print('before: ', before, 'after: ', after)

        graph[before].append(after)
        graph[after].append(before)  # 양방향이라서 이렇게 함

        before = after
    # print(graph)

    # 2. 그래프(인접리스트) DFS 탐색하면서 사이클 찾아내기
    traced = set()
    # 양방향 그래프라서 자기 자신으로 돌아오지 않게 해야함
    # 양방향이라서 방문체크가 필요함.....
    # 백트래킹할때를 카운트하면 어떨지....???/?
    # 백트링하는 시점을 어디서 출력해야 할지 고민해보기 
    # visited = []

    def dfs(node): #사이클이 있으면 재귀 종료가 안됨.
        print('node: ', node)
        if node in traced:
            return False

        traced.add(node)
        for w in graph[node]:
            if not dfs(w):
                return False
        return True

    #--main--
    start = (0, 0)
    for x in list(graph):
        if not dfs(x):
            print('----')

    return 0

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
