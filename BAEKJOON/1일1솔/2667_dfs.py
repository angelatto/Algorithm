"""
01.11.22
실버1
- 단지 번호 붙이기
- 총단지수 출력
- 총단지만큼, 각각 단지내 집의 수를 오름차순으로 정렬하여 한줄씩 출력

-입력
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
-출력
3
7
8
9
"""
import sys

# dfs 탐색
def dfs(x, y):
    # 종료 조건
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0  # 방문 표시
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


# main
n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 탐색 후 단지에 저장
# 그래프 전체 돌면서 1나오면 탐색 시작 , 방문 후에는 1->0 으로 변경
count = 0
danzi = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            # 탐색 시작
            danzi.append(count)
            count = 0


# 총단지수
danzi.sort()
print(len(danzi))
for dz in danzi:
    print(dz)
