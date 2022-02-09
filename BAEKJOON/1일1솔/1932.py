"""
정수 삼각형
22.02.09

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

입력과 동시에 최댓값 계산
점화식 느낌 -> 다이나믹 프로그래밍

1 <= n <= 500
"""
n = int(input())
dp = [[0 for _ in range(i+1)] for i in range(n)]
w = [list(map(int, input().split())) for _ in range(n)]
dp[0][0] = w[0][0]

for i in range(1, n):  # w 배열
    for j in range(i+1):
        # w 에서 맨 앞과 맨 끝만 주의
        if j == 0:
            dp[i][j] = w[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = w[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(w[i][j] + dp[i-1][j], w[i][j] + dp[i-1][j-1])

print(max(dp[n-1]))