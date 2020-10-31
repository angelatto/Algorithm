def solution(v):
    grid = v[:]
    answer = []
    def dfs(i, j, f):  # 동서남북체크
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or grid[i][j] != f:
            return      #종료 조건

        grid[i][j] = '#'

        dfs(i-1, j, f)
        dfs(i+1, j, f)
        dfs(i, j-1, f)
        dfs(i, j+1, f)

    # 3번 반복
    for food in range(3):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == food:
                    dfs(i, j, food)
                    count += 1
        answer.append(count)
        # 그리드 초기화
        grid = v[:]
    return answer


print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))
