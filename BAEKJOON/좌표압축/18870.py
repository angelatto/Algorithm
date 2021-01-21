"""
좌표 압축 (lev.silver-2)
"""

n = int(input())
coordinate = list(map(int, input().split()))
li = list(sorted(set(coordinate)))
# print(li)
# -10 -9 2 4  index

# dic = {}
# for i in range(len(li)):
#     dic[li[i]] = i
dic = {li[i]: i for i in range(len(li))}  # 딕셔너리를 한번에 정의
print(*[dic[c] for c in coordinate])  # 리스트를 한번에 출력
