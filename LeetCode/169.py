import collections
# 과반수를 차지하는 엘리먼트를 출력하는 문제

# 첫 번쨰 풀이
# def majorityElement(nums) -> int:
#     counter = collections.Counter(nums)
#     result = counter.most_common()
#
#     return result[0][0]
# print(majorityElement([3,2,3]))

# 두 번쨰 풀이 - 분할 정복 (우아한 풀이 방식)
def majorityElement(nums) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    # 재귀적으로 a와 b는 각각 최소 단위로 쪼개진다. - 분할 단계
    half = len(nums) // 2
    a = majorityElement(nums[:half])
    b = majorityElement(nums[half:])

    # 최소 단위로 쪼개지면 과반수인 수를 리턴하면서 백트래킹한다. - 정복 단계
    return [b, a][nums.count(a) > half]

# test-case
print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
