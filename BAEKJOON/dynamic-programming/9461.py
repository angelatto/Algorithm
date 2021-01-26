"""
파도반 수열 (lev.silver-3)
- 다이나믹 프로그래밍
"""
import collections

tc = int(input())
dp = collections.defaultdict(int)
dp[0], dp[1], dp[2] = 1, 1, 1
for _ in range(tc):
    N = int(input())
    for i in range(3, N):
        if not dp[i]:
            dp[i] = dp[i-2] + dp[i-3]
    print(dp[N-1])