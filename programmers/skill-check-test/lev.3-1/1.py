import collections


def solution(n, computers):
    graph = collections.defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    # print(graph)

    visited = [False for _ in range(n)]
    answer = 0

    for i in range(n):
        queue = collections.deque()

        if not visited[i]:
            queue.appendleft(i)
            answer += 1

            while queue: # bfs : 하나의 연결된 그래프에 대해서만 탐색
                node = queue.pop()
                visited[node] = True

                for w in graph[node]:
                    if not visited[w]:
                        queue.appendleft(w)

    return answer


# __test case__
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1
print(solution(5, [[1,1,1,1,1], [1,1,0,0,0], [1,0,1,0,0], [1,0,0,1,0], [1,0,0,0,1]])) # 1
print(solution(4, [[1,1,0,0], [1,1,0,0], [0,0,1,1], [0,0,1,1]])) # 2