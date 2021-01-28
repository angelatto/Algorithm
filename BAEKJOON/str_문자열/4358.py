"""
생태학 (lev.gold-4)
- 입력받는 개수가 정해지지 않음
- 사전순 출력, 백분율(소수점 4째자리까지 반올림)

"""
import collections
import sys
input = sys.stdin.readline

li = []
while True:
    tree = input().rstrip()
    if not tree:
        break
    li.append(tree)

count = collections.Counter(li)
total = sum(count.values())
count = sorted(count.items(), key=lambda x : x[0])  # -> 리스트

for k, v in count:
    print('%s %.4f' % (k, v*100/total))