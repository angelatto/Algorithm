"""
집합 (lev.silver-5)

- 집합으로 풀면 시간초과 -> in연산자 때문
- 배열로 true/ false로 인덱스를 값으로 생각하기
- pypy는 메모리 초과 -> python으로 해결

"""
import sys
input = sys.stdin.readline
n = int(input())

my_list = [False] * 20  # 0 ~ 19
for _ in range(n):
    c = input().split()
    if len(c) > 1:
        x = int(c[1]) - 1  # 1 ~ 20 -> 0 ~ 19
    if c[0] == 'add':
        my_list[x] = True
    elif c[0] == 'remove':
        my_list[x] = False
    elif c[0] == 'check':
        print(1 if my_list[x] else 0)
    elif c[0] == 'toggle':
        my_list[x] = not my_list[x]
    elif c[0] == 'all':
        my_list = [True] * 20
    elif c[0] == 'empty':
        my_list = [False] * 20