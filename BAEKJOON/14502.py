def countSafe(graph): #0의 개수를 카운트하는 함수
    count = 0
    for g in graph:
        count += g.count(0)
    return count

if __name__ == "__main__":
    row, col = map(int, input().strip().split())
    graph = [] #2차원배열은 1차원리스트에 요소를 리스트로 주면 된다.
    for i in range(row):
        graph.append(list(map(int, input().strip().split())))

    print(graph)
    print(countSafe(graph))

    # 1을 3개 추가하여 모든 경우의 수를 파악한다. -> 3개 고르는 것 (조합 이용)
    # 각각의 경우마다 2가 퍼질것을 고려하여 --->(그래프탐색) countSafe를 구한다.
    # 이전의 countSafe보다 큰 값이 나오면 값을 업데이트한다.
