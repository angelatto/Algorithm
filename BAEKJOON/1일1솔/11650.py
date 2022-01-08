"""
01.08.22
실버5

처음에 숫자로 형변환 안해줘서 틀림
"""
import sys

N = int(sys.stdin.readline().strip())
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort(key=lambda ll : (ll[0], ll[1]))
for ll in li:
    print(ll[0], ll[1])
