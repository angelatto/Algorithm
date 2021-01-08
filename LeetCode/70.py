# bucket = [1, 2] 중에서 중복으로 몇개를 뽑을 지 모르지만 -> 합이 n이되는 경우의 수를 구하기

# sol-1 ) 다이나믹 프로그래밍 - 메모이제이션
import collections
# def climbStairs(n: int) -> int:
#     dp = collections.defaultdict(int) # 생성 작업이 재귀함수 안에 있으면 안됨
#
#     def _climbStairs(n):
#         if n <= 2:
#             return n
#
#         if dp[n]:
#             return dp[n]
#         dp[n] = _climbStairs(n-1) + _climbStairs(n-2)
#         return dp[n]
#
#     return _climbStairs(n)
#
# print(climbStairs(38))

# # sol-1 ) 다이나믹 프로그래밍 (상향식) - 타뷸레이션
def climbStairs(n: int) -> int:
    climb = collections.defaultdict(int)
    for i in range(n+1):
        if i <= 2:
            climb[i] = i
        else:
            climb[i] = climb[i-1] + climb[i-2]

    return climb[n]

print(climbStairs(38))
