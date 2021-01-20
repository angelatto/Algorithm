"""
뱀 - lev.gold5
시뮬레이션 문제
"""
import collections

N = int(input())  # N행 N열
K = int(input())  # 사과의 개수
graph = [[0] * N for _ in range(N)]
for _ in range(K):
    i, j = list(map(int, input().split()))
    graph[i - 1][j - 1] = '#'  # 사과의 위치

L = int(input())  # 뱀의 방향 변환 횟수
dir = {}
for _ in range(L):
    a, b = input().split()
    dir[int(a)] = b  # X초가 끝난 뒤에 D : 오른쪽, L: 왼쪽으로 90도 회전

# -------------------------------------------------------------

time = 0  # 첫 시작은 0초 부터
x, y = 0, 0  # 뱀의 첫 위치

dx = [0, 1, 0, -1] # 동 , 남, 서, 북
dy = [1, 0, -1, 0]
# 현재는 동쪽, 오른쪽으로 직진
cur_d = 0
snake = collections.deque()  # 뱀 나타내기
snake.appendleft([0, 0])

while True:
    # 일단 뱀의 머리를 이동. 바라보고 있는 방향으로
    x += dx[cur_d]
    y += dy[cur_d]
    time += 1

    # 종료 조건 : 벽이거나 자기 몸이 닿을 때
    if not (0 <= x < N and 0 <= y < N) or [x, y] in snake:
        break

    snake.appendleft([x, y])  # 왼쪽이 머리, 오른쪽이 꼬리

    # 사과 체크
    if graph[x][y] == '#':
        graph[x][y] = 0
    else:
        snake.pop()

    # 방향 체크 -> 이 부분이 가장 생각하기 어려웠음, 머리만 방향 전환하면 되는 줄 몰랐음.
    if time in dir:
        if dir[time] == 'L':
            cur_d = (cur_d - 1) % 4  # 북쪽으로 방향 전환
        else:
            cur_d = (cur_d + 1) % 4  # 남쪽으로 방향 전환

# 답 리턴
print(time)
