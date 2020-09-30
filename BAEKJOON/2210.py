import sys
# 5X5 크기의 2차원 배열을 입력 받는다. str이여야함 <--숫자0도 맨앞에 올수 있도록 해야함..
graph = [sys.stdin.readline().split() for _ in range(5)]
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
#print(graph)

def dfs(i, j, newstr): #길이가 6이될때까지 재귀로 구하기
    #종료조건
    newstr += graph[i][j]

    if len(newstr) == 6:
        setA.add(newstr)
        return newstr

    for idx in range(4):
        nx = i + dx[idx]
        ny = j + dy[idx]
        if 0<=nx<5 and  0<=ny<5:
            dfs(nx, ny, newstr)

#------------------------
dx = [0,0,-1,1]
dy = [-1,1,0,0]

setA = set()
for i in range(5):
    for j in range(5):
        newstr = ''
        dfs(i, j, newstr)# 모든 경우에 대하여 깊이 우선 탐색

#print("setA : " , setA)
# 구하는것
print(len(setA))
