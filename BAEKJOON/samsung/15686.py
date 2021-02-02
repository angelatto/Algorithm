"""
치킨 배달 (lev.gold-5)
- 구현
- 도시 n * n -> 빈칸, 치킨집, 집 - 0, 2, 1
치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. (거리 구하는 방법 : |r1-r2| + |c1-c2| )
각각의 집 기준으로 치킨 거리를 가지며, 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

이 도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개 이다.
-> '도시의 치킨 거리' 최소값을 구하기 ( 조건 : 치킨집 최대 M개 )

"""
import sys
import itertools

# __main__
n, m = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
min_result = sys.maxsize

# 1. 전처리 - 치킨 위치와 집 위치 좌표 모두 저장하기
houses = [(i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]
chicken = [(i, j) for i in range(n) for j in range(n) if graph[i][j] == 2]
cnt = len(chicken)  # 치킨집 개수

# 선택한 치킨집이 많을 수록 도시의 치킨 거리가 최소라고 가정하기.
cases = list(itertools.combinations(chicken, m))
for case in cases:
    sumv = 0
    for hx, hy in houses:
        sumv += min([abs(hx-i) + abs(hy-j) for i, j in case])
    min_result = min(min_result, sumv)

# 답 출력
print(min_result)