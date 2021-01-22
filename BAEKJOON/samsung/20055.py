"""
컨베이어 벨트 위의 로봇 (lev.silver-1)
- 시뮬레이션
- 포인트 : 연결리스트 이용 -> deque() 모듈 이용
         rotate() 함수를 이용하여 실제 요소를 바꾸지 않고도 인덱스 번호를 바꿀 수 있다.
- N 번째 위치에서 로봇이 내려가기 때문에 N+1 ~ 2N 까지는 로봇이 없다.
"""
from collections import deque


N, K = list(map(int, input().split()))
A = deque(map(int, input().split()))
robot = deque([0]*2*N)
result = 0  # 1단계

while True:
    if A.count(0) >= K:  # 종료조건
        break

    # 벨트가 한 칸 회전한다. - 이때 인덱스 위치만 변경됨.
    A.rotate(1)
    robot.rotate(1)
    robot[N - 1] = 0  # 내려가는 위치의 로봇은 삭제

    for i in range(N-2, -1, -1):  # N-2부터 0 까지 , 가장 먼저 올라간 로봇부터
        if robot[i+1] == 0 and robot[i] == 1 and A[i+1] >= 1:
            robot[i] = 0
            robot[i+1] = 1
            A[i+1] -= 1
    robot[N-1] = 0  # 내려가는 위치의 로봇은 삭제

    if robot[0] == 0 and A[0] >= 1:  # 올라가는 위치에 로봇 올리기
        robot[0] = 1
        A[0] -= 1

    result += 1

# 답 출력ß
print(result)