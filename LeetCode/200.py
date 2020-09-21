def numIslands(grid):
    def dfs(i, j):  # 동서남북체크
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return      #종료 조건

        grid[i][j] = '#'

        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)


    count = 0 # 섬의 개수
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count



print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
