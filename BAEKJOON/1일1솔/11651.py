"""
01.08.22
실버5

"""
import sys

N = int(sys.stdin.readline().strip())
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort(key=lambda ll : (ll[1], ll[0]))
for ll in li:
    print(ll[0], ll[1])
