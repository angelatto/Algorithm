"""
타일 채우기 (lev.silver-1)
-다이나믹 프로그래밍
높이 3, 가로 길이 N인 직사각형 경우의 수
"""
import collections

N = int(input())
dp = collections.defaultdict(int)
dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = 2 + dp[i-2] * 3 + (sum(dp.values()) - dp[i-2]) * 2

print(dp[N])