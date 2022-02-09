"""
최소힙
22.02.09


9
0
12345678
1
2
0
0
0
0
32



"""
import heapq
import sys

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if li:
            print(heapq.heappop(li))
        else:
            print(0)
    else:
        heapq.heappush(li, num)



