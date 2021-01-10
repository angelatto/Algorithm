# 집에서 학교까지 최단 경로의 개수를 1,000,000,007로 나눈 나머지를 구하기
# 집 : (0,0)  학교 : (n-1, m-1)
# 최단경로를 하나만 구하는게 아니라면.. 다익스트라 아닐수도
# import heapq
# def solution(m, n, puddles): # n행 m열 테이블
#     answer = 0 # 최단 경로 개수 의미
#
#     # 오른쪽, 아래쪽으로만 이동 가능
#     dx, dy = [0, 1], [1, 0]
#
#     # puddles 재정의
#     for i in range(len(puddles)):
#         puddles[i] = [puddles[i][1]-1, puddles[i][0]-1]
#
#     # 최단 경로의 '개수'를 구하면 풀리는 문제
#     # 1. 먼저, 그래프를 만든다 -> pass : 여기서는 puddles가지고 바로 풀기 pass
#     flag = True; onlyCost = 0
#     # 2. 그 다음, 우선순위 큐를 이용하여 BFS 탐색을 한다.
#     queue = [(0, 0, 0)] # 비용과, 시작좌표
#     while queue:
#         cost, i, j = heapq.heappop(queue)
#
#         if i == n-1 and j == m-1: # 학교에 도착
#             answer += 1
#             if flag: # 최초 발견
#                 flag = False
#                 onlyCost = cost
#             elif cost != onlyCost:
#                 break
#
#         # 가능한 인접 정점들 큐에 삽입
#         for z in range(2):
#             nx = i + dx[z]
#             ny = j + dy[z]
#             if nx < n and ny < m and [nx, ny] not in puddles:
#                 heapq.heappush(queue, (cost+1, nx, ny))
#     print('answer: ', answer)
#     return answer % 1000000007
# print(solution(4, 3, [[2,2]])) # 4

# dp 풀이
def solution(m, n, puddles):
    dp = [[0]*(m+1) for _i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1: # (1,1) - 시작점 
                dp[i][j] = 1
            elif [j, i] not in puddles:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n][m]%1000000007
