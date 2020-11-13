# def solution(triangle):
#     answer = 0
#     # 모든 경우의 수 고려
#     for i in range(1, len(triangle)):
#         for j in range(i+1):
#             if j == 0: # 왼쪽 끝 깂
#                 triangle[i][j] += triangle[i-1][j]
#             elif j == i: # 오른쪽 끝
#                 triangle[i][j] += triangle[i-1][j-1]
#             else:
#                 triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
#
#     return max(triangle[-1])


def solution(triangle):
    memo = {}
    def dynamic(triangle, x, y):
        t_len = len(triangle) - 1
        if x == t_len: # 종료조건
            return triangle[x][y]

        # 메모이제이션
        if (x+1, y) not in memo:
            memo[(x+1,y)] = dynamic(triangle, x+1, y)

        # 메모이제이션
        if (x+1, y+1) not in memo:
            memo[(x+1,y+1)] = dynamic(triangle, x+1, y+1)

        return max(triangle[x][y] + memo[(x+1,y)],
                triangle[x][y] + memo[(x+1, y+1)])

    # main
    answer = dynamic(triangle, 0, 0)
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
