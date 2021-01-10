# 숫자 N과 사칙연산을 이용하여 number를 만들 때, N의 사용횟수의 최솟값을 구하기
import collections
def solution(N, number):
    if N == number:
        return 1

    dp = collections.defaultdict(set)
    dp[1].add(N)
    for i in range(2, 9):
        dp[i].add(int(str(N)*i))
        for key in range(1, i):
            for j in dp[key]:
                for z in dp[i-key]:
                    dp[i].add(j * z)
                    dp[i].add(j + z)
                    dp[i].add(j - z)
                    dp[i].add(z - j)
                    if z != 0:
                        dp[i].add(j // z)
                    if j != 0:
                        dp[i].add(z // j)

        # print('dp: ',  dp)
        if number in dp[i]:
            return i

    return -1

# print(solution(5, 12)) # 4
# print(solution(2, 11)) # 3
# print(solution(1, 1121)) # 7
