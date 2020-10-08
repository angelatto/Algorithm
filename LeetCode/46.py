# import itertools
# def permute(nums):
#     # return list(itertools.permutations(nums, len(nums)))
#     return list(map(list, itertools.permutations(nums, len(nums))))
# # 중복 없이, 순서 있음  -> 순열



#풀이 2 : DFS를 활용한 순열
def permute(nums):
    def dfs(elements):
        #종료 조건
        if len(elements) == 0:
            result.append(prev_elements[:])

        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    # main 시작
    result = []
    prev_elements = []

    dfs(nums)
    return result



print(permute([1,2,3]))
