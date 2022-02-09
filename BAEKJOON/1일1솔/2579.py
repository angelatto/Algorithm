"""
계단오르기
22.02.09


6
10
20
15
25
10
20


"""

def solution(n, w):
    if n == 1:
        return w[0]
    if n == 2:
        return w[0] + w[1]

    dp = [0 for _ in range(n+1)]
    dp[0], dp[1], dp[2] = 0, w[0], w[0]+w[1]
    for k in range(3, n+1):
        dp[k] = max(dp[k-3]+w[k-2]+w[k-1], dp[k-2]+w[k-1])
    return dp[n]


n = int(input())
w = [int(input()) for _ in range(n)]
print(solution(n, w))
