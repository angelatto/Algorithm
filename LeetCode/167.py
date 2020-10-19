# 두 수를 더해서 target이 되는 인덱스 2개를 구하기 (1부터 시작)
# 방법1 - 투 포인터 -> 시간복잡도 O(n)
# def twoSum(numbers, target: int):
#     # numbers는 정렬되어 있다 !! 오름차수으로 !!!
#     left, right = 0, len(numbers)-1
#     while left <= right:
#         if numbers[left] + numbers[right] < target:
#             left += 1
#         elif numbers[left] + numbers[right] > target:
#             right -= 1
#         else:
#             return left+1, right+1

# 방법2 - 이진 검색 -> 시간 복잡도 O(nlogN)
# def twoSum(numbers, target: int):
#     for k, v in enumerate(numbers):
#         left, right = k+1, len(numbers)-1
#         expected = target - v
#         # 이진 검색으로 나머지 값 검색하기
#         while left <= right:
#             mid = left + (right - left) // 2
#             if numbers[mid] < expected:
#                 left = mid + 1
#             elif numbers[mid] > expected:
#                 right = mid - 1
#             else:
#                 return k+1, mid+1


# 방법3 - bisect 모듈 이용
import bisect
def twoSum(numbers, target: int):
    for k, v in enumerate(numbers):
        expected = target - v
        index = bisect.bisect_left(numbers, expected, k+1, len(numbers)-1)
        if index < len(numbers) and numbers[index] == expected:
            return  k+1, index+1

print(twoSum([2,7,11,15],9))
