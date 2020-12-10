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

        graph[before].append(after) # 헐 사실은 이거 단방향임
        # graph[after].append(before)  # 양방향이라서 이렇게 함
        before = after
    # print(graph)

    # # 2. 그래프(인접리스트) DFS 탐색하면서 사이클 찾아내기
    traced = []

    # # 양방향 그래프라면 자기 자신으로 돌아오지 않게 해야함
    # # 양방향이라면 방문체크가 필요함.....
    # 하지만 이건 단방향이니까 이런게 필요없는 거임

    def dfs(node):
        global answer
        # print('node: ', node)

        if len(traced) != 0 and traced[-1][0] != node[0] and traced[-1][1] != node[1]: #대각선
            nx = (traced[-1][0]+node[0])/2
            ny = (traced[-1][1]+node[1])/2
            if (nx, ny) in traced:
                traced.append((nx, ny))
                answer += 1
            if node in traced:
                traced.append(node)
                answer += 1
            print(traced)

            if (nx, ny) in traced or node in traced:
                return False

        elif node in traced:  # 대각선 아닐때
            traced.append(node)
            print(traced)
            answer += 1
            return False


        if len(traced) != 0 and traced[-1][0] != node[0] and traced[-1][1] != node[1]:
            nx = (traced[-1][0]+node[0])/2
            ny = (traced[-1][1]+node[1])/2
            traced.append((nx, ny))
        traced.append(node)
        print('중복이 없을 때: ', traced)

        for w in graph[node]:
            if not dfs(w):
                return False

        return True

    #--main--
    global answer
    answer = 0
    start = (0, 0)
    for x in list(graph):
        if x not in traced:
            if not dfs(x):
                print('cycle')

    return answer

# print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
# print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]))
# print(solution([5, 2, 7, 1, 6, 3]))
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))
