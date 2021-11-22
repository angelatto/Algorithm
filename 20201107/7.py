def solution(n, horizontal):
    answer = [[0 for i in range(n)] for _ in range(n)]
    # 수직, 수평은 딱 1번씩만 이동 (1초)
    # 대각선은 경계에 도달할때까지 이동 증감추세 (2초를 여러번)

    flag = 1 # 현재 수직수평인지 대각선인지 판단
    for i in range(n):
        for j in range(n):
            if horizontal == True: # 오른쪽으로 시작
                answer[0][1] = answer[0][0] + 1





            else:
                answer[1][0] = answer[0][0] + 1

    return answer # 2차원 배열을 리턴

# test case
print(solution(4, True))
# print(solution(5, False))
