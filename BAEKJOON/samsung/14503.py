"""
로봇 청소기 (lev.gold-5)
- 시뮬레이션
- 처음에 틀린 이유
  1.  후진한다는 것을 청소한다고 생각함. 애초에 무조건 청소가능한 좌표만 큐에 넣는 코드로 작성함.
  2.  후진할 때, 청소안한 구역만 후진 가능한 줄 알았는데, 벽만 아니면 후진은 가능한 -> 청소랑 벽을 구분해야 함
"""
import collections

N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))  # 방향 - 0 북 , 1 동, 2 남 , 3 서
graph = [list(map(int, input().split())) for i in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = collections.deque()
queue.appendleft((r, c, d))  # 현재 위치 - (r, c), 현재 바라보는 방향 - d

# 현재 위치 청소
result = 1
graph[r][c] = 2
while queue:
    r, c, d = queue.pop()

    next_dir = d
    # 2. 현재 위치에서 왼쪽 방향 부터 차례대로 탐색
    for i in range(4):
        next_dir = (next_dir + 3) % 4
        nx, ny = r + dx[next_dir], c + dy[next_dir]

        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:  # 2-a
            # 1. 현재 위치 청소
            graph[nx][ny] = 2
            result += 1
            queue.appendleft((nx, ny, next_dir))  # 한 칸 전진
            break
        elif i == 3:  # 2-c 후진을 한다. -> 여기서 주의할 점은 후진하고 2번으로 돌아간다. 이 말 즉슨 청소를 하지 않는다.
            back_dir = (d + 2) % 4
            nx, ny = r + dx[back_dir], c + dy[back_dir]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 1:  # 벽이 아닌 이상 후진을 한다.
                queue.appendleft((nx, ny, d))  # 한 칸 후진


# 답 출력 - 청소한 영역
print(result)
