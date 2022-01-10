"""
01.11.22
실버5

N(1 ≤ N ≤ 1,000,000)
-> 시간 성능 주의
"""
from collections import deque


def merge_sort(array):
    # 재귀 종료조건 : 하나 남을때까지 분할
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = deque(merge_sort(array[:mid]))
    right = deque(merge_sort(array[mid:]))

    # 분할이 끝나고 합병
    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.popleft())
        else:
            merged.append(right.popleft())

    if len(left) > 0:
        merged += left
    if len(right) > 0:
        merged += right

    return merged


N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

# 정렬
array = merge_sort(array)

for num in array:
    print(num)