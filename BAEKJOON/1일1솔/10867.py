"""
01.08.22
실버5

10
1 4 2 3 1 4 2 3 1 2
"""
import sys

N = int(sys.stdin.readline().strip())
li = set(map(int, sys.stdin.readline().split()))
for ll in sorted(li):
    print(ll, end=' ')
