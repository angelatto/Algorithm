def subsets(nums): # 부분집합 구하기
    result = []

    def dfs(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i+1, path + [nums[i]])

    # main
    dfs(0, [])

    return result
print(subsets([1,2,3]))
