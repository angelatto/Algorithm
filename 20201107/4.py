def solution(n, board):
    answer = 0

    def dfs(i, j, z, count): #현재 해당하는 값을 찾을 때까지 탐색한다. 그 중 최소값을 리턴
        if i < 0 or j < 0 or i >= n or j >= n:
            print(" 벗 어 났 다 ", i, j)
            return 55, 55, 55
        if board[i][j] == list_num[z]: # 종료 조건 -> 최소값 따져줘야함
            print(" 찾 았 다 ", list_num[z])
            return i, j, count

        # print("----", i, j, board[i][j], list_num[z])
        print("못 찾 았 다 ", list_num[z])
        # if i < 0:
        #     dfs(n-1, j, z, count+1)
        # if j < 0:
        #     dfs(i, n-1, z, count+1)
        # if i >= n:
        #     dfs(0, j, z, count+1)
        # if j >= n:
        #     dfs(i, 0, z, count+1)

        dfs(i+1, j, z, count+1)
        dfs(i, j+1, z, count+1)
        dfs(i-1, j, z, count+1)
        dfs(i, j-1, z, count+1)


    # 지워야 하는 숫자는 1 ~ n*n 임
    list_num = [i for i in range(1, n*n+1)]

    z = 0; i = 0; j = 0
    while len(list_num) != 0:
        if board[i][j] == list_num[z]: # 해당 숫자에 도달하면
            answer += 1 # 지우는 행위
            list_num.remove(list_num[z])
            z += 1 # 다음 숫자 찾기
        # 주변을 탐색 - 커서이동해서 해당 숫자를 찾을 때 까지 카운트해서 최적의 경로 찾기
        #  이프문에 걸리면 z가 플러스 1인 상태를 구하는거고 아니면 그 전 숫자를 구하는 것
        print(" 현재 위치, 현재 찾는 값 : ", i, j, z)
        count = 0
        i, j, count = dfs(i, j, z, count)
        print("찾고 나서 - 재귀 빠져 나옴 : ", i, j, count)
        answer += count # 이 카운트는 커서가 이동하는 최소값임
    return answer

print(solution(3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]]))
