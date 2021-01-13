
import time
def solution(num):
    # 1에서 num 까지의 합을 분할과 정복으로 풀어보기
    list = [i for i in range(1, num+1)]
    def recursion(arr):
        if len(arr) == 1:
            return arr[0]

        half = len(arr) // 2
        result = recursion(arr[:half]) + recursion(arr[half:])
        return result

    return recursion(list)


# 실행 시간 측정
start = time.time()
print(solution(int(input())))
end = time.time()

# print('execute time: ', end - start) # 1.7066500186920166
