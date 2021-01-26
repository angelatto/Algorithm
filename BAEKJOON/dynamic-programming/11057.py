"""
오르막 수 (lev.silver-1)
-다이나믹 프로그래밍
수는 0부터 시작
N은 자릿 수

"""

N = int(input())
nums = [1] * 10  # 0-9
print(nums)

for _ in range(N-1):
    for i in range(1, 10):
        nums[i] = nums[i] + nums[i-1]
print(sum(nums) % 10007)