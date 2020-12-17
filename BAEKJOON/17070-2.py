import sys
import collections

input = sys.stdin.readline

# 입력
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

dd=[[(0,1), (1,1)],             # 가로
    [(1,0), (1,1)],             # 세로
    [(0,1), (1,0), (1,1)]]      # 대각선

def checkD(dx, dy):
   if dx: #dx가 1이면
       if dy: return 2   # 대각선
       else: return 1    # 세로
   else:
       return 0            # 가로

queue = collections.deque()
queue.append((0,1,0))   #x, y, d

answer = 0
memo = collections.defaultdict(list)

while queue:
    x, y, d = queue.popleft()
    print('x: ', x, ' y: ', y)

    if x == n-1 and y == n-1:
        answer += 1

    if (x, y, d) in memo:
        print('-----')
        for rr in memo[(x,y,d)]:
            queue.append(rr)
    else:
        for dx, dy in dd[d]:
           nx, ny, nd = x+dx, y+dy, checkD(dx, dy)
           if nx >= n or ny >= n or a[nx][ny]: continue
           if nd==2: # 대각선
               if a[x][ny] or a[nx][y]:
                   continue

           memo[(x, y, d)].append((nx, ny, nd))
           queue.append((nx, ny, nd))
print(answer)
