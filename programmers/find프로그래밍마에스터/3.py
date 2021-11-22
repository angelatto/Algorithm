# 나는 분할과 정복으로 풀어서 정확성은 통과하지만 효율성은 통과하지 못함
# divide and conquer && 중복된 하위 문제들
# -> 메모이제이션으로 최적화 or 타뷸레이션 -> 어쨋든 dp

# 다시 풀어보기 

import collections
def solution(arr):
    def compute(left, right, op):
        result = []
        for l in left:
            for r in right:
                result.append(eval(str(l) + op + str(r)))
        return result

    def recursion(arr):
        if len(arr) == 1:
            return [int(arr[0])]

        results = []
        for index, value in enumerate(arr):
            if value in '+-':
                left = recursion(arr[:index])
                right = recursion(arr[index+1:])

                results.extend(compute(left, right, value)) # 분할되고 다 쪼개지면 하는 일
        return results

    #__main__
    dic = collections.defaultdict()

    print(recursion(arr))
    return max(recursion(arr))

print(solution(['1','-','3','+','5','-','8']))
