import heapq
def solution(n, board):
    answer = 0
    li = [i for i in range(1, n*n+1)]

    # 좌/우/위/아래 방향 이동
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    i = j = count = 0
    while len(li) != 0: # 다 지울때까지 반복
        queue = [(0, i, j)] # 새로운 값을 찾기 시작할 때 count(커서이동횟수)는 항상 0으로 초기화

        while queue:
            count, i, j = queue.pop(0) # 현재 위치

            if board[i][j] == li[0]: # 현재위치와 찾는 값이 같으면
                li.remove(board[i][j])
                answer += 1 # 엔터키 누르는 비용
                answer += count # 커서 이동 횟수 - 최단거리
                print("-----------answer------------", answer)
                break
            else:  # 못찾으면
                count += 1
                for z in range(4):
                    x = i + dx[z]
                    y = j + dy[z]

                    if x < 0:  x = n-1
                    if y < 0:  y = n-1
                    if x >= n: x = 0
                    if y >= n: y = 0

                    heapq.heappush(queue, (count, x, y))

    return answer

# test case
print(solution(3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]]))
print(solution(2, [[2,3], [4,1]]))
print(solution(4, [[11,9,8,12], [2,15,4,14], [1,10,16,3], [13,7,5,6]]))
