import collections
def canFinish(numCourses: int, prerequisites) -> bool:

    graph = collections.defaultdict(list)
    for x, y in prerequisites:
        graph[x].append(y)

    visited = set()

    # dfs 내장 함수
    def dfs(i): # 사이클 검사하기
        if i in visited: # 사이클이 발견 !!
            return False

        visited.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False

        visited.remove(i)
        return True


    # main
    for x in list(graph):
        if not dfs(x): # 사이클 발견되면 false
            return False
    return True

print(canFinish(2, [[1,0], [0, 1]]))
