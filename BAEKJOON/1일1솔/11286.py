"""
절댓값 힙
22.02.09

18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0

배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
"""
import heapq
import sys

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if li:
            print(heapq.heappop(li)[2])
        else:
            print(0)
    else:
        heapq.heappush(li, (abs(num), num, num))

