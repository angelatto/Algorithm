"""
최대힙
22.02.09

13
0
1
2
0
0
3
2
1
0
0
0
0
0
"""
import heapq
import sys

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if li:
            print(heapq.heappop(li)[1])
        else:
            print(0)
    else:
        heapq.heappush(li, (-num, num))

