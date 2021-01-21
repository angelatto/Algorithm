"""
주사위 굴리기 (lev.gold-5)
- 시뮬레이션 문제
- 삼섬 sw 역량 테스트 기출 문제
"""

N, M, x, y, K = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
# 명령 : 동-1, 서-2, 북-3, 남-4

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 - 위 북 동 서 남 아래
dice = [0 for _ in range(6)]

for k in range(K):  # 명령 하나씩 실행할때 마다 주사위 맨 위 숫자 출력
    c = command[k] - 1
    # 이동할 주사위 위치
    nx = x + dx[c]
    ny = y + dy[c]

    if not (0 <= nx < N and 0 <= ny < M):  # 지도를 벗어나면 무시
        continue

    # 주사위를 굴리고나서 주사위 값 갱신
    if c == 0:  # 동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif c == 1:  # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif c == 2:  # 북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:  # 남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    #  주사위 바닥의 숫와 지도 값 갱신
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]  # 주사위 바닥-> 지도로
    else:
        dice[5] = graph[nx][ny]  # 지도 -> 주사위로
        graph[nx][ny] = 0

    x, y = nx, ny  # 현재 주사위 위치 갱신
    print(dice[0])  # 주사위 맨 윗면 출력
