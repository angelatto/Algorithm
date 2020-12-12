# gold5 - 파이프 옮기기1
# dp, graph

# 백준 입력
n = int(input())
graph = [[*map(int, input().split())] for _ in range(n)]
print(solution(n, graph))

def solution(n, graph):
    dx = [0,1,1]
    dy = [1,1,0]

    def checkStatus(u, v):
        if u[0] == v[0] and u[1] != v[1]: #가로
            return 0
        elif u[0] != v[0] and u[1] == v[1]: #세로
            return 1
        elif u[0] != v[0] and u[1] != v[1]: #대각선
            return 2

    def moveNext(next_u, next_v):
        if next_v[0] >= n or next_v[1] >= n:
            return False
        if graph[next_u[0]][next_u[1]] == 1 or graph[next_v[0]][next_v[1]] == 1:
            return False
        return True

    def dfs(u, v):
        global count
        # print('u: ', '(', u[0], u[1],')', ' v:', '(', v[0], v[1], ')')

        # 1. 종료조건
        if v[0] == v[1] == n-1:
            count += 1
            # print('도착함, 카운트 1증가해야함', count)

        # 2. status 파악 : 가로-0, 세로-1, 대각선-2
        # home에 1이 있으면 갈 수 없는 경우임
        status = checkStatus(u, v)
        if status == 0: #가로
            # print('가로->가로')
            next_u = [u[0], u[1]+1]
            next_v = [v[0], v[1]+1]
            if moveNext(next_u, next_v):
                dfs(next_u, next_v)

            # print('가로->대각선')
            next_u = [u[0], u[1]+1]
            next_v = [v[0]+1, v[1]+1]
            if moveNext(next_u, next_v):
                dfs(next_u, next_v)

        elif status == 1: #세로
            # print('세로->세로')
            next_u = [u[0]+1, u[1]]
            next_v = [v[0]+1, v[1]]
            if moveNext(next_u, next_v):
                dfs(next_u, next_v)

            # print('세로->대각선')
            next_u = [u[0]+1, u[1]]
            next_v = [v[0]+1, v[1]+1]
            if moveNext(next_u, next_v):
                dfs(next_u, next_v)

        elif status == 2: #대각선
            # print('대각선->가로')
            next_u = [u[0]+1, u[1]+1]
            next_v = [v[0], v[1]+1]
            if moveNext(next_u, next_v):
                dfs(next_u, next_v)

            # print('대각선->세로')
            next_u = [u[0]+1, u[1]+1]
            next_v = [v[0]+1, v[1]]
            if moveNext(next_u, next_v):
                dfs(next_u, next_v)

            # print('대각선->대각선')
            next_u = [u[0]+1, u[1]+1]
            next_v = [v[0]+1, v[1]+1]
            if moveNext(next_u, next_v):
                dfs(next_u, next_v)

        # print('count : ', count)
        return count

    # --main--
    global count
    count = 0
    answer = dfs([0,0], [0,1]) # start
    return answer #방법이 없으면 0



# test case
# print(solution(3, [[0,0,0], [0,0,0], [0,0,0]]))
# print(solution(4, [[0,0,0,0], [0,0,0,0],[0,0,0,0], [0,0,0,0]]))
# print(solution(5, [[0,0,1,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]))
# print(solution(6, [[0,0,0,0,0,0], [0,1,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]))
