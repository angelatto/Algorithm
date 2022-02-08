"""
1로 만들기
22.02.09

"""


def solution(n):
    if n == 1:
        return 0
    if n <= 3:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2], dp[3] = 0, 0, 1, 1

    if n <= 3:
        return dp[n]

    for k in range(4, n+1):
        case = []
        if k % 2 == 0:
            case.append(dp[k // 2])
        if k % 3 == 0:
            case.append(dp[k // 3])
        case.append(dp[k-1])
        dp[k] = min(case) + 1
    return dp[n]


n = int(input())
print(solution(n))