# fibonacci 재귀, 다이나믹 프로그래밍
import collections
# --------------sol-1) 브루트포스 방식, 가장 느림
# def fib(n: int) -> int:
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)


# --------------sol-2) 다이나믹 프로그래밍 (하향식) - 메모이제이션 이용
# def fib(n: int) -> int:
#     dp = collections.defaultdict(int)
#     if n <= 1:
#         return n
#
#     if dp[n]:
#         return dp[n]
#     dp[n] = fib(n-1) + fib(n-2)
#     return dp[n]

# --------------sol-2) 다이나믹 프로그래밍 (상향식) - 반복문 이용, 타뷸레이션, 진짜 dp
def fib(n: int) -> int:
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x+y
    return x

print(fib(4))
