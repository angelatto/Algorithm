# def search(nums, target: int) -> int:
#     try:
#         return nums.index(target)
#     except ValueError:
#         return -1

# 이진 검색으로 다시 풀어보기
def search(nums, target: int) -> int:
    if not nums:
        return -1

    # 이진탐색으로 최솟값을 찾아 피벗 설정
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right-left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    pivot = left

    # 피벗 기준으로 이진 검색
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right-left) // 2
        mid_pivot = (mid+pivot) % len(nums)

        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    return -1


print(search([4,5,6,7,0,1,2],0))
