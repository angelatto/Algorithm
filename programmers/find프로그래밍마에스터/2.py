# 게임 맵 최단거리
# visited 배열 안쓰고 maps 자체에서 1->0 으로 방문표시 했더니 효율성 통과
# 공간복잡도 최적화 고려하기

import heapq
def solution(maps):
    n = len(maps) # 행
    m = len(maps[0]) # 열

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    Q = [(1, 0, 0)] # 비용, 시작 정점 (i, j)

    while Q:
        cost, i, j = heapq.heappop(Q)

        if i == n-1 and j == m-1: #종료조건
            return cost

        for z in range(4):
            x = dx[z] + i
            y = dy[z] + j
            if not(x < 0 or x >= n or y < 0 or y >= m) and maps[x][y] == 1:
                maps[x][y] = 0
                heapq.heappush(Q, (cost+1, x, y))

    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))


# 최단거리를 구할 때 시작 정점에서 목적지까지 도달할 수 없는 경우도 있다면
# 동서남북으로 이동할수있을 때 무한으로 돌기 때문에
# 방문여부 체크해야 한다.

# 만약에 무조건 시작점에서 도착할 수 있는 경우만 있다면 최단경로 구할 때 방문체크 필요 없음
