"""
회의실배정
2022.02.08


11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""

n = int(input())
meets = [list(map(int, input().split())) for _ in range(n)]
meets.sort(key=lambda x:(x[1], x[0]))

answer = 0
last = 0
for start, end in meets:
    if start >= last:
        answer += 1
        last = end
print(answer)
