# 프렌즈4블록 - 게임 요구사항을 구현해보는 문제
# 난이도 - 상
# 비지니스 로직: 그래프를 탐색해서 2*2 형태의 블록을 찾아서 '#'로 바꾸고 다시 그래프 세팅

def solution(m, n, board):
    # 전처리: 그래프를 만든다 - 인접행렬
    graph = [list(x) for x in board]

    while True: # 더 이상 삭제할 후보들이 없을 때까지
        # 1. 삭제 후보 찾기 -> 여기서 바로 삭제하면 안됨. #으로 바꾸면 다음 행에서 못찾으니까.
        candidate = []
        for i in range(m-1):
            for j in range(n-1):
                if graph[i][j] == graph[i][j+1] == graph[i+1][j] == graph[i+1][j+1] != '#':
                        candidate.append([i, j])
        # 종료 조건
        if not candidate:
            break

        # 2. 삭제 후보들을 여기서 일괄적으로 삭제
        for i, j in candidate:
            graph[i][j] = graph[i][j+1] = graph[i+1][j] = graph[i+1][j+1] = '#'

        # 3. 삭제 된 공간 메꾸고, 다시 테이블 세팅 <- 여기가 까다로움!!!
        # 문제 설명하는 그림에서 보여주는 그대로 화살표를 쭉 밑으로 내린다고 생각 - swap
        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if graph[i+1][j] == '#':
                        graph[i+1][j], graph[i][j]  = graph[i][j], '#'
    print('graph: ', graph)

    # 마지막에 그래프에서 #개수를 카운트하면 정답이다.
    return sum(x.count('#') for x in graph)

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
