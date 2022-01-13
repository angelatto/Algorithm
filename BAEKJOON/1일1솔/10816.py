"""
01.13.22
실버4


10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

"""


from collections import Counter

N = int(input())
arr = list(map(int, input().split()))
arr = Counter(arr)

M = int(input())
arr2 = list(map(int, input().split()))

for num in arr2:
    # num이 arr 안에 몇개 있는지 조사
    print(arr[num], end=' ')


