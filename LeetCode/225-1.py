a = [1,2,3,4,5]
a.append(6)
print(a)
print(a.pop())
print(a.pop(0))
print(a)

from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)
print(q.popleft())
print(q)
q.append(5)
print(q)
