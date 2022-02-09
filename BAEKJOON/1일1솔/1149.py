"""
RGB거리
22.02.09

3
26 40 83
49 60 57
13 89 99

"""
n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    r, g, b = list(map(int, input().split()))

    if i == 0:
        dp[0][0] = r
        dp[0][1] = g
        dp[0][2] = b
    else:
        dp[i][0] = min(dp[i-1][1] + r, dp[i-1][2] + r)
        dp[i][1] = min(dp[i-1][0] + g, dp[i-1][2] + g)
        dp[i][2] = min(dp[i-1][0] + b, dp[i-1][1] + b)

print(min(dp[-1]))