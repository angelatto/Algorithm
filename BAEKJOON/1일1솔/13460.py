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
        if graph[i][j] == 'O':
            target = [i, j]
print(red, blue, target)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

"""
빨구 파구 기울이기는 최대로 진행 (더 이상 구슬이 움직이지 않을 때까지 이동! )
-> 즉, 타겟에 도착했다고 바로 리턴하면 안되고 끝까지 봐야함 
1. 빨구만 타겟에 도착해야함. 
2. 파구가 먼저 타겟에 도착하거나 빨구 뒤따라서 타겟에 도착하게되면 실패 
절대원칙 : 이 둘은 동시에 한 칸에 있을 수 없다!!!  에스파는 나야! 둘은 될 수 없어! 
"""

def bfs():
    queue = deque([[red, blue]])
    print(queue)
    while queue:
        r, b = queue.pop()
        print(r, b)

        # 타겟에 도착
        if r[0] == target[0] and r[1] == target[1]:
            # 바로 리턴하면 안되고, 파란색공까지 지켜봐야함.
            # 이렇게 단도직입적으로 종료지점이 같기보단? ,,,, 이건 밑에서 걸러줄거같기도하고,,,, 다시생각
            if b[0] == target[0] and b[1] == target[1]:
                return -1
            print('success')
            return

        # 방향은 4가지인데, 한칸만 이동하는게 아님! 최대로 그방향으로 이동. 벽이 나올때까지.
        # 그런데 최대로 이동하다가 구멍(도착지잠)이 발견되면 거기로 안착! 더이상 이동 불가.
        # 근데 그게 파구면 실패. 빨구더라도 뒤에 파구가 거기까지 따라오면 실패
        for i in range(4):
            # r2 = [x, y]
            r2, b2 = None, None
            # 빨간구슬, 파란구슬 동시에 기울이는 과정
            while graph[r[0]][r[1]] == 'O':
                r[0], r[1] = r[0] + dx[i], r[1] + dy[i]
                b[0], b[1] = b[0] + dx[i], b[1] + dy[i]

                # 이동가능 2가지  : ('.', 'O')
                if 0 < r[0] < M-1 and 0 < r[1] < N-1:
                    if graph[r[0]][r[1]] == 'O':
                        pass
                    elif graph[r[0]][r[1]] == '.':
                        pass

            queue.appendleft([r2, b2])

print(bfs())



