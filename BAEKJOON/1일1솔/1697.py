"""
01.11.22
실버1

수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때
    1. 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
    2. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때,
수빈이가 동생을 찾을 수 있는
    가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

이동할때마다 초가 늘어남

5 17
4
"""
from collections import deque

def bfs(start):
    queue = deque([start])
    global target

    while queue:
        n = queue.popleft()

        # 종료 조건
        if n == target:
            print('결과: ', graph[n])
            return

        if graph[n] != 0:
            print('방문: ', n)
            graph[n] += 1  # 방문표시

        if 0<n-1<max(start, target)+1 and graph[n-1] != 0:
            queue.append(n-1)
        if 0<n+1<max(start, target)+1 and graph[n+1] != 0:
            queue.append(n+1)
        if 0<n*2<max(start, target)+1 and graph[n*2] != 0:
            queue.append(n*2)


#  __main__
start, target = map(int, input().split())
# 방문시 +1로 변경 ??
graph = [0] * (max(start, target)+1)
# print(graph)

# start 정점에서 target 정점으로 도달하기까지 걸린 시간
bfs(start)
