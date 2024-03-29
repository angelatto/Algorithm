"""
01.06.22
실버4

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.


"""
import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
    li = sys.stdin.readline().split()
    cmd = li[0]
    if len(li) > 1:
        num = li[1]

    if cmd == 'push':
        q.append(num)
    elif cmd == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif cmd == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)