"""
스타트와 링크 (lev.silver-3)

먼저 팀을 N/2 로 나누는 경우를 모두 구하고,
-> 각각의 case 에서 능력치 차이를 구해서 최종 최솟값을 구한다.

"""
import sys
import itertools
import collections

N = int(input())  # 항상 짝수
graph = [list(map(int, input().split())) for _ in range(N)]

dp = collections.defaultdict(int)

all_cases = list(itertools.combinations(range(N), N//2))
for case in all_cases:
    temp = 0
    for i in range(len(case)-1):
        for j in range(i+1, len(case)):
            temp += graph[case[i]][case[j]]
            temp += graph[case[j]][case[i]]
    dp[case] = temp

# dp.values() 에서 두 값의 차이가 최소인 값을 출력
result = sys.maxsize
count = 0
for key in dp:
    if count >= len(dp) // 2:
        break
    other = tuple(set(range(N)) - set(key))  # 차집합
    temp = abs(dp[key] - dp[other])
    result = min(result, temp)
    count += 1
print(result)