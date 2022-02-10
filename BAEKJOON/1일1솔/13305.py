"""
주유소
22.02.10

4
2 3 1
5 2 4 1

"""
import sys

n = int(input())
dist = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

result = cost[0] * dist[0]
mincost = cost[0]
for i in range(1, n-1):
    if mincost > cost[i]:
        mincost = cost[i]
    result += mincost * dist[i]

print(result)