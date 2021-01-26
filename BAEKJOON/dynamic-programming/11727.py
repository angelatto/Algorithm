"""
2*n 타일링 2 (lev.silver-3)
- 다이나믹 프로그래밍
"""
import collections

N = int(input())
dp = collections.defaultdict(int)
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[N] % 10007)