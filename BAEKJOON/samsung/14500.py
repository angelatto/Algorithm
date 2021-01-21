"""
테트로미노 (lev.gold-5)
- brute force
- pypy3 통과, python3 시간초과
"""

N, M = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]

# 19가지 도형의 모양에 대해서 모든 경우를 따져보기
candidates = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],

    [(0, 0), (0, 1), (1, 0), (1, 1)],  # 3

    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(1, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],  # 9

    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # 15

    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (0, 1), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 1), (1, 1), (1, 0), (0, 2)]   # 19
]


def cal(x, y): # 19가지 모든 경우의 수 중에서 최댓 값 리턴
    result = 0
    for i in range(19):
        sub_sum = 0
        for j in range(4):
            nx = x + candidates[i][j][0]
            ny = y + candidates[i][j][1]
            if not(0 <= nx < N and 0 <= ny < M):
                break
            sub_sum += graph[nx][ny]
            result = max(result, sub_sum)
    return result


max_sum = 0
for i in range(N):
    for j in range(M):
        max_sum = max(cal(i, j), max_sum)

# 답 출력
print(max_sum)