
def solution(n, computers):
    visited = [False for i in range(n)]
    answer = 0

    def dfs(i):
        stack = [i]
        while stack:
            j = stack.pop()
            visited[j] = True

            for k in range(n):
                if computers[j][k] == 1 and not visited[k]:
                    stack.append(k)

    #---main---
    i = 0
    while False in visited:
        if not visited[i]: # 아직 방문안했으면
            dfs(i)
            answer += 1
        i += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1
print(solution(4, [[1, 1, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0],[0, 0, 0, 1]])) # 2
print(solution(4, [[1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 0], [0, 1, 0, 1]])) # 2
print(solution(8, [[1,1,1,1,1,0,0,0], [1,1,0,0,0,1,0,0], [1,0,1,0,0,0,0,0]
,[1,0,0,1,0,0,0,1], [1,0,0,0,1,0,1,0], [0,1,0,0,0,1,0,0], [0,0,0,0,1,0,1,0], [0,0,0,1,0,0,0,1]]))
print(solution(6, [[1,1,0,0,0,0], [1,1,1,0,0,0], [0,1,1,0,0,0], [0,0,0,1,1,0], [0,0,0,1,1,0], [0,0,0,0,0,1]]))
