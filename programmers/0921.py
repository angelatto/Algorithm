# def solution(numbers, target):
#     answer = 0
#     # 1. +-로 이루어진 버킷에서  len(numbers)먄큼 뽑기 문제
#     # 중복순열 문제!!!
#     # 2. 계산해서 타겟이 나오면 count += 1
#     if not numbers and target == 0:
#         return 1  # 종료 조건이자 카운트 +1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0])\
#                 +\
#                solution(numbers[1:], target+numbers[0])


def solution(numbers, target):
    global answer
    answer = 0
    def dfs(index, value):
        global answer
        N = len(numbers)
        if(index== N and target == value):
            answer += 1
            return
        if(index == N):
            return

        dfs(index+1, value+numbers[index])
        dfs(index+1, value-numbers[index])


    dfs(0 ,0)
    return answer




print(solution([1, 1, 1, 1, 1], 3))
print(solution([], 0))
