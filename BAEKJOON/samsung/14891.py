"""
톱니바퀴 (lev.silver-1)
- 시뮬레이션
- A가 회전할 때, 서로 맞닿은 극이 다르다면, B가 A와 반대방향으로 회전한다.
- N극 0, S극 1
- 방향이 1 - 시계, -1 반시계
"""
import collections

gears = []
for _ in range(4):
    gears.append(collections.deque(input()))

K = int(input())
rotation = []
for _ in range(K):
    a, b = list(map(int, input().split()))
    rotation.append((a - 1, b))  # 톱니바퀴 번호와 방향 시계 1, 반시계 -1


def rotate_fun(candi):  # 톱니바퀴를 시계 또는 반시계로 회전한 결과 리턴
    for can in candi:
        if can[1] == 1:
            gears[can[0]].rotate(1)
        else:
            gears[can[0]].rotate(-1)


for num, dir in rotation:  # 회전
    candidate = [(num, dir)] # 초기화
    # 양 쪽으로 투포인터로 확장해서 회전해야할 톱니바퀴 다 알아내기
    left, standard = num-1, num
    n_dir = dir
    while left >= 0:
        if gears[standard][-2] == gears[left][2]:
            break
        candidate.append((left, n_dir * (-1)))
        standard = left
        left -= 1
        n_dir = n_dir * (-1)

    right, standard,  = num+1, num
    n_dir = dir
    while right < 4:
        if gears[standard][2] == gears[right][-2]:
            break
        candidate.append((right, n_dir * (-1)))
        standard = right
        right += 1
        n_dir = n_dir * (-1)

    # 회전할 대상과 방을 모두 알아내면 회전시키기 
    rotate_fun(candidate)

# 답 출력
result = 0
for i in range(4):
    if gears[i][0] == '1':  # S극
        result += 2 ** i
print(result)