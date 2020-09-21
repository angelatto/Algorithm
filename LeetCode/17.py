def letterCombinations(digits):
    def dfs(index, path):
        # 종료 조건
        if len(path) == len(digits):
            result.append(path)
            return

        # 재귀 - 전체 탐색
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i+1, path+j)


    # main 시작
    if not digits: #예외 처리
        return []

    dic = { '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                    '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    result = []
    dfs(0, '')
    return result


print(letterCombinations("23"))
