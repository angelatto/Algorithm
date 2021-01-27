"""
감시 (lev.gold-5)

지도에서 0은 빈칸, 6은 벽, '''1-5'''는 시시티비 번호
1번은 한쪽 방향 1개 -> (4가지 경우)
2번은 180 2 -> (2가지 경우)
3번은 90도 2개 -> (4가지 경우)
4번은 3개 -> (4가지 경우)
5번은 동서남북 4개 -> (1가지 경우)

씨씨티비는 씨씨티를 통과할 수 있다. 하지만 벽은 통과할 수 없다.
씨씨티비의 방향을 정해서, 사각 지대의 최소 크기를 구하기 -> 이 말은 감시영역을 최대화
감시영역은 '#', 씨씨티비는 최대 8개이다.
"""
import copy

N, M = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
min_result = sum(graph[i].count(0) for i in range(N))

dx = [0, 0, 1, -1]  # 동(0), 서(1), 남(2), 북(2)
dy = [1, -1, 0, 0]

# 씨씨티비의 모든 경우의 수 나열 1-5번
direction = [[], [[0], [1], [2], [3]],
             [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]],
             [[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]],
             [[0, 1, 2, 3]]]

# 1. 일단 그래프에 있는 씨씨티비 정보를 모두 수집 -> 재귀적으로 브루트포스
cctv = [(i, j, graph[i][j]) for i in range(N) for j in range(M) if graph[i][j] in range(1, 6)]


def fill(x, y, graph, dir): # 지도에서 영역 채우기, (x, y)는 씨씨티비 좌표
    for d in dir:
        nx, ny = x, y   # 한가지 경우에 대하여 시작점 좌표 초기화
        while True:  # 한 방향으로 갈 수 있을 때까지 가야함
            nx += dx[d]
            ny += dy[d]
            if not(0 <= nx < N and 0 <= ny < M) or graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = '#'
    return None


def dfs(graph, cnt):
    global min_result
    if cnt == len(cctv): # 종료조건, 모두 뽑았을 때, 하나의 경우의 수
        min_result = min(min_result, sum(graph[i].count(0) for i in range(N)))
        return

    x, y, cc = cctv[cnt]  # 하나의 씨씨티비에 대하여
    for i in direction[cc]:
        temp = copy.deepcopy(graph)  # 새로 시작
        fill(x, y, temp, i)
        dfs(temp, cnt+1)
    return None


# 답 출력
dfs(graph, 0)
print(min_result)