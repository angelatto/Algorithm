# 구름 IDE는 입력을 직접 받아야 함

def solution():
    size =  int(input()) # 배열 크기
    arr = list(map(int, input().split()))  # 정렬되서 들어옴
    target = int(input()) # 찾고자 하는 값

    left, right = 0, size -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid + 1

    return 'X'

print(solution())


# 기본 세팅

# def solution():
#     user_input = input()
#     return user_input
# print(solution())
