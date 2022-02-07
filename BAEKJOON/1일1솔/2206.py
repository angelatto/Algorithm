"""
답 15
6 4
0100
1110
1000
0000
0111
0000

-------------------------------------------------------------------------------------------------
결국 중요한 아이디어는
기존에 최단거리문제는 해당 정점에 방문했으면, 그게 그리디하게 , 그 정점까지의 비용은 최소임을 가정했는데.
지금은 해당 정점까지의 비용이 최소라고 하더라도, 전체로봤을때 최단거리임을 보장하지는 못하기 때문에.. 왜냐면 아예 도착지에 도착을 못할 수도 있음.

다시말하면,  벽을 뚫고 해당정점 최단비용됐는데, 전체로봤을떄 거기까지 벽을 안뚫고 오더라도 나중에 뚫는게 더 이득일 수 있음.
그래서 해당 노드에 대해서 이전에 벽을 뚫고 온 비용인지, 벽을 안뚫고 도착한 비용인지 각각 저장해놓아야 한다... ! <-- 핵심 아이디어

그니까. 해당정점을 큐에서 꺼내서 딱 도착했을때 그 비용을 확신할 수 없다. 벽을 뚫고왔는지 안뚫고왔는지 옵션이 하나 생겼기 때문에 !!!
------------------------------------------------------------------------------------------------

오류나는 테스트케이스 찾음 ... 답은 9인데 -1이나옴.
4 6
010011
011001
000010
111110

"""

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문 체크를 2가지 케이스로 나눠서 진행해야함
# [0, 0] : 지나지않은케이스, 벽을 지나온케이스
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
print(visited)


def bfs():
    # 큐: x, y, 벽을 뚫었는지 여부 (1이면 이제 벽 못뚫음.)
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1  # 비용

    while queue:
        x, y, flag = queue.pop()

        print(f'방문함: (x, y)', x, y)
        print(f'비용: cost', visited[x][y][flag])
        print('queue: ', queue)

        # 여기가 이슈임. 무작정 방문했다고 컨티뉴 날려버리면안됨. 두가지 경우로 나눠야함.
        # if visited[x][y] == 1:
        #     continue

        if x == N - 1 and y == M - 1:
            return visited[x][y][flag]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 뚫여있고, 아직 방문하지 않은 상태
                if graph[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                    queue.appendleft((nx, ny, flag))
                    visited[nx][ny][flag] = visited[x][y][flag] + 1
                # 벽이 막혀있는 상태
                elif graph[nx][ny] == 1 and flag == 0:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][flag] + 1

    return -1


print(bfs())

