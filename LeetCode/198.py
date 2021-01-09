# 딕셔너리에서 가장 마지막 아이템을 추출하려면 popitem()을 사용해야 한다.
import collections

# 다이나믹 프로그래밍 - 타뷸레이션
def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    dp = collections.OrderedDict()
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp.popitem()[1] # key와 value중에 value만 출력 
