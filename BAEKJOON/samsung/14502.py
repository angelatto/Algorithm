"""
- 연구소 (lev.gold-5)

- 0 : 빈칸, 1 : 벽, 2 : 바이러스
- 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안정 영역. -> 안정 영역 크기의 최댓값 구하기
- 브루트 포스
- 벽 위치 (i, j) 뽑는다. 뽑을 때 graph[i][j] == 0 이어야 함

- python3로는 안돌아가고 pypy3로는 돌아감..
"""
import copy
import collections
import sys


max_safe = 0  # 안정 영역 최댓값
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = collections.deque()


def bfs():  # 2가 발견되면 bfs 탐색으로 0을 2로 바꿈.. 1로 막힐 때까지
    global max_safe
    temp = copy.deepcopy(graph)

    for a in range(N):
        for b in range(M):
            if temp[a][b] == 2:
                queue.appendleft((a, b))

    while queue:
        a, b = queue.pop()
        temp[a][b] = 2

        for z in range(4):
            x = a + dx[z]
            y = b + dy[z]

            if 0 <= x < N and 0 <= y < M and temp[x][y] == 0:
                queue.appendleft((x, y))

    # 0의 개수 카운트 -> safe 최대 크기 비교
    safe = 0
    for i in range(N):
        safe += temp[i].count(0)
    max_safe = max(max_safe, safe)


def solution(x):
    if x == 3: # 종료 조건 오직 하나
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0: # 벽을 세울 수 있을 때
                graph[i][j] = 1
                solution(x+1)
                graph[i][j] = 0 # 원상 복귀


# main
N, M = list(map(int, sys.stdin.readline().split()))  # 행과 열
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(N)]
solution(0) # 벽을 세울 수 있는 공간중에서 3개를 뽑는 모든 경우의 수
print(max_safe)