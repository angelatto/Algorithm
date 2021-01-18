import collections
dp = collections.defaultdict(int)


def solution(n):

    dp[0], dp[1], dp[2] = 0, 1, 1
    for i in range(3, n+1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2])
        else:
            dp[i] = dp[i - 1] + 1

    return dp[n]


# --main--
# print(solution(5))
# print(solution(6))
print(solution(5000))