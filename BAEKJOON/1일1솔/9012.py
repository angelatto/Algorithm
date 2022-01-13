"""
01.13.22
실버4

"""
import sys

N = int(sys.stdin.readline())
for _ in range(N):
    str = sys.stdin.readline()
    stack = []

    for s in str:
        if s == '(':
            stack.append('(')
        elif s == ')' and not stack:
            stack.append(')')
            break
        elif s == ')' and stack:
            stack.pop()

    if stack:
        print('NO')
    else:
        print('YES')




