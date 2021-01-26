"""
타일 채우기 (lev.silver-1)
-다이나믹 프로그래밍
점화식 설명
: 길이가 N인 자기 자신 2개 + 길이가 2인거랑 * 길이가 N-2인거랑 + 나머지꺼 각각 * 2(더 이상 쪼개지지 않는)
"""
import collections

N = int(input())
dp = collections.defaultdict(int)
dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = 2 + dp[i-2] * dp[2] + (sum(dp.values()) - dp[i-2]) * 2

print(dp[N])