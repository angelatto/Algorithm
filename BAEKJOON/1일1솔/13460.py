"""
구슬탈출2
2022.02.08

5 5
#####
#..B#
#.#.#
#RO.#
#####

"""
import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
print(graph)

# 출발점 찾아내기 : R, B 위치  /   타겟 지점 찾아내기 : 0 위치
# 결국 출발점 -> 도착점 최단거리 구하는 문제 (단지, 파란구슬 장애물 옵션 추가)
red, blue, target = None, None, None
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            red = [i, j]
        if graph[i][j] == 'B':
            blue = [i, j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

"""
빨구 파구 기울이기는 최대로 진행 (더 이상 구슬이 움직이지 않을 때까지 이동! )
-> 즉, 타겟에 도착했다고 바로 리턴하면 안되고 끝까지 봐야함 
1. 빨구만 타겟에 도착해야함. 
2. 파구가 먼저 타겟에 도착하거나 빨구 뒤따라서 타겟에 도착하게되면 실패 
절대원칙 : 이 둘은 동시에 한 칸에 있을 수 없다!!!  에스파는 나야! 둘은 될 수 없어! 


빨간색 큐랑 파란색 큐랑 각각 두어야 할 수도 ... 
"""

# 방문체크를 안하고 있음
# 최단거리 비용도 체크해야함.
visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs():
    queue = deque([[red, blue]])
    visited[red[0]][red[1]] = 1
    visited[blue[0]][blue[1]] = 1

    while queue:
        r, b = queue.pop()
        print(r, b)

        # 타겟에 도착
        if graph[r[0]][r[1]] == 'O':
            # 바로 리턴하면 안되고, 파란색공까지 지켜봐야함.
            # 이렇게 단도직입적으로 종료지점이 같기보단? ,,,, 이건 밑에서 걸러줄거같기도하고,,,, 다시생각
            # if b[0] == target[0] and b[1] == target[1]:
            #     return -1
            print('success')
            return visited[r[0]][r[1]]

        # 방향은 4가지인데, 한칸만 이동하는게 아님! 최대로 그방향으로 이동. 벽이 나올때까지.
        # 그런데 최대로 이동하다가 구멍(도착지잠)이 발견되면 거기로 안착! 더이상 이동 불가.
        # 더 이상 이동이 불가할때 queue에 삽입 !!!!
        # 근데 그게 구멍에 파구가 지나가면 실패. 빨구더라도 뒤에 파구가 거기까지 따라오면 실패
        for i in range(4):
            # 초기화
            r2, b2 = r, b
            # 빨간구슬 기울이는 과정 - 빨간거 먼저 싹 이동
            while True:
                r2[0], r2[1] = r2[0] + dx[i], r2[1] + dy[i]
                if 0 < r2[0] < M-1 and 0 < r2[1] < N-1 and not visited[r2[0]][r2[1]]:
                    # 빨간 구슬 끝까지 이동
                    if graph[r2[0]][r2[1]] in ('#', 'B'):
                        r2[0], r2[1] = r2[0] - dx[i], r2[1] - dy[i]
                        break
                    if graph[r2[0]][r2[1]] == 'O':
                        visited[r2[0]][r2[1]] = 1
                        break
                    visited[r2[0]][r2[1]] = 1
                else:
                    r2[0], r2[1] = r2[0] + dx[i], r2[1] + dy[i]
                    break



            # 파란구슬 기울이는 과정
            flag = True
            while True:
                b2[0], b2[1] = b2[0] + dx[i], b2[1] + dy[i]
                if 0 < b2[0] < M-1 and 0 < b2[1] < N-1 and not visited[b2[0]][b2[1]]:
                    # 끝까지 이동
                    if graph[b2[0]][b2[1]] in ('#', 'R'):
                        b2[0], b2[1] = b2[0] - dx[i], b2[1] - dy[i]
                        break
                    # 갈수는 있는데 가면 실패임.
                    if graph[b2[0]][b2[1]] == 'O':
                        visited[b2[0]][b2[1]] = 1
                        flag = False
                    visited[b2[0]][b2[1]] = 1
                else:
                    b2[0], b2[1] = b2[0] - dx[i], b2[1] - dy[i]
                    break

            # 둘다 끝까지 이동 완료.
            if flag:
                # visited[r2[0]][r2[1]] = 1
                # visited[b2[0]][b2[1]] = 1

                queue.appendleft([r2, b2])
    return -1


print(bfs())