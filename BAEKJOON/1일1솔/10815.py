"""
01.11.22
실버4

in 연산자를 쓰면 O(N) 이기 때문에 매우 비효율적
-> 찾기할때 이분탐색 이용해서 성능문제해결 !!
"""
import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
M = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))
arr.sort()
print(arr)

# 이분탐색은 일단 정렬된 상태에서 하는 것
# 가운데 인덱스의 값이 찾는 값인지 비교하고, 아니면 찾는 범위 좁히기
# 결국 찾는 범위를 반토막씩 줄여나가는 알고리즘
def binary_search(num):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == num:
            # 찾았다
            return mid
        elif arr[mid] < num:
            start = mid+1
        else:
            end = mid-1

    # 끝까지 못찾으면 None 리턴
    return None


# main
for num in arr2:
    # num 이 arra에 있으면 1 출력
    if binary_search(num) != None:
        print(1, end=' ')
    # 없으면 0 출력
    else:
        print(0, end=' ')
