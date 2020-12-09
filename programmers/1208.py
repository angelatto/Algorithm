# Floyd-Warshall
import sys
INF = sys.maxsize

def printGraph(n, graph): # 그래프 출력
    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                print('#', end=' ')
            else:
                print(graph[i][j], end=' ')
        print()
    print('----------------')

def makeGraph(n, results):
    graph = [[INF for _ in range(n)] for _ in range(n)]

    for r in results:
        graph[r[0]-1][r[1]-1] = 1

    return graph

def floyd(n, graph):

    for k in range(n):
        for i in range(n):
            # 최적화 - i에서 k로 가는 경로가 없다면 j에 대한 for문은 수행하지 않는다.
            if graph[i][k] != INF:
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph

def solution(n, results):
    # 선수가 한 명일때
    if n == 1:
        return 1

    # 그래프 만들기 - 인접행렬로 만들기, 단방향 그래프
    graph = makeGraph(n, results)
    printGraph(n, graph)

    # 인접행렬 그래프에 최단 거리를 계산해서 업데이트 한다.
    graph = floyd(n, graph)
    printGraph(n, graph)

    # 행, 열에서 무한대가 아닌 값이 n-1개 이면 카운트
    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if graph[i][j] != INF or graph[j][i] != INF:
                count +=1
        if count == n-1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
