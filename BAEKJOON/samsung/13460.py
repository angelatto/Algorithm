"""
01.11.22
골드1


"""
from collections import deque

# 세로, 가로
N, M = map(int, input().split())
graph = []

for _ in range(N):
   graph.append(list(input()))
# print(graph)

red, blue, target = None, None, None

# 1. 빨간구슬, 파란구슬, 구멍위치(타겟,종료조건에 이용됨)의 위치 각각 구하기
for i in range(N):
    for j in range(M):
        if red and blue and target:
            break
        if graph[i][j] == 'R':  # 빨구
            red = (i, j)
        elif graph[i][j] == 'B':  # 파구
            blue = (i, j)
        elif graph[i][j] == 'O':  # 파구
            target = (i, j)
print(red, blue, target)

# 2. 그래프를 탐색하면서 최소 구슬 이동횟수 구하기
# 이동제약이 많음. + 10번 이하로 뺴낼 수 없으면 -1 출력

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 탐색 시작점이 빨구와 파구 위치 이다. 시작점이 2개인게 특이한점!
# bfs 탐색 시작. -> 방문 표시는 그래프에 직접 0으로 변환
for i in range(N):
    for j in range(M):
        if graph[i][j] == '.':  # 빈칸
            pass
        elif graph[i][j] == '#':  # 이동못함
            pass
