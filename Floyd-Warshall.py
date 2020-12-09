import sys

INF = sys.maxsize

def floyd(n, graph):

    for k in range(n):
        for i in range(n):
            # 최적화 - i에서 k로 가는 경로가 없다면 j에 대한 for문은 수행하지 않는다.
            if graph[i][k] != INF:
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph

# --main--
n = 4 # 정점 개수
graph = [[0,2,INF,4], [2,0,INF,5], [3,INF,0,INF], [INF,2,1,0]]
# 원래는 그래프도 직접 만들어줘야 하는데 간선이 없으면 INF,i==j이면 0으로 초기화해준다.

# 결과
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print('INF', end='')
        else:
            print(graph[i][j], end='')
    print()


# 인접 행렬 그래프에 최단 거리를 계산한다.
graph = floyd(n, graph)

# 결과
for i in range(n):
    for j in range(n):
        print(graph[i][j], end='')
    print()
